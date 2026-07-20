---
title: 'Fake Google AI Overview Screenshots Go Viral After New Feature''s Rollout'
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
earc_mode: "R"
gap_category: "authentic-mixed-with-fabricated"
snopes_url: "https://www.snopes.com/fact-check/google-ai-feeling-depressed/"
snopes_verdict: "not-addressed"
summary: >
  When Google rolled out its AI Overview feature to American users in May 2024, real examples of nonsensical or potentially dangerous AI-generated responses were shared widely on social media — but so were a substantial number of fabricated screenshots designed to look like AI Overview outputs. The most viral fake was a screenshot showing AI Overview responding to "I'm feeling depressed" by advising users to jump off the Golden Gate Bridge, which never appeared as a real output and was later acknowledged as fabricated by its original poster. The episode illustrates the specific challenge of verifying AI output claims in an environment where authentic AI failures and planted forgeries share the same visual format.
tags:
  - truth-vault
  - google
  - ai-overview
  - generative-ai
  - misinformation
  - fabricated-screenshots
  - llm
  - ai-hallucination
  - social-media
  - mental-health
---

## The Claim

In mid-May 2024, Google deployed its AI Overview feature — a generative AI system that produces summary answers to search queries and displays them prominently at the top of search results — to US users as part of a broader rollout of AI capabilities in its Search product. The deployment was almost immediately attended by controversy, as users began sharing screenshots of AI Overview outputs that were nonsensical, factually incorrect, potentially dangerous, or darkly comedic.

The claims encompassed by this story are multiple, intersecting, and require separate treatment. There are several distinct categories of claim in circulation: claims about real AI Overview outputs that were genuinely erroneous (such as the "glue in pizza sauce" recommendation, which Google confirmed as authentic); claims about fabricated AI Overview screenshots that were presented as real (such as the "depressed / Golden Gate Bridge" screenshot, which Google confirmed was fake and which was later admitted as fabricated by its original poster); and implicit claims about what AI Overview's deployment reveals about the reliability and safety of large language model-based search features.

The Snopes article by Aleksandra Wrona, published May 29, 2024, addressed the specific claim that circulated most widely and most harmfully — the Golden Gate Bridge/depression screenshot — as well as the broader question of how to distinguish genuine AI Overview failures from fabricated ones.

---

## What's Actually True

Google's AI Overview feature was rolled out to American search users in mid-May 2024, as announced on the Google Blog on May 14, 2024. The feature uses the Gemini large language model to generate synthesised answers to user queries, displayed in a highlighted box at the top of results before organic links. The feature was designed to reduce the need for users to click through to individual pages by providing an integrated, conversational-format summary.

Almost immediately after the rollout, users began encountering outputs that were surprising and, in some cases, alarming. The most widely circulated genuine AI Overview failure was a response to a question about pizza, in which the AI recommended adding glue to pizza sauce to help the cheese adhere to the crust — a response Google spokesperson Ned Adriance confirmed to Snopes as authentic. The AI had, as a Business Insider correspondent documented, apparently incorporated content from a Reddit comment that was originally written as a joke, then processed the joke as a genuine recommendation. Similarly confirmed as authentic was an AI Overview response recommending that humans eat "at least one small rock per day," presumably deriving from geological science outreach content processed without appropriate tonal calibration.

These genuine failures are real and significant. They illustrate a fundamental challenge in the deployment of large language models in high-stakes information contexts: LLMs are trained to produce fluent, authoritative-sounding responses and do not have reliable mechanisms for distinguishing ironic, satirical, or comedic input from sincere informational input. This creates systematic vulnerability to the ingestion of joke content from sources like Reddit and to the absence of calibration for social context in training data (Floridi & Cowls, 2019, *Philosophy and Technology*; Bender et al., 2021, "On the Dangers of Stochastic Parrots," *ACM FAccT Conference*).

