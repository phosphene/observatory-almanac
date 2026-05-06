"""Canonical constants for the Observatory Almanac.

Includes pre-compiled regex for slugs and dates, and the reference
set of valid areas.
"""

import re

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

# Lowercase-hyphen slug (e.g. 'climate-change', 'sapolsky-robert')
# Must start and end with alphanumeric, can contain internal hyphens.
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")

# ISO 8601 date (YYYY-MM-DD)
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Markdown heading (# Title)
HEADING_RE = re.compile(r"^#\s+(.+)$", re.M)

# ---------------------------------------------------------------------------
# Taxonomy
# ---------------------------------------------------------------------------

VALID_AREAS = frozenset(
    {
        "agriculture",
        "animals",
        "arts-recreation",
        "charter-schools",
        "cooking",
        "dig-labs",
        "economy",
        "education",
        "energy",
        "environment",
        # "food" retired 2026-05-06 — merged into "cooking" (displayed as "Food")
        "health",
        "history",
        "human-bridges",
        "language",
        "literature",
        "local-peace-economy",
        "media",
        "natural-health",
        "peoples-movements",
        "philosophy",
        "psychology",
        "science",
        "technology",
        "voting-elections",
        "world-affairs",
    }
)
