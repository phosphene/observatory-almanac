---
title: "\"Put a Wet Phone in Rice to Fix Water Damage\""
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
earc_mode: C
gap_category: folk-remedy-persistence
snopes_url: https://www.snopes.com/fact-check/wet-phone-rice/
snopes_verdict: "False"
summary: >
  The widespread folk remedy of submerging a water-damaged smartphone in dry rice persists
  despite systematic testing showing it performs no better than leaving the device in open air
  and may actively worsen outcomes by introducing starch dust and delaying more effective
  interventions. The claim endures because intuitive folk physics, confirmation bias among
  occasional success stories, and absence of manufacturer endorsement has failed to dislodge
  a practice transmitted primarily through social network urgency.
tags:
  - truth-vault
  - technology
  - smartphones
  - folk-remedies
  - electronics
  - moisture-damage
  - consumer-technology
---

# "Put a Wet Phone in Rice to Fix Water Damage"

*EARC Assessment: **Contested consensus** — The claim is refuted by systematic testing, but remains widespread due to folk-physics plausibility, zero-cost accessibility, and survivor bias in personal anecdotes.*

---

## 1. The Claim

The claim is one of the most robustly transmitted pieces of technology folk knowledge in the smartphone era: when a phone gets wet — dropped in water, rained on, submerged, or splashed — the correct emergency response is to power it off immediately, place it in a sealed container of dry, uncooked white rice, and leave it for 24 to 72 hours. The rice, in this model, acts as a desiccant — absorbing moisture from the air around the device and thereby pulling residual water out of the phone's internals, allowing components to dry before power-on causes a short circuit.

The claim travels at remarkable speed. It has been standard advice in technology forums, social media threads, and word-of-mouth networks for at least fifteen years. It is the advice routinely offered in comment sections minutes after someone posts about a dropped phone. It appears in countless technology advice articles, YouTube repair tutorials, and help-desk responses. The sensory logic is clear: rice is visibly absorbent (cooking transforms it), it is available in almost every kitchen, and the instruction to seal it in a bag creates the image of a controlled desiccation environment.

Extensions of the claim include specifications about the type of rice (white rice is most commonly prescribed; some versions specify instant rice), the importance of adding silica gel packets if available, the necessity of removing the SIM card and battery cover before sealing, and the folklore that leaving it in the sun near a window accelerates drying. The basic rice protocol has become so entrenched that it functions as a cultural default — many people report following it without knowing why, simply because it was the first advice they received in a crisis moment.

The claim is not simply about rice as a material. It encodes a theory of damage: that smartphones fail after water contact because residual moisture triggers electrical short circuits, and that drying through desiccation is the primary corrective. This theory is partially correct about the failure mode but substantially mistaken about the remedy.

---

## 2. What's Actually True

Water damage in smartphones is genuinely dangerous, and the folk theory of why — liquid causes electrical shorts — is partially right. But the mechanism is more complex than simple moisture, and the rice remedy fails on multiple fronts.

**Why water damages electronics.** Pure distilled water is a poor electrical conductor; the conductivity that causes short circuits comes primarily from dissolved minerals and ions, which virtually all tap water, pool water, and even rainwater contain in varying concentrations. When water enters a phone and then evaporates, it leaves behind mineral deposits on circuit board traces — and these residues can cause ongoing corrosion and conductivity issues long after the phone appears dry. Research on marine electronics corrosion by Revie & Uhlig (2008, *Corrosion and Corrosion Control*) documents how ionic contamination accelerates oxidative corrosion on copper and gold traces. The damage from a water-immersion event is therefore not merely mechanical (liquid blocking contacts) but electrochemical (mineral deposits and oxide formation on conductive surfaces).

This electrochemical dimension is important for evaluating the rice remedy: even if rice were an effective desiccant at removing water vapor from enclosed spaces — which systematic testing shows it is not, at relevant scales — it cannot remove mineral deposits that have already been laid down on circuit traces. Drying the phone through any method does not reverse that contamination; only cleaning (typically through isopropyl alcohol wash or ultrasonic cleaning) does.

