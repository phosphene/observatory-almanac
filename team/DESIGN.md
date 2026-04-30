---
uri: team/design
owner: feelingflowingbot
updated: 2026-04-30
description: >
  System design document for the Observatory Almanac. Describes what we are
  producing, the rule set that governs each layer, and how those rules are
  proven. Intended as the shared reasoning surface for the whole team.
---

# Observatory Almanac — System Design

> This document is the team's shared map of what we're building and why it works the way it does.
> Every rule stated here is proven by a BDD scenario in `lib/python/almanac/tests/features/`.
> When a new rule is added, a scenario is added first.

---

## What We Are Producing

The Observatory Almanac is a **structured, git-native knowledge repository** built on the content of [Observatory.wiki](https://observatory.wiki) — the Independent Media Institute's expert-driven guide to the world.

It has three distinct outputs:

| Output | What it is | Who it serves |
|--------|-----------|---------------|
| **The site** | A navigable, indexed knowledge base at `phosphene.github.io/observatory-almanac` | Everyday readers |
| **The repository** | A machine-readable corpus of structured markdown files | Agents, tooling, future integrations |
| **The toolchain** | A validated pipeline from raw content → published site | Brittani (editor), Flow (agent), CI |

The content itself comes from Observatory.wiki: articles written by credentialed researchers and journalists, licensed CC BY-NC-SA 4.0. The almanac gives that content structure, addressability, and durability that the wiki alone cannot provide.

---

## Architecture in One Diagram

```
observatory.wiki
      │
      │ scrape / ingest
      ▼
areas/<area>/<slug>.md          ← content files (article, guide, etc.)
authors/<slug>.md               ← author profiles
guides/<slug>.md                ← curated reading guides
      │
      │ almanac validate        ← schema enforcement
      ▼
      │ almanac index           ← per-area index.md pages
      ▼
      │ almanac tree            ← docs/ symlink tree for MkDocs
      ▼
      │ mkdocs build            ← rendered HTML site
      ▼
GitHub Pages → live site
      │
      │ almanac tasks           ← task board for Brittani
      ▼
meta/brittani-tasks.md
```

Every stage is a separate, testable command. Each can be run independently or chained in CI.

---

## Layer 1: Content Schema

Every document in the repository must declare structured YAML frontmatter. The schema is defined in `SCHEMA.md`. Pydantic models in `almanac.models` enforce it.

### Rules

**Rule: Every article must declare all required fields.**

An article without `author`, `author_slug`, `source_url`, `area`, `type`, `license`, `published`, `updated`, `summary`, or `tags` is invalid. The validator will report each missing field by name.

> *Why:* These fields are the contract. Without them, search, indexing, attribution, and rendering all break. A partial document is worse than no document.

**Rule: The area slug must be a canonical value from AREAS.md.**

The `area` field in an article's frontmatter must match one of the 26 defined area slugs. Arbitrary values are rejected.

> *Why:* The area slug is the primary navigation axis. A non-canonical slug creates an orphaned document that no index will pick up.

**Rule: Auto-generated area `index.md` nav pages are excluded from content validation.**

The indexer generates a navigation `index.md` file in each area directory. These files use a reduced frontmatter (`title`, `area`, `hide`) and are not content documents. They must not be routed to the article or author schema validators.

> *Why:* This is a system file, not a contributor file. Validating it as content produces false positives that mask real errors.

---

## Layer 2: Area Indexes

The indexer (`almanac index`) generates two things:
1. A `meta/index.md` inventory of all documents
2. A per-area `areas/<area>/index.md` navigation page listing that area's articles

### Rules

**Rule: Every area directory receives an index page.**

Including empty areas. An empty area index is valid — it reflects an area that has been scaffolded but not yet filled.

**Rule: The index includes author attribution for each article.**

Every entry in the area index links the article and credits the author. Anonymous attribution is not valid.

**Rule: Dry run does not write files.**

`almanac index --dry-run` validates what would be generated without writing anything. No side effects.

---

## Layer 3: Documentation Tree

The tree builder (`almanac tree`) constructs the `docs/` symlink tree that MkDocs uses as its source. It does not copy files — it creates symbolic links so the canonical content always lives in `areas/`, `authors/`, and `guides/`.

### Rules

**Rule: All content directories are symlinked into `docs/`.**

`docs/areas/` mirrors `areas/` by area. `docs/authors/` mirrors `authors/`. `docs/guides/` mirrors `guides/`. A directory absent from `docs/` produces broken links from any document that references it.

**Rule: Each area in `docs/` has a `.pages` file for navigation title.**

MkDocs uses `.pages` files (via the awesome-pages plugin) to set the display name of each area in the navigation. Without this, area directories appear with raw slugs (e.g. `world-affairs`) instead of display names (e.g. `World Affairs`).

---

## Layer 4: Content Task Board

The task generator (`almanac tasks`) produces `meta/brittani-tasks.md` — Brittani's daily view of what needs attention. It is auto-generated from the actual repository state; it is never edited by hand.

### Rules

**Rule: Broken author profile links are surfaced as tasks.**

When an author profile contains a link to an article or guide that does not exist in the repository, that link is a live broken link on the published site. It appears in the 🔴 Broken Links section with the title, target path, and content type.

**Rule: Validation failures are surfaced as tasks.**

Content files that fail `almanac validate` appear in the 🟠 Validation Failures section. Each violation lists the file path and the specific field that failed.

**Rule: Empty areas are surfaced as tasks.**

Area directories that contain no content files appear in the 🟡 Empty Areas section. This tells Brittani which parts of the knowledge map are still blank.

> *Design note:* The task board regenerates nightly. Resolved items disappear automatically. Brittani does not need to update it — she just needs to fix what's on it.

---

## How Rules Are Proven

Every rule in this document corresponds to one or more BDD scenarios in `lib/python/almanac/tests/features/`. The scenarios use the Gherkin `Rule:` keyword to make the connection explicit.

| Feature file | Rules covered |
|---|---|
| `validator.feature` | Required fields; canonical area slug; index.md exclusion |
| `indexer.feature` | Per-area index generation; author attribution; dry run; empty areas |
| `tasks.feature` | Broken links surfaced; empty areas surfaced; validation failures surfaced |
| `content-workflow.feature` | Full validate → index pipeline; field errors block indexing |

**The rule-first protocol:** when a new rule is introduced (whether by fixing a bug, adding a feature, or discovering implicit behavior), the BDD scenario is written first. The scenario both documents what the rule IS and proves it holds — negative cases included.

This is what makes the test suite a living specification rather than just a safety net.

---

## Current State (2026-04-30)

| Layer | Rules proven | Open gaps |
|---|---|---|
| Content schema | 3 rules, 7 scenarios | Author slug format rule not yet formalized |
| Area indexes | 4 rules, 4 scenarios | Multi-area batch indexing not tested |
| Docs tree | guides/ symlink now included | `.pages` file generation not yet BDD-tested |
| Task board | 3 rules, 5 scenarios | Guide type display label (shows filename, not "guide") |

---

## Glossary

| Term | Meaning |
|------|---------|
| **area** | A subject category (`science`, `environment`, `history`, etc.). 26 defined in `AREAS.md`. |
| **slug** | A lowercase, hyphen-separated identifier derived from the content's URL. Never changes once set. |
| **frontmatter** | The YAML block at the top of every markdown file. The structured identity of the document. |
| **nav page** | An auto-generated `index.md` in each area directory. System file, not content. |
| **task board** | `meta/brittani-tasks.md`. Auto-generated daily. Brittani's work queue. |
| **proven rule** | A rule stated in this document that has at least one positive and one negative BDD scenario. |
