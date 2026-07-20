---
title: "'Anti-cheating bra' is real invention — but you can't really buy it"
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
earc_mode: "C"
gap_category: "real-but-misrepresented"
snopes_url: "https://www.snopes.com/news/2025/04/06/japan-bra-anti-cheating/
snopes_verdict: "not-addressed"
summary: >
  A video circulating since July 2024 shows a functional fingerprint-recognition bra clasp, promoted as an "anti-cheating" device. The device is real and functional, built from an M5Stack biometric module by Japanese creator ZAWAWORKS — a self-described "delusional inventor" known for comedic concept gadgets. It is not commercially available, was never intended for mass production, and was created explicitly as satirical content. The device's viral spread across Instagram, X, YouTube, and TikTok illustrates how satirical invention and genuine technology can become indistinguishable when stripped of context.
tags:
  - truth-vault
  - viral-invention
  - japan
  - wearable-technology
  - satire
  - biometrics
  - gender-technology
  - internet-culture
  - diy-electronics
---

## The Claim

Since mid-2024, a video has circulated repeatedly across Instagram, X (formerly Twitter), YouTube, Facebook, Threads, and TikTok claiming to show an "anti-cheating bra" invented in Japan. The device shown in the video is a bra clasp fitted with a biometric fingerprint scanner; the clasp remains locked until a registered fingerprint is detected by the scanner, at which point it pops open. The claims accompanying the video stated that the bra "only opens when your boyfriend's fingerprint is recognised" — presenting it as a technological solution to romantic infidelity by making the wearer's undergarments physically inaccessible without the partner's biometric authorisation.

By the time Snopes investigated in April 2025, a single Instagram post featuring the video had accumulated more than 135,000 likes (Wrona, 2025). The video appeared in multiple formats across platforms: as a reel, a short clip, a YouTube video, and a TikTok post. Reactions ranged from admiration ("this is genius") to concern ("this is a control device") to scepticism ("this must be fake") — with a substantial share of commenters approaching it as a genuine commercial product that could or should be purchased.

Two distinct claims require evaluation. The first is whether the device shown actually works — whether it is a functional fingerprint-recognition bra clasp or a prop. The second is whether the device is or was ever a commercially available product that consumers could purchase.

The answer to the first question is yes: the device is functional. The answer to the second is no: it is a one-off prototype never intended for sale.

---

## What's Actually True

The video originates from a July 19, 2024 post by a Japanese creator who operates under the name ZAWAWORKS on X (@zawa_works). The original Japanese-language caption translates as: "I invented a 'fingerprint recognition bra' to prevent cheating! Now only your boyfriend can remove your bra!" (Wrona, 2025).

ZAWAWORKS is a self-described "delusional inventor" (妄想発明家, *mōsō hatsumeika*) — a deliberate title that signals the satirical and comedic register of the work. His real name is Aizawa Yuki (相澤 裕貴), and he operates primarily on X, YouTube, and TikTok, where he posts a new comedic invention video every Friday. According to his website (zawa.works), his work has been featured in Japanese comedy shows and exhibitions, particularly in Osaka. He describes his creative mission as "inventing devices that make adolescent fantasies come true" — a framing that positions his output explicitly in the register of absurdist humour rather than genuine engineering ambition.

The fingerprint recognition bra is technically functional. ZAWAWORKS confirmed to Snopes via email that the clasp mechanism works and identified the specific hardware used: an M5Stack "Hat Finger" biometric fingerprint recognition module — a commercially available development board produced by M5Stack Technology Co., Ltd., a Hong Kong-based electronics company focused on modular IoT hardware (M5Stack, 2024). The M5Stack ecosystem is popular in the maker community for rapid prototyping: the modules are pre-built functional units with documented APIs, eliminating the need to build sensor hardware from scratch. The Hat Finger module includes an optical fingerprint scanner capable of registering and matching fingerprint patterns with reasonable accuracy.

