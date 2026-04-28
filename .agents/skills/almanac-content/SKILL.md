---
uri: skills.almanac/almanac-content
trigger: observatory almanac | almanac content | almanac article | scrape OW | add article | OW import
owner: feelingflowingbot
updated: 2026-04-28
description: Content operations for the Observatory Almanac — scraping, writing, auditing, and expanding OW coverage.
---

# Almanac Content Skill

## Axioms

1. **Index First.** Every session starts with `meta/CONTEXT_INDEX.md`. Load it once. Then filter by task. Never scan directories.
2. **Slugs Are Permanent.** Once written, a slug is never changed. It's a stable address. A typo is forever.
3. **Mirror, Don't Editorialize.** Body content is the article. Preserve OW's original structure and text. No rewriting.
4. **Prove Before Expanding.** Run `cd lib/python && uv run pytest scripts/feelingflowingbot/ -q` before any scraper change. 115 tests must pass.
5. **Rate Limit Is Sacred.** `FETCH_DELAY = 0.8s` — never reduce. OW is a small publisher.
6. **License Tracks Are Distinct.** OW content = `CC BY-NC-SA 4.0`. Almanac-native = `MIT`. Do not mix.
7. **Attribution Is Mandatory.** Every OW article ends with the CC attribution line.
8. **Schema Is the Contract.** Unknown frontmatter fields fail validation. Add fields to the schema first, then to content.

---

## Init Protocol

```python
# 1. Load orientation index
read("meta/CONTEXT_INDEX.md")

# 2. Filter by task
# content  → load schema, areas
# scraping → load scraper, import queue
# audit    → load meta/index.md (if current)
# spec     → load meta/SPEC_LOG.md

# 3. Check task board
read("meta/TASKS.md")  # pick highest-priority open task
```

---

## Turbo Commands

### T1 — Scrape one article
```bash
cd /path/to/shared/observatory-almanac
uv run --project ../../lib/python python3 -c "
import sys; sys.path.insert(0, '../../lib/python/scripts/feelingflowingbot')
from observatory_scraper import write_article
write_article('https://observatory.wiki/ARTICLE_TITLE', 'area-slug')
"
```

### T2 — Bulk scrape from import queue
```bash
uv run --project ../../lib/python python ../../lib/python/scripts/feelingflowingbot/observatory_scraper.py --bulk
```

### T3 — Validate all content
```bash
cd lib/python && uv run python -m almanac.validator --root ..
```

### T4 — Run scraper tests
```bash
cd ../../lib/python && uv run pytest scripts/feelingflowingbot/test_observatory_scraper.py scripts/feelingflowingbot/test_observatory_scraper_snapshot.py -q
```

### T5 — Run almanac lib tests
```bash
cd lib/python && uv run pytest -q
```

### T6 — Regenerate area indexes
```bash
python scripts/generate_area_indexes.py
```

### T7 — Rebuild docs symlink tree
```bash
python scripts/build_docs_tree.py
```

### T8 — Serve site locally
```bash
pip install -r requirements-docs.txt
python scripts/build_docs_tree.py
mkdocs serve
```

### T9 — Add article to import queue
Edit `meta/import-queue.yml`:
```yaml
  - url: https://observatory.wiki/Article_Title
    area: area-slug
```
Then run T2.

### T10 — Check area coverage
```bash
for area in areas/*/; do echo "$area: $(ls $area/*.md 2>/dev/null | grep -v index.md | wc -l) articles"; done
```

---

## Content Standards Quick Reference

### Article frontmatter (OW-scraped)
```yaml
---
title: "Exact Title From OW"
area: science
type: article
author: Author Name
author_slug: author-name
source: Publication Name
source_url: https://observatory.wiki/Article_Title
license: CC BY-NC-SA 4.0
published: '2024-01-15'
updated: '2024-01-15'
summary: 1–3 sentences for the reader. Not a lede copy.
tags:
  - topic-one
  - topic-two
---
```

### Attribution line (mandatory, end of every OW article)
```markdown
---
*Originally published at [observatory.wiki](https://observatory.wiki/Article_Title). © Independent Media Institute. Licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
```

### Author profile (minimum)
```yaml
---
uri: authors/author-slug
name: Author Name
author_slug: author-slug
bio: ""
articles: []
---
```

---

## Area Priority Queue

### High priority (empty, high OW coverage)
- `world-affairs` — geopolitics, foreign policy, international relations
- `education` — K-12, higher ed, learning theory
- `media` — journalism, press freedom, media literacy
- `energy` — renewable energy, fossil fuels, policy
- `dig-labs` — investigative journalism, data reporting

### Medium priority (empty, moderate OW coverage)
- `agriculture` — food systems, farming, soil
- `food` — food sovereignty, nutrition policy
- `peoples-movements` — labour, civil rights, organising
- `voting-elections` — democracy, electoral systems, voter rights
- `literature` — criticism, classic texts, public domain

### Low priority (niche)
- `charter-schools` — education policy subset
- `natural-health` — integrative medicine
- `arts-recreation` — culture, leisure

---

## Schema Reference

| Type | Location | License |
|------|----------|---------|
| `article` | `areas/<area>/<slug>.md` | CC BY-NC-SA 4.0 |
| `classic` | `areas/<area>/<slug>.md` | CC BY-NC-SA 4.0 |
| `guide` | `guides/<slug>.md` | CC BY-NC-SA 4.0 |
| `almanac` | `areas/<area>/<slug>.md` | MIT |
| `recipe` | `areas/cooking/<slug>.md` | MIT |
| `rulebook` | `areas/<area>/<slug>.md` | MIT |
| `factbook` | `areas/<area>/<slug>.md` | MIT |
| `reference` | `areas/<area>/<slug>.md` | MIT |
| `assessment` | `areas/<area>/<slug>.md` | MIT |
| `field-guide` | `areas/<area>/<slug>.md` | MIT |

Full schema: `SCHEMA.md`  
Full areas list: `AREAS.md`  
Pydantic models: `lib/python/almanac/src/almanac/schema.py`

---

## After Any Bulk Content Addition

1. `python scripts/generate_area_indexes.py` — area index pages
2. `python scripts/build_docs_tree.py` — symlink tree
3. `cd lib/python && uv run python -m almanac.validator --root ..` — validate
4. Update `meta/CONTEXT_INDEX.md` counts
5. Update `meta/TASKS.md` task statuses
6. Commit with task ID in message

---

## Key Files

| File | Purpose |
|------|---------|
| `meta/CONTEXT_INDEX.md` | Session-start orientation, asset map |
| `meta/SPEC_LOG.md` | Architectural decision log |
| `meta/TASKS.md` | Task board (E/D/C/I tracks) |
| `meta/import-queue.yml` | OW article scrape queue |
| `SCHEMA.md` | Human-readable content format spec |
| `AREAS.md` | 26 canonical area slugs |
| `lib/python/almanac/` | Pydantic schema + validator + index generator |
| `scripts/generate_area_indexes.py` | Area index page generator |
| `scripts/build_docs_tree.py` | docs/ symlink tree builder |
| `.github/workflows/deploy.yml` | GitHub Pages CI pipeline |
