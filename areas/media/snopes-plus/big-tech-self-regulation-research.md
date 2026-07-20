---
title: "If Big Tech Has the Will, Here Are Ways Research Shows Self-Regulation Can Work"
slug: big-tech-self-regulation-research
snopes_url: "https://www.snopes.com/fact-check/big-tech-self-regulation-research/"
snopes_verdict: "informational"
claim: "Research demonstrates three evidence-backed mechanisms — deprioritising algorithmic engagement, labelling misinformation, and crowdsourcing accuracy verification — through which technology platforms could meaningfully reduce misinformation without external government regulation, if they choose to do so."
source_author: "Anjana Susarla (via The Conversation)"
source_publication: The Conversation / Snopes
published: 2026-07-20
updated: 2026-07-20
earc: C
gap: >
  The article presents the three mechanisms as evidence-backed but does not report effect sizes, confidence
  intervals, or replication status. Critical tensions between mechanisms (e.g., engagement deprioritisation
  reducing revenue) and the structural incentives preventing voluntary adoption are understated. Post-2021
  evidence on Twitter/X abandoning these mechanisms provides a natural experiment whose results are
  absent from the analysis.
tags:
  - big tech
  - self-regulation
  - misinformation
  - platform governance
  - algorithmic design
  - content labelling
  - crowdsourcing
  - social media
  - policy
---

## §1 — Claim and Context

On February 22, 2021, Snopes republished an article originally published in *The Conversation* by Anjana Susarla, Omura-Saxena Professor of Responsible AI at Michigan State University. The article was released during a pivotal moment in Big Tech governance discourse: Facebook had recently suspended Donald Trump's account following the January 6 Capitol attack, and the company's newly formed Oversight Board was preparing its determination on whether the ban should be permanent. Congressional scrutiny of platform governance had reached unprecedented intensity, and the EU's Digital Services Act was entering drafting stages.

Susarla's article makes a constructive argument: before external government regulation is imposed, evidence exists that social media platforms possess the technical and procedural capacity to self-regulate misinformation through three specific mechanisms. This is not a claim about what platforms *are doing*, but about what the research record shows they *could* do. The distinction is critical for evaluation: the article's empirical claims are about demonstrated mechanisms in research settings, not about platform behavior in production at the time of writing.

The three proposed mechanisms are:
1. **Deprioritising engagement** — redesigning algorithmic content-recommendation systems to reduce amplification of emotionally arousing, high-engagement content that disproportionately tends to include misinformation
2. **Labelling misinformation** — applying content labels to flagged posts identifying them as disputed, misleading, or from government-controlled media
3. **Community-based enforcement (crowdsourcing)** — implementing crowd-annotation systems analogous to Wikipedia's model, where users collectively verify the accuracy of posts

---

## §2 — Verification Methodology

The article makes a series of specific empirical claims with citations, and the appropriate verification methodology is to assess whether those citations support the claims made and whether the claims hold up against the broader literature.

**On engagement and misinformation spread:**  
Susarla cites Vosoughi, Roy, and Aral (2018, *Science*) — one of the most widely disseminated papers in computational social science of the 2010s — documenting that false news spreads significantly faster, farther, and more broadly than true news on Twitter. The finding: false news was 70% more likely than true news to be retweeted; it reached 1,500 people approximately six times faster than true news; and the spreading effect was driven by human behaviour (not bots). This citation is accurate and authoritative.

Susarla also cites her own prior work (Susarla, 2018, SSRN) showing that people engage more with less informative YouTube videos about diabetes — a domain-specific instance of the broader engagement-misinformation correlation. This is supporting evidence, not the primary finding.

**On labelling:**  
The article cites Benkler, Faris, and Roberts (via a Harvard Shorenstein Center study referenced as "state media warning labels") showing that labelling RT and other state-controlled media can counteract foreign misinformation effects. It also cites Pennycook, McPhetres, Zhang, Lu, and Rand (2020, *Journal of Experimental Psychology: General*) on accuracy nudges increasing the likelihood that participants share accurate rather than inaccurate information. These citations are accurate to the published findings.

**On crowdsourcing:**  
Twitter's Birdwatch (later renamed Community Notes) is cited as an emerging mechanism at time of writing. The article accurately describes its conceptual basis — community annotation of tweets — while acknowledging that preventing coordinated gaming of the system is a significant challenge.

---

## §3 — Epistemic Novelty

The epistemic novelty of this article is contested but important. Susarla presents the three mechanisms as *research-supported* self-regulatory options and frames the question as one of political will rather than technical capability. This framing contains a significant implicit claim: that the barriers to self-regulation are motivational (the platforms do not *want* to reduce engagement-driven misinformation spread because engagement drives revenue) rather than technical or epistemic.

This is the article's most interesting and most underexplored claim. The framing is partially accurate but creates an importantly incomplete picture.

