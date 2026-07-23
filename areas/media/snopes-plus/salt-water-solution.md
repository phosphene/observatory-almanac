---
title: "Salt Water and Vending Machines"
slug: salt-water-solution
snopes_url: https://www.snopes.com/fact-check/salt-water-solution/
snopes_verdict: outdated
snopes_author: Barbara Mikkelson
published: 2026-07-23
updated: 2026-07-23
original_snopes_date: 2001-07-16
categories:
  - urban-legends
  - technology
  - theft
  - consumer-electronics
tags:
  - vending-machines
  - salt-water
  - electrical-short-circuit
  - salting
  - macgyver
  - vandalism
  - free-soda
  - theft-technique
earc_gap: E
epistemic_class: historical-technical-claim
---

## §1 Claim and Verdict Summary

A widely circulated piece of consumer advice—or, depending on framing, a theft tip—claimed that pouring salt water into the coin slot of a vending machine would cause the machine to dispense free product and money. The salt water, being electrically conductive, would allegedly short-circuit two internal switches that controlled product dispensing and change return, causing the machine to "jackpot" spontaneously and deliver sodas and coins without legitimate payment.

Snopes investigator Barbara Mikkelson rated this claim **Outdated**. The technique did work on a specific generation of vending machines manufactured and deployed primarily from the early 1980s through the mid-1990s, and was sufficiently prominent to attract criminal prosecutions and significant industry countermeasures. However, vending machine manufacturers responded by redesigning machines to eliminate the vulnerability—relocating coin slots, perforating coin channels to drain liquids, and adding bill validators that blocked access—so that by the late 1990s and certainly by the time of the Snopes article in 2001, the technique was essentially nonfunctional on contemporary equipment while remaining a prosecutable form of vandalism. The claim is historically true but technically obsolete.

This entry examines the electromechanical vulnerability that made "salting" functional, the social and cultural context in which the technique spread, the documented prosecutions it generated, a 2007 case where an out-of-date practitioner damaged modern machines without getting free product, the electrocution risk inherent in tampering with electrically powered equipment, and the broader significance of machine-exploitation folklore in popular culture.

---

## §2 The Technical Claim and Its Historical Evidence

The technical claim rests on genuine electromechanical properties of older vending machine designs. Vending machines of the relevant generation used coin-controlled circuits in which the coin channel—a path from the coin slot to the coin box—ran through or near the machine's electrical control board. Coins deposited along this path would complete or interrupt circuits, triggering product dispensing and coin return.

The mechanism of action for salting was as follows: salt water, being an ionic solution (sodium chloride dissolved in water produces Na⁺ and Cl⁻ ions that allow electrical current to flow), acted as a conductor across gaps in the control circuit that would normally require a physical coin to bridge. Industry publications documented this vulnerability explicitly. Industry analyst McDonald (1991, "Vendor Vandalism Sparks a Salt Water Solution," *Beverage World*, 1 February 1991, p. 57) described saline solution as acting as a "conductor" causing units to "jackpot both money and product." This published account is itself significant: the trade publication was discussing the problem in 1991 as an ongoing operational concern requiring a technical solution, confirming that the technique was both known and effective at that time.

The circulating instruction text recovered by Mikkelson (2001) specified the preparation method in detail: fill a two-liter bottle with lukewarm water, dissolve approximately half a cup of salt, create a funnel from a rolled newspaper, and slowly pour the saline solution into the coin slot of a vending machine in a "fairly deserted" location at night. The preference for night and isolated locations is consistent with the legal risk: the practice was understood by its practitioners to be illegal. The instruction to go slowly mirrors the food-chemistry rationale discussed in other contexts—slow introduction allows the liquid to flow into the coin box rather than simply draining from the channel.

The June 1994 Macomb County, Michigan prosecution is one of the earliest documented legal consequences. Three individuals arrested after a salting spree were found in possession of 154 cans of soda, representing an evening's worth of machine exploitation (Schabath, Gene, 1994, "Thieves Wade Into State Pop Machines," *The Detroit News*, 15 June 1994, p. A1). The estimate of $600 in loss and damage per salting incident—cited in the original instruction text recovered by Mikkelson—encompassed product theft, damage to the selection panel and coin mechanisms, sales downtime during repair, and repair costs. For widespread teen adoption of the technique across a city, the aggregate economic harm would have been substantial.

The alleged MacGyver connection—a suggestion on the television series (1985–1994) that inspired teens in the mid-1990s—is mentioned by Mikkelson (2001) but flagged as uncertain. MacGyver was the paradigmatic popular-culture vehicle for improvised technical problem-solving, and numerous real-world hacks of the 1990s claimed inspiration from the show. Whether the salting technique actually appeared on MacGyver in any explicit or implied form, or whether the show's general ethos of improvised engineering simply created a cultural context receptive to such ideas, cannot be verified from the available record.

