---
uri: team/status
owner: feelingflowingbot
updated: 2026-04-28
description: Current project status for the Observatory Almanac. Updated at the close of each significant work session.
---

# Observatory Almanac — Project Status

## Current State (2026-04-28)

### What Exists

| Layer | Status | Detail |
|-------|--------|--------|
| Content | ✅ Functional | 190 docs, 29 authors, 20/26 areas |
| Schema | ✅ Solid | Pydantic-enforced, 10 document types, CC/MIT tracks |
| Scraper | ✅ Production-ready | 115 tests, 2-strategy body detection, named pipeline |
| Validation | ✅ Working | Exit codes 0/1/2, stdout/stderr split |
| MkDocs site | ✅ Deployed | Material theme, awesome-pages, git revision dates |
| CI/CD | ✅ Wired | GitHub Actions → GitHub Pages |
| Agent infrastructure | ✅ Self-sufficient | Skills, memory, spec log, context index, task board |
| Documentation | ✅ Comprehensive | README, AGENTS.md, SPEC_LOG.md, SCHEMA.md |

### What's Missing

| Gap | Priority | Owner |
|-----|----------|-------|
| 6 areas have zero OW articles | P1 | Flow |
| Author profiles are stubs | P2 | Flow |
| Social cards (OG images) | P3 | Flow |
| Validator as hard CI gate | P3 | Flow |
| **Jan's requirements** | **P0** | **Jan + Ed Phil** |
| Strategic roadmap | P1 | Jan + Ed Phil + Flow |

---

## What Jan Hasn't Seen Yet

The infrastructure was built before Jan was briefed. His input is needed on:

1. **What an almanac IS** — his mental model, not ours
2. **Publishing cadence** — living/continuous, annual, or both?
3. **Primary audience** — who is this for?
4. **Modularity** — what does it mean to extract one area as a standalone product?
5. **Reproduction** — can another publisher run this process for their content?
6. **Observatory.wiki relationship** — supplement, replacement, or parallel track?

See `team/requirements/jan-almanac-brief.md` for the full requirements collection framework.

---

## Open Engineering Tasks

See `meta/TASKS.md` for the full board. Open items:

| ID | Priority | Title |
|----|----------|-------|
| C-003 | P2 | Seed 11 empty areas with OW articles |
| C-004 | P3 | Enrich author profiles beyond stubs |
| I-003 | P3 | Configure social cards (Material social plugin) |
| I-004 | P3 | Validator as hard CI gate |

---

## Recent History

| Date | Milestone |
|------|-----------|
| 2026-04-28 | Full build day — scraper, schema, MkDocs, CI, agent infrastructure |
| 2026-04-28 | 19 new OW articles scraped (5 new areas: health, psychology, philosophy, world-affairs, language) |
| 2026-04-28 | Complete documentation pass — README, AGENTS.md, SPEC_LOG.md, memory, skill |
| 2026-04-28 | Team area and planning infrastructure created |
