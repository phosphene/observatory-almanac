---
title: "Do TSA Full-Body Scans Show ... Everything?"
slug: "tsa-full-body-scans-private-parts"
snopes_url: "https://www.snopes.com/fact-check/tsa-full-body-scans-private-parts/"
snopes_verdict: "Outdated"
snopes_author: "Madison Dapcevich"
snopes_published: "2024-02-01"
published: "2026-07-20"
updated: "2026-07-20"
epistemic_status: "verified — TSA primary documentation, EPA, Congressional record, archival journalism"
earc: "R"
gap: "surveillance-privacy-technology-policy"
tags:
  - tsa
  - airport-security
  - backscatter-x-ray
  - body-scanning-privacy
  - millimeter-wave
  - advanced-imaging-technology
  - atd-software
  - civil-liberties
---

## §1 Claim & Verdict Summary

This entry covers a closely related but distinct Snopes fact-check by Madison Dapcevich (published 1 February 2024) on the same recurring TSA scanner privacy claim. The viral prompt in this version originated in an X post dated January 18, 2024, by user @Ragland1836, claiming the TSA "can see your c\*ck and b\*lls whenever you walk through the X-ray scanner." The claim accumulated hundreds of thousands of views before the original post was hidden; Snopes archived a version. Snopes rated this claim **Outdated**.

As with the companion article (`did-tsa-full-body-scans-once-show--everything.md`), the verdict reflects the following factual structure:

1. TSA deployed backscatter X-ray **Advanced Imaging Technology (AIT)** units at U.S. airports beginning in 2010. These devices produced body-surface images with sufficient anatomical resolution that agency documentation described them as resembling "a chalk etching." The authentic image circulated in the viral post was traced via reverse-image search (Yandex) to TSA's own 2010 documentation.

2. By 2013, all backscatter units had been removed from U.S. airports, replaced entirely by millimeter-wave AIT units that generate only a generic stick-figure avatar display — not an anatomically detailed image of the specific passenger.

3. Therefore, the present-tense claim that TSA *currently* can see anatomical details is inaccurate. The historical-tense claim that TSA *once* had that capability is accurate.

This entry shares the same core factual foundation with the companion article but was published 11 days earlier (1 February vs. 12 February 2024) and develops slightly different contextual emphases — differences this Truth Vault entry examines to add distinct analytical value.

---

## §2 Evidence Inventory

**2.1 The viral post and image authentication**

The source tweet was posted January 18, 2024 by @Ragland1836. The image attached to the tweet depicted the tanner-style chalk-etching outputs of a backscatter AIT unit — showing a male and female scan side-by-side with clear anatomical surface detail. Snopes conducted a reverse-image search using Yandex and confirmed that the earliest traceable web appearance of this image was in 2010 on TSA's official website, where it appeared as an illustration in an official "How It Works" explainer for the backscatter program.

The image was thus authentic in the strongest possible sense: it was produced by TSA, depicting real TSA technology, published by TSA. Its deployment in a 2024 tweet as evidence for a present-tense claim exploited the authenticity of the historical image to imply currency.

**2.2 Backscatter X-ray mechanics**

Backscatter X-ray AIT functions differently from transmission X-ray (the type used to scan luggage). In transmission X-ray, the radiation passes through the object of interest; in backscatter, very low-energy X-rays are projected at the body surface and detectors capture the fraction of radiation that backscatters (reflects back) toward the emitter. Because this reflected radiation encodes the surface profile of the body — including body contours under clothing — at relatively high spatial resolution, the resulting image is a surface map of the body, to which clothing is frequently semi-transparent or transparent depending on material composition and thickness.

The EPA confirmed that the dose from a single backscatter scan was approximately equivalent to the cosmic ray exposure during two minutes at altitude — extremely low by clinical diagnostic standards (EPA, 2017). However, questions were raised about cumulative exposure for frequent flyers and airport workers, and a letter signed by multiple UCSF radiation biologists in 2010 raised concerns about the concentration of dose in skin tissue; the concerns were subsequently reviewed and assessed as negligible by the FDA and Johns Hopkins Applied Physics Laboratory (FDA/JHPL review, 2010, cited in TSA briefing materials).

**2.3 The "chalk etching" description and official documentation**

TSA's official description of backscatter output as a "chalk etching" was a carefully chosen characterization that acknowledged the body-surface nature of the image while minimizing the phrase's evocativeness. Critics and civil liberties organizations pointed out that the description simultaneously confirmed and minimized the privacy implication: a chalk etching of the human body that includes clothing-penetrating surface detail is precisely what would concern privacy advocates, regardless of the artistic metaphor used to describe it.