---

## §3 Epistemic Novelty: The Electromechanics of Coin-Switch Vulnerabilities and the Industry Response

The epistemic novelty in this case concerns the specific electromechanical architecture that created the salting vulnerability and the precise engineering countermeasures that eliminated it—a case study in the iterative arms race between exploitation and technical hardening that characterizes many consumer technology security stories.

Older vending machine coin mechanisms employed a design in which the coin channel was a metallic trough oriented such that coins fell through it toward a coin box. The control circuits—triggering dispensing and change return—were located in close physical proximity to this channel and in some designs shared parts of it as a common ground path. When liquid entered the coin slot and traveled down the metallic coin trough, it could reach the electrical contacts for these switches without requiring a coin to physically depress them. The saline solution's electrical conductivity (measured in siemens per meter, where 0.9% saline has a conductivity of approximately 1.5 S/m compared to distilled water's approximately 5×10⁻⁶ S/m—a factor of roughly 300,000 times more conductive) meant that even relatively small quantities of salt water could establish effective electrical bridges across switch gaps (Robinson, R. A., & Stokes, R. H., 1959, *Electrolyte Solutions*, 2nd ed., Butterworths Scientific Publications, London).

The industry countermeasures documented by Mikkelson (2001), citing Holleran (1996, "Vending Dynamics," *Beverage Industry*, 1 May 1996, p. 40), were elegant in their engineering simplicity. Moving the coin slot to a different part of the machine altered the geometry so that liquid entering the slot could not flow toward the coin control electronics. Perforating the coin channel allowed liquids to drain before reaching the electronics while still allowing coins—which are solid and too large to pass through the perforations—to travel their usual path. Mounting the bill validator (for paper currency) above the coin channel provided a physical barrier that blocked access to the coin channel from the bill slot direction. Older machines were retrofitted with diverters—essentially small splash guards redirecting any liquid away from vulnerable electrical contacts while allowing coins to proceed normally.

These solutions represent a form of security-by-design that the computer security community would later formalize as "defense in depth": multiple independent mitigations such that defeating one does not compromise the overall security posture. A liquid entering the coin slot of a post-retrofit or newly designed machine would encounter at minimum a perforated channel (draining the liquid), a relocated control circuit (separating moisture from electronics), and possibly a bill validator barrier (blocking the original access path). Any one of these would suffice; all three in combination made the attack surface effectively zero.

The transition was not instantaneous. Older machines remained in operation through the mid-to-late 1990s as fleet turnover in the vending industry is slow—machines represent capital investments that operators depreciate over years. This created a mixed deployment environment in which some machines were vulnerable and some were not, meaning that young people who had learned the technique from peers or popular culture might attempt it on some machines successfully and others unsuccessfully, producing inconsistent results that contributed to confusion about the technique's current viability.

---

## §4 Legal Context and the 2007 Anachronism Case

The legal consequences available under U.S. law for salting vending machines were substantial, generally triggering charges for theft, vandalism, and potentially criminal mischief depending on jurisdiction and the assessed dollar value of property damage. The $600 per-incident damage estimate meant that in many jurisdictions, even a single salting event could meet the threshold for felony rather than misdemeanor charges.

The most epistemically interesting legal document in Mikkelson's account is the 2007 Memphis case, reported in the *Memphis Democrat* (2007, "Vandals Hit Vending Machines with Out-Dated Scheme," 3 May 2007). A would-be thief poured saline solution into the coin mechanisms of a car wash and a soda vending machine in Memphis—and damaged both machines without getting any free product. Officer Terry Simerl's report confirmed that the vandal was facing felony charges for the amount of damage done, entirely without benefit to themselves. The Memphis Democrat's report explicitly cited Snopes.com as "an authority on such urban legends" in explaining why the technique failed, an unusual instance of a police report invoking an internet fact-checking resource.

This case is a near-perfect illustration of the half-life problem in folk knowledge. The salting technique was genuine current intelligence about real machine vulnerabilities in 1991 and 1994. By 2001, Mikkelson rated it outdated. By 2007, someone acting on the same folk knowledge that had been valid technology a decade and a half earlier found themselves committing a crime that harmed others and gained them nothing. The folk knowledge had been accurate; its expiry date had not been communicated alongside the knowledge itself. This is a general feature of technical folk knowledge transmission: the social channels that spread "how to do X" rarely carry metadata about the validity conditions or temporal constraints on the information.

