"""Tests for almanac.validator — content tree validation.

Covers: extract_frontmatter_yaml, validate_document, validate_author_refs,
collect_content_files, and run_validation exit codes.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from almanac.validator import (
    collect_content_files,
    extract_frontmatter_yaml,
    run_validation,
    validate_author_refs,
    validate_document,
)


def _write_article(
    root: Path, area: str, slug: str, overrides: dict | None = None
) -> Path:
    """Write a valid article file and return its path.

    Args:
        root: Almanac root directory.
        area: Area slug.
        slug: File slug.
        overrides: Optional frontmatter field overrides.

    Returns:
        Path to the written file.
    """
    area_dir = root / "areas" / area
    area_dir.mkdir(parents=True, exist_ok=True)
    data = {
        "title": "Test Article",
        "area": area,
        "type": "article",
        "author": "Test Author",
        "author_slug": "test-author",
        "source": "The Observatory",
        "source_url": "https://observatory.wiki/Test_Article",
        "license": "CC BY-NC-SA 4.0",
        "published": "2024-01-01",
        "updated": "2024-01-01",
        "summary": "A test article used in automated validation tests.",
        "tags": ["test", "science"],
    }
    if overrides:
        data.update(overrides)
    fm = yaml.dump(data, allow_unicode=True)
    path = area_dir / f"{slug}.md"
    path.write_text(f"---\n{fm}---\n\nBody content.\n")
    return path


def _write_author(root: Path, slug: str) -> Path:
    """Write a minimal author profile and return its path.

    Args:
        root: Almanac root directory.
        slug: Author slug.

    Returns:
        Path to the written file.
    """
    authors_dir = root / "authors"
    authors_dir.mkdir(exist_ok=True)
    data = {"name": slug.replace("-", " ").title(), "slug": slug}
    fm = yaml.dump(data, allow_unicode=True)
    path = authors_dir / f"{slug}.md"
    path.write_text(f"---\n{fm}---\n\nAuthor bio.\n")
    return path


# ===========================================================================
# extract_frontmatter_yaml
# ===========================================================================


class TestExtractFrontmatterYaml:
    """Verify frontmatter extraction from raw markdown text."""

    def test_valid_frontmatter(self) -> None:
        """Valid YAML frontmatter is parsed into a dict."""
        text = "---\ntitle: Test\narea: science\n---\n\nBody."
        data, body = extract_frontmatter_yaml(text)
        assert data["title"] == "Test"
        assert "Body." in body

    def test_missing_frontmatter_raises(self) -> None:
        """Document without frontmatter raises ValueError."""
        with pytest.raises(ValueError, match="No frontmatter"):
            extract_frontmatter_yaml("# Just a heading\n\nNo YAML.")

    def test_unclosed_frontmatter_raises(self) -> None:
        """Frontmatter without closing --- raises ValueError."""
        with pytest.raises(ValueError, match="not closed"):
            extract_frontmatter_yaml("---\ntitle: Test\n# no closing")

    def test_body_stripped_of_leading_newlines(self) -> None:
        """Body text has leading newlines stripped."""
        text = "---\ntitle: T\n---\n\n\nFirst paragraph."
        _, body = extract_frontmatter_yaml(text)
        assert body.startswith("First")

    def test_empty_frontmatter_returns_empty_dict(self) -> None:
        """An empty frontmatter block returns an empty dict."""
        text = "---\n---\n\nBody."
        data, _ = extract_frontmatter_yaml(text)
        assert data == {}


# ===========================================================================
# validate_document
# ===========================================================================


class TestValidateDocument:
    """Verify per-document validation logic."""

    def test_valid_article_returns_no_violations(self, almanac_root: Path) -> None:
        """A valid article file returns an empty violation list."""
        path = _write_article(almanac_root, "science", "valid-article")
        violations = validate_document(path, almanac_root)
        assert violations == []

    def test_missing_required_field_is_detected(self, almanac_root: Path) -> None:
        """A file missing a required field produces a violation."""
        path = _write_article(
            almanac_root, "science", "bad-article", overrides={"source_url": None}
        )
        violations = validate_document(path, almanac_root)
        # source_url=None should fail the https validator or required check
        assert len(violations) >= 1

    def test_unknown_area_is_detected(self, almanac_root: Path) -> None:
        """An article with an unknown area slug produces a violation."""
        path = _write_article(
            almanac_root, "science", "wrong-area", overrides={"area": "fake-area"}
        )
        violations = validate_document(path, almanac_root)
        assert any("area" in v.field or "Unknown" in v.message for v in violations)

    def test_missing_frontmatter_is_detected(self, almanac_root: Path) -> None:
        """A file without frontmatter produces a violation."""
        path = almanac_root / "areas" / "science" / "no-fm.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# No Frontmatter\n\nBody only.")
        violations = validate_document(path, almanac_root)
        assert len(violations) >= 1
        assert violations[0].field == "frontmatter"

    def test_almanac_native_doc_validates(self, almanac_root: Path) -> None:
        """An almanac-native document (rulebook) validates cleanly."""
        area_dir = almanac_root / "areas" / "arts-recreation"
        area_dir.mkdir(parents=True, exist_ok=True)
        data = {
            "title": "Chess Rules",
            "area": "arts-recreation",
            "type": "rulebook",
            "source": "Observatory Almanac",
            "license": "MIT",
            "updated": "2026-04-28",
            "summary": "Complete rules for chess from opening to endgame technique.",
            "tags": ["games", "strategy"],
        }
        fm = yaml.dump(data, allow_unicode=True)
        path = area_dir / "chess.md"
        path.write_text(f"---\n{fm}---\n\nBody.\n")
        violations = validate_document(path, almanac_root)
        assert violations == []

    def test_violation_path_is_relative(self, almanac_root: Path) -> None:
        """Violation paths are relative to the almanac root."""
        path = almanac_root / "areas" / "science" / "no-fm.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("No frontmatter at all.")
        violations = validate_document(path, almanac_root)
        assert not Path(violations[0].path).is_absolute()


# ===========================================================================
# validate_author_refs
# ===========================================================================


class TestValidateAuthorRefs:
    """Verify cross-reference checks between articles and author profiles."""

    def test_matching_author_no_violation(self, almanac_root: Path) -> None:
        """An article whose author_slug has a matching profile passes."""
        _write_article(
            almanac_root,
            "science",
            "article-a",
            overrides={"author_slug": "jane-smith"},
        )
        _write_author(almanac_root, "jane-smith")
        violations = validate_author_refs(almanac_root)
        assert all(v.field != "author_slug" for v in violations)

    def test_missing_author_profile_flagged(self, almanac_root: Path) -> None:
        """An article whose author_slug has no profile produces a violation."""
        _write_article(
            almanac_root,
            "science",
            "article-b",
            overrides={"author_slug": "unknown-author"},
        )
        violations = validate_author_refs(almanac_root)
        assert any("unknown-author" in v.message for v in violations)

    def test_the_observatory_slug_exempt(self, almanac_root: Path) -> None:
        """'the-observatory' author_slug is exempt from profile requirement."""
        _write_article(
            almanac_root,
            "science",
            "article-c",
            overrides={"author_slug": "the-observatory"},
        )
        violations = validate_author_refs(almanac_root)
        assert not violations

    def test_no_areas_returns_empty(self, tmp_path: Path) -> None:
        """A root with no areas/ directory returns no violations."""
        root = tmp_path / "empty"
        root.mkdir()
        (root / "SCHEMA.md").write_text("")
        violations = validate_author_refs(root)
        assert violations == []


# ===========================================================================
# collect_content_files
# ===========================================================================


class TestCollectContentFiles:
    """Verify the content file collector enumerates correctly."""

    def test_collects_areas_and_authors(self, almanac_root: Path) -> None:
        """Files in areas/ and authors/ are collected."""
        _write_article(almanac_root, "science", "article-1")
        _write_author(almanac_root, "test-author")
        files = collect_content_files(almanac_root)
        paths = [str(f) for f in files]
        assert any("areas" in p for p in paths)
        assert any("authors" in p for p in paths)

    def test_excludes_meta_dir(self, almanac_root: Path) -> None:
        """Files in meta/ are not collected."""
        (almanac_root / "meta" / "index.md").write_text("meta content")
        files = collect_content_files(almanac_root)
        assert not any("meta" in str(f) for f in files)

    def test_empty_tree_returns_empty(self, almanac_root: Path) -> None:
        """An almanac with no content files returns an empty list."""
        files = collect_content_files(almanac_root)
        assert files == []


# ===========================================================================
# run_validation exit codes
# ===========================================================================


class TestRunValidation:
    """Verify run_validation returns correct exit codes."""

    def test_clean_tree_returns_zero(self, almanac_root: Path) -> None:
        """A tree with valid content returns exit code 0."""
        _write_article(
            almanac_root,
            "science",
            "good-article",
            overrides={"author_slug": "the-observatory"},
        )
        code = run_validation(almanac_root)
        assert code == 0

    def test_violations_return_one(self, almanac_root: Path) -> None:
        """A tree with invalid content returns exit code 1."""
        area_dir = almanac_root / "areas" / "science"
        area_dir.mkdir(parents=True, exist_ok=True)
        (area_dir / "bad.md").write_text("No frontmatter here.")
        code = run_validation(almanac_root)
        assert code == 1

    def test_empty_tree_returns_two(self, almanac_root: Path) -> None:
        """A tree with no content files returns exit code 2."""
        code = run_validation(almanac_root)
        assert code == 2
