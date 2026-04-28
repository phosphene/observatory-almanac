---
uri: meta/agents
owner: feelingflowingbot
status: living
updated: 2026-04-28
description: Agent specification for the Observatory Almanac — initialization, graduated discovery, content protocols, and safety.
---

# AGENTS.md — Observatory Almanac

Operational specification for agents working in the Observatory Almanac repository. Definitory in style: each section states what a thing IS and what WILL happen, not merely instructions.

Backwards-compatible with the Phosphene workspace AGENTS.md. The parent workspace (`phosphene/woodchipper`) governs memory, skills, and infrastructure. This file governs Almanac-specific content protocols.

---

## 1. Repository Identity

**Name:** Observatory Almanac
**Scope:** Structured, git-native mirror of [observatory.wiki](https://observatory.wiki)
**Producer:** Independent Media Institute
**License:** CC BY-NC-SA 4.0 (content) / MIT (tooling)
**Parent workspace:** `phosphene/woodchipper` (agents, skills, memory, infrastructure)
**Almanac root:** `shared/observatory-almanac/` (relative to woodchipper workspace)

---

## 2. Initialization Protocol

One index read, then targeted lookups. Follows **Graduated Discovery (T-043)**.

1. **Load Content Index** → `meta/CONTEXT_INDEX.md`
   YAML frontmatter carries the full asset map with `relevant_when` tags.

2. **Check Today's Activity** — what areas/articles have been touched recently?
   ```python
   active_keys = [k for k, v in idx.items() if "content" in v["relevant_when"]]
   ```

3. **Task Routing** — filter index by domain before loading:
   - `scraping` → `meta/CONTEXT_INDEX.md#scraper`
   - `content` → `meta/CONTEXT_INDEX.md#areas`
   - `author` → `meta/CONTEXT_INDEX.md#authors`
   - `schema` → `SCHEMA.md`, `AREAS.md`

4. **Skill Lookup** — match task trigger, load only the matched `SKILL.md`.
   Skills live at `../../.agents/skills/observatory-almanac/SKILL.md`
   (relative to almanac root = `shared/observatory-almanac/`).

5. **Never scan directories** — use the index. If the index is stale, regenerate it.

---

## 3. Content Architecture

### 3.1 Document Types

| Type | Location | Schema |
|------|----------|--------|
| Article | `areas/<area>/<slug>.md` | `SCHEMA.md#article` |
| Guide | `guides/<slug>.md` | `SCHEMA.md#guide` |
| Author profile | `authors/<slug>.md` | `SCHEMA.md#author` |
| Area index | `areas/<area>/index.md` | auto-generated |
| Meta | `meta/` | internal |

### 3.2 Canonical Identifiers

Every document has a stable compound identity:

```
{area}/{slug}   →  areas/science/why-scientists-are-still-puzzled-by-consciousness.md
authors/{slug}  →  authors/leslie-alan-horvitz.md
guides/{slug}   →  guides/guide-to-artificial-intelligence.md
```

Slugs are derived deterministically from the observatory.wiki URL path using the `slugify()` function in the scraper. Do not rename slugs without a migration plan — they are stable identifiers referenced across metadata.

### 3.3 Area Taxonomy

26 canonical areas defined in `AREAS.md`. Area slugs are stable. Do not create new areas — map to existing ones.

---

## 4. Content Protocols

### 4.1 Adding Articles

1. Use the scraper: `uv run python lib/python/scripts/feelingflowingbot/observatory_scraper.py <url> [area]`
2. Verify frontmatter matches `SCHEMA.md` — title, area, author, published, summary, tags.
3. Ensure author profile exists in `authors/<author-slug>.md`.
4. Update `meta/index.md` if it is maintained manually.

### 4.2 Frontmatter Standards (Non-Negotiable)

- `title`: exact title from observatory.wiki, quoted in YAML
- `area`: canonical slug from `AREAS.md`
- `type`: `article`, `guide`, or `classic`
- `author`: display name as credited
- `author_slug`: must match filename stem in `authors/`
- `source_url`: canonical observatory.wiki URL
- `license`: always `CC BY-NC-SA 4.0`
- `published`: ISO 8601 date
- `summary`: 1–3 sentences; written for the reader, not scraped verbatim
- `tags`: lowercase-hyphens; conceptual, not area names

### 4.3 Body Content

- Preserve original section structure (headings, lists)
- Do not editorialize; body is the article
- Attribution line at the very end (mandatory):
  ```markdown
  *Originally published at [observatory.wiki](…). © Independent Media Institute. Licensed [CC BY-NC-SA 4.0](…).*
  ```

### 4.4 Author Profiles

- One file per author in `authors/<slug>.md`
- Scraper creates stubs automatically
- Enrich with bio and article list when content volume justifies it

---

## 5. Graduated Discovery

The almanac uses the same Graduated Discovery protocol as the parent workspace (T-043).

### Discovery Tiers

| Tier | Asset | When |
|------|-------|------|
| T1 | `meta/CONTEXT_INDEX.md` | Every session start |
| T2 | `SCHEMA.md`, `AREAS.md` | Content schema questions |
| T3 | `areas/<area>/` directory | Area-specific work |
| T4 | Individual article files | Targeted content edits |

**Rule:** Read T1 first, always. Load T2–T4 only when the task demands it.

### Index Maintenance

`meta/CONTEXT_INDEX.md` is the orientation surface. Keep it current:
- Add entries when new asset types are created
- Update `updated:` when content changes significantly
- Run the index generator when the scraper adds a bulk batch

---

## 6. Scraper Infrastructure

The scraper lives in the parent workspace:

```
lib/python/scripts/feelingflowingbot/observatory_scraper.py
```

Tests are co-located:
```
lib/python/scripts/feelingflowingbot/test_observatory_scraper.py
```

Run tests before any scraper modification:
```bash
cd lib/python && uv run pytest scripts/feelingflowingbot/test_observatory_scraper.py -v
```

The scraper respects a 0.8s delay between requests. Do not reduce this.

---

## 7. Safety

- **Do not modify CC-licensed content** — preserve original text; only formatting normalisation is permitted
- **Do not create articles from non-observatory.wiki sources** without explicit instruction
- **Do not delete articles** without explicit instruction; git history is the safety net
- **Slugs are stable** — changing a slug breaks any external reference to that article

---

## 8. Relationship to Parent Workspace

| Concern | Where it lives |
|---------|---------------|
| Memory / daily logs | `phosphene/woodchipper/memory/` |
| Skills | `phosphene/woodchipper/.agents/skills/observatory-almanac/` |
| Scraper + tests | `phosphene/woodchipper/lib/python/scripts/feelingflowingbot/` |
| Almanac content | `phosphene/woodchipper/shared/observatory-almanac/` (this repo) |
| Tickets / decisions | `phosphene/woodchipper/team/SPEC_LOG.md` |

The Almanac repo has no agent infrastructure of its own — it is the content surface. All agent logic lives in the parent workspace.
