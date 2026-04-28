# Observatory Almanac — Document Schema

This document defines the explicit format for every file in the Almanac. The schema is designed so that a contributor can read it once and understand exactly what every field means and why it exists.

All files use YAML frontmatter followed by a markdown body. The frontmatter is the structured identity of the document. The body is the content.

---

## Article

**Location:** `areas/<area>/<slug>.md`
**Slug:** lowercase, hyphens, derived from the observatory.wiki URL.

### Frontmatter

```yaml
---
title: "Full article title"
area: science                      # canonical area slug (see AREAS.md)
type: article                      # article | guide | classic
author: Leslie Alan Horvitz        # display name as credited on observatory.wiki
author_slug: leslie-alan-horvitz   # links to authors/<slug>.md
source: The Observatory            # originating publication or project
source_url: https://observatory.wiki/...   # canonical URL on observatory.wiki
license: CC BY-NC-SA 4.0
published: 2026-02-06              # ISO 8601 date of first publication
updated: 2026-02-06                # ISO 8601 date of last edit
summary: >
  One to three sentence description of the article. This is the lede —
  what the piece is about and why it matters.
tags:
  - consciousness
  - neuroscience
  - philosophy-of-mind
---
```

### Field definitions

| Field | Required | Meaning |
|-------|----------|---------|
| `title` | yes | Exact title as it appears on observatory.wiki |
| `area` | yes | Canonical area slug from AREAS.md |
| `type` | yes | `article`, `guide`, or `classic` |
| `author` | yes | Author display name as credited |
| `author_slug` | yes | Filename stem of the author's profile in `authors/` |
| `source` | yes | The publication or project that produced this content (e.g. "The Observatory", "Earth Food Life Project", "Independent Media Institute") |
| `source_url` | yes | Canonical URL on observatory.wiki |
| `license` | yes | Always `CC BY-NC-SA 4.0` unless explicitly different |
| `published` | yes | First publication date, ISO 8601 |
| `updated` | yes | Last edit date on observatory.wiki, ISO 8601 |
| `summary` | yes | 1–3 sentence description. Written by the Almanac, not scraped — should be accurate and useful to someone deciding whether to read |
| `tags` | yes | Lowercase, hyphens. Conceptual tags, not area names (area is already in frontmatter) |

### Body

The body is the article text in standard markdown. Preserve the original structure (headings, lists, pull quotes) as closely as possible. Do not add editorial commentary or wrappers — the body should read as the article itself.

Attribution line at the end (mandatory):

```markdown
---
*Originally published at [observatory.wiki](<source_url>). © Independent Media Institute. Licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
```

---

## Guide

**Location:** `guides/<slug>.md`

Guides are editorial collections — a curated set of articles on a theme, with an introductory frame written by an editor.

### Frontmatter

```yaml
---
title: "Guide to Artificial Intelligence"
type: guide
editor: Leslie Alan Horvitz
editor_slug: leslie-alan-horvitz
source: The Observatory
source_url: https://observatory.wiki/Guide_to_Artificial_Intelligence
license: CC BY-NC-SA 4.0
published: 2025-01-01
updated: 2026-04-01
summary: >
  A curated collection of Observatory articles exploring AI's unresolved
  issues: energy costs, autonomous weapons, creative displacement, and more.
tags:
  - artificial-intelligence
  - technology
  - ethics
articles:
  - slug: areas/technology/hidden-cost-of-ai-energy.md
    author: Sharon Kumar
    note: "Data centers and the electric grid"
  - slug: areas/technology/rise-of-ai-warfare.md
    author: Leslie Alan Horvitz
    note: "Autonomous weapons and cognitive warfare"
---
```

### Body

Editor's introductory frame, then a numbered list of the articles with brief description of each. Body mirrors the observatory.wiki guide structure.

---

## Author Profile

**Location:** `authors/<slug>.md`

### Frontmatter

```yaml
---
name: Leslie Alan Horvitz
slug: leslie-alan-horvitz
credentials: >
  Leslie Alan Horvitz is an author and journalist based in New York.
  He has written extensively on science, history, and geopolitics.
source_url: https://observatory.wiki/Leslie_Alan_Horvitz
---
```

### Body

One paragraph bio (as it appears on observatory.wiki), followed by a list of their Observatory articles:

```markdown
## Articles

- [Why Scientists Are Still Puzzled by Consciousness](../areas/science/why-scientists-are-still-puzzled-by-consciousness.md) — Science
- [Guide to Artificial Intelligence](../guides/guide-to-artificial-intelligence.md) — Guide
```

---

## Almanac Reference Document

**Location:** `areas/<area>/<slug>.md`

Almanac-native reference content (not from observatory.wiki). Includes rulebooks, recipes, field guides, factbooks, assessments, and practical reference material from the Observatory Almanac source.

### Frontmatter

```yaml
---
title: "Document Title"
area: arts-recreation              # canonical area slug (see AREAS.md)
type: rulebook                     # see type list below
source: Observatory Almanac
license: MIT
updated: 2026-04-28
summary: >
  One to three sentence description.
tags:
  - games
  - strategy
---
```

### Type values (full list)

| Type | Used for |
|------|----------|
| `article` | Observatory.wiki journalism, expert-authored pieces |
| `guide` | Editorial collections, multi-article curation |
| `classic` | Canonical long-form journalism |
| `almanac` | General almanac reference (multi-topic, section-spanning) |
| `recipe` | Culinary recipes and food preparation |
| `rulebook` | Game rules and ludology |
| `factbook` | Country or regional reference profiles |
| `reference` | Practical reference (emergency, conversions, templates) |
| `assessment` | Self-knowledge and psychological assessment tools |
| `field-guide` | Natural history and identification guides |

### License

Almanac-native content: `MIT`
Observatory.wiki content: `CC BY-NC-SA 4.0`

---

## Naming conventions

- Slugs are always lowercase with hyphens: `why-scientists-are-still-puzzled-by-consciousness`
- Area slugs match the directory names in `areas/` exactly (see AREAS.md)
- Author slugs match the filename in `authors/` exactly
- No spaces, no underscores, no special characters in filenames