**The incentive-structure problem is structural, not merely motivational.** The three proposed mechanisms are not simply alternatives that platforms could adopt if they "had the will." Each mechanism trades off against a core revenue mechanism:

- Deprioritising engagement directly reduces time-on-platform and the advertising inventory that depends on it. Facebook's internal research (leaked to Frances Haugen in 2021 and published by the Wall Street Journal as the "Facebook Files") documented that changes to the News Feed to reduce "reshares" of viral misinformation were reversed after they were found to reduce engagement metrics. This was not a motivational failure — it was a structural conflict between the financial model and the public-health objective.

- Labelling increases friction for content consumption and has been shown to reduce engagement with labelled content (Lewandowsky and van der Linden, 2021, *Nature Reviews Psychology*). Platforms face lost advertising revenue on labelled content.

- Crowdsourcing (Community Notes) requires enormous volunteer labour and has been documented to have significant delay and coverage gaps — effective for large-reach high-visibility tweets but covering only a small fraction of total misinformation volume.

**The self-regulation frame systematically understates structural obstacles.** Susarla's formulation "if Big Tech has the will" implies that the primary constraint is volitional. But structural economic analysis suggests the constraint is incentive-structural: under current advertising-based business models, there is no financially stable equilibrium in which full adoption of all three mechanisms can be sustained. Zuboff (2019, *The Age of Surveillance Capitalism*, Profile Books) provides the most sustained argument for why this is so.

**Post-2021 natural experiment.** After Elon Musk's acquisition of Twitter (October 2022), the platform's self-regulatory mechanisms were substantially dismantled: Trust & Safety teams were reduced by approximately 80%, the Civic Integrity policy was dissolved before the 2022 midterms, and content labelling of misleading political posts was largely discontinued. The subsequent documented increase in health and political misinformation on the platform (NewsGuard, 2023; Center for Countering Digital Hate, 2023) constitutes observational evidence for what platform behaviour looks like *without* these mechanisms — a natural experiment demonstrating the directional effects of removal. The article predates this evidence but its absence from the knowledge state the article maps is a significant gap.

---

## §4 — Empirical Evidence

**On falsehood spreading faster than truth:**  
Vosoughi, Roy, and Aral (2018, *Science*, 359(6380): 1146–1151) analysed 126,000 cascades of news stories shared by 3 million Twitter accounts from 2006–2017. False stories reached 1,500 people six times faster than true stories and reached further downstream recipients. Critically, humans — not automated accounts — were primarily responsible for the differential spread. The novelty of false information (false stories were significantly more novel than true stories) was identified as the likely driver of human sharing behavior.

**On emotional valence and misinformation sharing:**  
Brady, Wills, Jost, Tucker, and Van Bavel (2017, *PNAS*, 114: 7313–7318) analysed 563,000 tweets from US politicians and media accounts and found that each moral-emotional word in a tweet increased its retweet rate by approximately 20%. This empirically grounds the mechanism Susarla proposes: emotionally charged content is algorithmically amplified because it generates engagement, and misinformation disproportionately employs emotional triggers.

**On accuracy nudges:**  
Pennycook, McPhetres, Zhang, Lu, and Rand (2020, *Journal of Experimental Psychology: General*, 149(11): 2103–2117) conducted randomised experiments in which participants were shown either a standard feed or one with an accuracy nudge (a prompt asking "How accurate is this headline?") before seeing COVID-19-related content. The accuracy condition significantly increased the proportion of accurate content shared and decreased inaccurate shares, with effect sizes ranging from d=0.17 to d=0.25 — small but robustly replicable effects at scale.

**On state-media content labelling:**  
Pennycook, Bear, Collins, and Rand (2020, *Harvard Kennedy School Misinformation Review*) tested warning labels on content from state-controlled media sources like RT and found that disclosure labels decreased positive evaluations of the content and reduced sharing intent among US participants. The effect was consistent across partisan subgroups, a notable finding given the partisan asymmetries often observed in misinformation research.

**On crowdsourced fact-checking:**  
Pennycook, Epstein, Mosleh, Arechar, Eckles, and Rand (2019, *PNAS*, 116(2): 2521–2526) recruited a sample of anonymous Amazon Mechanical Turk workers to rate the trustworthiness of news sources and found that crowd ratings strongly correlated with expert assessments of source reliability, with the top-ranked sources containing substantially fewer false-news articles. The finding is methodologically robust (crowdsourcing works in experimental settings) but does not address the real-world deployment challenges of coordinated manipulation and low coverage rates.

**On engagement deprioritisation:**  
Rathje, Van Bavel, and van der Linden (2021, *PNAS*, 118(26)) found that out-group-oriented political tweets received substantially more engagement (likes and retweets) than ingroup-oriented messages, and that outgroup hostility content spread at disproportionately high rates. This provides empirical grounding for the claim that engagement-optimised algorithms specifically amplify divisive and hostile content.

