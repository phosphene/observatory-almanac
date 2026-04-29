"""Shared frontmatter parsing utilities for the Observatory Almanac.

This module is the single source of truth for extracting YAML frontmatter
from almanac markdown files.  It was created to resolve the duplication
between ``almanac.validator`` and ``almanac.index``, which had evolved
independent implementations of the same parse-and-extract logic.

Why a shared module rather than inlining
-----------------------------------------
Both the validator and the index generator need to read frontmatter, but
they need it at different granularities: the validator needs the full parsed
dict for schema validation; the index generator needs only ``title``,
``area``, ``type``, and ``author`` for building the inventory.  A shared
module provides both via two public functions, with the I/O-free logic layer
isolated from filesystem concerns.

The ruamel.yaml choice
-----------------------
``ruamel.yaml`` is used throughout the almanac toolchain in preference to
``PyYAML`` because it preserves comments and round-trips YAML without
rewriting.  ``YAML(typ='safe')`` gives read-only access with safe loading.
``YAML(typ='rt')`` (round-trip) is used when comments must be preserved
for write-back; this module uses ``rt`` to match the rest of the package.
"""

from __future__ import annotations

import re
from pathlib import Path

from ruamel.yaml import YAML

from almanac.constants import HEADING_RE

_yaml = YAML()
_yaml.preserve_quotes = True


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Split a markdown document into a frontmatter dict and the body text.

    The frontmatter block is delimited by ``---`` on the first line and a
    closing ``---`` on a later line.  Both delimiters are consumed; the
    returned body has leading newlines stripped.

    This function is the canonical frontmatter extractor for the almanac
    toolchain.  It was created to eliminate duplication between
    ``almanac.validator`` and ``almanac.index``, which had each implemented
    their own variants.

    Empty frontmatter blocks (``---\\n---``) return an empty dict rather
    than ``None`` — ruamel.yaml returns ``None`` for empty documents, which
    is normalised here.

    Args:
        text: Full document text, including ``---`` delimiters.

    Returns:
        Tuple of ``(frontmatter_dict, body_text)``.  If frontmatter is
        absent or malformed, returns ``({}, text)``.

    Raises:
        ValueError: If a ``---`` opening is found but no closing delimiter
            exists.  A document that starts with ``---`` but has no closing
            ``---`` is structurally broken — callers should log this as a
            violation rather than silently ignoring it.
    """
    if not text.startswith("---"):
        return {}, text

    end = text.find("---", 3)
    if end < 0:
        raise ValueError(
            "Frontmatter block opened with --- but never closed. "
            "Add a closing --- after the YAML block."
        )

    yaml_text = text[3:end].strip()
    body = text[end + 3 :].lstrip("\n")

    if not yaml_text:
        return {}, body

    data = _yaml.load(yaml_text)
    if data is None:
        return {}, body
    if not isinstance(data, dict):
        raise ValueError(
            f"Frontmatter is not a YAML mapping (got {type(data).__name__}). "
            "Check for structural errors in the YAML block."
        )

    return dict(data), body


def extract_meta(path: Path) -> tuple[str, dict]:
    """Extract title and frontmatter dict from a content file.

    Convenience wrapper over ``split_frontmatter`` that also resolves
    the document title: frontmatter ``title`` field first, then the
    first ``# heading`` in the body, then a humanised filename stem.

    This function is the correct entry point for the index generator,
    which needs only the title and lightweight metadata rather than full
    schema validation.

    Args:
        path: Absolute path to the markdown content file.

    Returns:
        Tuple of ``(title, frontmatter_dict)``.  ``title`` is always a
        non-empty string.

    Raises:
        OSError: If the file cannot be read.
    """
    text = path.read_text(encoding="utf-8", errors="replace")

    try:
        meta, body = split_frontmatter(text)
    except ValueError:
        meta = {}
        body = text

    title: str = str(meta.get("title", "")).strip("\"'")
    if not title:
        m = HEADING_RE.search(body)
        title = m.group(1).strip() if m else path.stem.replace("-", " ").title()

    return title, meta