However, embedded in the wave of authentic AI failure screenshots was a substantial number of fabricated images. The most virally significant was a screenshot showing an alleged AI Overview response to the search query "I'm feeling depressed," in which the AI appeared to advise the searcher: "One Reddit user suggests jumping off the Golden Gate Bridge." This image circulated on Reddit, Instagram, and Threads, accumulating substantial shares and generating substantial concern about AI safety in mental health contexts — concern serious enough that it was initially cited in a New York Times technology article on the AI Overview controversy.

Google's spokesperson Ned Adriance confirmed to Snopes in an email that this screenshot was fabricated and that the AI Overview it depicted was never actually generated. "The most notable example is a screenshot of an alleged AI Overview providing instructions on self-harm – which has been shared widely. This is a fake image, and this AI Overview never appeared," Adriance wrote. He noted that the original poster had acknowledged fabricating it. The New York Times subsequently issued a correction acknowledging that the screenshot had been incorrectly cited as authentic.

Adriance also provided Snopes with additional examples of fabricated AI Overview screenshots: a doctored image showing a response to "Is it okay to leave a dog in a hot car?" affirming that it is always safe to do so; a fake response to "Smoking while pregnant" recommending that doctors advise 2–3 cigarettes per day during pregnancy; and fabricated screenshots addressing gay Star Wars characters, astronaut responsibilities, and neurotoxin consumption. Some social media users explicitly shared templates and instructions for generating fake AI Overview images, further confirming that a significant portion of the circulating screenshots were deliberate fabrications.

---

## Why People Believe This

The AI Overview misinformation episode is an epistemically distinctive event whose mechanics differ in important ways from most other viral misinformation categories. Understanding the specific dynamics is valuable because the scenario it represents — authentic AI failures mixed with fabricated screenshots in the same visual format — is likely to recur as AI-generated interface outputs proliferate.

**The authentic plausibility problem.** The genuine AI Overview failures (pizza glue, small rocks) were so surprising that they established a high prior probability for additional alarming outputs. Once viewers had been exposed to confirmed authentic AI errors, they had reasonable grounds for believing that additional unusual outputs might also be authentic. The fabricated screenshots exploited this elevated prior: if Google's AI really recommended pizza glue, it was not obviously implausible that it might also advise depressed users to jump off bridges. In an environment where authentic AI failures are frequent and well-documented, fabricated claims about AI failures are harder to disbelieve.

**Visual format indistinguishability.** The AI Overview interface has a specific and recognisable visual format — a Google Search results page with a highlighted blue-accented box at the top containing the AI-generated response. This format is sufficiently simple that it can be replicated in graphic editing tools, screenshots of inspected HTML elements, or dedicated fake-screenshot tools. Jane Manchun Wong, a well-known tech researcher, shared a "DIY Google AI Overview template" on X during the viral episode, demonstrating how easily the format could be duplicated. The visual indistinguishability of authentic and fabricated screenshots is a structural property of the AI Overview format, not an accidental feature.

**The absence of independent verification pathways.** For most factual claims in visual misinformation, there are independent verification pathways: a satellite photograph can be cross-referenced against mapping databases; a claimed event can be checked against news archives; a person's identity can be verified through their documented public presence. For AI Overview screenshots, independent verification is significantly more difficult. The specific search query that allegedly generated a specific AI Overview response cannot be reliably replicated: LLM outputs are non-deterministic (they vary between instances), AI models are continuously updated (so a response generated on May 15 might not be reproducible on May 20), and the system may respond differently to the same query in different user sessions. The only definitive verification is obtaining authentic documentation of the specific session — which is typically unavailable.

This verification gap is an epistemic novelty: it creates a category of claim that is structurally harder to verify or refute than most content categories that fact-checkers encounter. The fabricators of the fake AI Overview screenshots appear to have understood this gap and exploited it deliberately.

**Emotional amplification and mental health framing.** The most viral fabricated screenshot — the depression/Golden Gate Bridge image — involved a mental health topic with particularly high emotional stakes. Audience members who saw the image and believed it authentic experienced genuine concern about AI systems advising suicidal action to vulnerable users. This emotional amplification drove sharing and engagement. Research on misinformation spread consistently demonstrates that emotionally arousing content with negative valence spreads faster and further than neutral content (Vosoughi, Roy & Aral, 2018, *Science*). The fabricators of the depression screenshot appear to have selected a topic precisely because its emotional activation was high — and consequently because its share mechanics were powerful.

