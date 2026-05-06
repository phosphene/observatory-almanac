"""Area index page generation logic for the Observatory Almanac.

Creates ``areas/<area>/index.md`` for each area, grouping documents
by type and providing author attribution.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from almanac.io import write_text
from almanac.parsing import split_frontmatter
from almanac.rendering import (
    load_area_metadata,
    load_type_icons,
    render_area_index,
)


def build_area_data(area_dir: Path) -> dict[str, list[dict[str, Any]]]:
    """Group documents in an area by their type.

    Args:
        area_dir: Path to the area directory.

    Returns:
        Dictionary mapping doc_type to a list of entry dicts.
    """
    by_type: dict[str, list[dict[str, Any]]] = {}
    for md in sorted(area_dir.glob("*.md")):
        if md.name == "index.md":
            continue

        try:
            text = md.read_text(encoding="utf-8")
            meta, _ = split_frontmatter(text)
        except (OSError, ValueError):
            meta = {}

        doc_type = str(meta.get("type", "almanac"))
        entry = {
            "filename": md.name,
            "title": str(meta.get("title", md.stem.replace("-", " ").title())).strip(
                "\"'"
            ),
            "author": str(meta.get("author", "")),
        }
        by_type.setdefault(doc_type, []).append(entry)

    return by_type


def run(root: Path, dry_run: bool = False) -> None:
    """Generate index pages for all areas in the almanac.

    Args:
        root: Almanac repository root.
        dry_run: If True, print status without writing files.
    """
    areas_dir = root / "areas"
    if not areas_dir.exists():
        return

    config_path = root / "meta" / "areas.yml"
    area_meta = load_area_metadata(config_path)
    type_icons = load_type_icons(config_path)

    for area_dir in sorted(areas_dir.iterdir()):
        if not area_dir.is_dir():
            continue

        area = area_dir.name
        meta = area_meta.get(area, {})
        display_name = meta.get("display", area.replace("-", " ").title())
        description = meta.get(
            "description", f"Content in the {display_name} area."
        )

        subareas = meta.get("subareas") or []
        entries_by_type = build_area_data(area_dir)
        content = render_area_index(
            area=area,
            display_name=display_name,
            description=description,
            entries_by_type=entries_by_type,
            type_icons=type_icons,
            subareas=subareas,
        )

        out_path = area_dir / "index.md"
        if dry_run:
            print(f"  DRY  {out_path.relative_to(root)}")
        else:
            write_text(out_path, content)
            print(f"  OK   {out_path.relative_to(root)}")
