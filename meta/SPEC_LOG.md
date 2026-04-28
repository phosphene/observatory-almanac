---
uri: meta/spec-log
owner: feelingflowingbot
updated: 2026-04-28
description: Architectural decision log for the Observatory Almanac. Every significant design choice recorded here with rationale. Append-only — do not edit past entries.
---

# Observatory Almanac — Spec Log

Append-only architectural decision register. Format: `[SPEC-NNN]` sequential ID, date, decision, rationale, consequences.

---

## SPEC-001 — Repository is content-only; agent infrastructure in parent workspace
**Date:** 2026-04-28  
**Decision:** The almanac repository is a content surface. All agent logic (skills, scraper, tests, memory) lives in `phosphene/woodchipper`. The almanac repo contains only content files, schema, and the minimal Python package needed to validate that content.  
**Rationale:** Keeps the almanac repo clean and deployable (just `mkdocs build`). No agent tooling leaks into the published site. Skills and scraper can evolve without touching the content repo.  
**Consequences:** Agents need both repos checked out. A session working on almanac content must also have woodchipper available for the scraper. Scripts reference back to woodchipper via `ALMANAC_ROOT` discovery.  
**Status:** Superseded by SPEC-018 (skills and memory now live in almanac repo too).

---

## SPEC-002 — Slugs are stable identifiers
**Date:** 2026-04-28  
**Decision:** Once written, a document slug is never changed. Slugs are derived from the original OW URL path using `slugify()`.  
**Rationale:** Slugs are the primary stable address for content. External links, search indexes, and the author profile `articles` list all reference them. Renaming breaks the reference chain silently.  
**Consequences:** A typo in a slug is permanent. The `slugify()` function is authoritative — fix it there, not in the filename.  
**Status:** Active.

---

