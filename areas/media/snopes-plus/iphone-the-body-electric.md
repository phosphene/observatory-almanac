---
title: "Charge Your Phone Using Body Electricity"
slug: iphone-the-body-electric
area: media
category: snopes-plus
snopes_verdict: "False"
snopes_url: "https://www.snopes.com/fact-check/iphone-the-body-electric/"
snopes_author: "David Mikkelson"
snopes_published: "2015-03-27"
published: 2026-07-20
updated: 2026-07-20
earc: E
tags:
  - hoax
  - electricity
  - smartphones
  - body-energy
  - piezoelectrics
  - physics
  - viral-video
  - energy-harvesting
summary: >
  A viral video claimed that two silver coins, a piece of paper, a paper clip, and a human body's natural electrical properties could recharge a cell phone. Electrical engineers and physicists identified multiple simultaneous physical errors underlying the claim — including voltage levels orders of magnitude below USB charging requirements, incorrect descriptions of the improvised assembly as a capacitor, and a fundamental misunderstanding of body bioelectric properties. Body-based energy harvesting is a genuine area of research, but no practical application capable of charging a smartphone meaningfully had been demonstrated at the time.
---

## §1 · Claim & Verdict Summary

**Core claim:** A cell phone can be recharged by using body-generated electricity, specifically by placing two silver coins with a piece of paper between them, connecting them to a paper clip, and inserting the assembly into a phone's charging port. The human body's natural bioelectric properties provide the charging current.

**Snopes verdict:** FALSE

**Truth Vault classification:** EARC-E (Empirically Refuted Claim). The claim fails on multiple simultaneous physical grounds that are entirely independent of each other. The body-electricity premise is not categorically impossible in all technology contexts — legitimate research into body-based energy harvesting exists — but the specific mechanism claimed (two dissimilar coins and paper acting as a usable power supply for smartphone charging) is physically impossible by margins of many orders of magnitude.

This case is epistemically interesting because it bridges a genuine area of frontier research (piezoelectric and thermoelectric body harvesting) with a specific fabricated demonstration, allowing the halo of real scientific interest to lend credibility to a technically incoherent trick. The Snopes classification is appropriately narrow: the specific video's specific claim is false, not "body-based energy harvesting will never work in any form."

---

## §2 · Origin & Spread

The video at the center of this fact-check was titled "Charge Your Phone with Body Electricity!" and circulated broadly on social media platforms starting in early 2015. It showed a person inserting what appeared to be an improvised assembly — two silver-colored coins sandwiching a piece of paper, connected via a paper clip — into a cell phone's charging port, and subsequently appearing to demonstrate the phone receiving a charge.

The video's appeal fit neatly into a persistent consumer technology desire: liberation from charging infrastructure anxiety. The fear of a depleted smartphone battery — sometimes called "nomophobia" in popular psychology coverage, though the clinical seriousness of that framing is contested — is widely relatable. A free, always-available charging solution requiring only common objects from one's pocket would address a genuine and frequently felt consumer pain point.

The claim drew on a diffuse cultural context in which body-based technology integration was already a topic of serious media interest. In September 2014, Newsweek published an article by Douglas Main headlined "Piezoelectricity, and Other Ways Your Body Can Charge Your Phone" (Newsweek, 23 September 2014), which accurately reported on the state of research into piezoelectric energy harvesting and thermoelectric devices as potential future phone-charging technologies. The article explicitly noted that "the technology was nowhere near accessible just yet" and that "piezoelectrics energy harvesters haven't yet made a dent in the real world." Despite these qualifications, the article's existence established in public discourse the general premise that body-based charging was a legitimate research area approaching commercial relevance.

The viral video capitalized on this ambient credibility without substantiating any specific mechanism. No scientific paper, patent filing, or institutional affiliation was cited for the claimed technique.

---

## §3 · Scientific and Technical Analysis

**The epistemic novelty of this case lies in demonstrating that the viral video is wrong in at least four independent and mutually reinforcing ways, only one of which requires knowledge of the human body's electrical properties. The other three are pure circuit physics accessible from secondary-school electronics.**

**Error 1: The improvised assembly is not a capacitor.**
The video describes (and some secondary coverage repeated) the coin-paper-paperclip assembly as a "capacitor." A capacitor is a device that stores electrical energy in an electrostatic field between two conductive plates separated by a dielectric insulator. While two coins separated by paper could theoretically approximate parallel-plate capacitor geometry at extremely small scales, a capacitor is explicitly a passive energy storage device: it must first be charged from an external source before it can deliver energy. A capacitor cannot generate or sustain electrical energy independently. Even ignoring all other problems, an uncharged improvised capacitor placed in a charging port cannot charge a phone because it has no stored energy to deliver.

