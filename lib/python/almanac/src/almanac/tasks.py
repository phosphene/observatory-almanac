"""Brittani task board generator for the Observatory Almanac.

Scans the repository for content gaps, broken links in author profiles,
validation failures, and empty areas. Produces a structured markdown task
board at ``meta/brittani-tasks.md``.

Run via CLI: ``almanac tasks --root <root>``
"""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import date, timezone, datetime
from pathlib import Path

import yaml


def _collect_areas(root: Path) -> dict[str, dict]:
    """Return area metadata keyed by slug.

    Args:
        root: Almanac repository root.

    Returns:
        Mapping of area slug to metadata dict (display, description).
    """
    config_path = root / "meta" / "areas.yml"
    if not config_path.exists():
        return {}
    with config_path.open() as f:
        raw = yaml.safe_load(f)
    return raw.get("areas", {})


def _content_files(root: Path) -> list[Path]:
    """Return all content markdown files (excluding index.md).

    Args:
        root: Almanac repository root.

    Returns:
        Sorted list of content file paths.
    """
    files = []
    for f in (root / "areas").rglob("*.md"):
        if f.name != "index.md":
            files.append(f)
    for f in (root / "guides").rglob("*.md"):
        files.append(f)
    return sorted(files)


def _missing_linked_content(root: Path) -> dict[str, list[tuple[str, str]]]:
    """Find articles/guides linked from author profiles that don't exist yet.

    Args:
        root: Almanac repository root.

    Returns:
        Mapping of author display name to list of (title, target_path) tuples.
    """
    root_abs = root.resolve()
    existing = {f.resolve() for f in _content_files(root)}
    link_re = re.compile(r"\[(.*?)\]\((\.\./.*?\.md)\)")
    missing: dict[str, list[tuple[str, str]]] = {}

    for author_file in sorted((root / "authors").glob("*.md")):
        text = author_file.read_text()
        fm_name = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
        display_name = fm_name.group(1).strip() if fm_name else author_file.stem
        for match in link_re.finditer(text):
            title = match.group(1)
            rel = match.group(2)
            target_abs = (root / "authors" / rel).resolve()
            if target_abs not in existing:
                target_rel = str(target_abs.relative_to(root_abs))
                missing.setdefault(display_name, []).append((title, target_rel))

    return missing


def _empty_areas(root: Path, area_meta: dict[str, dict]) -> list[tuple[str, str]]:
    """Return area directories that contain no content files.

    Scans the filesystem directly so results always reflect actual state.
    Uses area_meta for display names when available; falls back to title-cased slug.

    Args:
        root: Almanac repository root.
        area_meta: Area metadata from areas.yml (may be empty if file absent).

    Returns:
        List of (slug, display_name) tuples for empty areas, sorted by slug.
    """
    areas_dir = root / "areas"
    if not areas_dir.exists():
        return []
    empty = []
    for area_dir in sorted(areas_dir.iterdir()):
        if not area_dir.is_dir():
            continue
        content = [f for f in area_dir.glob("*.md") if f.name != "index.md"]
        if not content:
            slug = area_dir.name
            display = area_meta.get(slug, {}).get(
                "display", slug.replace("-", " ").title()
            )
            empty.append((slug, display))
    return empty


def _validation_violations(root: Path) -> list[dict]:
    """Run the validator and collect any violations.

    Args:
        root: Almanac repository root.

    Returns:
        List of violation dicts with keys: path, field, message.
    """
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            f"from almanac.cli import main; import sys; "
            f"sys.exit(main(['validate', '--root', '{root}']))",
        ],
        capture_output=True,
        text=True,
    )
    violations = []
    current: dict = {}
    for line in result.stdout.splitlines():
        if line.startswith("- path:"):
            if current:
                violations.append(current)
            current = {"path": line.split(":", 1)[1].strip()}
        elif line.startswith("  field:") and current:
            current["field"] = line.split(":", 1)[1].strip()
        elif line.startswith("  message:") and current:
            current["message"] = line.split(":", 1)[1].strip()
    if current:
        violations.append(current)
    return violations


def generate_tasks(root: Path) -> str:
    """Generate the Brittani task board as a markdown string.

    Args:
        root: Almanac repository root.

    Returns:
        Markdown content for the task board.
    """
    today = date.today().isoformat()
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    area_meta = _collect_areas(root)
    missing = _missing_linked_content(root)
    empty = _empty_areas(root, area_meta)
    violations = _validation_violations(root)

    lines = [
        "---",
        "generated: " + now,
        "owner: feelingflowingbot",
        "for: brittani",
        "---",
        "",
        f"# Brittani — Content Task Board ({today})",
        "",
        "> Auto-generated from repository state. Regenerated nightly.",
        "> Fix items from the top: broken links block the live site.",
        "",
    ]

    # ── Section 1: Broken links ────────────────────────────────────────────
    total_missing = sum(len(v) for v in missing.values())
    lines += [
        f"## 🔴 Broken Links ({total_missing} item{'s' if total_missing != 1 else ''})",
        "",
        "Articles and guides referenced in author profiles but not yet in the repo.",
        "These are **live broken links** on the published site.",
        "",
    ]
    if missing:
        for author, items in sorted(missing.items()):
            lines.append(f"### {author}")
            lines.append("")
            for title, path in items:
                parts = path.split("/")
                area = parts[0] if len(parts) == 1 else parts[0] if parts[0] != "areas" else parts[1]
                lines.append(f"- [ ] **{title}**  ")
                lines.append(f"      `{path}` · type: `{area}`")
            lines.append("")
    else:
        lines += ["✅ No broken links found.", ""]

    # ── Section 2: Validation failures ────────────────────────────────────
    lines += [
        f"## 🟠 Validation Failures ({len(violations)} violation{'s' if len(violations) != 1 else ''})",
        "",
        "Content files that fail schema validation. Fix before next build.",
        "",
    ]
    if violations:
        by_file: dict[str, list[dict]] = {}
        for v in violations:
            by_file.setdefault(v.get("path", "unknown"), []).append(v)
        for path, vs in sorted(by_file.items()):
            lines.append(f"- [ ] `{path}`")
            for v in vs:
                lines.append(f"  - field `{v.get('field', '?')}`: {v.get('message', '')}")
        lines.append("")
    else:
        lines += ["✅ All content passes validation.", ""]

    # ── Section 3: Empty areas ─────────────────────────────────────────────
    lines += [
        f"## 🟡 Empty Areas ({len(empty)} area{'s' if len(empty) != 1 else ''})",
        "",
        "These areas exist in the almanac but have no articles yet.",
        "",
    ]
    if empty:
        for slug, display in empty:
            lines.append(f"- [ ] **{display}** (`{slug}`)")
        lines.append("")
    else:
        lines += ["✅ All areas have content.", ""]

    # ── Footer ─────────────────────────────────────────────────────────────
    total_tasks = total_missing + len(violations) + len(empty)
    lines += [
        "---",
        f"**Total open items:** {total_tasks}  ",
        "**Workflow:** fetch article from observatory.wiki → create file at listed path",
        "→ `almanac validate` → `almanac index` → commit",
    ]

    return "\n".join(lines)


def run_tasks(root: Path) -> int:
    """Generate and write the task board. Return exit code.

    Args:
        root: Almanac repository root.

    Returns:
        0 on success.
    """
    content = generate_tasks(root)
    out = root / "meta" / "brittani-tasks.md"
    out.write_text(content, encoding="utf-8")
    print(f"Task board written → {out}", file=sys.stderr)
    return 0
