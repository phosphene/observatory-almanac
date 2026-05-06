"""Tests for the Agriculture area — slug recognition, article validation, and index exclusion.

Covers:
- `agriculture` is a canonical area slug in VALID_AREAS
- A valid article filed under `agriculture` passes validation
- An almanac-native document filed under `agriculture` passes validation
- The agriculture area index.md nav page is excluded from content validation
- An article under `agriculture` with missing required fields is rejected
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from almanac.constants import VALID_AREAS
from almanac.validator import run_validation, validate_document


def _write_agriculture_article(
    root: Path,
    slug: str,
    overrides: dict | None = None,
) -> Path:
    """Write a valid agriculture article and return its path.

    Args:
        root: Almanac root directory.
        slug: File slug (no .md extension).
        overrides: Optional frontmatter field overrides.

    Returns:
        Path to the written file.
    """
    area_dir = root / "areas" / "agriculture"
    area_dir.mkdir(parents=True, exist_ok=True)
    data: dict = {
        "title": "Regenerative Farming and Soil Health",
        "area": "agriculture",
        "type": "article",
        "author": "Test Author",
        "author_slug": "the-observatory",
        "source": "The Observatory",
        "source_url": "https://observatory.wiki/Regenerative_Farming",
        "license": "CC BY-NC-SA 4.0",
        "published": "2026-01-01",
        "updated": "2026-01-01",
        "summary": "How regenerative practices restore soil carbon and biodiversity.",
        "tags": ["agriculture", "soil", "regenerative-farming"],
    }
    if overrides:
        data.update(overrides)
    fm = yaml.dump(data, allow_unicode=True)
    path = area_dir / f"{slug}.md"
    path.write_text(f"---\n{fm}---\n\nBody content.\n")
    return path


def _write_agriculture_index(root: Path) -> Path:
    """Write the agriculture area nav index page and return its path.

    Args:
        root: Almanac root directory.

    Returns:
        Path to the written index.md.
    """
    area_dir = root / "areas" / "agriculture"
    area_dir.mkdir(parents=True, exist_ok=True)
    content = (
        "---\n"
        "title: Agriculture\n"
        "area: agriculture\n"
        "hide:\n"
        "  - toc\n"
        "---\n\n"
        "# Agriculture\n\n"
        "Sustainable farming, soil science, and food systems.\n\n"
        "## Subareas\n\n"
        "- **Gardening** · home and community growing, soil health, plant care\n"
        "- **Seasonal Planting** · planting calendars, crop rotation, climate-adapted growing\n\n"
        "*0 documents*\n"
    )
    path = area_dir / "index.md"
    path.write_text(content)
    return path


# ===========================================================================
# Canonical slug
# ===========================================================================


class TestAgricultureSlug:
    """Verify `agriculture` is a recognised canonical area slug."""

    def test_agriculture_in_valid_areas(self) -> None:
        """`agriculture` must appear in the VALID_AREAS constant."""
        assert "agriculture" in VALID_AREAS

    def test_agriculture_slug_is_lowercase_hyphen(self) -> None:
        """`agriculture` conforms to the lowercase-hyphen slug pattern."""
        import re

        slug_re = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$")
        assert slug_re.match("agriculture")


# ===========================================================================
# Article validation
# ===========================================================================


class TestAgricultureArticleValidation:
    """Verify that articles filed under `agriculture` validate correctly."""

    def test_valid_article_passes(self, almanac_root: Path) -> None:
        """A fully specified agriculture article returns no violations."""
        path = _write_agriculture_article(almanac_root, "regenerative-farming")
        violations = validate_document(path, almanac_root)
        assert violations == []

    def test_missing_title_is_rejected(self, almanac_root: Path) -> None:
        """An agriculture article missing `title` produces a violation."""
        path = _write_agriculture_article(
            almanac_root,
            "no-title",
            overrides={"title": None},
        )
        violations = validate_document(path, almanac_root)
        assert len(violations) >= 1

    def test_missing_source_url_is_rejected(self, almanac_root: Path) -> None:
        """An agriculture article missing `source_url` produces a violation."""
        path = _write_agriculture_article(
            almanac_root,
            "no-source-url",
            overrides={"source_url": None},
        )
        violations = validate_document(path, almanac_root)
        assert len(violations) >= 1

    def test_invalid_area_slug_rejected(self, almanac_root: Path) -> None:
        """An article with `area: fake-area` filed in agriculture/ is rejected."""
        path = _write_agriculture_article(
            almanac_root,
            "wrong-area",
            overrides={"area": "fake-area"},
        )
        violations = validate_document(path, almanac_root)
        assert any("area" in v.field or "Unknown" in v.message for v in violations)

    def test_almanac_native_doc_validates(self, almanac_root: Path) -> None:
        """An almanac-native document (type: almanac) under agriculture validates cleanly."""
        area_dir = almanac_root / "areas" / "agriculture"
        area_dir.mkdir(parents=True, exist_ok=True)
        data = {
            "title": "Seasonal Planting Calendar",
            "area": "agriculture",
            "type": "almanac",
            "source": "Observatory Almanac",
            "license": "MIT",
            "updated": "2026-05-06",
            "summary": "Month-by-month planting guide for temperate and subtropical climates.",
            "tags": ["seasonal-planting", "gardening", "calendar"],
        }
        fm = yaml.dump(data, allow_unicode=True)
        path = area_dir / "seasonal-planting-calendar.md"
        path.write_text(f"---\n{fm}---\n\nBody content.\n")
        violations = validate_document(path, almanac_root)
        assert violations == []


# ===========================================================================
# Index nav page exclusion
# ===========================================================================


class TestAgricultureIndexExclusion:
    """Verify the agriculture index.md nav page is excluded from content validation."""

    def test_index_alone_produces_no_violations(self, almanac_root: Path) -> None:
        """An agriculture area with only index.md returns exit code 0."""
        _write_agriculture_index(almanac_root)
        code = run_validation(almanac_root)
        assert code == 0

    def test_index_alongside_article_does_not_cause_violations(
        self, almanac_root: Path
    ) -> None:
        """index.md alongside a valid article does not produce extra violations."""
        _write_agriculture_index(almanac_root)
        _write_agriculture_article(almanac_root, "companion-article")
        code = run_validation(almanac_root)
        assert code == 0

    def test_index_excluded_by_collect_not_validate_document(
        self, almanac_root: Path
    ) -> None:
        """index.md is excluded at collect_content_files level, not validate_document.

        run_validation returns 0 for an area with only index.md because
        collect_content_files skips index.md files — validate_document is
        never called on them during a normal run.
        """
        from almanac.validator import collect_content_files

        _write_agriculture_index(almanac_root)
        collected = collect_content_files(almanac_root)
        # index.md must not appear in the collected file list
        assert not any(f.name == "index.md" for f in collected)
