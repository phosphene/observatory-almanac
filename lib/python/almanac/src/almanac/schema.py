"""Pydantic schema models for Observatory Almanac document types.

Each model corresponds to one document type defined in ``SCHEMA.md``.
The models are the machine-readable specification of the schema — they
drive both validation and documentation generation.

Design rationale
----------------
Frontmatter in the almanac serves two audiences simultaneously: agents
who write and validate content, and MkDocs Material which reads ``title``,
``tags``, and ``summary`` for search and social cards.  The models are
therefore a strict intersection: every field present here MUST appear in
every document of that type, and every field the theme expects MUST be
declared in the model.

The ``type`` discriminator field is used for validation routing — the
validator reads it first, then instantiates the correct model.  This
avoids a single monolithic model that conflates all document types.

Failure modes of the prior (un-typed) approach
-----------------------------------------------
Without Pydantic models, validation relied on ``re.search`` for each
required field name.  This caught missing fields but not type errors,
malformed ISO dates, invalid area slugs, or license drift.  The models
encode all of these constraints declaratively.
"""

from __future__ import annotations

import re
from datetime import date
from enum import StrEnum
from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    BeforeValidator,
)

# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

IsoDate = Annotated[
    str, BeforeValidator(lambda v: v.isoformat() if isinstance(v, date) else str(v))
]

# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------


class DocumentType(StrEnum):
    """Discriminator enum for all document types in the Almanac.

    The ``article``/``almanac`` boundary is the most consequential
    distinction in the corpus: it tracks intellectual provenance.
    Observatory.wiki articles are CC BY-NC-SA 4.0 — they were authored
    by external experts and published by IMI; the Almanac mirrors them.
    Almanac-native documents are MIT-licensed first-party content.
    Conflating the two would misrepresent the licensing chain for any
    downstream reuser.

    Type selection guide
    --------------------
    ``article``
        Expert-authored piece scraped from observatory.wiki.  Always
        carries ``source_url``, ``author``, ``author_slug``, and
        ``license: CC BY-NC-SA 4.0``.

    ``classic``
        Long-form canonical journalism elevated to reference status.
        Distinct from ``article`` in editorial weight and search ranking;
        use when a piece has been designated as a primary reference rather
        than current-events reporting.

    ``guide``
        Curated multi-article collection with an editor.  Lives in
        ``guides/`` rather than ``areas/``.  Has ``editor`` and
        ``editor_slug`` in place of ``author`` and ``author_slug``.

    ``almanac``
        General reference content from the Almanac source library that
        does not fit a more specific native type.  MIT licensed.

    ``recipe``
        Culinary recipe or food preparation guide.  MIT licensed.

    ``rulebook``
        Complete game rules document.  MIT licensed.

    ``factbook``
        Country or regional reference profile.  MIT licensed.

    ``reference``
        Practical reference material (emergency procedures, conversion
        tables, civic document templates).  MIT licensed.

    ``assessment``
        Self-knowledge or psychological assessment instrument.  MIT licensed.

    ``field-guide``
        Natural history identification guide (birds, trees, insects).
        MIT licensed.  Note: the enum *value* uses a hyphen (``field-guide``)
        to match the YAML frontmatter slug convention.
    """

    article = "article"
    guide = "guide"
    classic = "classic"
    almanac = "almanac"
    recipe = "recipe"
    rulebook = "rulebook"
    factbook = "factbook"
    reference = "reference"
    assessment = "assessment"
    field_guide = "field-guide"


class LicenseType(StrEnum):
    """Permitted license identifiers for almanac content.

    The two licenses map cleanly to the two content origins:

    ``CC BY-NC-SA 4.0``
        Observatory.wiki content.  The license is set by IMI as the
        upstream publisher and cannot be changed.  Non-commercial,
        share-alike attribution required.  All ``article``, ``classic``,
        and ``guide`` documents carry this license.

    ``MIT``
        Almanac-native content — reference material, recipes, rulebooks,
        factbooks, and assessments authored directly for the Almanac.
        MIT was chosen over CC because it imposes no share-alike
        restriction on downstream software integrations (e.g., a Telegram
        bot or PWA that bundles the content).
    """

    cc_by_nc_sa_40 = "CC BY-NC-SA 4.0"
    mit = "MIT"


from almanac.constants import ISO_DATE_RE, SLUG_RE, VALID_AREAS


# ---------------------------------------------------------------------------
# Base model
# ---------------------------------------------------------------------------