The electrocution risk mentioned by Mikkelson (2001), citing the death of ten-year-old Shawn Ramanauskas on 21 August 1995, is worth examining on its own terms. Shawn was electrocuted by a candy machine in Alabama; the Poovey (1999, "Alabama Supreme Court Reduces Award in Vending Machine Case," *The Associated Press*, 5 March 1999) report established that the machine was improperly connected to an ungrounded, wrongly polarized electrical outlet rigged by a handyman, and that guests had reported shocks from the machine cluster two days before the fatality. Mikkelson correctly notes that there is no reason to suppose Shawn was engaged in salting, but uses the case to illustrate a real risk: a person deliberately introducing water into a machine's coin mechanism while the machine is powered creates conditions very similar to an ungrounded fault, and an improperly grounded machine under those conditions could deliver a life-threatening shock.

---

## §5 The MacGyver Effect and the Spread of Technical Folk Knowledge

The cultural role of popular media in transmitting technical folk knowledge has received scholarly attention, though the specific MacGyver claim regarding salting remains unconfirmed. The broader phenomenon—television programs, films, and later the internet serving as vehicles for the transmission of criminal techniques—has been documented across multiple domains. The MacGyver series ran from 1985 to 1994 on ABC and was explicitly built around the premise that everyday materials and improvised engineering could solve extraordinary problems; its eponymous character became a cultural archetype to the point where "macgyver-ing" entered informal English as a verb meaning to improvise a technical solution.

Research on script-based crime knowledge—the idea that crime scripts (sequences of steps required to execute a criminal act) can be transmitted through media representation—has found that media portrayals can both teach techniques and create cognitive permission structures for their use (Cornish, Derek B., 1994, "The Procedural Analysis of Offending and Its Relevance for Situational Prevention," in Clarke, Ronald V., ed., *Crime Prevention Studies*, Vol. 3, Criminal Justice Press). The salting technique, if it did appear on or near MacGyver in any form, would represent a relatively straightforward transfer from television fictional scenario to real-world criminal exploitation of genuine machine vulnerability.

The instruction text itself—specifying two-liter bottles, half a cup of salt, rolled newspaper funnels, deserted locations, nighttime operation—represents what criminologists call an "enabling script": information detailed enough to allow a novice to execute the technique without prior technical knowledge. The level of specificity suggests that whoever first formalized the instructions had either direct experience or reliable second-hand knowledge of actual operational parameters, rather than having invented a plausible-sounding but fictional technique. This is consistent with the technique's documented effectiveness in the historical record.

---

## §6 Broader Significance: Machine Exploitation, Folk Knowledge Half-Life, and the Outdated Rating

The "Outdated" rating that Snopes applied to this claim represents an underused but analytically important epistemic category. Most fact-check verdicts are binary (true/false) or three-way (true/false/mixed), treating claims as having time-invariant truth values. The Outdated rating acknowledges that some claims were accurate at one point and cease to be accurate as the world changes—not because anyone was wrong or misled, but because the underlying technical or social conditions changed. This is particularly important for claims about system vulnerabilities, where the adversarial response to exploitation predictably hardens the target.

The EARC gap designation of **E** (Empirical) reflects the need for a more complete historical record of the specific machine generations affected, the precise engineering specifications of the circuit access in vulnerable coin mechanisms, and the full extent of documented criminal prosecutions for salting across U.S. jurisdictions in the early-to-mid 1990s. The existing record is largely anecdotal (news reports, industry publications) rather than systematic. A proper engineering-historical account of vending machine security evolution—similar to what has been done for ATM skimming, another electromechanical vulnerability with a well-documented arms-race history—would constitute a meaningful scholarly contribution to the intersection of technology history and crime prevention studies.

The salt-water vending machine story also serves as a useful pedagogical case for discussions of technology-specific folk knowledge, the social transmission of criminal techniques, and the design philosophy of security hardening. It demonstrates that the same design feature (a coin coin channel adjacent to control electronics) that was invisible as a vulnerability during normal operation became a liability once the attack surface was socially identified and shared. The industry's relatively rapid response—documented by 1991, with new designs deployed by the mid-to-late 1990s—reflects a responsive security posture that successfully neutralized the vulnerability within a reasonable deployment cycle, at the cost of significant interim losses.

---

*Sources: Mikkelson, Barbara (2001/2014), Snopes.com; McDonald, B. (1991), Beverage World; Holleran, Joan (1996), Beverage Industry; Schabath, Gene (1994), The Detroit News; Memphis Democrat (2007); Poovey, Bill (1999), The Associated Press; Robinson, R. A., & Stokes, R. H. (1959), Electrolyte Solutions, Butterworths; Cornish, Derek B. (1994), Crime Prevention Studies, Vol. 3.*
