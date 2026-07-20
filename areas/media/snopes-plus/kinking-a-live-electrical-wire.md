---
title: "Does Kinking a Live Electrical Wire Stop Electricity and Make it Safe?"
snopes_url: "https://www.snopes.com/fact-check/kinking-a-live-electrical-wire/"
snopes_verdict: "False"
verdict_short: false
published: 2026-07-20
updated: 2026-07-20
author: "Bethania Palma"
snopes_author: "Bethania Palma"
snopes_published: "2016-08-26"
categories:
  - science
  - safety
  - electricity
  - social-media-dangers
tags:
  - electrical safety
  - electrocution risk
  - physics
  - meme
  - iFunny
  - natural selection
  - Ohm's Law
  - dangerous misinformation
earc: C
epistemic_gap: low
---

## §1 · Claim & Verdict

An image circulating primarily on Facebook and other social media platforms in 2016 claimed that bending or "kinking" a live electrical wire would stop the flow of electricity through it, rendering it safe to work on — by analogy with the common experience of kinking a garden hose to stop water flow. The accompanying text read: "If you need to work on something electrical but don't know where the breaker panel is, simply kink the wire like a garden hose to stop the flow of electricity." The implication was that this technique could be used as a safe substitute for turning off the electrical supply at the circuit breaker before beginning electrical work.

Snopes rated this claim **False**, and the rating has a dimension of urgency not present in most other Snopes verdicts: this is dangerous misinformation whose practical application could result in serious injury or death. Bill Elarton, chair of Construction, Maintenance and Utilities at Los Angeles Trade-Tech College, told Snopes reporter Bethania Palma: "Nothing short of breaking the wire will stop the flow of electricity, and that's not safe either." Elarton further noted that even then, physically breaking a wire does not render the electrical system safe — it merely introduces a different set of hazards, and would defeat the purpose of attempting a repair.

## §2 · Context & Background

The meme originated, according to the Snopes investigation, from the website iFunny.com, specifically within a section tagged #NaturalSelection — a community predicated on darkly ironic humor about self-inflicted injuries as a form of evolutionary pressure on the population. The tagging context makes clear that the original post was almost certainly intended as a joke rather than sincere safety advice. The danger lies precisely in the fact that jokes shared on one platform migrate to others stripped of their ironic context: when the image circulated on Facebook without the iFunny/#NaturalSelection framing, it appeared to be a genuine household tip.

This pattern — dangerous fake advice circulating under the cover of stripped irony — represents a recognized category of social media hazard distinct from ordinary misinformation. A person who encounters the iFunny post in context can recognize the #NaturalSelection tag as a signal that the "advice" is satirical. A person who encounters a screenshot or reshared image on a home improvement Facebook group, or who finds the image via a search while actually facing an electrical problem, lacks that contextual cue and may treat it as genuine guidance.

The specific analogy invoked — water flow through a kinked hose — has genuine intuitive appeal, which is part of what makes this meme both plausible-seeming and dangerous. The hydraulic analogy for electrical circuits is actually a legitimate pedagogical tool: voltage is analogous to water pressure, current to flow rate, and resistance to pipe diameter or constriction. In this framing, kinking a wire — adding a "constriction" — might be expected to reduce current flow. The analogy is widely used in introductory physics and electrical engineering education precisely because it captures something real about the relationship between circuit parameters (Glover et al., 2012, *Power System Analysis and Design*). The problem is that the analogy breaks down at the very point where the meme applies it: a physical kink in a wire, unless it creates an open circuit by breaking the conductor, does not meaningfully impede current flow in the way that a kink in a hose nearly completely stops water flow. The reasons for this failure involve the underlying physics of electrical conduction and mechanical deformation of conductors.

## §3 · Epistemic Analysis & Novelty

The epistemic novelty in this entry concerns the specific failure mode of **pedagogical analogy inversion** — a process by which a simplified teaching metaphor that conveys approximately correct intuitions within its pedagogical scope is misapplied outside that scope in ways that generate dangerously incorrect predictions.

The water-flow/electricity analogy is a genuine and valuable teaching tool. It correctly conveys that increasing "constriction" (resistance) reduces flow (current) at a given pressure (voltage). However, the analogy fails to convey several critical properties of electrical conductors that have no hydraulic counterpart. First, the relationship between physical compression of a wire and resistance change is dramatically different from the relationship between hose constriction and flow reduction. When you kink a garden hose, you create a near-complete seal, reducing water flow to near zero with relatively small deformation. When you kink an electrical wire, the actual electrical resistance of the conductor changes very little, because electrical conduction in metals depends on the quantum mechanics of electron movement through the metal lattice, not on the geometric cross-sectional area in the way that laminar fluid flow depends on pipe diameter (Griffiths, 1999, *Introduction to Electrodynamics*; Ashcroft & Mermin, 1976, *Solid State Physics*).