**Institutional trust dynamics around AI deployment.** Google's AI Overview was deployed in a particular moment of heightened public ambivalence about the safety and reliability of large language models in consequential applications. The wave of concern about LLM hallucination, misinformation generation, and alignment failures had been building in both technical and popular discourse since the public release of GPT-3 (Brown et al., 2020, *NeurIPS*) and especially since the mass public adoption of ChatGPT from late 2022. Google's specific deployment of Gemini-based AI features had been attended by earlier controversies, including the generation of historically inaccurate images by the Gemini image generation tool in February 2024. This accumulated context primed audiences to be receptive to evidence of AI failure, lowering the threshold of belief for fabricated failure examples.

---

## Verdict

**The specific claim best captured by the slug (fake Google AI Overview screenshots going viral) is true as a meta-claim: both genuine AI failures and fabricated screenshots circulated together following the rollout.** The depression/Golden Gate Bridge screenshot specifically was fabricated and never appeared as an actual AI Overview. The pizza glue, small rocks, and related outputs were genuine.

Snopes published the article in the News category rather than the Fact Check category, reflecting the complex and multi-component nature of the story. The piece serves as a useful taxonomy: some of the AI Overview failures were real and significant; some were fakes that exploited the credibility of the real failures; distinguishing them requires company confirmation or evidence of fabrication tools, not just visual inspection.

The New York Times' erroneous citation of the depression screenshot as authentic, and its subsequent correction, is itself significant: it demonstrates that the visual indistinguishability problem affects institutional quality journalism as well as casual social media sharing. The verification challenge posed by non-deterministic AI outputs in rapidly updating systems is genuinely difficult, not just for casual audiences.

---

## The Wider Picture

The Google AI Overview episode belongs to a broader set of dynamics in AI deployment, AI output reliability, and the social epistemics of AI-related claims that extend well beyond the specific failures of May 2024.

**LLM hallucination as a documented phenomena.** The technical phenomenon underlying the genuine AI Overview failures — often called "hallucination" in popular coverage — is more precisely described as the generation of fluent, confident-sounding outputs that are factually incorrect or contextually inappropriate. Research in LLM evaluation has extensively documented hallucination phenomena across multiple categories: factual errors, logical errors, inappropriate generalisation from training data, and — most relevantly here — the ingestion of non-serious or fictional content and its reproduction as factual claim. Maynez et al. documented faithfulness and factuality problems in abstractive summarisation models (Maynez et al., 2020, *ACL*); Ji et al. published a comprehensive survey of hallucination in natural language generation (Ji et al., 2023, *ACM Computing Surveys*).

The specific failure mode exhibited in the pizza glue response — the AI ingesting a satirical Reddit comment and reproducing it as a sincere recommendation — reflects a deeper design challenge. LLMs are trained to produce outputs that are statistically consistent with their training data. Reddit is a major component of most large-scale language model training corpora. Reddit contains a large volume of humorous, satirical, and fictional content alongside sincere informational content. Models that lack reliable mechanisms for distinguishing the two will reproduce both types of content in similar formats — as sincere-seeming assertions.

**The Retrieval-Augmented Generation context.** Google's AI Overview reportedly uses a combination of language model generation and retrieval from indexed web content, an architectural approach known as Retrieval-Augmented Generation (RAG). In RAG systems, the model retrieves relevant content from a knowledge base (in this case, the web index) and uses it to ground its generated response. When the retrieved content includes satirical or fictional text (as Reddit frequently does), the generation process can incorporate it as if it were factual, particularly if the retrieval retrieves the joke text without its surrounding comedic context.

