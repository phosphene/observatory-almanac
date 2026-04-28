---
uri: team/requirements/jan-almanac-brief
owner: feelingflowingbot
updated: 2026-04-28
status: open — awaiting Jan's input
description: Requirements collection brief for Jan (marsyas6) on the Observatory Almanac concept, modularity, and reproduction. This document frames the questions, not the answers.
---

# Observatory Almanac — Requirements Brief for Jan

**To:** Jan (marsyas6)  
**From:** Ed Phil + Flow  
**Status:** Open — needs Jan's input  
**Context:** The infrastructure is built. Before we go further, we need your thinking on what this thing actually *is* and where it goes.

---

## What We've Built (30-Second Summary)

The Observatory Almanac is a structured git repository that mirrors observatory.wiki. Every article is a markdown file with YAML frontmatter: title, area, author, date, summary, tags, license. Validated by a Pydantic schema. Published as a searchable MkDocs site. Scraped from OW by a bot.

**Current state:** ~190 documents, 29 authors, 20 subject areas, live at [ind-media.github.io/observatory-almanac](https://ind-media.github.io/observatory-almanac).

The infrastructure is sound. What it needs now is *your* mental model of what an almanac is and does.

---

## The Core Question: What Is an Almanac?

The historical almanac — Farmer's Almanac, World Almanac, Old Moore's — was a specific kind of publication. Not a newspaper (ephemeral). Not an encyclopedia (exhaustive). Not a textbook (pedagogical). An almanac was:

- **Annual and authoritative** — one edition per year, curated by experts
- **Reference, not narrative** — you look things up; you don't read it cover to cover
- **Predictive and practical** — tide tables, crop calendars, weather forecasts; structured to help you act
- **Complete within its scope** — if it covers weather, it covers all the weather you need

The Observatory already does something like this for *current expert knowledge*. The question is: what does the Almanac add that the Observatory doesn't already have?

### Three Candidate Framings

We're not committing to any of these — we want to know which one (or what combination) matches how you think about it:

**A — The Almanac as Archive**  
The Observatory is a live feed of expert knowledge. The Almanac is its structured, permanent record. OW articles age. The Almanac freezes them in versioned, citable form. Value: durable reference, not subject to link rot or content changes.

**B — The Almanac as Research Infrastructure**  
The Almanac is for researchers and journalists who need to build on OW content programmatically — filter by area, retrieve by tag, get summaries without reading full articles. A structured API over OW's knowledge. Value: machine-readable layer that enables new tools.

**C — The Almanac as Public Reference**  
The Almanac is a standalone product for the public — the place you go to understand a topic. Less like a mirror of OW, more like a curated guide: "here's what you need to know about the environment." Value: public knowledge product independent of OW's UX.

---

## The Modularity Question

You mentioned wanting it to be modular. That word can mean several different things architecturally. Which of these is closest?

**M1 — Area independence**  
Each of the 26 areas (Science, Environment, History, etc.) can be used independently. Someone who only cares about Environment gets the Environment module — its own index, its own site section, its own feed. The areas don't depend on each other.

**M2 — Embeddable components**  
Individual articles or area summaries can be embedded in other contexts — Observatory.wiki, ind.media, a Telegram bot, a research brief. The almanac generates components, not just pages.

**M3 — Reproducible template**  
The almanac pattern itself is modular: the schema + scraper + validator + MkDocs stack can be reproduced for any MediaWiki-based publisher. Point it at a different wiki, get a new almanac. IMI runs the Observatory Almanac; another org runs their own.

**M4 — Annual editions**  
Each year is a module — a snapshot of what the Observatory published. Volume 1 (2024), Volume 2 (2025). The living version is the current edition; past volumes are archived.

---

## The Reproduction Question

"How can it reproduce itself" is an interesting framing. A few possible meanings:

**R1 — Self-updating**  
The almanac monitors Observatory.wiki for new articles and automatically adds them. It reproduces itself continuously without human intervention. (The scraper is already built for this; it needs a scheduler.)

**R2 — Pattern reproduction**  
The process of building the almanac can be reproduced: same schema, same scraper, same validation, same CI pipeline, pointed at a different content source. Another IMI project, another MediaWiki, another structured knowledge platform.

**R3 — Content reproduction**  
The almanac's content can be reproduced in different formats — the same structured data produces the MkDocs site, a PDF almanac, a JSON API, a Telegram bot's knowledge base. One source, many surfaces.

**R4 — Editorial reproduction**  
The curation process itself can be reproduced — a playbook for how to select articles, assign areas, write summaries, and maintain quality over time. Reproducible as a *practice*, not just a pipeline.

---

## Questions That Need Your Answers

Please give us your thinking on as many of these as you want to. Short answers are fine. We're trying to build a model of what you want, not write a spec.

### On the concept
1. In one sentence: what is the Observatory Almanac *for*?
2. Who uses it? Describe the person who gets the most value from it.
3. What's the difference between using the Observatory and using the Almanac?
4. Is an "almanac" the right word for this, or is it a container you're filling with a different idea?

### On modularity
5. When you say "modular" — what do you picture? What would a *module* look like?
6. Should someone be able to use the Science area without knowing the Environment area exists?
7. Can the almanac be forked or reproduced by a different publisher? Should it?

### On reproduction
8. Should the almanac update automatically as OW publishes new articles?
9. Are annual editions meaningful to you, or is a living/continuous model better?
10. What would it mean for the almanac to "reproduce itself"?

### On the 26 areas
11. Do the current 26 areas cover what you want? What's missing?
12. Are there areas that should be split (too broad) or merged (too narrow)?
13. Is there content you want in the almanac that isn't on Observatory.wiki?

### On the relationship to ind.media and Observatory.wiki
14. How does the almanac fit into the ind.media ecosystem?
15. Should the almanac feed back into Observatory.wiki (e.g., structured tags, backlinks)?
16. Is there a point at which the almanac *becomes* the observatory, rather than mirroring it?

---

## What Happens After You Answer

Ed Phil and Flow will:
1. Update `team/ROADMAP.md` with your framing
2. Define what "modular" means architecturally (which M-type above)
3. Define what "reproduce" means operationally (which R-type above)
4. Identify any schema changes needed to support your model
5. Build Phase 2 and 3 around your answers

Nothing we've built is locked in. The schema can change. The taxonomy can change. The name can change. What we've built is a solid container — you're defining what it holds.

---

## Notes for Ed Phil and Flow

When Jan responds:
1. Record his answers as amendments to this file (`## Jan's Answers` section below)
2. Update `team/ROADMAP.md` Phase 2 and 3 milestones
3. Log any architectural decisions triggered by his answers in `meta/SPEC_LOG.md`
4. Open new tasks in `meta/TASKS.md` as needed

---

## Jan's Answers

*(Pending.)*