ZAWAWORKS attached the M5Stack fingerprint module to the bra clasp mechanism so that actuation of the clasp release was gated on fingerprint verification. The device described in his X post is therefore the result of integrating a commodity biometric module with a standard garment fastener — not a custom-engineered technology from first principles. This is creative prototyping within the DIY electronics and maker tradition, not industrial product development. The device works, but it is a proof-of-concept assembled for comedic content creation, not an engineered product with durability requirements, regulatory compliance, or consumer safety review.

ZAWAWORKS explicitly confirmed to Snopes that the bra was a "one-off prototype" (Wrona, 2025). He clarified that his content model — weekly short-form video of comedic inventions — is the purpose, not the inventions themselves. "I create funny contents and post the videos on X and YouTube every Friday, to make people laugh," he said via email. The "anti-cheating bra" fits into a catalogue of his other inventions showcased on his website, which includes a "device that cuts only underwear," a "breastfeeding cigarette," and a "boobs keyboard" — a set of devices sharing an absurdist adolescent-fantasy conceptual logic that is broadly recognisable as satire.

---

## Why the Video Went Viral Without Its Context

The "anti-cheating bra" video's global spread, reaching audiences in Indonesia, the Philippines, Brazil, Kenya, and elsewhere across multiple platform contexts, illustrates a specific mechanism of viral decontextualisation that is worth examining carefully.

**The satirical register was invisible without context.** The video demonstrates a working device with minimal contextual framing. There is no laugh track, no obvious comedic staging, no disclaimer labelling it fiction, and no Japanese comedy-show context visible in the clip as it circulated. The demonstration is matter-of-fact: a hand approaches the bra clasp, a fingerprint is scanned on the attached module, and the clasp springs open. Without knowledge of ZAWAWORKS or the Japanese maker-comedy tradition he operates in, the video is simply a demonstration of a working device. The satirical intent is entirely in the creator's title ("delusional inventor"), his caption framing, and his broader content catalogue — none of which survived the decontextualised clip's spread across platforms.

This is a general problem with satire in the age of platform-mediated content distribution. Satire depends on shared context: the audience needs to be able to identify the satirical register in order to process the content correctly. When content travels from its original context — a Friday-posting Japanese DIY comedy creator with 11,000 X followers and 47,000 TikTok followers, posting explicitly within an absurdist invention genre — to global viral distribution across platforms with different audience demographics and zero ambient context, the satirical signal is stripped and the literal content remains. A video of a working fingerprint-recognition bra clasp, stripped of ZAWAWORKS' creative context, reads as a video of a working fingerprint-recognition bra clasp.

**The device's technical plausibility aided misreading.** The barrier to building a working fingerprint-recognition door lock, phone case, or garment fastener is currently very low. Biometric fingerprint modules cost under $20 on component marketplaces; the M5Stack Hat Finger module used by ZAWAWORKS is a standard retail product. For a technically literate audience, a working fingerprint-recognition bra clasp is not surprising — it's simply an application of commodity biometric hardware to a garment fastener, requiring modest microcontroller programming. For a non-technically literate audience, the functionality may seem genuinely impressive and the commercially-available inference plausible, because many sophisticated consumer electronics (phones, laptops) already use fingerprint recognition and the jump to a garment application is conceptually small. The plausibility of the device made the commercial framing in circulation ("a Japanese inventor made a product you might buy") easy to accept uncritically.

**The gendered framing leveraged existing viral mechanics.** The premise of the device — a garment that grants access to the wearer's body only with biometric authorisation from a designated male partner — sits at the intersection of technology, sexuality, and gender relations in a way that generates strong reactions across a wide range of ideological positions. Reactions were varied: some found the device empowering for women (controlling who can undress them), others found it controlling (positioning the boyfriend's fingerprint as the authorisation authority), others found it funny, others found it creepy. The device generated strong cross-cutting reactions because it touched on topics people hold real views about: consent, bodily autonomy, technological surveillance, relationship dynamics, and the gendered politics of wearable technology. Strong cross-cutting reactions drive sharing. The viral spread of the video was substantially amplified by the fact that it generated this range of responses, each of which motivated different sharing behaviours.

