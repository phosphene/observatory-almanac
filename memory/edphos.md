---
uri: memory/edphos
owner: feelingflowingbot
updated: 2026-04-28
description: Ed Phil's project-scoped memory for the Observatory Almanac. Tracks his preferences, decisions, and working style as observed in this project.
---

# Ed Phil — Observatory Almanac Memory

Project memory for Ed Phil (`edphos`, id: `8031635700`). Tracks what I know about how he works and what he wants from this project.

---

## Role

Systems architect on the Phosphene platform. In the Observatory Almanac specifically: he initiated the build, set all axiomatic standards, and made every major architectural decision either directly or through review.

---

## Working Style (observed this session)

**Decision velocity is high.** When given options, he picks fast and expects immediate execution. "b" for option B — that's all. No elaboration needed.

**Progress transparency preferred.** Explicitly asked for "short outputs to show progress" during the engineering sweep. Not a long summary at the end — a running feed.

**Review before build.** Before the refactor sweep, he said "review for best practices." He wanted to see the issues identified before fixing them. Once the review was out, "clean up all of those issues one after another" — full sweep, no cherry-picking.

**Wants the right thing, not the fast thing.** "Only duplicate existing observatory for now. Closely model it and write tests to prove" — evidence-first, prove it works before expanding. The 3-bug fix + snapshot tests approach was exactly what he wanted.

**Stops cleanly.** "This is a good place to pause" — knows when to wrap. Doesn't push past natural stopping points.

**Values documentation as part of completion.** This session: "update all the documentation... add memory for you and I... spec log... add agent skills." Documentation isn't an afterthought — it's part of done.

---

## Preferences (from this project)

| Preference | Detail |
|------------|--------|
| Python standard | uv, ruff, Google docstrings, frozen Pydantic, StrEnum, `extra='forbid'` |
| Docstring philosophy | Literate — explain WHY, not just WHAT; rationale embedded in code |
| Test philosophy | Proof, not coverage metrics. Tests prove the system works. |
| Commit style | Detailed multi-line commit messages with explicit task IDs |
| Rate limit | 0.8s between OW requests — immutable, never discuss |
| Slugs | Stable identifiers. Never rename after first write. |
| Content fidelity | No editorialising. Mirror, don't interpret. |

---

## Decisions Made This Project

All decisions are also logged in `meta/SPEC_LOG.md` — this section is a quick-reference summary.

| Decision | SPEC |
|----------|------|
| Almanac is content-only; agent logic in parent workspace | SPEC-001 (superseded) |
| Slugs are stable identifiers | SPEC-002 |
| Two license tracks: CC BY-NC-SA + MIT | SPEC-003 |
| `ParsedArticle` frozen dataclass instead of dict | SPEC-004 |
| `ruamel.yaml` for frontmatter serialisation | SPEC-005 |
| Sentinel-file walk for `ALMANAC_ROOT` | SPEC-006 |
| Import queue externalised to YAML | SPEC-007 |
| Named pipeline for `html_to_markdown` | SPEC-008 |
| `_convert_inline` must precede `_convert_block_elements` | SPEC-009 |
| `split_frontmatter` raises on unclosed blocks | SPEC-010 |
| `almanac.parsing` as single extraction surface | SPEC-011 |
| `docs_dir: docs`, not `docs_dir: .` | SPEC-012 |
| `awesome-pages` plugin for nav | SPEC-013 |
| `git-revision-date` fallback always on | SPEC-014 |
| `frozen=True, extra='forbid'` on all Pydantic models | SPEC-015 |
| `the-observatory` slug exempt from author profile | SPEC-016 |
| Two-strategy body detection | SPEC-017 |
| Native agent infrastructure in almanac repo | SPEC-018 |

---

## What He Cares About Most

1. **Correctness over speed.** The scraper must faithfully mirror OW. Test it against real HTML fixtures. Don't claim it works without proof.
2. **The engineering is the product.** The code structure, docstrings, and architecture matter as much as the content output.
3. **Infrastructure for Jan.** Everything built here serves Jan's research platform. Quality reflects on the whole Phosphene vision.
4. **No technical debt tolerated.** When the review surfaced 18 issues, he wanted all of them fixed in one sweep.

---

## Open Items He'd Care About

- C-003: 11 areas still entirely empty — OW has content for most of them; needs systematic discovery
- C-004: Author profiles are stubs — enriching them would improve the site quality
- I-003: Social cards — Material social plugin would significantly improve link sharing
- I-004: Validator as hard CI gate (currently `continue-on-error: true`)