Second, kinking a wire in a way that physically creases or compresses the conductor may actually introduce localized heating at the kink point — not because resistance is dramatically increased throughout the wire, but because if contact resistance at the kink point increases locally, current forcing through that elevated-resistance point will generate heat (P = I²R), potentially reaching temperatures sufficient to ignite the insulation jacket or surrounding materials. This is the mechanism underlying many electrical fires at connection points, splice junctions, and corroded contacts (NFPA, 2019, *NFPA 70E: Standard for Electrical Safety in the Workplace*; Babrauskas, 2003, *Ignition Handbook*).

Third — and perhaps most safety-critically — the hydraulic analogy conveys nothing about the physiological effects of electrical contact, which are profoundly different from the effects of water contact. Elarton's point about skin resistance is important: dry human skin has an electrical resistance of approximately 100,000 ohms under dry conditions, which provides a meaningful barrier to lethal current at household voltages. However, wet skin can drop this resistance to 1,000 ohms or lower (Dalziel & Lee, 1968, *Transactions of the IEEE Industry and General Applications Group*). A person working on a live wire in hot conditions — perspiring — has dramatically reduced skin resistance and faces a proportionally higher risk of lethal shock. A person who has been told that "kinking" the wire has made it safe may be more likely to handle it without the caution they would otherwise apply, eliminating the behavioral safety margin that might have compensated for physiological risk.

A fourth dimension involves the neurophysiological mechanism of electrocution: when a person contacts a live wire and sufficient current passes through the body, the current can cause involuntary muscle tetanic contraction — the person's hand clamps down on the wire rather than releasing it (Ohashi et al., 1999, *Legal Medicine*). Elarton specifically mentioned this: "when people get shocked that phenomenon can cause muscles to contract — and instead of dropping a wire, you can clamp down on it. This can be fatal." This physiological mechanism reverses the intuitive assumption that a person can simply let go of a hazardous object. The same mechanism underlies the "let-go current" threshold established in electrical safety research: the maximum current at which a person can voluntarily release a grasped conductor is approximately 6–9 mA for adult males; at higher currents, voluntary release becomes impossible and the duration of contact extends until extrinsic separation or physiological disruption of cardiac rhythm (Dalziel & Lee, 1968).

## §4 · Scientific Evidence

The physics underlying the meme's falseness is straightforward and not scientifically contested. A brief review of the relevant principles follows.

**Ohm's Law and conductor resistance:** Electrical resistance in a metal conductor is governed by R = ρL/A, where ρ is the resistivity of the material, L the length of the conductor, and A its cross-sectional area (Hayt & Kemmerly, 2012, *Engineering Circuit Analysis*). For a copper household wire, ρ is approximately 1.7 × 10⁻⁸ Ω·m. Kinking the wire introduces a local geometric deformation but does not meaningfully change the bulk resistivity of the copper or the effective cross-sectional area through which current flows — the electrons conducting current in a metal occupy the entire conductor volume through the quantum mechanical phenomenon of band conduction (Kittel, 2004, *Introduction to Solid State Physics*). The kinked geometry might slightly increase the effective conductor length through the deformed region, but this effect is negligibly small compared to the overall circuit resistance. Under typical household wiring conditions (12 AWG or 14 AWG wire, 120V or 240V service), the resistance change induced by kinking would be too small to measure with consumer-grade instruments.

**Current path and body conductance:** Human tissue conductance has been measured across decades of research; the key finding for safety assessment is that path, duration, and current magnitude all determine the severity of electrical shock (Dalziel & Lee, 1968; IEEE Standard 80, 2013, *Guide for Safety in AC Substation Grounding*). Currents as low as 10–20 mA across the chest can induce ventricular fibrillation under some conditions; currents of 100 mA or more are almost universally lethal if sustained for more than a fraction of a second. At 120V household current and even with dry skin (100,000 Ω resistance), the Ohm's Law current would be 1.2 mA — near the threshold of perception. With wet skin (1,000 Ω), the same voltage drives 120 mA — well into the lethal range. Whether a wire is kinked does not alter these calculations; what alters them is whether the circuit is de-energized.

**Professional standards:** The NFPA 70E standard (2019) and OSHA 29 CFR 1910.331-1910.360 require electrical workers to treat all conductors as energized unless confirmed de-energized by lockout/tagout procedures. These standards reflect the accumulated industry knowledge, including fatality data, indicating that the only reliably safe approach to electrical work is confirmed de-energization — not any work-around technique claimed to render live wires safe.

## §5 · Verdict Evaluation

