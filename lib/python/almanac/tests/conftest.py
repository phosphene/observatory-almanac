"""Shared pytest fixtures for the almanac test suite."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture()
def article_data() -> dict:
    """Return a valid ArticleFrontmatter dict for testing."""
    return {
        "title": "Why Scientists Are Still Puzzled by Consciousness",
        "area": "science",
        "type": "article",
        "author": "Leslie Alan Horvitz",
        "author_slug": "leslie-alan-horvitz",
        "source": "The Observatory",
        "source_url": "https://observatory.wiki/Why_Scientists_Are_Still_Puzzled",
        "license": "CC BY-NC-SA 4.0",
        "published": "2026-02-06",
        "updated": "2026-02-06",
        "summary": "An expert survey of why consciousness remains one of the hardest problems in science.",
        "tags": ["consciousness", "neuroscience", "philosophy-of-mind"],
    }


@pytest.fixture()
def almanac_doc_data() -> dict:
    """Return a valid AlmanacDocFrontmatter dict for testing."""
    return {
        "title": "Chess",
        "area": "arts-recreation",
        "type": "rulebook",
        "source": "Observatory Almanac",
        "source_path": "docs/02-universal-rulebook/chess.md",
        "license": "MIT",
        "updated": "2026-04-28",
        "summary": "Complete rules and strategy guide for chess, from basic moves to endgame technique.",
        "tags": ["games", "strategy", "play"],
    }


@pytest.fixture()
def author_data() -> dict:
    """Return a valid AuthorFrontmatter dict for testing."""
    return {
        "name": "Leslie Alan Horvitz",
        "slug": "leslie-alan-horvitz",
        "source_url": "https://observatory.wiki/Leslie_Alan_Horvitz",
    }


@pytest.fixture()
def almanac_root(tmp_path: Path) -> Path:
    """Create a minimal almanac tree in a temp directory.

    Returns:
        Path to the root of the mock almanac.
    """
    root = tmp_path / "almanac"
    root.mkdir()
    (root / "SCHEMA.md").write_text("# Schema placeholder")
    (root / "AREAS.md").write_text("# Areas placeholder")
    (root / "areas" / "science").mkdir(parents=True)
    (root / "authors").mkdir()
    (root / "guides").mkdir()
    (root / "meta").mkdir()
    return root


@pytest.fixture()
def valid_article_file(almanac_root: Path, article_data: dict) -> Path:
    """Write a valid article file and return its path."""
    import yaml

    fm = yaml.dump(article_data, allow_unicode=True)
    content = f"---\n{fm}---\n\n# Article Title\n\nBody text here.\n"
    path = almanac_root / "areas" / "science" / "test-article.md"
    path.write_text(content)
    return path
