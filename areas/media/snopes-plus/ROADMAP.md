---
title: "Truth Vault Roadmap"
status: living
created: 2026-06-14
updated: 2026-07-17
owner: observatory-editorial
---

# Truth Vault — Roadmap

Living roadmap for the Snopes+ / Truth Vault library. This document tracks what
we have, what's in the pipeline, and what we're building toward.

---

## Current State (2026-07-17)

| Metric | Count |
|--------|-------|
| Published entries | 1,333 |
| On GitHub (`truthvault` branch) | 1,333 |
| On `origin/main` | 449 |
| Topic bank (candidates) | 6,555 |
| Remaining candidates | ~5,222 |
| Words produced (est.) | ~3.5M |

### Source Material Inventory

| Source | Available topics | Status |
|--------|-----------------|--------|
| Snopes timeless (Science, Lifestyle, Entertainment) | ~9,327 timeless articles | 221 in production queue |
| Wikipedia common misconceptions | ~300 misconceptions | 86 in production queue |
| Wikipedia urban legends | ~200 legends | Catalogued |
| Lateral sources (RationalWiki, SBM, IFLScience) | Thousands | Surveyed, not yet queued |
| Original EARC seed claims (manifesto Section 6) | 40 | 10 completed, 30 remaining |

---

## The Product

### What It Is
Independent epistemological review of fact-checking — not anti-Snopes, but
the next layer. Each entry audits the entire epistemic chain:

1. **Claim Fidelity** — Does Snopes accurately represent the claim as it circulates?
2. **Review Epistemology** — What sources and methods does Snopes use?
3. **Conclusion Epistemology** — How do they get from evidence to verdict?
4. **The Wider Field** — Folk wisdom, phenomenology, academic jargon ecology, empirical deep-cuts

### EARC Framework
Every entry is tagged with a processing mode:

| Mode | Description |
|------|-------------|
| **E** — Enhance | Snopes got it right; we add depth, context, wider field |
| **A** — Augment | Snopes is partially right; we fill gaps and add nuance |
| **R** — Replicate | We independently verify and either confirm or diverge |
| **C** — Contrast | We reach a materially different conclusion with evidence |

### Four Gap Categories
Claims that journalistic fact-checking can't reach well:

| Category | % of corpus | Description |
|----------|------------|-------------|
| Distorted-but-Grounded | 42.4% | Real phenomenon, distorted in representation |
| Epistemologically-Loaded | 21.8% | Question presupposes contested frameworks |
| Contested-Consensus | 20.6% | Evidence genuinely divided or evolving |
| Phenomenologically-Real | 14.8% | Experience is genuine, proposed mechanism is wrong |

**The kernel-of-truth finding:** >70% of persistent false beliefs contain a
demonstrably true core. Correction requires accounting for what's real, not
just declaring "false."

---

## Articles in Development

### Meta-Analysis Series
- [x] **"How Truth Gets Made"** — Landscape analysis of 1,400 contested
  claims. Draft complete (`truth_vault/drafts/meta-analysis/how-truth-gets-made.md`).
  Findings: kernel-of-truth at 70%+, belief mechanism taxonomy, four gap
  categories derived from corpus study.

### Manifesto / About Page
- [x] **"The Snopes+ Library: An Independent Epistemological Review"** —
  Full methodology document with Snopes audit (8,900+ words).
  Published: `areas/media/snopes-plus-library.md`

### Research Products (Open TODOs from topic discussions)
- [ ] **Folk Wisdom Index** — Structured reference of what folk claims actually track.
  Systematize the "epistemic archaeology" of real phenomena underneath
  propositionally wrong folk claims.
- [ ] **Epistemology of Verdict** — Running analysis of fact-checking as cultural
  phenomenon. How verdict structures shape public epistemics.
- [ ] **Cross-Reviews** — Same claim across multiple fact-checkers. Consistency
  analysis of fact-checking ecosystem.
- [ ] **Snopes Archival Audit** — The Wayback Machine blackout (pre-2021),
  lost articles, the Mikkelson retraction gap. What's gone and what it means.

---

## Production Pipeline

### Topic Sources (Priority Order)

1. **Snopes Timeless Queue** (221 topics ready)
   - Science & Technology: 1,207 timeless articles identified
   - Lifestyle: 134 timeless articles
   - Entertainment: 2,230 timeless articles
   - Filtered from 14,809 total Snopes articles crawled across 4 categories

2. **Wikipedia Misconceptions** (86 topics ready)
   - Arts & Culture, History, Science/Tech/Math sub-articles
   - ~300 individual misconceptions, structured with citations
   - CC-licensed, fully scrapeable via MediaWiki API

3. **Snopes Final Gap** (318 URLs)
   - Snopes URLs not yet covered by our library

4. **Snopes Truly-Timeless Gap** (647 URLs)
   - Subset of timeless content we haven't touched

5. **Topic Bank** (6,555 candidates total)
   - Consolidated from all sources with deduplication
   - Each tagged with EARC mode and gap category

### Lateral Sources (Surveyed, Not Yet Queued)
- **RationalWiki** — Deep pseudoscience & alt-med coverage
- **Science-Based Medicine** — Rigorous medical claim analysis
- **IFLScience / Live Science / Mental Floss** — Popular science myths
- **Full Fact / PolitiFact** — Primarily current-events, thin on timeless
- **Academic datasets**: FACTors (118K claims), Kaggle (4,525), Harvard (11,639)
- **Books**: Lilienfeld et al. (*50 Great Myths of Popular Psychology*),
  Goldacre (*Bad Science*)

---

## Analytics & Tooling

### Truth Vault Python Package
Location: `lib/python/truth_vault/`

Provides:
- Schema validation (Pydantic models, EARC modes, gap categories)
- Inventory scanning and statistics
- Duplicate detection
- Candidate management with collision detection
- TaskFlow integration for manifest-driven production
- Analytics pipeline: parse → match → classify → record → aggregate

### Key Data Files
| File | Contents |
|------|----------|
| `topic_bank.json` | 6,555 candidate topics with metadata |
| `drafts/production-queue.json` | Active queue (221 Snopes + 86 Wikipedia) |
| `drafts/snopes-categories-summary.md` | 14,809 Snopes articles by category |
| `drafts/lateral-sources.md` | Survey of non-Snopes myth/misconception sources |
| `drafts/snopes-timeless-gap.json` | 647 uncovered timeless Snopes URLs |
| `drafts/meta-analysis/corpus-report.json` | Analytics output from corpus study |

---

## Publication Path

```
Topic bank → Production run → Entry written to areas/media/snopes-plus/
  → Committed to truthvault branch → PR to main → Pipeline → observatory.wiki
```

All entries follow Observatory Almanac schema:
- Area: `media`
- Type: `article`
- Author: `observatory-editorial`
- License: `CC BY-NC-SA 4.0`
- Minimum 2,500 words per entry

---

## Snopes Landscape (Reference Numbers)

- **32,134** total Snopes URLs across 362 monthly sitemaps (Sept 1995 – present)
- **19,792** dedicated fact-check reports (FACTors SIGIR 2025 dataset)
- **20** rating labels (16 active, 4 retired)
- **69** authors over 29.3 years
- Pre-2021: **no Wayback Machine copies** (Snopes blocked archival crawling)
- Current: blocks ClaudeBot, GPTBot, PerplexityBot, CCBot; `ai-train=no`
- No public API
- Methodology explicitly ad hoc — no reviewable epistemological framework
