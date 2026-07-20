---
title: "The FBI warned people to stop using two-factor authentication via SMS"
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
gap_category: distorted-but-grounded
snopes_url: not-addressed
snopes_verdict: not-addressed
summary: >
  The claim that the FBI warned people to "stop using" SMS-based two-factor authentication conflates and overstates a real but narrower advisory record. The FBI, together with CISA and NSA, did explicitly warn in late 2024 that SMS-based authentication is vulnerable to interception and specifically should not be used for high-value targets, advising Americans to prefer end-to-end-encrypted communications and hardware-based multi-factor authentication. The strong version of the claim — that anyone using SMS 2FA should stop immediately — is an overcorrection: the FBI and cybersecurity consensus position is that SMS 2FA is substantially better than no 2FA at all, and stopping the practice without substituting a more secure alternative would worsen the security posture of most users.
tags:
  - truth-vault
  - two-factor-authentication
  - SMS
  - FBI
  - cybersecurity
  - CISA
  - MFA
  - SIM-swapping
  - SS7
  - authentication
  - security
---


# The FBI warned people to stop using two-factor authentication via SMS


## 1. The Claim

A claim that spread widely in late 2024 and continues to circulate holds that the FBI issued a warning urging the public to stop using SMS-based two-factor authentication (2FA). In its most pointed formulation, the claim presents this as a definitive federal advisory: if you receive one-time passcodes by text message when logging into accounts, the FBI is telling you that this practice is dangerous and should be discontinued immediately. Variations of the claim specify different targets of the threat — Chinese state hackers are the most commonly named actors in the 2024 wave, connected to the documented intrusions attributed to a group known as Salt Typhoon — while others frame it more generically as a blanket security advisory applying to everyone.

The claim circulated across news outlets, technology blogs, social media, and general-interest publications throughout late 2024. Headlines including "FBI warns Americans to stop using SMS for 2FA" and "Feds say to stop using SMS two-factor authentication" appeared in technology and mainstream media. The claim generated significant public anxiety about password security practices, with many readers concluding that they should remove SMS-based 2FA from their accounts — sometimes with the unintended consequence of disabling multi-factor authentication entirely because a more secure alternative was not readily available or understood.

To evaluate the claim accurately, it is necessary to examine what the FBI and associated federal agencies actually said, in what context they said it, to whom the advisory was directed, and how the security recommendation was framed relative to alternatives. The claim is not entirely wrong: there is a real advisory record, conducted by real federal agencies, that does express concern about SMS-based authentication. But the strong popular version of the claim — stop using it now, it is not safe, the government has warned you away from it — elides context and nuance that substantially changes the practical implications of the underlying advice.

Two-factor authentication — the practice of requiring a second verification step in addition to a password when logging into accounts — is one of the most consequential security practices available to ordinary users. Bad information about whether to use it, in what form, and for what purposes has direct implications for the security of millions of people's accounts. The claim therefore deserves careful examination rather than either casual acceptance or dismissal.


## 2. What's Actually True

**The Salt Typhoon intrusion and the federal advisory.** In November 2024, the Federal Bureau of Investigation (FBI), the Cybersecurity and Infrastructure Security Agency (CISA), the National Security Agency (NSA), and their Five Eyes partners issued a joint advisory responding to a large-scale intrusion by a Chinese state-sponsored hacking group, designated Salt Typhoon (also tracked under names including Earth Estries and GhostEmperor by different threat intelligence vendors). The intrusion targeted major US telecommunications carriers — AT&T, Verizon, and Lumen Technologies were among those publicly identified — and specifically compromised lawful intercept infrastructure: the technical systems telecommunications carriers maintain to comply with court-ordered surveillance requirements under the Communications Assistance for Law Enforcement Act (CALEA). Salt Typhoon's access allowed the interception of communications — including SMS traffic — for a substantial period before the intrusion was detected and contained.