Snopes' "False" verdict is unambiguously correct, well-supported by physical principles and direct expert testimony. The rating is not merely accurate but serves an important public safety function. Unlike many Snopes fact-checks addressing false or misleading claims whose practical impact is primarily epistemic (people believe something untrue), this case involves a false claim whose practical application creates direct risk of electrocution, electrical fire, and death.

The fact-check integrates expert testimony from a credentialed electrical safety educator (Elarton, chair of Construction, Maintenance and Utilities at LA Trade-Tech College), references to professional safety standards and practices, and straightforward application of physical principles. The article is relatively brief by Snopes standards but offers all information necessary to refute the claim and crucially includes the correct alternative behavior ("if you have an electrical problem, call in a professional trained to deal with it... make sure all power is off and nothing is live before you do").

One area where the fact-check could have added epistemic value would have been a more explicit discussion of the hydraulic analogy's pedagogical validity and its specific failure modes here — the fact that the intuition "kinking reduces flow" works for water and fails for electricity because of fundamental differences in the mechanisms of fluid flow versus electron conduction. Making this explicit would help readers understand not just that the claim is false but why it is false in a way that immunizes against similar analogical errors in the future. As the fact-check stands, it correctly identifies the danger and supports that identification with expert authority, which appropriately prioritizes safety over analytical depth given the stakes.

## §6 · Epistemic Gap & Further Research

The primary gap this entry identifies is the lack of systematic research into the specific category of "stripped-irony misinformation" — dangerous false claims that originate in satirical or ironic contexts and become genuinely harmful when de-contextualized. The iFunny/#NaturalSelection origin of this meme is a clear example: within its original context, the humor signal (the #NaturalSelection hashtag implying the audience should not follow this advice) was present. The stripped-context resharing removed that signal. Characterizing this category of misinformation, its prevalence relative to other categories, and the contexts in which irony-signal stripping is most likely to occur would be a useful contribution to the misinformation studies literature.

A second gap concerns outcome data: how many electrical injuries or fatalities annually might be attributed to misinformation-driven DIY electrical work? The CPSC tracks electrical-related injuries and fatalities in general, and OSHA tracks occupational electrical fatalities, but to the author's knowledge there is no systematic effort to distinguish misinformation-induced incidents from ordinary accidents. Such data would help quantify the harm that safety-specific misinformation causes and could inform platform safety policies.

Third, the pedagogical dimension deserves attention: how should introductory electrical education present and delimit the hydraulic analogy to prevent the misapplication documented here? Research in physics education (Gentner & Gentner, 1983, *Mental Models*; Chi et al., 1994, *The Journal of the Learning Sciences*) suggests that novice learners tend to over-extend analogies beyond their intended scope. Experimental work examining whether explicitly teaching the limits of the hydraulic analogy (including the kinking-is-not-resistance point) reduces misapplication incidents would contribute both to physics education and to broader safety communication research.

---

### References

- Ashcroft, N.W., & Mermin, N.D. (1976). *Solid State Physics*. Holt, Rinehart and Winston.
- Babrauskas, V. (2003). *Ignition Handbook: Principles and Applications to Fire Safety Engineering, Fire Investigation, Risk Management and Forensic Science*. Fire Science Publishers.
- Chi, M.T.H., et al. (1994). Eliciting self-explanations improves understanding. *Cognitive Science*, 18(3), 439–477.
- Dalziel, C.F., & Lee, W.R. (1968). Lethal electric currents. *IEEE Spectrum*, 5(2), 44–50.
- Gentner, D., & Gentner, D.R. (1983). Flowing waters or teeming crowds: Mental models of electricity. In D. Gentner & A. Stevens (Eds.), *Mental Models* (pp. 99–130). Lawrence Erlbaum Associates.
- Glover, J.D., et al. (2012). *Power System Analysis and Design* (5th ed.). Cengage Learning.
- Griffiths, D.J. (1999). *Introduction to Electrodynamics* (3rd ed.). Prentice Hall.
- Hayt, W.H., & Kemmerly, J.E. (2012). *Engineering Circuit Analysis* (8th ed.). McGraw-Hill.
- IEEE. (2013). *IEEE Standard 80: Guide for Safety in AC Substation Grounding*. IEEE.
- Kittel, C. (2004). *Introduction to Solid State Physics* (8th ed.). Wiley.
- NFPA. (2019). *NFPA 70E: Standard for Electrical Safety in the Workplace*. National Fire Protection Association.
- Ohashi, M., et al. (1999). Electrocution: A review with special reference to medicolegal aspects. *Legal Medicine*, 1(1), 22–30.
- OSHA. 29 CFR 1910.331–1910.360. *Electrical Safety-Related Work Practices*. Occupational Safety and Health Administration.
