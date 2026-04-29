"""Build the MkDocs ``docs/`` symlink tree for the Observatory Almanac.

MkDocs requires all source files to live under ``docs_dir`` (``docs/``).
The authoritative content lives in ``areas/`` and ``authors/`` at the
repo root.  This script creates ``docs/areas/<area>/`` directories with
symlinks pointing back to the real content files, so MkDocs can find them
without duplicating or moving the originals.

It also writes per-area ``.pages`` files for ``mkdocs-awesome-pages-plugin``
which control section titles and nav ordering.

Idempotent
----------
Re-running the script is safe.  Existing symlinks are left in place;
new content files that appeared since the last run get new symlinks;
``.pages`` files are always rewritten to pick up any display-name changes.

Usage::

    python scripts/build_docs_tree.py          # from almanac repo root
    python scripts/build_docs_tree.py --root . # explicit root

The script is called by the GitHub Actions deploy workflow before
``mkdocs build`` so that the ``docs/`` tree always reflects the current
``areas/`` state.
"""

from __future__ import annotations

import argparse
from pathlib import Path

AREA_DISPLAY: dict[str, str] = {
    "agriculture": "Agriculture",
    "animals": "Animals",
    "arts-recreation": "Arts & Recreation",
    "charter-schools": "Charter Schools",
    "cooking": "Cooking",
    "dig-labs": "Dig Labs",
    "economy": "Economy",
    "education": "Education",
    "energy": "Energy",
    "environment": "Environment",
    "food": "Food",
    "health": "Health",
    "history": "History",
    "human-bridges": "Human Bridges",
    "language": "Language",
    "literature": "Literature",
    "local-peace-economy": "Local Peace Economy",
    "media": "Media",
    "natural-health": "Natural Health",
    "peoples-movements": "People's Movements",
    "philosophy": "Philosophy",
    "psychology": "Psychology",
    "science": "Science",
    "technology": "Technology",
    "voting-elections": "Voting & Elections",
    "world-affairs": "World Affairs",
}


def build_docs_tree(root: Path) -> None:
    """Build ``docs/areas/`` symlink tree and per-area ``.pages`` files.

    Args:
        root: Almanac repository root (contains ``areas/`` and ``docs/``).

    Raises:
        FileNotFoundError: If ``areas/`` does not exist under ``root``.
    """
    areas_src = root / "areas"
    if not areas_src.exists():
        raise FileNotFoundError(f"areas/ directory not found under {root}")

    docs_areas = root / "docs" / "areas"
    docs_areas.mkdir(parents=True, exist_ok=True)

    total_links = 0
    for area_dir in sorted(areas_src.iterdir()):
        if not area_dir.is_dir():
            continue

        area = area_dir.name
        out_dir = docs_areas / area
        out_dir.mkdir(exist_ok=True)

        for md in sorted(area_dir.glob("*.md")):
            link = out_dir / md.name
            if link.is_symlink() or link.exists():
                link.unlink()
            link.symlink_to(md.resolve())
            total_links += 1

        display = AREA_DISPLAY.get(area, area.replace("-", " ").title())
        (out_dir / ".pages").write_text(
            f"title: {display}\nnav:\n  - index.md\n  - ...\n",
            encoding="utf-8",
        )

    # Symlink top-level reference docs into docs/ if not present
    for name in ("SCHEMA.md", "AREAS.md"):
        link = root / "docs" / name
        src = root / name
        if src.exists() and not link.exists():
            link.symlink_to(src.resolve())

    # Symlink authors/ directory
    authors_link = root / "docs" / "authors"
    if not authors_link.exists() and (root / "authors").exists():
        authors_link.symlink_to((root / "authors").resolve())

    # Ensure tags placeholder exists
    tags_md = root / "docs" / "tags.md"
    if not tags_md.exists():
        tags_md.write_text(
            "---\nhide:\n  - toc\n---\n\n# Tags\n\n*Auto-generated.*\n",
            encoding="utf-8",
        )

    print(f"docs/ tree built — {total_links} new symlinks")


def _find_root() -> Path:
    """Locate the almanac repo root by walking up from this script.

    Returns:
        Repository root containing ``areas/`` and ``docs/``.

    Raises:
        RuntimeError: If the root cannot be located.
    """
    here = Path(__file__).resolve().parent
    for candidate in [here.parent, here, *here.parents]:
        if (candidate / "areas").exists() and (candidate / "docs").exists():
            return candidate
    raise RuntimeError(
        "Could not locate almanac root (expected 'areas/' and 'docs/' siblings). "
        "Run from the repo root or pass --root."
    )


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=None,
        help="Almanac repo root (default: auto-detected)",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else _find_root()
    build_docs_tree(root)


if __name__ == "__main__":
    main()