**Testing rice as a desiccant.** The first systematic, experimentally rigorous test of the rice remedy was conducted by Gazelle (2014), a consumer electronics refurbishment company that tested rice and four alternative methods — cat litter, oatmeal, instant couscous, and open air — for their ability to remove moisture from a water-saturated chamber over 24 hours. The results were unambiguous: uncooked white rice had virtually no performance advantage over leaving the phone in open air, and both performed substantially worse than purpose-made silica gel desiccant packets. Open air actually performed comparably to rice in most conditions, a finding replicated in multiple subsequent independent tests. Gazelle's testing methodology used moisture meter readings to quantify humidity reduction rather than phone survival, providing objective measurement rather than anecdotal outcome assessment.

Samsung's official guidance, updated in 2023 following complaints that the rice method was delaying proper repair-shop wet-device treatment, explicitly stated that they do not recommend the rice method and that the correct approach is to allow the device to air-dry in a well-ventilated area. Apple's same-year guidance on water damage specifically warns against rice, citing starch and small particles that can accumulate in ports.

**The actual mechanism of rice failure.** Dry rice absorbs moisture slowly through the endosperm's starch matrix. In a sealed bag or container, it can reduce ambient humidity over hours, but at a rate far below that of even moderate airflow over an open surface. An open air environment provides continuous vapor pressure differential driving evaporation; a sealed rice container creates a slowly equilibrating closed system. Unless the rice-to-air-volume ratio is very high and the rice is completely dry, the drying rate is comparable to or inferior to open-air exposure.

Additionally, dry rice produces starch dust and small particles that can enter phone ports, speaker meshes, and charge connectors. Samsung and Apple's cautionary language specifically addresses this. Gazelle's testing documented visible starch contamination in devices removed from rice after 24-hour exposure.

**What actually works.** Professional electronics restorers use a sequence that the rice method disrupts: (1) immediate power-off to eliminate the electrical current that accelerates electrochemical damage, (2) rapid disassembly to interrupt ongoing contact between water and components, (3) isopropyl alcohol (≥90%) cleaning of circuit boards to displace water and dissolve ionic residues, (4) ultrasonic cleaning for severe contamination, and (5) desiccation using purpose-made silica gel or electronic drying boxes with low-temperature forced airflow. The critical intervention is the ionic residue cleaning step — something no passive desiccation method addresses.

Beddow & Beddow's professional electronics repair guidance, widely adopted in certified repair networks, emphasizes that the probability of full recovery decreases significantly with each hour of delay before professional cleaning, not because of moisture per se but because of ongoing corrosion chemistry at contaminated surfaces. The rice method, insofar as it encourages owners to wait 24–72 hours at home before seeking professional repair, may actually worsen outcomes by extending the electrochemical damage window.

**IP ratings and modern waterproofing.** Modern smartphones — including iPhone models since the iPhone 7 (2016) and flagship Android devices — carry IP67 or IP68 ratings under the IEC 60529 standard, meaning they are rated to withstand fresh water submersion at 1–1.5 meters depth for 30 minutes. These ratings use silicon gaskets, membrane covers over ports, and hydrophobic coatings on circuit boards. IP-rated devices that fail after water contact typically do so because the gasket has degraded (common after previous repair or aging), because the submersion depth or duration exceeded rated parameters, or because salt water or chlorinated pool water was involved (the IP rating is for fresh water). For IP-rated devices, the rice remedy is additionally unnecessary: the appropriate response is to dry external ports before charging — Apple's own guidance — and seek repair only if functional issues emerge.

---

## 3. Why People Believe This

The rice remedy is an instructive study in how folk remedies achieve and maintain cultural saturation even when systematically contradicted by evidence, because it sits at the intersection of four reinforcing factors.

**Confirmation bias and survivor selection.** Many people who have used the rice method report that their phone subsequently worked. This observation is real but confounded. Smartphones are resistant enough to brief water exposure — especially modern IP-rated devices, and given that most drops are brief surface contacts or splashes rather than extended submersions — that a substantial fraction would have worked regardless of any remedy. The rice method gets credit for outcomes that would have obtained through open-air drying or even doing nothing. Failed rice-method attempts (the phone that went in the rice and never worked again) are under-reported in social networks: people whose phones are salvaged post happily, while people whose phones die tend to attribute failure to the severity of the water contact rather than the inadequacy of the remedy. Kahneman & Tversky's work on availability heuristics and narrative causation (1979, *Econometrica*) provides the general framework; Gilovich's (1991) application to sporting streaks and folk remedies illuminates the specific mechanism.

