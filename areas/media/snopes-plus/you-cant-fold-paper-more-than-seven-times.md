---
title: "\"You Can't Fold a Piece of Paper More Than Seven Times\""
area: media
type: article
author: Observatory Editorial
author_slug: observatory-editorial
source: Observatory Almanac
source_url: https://observatory.wiki
license: CC BY-NC-SA 4.0
published: 2026-07-20
updated: 2026-07-20
series: The Truth Vault
earc_mode: R
gap_category: conditionally-true
snopes_url: https://www.snopes.com/fact-check/paper-fold/
snopes_verdict: mixture
summary: >
  For standard letter-size paper, seven or eight folds is indeed the practical limit — but this is a consequence of shrinking area and growing thickness, not some inherent physical law. With a large enough sheet, far more folds are achievable.
tags:
  - truth-vault
  - mathematics
  - paper-folding
  - exponential-growth
  - physics
  - recreational-mathematics
  - origami
  - Britney-Gallivan
---


# "You Can't Fold a Piece of Paper More Than Seven Times"


## 1. The Claim

This is one of the most widely repeated "fun facts" in popular science communication: a piece of paper cannot be folded in half more than seven times, no matter how hard you try or how strong you are. The claim circulates in classrooms, in science popularization materials, in pub quiz circuits, and across social media, usually accompanied by a vague explanation about paper becoming too thick to fold further. It appears in school textbooks in multiple countries and is frequently deployed as an example of exponential growth.

The claim typically comes packaged with an implicit or explicit universality: *any* piece of paper, regardless of size, material, or who is doing the folding, obeys this seven-fold limit. In some versions the limit is given as eight folds rather than seven, a small inconsistency that reveals the intuitive rather than empirically derived origin of the specific number.

The appeal of the claim is its apparent paradox: paper seems flimsy, yet folding it just a few times makes it too thick to fold further. The underlying mathematics — fold a piece of paper 42 times and it would theoretically reach the Moon — is genuinely remarkable, and the claim is often used as a gateway to discussions of exponential growth. Unfortunately, the specific "seven folds" assertion is misleading in ways that matter.


## 2. What's Actually True

The seven-fold claim is what might be called a *circumstantially true statement presented as a universal law*. It is accurate for standard-sized paper under typical conditions, but it is definitively false as a general claim, having been falsified numerous times by empirical demonstration.

**The mathematics of folding:** Each time a piece of paper is folded in half, the number of layers doubles and the surface area halves. After *n* folds in the same direction, the paper has 2^n layers and 1/2^n of its original area. This is genuine exponential growth of thickness. Starting with standard printer paper approximately 0.1 mm thick, after 7 folds the stack is 0.1 × 2^7 = 12.8 mm thick — roughly the thickness of a trade paperback book spine. After 8 folds: 25.6 mm. After 10 folds: 102.4 mm — over 10 centimeters. The mathematics is unambiguous.

**Why standard paper stops around 7–8 folds:** The practical limit for ordinary paper folds is reached when the radius of curvature required to complete the next fold cannot be achieved given the thickness of the stack. The ratio of the crease radius to paper thickness is constrained by the paper's physical properties. As thickness increases exponentially but available paper length decreases by half with each fold, a point is reached where there is not enough remaining paper to wrap around the entire stack thickness. This is the physical mechanism, and it is a function of the ratio of original paper area to paper thickness — not a universal physical constant.

**Britney Gallivan's formal solution:** In 2001, then-high-school student Britney Gallivan set out to formally prove whether the limit was real or an artifact of paper choice. She derived the mathematical formula for the maximum number of folds as a function of paper dimensions, known today as the Gallivan Equation. For folding in a single direction, the limit *n* is given by: *L = (π·t/6) × (2^n + 4)(2^n - 1)*, where *L* is the length of the paper, *t* is the paper thickness, and *n* is the number of folds. This equation, first published in Gallivan's 2002 booklet *How to Fold Paper in Half Twelve Times* (Historical Society of Pomona Valley), predicts that a sufficiently long piece of paper imposes no fixed seven-fold ceiling — it simply sets the minimum length required for each additional fold.

Gallivan subsequently demonstrated her equation empirically. Using a 1,219-meter (roughly 4,000-foot) roll of single-ply toilet paper, she folded it in half 12 times — definitively shattering the "seven is the maximum" rule (Gallivan, 2002). The accomplishment was acknowledged in the American Mathematical Society's *What's Happening in the Mathematical Sciences* (volume 6).

**The MythBusters confirmation:** In 2007, the television program *MythBusters* conducted a large-scale empirical test using a sheet of paper the size of an airplane hangar floor. The team achieved 11 folds before stopping not because of any physical impossibility but because of equipment and practical constraints. This independently confirmed Gallivan's theoretical prediction that large paper allows many more folds.