class AlmanacBase(BaseModel, frozen=True, extra="forbid"):
    """Shared invariant base for all Almanac document frontmatter.

    Design constraints
    ------------------
    ``frozen=True`` — models are immutable once constructed, following the
    evolutionary (not mutational) update pattern.  To produce a modified
    copy, use ``model.model_copy(update={"field": new_value})``::

        original = ArticleFrontmatter(**data)
        corrected = original.model_copy(update={"area": "science"})

    Attempting direct attribute assignment raises ``ValidationError``.
    This is intentional: it forces all content changes through the
    validation layer rather than bypassing it with an in-place mutation.

    ``extra='forbid'`` — any field present in the frontmatter but absent
    from the model is a schema violation.  This is stricter than
    ``extra='ignore'`` (silent drop) or ``extra='allow'`` (untyped
    pass-through).  The rationale: unknown fields are almost always
    migration artifacts or typos; surfacing them as errors catches
    problems before they propagate into the index and search database.
    """

    title: str = Field(min_length=1, max_length=300)
    area: str
    type: DocumentType
    license: LicenseType
    updated: IsoDate
    summary: str = Field(min_length=10, max_length=600)
    tags: list[str] = Field(min_length=1)

    @field_validator("area")
    @classmethod
    def area_must_be_canonical(cls, v: str) -> str:
        """Validate area slug against the canonical AREAS.md taxonomy.

        Args:
            v: Raw area value from frontmatter.

        Returns:
            Validated area slug.

        Raises:
            ValueError: If the area is not in the canonical set.
        """
        if v not in VALID_AREAS:
            raise ValueError(f"Unknown area '{v}'. See AREAS.md for canonical slugs.")
        return v

    @field_validator("updated")
    @classmethod
    def updated_must_be_iso(cls, v: str) -> str:
        """Validate that updated is an ISO 8601 date string.

        Args:
            v: Raw updated value.

        Returns:
            Validated date string.

        Raises:
            ValueError: If the value is not a valid ISO date.
        """
        if not ISO_DATE_RE.match(v):
            raise ValueError(f"updated must be ISO 8601 (YYYY-MM-DD), got '{v}'")
        return v

    @field_validator("tags")
    @classmethod
    def tags_must_be_slugs(cls, v: list[str]) -> list[str]:
        """Validate that all tags are lowercase-hyphen slugs.

        Args:
            v: List of tag strings.

        Returns:
            Validated tag list.

        Raises:
            ValueError: If any tag contains invalid characters.
        """
        for tag in v:
            if not SLUG_RE.match(tag):
                raise ValueError(
                    f"Tag '{tag}' must be lowercase-hyphen (e.g. climate-change)"
                )
        return v


# ---------------------------------------------------------------------------
# Observatory.wiki article
# ---------------------------------------------------------------------------


class ArticleFrontmatter(AlmanacBase, frozen=True, extra="forbid"):
    """Frontmatter model for observatory.wiki-sourced articles.

    The ``author_slug`` field must match a file in ``authors/``.
    The ``source_url`` anchors provenance and enables deduplication —
    two articles cannot share a source URL without being the same article.
    """

    author: str = Field(min_length=1)
    author_slug: str
    source: str = Field(min_length=1)
    source_url: str
    published: IsoDate

    @field_validator("author_slug")
    @classmethod
    def author_slug_must_be_valid(cls, v: str) -> str:
        """Validate author_slug is a lowercase-hyphen identifier.

        Args:
            v: Raw author_slug value.

        Returns:
            Validated slug.

        Raises:
            ValueError: If slug format is invalid.
        """
        if not SLUG_RE.match(v):
            raise ValueError(f"author_slug '{v}' must be lowercase-hyphen")
        return v

    @field_validator("published")
    @classmethod
    def published_must_be_iso(cls, v: str) -> str:
        """Validate published date is ISO 8601.

        Args:
            v: Raw published value.

        Returns:
            Validated date string.

        Raises:
            ValueError: If the value is not a valid ISO date.
        """
        if not ISO_DATE_RE.match(v):
            raise ValueError(f"published must be ISO 8601, got '{v}'")
        return v

    @field_validator("source_url")
    @classmethod
    def source_url_must_be_https(cls, v: str) -> str:
        """Validate source_url is an HTTPS URL.

        Args:
            v: Raw source_url value.

        Returns:
            Validated URL.

        Raises:
            ValueError: If URL does not start with https://.
        """
        if not v.startswith("https://"):
            raise ValueError(f"source_url must be https://, got '{v}'")
        return v


# ---------------------------------------------------------------------------
# Almanac-native document
# ---------------------------------------------------------------------------


