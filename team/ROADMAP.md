---
uri: team/roadmap
owner: feelingflowingbot
updated: 2026-04-28
description: Strategic roadmap for the Observatory Almanac. Tracks phases, milestones, and open strategic questions. Updated as Jan's requirements are collected.
stage: draft — awaiting Jan's input on core questions
---

# Observatory Almanac — Roadmap

⚠️ **Draft status.** This roadmap is structurally sound but strategically incomplete. Jan's requirements (see `team/requirements/jan-almanac-brief.md`) must inform Phase 2 and beyond before this is considered authoritative.

---

## North Star

The Observatory Almanac is a **living, structured reference** — expert knowledge organized for repeated use, not for a feed. It is:

- **Curated**, not crowdsourced
- **Structured**, not narrative
- **Reproducible**, not proprietary
- **Modular**, not monolithic

The question "what is an almanac?" is not rhetorical. The historical almanac (Farmer's Almanac, World Almanac) was a trusted annual reference covering everything a person needed to navigate the year — weather, tides, astronomical data, political facts, crop guidance. The Observatory Almanac is that model applied to expert knowledge: structured coverage of 26 subject areas, updated continuously, built to be used rather than merely read.

---

## Phase 1 — Infrastructure ✅ Complete

**Goal:** A functioning, deployable knowledge repository with production-quality tooling.

| Milestone | Status |
|-----------|--------|
| Schema design (10 document types, Pydantic enforcement) | ✅ Done |
| OW scraper with 115 tests | ✅ Done |
| 190 documents across 20 areas | ✅ Done |
| MkDocs Material site with CI/CD | ✅ Done |
| Validation pipeline | ✅ Done |
| Agent infrastructure (skills, memory, spec log) | ✅ Done |
| Full documentation | ✅ Done |

---

## Phase 2 — Content Depth (Pending Jan's Input)

**Goal:** All 26 areas have meaningful OW article coverage. Author profiles are enriched. Site is genuinely useful to a first-time visitor.

| Milestone | Status | Depends On |
|-----------|--------|------------|
| All 26 areas populated with OW articles | Open | Jan: area priority ranking |
| Author profiles enriched (credentials, bio, article list) | Open | — |
| Social cards configured | Open | — |
| Validator as hard CI gate | Open | — |
| Annual/snapshot release model | Open | Jan: publishing cadence |

---

## Phase 3 — Modularity (Requires Definition)

**Goal:** Individual areas can be extracted, embedded, or published as standalone products. The almanac pattern is reproducible by other publishers.

This phase is entirely dependent on Jan's answers to the modularity questions in `team/requirements/jan-almanac-brief.md`.

Possible directions (not committed):

| Direction | What It Would Mean |
|-----------|--------------------|
| Area-as-package | Each area is an independently deployable MkDocs site |
| Almanac-as-template | Fork this repo, point at a different mediawiki, get a new almanac |
| Embedded widgets | Each article/area embeddable in the Observatory.wiki or ind.media ecosystem |
| API surface | The frontmatter index queryable as a structured data endpoint |
| Annual edition | Snapshot release with editorial curation — a "volume" |

---

## Phase 4 — Integration (Speculative)

**Goal:** The Almanac feeds back into the Observatory.wiki and ind.media research infrastructure.

| Direction | What It Would Mean |
|-----------|-------------------|
| RAG pipeline | Almanac frontmatter as context for researcher queries |
| Observatory.wiki backlinks | Each article links to its Almanac entry |
| Research brief generation | Area coverage summaries for journalists and researchers |
| Watchlist / alerts | New OW articles in subscribed areas delivered to subscribers |

---

## Open Strategic Questions

These cannot be answered without Jan. They gate Phase 2 and 3.

1. **What IS the almanac to Jan?** Is it a reference tool? A publishing infrastructure? A research aid? A public product?
2. **Who is the primary audience?** IMI staff? Journalists? Researchers? General public?
3. **What does "modular" mean?** Can someone subscribe to just the Science area? Fork just the Environment area?
4. **What does "reproduce" mean?** Can another org run this process for their MediaWiki content?
5. **Publishing cadence?** Living (continuous) or annual editions or both?
6. **Relationship to Observatory.wiki?** Supplement (adds structure), replacement (standalone), or integration (feeds back)?
7. **What is missing from the current 26 areas?** Does Jan see gaps in the taxonomy?