The specific advisory published jointly by FBI and CISA in December 2024 recommended that "highly targeted individuals" — including government officials, political operatives, and others who might be of particular interest to nation-state threat actors — should prioritise encrypted communications and hardware-based multi-factor authentication over SMS-based communications and authentication. The advisory specifically stated that targeted individuals should "use only end-to-end encrypted communications" and avoid SMS as an authentication channel given the demonstrated ability of sophisticated adversaries to intercept it.

This is a real advisory, issued by real federal agencies, with real security rationale. It should not be dismissed or minimised. US telecommunications infrastructure was genuinely compromised in a manner that exposed SMS traffic, and the advisory correctly identified SMS interception as a consequence of that compromise.

**What the advisory said — and did not say.** The key analytical question is the scope of the advisory: was it directed at the general public, and did it advise stopping SMS 2FA? The FBI/CISA advisory was specifically framed around high-value targets of Chinese intelligence interest, not the general American public. The language about encrypted communications and hardware-based MFA appeared in the context of advising people who might plausibly be targets of nation-state APT (Advanced Persistent Threat) actors. The advisory did not contain language advising the general public to disable SMS-based 2FA for their personal email, banking, or social media accounts. The operative phrase was "highly targeted individuals."

Moreover, no FBI, CISA, or NSA communication in 2024 stated or implied that SMS 2FA should be replaced with nothing. The consistent message across official cybersecurity guidance from these agencies — in the advisory itself and in surrounding communications — was that any form of multi-factor authentication is substantially better than a password alone. CISA's broader identity and authentication guidance, published in its "More Than a Password" campaign and maintained as standing guidance, explicitly recommends enabling any available 2FA over using none, while noting that phishing-resistant methods (hardware security keys, FIDO2/WebAuthn standards) are superior to SMS-based codes.

**The real vulnerabilities of SMS-based 2FA.** The security concerns behind the advisory are genuine and well-documented, predating the Salt Typhoon intrusion by many years. SMS authentication is vulnerable to at least three distinct attack classes:

*SS7 protocol attacks:* The Signalling System No. 7 (SS7) protocol, which manages cell phone network routing worldwide, was designed in 1975 with minimal security assumptions appropriate to a closed network of trusted telecoms operators. Its current deployment in a landscape of interconnected global carriers, some operating in jurisdictions with poor security controls or active state compromise, allows a technically sophisticated adversary with access to SS7 infrastructure to redirect SMS messages in real time. Engel (2014, presented at the 31st Chaos Communication Congress and widely cited in subsequent security literature) demonstrated live SS7 SMS interception attack capabilities. Kopp, Kargl, and Holz (2017, in *Proceedings of the 12th ACM Asia Conference on Computer and Communications Security*, pages 297–307) documented SS7 vulnerability exploitation in the context of 2FA bypass.

*SIM swapping:* SIM swapping attacks exploit social engineering vulnerabilities in mobile carrier identity verification to fraudulently transfer a target's phone number to a SIM card controlled by the attacker, after which all SMS traffic — including authentication codes — routes to the attacker's device until the victim discovers the transfer. Jover (2020, *IEEE Security & Privacy*, vol. 18, pages 61–70) provided a structured analysis of SIM-swap attacks as a systematic 2FA bypass mechanism and documented their use in targeted financial theft and account takeover campaigns.

*Carrier infrastructure compromise:* The Salt Typhoon intrusion specifically demonstrated that nation-state threat actors can gain access to carrier traffic at the infrastructure level, with access to SMS content without any interaction with the end user's device. This attack class is qualitatively different from SS7 and SIM-swap attacks in that it does not require targeting specific communications; it allows bulk collection of traffic passing through the compromised carrier.

**The comparative security picture.** Despite these real vulnerabilities, SMS-based 2FA remains substantially more secure than a password alone for most users in most threat environments. Academic and industry analysis has consistently found that mass-scale credential stuffing and phishing attacks — which account for the vast majority of consumer account compromises — are effectively mitigated by any form of 2FA including SMS. Bonneau, Herley, van Oorschot, and Stajano (2012, *Proceedings of the IEEE Security and Privacy Symposium*, pages 467–481) provided a rigorous comparative analysis of authentication mechanisms and concluded that multi-factor approaches improve resistance to broad-based attacks significantly over single-factor authentication, with the residual risk varying by attacker capability. Google's internal security research, documented by Milka (2018 presentation at USENIX Enigma, referenced in industry security literature) found that SMS-based 2FA blocked 100% of automated bot attacks and approximately 96% of phishing attacks in their user base — imperfect protection against sophisticated targeted attacks but effective against mass-scale threats that affect far more users.