class AlmanacDocFrontmatter(AlmanacBase, frozen=True, extra="forbid"):
    """Frontmatter model for almanac-native documents.

    Almanac-native documents (recipes, rulebooks, factbooks, etc.) originate
    in the Observatory Almanac itself rather than on observatory.wiki.  They
    carry a ``source_path`` tracing their origin in the source tree, and are
    MIT-licensed rather than CC BY-NC-SA.

    The ``source_path`` enables the migration script to be idempotent:
    if a file already exists with the same source_path, it was already
    migrated and should not be overwritten.
    """

    source: str = Field(default="Observatory Almanac")
    source_path: str | None = Field(default=None)


# ---------------------------------------------------------------------------
# Guide
# ---------------------------------------------------------------------------


class GuideFrontmatter(BaseModel, frozen=True, extra="forbid"):
    """Frontmatter model for editorial guide documents.

    Guides are curated multi-article collections with an editor rather
    than a single author.  They live in ``guides/`` rather than ``areas/``.
    """

    title: str = Field(min_length=1, max_length=300)
    type: DocumentType
    editor: str
    editor_slug: str
    source: str
    source_url: str
    license: LicenseType
    published: IsoDate
    updated: IsoDate
    summary: str = Field(min_length=10)
    tags: list[str] = Field(min_length=1)
    articles: list[Annotated[dict, Field()]] = Field(default_factory=list)

    @model_validator(mode="after")
    def type_must_be_guide(self) -> GuideFrontmatter:
        """Enforce that ``GuideFrontmatter`` documents declare ``type: guide``.

        This discriminator check exists because ``parse_frontmatter`` selects
        a schema model based on the ``type`` field before constructing the
        Pydantic model, so a document that was *routed* to ``GuideFrontmatter``
        but declares a different ``type`` indicates a routing bug in the
        caller — not a content error.  Raising here makes that routing failure
        visible as a validation error rather than a silent schema mismatch.

        Without this check, an ``article`` document accidentally filed under
        ``guides/`` would pass validation as a ``GuideFrontmatter`` with a
        wrong type label, and downstream consumers (search index, MkDocs nav)
        would treat it as a guide.

        Returns:
            Self if ``type == DocumentType.guide``.

        Raises:
            ValueError: If ``type`` is any value other than ``'guide'``.
                The caller has routed a non-guide document to this model.
        """
        if self.type != DocumentType.guide:
            raise ValueError(
                f"Document routed to GuideFrontmatter but declares type={self.type!r}. "
                "Check the routing logic in parse_frontmatter — guide documents must "
                "have 'type: guide' in their frontmatter."
            )
        return self


# ---------------------------------------------------------------------------
# Author profile
# ---------------------------------------------------------------------------


class AuthorFrontmatter(BaseModel, frozen=True, extra="forbid"):
    """Frontmatter model for author profile documents.

    Author profiles are the referential anchor for ``author_slug`` fields
    in articles.  A valid almanac has a profile file for every unique
    author_slug used in article frontmatter.
    """

    name: str = Field(min_length=1)
    slug: str
    source_url: str | None = None
    credentials: str | None = None

    @field_validator("slug")
    @classmethod
    def slug_must_be_valid(cls, v: str) -> str:
        """Validate slug is a lowercase-hyphen identifier.

        Args:
            v: Raw slug value.

        Returns:
            Validated slug.

        Raises:
            ValueError: If slug format is invalid.
        """
        if not SLUG_RE.match(v):
            raise ValueError(f"slug '{v}' must be lowercase-hyphen")
        return v


# ---------------------------------------------------------------------------
# Parse helpers
# ---------------------------------------------------------------------------


def parse_frontmatter(
    raw_yaml: dict,
) -> AlmanacBase | AlmanacDocFrontmatter | GuideFrontmatter | AuthorFrontmatter:
    """Instantiate the correct model from a parsed YAML dict.

    Routing is done by ``type`` field first.  Documents without ``type``
    are assumed to be author profiles.

    Args:
        raw_yaml: Dict parsed from YAML frontmatter.

    Returns:
        Validated Pydantic model instance.

    Raises:
        ValueError: If ``type`` is present but unrecognised, or if
            validation fails.
    """
    doc_type = raw_yaml.get("type")
    if doc_type is None:
        # Author profiles have no 'type' field
        return AuthorFrontmatter(**raw_yaml)

    if doc_type == "guide":
        return GuideFrontmatter(**raw_yaml)

    if doc_type in {"article", "classic"}:
        return ArticleFrontmatter(**raw_yaml)

    # Almanac-native types
    native_types = {dt.value for dt in DocumentType} - {"article", "guide", "classic"}
    if doc_type in native_types:
        return AlmanacDocFrontmatter(**raw_yaml)

    raise ValueError(f"Unrecognised document type '{doc_type}'")


def today_iso() -> str:
    """Return today's date as an ISO 8601 string.

    Returns:
        Date string in YYYY-MM-DD format.
    """
    return date.today().isoformat()
