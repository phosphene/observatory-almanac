"""MkDocs docs_dir tree management for the Observatory Almanac.

Synchronizes the ``docs/`` directory with the authoritative content in
``areas/`` and ``authors/`` using symlinks and .pages files.
"""

from __future__ import annotations

from pathlib import Path

from almanac.io import create_symlink, write_text
from almanac.rendering import load_area_metadata, render_pages_file


def build_docs_tree(root: Path) -> None:
    """Build the ``docs/areas/`` symlink tree and per-area ``.pages`` files.

    Args:
        root: Almanac repository root.
    """
    areas_src = root / "areas"
    if not areas_src.exists():
        raise FileNotFoundError(f"areas/ directory not found under {root}")

    docs_areas = root / "docs" / "areas"
    docs_areas.mkdir(parents=True, exist_ok=True)

    config_path = root / "meta" / "areas.yml"
    area_meta = load_area_metadata(config_path)

    total_links = 0
    for area_dir in sorted(areas_src.iterdir()):
        if not area_dir.is_dir():
            continue

        area = area_dir.name
        out_dir = docs_areas / area
        out_dir.mkdir(exist_ok=True)

        # Symlink all markdown files in the area
        for md in sorted(area_dir.glob("*.md")):
            create_symlink(md, out_dir / md.name)
            total_links += 1

        # Write .pages file for navigation title
        display = area_meta.get(area, {}).get("display", area.replace("-", " ").title())
        write_text(out_dir / ".pages", render_pages_file(display))

    # Symlink top-level reference docs into docs/
    for name in ("SCHEMA.md", "AREAS.md"):
        src = root / name
        if src.exists():
            create_symlink(src, root / "docs" / name)

    # Symlink guides/ directory
    if (root / "guides").exists():
        create_symlink(root / "guides", root / "docs" / "guides")

    # Symlink authors/ directory
    if (root / "authors").exists():
        create_symlink(root / "authors", root / "docs" / "authors")

    # Symlink team/ directory (design doc, status, planning)
    if (root / "team").exists():
        create_symlink(root / "team", root / "docs" / "team")

    # Ensure tags placeholder exists
    tags_md = root / "docs" / "tags.md"
    if not tags_md.exists():
        write_text(
            tags_md,
            "---\nhide:\n  - toc\n---\n\n# Tags\n\n*Auto-generated.*\n",
        )

    print(f"docs/ tree built — {total_links} new symlinks")
