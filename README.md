# Observatory Almanac

A structured, git-native mirror of [Observatory.wiki](https://observatory.wiki) — the expert-driven guide to the world produced by the Independent Media Institute.

The Almanac makes Observatory content versionable, searchable, and composable. Every article, guide, and author profile lives as a plain markdown file with explicit frontmatter. No database. No CMS. Just text that anyone can read, fork, or build on.

---

## What the Observatory Is

The Observatory publishes expert-authored articles across 26 subject areas — from Science and Environment to History, Philosophy, and World Affairs. Articles are written by credentialed researchers, journalists, and practitioners. All content is licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

The Almanac's job is to hold that content in a form that is:
- **Explicit** — every field has a defined meaning (see [SCHEMA.md](SCHEMA.md))
- **Stable** — git history is the record of truth
- **Open** — forkable, searchable, composable by anyone

---

## Structure

```
observatory-almanac/
├── README.md          ← this file
├── SCHEMA.md          ← article, guide, and author format spec
├── AREAS.md           ← canonical area taxonomy
├── areas/             ← articles, one directory per area
│   ├── science/
│   ├── environment/
│   └── ...
├── guides/            ← curated multi-article collections
├── authors/           ← author profiles
└── meta/              ← index, stats, editorial notes
```

### Articles

Each article is a markdown file in `areas/<area>/`. Filename is the URL slug from observatory.wiki (lowercase, hyphens). Example:

```
areas/science/why-scientists-are-still-puzzled-by-consciousness.md
```

### Guides

Guides are editorial collections — a curated set of articles on a theme with an introductory frame. They live in `guides/`.

### Author Profiles

Each author gets one file in `authors/`. It holds their bio, credentials, and a list of their Observatory articles.

---

## Format

See [SCHEMA.md](SCHEMA.md) for the full specification. The short version: every file starts with YAML frontmatter that makes the article's identity, provenance, and metadata machine-readable. The body is the article content in markdown.

---

## License

All Observatory content is © Independent Media Institute, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) unless otherwise noted. The Almanac structure and tooling are MIT licensed.