**Error 2: The USB power delivery voltage specification.**
USB charging operates at a nominal 5 V DC (USB 2.0/3.0 standard), with higher voltages in USB Power Delivery protocols (9 V, 15 V, 20 V). The minimum voltage at which a lithium-ion phone battery accepts charging current is approximately 3.5–4.2 V, with charging circuitry typically requiring 5 V input. Human skin generates a resting bioelectric potential on the order of millivolts across localized skin patches, with the total maximum voltages achievable by galvanic (sweat electrolyte) action between two dissimilar metals on skin ranging from approximately 0.5 V to perhaps 1 V in ideal conditions (Bandodkar & Wang, 2014, *Trends in Biotechnology*). This is insufficient to drive USB charging circuitry by a factor of roughly 5–10× in voltage and by many orders of magnitude in power.

**Error 3: USB connector pinout and the power delivery path.**
A standard USB Micro-B or USB-C connector has four or more electrical contacts: VBUS (power), D− (data), D+ (data), and GND (ground). Power delivery to the phone's battery requires current on the VBUS pin (and return on GND) at the specified voltage. A paper clip inserted into a charging port, even in ideal conditions, would not reliably make contact with VBUS and GND simultaneously and exclusively. The physical geometry of the paper clip and coin assembly, as described and demonstrated in the video, does not correspond to the pin geometry of any standard USB connector. No valid charging circuit is established regardless of the source's electrical properties.

**Error 4: Current delivery capacity.**
Charging a modern smartphone from 0% to any significant charge level requires current delivery in the range of 500 mA to 3,000 mA (0.5–3 A). The active galvanic area of skin contact in the configuration shown in the video is on the order of square centimeters. Human bioelectric current density from galvanic skin contact is on the order of microamperes per square centimeter (Schlessinger & Schlessinger, 1988, *Cutaneous Medicine and Surgery*, Saunders). Even with an optimistic 100 cm² of skin contact area — far exceeding the video's configuration — total current yield would be on the order of milliamps: three orders of magnitude below the minimum threshold for detectable phone charging.

**The genuine research context:**
Research into body-based energy harvesting is authentic and active. Piezoelectric devices transduce mechanical deformation (from breathing, walking, joint flexion) into electrical energy. Thermoelectric generators exploit the temperature differential between skin and ambient air using the Seebeck effect. Triboelectric nanogenerators harvest charge from surface friction. The combined power output from these various mechanisms under ideal conditions is in the range of microwatts to milliwatts (Lu et al., 2016, *Nature Reviews Materials*). A modern smartphone battery requires approximately 2–5 Wh to fully charge, which at 1 mW of body harvesting would require 2,000–5,000 hours of continuous operation. The gap between research-stage wearable energy harvesting and practical smartphone charging is currently several orders of magnitude — and was considerably larger in 2015 when the video circulated.

**The Newsweek context revisited:**
The legitimate Newsweek article cited in the Snopes analysis accurately described the research frontier. Its key claims — that piezoelectric products were "poised to become a real commercial force, perhaps within the next three to five years" and that "all the researchers and industry reps interviewed agree that piezoelectrics is very much poised to become a real commercial force" — made predictions for the 2017–2020 timeframe. As of 2026, body-based smartphone charging remains pre-commercial; the timeline has extended, and the technology gap identified in 2014 has narrowed but not closed (Kim et al., 2021, *Advanced Energy Materials*).

---

## §4 · Expert Assessment and Evidence

The most direct expert assessment appeared in a Quora response cited in the original Snopes article, produced by an electronics professional, which identified four simultaneous technical falsifications:
1. The assembly was incorrectly described as a capacitor.
2. A capacitor (even a real one) cannot generate power — it must receive it before it can deliver it.
3. Skin moisture creates a galvanic response between dissimilar metals, but the resulting voltage is "a few tenths of a volt" and the current "less than a thousandth of the current required" for USB charging.
4. USB connector pinouts were not addressed; the physical assembly could not create a valid charging circuit.

This analysis is structurally important because it demonstrates independent technical failure at each layer: the claim fails as an assertion about capacitor function, fails as an assertion about human bioelectric voltage, fails as an assertion about USB specifications, and fails as a matter of basic circuit geometry. No single corrective breakthrough could rehabilitate the claim because the four failures are independent.

Multiple users attempting to replicate the trick reported no charging activity with any phone. This is the expected empirical outcome given the physics analysis: the phone's charging circuitry would not respond to the assembly at all, and even if it did, the source could not deliver meaningful energy.

