# Observatory Almanac

A structured, git-native knowledge repository built on [Observatory.wiki](https://observatory.wiki) — the expert-driven guide to the world produced by the [Independent Media Institute](https://ind.media).

**Live site:** [ind-media.github.io/observatory-almanac](https://ind-media.github.io/observatory-almanac)

---

## What This Is

The Observatory publishes expert-authored articles across 26 subject areas — Science, Environment, History, Philosophy, World Affairs, and more. Every article is written by credentialed researchers, journalists, and practitioners, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

The Almanac holds that content in a form that is **structured, versionable, and machine-readable** — without a database, without a CMS, without a platform dependency. Every document is a plain markdown file with explicit YAML frontmatter. Git is the database. The file system is the API.

This is not a scrape dump. The Almanac is a **knowledge architecture**: a system where content, tooling, documentation, and agent intelligence are co-located and mutually reinforcing.

---

## The Architecture

### 1. Frontmatter as the Primary Interface

Every document in this repository begins with a YAML frontmatter block. This is not decoration — it is the contract between content and tooling:

```yaml
---
title: "Debt Forgiveness in the Bronze Age"
area: history
type: article
author: Michael Hudson
author_slug: michael-hudson
source: The Observatory
source_url: https://observatory.wiki/Debt_Forgiveness_in_the_Bronze_Age
license: CC BY-NC-SA 4.0
published: '2024-09-19'
updated: '2024-09-19'
summary: How ancient civilisations used periodic debt cancellations to maintain
  social stability — and why the modern world has forgotten the lesson.
tags:
  - debt
  - bronze-age
  - inequality
  - ancient-history
---
```

Every field has a defined meaning, enforced by the Pydantic schema in `lib/python/almanac/src/almanac/schema.py`. Unknown fields fail validation. Missing required fields fail validation. The frontmatter is the document's identity — not its filename, not its position in a tree.

See [SCHEMA.md](SCHEMA.md) for the full specification of all 10 document types.

---

### 2. Frontmatter-Driven RAG

The frontmatter structure enables **Retrieval-Augmented Generation** directly over the file system. Each document is a self-describing unit: it declares its topic (`area`, `tags`), its provenance (`author`, `source_url`, `license`), its temporal position (`published`, `updated`), and its semantic summary (`summary`).

An agent or search system can:
- Filter by `area` to get domain-scoped context
- Filter by `tags` for concept-level retrieval
- Read `summary` for lightweight triage before loading the full body
- Follow `author_slug` to get author context
- Verify `license` before any downstream use

The `meta/SPEC_LOG.md`, `meta/TASKS.md`, and `memory/` files extend this model to agent infrastructure: every decision, task, and operational pattern is a structured document that agents can index, retrieve, and reason over.

---

### 3. MkDocs — The Published Surface

The frontmatter fields `title`, `tags`, and `summary` are read directly by [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) to produce a rich documentation site. The build process is orchestrated by a unified CLI:

1. **Validation**: All content is verified against the Pydantic schema using `almanac-validator`.
2. **Indexing**: Area index pages and the global content inventory are regenerated via `almanac-indexer`.
3. **Tree Building**: An idempotent symlink tree is constructed in `docs/` via `almanac-tree`.

Content in `areas/` and `authors/` is symlinked into `docs/` at build time — the canonical files live at the repo root, not inside `docs/`. This keeps the content structure clean and the MkDocs configuration minimal.

---

### 4. Agent Infrastructure

This repository is an agent workspace, not just a content repository. Agents working here operate within a defined architecture:

```
.agents/skills/almanac-content/SKILL.md  — turbo commands, axioms, standards
memory/feelingflowingbot.md              — Flow's operational memory
meta/CONTEXT_INDEX.md                    — session-start orientation index
meta/SPEC_LOG.md                         — architectural decisions (append-only)
meta/TASKS.md                            — task board (E/D/C/I tracks)
```

**Graduated Discovery** — agents read `meta/CONTEXT_INDEX.md` first, then load only what the task requires. No directory scanning. No guessing. The index is the map.

**Behavioral Proof** — The core CLI tools are backed by a **Behave BDD** suite (`lib/python/almanac/tests/features/`), ensuring that architectural contracts are enforced and verifiable through human-readable scenarios.

---

## Repository Structure

```
observatory-almanac/
├── .agents/
│   └── skills/almanac-content/SKILL.md  ← native agent skill
├── .github/workflows/deploy.yml          ← GitHub Pages CI
├── areas/                                ← content by subject area (26 areas)
├── authors/                              ← author profiles
├── docs/                                 ← MkDocs source (symlinked from areas/)
├── guides/                               ← curated multi-article collections
├── lib/python/almanac/                   ← modular almanac package
│   ├── src/almanac/
│   │   ├── cli.py                        ← unified entry point (validate/index/tree)
│   │   ├── schema.py                     ← Pydantic models (10 document types)
│   │   ├── validator.py                  ← logic layer for content validation
│   │   ├── io.py                         ← isolated filesystem operations
│   │   ├── rendering.py                  ← pure Markdown rendering logic
│   │   └── constants.py                  ← centralized regex and taxonomy
│   └── tests/
│       ├── features/                     ← Behave BDD CLI scenarios
│       └── test_schema.py                ← unit tests for models
├── memory/
│   └── feelingflowingbot.md              ← Flow's project memory
├── meta/
│   ├── areas.yml                         ← centralized taxonomy metadata
│   ├── CONTEXT_INDEX.md                  ← session-start orientation
│   ├── SPEC_LOG.md                       ← architectural decisions
│   ├── TASKS.md                          ← task board
│   └── import-queue.yml                  ← OW article scrape queue
├── AGENTS.md                             ← agent protocol and infrastructure map
├── AREAS.md                              ← 26 canonical area slugs
├── mkdocs.yml                            ← MkDocs Material configuration
├── requirements-docs.txt                 ← Python deps for docs build
└── SCHEMA.md                             ← human-readable content format spec
```

---

## Content State

| Area | OW Articles | Almanac-Native | Total |
|------|-------------|----------------|-------|
| science | 8 | 7 | 15 |
| environment | 7 | 8 | 15 |
| history | 5 | 4 | 9 |
| cooking | 0 | 27 | 27 |
| health | 4 | 22 | 26 |
| arts-recreation | 0 | 24 | 24 |
| psychology | 4 | 9 | 13 |
| philosophy | 4 | 9 | 13 |
| world-affairs | 2 | 9 | 11 |
| language | 5 | 4 | 9 |
| economy | 4 | 0 | 4 |
| animals | 4 | 0 | 4 |
| technology | 1 | 6 | 7 |
| local-peace-economy | 0 | 6 | 6 |
| human-bridges | 1 | 0 | 1 |

**~190 documents · 29 author profiles · 1 guide · 20 populated areas**

*Last updated: 2026-04-28*

---

## Working With This Repository

### Scrape a new OW article
```bash
# Add to the queue
echo "  - url: https://observatory.wiki/Article_Title\n    area: area-slug" >> meta/import-queue.yml

# Scrape (from workspace root — scraper lives in parent workspace)
uv run --project ../../lib/python python ../../lib/python/scripts/feelingflowingbot/observatory_scraper.py --bulk
```

### Validate all content
```bash
cd lib/python/almanac
uv run almanac-validator --root ../../..
```

### Build and preview the site locally
```bash
pip install -r requirements-docs.txt
cd lib/python/almanac
uv run almanac-indexer --root ../../..
uv run almanac-tree --root ../../..
mkdocs serve
```

### Run tests
```bash
cd lib/python/almanac
uv run pytest              # Unit tests
uv run behave              # BDD behavioral tests
```

---

## Two Content Tracks

**Observatory.wiki articles** (`type: article`, `type: classic`, `type: guide`)
- Licensed CC BY-NC-SA 4.0 by the Independent Media Institute
- Scraped and structured by the Observatory Almanac Bot
- Attribution line mandatory at the end of every document

**Almanac-native content** (`type: almanac`, `type: recipe`, `type: rulebook`, etc.)
- MIT licensed
- Reference material, recipes, field guides, factbooks, assessments
- Authored directly for the Almanac

---

## License

Observatory.wiki content: © Independent Media Institute, [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Almanac structure, tooling, and native content: [MIT](LICENSE)
