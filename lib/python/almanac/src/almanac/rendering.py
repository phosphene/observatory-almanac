"""Pure Markdown rendering logic for the Observatory Almanac.

Provides functions for building area indices, context indices, and
navigation files. This module is I/O-free: it takes data and returns
strings.
"""

from __future__ import annotations

from typing import Any

from ruamel.yaml import YAML

_yaml = YAML(typ="safe")


def load_area_metadata(config_path: Path) -> dict[str, Any]:
    """Load area metadata from a YAML configuration file.

    Args:
        config_path: Path to areas.yml.

    Returns:
        Dictionary mapping area slugs to metadata.
    """
    if not config_path.exists():
        return {}
    data = _yaml.load(config_path.read_text(encoding="utf-8"))
    return data.get("areas", {}) if isinstance(data, dict) else {}


def load_type_icons(config_path: Path) -> dict[str, str]:
    """Load document type icons from a YAML configuration file.

    Args:
        config_path: Path to areas.yml.

    Returns:
        Dictionary mapping document types to emoji icons.
    """
    if not config_path.exists():
        return {}
    data = _yaml.load(config_path.read_text(encoding="utf-8"))
    return data.get("type_icons", {}) if isinstance(data, dict) else {}


def render_area_index(
    area: str,
    display_name: str,
    description: str,
    entries_by_type: dict[str, list[dict[str, Any]]],
    type_icons: dict[str, str],
) -> str:
    """Render the index.md content for an area.

    Args:
        area: Area slug.
        display_name: Human-readable area name.
        description: Area description.
        entries_by_type: Map of document type to list of entry dicts.
        type_icons: Map of document type to emoji icons.

    Returns:
        Markdown-formatted string.
    """
    total_docs = sum(len(v) for v in entries_by_type.values())
    lines = [
        f"---\ntitle: {display_name}\narea: {area}\nhide:\n  - toc\n---\n",
        f"# {display_name}\n",
        f"{description}\n",
        f"*{total_docs} documents*\n",
    ]

    for doc_type in sorted(entries_by_type):
        entries = entries_by_type[doc_type]
        icon = type_icons.get(doc_type, "📄")
        lines.append(
            f"\n## {icon} {doc_type.replace('-', ' ').title()} ({len(entries)})\n"
        )
        for e in entries:
            title = e["title"]
            author = e.get("author", "")
            author_part = (
                f" · *{author}*" if author and author != "The Observatory" else ""
            )
            lines.append(f"- [{title}]({e['filename']}){author_part}")

    return "\n".join(lines) + "\n"


def render_pages_file(title: str) -> str:
    """Render a .pages file for mkdocs-awesome-pages-plugin.

    Args:
        title: Section title.

    Returns:
        YAML-formatted string for the .pages file.
    """
    return f"title: {title}\nnav:\n  - index.md\n  - ...\n"