---

## Epistemic Novelty: The "Delusional Inventor" as Media Genre

ZAWAWORKS operates within a recognisable creative tradition that straddles Japan's specific comedy and maker cultures, and understanding that tradition is important for correctly reading what his content is and how it circulates.

**The Japanese kaden (home appliance) invention comedy tradition** has a long history in Japanese popular culture, appearing repeatedly in televised comedy formats, exhibition contexts, and online platforms. Inventors creating absurd, technically plausible but socially bizarre devices — gadgets that solve non-problems, indulge adolescent fantasies, or apply engineering rationality to domains where it is comically inappropriate — have been a recurring comedic category. ZAWAWORKS' self-description as "delusional inventor" explicitly invokes this tradition. His public performances at comedy events in Osaka and his appearances on comedy shows place him within that institutional context in ways that would be legible to a Japanese audience familiar with the genre, but entirely invisible to an international audience encountering the video without that framing.

**The maker movement and open hardware ecosystem** that ZAWAWORKS works within — characterised by the use of platforms like Arduino, Raspberry Pi, M5Stack, and similar modular embedded computing kits — has produced a global community of creators who build functional prototypes for demonstrations, content creation, and personal exploration rather than product development. Within this community, the distinction between "working prototype" and "commercially viable product" is clear and well understood: working prototypes are common; commercially viable products are rare and require engineering, testing, manufacturing, regulatory compliance, and supply chain development that most maker-community creators neither pursue nor intend to. The M5Stack Hat Finger fingerprint module being available for purchase does not make a device built with it "commercially available" — it makes it a creative application of a development tool.

This distinction — between technology that works and technology that is productised — is frequently lost in viral content distribution. When a working biometric bra clasp demonstation circulates globally, the information "this was made with a $20 development board by a comedy creator as weekly content" does not travel with it. What travels is: "someone in Japan made a bra that only your boyfriend can open." That proposition is simultaneously true (the device functions) and false (there is no product you can buy) — a conjunction that generates exactly the kind of confused, contested viral response the video received.

**The consent and control dimensions** of the device as it was presented in viral circulation deserve separate attention. Several commenters on Instagram and X raised the criticism that a device whose premise is that a woman's bra can only be opened by her boyfriend's fingerprint implies a concerning power dynamic — that the device is framed from the perspective of the boyfriend's desire to control access to the wearer's body rather than from the perspective of the wearer's control over their own body. ZAWAWORKS' original post was phrased as "now only your boyfriend can remove your bra" and "please give it as a gift to your girlfriend or wife" — framing that addresses male partners as the audience, not female wearers.

This framing dimension is not unique to ZAWAWORKS and not attributable solely to satirical failure: the viral captions that circulated with the video across Instagram and X reproduced and amplified this framing. "An inventor in Japan has created a bra against Touch ID cheating. It only opens when your boyfriend's fingerprint is recognised" positions the device as the boyfriend's tool for management of the girlfriend's accessibility. That this framing is itself part of the comedic register — the absurdity of men trying to technologically enforce fidelity through garment design — does not neutralise its effect when framed straight in viral circulation. The satirical commentary on a specific kind of male anxiety about partner fidelity becomes, when stripped of context, simply the expression of that anxiety in product form.

This is one of the ways in which the decontextualisation dynamic described above is not merely epistemically neutral. Satirical content that comments on gendered power dynamics can, when its satirical register is invisibilised, circulate as uncritical endorsement of those dynamics. Understanding ZAWAWORKS' comedy requires knowing that he is doing something in the tradition of absurdist commentary on male adolescent fantasy — including the fantasy of technologically controlling a partner. Encountering only the demonstration video without that context leaves the commentary stripped and the fantasy object intact.

---

## The Technology: Biometrics and Wearables

Setting aside the satirical dimensions, the device ZAWAWORKS created raises genuine questions about the intersection of biometric technology and wearable garments that are worth brief consideration, as they are not purely hypothetical even if this particular device is not commercially produced.

