---
uri: memory/feelingflowingbot
owner: feelingflowingbot
updated: 2026-04-28
description: Flow's project-scoped memory for the Observatory Almanac. Tracks patterns, decisions, and operational context accumulated across sessions.
---

# Flow — Observatory Almanac Memory

Project-scoped memory. Covers what I've learned about this specific project. Global memory lives in `phosphene/woodchipper/memory/feelingflowingbot/`.

---

## Project Identity

**What it is:** A structured git-native mirror of observatory.wiki — an expert-authored knowledge platform run by the Independent Media Institute. The almanac makes OW content indexable, searchable, and deployable as a static site.

**What it is not:** A blog, a CMS, or a content-creation platform. We mirror and curate; we don't author.

**Ed Phil's stake:** Infrastructure architect. Built the skeleton (schema, Python package, scraper). Cares about correctness, axiomatics, and the quality of the engineering as much as the content.

**Jan's stake:** Principal researcher and OW producer. The content is his. The almanac serves his research infrastructure vision. He hasn't been directly in this build — but it's for him.

---

## What I've Learned About This Project

### Scraper behaviour
- OW uses MediaWiki with the Chameleon skin. HTML structure is stable and predictable.
- ~10% of articles have no h2 headings (short excerpts) — Strategy 2 body detection handles them.
- The TOC `div#toc` is 4 levels deep; a simple `.*?</div>` regex terminates at the first inner div. `_strip_div_by_id` counts depth to find the true closing tag.
- Author attribution lives in `div.authors.interface` with a "By <a>" pattern. Some articles only have the plain-text variant (no link).
- Source publication lives in `div.sources.interface`. Absent when OW itself is the publisher — defaults to "The Observatory".
- `Last edited:` in the footer is the only date OW exposes. Not the publication date — the last edit. Good enough.

### Content quality
- OW articles vary in depth: science/history/environment tend to be substantive (1500–3000 words). Health/psychology/philosophy tend to be shorter (500–1200 words).
- Almanac-native content from the source zip is reference material: recipes, game rules, factbooks, navigator guides. It's lower-stakes than OW articles but fills area gaps.
- Summary generation from lede works well (≥30 char threshold). The fallback (title + area) is sometimes weak — worth enriching manually for featured articles.

### Infrastructure patterns
- `uv run` from `lib/python/` is the correct Python invocation. Never bare `python3`.
- `ruamel.yaml` is in the uv venv but not system Python. All scripts that need it must run via `uv run`.
- `build_docs_tree.py` must run after any bulk content addition before `mkdocs serve`/`build`. Creates symlinks — idempotent.
- Symlinks in `docs/areas/` point to absolute paths. They will break if the repo is moved. Acceptable for now.

### Testing discipline
- 115 scraper tests must pass before any scraper change. Run: `cd lib/python && uv run pytest scripts/feelingflowingbot/test_observatory_scraper.py -q`
- 50 almanac lib tests must pass before any schema/validator change. Run: `cd shared/observatory-almanac/lib/python && uv run pytest -q`
- Snapshot tests use real saved OW HTML fixtures in `scripts/feelingflowingbot/fixtures/`. Three articles: debt-forgiveness, bees-sentient, chickens.

---

## Operational Patterns

### Adding OW articles (fast path)
1. Add entry to `meta/import-queue.yml`
2. `cd shared/observatory-almanac && uv run --project ../../lib/python python3 -c "from observatory_scraper import write_article; write_article('<url>', '<area>')"`
3. Verify frontmatter, check author profile was created
4. Commit

### Adding OW articles (bulk)
1. Add entries to `meta/import-queue.yml`
2. `uv run --project lib/python python lib/python/scripts/feelingflowingbot/observatory_scraper.py --bulk`
3. Run validator: `cd shared/observatory-almanac/lib/python && uv run python -m almanac.validator --root ..`

### Schema change protocol
1. Update `SCHEMA.md` (human-readable spec)
2. Update `almanac/src/almanac/schema.py` (Pydantic models)
3. Update tests in `almanac/tests/`
4. Run full test suite
5. Update `meta/SPEC_LOG.md` with decision

### After any bulk content change
1. Run `python scripts/generate_area_indexes.py` — regenerates area index pages
2. Run `python scripts/build_docs_tree.py` — rebuilds symlink tree
3. Run validator
4. Update `meta/CONTEXT_INDEX.md` counts
5. Commit

---

## Things That Went Wrong (and the fixes)

| Problem | Root cause | Fix |
|---------|------------|-----|
| 10 articles with 0 body words | `find_body_start` only had Strategy 1; flat articles have no h2 | Added Strategy 2: first `<p>` after `article-top` |
| TOC content leaking into body | `_strip_div_by_id` stopped at first inner `</div>` | Depth-counter walk to find true matching close tag |
| `<div` fragment at body end | `find_body_end` cut mid-tag | Back up past any unclosed `<` at cut point |
| Bold/italic lost in output | `strip_tags` inside `<p>` handler ran before inline conversion | `_convert_inline` now runs first in pipeline |
| `render_article` broke on titles with colons | f-string YAML doesn't quote | Switched to `ruamel.yaml` serialisation |
| `ALMANAC_ROOT` broke when script moved | `parents[4]` hardcoded depth | Sentinel-file walk (`_find_almanac_root`) |
| `ruamel` import failed in CI validator step | Wrong pip install in wrong directory | Consolidated: `pip install -e lib/python/almanac` handles deps |

---

## Current State (2026-04-28 19:26 UTC)

| Metric | Value |
|--------|-------|
| Total documents | 190 |
| OW articles | 30 |
| Almanac-native | 160 |
| Author profiles | 29 |
| Populated areas | 20 / 26 |
| Scraper tests | 115 passing |
| Almanac lib tests | 50 passing |
| Open tasks | C-003, C-004, I-003, I-004 |

### Empty areas still needing OW articles
`agriculture`, `arts-recreation`, `charter-schools`, `cooking`, `dig-labs`, `education`, `energy`, `food`, `literature`, `media`, `natural-health`, `peoples-movements`, `voting-elections`

---

## Collaborators

**Ed Phil (edphos)** — Systems architect. Sets engineering standards. Calls when things need to be built right. In this project: initiated the build, set all axiomatic constraints, approved all major architectural choices.

**Jan (marsyas6)** — Principal researcher. OW producer. Has not been in this build session but it's built for his research infrastructure.