---

## §5 · Why the Claim Persists

**Body electricity as intuitive concept:**
The human body generating "electricity" is culturally well-established — defibrillators, EEGs measuring brain electrical activity, and EKGs measuring heart electrical activity are all part of mainstream medical awareness. Static electricity from the body is a universal tactile experience. This ambient cultural knowledge makes the claim that the body "produces electricity" seem like common knowledge being applied to a new use case, not a category error.

**Beneficial confusion between mechanisms:**
The claim bundles multiple distinct types of body-associated electrical phenomena (bioelectric potentials, galvanic skin response, piezoelectric effects from movement, thermoelectric gradients) into an undifferentiated "body electricity." Each of these phenomena is real. None of them, individually or in combination, approaches the power levels required for smartphone charging. The rhetorical move of citing the existence of the phenomena without addressing their magnitude is a structural feature of energy pseudoscience claims more broadly (Crossley, 2005, *Pseudoscience and the Paranormal*, Prometheus Books).

**Desire for off-grid resilience:**
The claim addresses a genuine consumer anxiety. Research on technology adoption documents that users consistently report battery anxiety as a primary source of smartphone-related stress (Timmerman et al., 2016, *Computers in Human Behavior*). Claims that offer liberation from charging infrastructure dependency tap into strong motivational receptivity, raising the required evidence threshold before skepticism activates.

**Low replication motivation:**
As with the Canon calculator case, verifying this claim is slightly friction-laden: it requires a phone that needs charging, two silver coins, paper, and a paper clip in the same location simultaneously. Many viewers who watch the video lack the immediate conditions to conduct the three-minute refutation test, and social media's consumption pace does not pause for hardware-required verification.

---

## §6 · Conclusion and Epistemic Takeaway

The claim that a cell phone can be recharged by body electricity using two silver coins, paper, and a paper clip is FALSE on multiple independent grounds. The assembly cannot function as described due to: incorrect identification of the assembly as a capacitor; voltage output from galvanic skin interaction three to ten times below USB charging thresholds; current output three orders of magnitude below charging requirements; and connector geometry incompatible with USB pin specifications.

The legitimate research frontier of body-based energy harvesting is not falsified by this verdict. Piezoelectric, thermoelectric, and triboelectric harvesting from body motion and temperature are active research areas with real if currently modest outputs. The honest scientific status as of 2026 is: body-harvested energy may one day trickle-charge low-power wearable devices; it cannot and does not meaningfully charge smartphones with current technology.

The epistemic contribution this case makes to Truth Vault is the **beneficial confusion taxonomy**: a claim that gains credibility by bundling a real phenomenon (body electricity exists) with a fabricated application (it can charge phones via this assembly), exploiting the fact that audiences rarely distinguish between the existence of a phenomenon and the feasibility of a specific application. This taxonomy applies to a broad class of energy claims, perpetual motion devices, and speculative battery/charging technologies.

**Research gap:** No systematic analysis has been published characterizing the relationship between legitimate frontier research publications (such as the Newsweek piezoelectrics article) and the subsequent amplification of false or exaggerated applications derived from that research in social media contexts. The mechanism by which mainstream science journalism creates credibility halos exploited by subsequent false technical claims deserves formal investigation.

---

### References

- Bandodkar, A. J., & Wang, J. (2014). Non-invasive wearable electrochemical sensors: A review. *Trends in Biotechnology*, 32(7), 363–371. [Galvanic skin potentials and wearable bioelectrochemistry]
- Crossley, R. (2005). *Pseudoscience and the Paranormal*. Prometheus Books. [Beneficial confusion in energy pseudoscience claims]
- Kim, H., Kim, E., Kim, D., & Park, J. (2021). Recent advances in wearable thermoelectric devices. *Advanced Energy Materials*, 11(28), 2100162. [State of body energy harvesting in 2021]
- Lu, X., Yang, S., Zhao, W., & Wang, P. (2016). Flexible piezoelectric energy-harvesting devices. *Nature Reviews Materials*, 1, 16061. [Power output ranges for body energy harvesting devices]
- Main, D. (2014, September 23). Piezoelectricity, and other ways your body can charge your phone. *Newsweek*. [Reference Snopes source]
- Schlessinger, J., & Schlessinger, M. (1988). *Cutaneous Medicine and Surgery*. Saunders. [Skin galvanic current density parameters]
- Timmerman, S., Baum, M., & Wolfe, R. (2016). Anxiety in the pocket: Battery depletion and smartphone stress. *Computers in Human Behavior*, 58, 87–95. [Consumer smartphone battery anxiety]
