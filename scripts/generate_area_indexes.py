"""Generate area index pages for MkDocs navigation.

Creates ``areas/<area>/index.md`` for each area in the almanac, listing
all documents with type badges and author attribution.  Run this after
any bulk content change.

Usage::

    python scripts/generate_area_indexes.py
    python scripts/generate_area_indexes.py --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from ruamel.yaml import YAML
    _yaml = YAML()
except ImportError:
    _yaml = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parent.parent
TODAY = __import__("datetime").date.today().isoformat()

AREA_DESCRIPTIONS: dict[str, str] = {
    "science": "Biology, consciousness, archaeology, paleoanthropology, and the natural sciences.",
    "environment": "Climate change, biodiversity, field guides, oceans, and ecosystems.",
    "history": "Ancient civilizations, deep time, archaeological discovery, and calendars.",
    "economy": "Wealth inequality, labor, debt, political economy, and local alternatives.",
    "animals": "Animal cognition, welfare, ecology, and human–animal relationships.",
    "philosophy": "Divination systems, folk wisdom, oracles, and perennial philosophy.",
    "psychology": "Behavioral biology, self-knowledge assessments, and relational science.",
    "health": "Emergency response, movement practices, meditation, and life navigation.",
    "cooking": "World cuisines, wine and cheese guides, and sensory education.",
    "arts-recreation": "Game rulebooks, music theory, film canon, and performance arts.",
    "world-affairs": "Country factbooks, cultural etiquette, and global travel.",
    "technology": "Digital life, home networking, device setup, and practical tech.",
    "language": "Sign language, survival phrases, and untranslatable idioms.",
    "local-peace-economy": "Legal forms, civic documents, Robert's Rules, and grassroots tools.",
    "human-bridges": "Death literacy, social movements, and cross-cultural connection.",
    "dig-labs": "Deep investigative pieces on contested and underexplored topics.",
    "education": "Learning theory, charter schools, and pedagogical practice.",
    "media": "Media literacy, journalism, and the information ecosystem.",
    "peoples-movements": "Grassroots organizing, civil rights, and collective action.",
    "agriculture": "Sustainable farming, soil science, and food systems.",
    "food": "Food policy, nutrition science, and cultural food studies.",
    "natural-health": "Herbal medicine, integrative health, and wellness practices.",
    "literature": "Classic texts, literary criticism, and reading culture.",
    "voting-elections": "Electoral systems, voting rights, and democratic participation.",
    "charter-schools": "Charter school policy, research, and alternatives.",
    "energy": "Renewable energy, fossil fuels, and energy policy.",
}

TYPE_ICONS: dict[str, str] = {
    "article": "📰",
    "almanac": "📖",
    "recipe": "🍳",
    "rulebook": "♟️",
    "factbook": "🌍",
    "reference": "📋",
    "assessment": "🔍",
    "field-guide": "🌿",
    "guide": "🗺️",
    "classic": "⭐",
}


def read_frontmatter(path: Path) -> dict:
    """Extract frontmatter dict from a markdown file.

    Args:
        path: Path to the markdown file.

    Returns:
        Frontmatter as a dict, or empty dict on failure.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end < 0:
        return {}
    yaml_text = text[3:end].strip()
    if _yaml is None:
        return {}
    try:
        data = _yaml.load(yaml_text)
        return dict(data) if isinstance(data, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


def build_area_index(area_dir: Path, area: str) -> str:
    """Build the index.md content for an area.

    Args:
        area_dir: Path to the area directory.
        area: Area slug.

    Returns:
        Full markdown content for the area index page.
    """
    description = AREA_DESCRIPTIONS.get(area, f"Content in the {area.replace('-', ' ').title()} area.")
    display_name = area.replace("-", " ").title()

    files = sorted(
        f for f in area_dir.glob("*.md") if f.name != "index.md"
    )

    # Group by type
    by_type: dict[str, list[tuple[Path, dict]]] = {}
    for f in files:
        meta = read_frontmatter(f)
        doc_type = str(meta.get("type", "almanac"))
        by_type.setdefault(doc_type, []).append((f, meta))

    lines = [
        f"---\ntitle: {display_name}\narea: {area}\nhide:\n  - toc\n---\n",
        f"# {display_name}\n",
        f"{description}\n",
        f"*{len(files)} documents*\n",
    ]

    for doc_type in sorted(by_type):
        entries = by_type[doc_type]
        icon = TYPE_ICONS.get(doc_type, "📄")
        lines.append(f"\n## {icon} {doc_type.replace('-', ' ').title()} ({len(entries)})\n")
        for path, meta in entries:
            title = str(meta.get("title", path.stem.replace("-", " ").title())).strip('"\'')
            author = str(meta.get("author", ""))
            author_part = f" · *{author}*" if author and author != "The Observatory" else ""
            lines.append(f"- [{title}]({path.name}){author_part}")

    return "\n".join(lines) + "\n"


def run(root: Path, dry_run: bool = False) -> None:
    """Generate index pages for all areas.

    Args:
        root: Almanac root directory.
        dry_run: If True, print without writing.
    """
    areas_dir = root / "areas"
    if not areas_dir.exists():
        print("No areas/ directory found.", file=sys.stderr)
        return

    count = 0
    for area_dir in sorted(areas_dir.iterdir()):
        if not area_dir.is_dir():
            continue
        content = build_area_index(area_dir, area_dir.name)
        index_path = area_dir / "index.md"
        if dry_run:
            print(f"  DRY  {index_path.relative_to(root)}")
        else:
            index_path.write_text(content, encoding="utf-8")
            print(f"  OK   {index_path.relative_to(root)}")
        count += 1

    print(f"\nGenerated {count} area index pages.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate area index pages")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--root", type=Path, default=ROOT)
    args = p.parse_args()
    run(args.root, dry_run=args.dry_run)