For users who are not targeted by nation-state APT actors with access to SS7 infrastructure or carrier-level intercept — which is the overwhelming majority of consumers — SMS 2FA provides meaningful, measurable security improvement over passwords alone.


## 3. Why People Believe This

**Compression of a qualified advisory into a universal imperative.** The most claim-specific mechanism producing belief in the strong version is what might be called directive flattening: the transformation of a contextually scoped recommendation into a universal command. The original advisory addressed a specific threat actor, a specific victim population, and a specific threat model (nation-state intercept capability). Journalism reporting on the advisory, particularly in technology media, condensed this into headline language — "stop using SMS 2FA" — that stripped the qualifying context. Readers who encountered the headline without reading the full advisory absorbed the unqualified directive. The problem is structural: security advisory language is inherently contextual, but headline language is inherently absolute, and the translation between them systematically removes the scope conditions that made the original claim accurate.

**Availability heuristic primed by a salient intrusion.** The Salt Typhoon intrusion was extensively covered in major media and provided a vivid, specific, named example of SMS interception in practice. When an available concrete example of a risk exists, the risk is typically judged as more prevalent and serious than it actually is for any specific individual — a well-documented manifestation of the availability heuristic described by Tversky and Kahneman (1973, *Cognitive Psychology*, vol. 5, pages 207–232). The existence of a dramatic operational example of SMS interception by Chinese state hackers made the threat feel immediately applicable to ordinary users' bank accounts and email logins, even though the attack specifically targeted people of interest to Chinese intelligence — a tiny and distinguishable population.

**Techno-precautionary over-correction.** Security advice tends to be received with a particular asymmetric interpretation: concerns about existing practices are alarming, while recommendations to do something different are often not immediately actionable. The result is that users who absorb the message that SMS 2FA is unsafe will sometimes disable it without implementing a stronger alternative — producing a net security regression from the advisory. This over-correction is a predictable consequence of communicating a contextually qualified security recommendation to a general audience for which the qualification is largely invisible.


## 4. Verdict

**Distorted but grounded — a real and important advisory has been overstated and decontextualised.** The FBI and associated agencies did issue advisories in late 2024 connecting to vulnerabilities in SMS communications following the documented Salt Typhoon intrusion into US carrier infrastructure. The advisory explicitly recommended that highly targeted individuals — people with particular exposure to nation-state intelligence interest — use end-to-end encrypted communications and hardware-based multi-factor authentication rather than SMS-dependent alternatives. This is real, official guidance with solid technical justification.

The popular claim that "the FBI warned people to stop using two-factor authentication via SMS" overstates the advisory in two critical ways. First, it universalises a recommendation that was specifically directed at high-value targets of nation-state actors, not the general public. Second, it erases the comparative context: neither the FBI, CISA, nor any authoritative security source has recommended replacing SMS 2FA with nothing. The standing consensus of US federal cybersecurity guidance is that any multi-factor authentication is substantially better than none, and that users who cannot or will not implement hardware MFA or authenticator apps are better served by continuing to use SMS 2FA than by disabling the second factor entirely.

The correct practical takeaway is: SMS 2FA has real vulnerabilities that matter most to high-value targets of sophisticated adversaries; hardware security keys and authenticator apps are more secure alternatives; for most users in most situations, SMS 2FA is still well worth using; if you are a government official, political operative, or journalist facing nation-state targeting, upgrade to stronger authentication methods.


## 5. The Wider Picture

The episode illustrates a persistent structural problem in cybersecurity communication to general audiences: the mismatch between the threat model of security professionals and the threat model of ordinary users. Security researchers and practitioners correctly identify and communicate real vulnerabilities — SS7, SIM swapping, carrier-level intercept — because those vulnerabilities are consequential in specific high-stakes threat environments. But communication that is calibrated to nation-state threat actors resonates very differently with a general audience that should be thinking about credential stuffing attacks and mass-scale phishing, which are the threats that actually affect millions of consumers annually.