**The correct statement of the constraint:** The precise, accurate statement is: for a standard US letter-size sheet (approximately 0.1 mm thick, 28 × 22 cm), approximately seven to eight folds in alternating directions (or seven in a single direction) are achievable before the geometry becomes physically impossible. This is not a universal rule: it is a property of the particular ratio of that paper's size to its thickness.


## 3. Why People Believe This

**The claim exploits the non-intuitive nature of exponential growth:** Exponential doubling is notoriously counter-intuitive for humans. When told that paper doubles in thickness with each fold, most people's intuitions about how quickly this grows are systematically wrong. The famous rice-on-chessboard problem produces the same intuitive failure: successive doublings seem manageable at first and then suddenly overwhelming. This is the genuine core of an accurate insight — exponential growth is surprising — but the seven-fold limit attaches that genuine insight to a false universal rule.

**Personal experience appears to confirm it:** Anyone who has tried to fold a piece of standard printer paper will quickly find that around fold seven or eight, it becomes effectively impossible. The stack is thick, the remaining paper is small, and the required force is enormous. This personal experience, which every person can reproduce at home, provides what feels like powerful empirical confirmation of the claim. The problem is that the experience confirms only that the limit applies to *that particular piece of paper* — not to paper universally.

**The claim is pedagogically convenient:** Teachers deploying this claim to introduce exponential growth have strong incentive to overstate its universality. "You can't fold paper more than seven times" is memorable and verifiable in the classroom right now. "With a piece of paper large enough, you can beat the limit, but with standard letter-size paper you cannot" is less crisp and pedagogically awkward. The simplification to a universal rule improves the lesson while destroying its accuracy.

**The mechanism is invisible:** When you try to fold paper for the seventh or eighth time and fail, you cannot determine by inspection whether you failed because of a universal physical law or because of a contingent fact about the specific paper you're using. The failure feels total and inexplicable, and the "explanation" provided by the seven-fold claim fills the gap. Without Gallivan's mathematics or access to a very large piece of paper, there's no obvious way to test the universality of the claim.

**The claim is categorically ambiguous:** Some versions of the claim specify "in the same direction," others don't. Some specify regular notebook paper, others claim universality. This vagueness allows the claim to shift when challenged: if someone reports folding paper nine times, it can be dismissed as "that doesn't count because the folds were alternating" or "that was special paper." This unfalsifiability-by-redefinition helps the claim survive contact with counter-evidence.

**Epistemic novelty of the correction:** Most people who know the seven-fold claim have never heard of Britney Gallivan. The corrective counter-fact — a high-school student formally disproved this in 2001 — is genuinely surprising and underknown. This asymmetry between the wide circulation of the myth and the narrow circulation of the refutation is a recurring pattern in science communication: the catchy false version spreads far further than the accurate but less catchy correction.

**The precise number is memorable in a way the truth is not:** "No more than seven folds" is a specific, memorable claim. "The maximum number of folds depends on the ratio of the paper's surface area to its thickness, as described by the Gallivan equation" is accurate but not memorable. The myth wins the memability competition decisively, which ensures it continues to be repeated in contexts where brevity is valued.


## 4. Verdict

**MIXTURE** — The seven-fold claim is approximately true for standard letter-size paper but is definitively false as a universal physical law. The claim conflates a specific quantitative constraint that applies to ordinary paper with a universal impossibility that applies to paper of any size.

**The accurate core:** For standard printer or notebook paper (~0.1 mm thick, approximately 28 × 22 cm), practical folding in a single direction typically reaches its geometric limit at 7–8 folds. This is real and reproducible by anyone.

**The false generalization:** The claim that no piece of paper — regardless of size — can be folded more than seven times is definitively false. Britney Gallivan (2002) folded a 1,219-meter roll of toilet paper twelve times and formally derived the equation governing folding limits. The *MythBusters* team subsequently achieved eleven folds with a hangar-sized sheet of paper independently. Both demonstrations confirm that the limit is a geometric consequence of the size-to-thickness ratio, not a universal physical constant.

**The correct statement:** The maximum number of times a piece of paper can be folded in half is determined by the formula *L = (π·t/6) × (2^n + 4)(2^n - 1)*, where *L* is the paper's length, *t* is its thickness, and *n* is the number of folds (Gallivan, 2002, *How to Fold Paper in Half Twelve Times*). This means that with sufficiently large paper, arbitrarily many (in principle) folds are achievable as long as enough paper length is available to wrap around the accumulated thickness.

The practical value of the seven-fold claim as a classroom demonstration of exponential growth is real — letting students fold paper until they cannot is a vivid experience. But this educational use should be accompanied by accurate framing: the limit is specific to the paper being used, not universal, and it has been surpassed experimentally by anyone with access to a large enough sheet.


## 5. The Wider Picture

