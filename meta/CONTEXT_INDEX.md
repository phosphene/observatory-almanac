---
uri: meta/context-index
owner: feelingflowingbot
updated: 2026-04-28
description: Session-start orientation index for the Observatory Almanac. Load this first; filter by relevant_when tag; load only what the task needs.

index:
  agents:
    path: AGENTS.md
    description: Agent initialization protocol, content standards, safety rules
    relevant_when: [session-start, schema, safety, architecture]

  schema:
    path: SCHEMA.md
    description: Canonical format spec for articles, guides, and author profiles
    relevant_when: [session-start, schema, content, scraping]

  areas:
    path: AREAS.md
    description: 26 canonical area slugs and their directory mapping
    relevant_when: [session-start, schema, content, scraping]

  content-index:
    path: meta/index.md
    description: Human-readable content inventory (articles, guides, authors)
    relevant_when: [session-start, content, audit]

  readme:
    path: README.md
    description: Project overview and structure
    relevant_when: [session-start, onboarding]

  scraper:
    path: ../../lib/python/scripts/feelingflowingbot/observatory_scraper.py
    description: Scraper logic (pure functions + I/O). Read when modifying or debugging fetch/parse/render.
    relevant_when: [scraping, debug]

  scraper-tests:
    path: ../../lib/python/scripts/feelingflowingbot/test_observatory_scraper.py
    description: 78-test suite covering all pure logic functions. Run before any scraper change.
    relevant_when: [scraping, testing]

  skill:
    path: ../../.agents/skills/observatory-almanac/SKILL.md
    description: Skill file with turbo commands, axioms, and session patterns for almanac work
    relevant_when: [session-start, scraping, content]

  areas-science:
    path: areas/science/
    description: Science area — biology, archaeology, consciousness, paleoanthropology
    relevant_when: [content, science]

  areas-environment:
    path: areas/environment/
    description: Environment area — climate, biodiversity, pollution, oceans
    relevant_when: [content, environment]

  areas-history:
    path: areas/history/
    description: History area — ancient civilizations, archaeology, political history
    relevant_when: [content, history]

  areas-economy:
    path: areas/economy/
    description: Economy area — inequality, labor, debt, political economy
    relevant_when: [content, economy]

  areas-animals:
    path: areas/animals/
    description: Animals area — animal cognition, welfare, ecology
    relevant_when: [content, animals]

  areas-technology:
    path: areas/technology/
    description: Technology area — energy, AI, agrivoltaics, infrastructure
    relevant_when: [content, technology]

  areas-human-bridges:
    path: areas/human-bridges/
    description: Human Bridges area — social movements, end-of-life, community
    relevant_when: [content, human-bridges]

  authors-dir:
    path: authors/
    description: Author profiles — one file per contributor
    relevant_when: [content, author]
---

# Observatory Almanac — Context Index

**Read this first.** Use the YAML frontmatter above to navigate. Load only what the task requires.

## Discovery Protocol

```python
# Session start — always load:
load("meta/CONTEXT_INDEX.md")    # this file

# Then filter by task:
task_keys = [k for k, v in idx.items() if task_tag in v["relevant_when"]]

# Load at most 2-3 targeted assets. Never scan directories.
```

## Quick Reference

| Task | Load |
|------|------|
| Add new articles | `SCHEMA.md`, `AREAS.md`, scraper docs |
| Fix scraper bug | `scraper` + `scraper-tests` |
| Schema question | `SCHEMA.md` |
| Audit content | `meta/index.md` |
| Check area coverage | relevant `areas-*` entry |
| New area | `AREAS.md` (check first — 26 areas are stable) |

## Current Content State

*(Updated: 2026-04-28)*

| Area | Article Count |
|------|--------------|
| science | 8 |
| environment | 7 |
| history | 5 |
| animals | 4 |
| economy | 4 |
| human-bridges | 1 |
| technology | 1 |

Total: ~30 articles, 21 authors, 1 guide

## Regenerate This Index

When bulk articles are added, update the content state table above and the `updated:` frontmatter field. A generator script will automate this in a future iteration.
