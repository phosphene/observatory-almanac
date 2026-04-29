"""Content index generator for the Observatory Almanac.

Rebuilds ``meta/CONTEXT_INDEX.md`` and ``meta/index.md`` from the live
content tree.  Designed to run as a heartbeat task after bulk content
changes or as part of CI.

The generator is a pure function over the filesystem — it reads content
files, builds an in-memory inventory, and writes two output files.  It
does not modify content files.

Design note on Hot-Lookup indices
-----------------------------------
The index is a pre-computed hot-lookup map.  Agents read it once at
session start and filter by ``relevant_when`` tag — they never scan
the directory tree at runtime.  The generator is the only component
that performs tree traversal, and it runs offline (not on agent startup).
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from almanac.parsing import extract_meta

# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass
class ContentEntry:
    """A single indexed content document.

    Attributes:
        area: Canonical area slug.
        slug: Filename stem (stable identifier).
        title: Document title from frontmatter or first heading.
        doc_type: Document type string.
        author: Author display name (empty for non-articles).
        published: Publication date string.
        path: Relative path from almanac root.
    """

    area: str
    slug: str
    title: str
    doc_type: str
    author: str
    published: str
    path: str


@dataclass
class ContentInventory:
    """Full content inventory derived from the almanac tree.

    Attributes:
        articles: All content entries, grouped by area.
        total: Total document count.
        author_count: Number of distinct author profiles.
        guide_count: Number of guide documents.
        areas_covered: Set of area slugs with at least one document.
    """

    articles: dict[str, list[ContentEntry]] = field(
        default_factory=lambda: defaultdict(list)
    )
    total: int = 0
    author_count: int = 0
    guide_count: int = 0
    areas_covered: set[str] = field(default_factory=set)


# ---------------------------------------------------------------------------
# Logic layer (pure)
# ---------------------------------------------------------------------------


def build_inventory(root: Path) -> ContentInventory:
    """Build a full content inventory from the almanac tree.

    Args:
        root: Almanac repository root.

    Returns:
        Populated ``ContentInventory``.
    """
    inv = ContentInventory()

    areas_dir = root / "areas"
    if areas_dir.exists():
        for area_dir in sorted(areas_dir.iterdir()):
            if not area_dir.is_dir():
                continue
            area = area_dir.name
            for md_file in sorted(area_dir.glob("*.md")):
                title, meta = extract_meta(md_file)
                entry = ContentEntry(
                    area=area,
                    slug=md_file.stem,
                    title=title,
                    doc_type=str(meta.get("type", "almanac")),
                    author=str(meta.get("author", "")),
                    published=str(meta.get("published", "")),
                    path=str(md_file.relative_to(root)),
                )
                inv.articles[area].append(entry)
                inv.areas_covered.add(area)
                inv.total += 1

    authors_dir = root / "authors"
    if authors_dir.exists():
        inv.author_count = sum(1 for _ in authors_dir.glob("*.md"))

    guides_dir = root / "guides"
    if guides_dir.exists():
        inv.guide_count = sum(1 for _ in guides_dir.glob("*.md"))

    return inv


def render_content_index(inv: ContentInventory, today: str) -> str:
    """Render the ``meta/index.md`` content inventory.

    Args:
        inv: Populated content inventory.
        today: ISO 8601 date string for the update timestamp.

    Returns:
        Full markdown document string.
    """
    lines = [
        f"---\ntitle: Observatory Almanac Index\nupdated: {today}\n---\n",
        "# Observatory Almanac — Content Index\n",
        f"*Generated: {today} — {inv.total} documents across {len(inv.areas_covered)} areas, "
        f"{inv.author_count} authors, {inv.guide_count} guides.*\n",
    ]

    for area in sorted(inv.articles):
        entries = inv.articles[area]
        lines.append(f"\n## {area.replace('-', ' ').title()} ({len(entries)})\n")
        lines.append("| Slug | Title | Type | Author |")
        lines.append("|------|-------|------|--------|")
        for e in entries:
            link = f"[{e.slug}](../{e.path})"
            lines.append(
                f"| {link} | {e.title[:60]} | {e.doc_type} | {e.author or '—'} |"
            )

    if inv.guide_count:
        lines.append(f"\n## Guides ({inv.guide_count})\n")
        lines.append("*See guides/ directory.*")

    return "\n".join(lines) + "\n"


def render_context_index_update(
    inv: ContentInventory, today: str, existing: str
) -> str:
    """Update the ``updated:`` and content state table in CONTEXT_INDEX.md.

    This is a targeted update — it only replaces the ``updated:`` date in the
    YAML frontmatter and the content state table, leaving all other content
    intact.

    Args:
        inv: Current content inventory.
        today: ISO 8601 date string.
        existing: Current content of CONTEXT_INDEX.md.

    Returns:
        Updated CONTEXT_INDEX.md content.
    """
    # Update updated: date in frontmatter
    updated = re.sub(r"^(updated:\s*)[\d-]+", rf"\g<1>{today}", existing, flags=re.M)

    # Rebuild the content state table
    table_lines = ["| Area | Article Count |", "|------|--------------|"]
    for area in sorted(inv.articles):
        count = len(inv.articles[area])
        table_lines.append(f"| {area} | {count} |")
    table_lines.append(
        f"\nTotal: ~{inv.total} articles, {inv.author_count} authors, {inv.guide_count} guides"
    )
    new_table = "\n".join(table_lines)

    # Replace the existing table (between ## Current Content State and the next ##)
    updated = re.sub(
        r"(## Current Content State\n\n\*Updated:.*?\*\n\n).*?(?=\n## |\Z)",
        rf"\g<1>{new_table}\n",
        updated,
        flags=re.S,
    )
    # Update the inline timestamp
    updated = re.sub(
        r"\(\*Updated:.*?\*\)",
        f"(*Updated: {today}*)",
        updated,
    )

    return updated


# ---------------------------------------------------------------------------
# I/O layer
# ---------------------------------------------------------------------------


def run(root: Path, dry_run: bool = False) -> int:
    """Generate content index files.

    Args:
        root: Almanac repository root.
        dry_run: If True, print to stderr without writing.

    Returns:
        Exit code: 0 for success, 1 for error.
    """
    if not (root / "SCHEMA.md").exists():
        print(f"SCHEMA.md not found at {root}.", file=sys.stderr)
        return 1

    today = date.today().isoformat()
    inv = build_inventory(root)

    print(
        f"Indexed: {inv.total} docs, {inv.author_count} authors, "
        f"{inv.guide_count} guides, {len(inv.areas_covered)} areas",
        file=sys.stderr,
    )

    meta_dir = root / "meta"
    meta_dir.mkdir(exist_ok=True)

    # meta/index.md — full content inventory
    index_content = render_content_index(inv, today)
    if dry_run:
        print("--- meta/index.md ---", file=sys.stderr)
        print(index_content[:500], file=sys.stderr)
    else:
        (meta_dir / "index.md").write_text(index_content, encoding="utf-8")
        print("  Written: meta/index.md", file=sys.stderr)

    # meta/CONTEXT_INDEX.md — targeted update
    ctx_path = meta_dir / "CONTEXT_INDEX.md"
    if ctx_path.exists():
        existing = ctx_path.read_text(encoding="utf-8")
        updated = render_context_index_update(inv, today, existing)
        if dry_run:
            print("--- meta/CONTEXT_INDEX.md (updated) ---", file=sys.stderr)
        else:
            ctx_path.write_text(updated, encoding="utf-8")
            print("  Updated: meta/CONTEXT_INDEX.md", file=sys.stderr)

    return 0


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for the index generator.

    Args:
        argv: Argument list (defaults to sys.argv).

    Returns:
        Exit code.
    """
    import argparse

    p = argparse.ArgumentParser(
        description="Generate Observatory Almanac content index"
    )
    p.add_argument("--root", type=Path, default=Path("."), help="Almanac root")
    p.add_argument("--dry-run", action="store_true", help="Print without writing")
    args = p.parse_args(argv)
    return run(args.root.resolve(), dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
