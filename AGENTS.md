---
uri: meta/agents
owner: feelingflowingbot
status: living
updated: 2026-04-28
description: Agent specification for the Observatory Almanac — initialization, graduated discovery, content protocols, and safety.
---

# AGENTS.md — Observatory Almanac

Operational specification for agents working in the Observatory Almanac repository. Definitory in style: each section states what a thing IS and what WILL happen.

The almanac now has **native agent infrastructure**: skills, memory, and a spec log live here alongside the content. The parent workspace (`phosphene/woodchipper`) continues to host the scraper, Python tooling, and global memory.

---

## 1. Repository Identity

**Name:** Observatory Almanac  
**Scope:** Structured, git-native mirror of [observatory.wiki](https://observatory.wiki)  
**Producer:** Independent Media Institute  
**License:** CC BY-NC-SA 4.0 (OW content) / MIT (almanac-native content + tooling)  
**Parent workspace:** `phosphene/woodchipper` (scraper, tests, global memory)  
**Almanac root:** `shared/observatory-almanac/` (relative to woodchipper workspace)  
**Published site:** https://ind-media.github.io/observatory-almanac  

---

## 2. Initialization Protocol

One index read, then targeted lookups. Follows **Graduated Discovery (T-043)**.

1. **Load Content Index** → `meta/CONTEXT_INDEX.md`
   YAML frontmatter carries the full asset map with `relevant_when` tags.

2. **Check Task Board** → `meta/TASKS.md`
   Pick the highest-priority `open` task. Mark it `in-progress` before starting.

3. **Task Routing** — filter index by domain before loading:
   - `scraping` → import queue, scraper (in parent workspace)
   - `content` → `SCHEMA.md`, `AREAS.md`, relevant `areas-*` entry
   - `author` → `authors/` directory
   - `schema` → `SCHEMA.md`, `lib/python/almanac/src/almanac/schema.py`
   - `architecture` → `meta/SPEC_LOG.md`

4. **Skill Lookup** → `.agents/skills/almanac-content/SKILL.md`
   Turbo commands, axioms, content standards, area priority queue.

5. **Memory** → `memory/feelingflowingbot.md` (operational patterns, known issues)
   Load when context about prior decisions is needed.

6. **Never scan directories** — use the index. If the index is stale, regenerate it.

---

## 3. Infrastructure Map

```
shared/observatory-almanac/
├── .agents/
│   └── skills/
│       └── almanac-content/SKILL.md  ← native content skill
├── memory/
│   ├── feelingflowingbot.md           ← Flow's project memory
│   └── edphos.md                      ← Ed Phil's project memory
├── meta/
│   ├── CONTEXT_INDEX.md               ← session-start orientation
│   ├── SPEC_LOG.md                    ← architectural decisions (append-only)
│   ├── TASKS.md                       ← task board (E/D/C/I tracks)
│   └── import-queue.yml               ← OW article scrape queue
├── areas/                             ← content by area
├── authors/                           ← author profiles
├── guides/                            ← curated multi-article collections
├── lib/python/almanac/                ← Pydantic schema + validator + index generator
├── scripts/
│   ├── generate_area_indexes.py       ← area index pages
│   └── build_docs_tree.py             ← docs/ symlink tree for MkDocs
├── docs/                              ← MkDocs source (symlinks to areas/)
├── SCHEMA.md                          ← human-readable content spec
├── AREAS.md                           ← 26 canonical area slugs
└── .github/workflows/deploy.yml       ← GitHub Pages CI
```

**Scraper lives in parent workspace:**
```
phosphene/woodchipper/
└── lib/python/scripts/feelingflowingbot/
    ├── observatory_scraper.py
    ├── test_observatory_scraper.py
    └── test_observatory_scraper_snapshot.py
```

---

## 4. Content Architecture

### 4.1 Document Types

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

### 4.2 Canonical Identifiers

Every document has a stable compound identity:

```
{area}/{slug}   →  areas/science/why-scientists-are-still-puzzled-by-consciousness.md
authors/{slug}  →  authors/leslie-alan-horvitz.md
guides/{slug}   →  guides/guide-to-artificial-intelligence.md
```

Slugs are **permanent**. Derived from OW URL path via `slugify()`. Do not rename.

### 4.3 Area Taxonomy

26 canonical areas defined in `AREAS.md`. Do not create new areas — map to existing ones.

---

## 5. Content Protocols

### 5.1 Adding OW Articles

1. Add to `meta/import-queue.yml`
2. Run scraper (see Skill T1/T2)
3. Verify frontmatter matches `SCHEMA.md`
4. Confirm author profile exists
5. Run `python scripts/generate_area_indexes.py && python scripts/build_docs_tree.py`
6. Commit with task ID

### 5.2 Frontmatter Standards (Non-Negotiable)

- `title`: exact title from observatory.wiki
- `area`: canonical slug from `AREAS.md`
- `type`: declared document type
- `author`: display name as credited on OW
- `author_slug`: must match filename stem in `authors/`
- `source_url`: canonical observatory.wiki URL
- `license`: `CC BY-NC-SA 4.0` for OW content; `MIT` for almanac-native
- `published`: ISO 8601 date
- `summary`: 1–3 sentences; written for the reader
- `tags`: lowercase-hyphens; conceptual, not area names

### 5.3 Body Content

- Preserve original section structure
- Do not editorialize — body is the article
- Attribution line mandatory at document end:
  ```markdown
  *Originally published at [observatory.wiki](…). © Independent Media Institute. Licensed [CC BY-NC-SA 4.0](…).*
  ```

### 5.4 Author Profiles

- One file per author in `authors/<slug>.md`
- Scraper auto-creates stubs
- `the-observatory` slug is exempt (collective attribution)

---

## 6. Schema & Validation

**Schema:** `SCHEMA.md` (human-readable) + `lib/python/almanac/src/almanac/schema.py` (Pydantic)

**Validation:**
```bash
cd lib/python && uv run python -m almanac.validator --root ..
```

**Test suite:**
```bash
cd lib/python && uv run pytest -q   # 50 tests
```

**Schema change protocol:**
1. Update `SCHEMA.md`
2. Update Pydantic models in `schema.py`
3. Update tests
4. Add decision to `meta/SPEC_LOG.md`
5. Commit with `SPEC-NNN` reference

---

## 7. Graduated Discovery

| Tier | Asset | Load When |
|------|-------|-----------|
| T1 | `meta/CONTEXT_INDEX.md` | Every session start |
| T2 | `SCHEMA.md`, `AREAS.md` | Schema/content questions |
| T3 | `meta/SPEC_LOG.md` | Architecture decisions |
| T4 | `areas/<area>/` | Area-specific work |
| T5 | Individual article files | Targeted content edits |

**Rule:** Read T1 first, always. Load T2–T5 only when the task demands it.

---

## 8. Safety

- **Do not modify CC-licensed body content** — preserve original text; formatting normalisation only
- **Do not create articles from non-OW sources** without explicit instruction
- **Do not delete articles** without explicit instruction
- **Slugs are permanent** — renaming breaks all external references silently
- **Rate limit is immutable** — 0.8s between OW requests

---

## 9. Parent Workspace Relationship

| Concern | Location |
|---------|----------|
| Global memory / daily logs | `phosphene/woodchipper/memory/feelingflowingbot/` |
| Project memory | `shared/observatory-almanac/memory/` |
| Woodchipper skills | `phosphene/woodchipper/.agents/skills/observatory-almanac/` |
| Almanac native skills | `shared/observatory-almanac/.agents/skills/` |
| Scraper + tests | `phosphene/woodchipper/lib/python/scripts/feelingflowingbot/` |
| Woodchipper spec log | `phosphene/woodchipper/team/SPEC_LOG.md` |
| Almanac spec log | `shared/observatory-almanac/meta/SPEC_LOG.md` |
| Tickets / OKRs | `phosphene/woodchipper/team/` |