**Intuitive desiccation folk physics.** Rice visibly absorbs water during cooking — this is understood by everyone who has ever prepared the grain. The extrapolation from "rice absorbs water when cooked in it" to "rice will absorb water vapor from a sealed container" seems physically continuous, but it involves a significant shift: the cooking transformation involves large amounts of liquid water in direct physical contact with the grain over sustained heat, while the phone scenario involves vapor-phase water in air at ambient temperature. These are different physical processes with different rates and equilibria. The folk-physics model treats them as equivalent.

**Epistemic novelty — The Reverse Placebo Effect in Material Culture.** The rice-and-phone scenario demonstrates what might be called the *reverse placebo effect in material culture*: a ritual intervention that works primarily by preventing more harmful actions. In this framing, the rice remedy's true mechanism of action is not desiccation but behavioral displacement. Without the rice protocol, many users power on their wet phone immediately, hoping to see if it works — a behavior that dramatically increases the probability of short-circuit damage. The rice method's instruction to power off, disassemble, and wait creates a period of enforced rest that, independent of the rice, reduces the risk of user-inflicted immediate short circuit. The rice is doing nothing; the waiting is doing something. This insight reframes the folk remedy not as a harmful placebo but as a partially functional behavioral script that achieves one component of correct intervention (rest) while displacing a more effective intervention (professional cleaning). To understand the durability of the rice myth, this behavioral scaffolding function must be accounted for: the remedy "works" often enough in low-severity cases precisely because the behavioral component — enforced wait, no power-on — does genuine work, and this gets attributed to the rice.

**Accessibility and cost symmetry.** The rice remedy requires no tools, no specialized knowledge, and no expense. It is executable at 11pm with no stores open and no prior preparation. This accessibility creates a strong selection pressure for its transmission: it is the advice you can act on immediately, and in a moment of device-loss panic, actionability matters more than accuracy. Alternative interventions — silica gel packets, professional repair shops — have higher barriers to immediate deployment. The folk remedy occupies a temporal niche (the first hour after a drop) where its only competition is either the correct professional response (go to a repair shop) or harmful alternative responses (try to power on immediately). Compared to the latter, rice performs adequately because of its behavioral effect rather than its physical one.

---

## 4. Verdict

**Assessment: False — the rice method does not work through its claimed mechanism, performs no better than open air in controlled testing, and delays more effective interventions**

Snopes rates this as False, which is correct, though coverage up to the time of publication was more provisional than the evidence warranted — allowing some residual credibility to the claim as "perhaps not optimal but not harmful." The Gazelle testing data and the subsequent manufacturer advisories from both Apple and Samsung clarify that the harm case is real: starch contamination and repair delay are genuine risks, not hypothetical ones.

The more important verdict is etiological: this is a folk remedy that travels primarily by social urgency and selection bias, achieves apparent effectiveness by a mechanism entirely unrelated to its proposed action (rice as desiccant), and actively monopolizes the behavioral slot where a more effective intervention — immediate professional cleaning — belongs. Correcting the myth requires not just explaining why rice doesn't work as a desiccant but replacing the behavioral script with the correct one: power off, do not attempt to charge, and seek professional ultrasonic cleaning within hours rather than days.

**Evidence Grade: A (Systematic experimental testing, manufacturer guidance, and professional consensus)**
**Consensus Level: Strong professional consensus with manufacturer endorsement of correction**
**Practical Impact: Consumer electronics loss prevention, repair-shop counseling**

---

## 5. The Wider Picture

The rice-and-phone myth belongs to a category of technology folk knowledge that emerged rapidly after the mass adoption of smartphones and has proven remarkably resistant to correction despite systematic debunking — partly because the information ecosystem that generates and transmits folk remedies is faster, more decentralized, and more socially credible in crisis moments than the information ecosystem that transmits manufacturer guidance.

**The broader landscape of phone care myths.** Rice is not the only technologically inaccurate piece of smartphone care advice that circulates widely. The belief that charging a phone overnight damages the battery was valid for early nickel-cadmium battery technology but has been technically untrue since the widespread adoption of lithium-ion batteries with overcharge protection circuits (Blomgren, 2017, *Journal of the Electrochemical Society*). The belief that closing background apps improves battery life contradicts iOS and Android memory management architecture; the operating systems manage memory more efficiently when allowed to keep recent apps in RAM than when forced to reload from storage. The related belief that "letting the battery drain to zero then charging to 100% recalibrates it" mixes a real phenomenon from the nickel-cadmium era with a completely different lithium-ion chemistry. These myths share the rice property of being technically coherent within folk-physics models that do not correspond to current device architecture.

