"""Unit tests for the Almanac IO and Rendering modules.

Verifies isolated filesystem operations and pure string-building logic.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from almanac.io import collect_content_files, find_root
from almanac.rendering import (
    render_area_index,
    render_pages_file,
)


def test_collect_content_files(almanac_root: Path):
    """Verify that only markdown files from relevant directories are collected."""
    # Add a file in areas
    (almanac_root / "areas" / "science" / "physics.md").write_text("# Physics")
    # Add a file in guides
    (almanac_root / "guides" / "ai-guide.md").write_text("# AI")
    # Add a file in authors
    (almanac_root / "authors" / "ed-phil.md").write_text("# Ed Phil")
    # Add a file in meta (should be ignored)
    (almanac_root / "meta" / "ignore.md").write_text("# Ignore")

    files = collect_content_files(almanac_root)
    names = {f.name for f in files}

    assert "physics.md" in names
    assert "ai-guide.md" in names
    assert "ed-phil.md" in names
    assert "ignore.md" not in names


def test_find_root(almanac_root: Path):
    """Verify that find_root locates the repo root by sentinel files."""
    start = almanac_root / "areas" / "science"
    start.mkdir(parents=True, exist_ok=True)

    root = find_root(start)
    assert root == almanac_root


def test_render_area_index():
    """Verify area index generation with grouped documents."""
    entries_by_type = {
        "article": [{"title": "Consciousness", "filename": "consciousness.md", "author": "Leslie"}]
    }
    type_icons = {"article": "📰"}

    content = render_area_index(
        area="science",
        display_name="Science",
        description="The study of nature.",
        entries_by_type=entries_by_type,
        type_icons=type_icons,
    )

    assert "title: Science" in content
    assert "# Science" in content
    assert "The study of nature." in content
    assert "📰 Article (1)" in content
    assert "- [Consciousness](consciousness.md) · *Leslie*" in content


def test_render_pages_file():
    """Verify .pages file rendering."""
    content = render_pages_file("Science")
    assert "title: Science" in content
    assert "nav:" in content
    assert "index.md" in content
