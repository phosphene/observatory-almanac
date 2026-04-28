---
uri: meta/context-index
owner: feelingflowingbot
updated: 2026-04-28
description: Session-start orientation index for the Observatory Almanac. Load this first; filter by relevant_when tag; load only what the task needs.

index:
  agents:
    path: AGENTS.md
    description: Agent init protocol, infrastructure map, content standards, safety, parent workspace relationship
    relevant_when: [session-start, schema, safety, architecture]

  schema:
    path: SCHEMA.md
    description: Canonical format spec for articles, guides, authors, and all 10 document types
    relevant_when: [session-start, schema, content, scraping]

  areas:
    path: AREAS.md
    description: 26 canonical area slugs and their directory mapping
    relevant_when: [session-start, schema, content, scraping]

  spec-log:
    path: meta/SPEC_LOG.md
    description: Architectural decision log — 18 decisions recorded; append-only
    relevant_when: [architecture, schema, session-start]

  tasks:
    path: meta/TASKS.md
    description: Task board with E/D/C/I tracks; open tasks C-003/C-004/I-003/I-004
    relevant_when: [session-start, planning]

  import-queue:
    path: meta/import-queue.yml
    description: OW article scrape queue — 49 entries (30 original + 19 new areas)
    relevant_when: [scraping, content]

  memory-flow:
    path: memory/feelingflowingbot.md
    description: Flow's project memory — scraper patterns, known issues, operational shortcuts
    relevant_when: [session-start, debug, scraping]

  memory-edphos:
    path: memory/edphos.md
    description: Ed Phil's project memory — preferences, decisions, working style
    relevant_when: [session-start, architecture]

  skill:
    path: .agents/skills/almanac-content/SKILL.md
    description: Native content skill — turbo commands T1-T10, axioms, area priority queue
    relevant_when: [session-start, scraping, content]

  readme:
    path: README.md
    description: Project overview — architecture, frontmatter RAG, MkDocs, agent infrastructure
    relevant_when: [onboarding, session-start]

  team-status:
    path: team/STATUS.md
    description: Current project state — what exists, what's missing, recent history
    relevant_when: [session-start, planning]

  team-roadmap:
    path: team/ROADMAP.md
    description: Strategic roadmap — Phase 1 done, Phase 2-3 pending Jan's input
    relevant_when: [planning, architecture]

  team-planning:
    path: team/PLANNING.md
    description: Strategic planning register — S-001 through S-006 all blocked on Jan
    relevant_when: [planning, session-start]

  requirements-jan:
    path: team/requirements/jan-almanac-brief.md
    description: Requirements brief for Jan — almanac concept, modularity, reproduction questions
    relevant_when: [planning, architecture, requirements]

  scraper:
    path: ../../lib/python/scripts/feelingflowingbot/observatory_scraper.py
    description: OW scraper (parent workspace) — ParsedArticle, pipeline stages, bulk runner
    relevant_when: [scraping, debug]

  scraper-tests:
    path: ../../lib/python/scripts/feelingflowingbot/test_observatory_scraper.py
    description: 115 scraper tests — run before any scraper change
    relevant_when: [scraping, testing]

  snapshot-tests:
    path: ../../lib/python/scripts/feelingflowingbot/test_observatory_scraper_snapshot.py
    description: 37 snapshot tests against real OW HTML fixtures (debt-forgiveness, bees, chickens)
    relevant_when: [scraping, testing]

  almanac-schema-py:
    path: lib/python/almanac/src/almanac/schema.py
    description: Pydantic schema models — all 10 document types, frozen + extra=forbid
    relevant_when: [schema, testing]

  almanac-parsing-py:
    path: lib/python/almanac/src/almanac/parsing.py
    description: Canonical frontmatter extractor — split_frontmatter + extract_meta
    relevant_when: [schema, debug]

  almanac-validator-py:
    path: lib/python/almanac/src/almanac/validator.py
    description: Content validator — exit codes 0/1/2, stdout/stderr split
    relevant_when: [schema, testing, ci]

  generate-area-indexes:
    path: scripts/generate_area_indexes.py
    description: Area index page generator — run after bulk content additions
    relevant_when: [content, ci]

  build-docs-tree:
    path: scripts/build_docs_tree.py
    description: Idempotent docs/ symlink tree builder — run before mkdocs build
    relevant_when: [ci, mkdocs]

  deploy-workflow:
    path: .github/workflows/deploy.yml
    description: GitHub Pages CI — build_docs_tree + validator + mkdocs --strict + deploy
    relevant_when: [ci, architecture]

  areas-science:
    path: areas/science/
    description: Science — biology, archaeology, consciousness, paleoanthropology (8 OW articles)
    relevant_when: [content, science]

  areas-environment:
    path: areas/environment/
    description: Environment — climate, biodiversity, pollution, oceans (7 OW articles)
    relevant_when: [content, environment]

  areas-history:
    path: areas/history/
    description: History — ancient civilizations, archaeology, political history (5 OW articles)
    relevant_when: [content, history]

  areas-economy:
    path: areas/economy/
    description: Economy — inequality, labor, debt, political economy (4 OW articles)
    relevant_when: [content, economy]

  areas-animals:
    path: areas/animals/
    description: Animals — animal cognition, welfare, ecology (4 OW articles)
    relevant_when: [content, animals]

  areas-health:
    path: areas/health/
    description: Health — public health, caregiving, youth health (4 OW articles)
    relevant_when: [content, health]

  areas-psychology:
    path: areas/psychology/
    description: Psychology — consciousness, news fatigue, grief (4 OW articles)
    relevant_when: [content, psychology]

  areas-philosophy:
    path: areas/philosophy/
    description: Philosophy — consciousness, ancient time concepts, Fichte (4 OW articles)
    relevant_when: [content, philosophy]

  areas-world-affairs:
    path: areas/world-affairs/
    description: World Affairs — climate justice, nuclear risk (2 OW articles)
    relevant_when: [content, world-affairs]

  areas-language:
    path: areas/language/
    description: Language — nature language, Volapük, accent discrimination (5 OW articles)
    relevant_when: [content, language]

  areas-technology:
    path: areas/technology/
    description: Technology — agrivoltaics, AI, infrastructure (1 OW article)
    relevant_when: [content, technology]

  areas-human-bridges:
    path: areas/human-bridges/
    description: Human Bridges — social movements, end-of-life (1 OW article)
    relevant_when: [content, human-bridges]

  authors-dir:
    path: authors/
    description: 29 author profiles — stubs auto-created by scraper
    relevant_when: [content, author]
