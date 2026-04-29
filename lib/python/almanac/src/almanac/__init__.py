"""Observatory Almanac — Python tooling library.

Provides schema validation, content indexing, and MkDocs site generation
for the Observatory Almanac repository.

Three public subsystems:

- ``almanac.schema`` — Pydantic models for every document type defined in
  SCHEMA.md.  The models are the authoritative, machine-readable form of
  the schema specification; validation is a corollary, not the primary aim.

- ``almanac.validator`` — Walks the content tree, applies schema models,
  and reports structural violations.  Exit-code-safe for CI.

- ``almanac.index`` — Generates ``meta/CONTEXT_INDEX.md`` and the content
  inventory from the live content tree.  Designed to be run as a nightly
  heartbeat task or on every bulk content change.
"""

__version__ = "0.1.0"