This mismatch has been noted in the academic security literature. Herley (2009, *New Security Paradigms Workshop*) argued systematically that most security advice given to users is not calibrated to actual user threat models, and that advice appropriate for high-value targets is counterproductive when applied to ordinary users because it imposes real costs while providing negligible protection against the actual threat distribution. The SMS 2FA episode is a case study in this dynamic: advice correctly calibrated to the threat model of US government officials communicating over carrier networks targeted by Chinese intelligence became decontextualised advice urging millions of ordinary consumers to weaken their account security by removing authentication factors.

The multi-factor authentication landscape has evolved considerably. FIDO2/WebAuthn hardware security keys — produced by vendors including YubiKey (Yubico) and Titan (Google) — provide phishing-resistant authentication that is cryptographically robust against network-level attacks and cannot be socially engineered in the manner of SMS codes. TOTP authenticator applications (Google Authenticator, Authy, 1Password TOTP, and similar) are intermediate: more resistant than SMS because codes are generated locally and never transmitted over the same channel as account credentials, but potentially vulnerable to real-time phishing attacks that can relay codes to attackers during the narrow window of their validity. The security hierarchy, broadly: hardware keys > authenticator apps > SMS > no 2FA, with each level providing substantially better security than nothing.

The National Institute of Standards and Technology (NIST) addressed SMS-based out-of-band authentication in its Digital Identity Guidelines (SP 800-63B, first published 2017 with subsequent revisions). NIST's 2017 guidance explicitly deprecating SMS out-of-band authentication was widely — and somewhat inaccurately — reported as banning or condemning SMS 2FA at the time. The NIST guidelines deprecated the use of public switched telephone network authentication for certain assurance levels in government-facing applications, not as a blanket consumer recommendation. Subsequent NIST revisions have moderated earlier language while maintaining the preference for phishing-resistant authentication. This pattern — qualified government guidance being reported as a universal prohibition, creating confusion about whether 2FA is worth doing at all — has recurred multiple times over the past decade.


## 6. How Fact-Checkers Handle It

This claim has not been formally adjudicated by dedicated fact-check organisations as of this writing. The claim received significant news coverage in late 2024 that was itself partly responsible for the distorted version, making the corrective fact-check unusual in that the correction would need to address not only a viral social media claim but also the original news coverage that helped generate it.

For fact-checkers and media literacy practitioners, the most productive approach to this claim involves three steps. First, locate and read the primary source material — the actual FBI/CISA advisory language — and compare it to how the claim is being stated in secondary sources. The gap between "highly targeted individuals should use end-to-end encrypted communications and hardware MFA" and "stop using SMS 2FA" is visible immediately on comparison. Second, consult the standing guidance of the relevant agencies, which provides the comparative context missing from the specific advisory: both CISA's "More Than a Password" guidance and NIST SP 800-63B affirm that multi-factor authentication is a substantial security improvement over single-factor authentication at any implementation quality. Third, note the target population specification: the advisory is not applicable to everyone in the same way.

The broader media literacy lesson is that security advisories always carry implicit threat models, and translating those advisories into practical action requires understanding the threat model, not just the directive. "Avoid behaviour X because it exposes you to attack class Y by adversary Z at impact level W against target population V" is the full advisory structure; journalistic compression into "avoid behaviour X" drops four of five components. The dropped components are precisely the ones needed to determine whether the advice is applicable to any given person's situation.

Digital security is an area where the stakes of miscommunication are particularly high: bad practice leaves accounts vulnerable, but bad information about what constitutes good practice can also leave accounts vulnerable by inducing overcorrection. The goal of accurate security communication is to help users make choices that improve their actual security posture relative to the threats they actually face — which, for most people, means enabling any available second factor, and ideally upgrading from SMS to an authenticator app or hardware key when feasible, but explicitly not interpreting federal advisories about nation-state threat actors as grounds for disabling 2FA entirely.
