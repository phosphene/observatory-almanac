"""Tests for almanac.schema — Pydantic models and parse_frontmatter routing.

Covers: ArticleFrontmatter, AlmanacDocFrontmatter, AuthorFrontmatter,
GuideFrontmatter, and the parse_frontmatter dispatcher.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from almanac.schema import (
    VALID_AREAS,
    AlmanacDocFrontmatter,
    ArticleFrontmatter,
    AuthorFrontmatter,
    DocumentType,
    GuideFrontmatter,
    LicenseType,
    parse_frontmatter,
    today_iso,
)

# ===========================================================================
# ArticleFrontmatter
# ===========================================================================


class TestArticleFrontmatter:
    """Validate ArticleFrontmatter model constraints."""

    def test_valid_article(self, article_data: dict) -> None:
        """A well-formed article dict passes validation."""
        model = ArticleFrontmatter(**article_data)
        assert model.title == article_data["title"]
        assert model.area == "science"

    def test_missing_required_field_raises(self, article_data: dict) -> None:
        """Omitting a required field raises ValidationError."""
        del article_data["source_url"]
        with pytest.raises(ValidationError):
            ArticleFrontmatter(**article_data)

    def test_unknown_area_raises(self, article_data: dict) -> None:
        """An area slug not in AREAS.md raises ValidationError."""
        article_data["area"] = "not-a-real-area"
        with pytest.raises(ValidationError, match="Unknown area"):
            ArticleFrontmatter(**article_data)

    def test_invalid_iso_date_raises(self, article_data: dict) -> None:
        """A malformed published date raises ValidationError."""
        article_data["published"] = "Feb 6 2026"
        with pytest.raises(ValidationError, match="ISO 8601"):
            ArticleFrontmatter(**article_data)

    def test_non_https_source_url_raises(self, article_data: dict) -> None:
        """A non-HTTPS source_url raises ValidationError."""
        article_data["source_url"] = "http://observatory.wiki/Article"
        with pytest.raises(ValidationError, match="https"):
            ArticleFrontmatter(**article_data)

    def test_invalid_author_slug_raises(self, article_data: dict) -> None:
        """An author_slug with spaces or uppercase raises ValidationError."""
        article_data["author_slug"] = "Jane Smith"
        with pytest.raises(ValidationError, match="lowercase-hyphen"):
            ArticleFrontmatter(**article_data)

    def test_invalid_tag_raises(self, article_data: dict) -> None:
        """A tag with uppercase letters raises ValidationError."""
        article_data["tags"] = ["ValidTag"]
        with pytest.raises(ValidationError, match="lowercase-hyphen"):
            ArticleFrontmatter(**article_data)

    def test_empty_tags_raises(self, article_data: dict) -> None:
        """An empty tags list raises ValidationError."""
        article_data["tags"] = []
        with pytest.raises(ValidationError):
            ArticleFrontmatter(**article_data)

    def test_short_summary_raises(self, article_data: dict) -> None:
        """A summary under 10 characters raises ValidationError."""
        article_data["summary"] = "Too short"
        with pytest.raises(ValidationError):
            ArticleFrontmatter(**article_data)

    def test_frozen_prevents_mutation(self, article_data: dict) -> None:
        """Frozen model raises on direct attribute assignment."""
        model = ArticleFrontmatter(**article_data)
        with pytest.raises(ValidationError):
            model.title = "Changed"  # type: ignore[misc]

    def test_extra_fields_forbidden(self, article_data: dict) -> None:
        """Unknown extra fields are rejected (extra='forbid')."""
        article_data["mystery_field"] = "value"
        with pytest.raises(ValidationError):
            ArticleFrontmatter(**article_data)


# ===========================================================================
# AlmanacDocFrontmatter
# ===========================================================================


class TestAlmanacDocFrontmatter:
    """Validate AlmanacDocFrontmatter for almanac-native content."""

    def test_valid_rulebook(self, almanac_doc_data: dict) -> None:
        """A valid rulebook document passes validation."""
        model = AlmanacDocFrontmatter(**almanac_doc_data)
        assert model.type == DocumentType.rulebook
        assert model.license == LicenseType.mit

    def test_valid_recipe(self, almanac_doc_data: dict) -> None:
        """A recipe document with correct type passes."""
        almanac_doc_data["type"] = "recipe"
        model = AlmanacDocFrontmatter(**almanac_doc_data)
        assert model.type == DocumentType.recipe

    def test_all_native_types_accepted(self, almanac_doc_data: dict) -> None:
        """Every almanac-native type is accepted by the model."""
        native_types = [
            "almanac",
            "recipe",
            "rulebook",
            "factbook",
            "reference",
            "assessment",
            "field-guide",
        ]
        for t in native_types:
            almanac_doc_data["type"] = t
            model = AlmanacDocFrontmatter(**almanac_doc_data)
            assert model.type.value == t

    def test_source_path_optional(self, almanac_doc_data: dict) -> None:
        """source_path is optional and defaults to None."""
        del almanac_doc_data["source_path"]
        model = AlmanacDocFrontmatter(**almanac_doc_data)
        assert model.source_path is None


# ===========================================================================
# AuthorFrontmatter
# ===========================================================================


class TestAuthorFrontmatter:
    """Validate AuthorFrontmatter model."""

    def test_valid_author(self, author_data: dict) -> None:
        """A well-formed author dict passes validation."""
        model = AuthorFrontmatter(**author_data)
        assert model.name == "Leslie Alan Horvitz"
        assert model.slug == "leslie-alan-horvitz"

    def test_invalid_slug_raises(self, author_data: dict) -> None:
        """A slug with spaces raises ValidationError."""
        author_data["slug"] = "Leslie Horvitz"
        with pytest.raises(ValidationError, match="lowercase-hyphen"):
            AuthorFrontmatter(**author_data)

    def test_source_url_optional(self, author_data: dict) -> None:
        """source_url is optional."""
        del author_data["source_url"]
        model = AuthorFrontmatter(**author_data)
        assert model.source_url is None

    def test_credentials_optional(self, author_data: dict) -> None:
        """credentials field is optional."""
        model = AuthorFrontmatter(**author_data)
        assert model.credentials is None


# ===========================================================================
# GuideFrontmatter
# ===========================================================================


class TestGuideFrontmatter:
    """Validate GuideFrontmatter model."""

    def _guide_data(self) -> dict:
        """Return a valid guide frontmatter dict."""
        return {
            "title": "Guide to Artificial Intelligence",
            "type": "guide",
            "editor": "Leslie Alan Horvitz",
            "editor_slug": "leslie-alan-horvitz",
            "source": "The Observatory",
            "source_url": "https://observatory.wiki/Guide_to_AI",
            "license": "CC BY-NC-SA 4.0",
            "published": "2025-01-01",
            "updated": "2026-04-01",
            "summary": "A curated collection of Observatory articles on artificial intelligence.",
            "tags": ["artificial-intelligence", "technology"],
        }

    def test_valid_guide(self) -> None:
        """A well-formed guide dict passes validation."""
        model = GuideFrontmatter(**self._guide_data())
        assert model.type == DocumentType.guide

    def test_non_guide_type_raises(self) -> None:
        """A guide with type != 'guide' raises ValidationError."""
        data = self._guide_data()
        data["type"] = "article"
        with pytest.raises(ValidationError, match="type: guide"):
            GuideFrontmatter(**data)


# ===========================================================================
# parse_frontmatter dispatcher
# ===========================================================================


class TestParseFrontmatter:
    """Verify parse_frontmatter routes to the correct model."""

    def test_routes_article(self, article_data: dict) -> None:
        """Article type routes to ArticleFrontmatter."""
        result = parse_frontmatter(article_data)
        assert isinstance(result, ArticleFrontmatter)

    def test_routes_almanac_native(self, almanac_doc_data: dict) -> None:
        """Rulebook type routes to AlmanacDocFrontmatter."""
        result = parse_frontmatter(almanac_doc_data)
        assert isinstance(result, AlmanacDocFrontmatter)

    def test_routes_author(self, author_data: dict) -> None:
        """No type field routes to AuthorFrontmatter."""
        result = parse_frontmatter(author_data)
        assert isinstance(result, AuthorFrontmatter)

    def test_unknown_type_raises(self, article_data: dict) -> None:
        """An unrecognised type raises ValueError."""
        article_data["type"] = "bogus-type"
        with pytest.raises((ValueError, ValidationError)):
            parse_frontmatter(article_data)


# ===========================================================================
# Constants / enums
# ===========================================================================


class TestConstants:
    """Verify canonical constants are self-consistent."""

    def test_valid_areas_non_empty(self) -> None:
        """VALID_AREAS contains at least the 25 canonical areas.

        Note: `food` was retired 2026-05-06 and merged into `cooking`
        (displayed as "Food"). Count reduced from 26 to 25.
        """
        assert len(VALID_AREAS) >= 25

    def test_science_in_valid_areas(self) -> None:
        """'science' is a valid area."""
        assert "science" in VALID_AREAS

    def test_document_type_values_are_slugs(self) -> None:
        """All DocumentType values are lowercase-hyphen strings."""
        import re

        for dt in DocumentType:
            assert re.match(r"^[a-z][a-z-]*$", dt.value), f"Invalid: {dt.value}"

    def test_today_iso_format(self) -> None:
        """today_iso() returns a valid ISO 8601 date string."""
        import re

        result = today_iso()
        assert re.match(r"^\d{4}-\d{2}-\d{2}$", result)