## SPEC-003 — Two license tracks: CC BY-NC-SA 4.0 and MIT
**Date:** 2026-04-28  
**Decision:** OW-scraped content is `CC BY-NC-SA 4.0` (IMI's upstream license, not negotiable). All almanac-native content (reference material, recipes, rulebooks, factbooks, assessments) is `MIT`.  
**Rationale:** MIT imposes no share-alike restriction on downstream software integrations (Telegram bot, PWA, RAG pipeline). CC BY-NC-SA is required to comply with IMI's reuse terms for OW articles.  
**Consequences:** `LicenseType` enum has exactly two values. Any new document type must declare which license applies.  
**Status:** Active.

---

## SPEC-004 — `parse_article` returns `ParsedArticle` frozen dataclass, not dict
**Date:** 2026-04-28  
**Decision:** `parse_article()` returns a `ParsedArticle` frozen `@dataclass` rather than an untyped `dict`.  
**Rationale:** Typed access surfaces attribute errors at development time rather than KeyError at runtime. `frozen=True` ensures parse output is immutable — callers must use `dataclasses.replace()` to produce modified copies, forcing changes through the same field definitions.  
**Consequences:** All callers updated to attribute access (`article.title`). `render_article()` accepts `ParsedArticle`. Tests use attribute access throughout.  
**Note:** `ParsedArticle` is a `dataclass` not a Pydantic model — it is scraper output (untrusted), not schema-validated content. Pydantic lives in `almanac.schema` for the validate-at-write boundary.  
**Status:** Active.

---

## SPEC-005 — `render_article` uses `ruamel.yaml` for frontmatter serialisation
**Date:** 2026-04-28  
**Decision:** Frontmatter YAML is produced via `ruamel.yaml`, not f-string construction.  
**Rationale:** f-string YAML breaks on titles containing colons, quotation marks, or non-ASCII characters. `ruamel.yaml` handles all cases correctly and quotes values that need it (e.g., ISO date strings).  
**Consequences:** Frontmatter format changed slightly: dates are quoted (`'2024-01-15'`), tag lists use block style (`- science`). All tests updated.  
**Status:** Active.

---

## SPEC-006 — `ALMANAC_ROOT` discovered via sentinel-file walk
**Date:** 2026-04-28  
**Decision:** `ALMANAC_ROOT` is found by walking up to 8 parent directories looking for `shared/observatory-almanac/SCHEMA.md`. Replaces `Path(__file__).parents[4]`.  
**Rationale:** `parents[4]` is a fragile depth-count that breaks if the script moves. Sentinel-file discovery is location-independent.  
**Consequences:** `RuntimeError` with diagnostic message if the sentinel is not found. Never silent.  
**Status:** Active.

---

## SPEC-007 — `PRIORITY_ARTICLES` externalised to `meta/import-queue.yml`
**Date:** 2026-04-28  
**Decision:** The OW article import queue lives in `shared/observatory-almanac/meta/import-queue.yml`, not hardcoded in the scraper Python source.  
**Rationale:** Adding a new article to the scrape queue should not require editing Python. The YAML file is editable by non-developers and is version-controlled in the content repo alongside the content it produces.  
**Consequences:** `_load_import_queue()` reads the file at runtime via `ruamel.yaml`. `run_bulk()` calls it. If the file is absent, returns empty list (non-fatal).  
**Status:** Active.

---

## SPEC-008 — `html_to_markdown` is a named pipeline, not a monolith
**Date:** 2026-04-28  
**Decision:** `html_to_markdown()` chains five named pure functions: `_strip_chrome`, `_convert_inline`, `_convert_block_elements`, `_convert_links`, `_normalise_whitespace`.  
**Rationale:** The monolithic version had an ordering constraint (inline before block) that was invisible — it was just a comment. Named stages make the constraint structurally explicit: each stage's docstring explains what must come before it and why. Each stage is independently testable.  
**Consequences:** Public API unchanged. If OW changes their skin, only the affected stage needs updating.  
**Status:** Active.

---

## SPEC-009 — `_convert_inline` must precede `_convert_block_elements`
**Date:** 2026-04-28  
**Decision:** Inline formatting (`<strong>`, `<em>`) must be converted to Markdown before paragraph handlers run.  
**Rationale:** The paragraph handler calls `strip_tags()` on the `<p>` content. If `<strong>` tags are still present when `strip_tags` runs, they are destroyed and the bold text becomes plain text. Converting inline first means `**...**` markers survive into the output.  
**Consequences:** This ordering is enforced by the pipeline structure. Any restructuring of the pipeline must respect this dependency.  
**Status:** Active.

---

## SPEC-010 — `split_frontmatter` raises on unclosed blocks
**Date:** 2026-04-28  
**Decision:** `almanac.parsing.split_frontmatter()` raises `ValueError` if a `---` opening is found but no closing `---` exists. Does not return an empty dict.  
**Rationale:** An unclosed frontmatter block is structural damage — the document is broken. Silent failure (returning `{}`) would let a broken document pass the validator with all fields missing. A loud error forces the agent to investigate.  
**Consequences:** Callers must handle `ValueError`. The validator wraps it in a validation error with the file path.  
**Status:** Active.

---

## SPEC-011 — `almanac.parsing` is the single frontmatter extraction surface
**Date:** 2026-04-28  
**Decision:** All frontmatter parsing in the almanac Python package goes through `almanac.parsing.split_frontmatter()` and `almanac.parsing.extract_meta()`. `validator.py` and `index.py` both delegate here.  
**Rationale:** Both modules had grown independent implementations of the same logic with subtle differences. A single module with documented behaviour eliminates drift.  
**Consequences:** `extract_frontmatter_yaml()` in `validator.py` is now a thin wrapper that adapts the error message — kept for backward compatibility.  
**Status:** Active.

---

## SPEC-012 — `docs_dir: docs`, not `docs_dir: .`
**Date:** 2026-04-28  
**Decision:** MkDocs is configured with `docs_dir: docs`. Content in `areas/` and `authors/` is symlinked into `docs/areas/` and `docs/authors/` by `scripts/build_docs_tree.py`.  
**Rationale:** `docs_dir: .` exposes the entire repo root to MkDocs. Any new file at root (AGENTS.md, NOTES.md, etc.) leaks into the published site. The `exclude_docs` blocklist required to compensate would grow without bound.  
**Consequences:** `build_docs_tree.py` must run before `mkdocs build`. CI workflow includes it. Local development also needs it (run once after a fresh checkout).  
**Status:** Active.

---

## SPEC-013 — `mkdocs-awesome-pages-plugin` for nav ordering
**Date:** 2026-04-28  
**Decision:** Use `mkdocs-awesome-pages-plugin` instead of a hand-authored `nav:` block in `mkdocs.yml`.  
**Rationale:** A hand-authored `nav:` must be updated every time an article is added. With 190+ documents across 26 areas this is unworkable. `awesome-pages` reads `.pages` files in each area directory, giving per-area ordering control without a central nav manifest.  
**Consequences:** `build_docs_tree.py` writes `.pages` files for each area. `requirements-docs.txt` includes `mkdocs-awesome-pages-plugin>=2.9`.  
**Status:** Active.

---

## SPEC-014 — `git-revision-date-localized` with `fallback_to_build_date: true`
**Date:** 2026-04-28  
**Decision:** `fallback_to_build_date: true` is permanently enabled in `mkdocs.yml`.  
**Rationale:** The plugin raises `GitCommandError` on files with no reachable commit history in shallow clones. CI uses `fetch-depth: 0` to mitigate this, but that could change. The fallback is a second safety net that costs nothing.  
**Consequences:** If CI ever reverts to a shallow clone, dates will show the build date rather than breaking the deploy. Documented in `mkdocs.yml` comment.  
**Status:** Active.

---

## SPEC-015 — `frozen=True, extra='forbid'` on all Pydantic models
**Date:** 2026-04-28  
**Decision:** All Pydantic schema models in `almanac.schema` use `frozen=True, extra='forbid'`.  
**Rationale:** `frozen=True` — models are immutable; callers use `model_copy(update=...)` for modifications. `extra='forbid'` — unknown frontmatter fields are a schema violation (likely a typo or migration artifact) and should fail loudly.  
**Consequences:** Any new frontmatter field requires a model update. This is intentional — schema drift is visible rather than silent.  
**Status:** Active.

---

## SPEC-016 — `the-observatory` author slug is exempt from profile requirement
**Date:** 2026-04-28  
**Decision:** Articles authored by `The Observatory` (author_slug = `the-observatory`) do not require an author profile in `authors/`.  
**Rationale:** "The Observatory" is a collective attribution, not an individual author. Creating a profile file would be misleading.  
**Consequences:** `ensure_author()` checks for this slug and skips. `validate_author_refs()` has explicit exemption.  
**Status:** Active.

---

## SPEC-017 — `find_body_start` uses two strategies
**Date:** 2026-04-28  
**Decision:** Body start detection tries two strategies in order:
1. **Sectioned:** first `h2.mw-headline` that isn't TOC; back up to nearest `<p>` within 5000 bytes
2. **Flat/excerpt:** first `<p>` after `div#article-top` closes  
**Rationale:** Strategy 1 fails (returns -1) for ~10% of OW articles that have no h2 section headings. These are short pieces, excerpts, or essays. Strategy 2 recovers the full body for all of them.  
**Consequences:** The 10 thin-body articles from the initial batch have been re-scraped and all now have full body content.  
**Status:** Active.

---

## SPEC-018 — Almanac repo now has native agent infrastructure
**Date:** 2026-04-28  
**Decision:** The almanac repo has its own `.agents/skills/`, `memory/`, and `meta/SPEC_LOG.md`. It is no longer purely a content surface delegating all agent logic to the parent workspace.  
**Rationale:** As the project matures, project-specific skills and contextual memory are better co-located with the content they govern. Agents working exclusively in the almanac repo shouldn't need woodchipper context for routine content tasks.  
**Consequences:** AGENTS.md updated to reflect this. Woodchipper skills file remains as the infrastructure/scraper skill. Almanac skills cover content operations. Memory files in `memory/` capture project-specific context for each collaborator.  
**Supersedes:** SPEC-001 (partial — content-only surface is no longer accurate).  
**Status:** Active.