**The Gallivan Equation in context:** Britney Gallivan's derivation represents a significant contribution to recreational mathematics. Her approach was to analyze the relationship between the minimum paper length and the number of single-direction folds, accounting for the fact that at each fold, some paper is "used up" forming the curved crease. Unlike simple models that treat folds as instantaneous events, Gallivan's formula accounts for the semicircular geometry of each crease. The formula has been independently verified by mathematicians and correctly predicts both the physical feasibility of specific fold numbers and the precise paper lengths required to achieve them (Weisstein, *MathWorld* entry "Paper Folding").

This is a case where recreational mathematics — pursuing a popular puzzle seriously — produced a genuine mathematical result. The claim that the seven-fold limit was a universal law was so widely accepted that Gallivan's work in disproving it was essentially original research. The fact that a high-school student accomplished this, operating outside professional mathematics channels, is both a testament to her insight and a mild embarrassment for the mathematical establishment that allowed an incorrect "fact" to circulate as truth for decades.

**Exponential growth and human intuition:** The paper-folding problem is one of several canonical demonstrations that human intuitions about exponential growth are systematically poor. Others include the rice-on-chessboard problem, compound interest, viral spread, and the Malthusian growth of populations. Research in cognitive psychology and behavioral economics consistently finds that people tend to linearize exponential processes, underestimating how quickly they accelerate (Wagenaar & Sagaria, 1975, *Perception & Psychophysics*, 18(6), 446-450). The paper-folding demonstration leverages this intuitive failure effectively: people don't believe paper could become as thick as a skyscraper in 23 folds, so the seven-fold limit seems correspondingly reasonable as a "safety valve" against such absurdity.

The pedagogical danger is that framing the seven-fold limit as a universal law implicitly misrepresents the nature of exponential growth. The real insight is that exponential growth becomes unmanageable *very quickly* — not that it hits a hard physical limit. Correcting the oversimplification actually sharpens the lesson: it's not that seven folds is impossible to exceed because of some mystical physical barrier; it's that the growth is so fast that ordinary size constraints are almost immediately overwhelmed.

**Alternative folding configurations:** The seven-fold (or eight-fold) limit strictly applies to folding in a single direction. Alternating folds — folding left-to-right, then front-to-back, alternating — distribute the thickness more evenly and allow more total folds than single-direction folding with the same paper. This is why competitive paper-folding attempts typically use alternating folds to maximize fold count. Gallivan's 2002 record of twelve folds was achieved with single-direction folds, meaning alternating-fold configurations may permit higher fold counts at equivalent paper sizes.

The broader category of paper-folding mathematics is a rich field with implications for origami design, surgical tools made from folded materials, and deployable space structures. Origami mathematics — including Huzita-Hatori axioms and computational origami theory — has become an area of serious mathematical research, with applications including the folding of airbag designs (for maximum compactness) and deployable telescope lenses (Demaine & O'Rourke, 2007, *Geometric Folding Algorithms*, Cambridge University Press).

**Myth typology — "circumstantially true universals":** The paper-folding claim belongs to an interesting category of scientific myths: claims that are true in a specific, commonly experienced context but are false as universal statements. This category is distinct from myths that are simply wrong, because the false universal can always point to a genuine true case as its evidential basis. Other examples include "you can't see the Great Wall from space" (true for the naked eye from low Earth orbit, often misrepresented as universally impossible), and "lightning never strikes the same place twice" (statistically false; tall structures are repeatedly struck). These myths are particularly resistant to correction because challenging them seems to contradict personal experience.

**Practical consequences for education:** The widespread use of this claim in educational contexts — with its false universal framing — represents a missed opportunity. Rather than teaching that there is a hard physical limit to folding, educators could accurately teach that the limit is set by geometry and scales with paper dimensions, making the Gallivan equation an accessible real-world example of applied algebra. The corrective version is at least as pedagogically interesting as the mythologized version, with the added benefit of being true.

What's more, Britney Gallivan's story — a high-school student taking a recreational "impossible" challenge seriously, deriving a formal equation, and then empirically validating it with a roll of toilet paper — is a more inspiring science narrative than "and that's just how physics works." It illustrates that seemingly settled popular-science claims can be wrong, that mathematics can be applied to playful problems with serious results, and that individual investigation can correct widely accepted myths.


## 6. How Fact-Checkers Handle It

Snopes rates this claim a **Mixture**, noting that the seven-fold limit applies to standard paper sizes but has been definitively exceeded with different formats. This rating accurately captures the conditional truth of the claim and its false universalization.

The claim illustrates a category failure in popular science communication: "fun facts" frequently sacrifice accuracy for memorability, replacing nuanced conditional truths ("this is true in these specific circumstances") with false universal laws ("this is always true"). Science communicators operate under pressure to be crisp and quotable; accuracy often suffers. The paper-folding claim has been repeated in textbooks, documentaries, and classroom exercises for decades, despite being publically refuted in 2002 by a high-school student working with toilet paper and basic algebra. This gap between the refutation and the myth's continued circulation is striking, and suggests that the path from "this has been debunked" to "this stops being taught as fact" is very long indeed.