---

# Observatory Almanac — Context Index

**Read this first.** Use the YAML frontmatter above to navigate. Load only what the task requires.

## Discovery Protocol

```python
# Every session start — load this file once
load("meta/CONTEXT_INDEX.md")

# Check task board
load("meta/TASKS.md")  # pick highest-priority open task

# Filter by task domain
task_keys = [k for k, v in idx.items() if task_tag in v["relevant_when"]]

# Load at most 2-3 targeted assets. Never scan directories.
```

## Quick Reference

| Task | Load |
|------|------|
| Add OW articles | `skill` → T1/T2; `import-queue` |
| Fix scraper bug | `scraper` + `scraper-tests` + `snapshot-tests` |
| Schema question | `schema` + `almanac-schema-py` |
| Architecture decision | `spec-log` |
| Validate content | `almanac-validator-py` |
| Prior context | `memory-flow` or `memory-edphos` |
| CI pipeline | `deploy-workflow` |
| MkDocs build | `build-docs-tree` then `mkdocs build` |

## Current Content State

*(Updated: 2026-04-28)*

| Area | OW Articles | Almanac-Native | Total |
|------|-------------|----------------|-------|
| science | 8 | 7 | 15 |
| environment | 7 | 8 | 15 |
| history | 5 | 4 | 9 |
| cooking | 0 | 27 | 27 |
| health | 4 | 22 | 26 |
| arts-recreation | 0 | 24 | 24 |
| psychology | 4 | 9 | 13 |
| world-affairs | 2 | 9 | 11 |
| philosophy | 4 | 9 | 13 |
| animals | 4 | 0 | 4 |
| economy | 4 | 0 | 4 |
| language | 5 | 4 | 9 |
| technology | 1 | 6 | 7 |
| local-peace-economy | 0 | 6 | 6 |
| human-bridges | 1 | 0 | 1 |
| *other areas* | 0 | varies | — |

**Totals:** ~190 documents · 29 author profiles · 1 guide · 20 populated areas

## Empty Areas (OW articles)
`agriculture` · `arts-recreation` · `charter-schools` · `cooking` · `dig-labs` · `education` · `energy` · `food` · `literature` · `media` · `natural-health` · `peoples-movements` · `voting-elections`

## Regenerate This Index

Update the content state table and `updated:` field after bulk article additions. Add new asset entries when infrastructure changes.
