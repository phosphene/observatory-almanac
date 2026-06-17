# Snopes+ Library — QA Tickets

## T-SP-001: Rewrite 5 phenomenology entries to standard format [CRITICAL]
**Files:** burnout.md, executive-function.md, processing-speed.md, toxic-relationship.md, trauma-response.md
**Issue:** These were written with a 6-component phenomenology framework instead of the standard 7-component EARC framework. Missing earc_mode and gap_category frontmatter. Missing "Claim Statement" and "Snopes+ Verdict" sections.
**Fix:** Rewrite all 5 to match the standard 7-component structure with proper frontmatter.
**Priority:** Critical — structural inconsistency in the library.

## T-SP-002: Pad thin entries to minimum word count [HIGH]
**Issue:** Multiple entries from recent batches are below 1500 words (some as low as 800). The specification is 1500-2500.
**Affected:** elephants-never-forget (800w), bats-blind (817w), laughter-best-medicine (843w), lightning-same-place (849w), selfish-gene (858w), mothers-intuition (862w), cold-weather-sick (884w), ecosystem-business (884w), instinct-jargon (894w), chicken-soup-cold (901w), plus likely 20+ more under 1200w.
**Fix:** Identify all entries under 1200 words and expand with additional research depth, wider field analysis, and more detailed verdict sections.
**Priority:** High — undermines publication quality.

## T-SP-003: Normalize publication dates [LOW]
**Issue:** 110 entries dated 2026-06-14, 29 dated 2026-06-15.
**Fix:** Normalize all to 2026-06-14 (production start date) or use actual file creation date.
**Priority:** Low — cosmetic.

## T-SP-004: Research and add Snopes URLs [MEDIUM]
**Issue:** Only 39/135 entries have actual Snopes URLs. Many claims that Snopes HAS fact-checked are marked "not-addressed."
**Fix:** Systematic search of Snopes.com for each claim; update snopes_url and snopes_verdict fields where applicable.
**Priority:** Medium — improves cross-referencing and credibility.

## T-SP-005: EARC mode distribution rebalancing [LOW]
**Issue:** 79+ Contrast entries, only 3 Replicate. The library is heavily skewed toward C mode.
**Fix:** Future entries should preferentially target Enhance, Augment, and Replicate modes where appropriate. Consider converting some existing C entries to more specific modes where warranted.
**Priority:** Low — editorial balance, not structural.

## T-SP-006: Gap category coverage [LOW]
**Issue:** Epistemologically-loaded (11) is underrepresented vs distorted-but-grounded (31) and contested-consensus (35).
**Fix:** Future entries should target epistemologically-loaded claims. These are the hardest but most valuable entries.
**Priority:** Low — the imbalance reflects natural claim distribution.

## T-SP-007: Verify all cited studies exist [MEDIUM]
**Issue:** Entries cite hundreds of studies by author and year. These are generated from training data and may contain hallucinated or misattributed citations.
**Fix:** Spot-check 10% of citations across the library against actual publication records. Flag and correct any fabricated citations.
**Priority:** Medium — publication credibility depends on citation accuracy.