Internal TSA guidelines did require that the reviewing officer be stationed in a separate room from the checkpoint, unable to see the passenger directly, to prevent the possibility of matching a detailed scan image to a visible face. Images were to be deleted immediately after review. However, a congressional investigation and reporting by ProPublica (Grabell, 2010) revealed that at least one TSA vendor (not Rapiscan) had retained scan images in violation of published policy during a government vulnerability assessment, demonstrating the gap between stated policy and actual practice.

**2.4 Millimeter-wave AIT and the avatar display**

The currently deployed millimeter-wave AIT units (manufactured primarily by Leidos, the successor to L-3's security products division) produce a three-dimensional body-surface model internally but display only a generic anatomical-neutral avatar to the TSA officer. The avatar has a schematic figure without individualized features; anomalies detected by the automated threat recognition software are displayed as yellow boxes on the corresponding body region of the avatar, indicating where a manual secondary screening should focus.

This architecture implements privacy protection at the algorithmic and interface level rather than at the detection level. The underlying sensor data does encode body-surface geometry, but the system is designed such that this data does not produce a viewer-accessible anatomically detailed image. Whether the raw sensor data is retained in any form, or could be accessed through system diagnostics or maintenance interfaces, has been a subject of ongoing privacy research and advocacy concern.

**2.5 The chronology of removal**

- **2010**: Mass deployment of backscatter AIT units at U.S. airports begins.
- **January 2011**: House Representative Jason Chaffetz introduces the "Secure Travel and Counterterrorism Preparedness Act," proposing to ban AIT units without generic avatar software.
- **2012 FAA Modernization and Reform Act**: Requires TSA to implement generic "Automated Target Recognition" software on all AIT units by a specified deadline.
- **October 2012**: TSA begins removing backscatter units; Rapiscan Systems fails to develop compliant ATR software.
- **June 2013**: All ~250 backscatter units removed from U.S. airports. Millimeter-wave units with ATR software remain in service.

---

## §3 Epistemic Novelty

**3.1 Two articles, one viral trigger: the recycling of viral content**

An epistemically interesting dimension of these two Snopes fact-checks (this one from February 1, and the companion from February 12) is that they address the same viral claim, from the same post, eleven days apart. This reflects a practical challenge in internet fact-checking: claims that go viral can generate multiple waves of inquiry from different entry points, requiring the same fact-checking organization to produce distinct response pieces that cover overlapping ground for different audience segments arriving at different times through different pathways.

The two articles are substantively nearly identical in their fact content. Their existence as separate pieces — rather than a single definitive article — represents the tension between the economics of social media engagement (distinct URL, distinct publication date, captured as distinct search result) and epistemic efficiency (one comprehensive treatment). This structural feature of fact-checking as an industry has implications for how fact-check archives function as knowledge repositories: the same claim may have multiple valid fact-check records with different dates, and a researcher using fact-check archives must decide how to handle duplicates without treating the duplication as evidence of inconsistency.

**3.2 Authenticity as a weapon: the forensic reversal**

The viral post exploited the authenticity of the TSA image as its primary persuasive mechanism. Unlike cases where misinformation involves fabricated or manipulated images, this case involved a *real* image being deployed in a misleading temporal context. This creates an unusual epistemological structure: the image passed any forensic authenticity test (ELA would show no anomalies; reverse-image search confirmed its age and provenance) and yet the overall claim was misleading because of the mismatch between the image's referent (2010 technology) and the claim's timeframe (2024 present tense).

This "authentic document, false context" structure is distinct from deepfakes and image manipulation. It is closer to what Wardle and Derakhshan (2017, *Council of Europe report*) call "false context" — real content deployed in a fabricated informational frame. Their taxonomy of misinformation distinguishes: (a) fabricated content (completely false), (b) manipulated content (altered genuine material), and (c) misleading context (genuine material paired with false framing). TSA scanner posts of this type are category (c), and they are epistemically harder to correct than (a) or (b) because there is no forensic tool for detecting contextual misrepresentation — only temporal reasoning and primary-source research can reveal the mismatch.

**3.3 The privacy policy lifecycle and epistemic lag**

The TSA scanner case illustrates a structural "epistemic lag" problem in public knowledge of technology policy: policy changes occur (technology removed, regulations adopted), but these changes are rarely amplified with the same virality as the original controversy. The controversy over backscatter scanners in 2010–2012 generated enormous media coverage. The resolution — removal of the units, deployment of avatar-based alternatives — received substantially less coverage, and almost no coverage designed to reach the same audiences who saw the original controversy reporting.

This asymmetry means that public belief states are likely to lag behind policy reality by years or decades for any technology controversy that is resolved through administrative action rather than continued public drama. A person who saw news coverage of the "TSA digital strip search" controversy in 2010–2012 and never saw the 2013 removal coverage would rationally believe that the technology remains deployed. This is not irrationality; it is the predictable consequence of asymmetric coverage intensities across the controversy and resolution phases of a policy cycle.

---

## §4 Contextual Analysis

**4.1 The role of Congressional oversight in technology accountability**

The backscatter removal was not driven by TSA administrative discretion but by statutory mandate. The 2012 Congressional requirement that all AIT must display only generic avatars represented a specific legislative intervention into administrative technology procurement and use — unusual in its specificity about technical requirements (software functionality, not just performance standards or privacy impact assessments).

This legislative specificity was itself a consequence of the sustained advocacy campaign by EPIC and allied organizations, which kept the issue in front of Congress through hearings, litigation, and public campaigns for several consecutive years. The outcome illustrates a model of technology accountability in which civil society litigation and advocacy creates sufficient political pressure that legislative intervention becomes an attractive exit for lawmakers who wish to be seen as protecting privacy without directly blocking a national security program.

**4.2 Comparative international policy responses**

Several European Union member states deployed millimeter-wave AIT units in airports beginning around 2008–2010, in parallel with the US deployment but under different regulatory frameworks. The UK began trials at Manchester and Heathrow airports in 2008, initially allowing operators to view anatomically detailed scans. Following complaints, the UK's Information Commissioner's Office issued guidance requiring that anatomically detailed imagery be replaced with generic avatars, and the UK's trial program transitioned to avatar-only display by 2011.

Germany's Bundespolizei conducted a trial of millimeter-wave technology at Hamburg Airport from 2010 to 2011. The trial produced a false-alarm rate considered operationally unacceptable (up to 54% of passengers required secondary screening based on scanner alerts in some phases of the trial, according to the 2011 evaluation). Germany suspended the program and did not proceed to wide deployment, representing one of the more data-driven national decisions about AIT technology during this period.

**4.3 Health concerns: the UCSF radiobiologist letter**

In April 2010, a group of UCSF faculty members — including professors of biochemistry and biophysics — wrote to the President's science advisor raising concerns about the backscatter technology. Their letter pointed out that while the total body dose was indeed very low, the TSA and FDA safety assessments had used whole-body averaging; the UCSF scientists argued that because backscatter X-rays are absorbed primarily in the skin, a more relevant dose metric would be skin dose, which could be considerably higher on a per-volume-of-tissue basis than the whole-body average.

The FDA and the National Council on Radiation Protection and Measurements subsequently reviewed the concern and concluded that even using skin dose metrics, the radiation risk from backscatter scanning was negligible. The UCSF letter nonetheless illustrates an important epistemic dimension of the controversy: the domain-specific expertise required to evaluate radiation safety claims was sufficiently specialized that the initial public discussion produced conflicting credible-seeming expert statements, creating uncertainty that contributed to public opposition even though the scientific consensus ultimately supported the safety of the technology.

**4.4 TSA's public communication failures**

Multiple reviews of TSA's communication strategy around AIT deployment noted significant deficiencies. The agency rolled out the technology with limited advance public communication, provided technical descriptions that were simultaneously accurate and evasive, and responded to privacy concerns defensively rather than with substantive engagement. A Government Accountability Office (GAO) report from 2013 (GAO-13-623) recommended improvements to TSA's AIT program management and passenger communication, finding that TSA had not conducted adequately rigorous evaluation of the technology's effectiveness relative to alternative screening methods, and that it had not clearly communicated to passengers what the technology detected and displayed.

This communication failure contributed directly to the epistemic confusion that now sustains the "TSA can see everything" claim: if TSA had proactively and clearly communicated both the nature of the backscatter images (yes, anatomically detailed) and the subsequent transition to avatar-only systems (no longer anatomically detailed), the claim would have less purchase precisely because the institutional record would be clearer.

---

## §5 Broader Implications

**5.1 Technology lifecycles and the persistence of outdated claims**

The TSA backscatter case is an instance of a general phenomenon: security and surveillance technologies are deployed with significant controversy, subsequently modified or retired in response to that controversy, and then continue to generate viral misinformation based on the earlier state of the technology rather than its current state. Given the internet's permanent accessibility of historical documentation, this pattern will persist for any technology that:
(a) was controversial at deployment
(b) generated significant media and advocacy documentation
(c) was subsequently modified or retired through administrative action rather than public spectacle

Maintaining accurate public mental models of surveillance technology capabilities requires ongoing "correction infrastructure" — not just one-time fact-check articles but living documents, prominently discoverable, that explicitly address the historical controversy and the current state simultaneously.

**5.2 Physical infrastructure vs. policy: the asymmetric reversal problem**

Surveillance technology deployment creates lasting physical, institutional, and documentary infrastructure. When a technology is retired, the physical infrastructure is dismantled, but the documentary infrastructure — archived images, congressional testimony, advocacy reports, news articles — remains permanently accessible online. The asymmetry is structural: deployment creates artifacts that persist; removal does not create equivalent counter-artifacts. This asymmetry systematically favors the resurfacing of outdated "surveillance capability" claims over the resurfacing of "capability removed" corrections.

A potential remedy would be for federal agencies to publish prominent, search-optimized documentation of technology retirements with explicit statements of what is no longer deployed and why, providing corrective documentary infrastructure comparable in its search-engine accessibility to the original deployment documentation. TSA's timeline page does record the removal of backscatter units, but it is not structured for the kind of search optimization that would make it a prominent result for "do TSA scanners see everything" queries.

**5.3 The civic epistemology of security technology**

The recurring virality of TSA scanner claims reflects a broader civic epistemological challenge: most citizens have no independent means of verifying what technology is deployed in public spaces they are required to use. Unlike consumer products, where purchasing decisions provide some feedback about product existence, airport security screening is mandatory, non-transparent, and defined by classified threat assessment criteria. The information environment around TSA technology is therefore structurally asymmetric: TSA knows what it deploys; passengers know only what TSA chooses to disclose and what advocacy organizations manage to expose through FOIA requests and litigation.

This structural asymmetry creates a standing credibility advantage for claims asserting surveillance capabilities even when those claims are outdated or inaccurate, because the audience cannot directly verify the contrary. Trust in institutional disclosure — or its absence — becomes the primary epistemic resource available to the ordinary traveler.

**5.4 Privacy as a permanent policy dialogue**

Even if current TSA technology does not show anatomical detail at the viewer-facing interface, the underlying policy questions about bodily privacy in mandatory screening contexts remain live. Questions about what raw sensor data is retained, how it is secured, whether it can be subpoenaed, what happens to data for passengers who opt out versus those who do not, and how the algorithm defines "anomalies" worthy of secondary screening (with potential disparate impacts on body types medical conditions, or prosthetics) are all ongoing matters of legitimate public concern. The "Outdated" verdict on the specific "sees everything" claim does not resolve these broader questions but clarifies which specific claim is no longer accurate as a description of current technology.

---

## §6 References

- Dapcevich, Madison. "Do TSA Full-Body Scans Show ... Everything?" *Snopes*, 1 Feb. 2024. https://www.snopes.com/fact-check/tsa-full-body-scans-private-parts/
- Electronic Privacy Information Center (EPIC). "Whole Body Imaging Technology and Body Scanners." https://archive.epic.org/privacy/airtravel/backscatter/
- Grabell, Michael. "TSA Removes X-Ray Body Scanners From Major Airports." *ProPublica*, 19 Oct. 2012. https://www.propublica.org/article/tsa-removes-x-ray-body-scanners-from-major-airports
- Duffy, Lizzy. "'Invasive' Body Scanners Will Be Removed From Airports." *NPR*, 18 Jan. 2013. https://www.npr.org/sections/thetwo-way/2013/01/18/169733300/invasive-body-scanners-will-be-removed-from-airports
- Government Accountability Office. *Aviation Security: TSA Should Limit Future Acquisitions of Advanced Imaging Technology.* GAO-13-623, 2013. https://www.gao.gov/products/gao-13-623
- Transportation Security Administration. "Transportation Security Timeline." https://www.tsa.gov/timeline
- TSA. Backscatter AIT "How It Works." Archived 2010. https://web.archive.org/web/20100719104853/https://www.tsa.gov/approach/tech/ait/how_it_works.shtm
- US Environmental Protection Agency. "Radiation and Airport Security Scanning." 15 Aug. 2017. https://www.epa.gov/radtown/radiation-and-airport-security-scanning
- Wardle, Claire, and Hossein Derakhshan. *Information Disorder: Toward an Interdisciplinary Framework for Research and Policymaking.* Council of Europe, 2017. https://rm.coe.int/information-disorder-toward-an-interdisciplinary-framework-for-researc/168076277c
- Slovic, Paul. "Perception of Risk." *Science* 236, no. 4799 (1987): 280–285. https://doi.org/10.1126/science.3563507
- Nyhan, Brendan, and Jason Reifler. "When Corrections Fail: The Persistence of Political Misperceptions." *Political Behavior* 32, no. 2 (2010): 303–330. https://doi.org/10.1007/s11109-010-9112-2