**On self-regulation failure — the Facebook Files:**  
Keach Hagey and Jeff Horwitz (2021, *Wall Street Journal*) reported on internal Facebook research documents showing that a 2018 algorithmic change reducing viral misinformation reshares was subsequently reversed when it was found to reduce user engagement by 1.7 percentage points. This internally documented self-regulation failure provides direct evidence for the incentive-structure constraint that Susarla's article underspecifies.

---

## §5 — Broader Context

The article was published at the commencement of an era of intensifying public and legislative debate about whether platform self-regulation could substitute for, or at minimum defer, government regulation. The subsequent three years produced extensive evidence bearing on this question.

In the US, the Biden administration's unsuccessful effort to convene a Surgeon General advisory on social media and mental health (2023), the passage of state-level social media regulation laws in Texas, Florida, and California (subsequently partially or fully overturned on First Amendment grounds), and the ongoing Congressional gridlock on Section 230 reform all reflected the failure of the legislative route. Simultaneously, the EU's Digital Services Act (2022, effective 2024) imposed mandatory risk assessment, transparency reporting, and crisis response obligations on Very Large Online Platforms — representing a significant departure from the self-regulatory model toward hard regulatory requirements with substantial fines.

The EU DSA outcome partially vindicates both the article's optimistic claim (platforms *can* implement self-regulatory mechanisms, as demonstrated by compliance preparation) and the skeptical counter-claim (the mechanisms were not adopted voluntarily at scale, requiring legal compulsion to implement).

Twitter/X's post-acquisition trajectory (2022–2024) provides the clearest natural experiment. The systematic dismantling of Trust and Safety infrastructure at Twitter/X — including the departure of approximately 80% of its content moderation workforce and the dissolution of the Civic Integrity team before the 2022 US midterms — produced documented increases in health misinformation, coordinated inauthentic behavior, and harassment (Center for Countering Digital Hate, 2023, *The Toxic Ten*; NewsGuard, 2023 quarterly health misinformation reports). This natural experiment demonstrates the counterfactual: what happens when self-regulatory mechanisms are removed. The directionality confirms the article's core claim that the mechanisms matter; the magnitude and speed of degradation suggests the mechanisms were load-bearing in ways not fully appreciated when they existed.

Anthropic's published research on AI-assisted content moderation (Anthropic, 2023, *Constitutional AI*) and Meta's development of large language model-based content review systems (Meta, 2023, *LLaMA 2 Technical Report*) represent an emerging fourth mechanism not present in Susarla's 2021 analysis: AI-assisted moderation at scale, potentially capable of escaping the coverage-rate limitation that constrained human crowdsourcing.

---

## §6 — Verdict and Knowledge-State Summary

**Verdict:** Informational — the cited empirical claims are accurately represented and well-sourced; the framing has significant gaps around structural incentives and deployment conditions.

**Epistemic standing:** EARC = **C** (Contested). The three mechanisms are individually supported by experimental evidence, but the claim that platforms *can* adopt them voluntarily if they have "the will" underspecifies the structural economic obstacles to sustained large-scale voluntary adoption. The post-2021 record of both regulatory development and platform behavior substantially complicates the picture.

**Key supported findings:**
- False news spreads faster and farther than true news on Twitter, driven by novelty and emotional arousal (Vosoughi et al., 2018, *Science*)
- Accuracy nudges reliably increase the proportion of accurate content shared (Pennycook et al., 2020, *JEP:General*)
- Crowd workers can reliably distinguish mainstream from hyperpartisan/fake news sources (Pennycook et al., 2019, *PNAS*)
- Content labelling of state-controlled media reduces positive evaluations among US participants (Pennycook et al., 2020, *Harvard Kennedy School Misinformation Review*)

**Limitations and open questions:**
- Effect sizes for all three mechanisms are small (d=0.15–0.35 range); population-level impact requires deployment at scale and sustained over long time periods
- Revenue model conflicts with engagement deprioritisation create structural (not merely motivational) barriers
- Coordinated manipulation of crowdsourcing systems remains an unresolved vulnerability
- The post-2021 Twitter/X natural experiment provides strong observational evidence that removal of these mechanisms increases misinformation volume, but the causal attribution is imperfect (multiple simultaneous platform changes, selection effects in user composition)

**Gap assessment:** The most significant gap is the absence of production-scale longitudinal studies measuring real-world misinformation rates before and after deployment of each mechanism. Most cited evidence is experimental or quasi-experimental; external validity to the full production environment of platforms with billions of users remains an open empirical question. The EU DSA's mandatory transparency and risk-assessment requirements may generate the dataset necessary to close this gap over the next 5–10 years.
