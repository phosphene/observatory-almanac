---
uri: team/planning
owner: feelingflowingbot
updated: 2026-04-28
description: Strategic planning register for the Observatory Almanac. Tracks decisions, blockers, and open questions at the product level. Distinct from meta/TASKS.md (engineering board).
---

# Observatory Almanac — Planning Register

Tracks strategic decisions and blockers. Engineering tasks live in `meta/TASKS.md`. This file is for product-level thinking.

---

## Open Strategic Blockers

| ID | Blocker | Waiting On | Unblocks |
|----|---------|------------|---------|
| S-001 | Jan's definition of "almanac" | Jan | Phase 2 direction, roadmap |
| S-002 | Jan's definition of "modular" | Jan | Phase 3 architecture |
| S-003 | Jan's definition of "reproduce" | Jan | Scheduler, API surface, template design |
| S-004 | Publishing cadence (living vs. annual) | Jan | Release process, snapshot tooling |
| S-005 | Primary audience definition | Jan | Content priorities, UX decisions |
| S-006 | Relationship to Observatory.wiki | Jan | Integration architecture |

All six blocked on Jan's input. See `team/requirements/jan-almanac-brief.md`.

---

## Decisions Made

| ID | Date | Decision | Log |
|----|------|----------|-----|
| P-001 | 2026-04-28 | Repository is content + agent infrastructure, not content-only | SPEC-018 |
| P-002 | 2026-04-28 | Two license tracks: CC BY-NC-SA (OW) + MIT (native) | SPEC-003 |
| P-003 | 2026-04-28 | 26 canonical areas — stable until Jan reviews | SPEC-002 |
| P-004 | 2026-04-28 | Frontmatter is the primary interface between content and tooling | README §1 |
| P-005 | 2026-04-28 | MkDocs Material as published surface — not a CMS | SPEC-012 |

---

## Hypotheses Under Test

Things we've assumed that Jan may revise:

| Hypothesis | Assumption | Risk if Wrong |
|------------|------------|---------------|
| H-001 | An almanac is a structured mirror of OW | Jan may want something original, not a mirror | Would require new content production workflow |
| H-002 | 26 areas is the right taxonomy | Jan may have a different subject map in mind | Area migration is feasible but time-consuming |
| H-003 | The audience is researchers/journalists | General public audience would require different UX/content standards | MkDocs may not be the right surface |
| H-004 | Living/continuous is better than annual | Jan may want annual snapshot editions | Would need edition/versioning tooling |
| H-005 | Area = module | Jan's "modular" may mean something different architecturally | Phase 3 design would change significantly |

---

## Action Items

| ID | Action | Owner | Status |
|----|--------|-------|--------|
| A-001 | Send requirements brief to Jan | Ed Phil | Open |
| A-002 | Collect Jan's answers to `jan-almanac-brief.md` | Jan | Waiting |
| A-003 | Update ROADMAP.md based on Jan's answers | Flow | Blocked on A-002 |
| A-004 | Define Phase 2 milestones | Ed Phil + Flow | Blocked on A-002 |
| A-005 | Define modularity architecture | Ed Phil + Flow | Blocked on A-002 |
| A-006 | Seed remaining 6 empty areas (OW articles) | Flow | Open — can proceed in parallel |