**Biometric access control in wearable contexts** is an active area of research and product development, though currently concentrated in smartwatches, fitness trackers, and authentication tokens rather than garments. The integration of biometric sensors into flexible, washable garment structures presents real engineering challenges: sensors require power; garments are washed; electronic connections on worn garments experience flexion stress that degrades connectors and circuit traces; and biometric sensors require calibration stability that may not survive the conditions garments encounter (sweat, body heat variation, mechanical deformation). None of these challenges are insuperable, but they require engineering investment beyond what a maker prototype demonstrates.

The M5Stack Hat Finger module used by ZAWAWORKS was not designed for integration into wearables — it is a rigid development board with no flexibility, washability, or garment-integration features. Producing a commercially viable garment-integrated biometric clasp would require either significant miniaturisation and ruggedisation of the sensing technology or the use of flexible electronics substrate technology currently in laboratory development rather than commodity production. The fact that the prototype works does not imply that a commercial version would be straightforward to produce.

**The philosophical paradox of access-controlled intimate garments** is genuinely interesting as a thought experiment in the philosophy of technology, consent, and body autonomy, independent of its ZAWAWORKS origin. Garment access control devices do exist in other forms — chastity devices with lock mechanisms are a real product category with documented use in certain communities. The fingerprint recognition version introduces a biometric-data dimension: the authorised person's fingerprint is enrolled in the device, creating a data relationship between a bodily biometric and the device's authorisation logic. Questions about who controls the enrolled fingerprint data, what happens if the relationship changes and the enrolled fingerprint needs to be changed, and how the device handles failure modes (battery death, module malfunction, emergency) are not trivial engineering or policy questions, even if they arise only in the context of a satirical prototype.

---

## Verdict

**The device is real; the product is not.** The fingerprint recognition bra clasp shown in videos circulating since July 2024 is a genuine, functional device built by Japanese creator ZAWAWORKS using an M5Stack biometric fingerprint module. It works as shown: the clasp is locked until a registered fingerprint is verified, then springs open. ZAWAWORKS confirmed its functionality and its construction materials to Snopes (Wrona, 2025).

However, the device is a one-off comedic prototype, created for weekly short-form video content by a creator operating in an explicitly satirical absurdist-invention genre. It was never intended for commercial production, has not been patented or licenced, and is not available for purchase anywhere. The viral spread of the video, which reached audiences across multiple continents and dozens of platforms, stripped the device of its original comedic context and circulated it as a genuine commercial product claim. The spread illustrates how satire and technical demonstration can become indistinguishable at scale when the signals that mark satirical register — creator context, platform community norms, cultural familiarity with the genre — do not travel with the content.

---

### Sources

- Wrona, A. (2025, April 6). 'Anti-cheating bra' is real invention — but you can't really buy it. *Snopes*. https://www.snopes.com/news/2025/04/06/japan-bra-anti-cheating/
- ZAWAWORKS. (2024, July 19). [X post demonstrating fingerprint recognition bra]. X. https://x.com/zawa_works/status/1814268957807051071
- ZAWAWORKS. (2024). Fingerprint recognition bra [YouTube video]. YouTube. https://www.youtube.com/watch?v=X06PQvEFiFI
- ZAWAWORKS. (2025). About ZAWAWORKS. https://zawa.works/abouts
- M5Stack Technology Co., Ltd. (2024). Hat Finger – Fingerprint Sensor. https://docs.m5stack.com/ja/hat/hat-finger
- Pasquale, F. (2015). *The Black Box Society: The Secret Algorithms That Control Money and Information*. Harvard University Press.
- Turkle, S. (2011). *Alone Together: Why We Expect More from Technology and Less from Each Other*. Basic Books.
- Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence*. Yale University Press.
- Wardle, C., & Derakhshan, H. (2017). *Information Disorder: Toward an Interdisciplinary Framework for Research and Policy Making*. Council of Europe.
- boyd, d., & Crawford, K. (2012). Critical questions for big data: Provocations for a cultural, technological, and scholarly phenomenon. *Information, Communication & Society*, 15(5), 662–679.