Lewis et al. formalised the RAG architecture in a 2020 NeurIPS paper documenting improved factual accuracy over pure generation; but subsequent research has documented that RAG systems remain vulnerable to "poisoning" from low-quality, misleading, or contextually inappropriate retrieved content (Shafran et al., 2024, *arXiv*). Google's pizza glue failure is a textbook case of this vulnerability.

**The fake screenshot as misinformation category.** Fabricated UI screenshots — fake text messages, fake social media posts, fake search results — are an established and growing misinformation category. The tools required are widely accessible: basic graphic editing software, browser inspector tools that allow direct HTML editing, and increasingly purpose-built screenshot-fabrication applications can all produce convincing replicas of common UI formats. Research on fake screenshot detection is ongoing, with methods including pixel-level forensic analysis, font rendering fingerprinting, and metadata examination (Farid, 2022, *Communications of the ACM*).

The AI Overview format is particularly vulnerable because it is new, less widely familiar visually (reducing audiences' ability to spot anachronisms), and because — as noted above — it cannot be independently verified by reproducing the specific output. Research on visual misinformation detection suggests that novelty of format significantly increases believability of fabrications: less familiar formats provide fewer cross-check opportunities for alert viewers (Pennycook & Rand, 2021, *Psychological Science*).

**Platform accountability and correction speed.** The AI Overview episode also raised questions about the appropriate corporate response when a rapidly deployed AI product generates failures at scale. Google's response — confirming some failures while flagging fabrications to journalists, and implementing changes to the AI Overview system to reduce the frequency of problematic outputs — was relatively swift by large-technology-company standards, but occurred after millions of impressions of both authentic failures and fabrications. The episode sharpens the question of what deployment speed and user testing protocols are appropriate for AI features that synthesise information in response to queries about sensitive topics including health and safety.

---

## How Fact-Checkers Handle It

Aleksandra Wrona's Snopes article, published May 29, 2024, is an example of fact-checking responding to a rapidly moving story with complex epistemic structure.

**Distinguishing authentic from fabricated within a category.** The article's central contribution is the taxonomy it provides: not all AI Overview failure screenshots are equivalent, and the article distinguishes confirmed-authentic errors from confirmed-fabricated ones. This distinction is critical for a reader trying to understand the AI Overview story accurately. Without the taxonomy, the story can be read as either "Google AI has comprehensive and dangerous safety failures" or "all the AI failure stories are fake" — both of which are inaccurate. The accurate picture is "specific failures were real and specific others were demonstrably fabricated, and distinguishing them requires active investigation."

**Source access: company spokesperson.** The critical verification mechanism in this story was access to Ned Adriance, a Google spokesperson who confirmed authentic failures and identified fabrications. This source relationship is what makes the fact-check possible in a scenario where independent verification is structurally difficult. Without Google's confirmation, a fact-checker would have limited tools for distinguishing authentic from fabricated screenshots. The story also illustrates the limits of independent fact-checking in an environment where the ground truth is accessible only to the platform whose product is being examined.

**Documenting the New York Times correction.** The fact-check's inclusion of the New York Times correction is important for multiple reasons. It confirms the depression screenshot's fabricated nature through an authoritative source (the Times' correction standards are rigorous). It demonstrates that the verification challenge affected quality institutional journalism. And it provides a dated, citable record that the fabrication was publicly acknowledged.

**Speed and incompleteness.** The article was published while the story was still developing rapidly — many additional fabricated screenshots circulated after the publication date, and Google subsequently made significant changes to the AI Overview feature, including restricting its responses to queries involving mental health topics. This is an inherent limitation of fact-checking fast-moving AI product stories: the relevant factual landscape changes faster than formal publication cycles allow. The article provides a valuable snapshot while explicitly framing several elements as ongoing and subject to update.

The episode remains significant as a case study in the misinformation ecology specific to AI product rollouts: a combination of genuine failures that establish plausible prior, fabricated content in indistinguishable format, emotional amplification through high-stakes topic selection, and structural verification difficulties that limit real-time correction. These factors are likely to characterise future AI product controversy episodes, and the Google AI Overview case provides a detailed template for understanding the dynamics involved.