**Manufacturer liability and communication failures.** The persistence of the rice myth reflects a communication failure on the part of device manufacturers. The correct guidance — power off, seek professional cleaning, do not use rice — was not prominently communicated in Apple or Samsung warranty documentation or support channels for the bulk of the period during which the myth was entrenching itself. Warranty conditions that void coverage for water damage created a perverse incentive: users who disclosed water exposure risked losing warranty repair eligibility, while users who privately attempted home remedies and then presented phones with "unexplained" failure sometimes received warranty service. This created a market ecology in which the rice method had social advantages over transparency.

**iFixit and the right-to-repair dimension.** The rice myth intersects with the right-to-repair movement in an interesting way. Professional ultrasonic cleaning and board-level repair are not covered by manufacturer warranties and require either third-party repair shops or DIY skill and equipment. The cost of correct water damage remediation — $100–$300 at professional shops — creates a real access barrier that makes the free rice method attractive independent of its efficacy. iFixit's open repair guides have democratized some of this knowledge, but the material barrier (ultrasonic cleaners, isopropyl alcohol, microscopy tools for board inspection) remains meaningful. A complete debunking story should acknowledge that "seek professional cleaning" is better advice for a $1,200 flagship than for a three-year-old budget phone, and that the rice remedy fills a genuine gap in accessible, low-cost intervention that a complete remediation infrastructure has not fully addressed.

**Signal intelligence: the second-order myth.** A secondary myth has emerged in the wake of debunking coverage: that the real solution is silica gel desiccant packets (those small pouches that say "Do Not Eat"), sometimes supplemented with dry rice or cat litter. Silica gel does significantly outperform rice as a desiccant in the Gazelle testing, but it shares the fundamental limitation of the entire folk-remedy approach: it addresses water removal while leaving ionic contamination intact. The silica gel version of the myth may actually be marginally more harmful than the rice version because it instills more confidence in passive desiccation methods, further delaying professional intervention, while providing only marginally better drying. The myth has adapted to the debunking, incorporating the critique (rice is not the best desiccant) while preserving the core misconception (any desiccant approach is adequate repair).

---

## 6. How Fact-Checkers Handle It

Snopes has addressed the rice myth directly, rating it False and explaining that rice is not a significantly effective desiccant for enclosed devices. The coverage correctly identifies that rice provides no benefit over open-air drying in controlled testing and that manufacturer guidance recommends against it.

The fact-checking coverage is adequate but misses several dimensions that would strengthen its practical impact:

**1. The behavioral mechanism gap.** Explaining why rice superficially appears to work — not because of desiccation but because it enforces the correct behavioral default of not powering on — is essential for dislodging the belief. People who "tried rice and it worked" have evidence they consider personal and therefore strongly weighted. Simply stating that rice is ineffective does not address their evidence; explaining the actual mechanism of recovery (waiting, not rice) does.

**2. The replacement script.** Successful myth correction requires not just disconfirmation but a replacement script that the audience can deploy in the same situation. Snopes and most debunking coverage explain what doesn't work without providing a clear, actionable replacement protocol: power off immediately, do not charge or attempt to power on, remove the case and any covers, allow any external moisture to drain, and if the device has been submerged (not just splashed), take to a professional electronics cleaner within 12 hours. This protocol is deployable in the same panicked midnight scenario where rice provides comfort.

**3. The IP rating context.** Coverage should consistently note the change in landscape created by IP-rated devices after 2016. For most current flagship smartphones, a brief submersion in fresh water should not cause the catastrophic damage that justified aggressive desiccation protocols in earlier eras. The correct guidance has shifted: for IP-rated devices, the primary risk is charging while water is still in the charging port (which iOS and Android now detect and warn against), not residual internal moisture.

**4. The delay cost.** The opportunity cost of the 24–72 hour rice window is the period during which professional ultrasonic cleaning would be most effective. This time-sensitivity should be communicated prominently: the rice method is not just ineffective; it consumes the hours during which intervention has the highest probability of success.

Fact-checker coverage of technology myths benefits from collaboration with certified electronics repair professionals who can provide the replacement script and explain the professional standard of care. The rice myth is an excellent case because the correct answer is specific, testable, and actionable — and because the testing data (Gazelle, 2014; Samsung and Apple guidelines, 2023) is public and clear.
