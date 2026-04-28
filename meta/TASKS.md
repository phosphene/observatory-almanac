---
uri: meta/tasks
owner: feelingflowingbot
updated: 2026-04-28
description: Task tracking for the Observatory Almanac repository. Covers engineering, content, and infrastructure work.
---

# Observatory Almanac — Task Board

Agent-readable task register. One row per task. Status updated in-place.

**Statuses:** `open` · `in-progress` · `done` · `blocked` · `deferred`
**Priorities:** `P0` critical · `P1` high · `P2` medium · `P3` low

---

## Engineering

| ID | Priority | Status | Title | Notes |
|----|----------|--------|-------|-------|
| E-001 | P1 | `done` | `parse_article` returns untyped `dict` — replace with `ParsedArticle` dataclass | Affects scraper, tests, render pipeline |
| E-002 | P1 | `done` | `extract_frontmatter_yaml` duplicated in `validator.py` and `index.py` | Extract to `almanac.parsing` shared module |
| E-003 | P1 | `done` | `docs_dir: .` antipattern — fix MkDocs to use `docs/` + `gen-files` or `awesome-pages` | `articles: dir/` nav syntax also invalid without the plugin |
| E-004 | P2 | `done` | `ALMANAC_ROOT` uses fragile `parents[4]` depth arithmetic | Replace with sentinel-file discovery |
| E-005 | P2 | `done` | `render_article` builds YAML frontmatter via f-string | Serialize via `ruamel.yaml` to handle special chars safely |
| E-006 | P2 | `done` | `PRIORITY_ARTICLES` URLs hardcoded in Python source | Externalize to `meta/import-queue.yml` |
| E-007 | P3 | `done` | `html_to_markdown` is a monolithic 60-line sequential transform | Decompose into named composable transform functions |
| E-008 | P3 | `done` | `git-revision-dates-localized-plugin` misleading with shallow CI checkout | Document or remove fallback behaviour |

---

## Documentation / Docstrings

| ID | Priority | Status | Title | Notes |
|----|----------|--------|-------|-------|
| D-001 | P2 | `done` | `observatory_scraper.py` module docstring — functional not literate | Add rationale for two-strategy body detection, depth-aware stripping |
| D-002 | P2 | `done` | `_strip_div_by_id` — missing domain context (MediaWiki TOC structure) | Name the failure mode concretely |
| D-003 | P2 | `done` | `DocumentType` enum values lack individual docstrings | Explain when each type applies and how it differs from neighbours |
| D-004 | P2 | `done` | `AlmanacBase` missing evolutionary pattern documentation | Add `model_copy(update=...)` pattern to docstring |
| D-005 | P3 | `done` | `parse_article` docstring — doesn't explain extraction hierarchy or failure modes | |
| D-006 | P3 | `done` | `LicenseType` — explain WHY MIT vs CC BY-NC-SA, not just WHAT | |
| D-007 | P3 | `done` | `GuideFrontmatter.type_must_be_guide` — tautological error message | Explain why the discriminator check exists |

---

## Content

| ID | Priority | Status | Title | Notes |
|----|----------|--------|-------|-------|
| C-001 | P1 | `done` | Expand OW articles in empty high-priority areas | health(4), psychology(4), philosophy(4), world-affairs(2), language(5) |
| C-002 | P2 | `done` | Monthly stats files mis-mapped to `health/` | Verified: no monthly files present; non-issue |
| C-003 | P2 | `open` | 11 OW taxonomy areas entirely empty | agriculture, charter-schools, dig-labs, education, energy, food, literature, media, natural-health, peoples-movements, voting-elections |
| C-004 | P3 | `open` | Author profiles sparse (21 profiles, minimal bios) | Enrich with credentials and publication history |

---

## Infrastructure

| ID | Priority | Status | Title | Notes |
|----|----------|--------|-------|-------|
| I-001 | P2 | `done` | GitHub Actions deploy untested end-to-end | deploy.yml overhauled: build_docs_tree step, --strict mkdocs, comments |
| I-002 | P2 | `done` | Index generator not wired to CI | generate_area_indexes.py + build_docs_tree.py both in deploy workflow |
| I-003 | P3 | `open` | Social cards (Open Graph images) not configured | Material `social` plugin + privacy plugin for Google Fonts GDPR |
| I-004 | P3 | `open` | Validator exit codes not surfaced in CI output | `continue-on-error: true` hides violations; consider a violation report artifact |

---

## How to use this file

Agents: read this file at session start when working on the almanac. Pick the highest-priority `open` task. Update status to `in-progress` before starting, `done` when complete. Add a note if blocked.

Commits: reference the task ID in commit messages — `fix(E-001): ParsedArticle dataclass`.
