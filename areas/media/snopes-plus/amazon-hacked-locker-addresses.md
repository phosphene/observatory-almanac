---
title: "'Amazon Got Hacked': Viral Rumor Says Criminals Added Fake Locker Addresses"
slug: amazon-hacked-locker-addresses
snopes_url: https://www.snopes.com/fact-check/amazon-hacked-locker-addresses/
snopes_verdict: Unverified (reported as news; no formal Snopes verdict rating applied)
snopes_author: Jordan Liles
published: 2026-07-20
updated: 2026-07-20
earc: R
epistemic_gap: high
tags:
  - Amazon
  - package theft
  - address fraud
  - social media rumor
  - copypasta
  - cybersecurity
  - account security
area: media
section: snopes-plus
---

# 'Amazon Got Hacked': Viral Rumor Says Criminals Added Fake Locker Addresses

## §1 — Claim & Verdict

In early December 2023, a viral Facebook rumor circulated asserting that "Amazon got hacked" and that criminals had added fraudulent Amazon Locker, Amazon Hub Locker, Amazon Fresh, or Amazon Counter pickup addresses to innocent users' accounts. The posts encouraged recipients to check their saved addresses, look for unrecognized orders, and verify their payment methods. The text spread rapidly as a copy-pasted warning, becoming one of numerous examples of the recurring genre of social-media security panic posts.

Senior Reporter Jordan Liles at Snopes investigated the claim. The case was unusual in that Amazon itself provided two successive, somewhat contradictory statements: an initial denial of any security breach and a later acknowledgement that pickup addresses had been added to "a small number" of customer accounts "in error." This created a fact-checking situation that resists a simple True/False verdict. The article is filed under Snopes's News category rather than the Fact Check category, reflecting the fluid and multi-faceted nature of the underlying events at the time of publication. The story illustrates the **structural tensions in platform-scale security communications**, the epidemiology of viral rumor amplification, and the meaningful differences between an "error," a "hack," and fraud.

This entry provides a detailed analysis of the anatomy of the Amazon locker rumor, reviews what is known about the technical events, examines Amazon's dual statements, charts the social-media spread pattern, and assesses what verified conclusions can be drawn.

---

## §2 — Mechanism: What Did Users Actually Observe?

The core observable phenomenon reported by users was straightforward: Amazon account holders checking their saved addresses found one or more addresses labeled as Amazon Locker or related pickup services — addresses they had not added themselves. Multiple users posted screenshots showing the unexpected addresses on Facebook and Reddit.

Amazon Locker is a network of self-service kiosks located in thousands of retail and convenience locations — Whole Foods stores, 7-Elevens, Rite Aids, and others — that allow customers to have packages delivered to a secure locker and retrieved using a one-time six-digit code sent by Amazon. Amazon Hub Locker, Amazon Counter, and Amazon Fresh pickup locations operate on similar principles. The premise of the viral rumor was that **criminals had added fraudulent addresses resembling these legitimate pickup types** so that packages ordered on a victim's account and charged to the victim's payment method could be intercepted and collected by the criminals before the legitimate account holder discovered the unauthorized orders.

This is, in principle, a plausible fraud vector. So-called "ship-to fraudster" schemes are a documented form of account takeover fraud: a criminal who has obtained account credentials adds a delivery address they control, then places orders using saved payment methods. The criminal receives the goods while the chargebacks and discovery process unfolds later. Such schemes are categorized under the broader label of **e-commerce account takeover (ATO) fraud**, which the Association of Certified Fraud Examiners estimates cost organizations billions annually (ACFE, 2022, *Report to the Nations on Occupational Fraud and Abuse*, acfe.com).

However, Snopes identified a critical evidential gap in the viral claims: **none of the users who reported finding unexpected addresses also reported finding unauthorized orders on their accounts**. The framework of the feared fraud — unauthorized packages shipped to fraudster-controlled locker addresses at the victim's expense — would producing visible fraudulent orders. The absence of such reports in the wild strongly suggested that whatever was adding addresses to accounts was not concurrently executing the second stage of the fraud scheme.

---

## §3 — Epistemic Novelty: Amazon's Two Statements and the Semantics of "Error" vs. "Hack"

The most epistemically interesting element of this story is the contrast between Amazon's two official statements, issued one day apart.

**Statement 1 (December 7, 2023):** "We have no evidence of a security event at Amazon and our systems remain secure."

**Statement 2 (December 8, 2023):** "This isn't a data security matter and our systems are secure. Amazon pickup locations were added to a small number of customer accounts in error, and we are working to fix the issue. We apologize for any inconvenience this may have caused, and customers with questions about their account are welcome to contact customer service."

The second statement acknowledges what the first implicitly denied — that addresses had been added to accounts by some mechanism other than the account holders themselves. The word "error" in the second statement is doing significant semantic work. It could encompass at least three distinct explanatory models:

1. **Software bug in address management**: An internal software defect could cause the accounts of nearby or algorithmically grouped users to be populated with locker addresses from a recommendation engine or synchronization service that malfunctioned. No hack required; pure systems error.

2. **Data migration error**: In scenarios involving database migrations, account merges, or A/B testing, addresses can be incorrectly assigned to accounts. Again, no external actor required.

3. **Third-party API misconfiguration**: Amazon integrates with numerous third-party logistics partners. A partner's API call providing address data could have been incorrectly scoped, causing locker-address data to be written to the wrong accounts.

What Amazon explicitly did not claim: that the addresses were added by criminals exploiting compromised credentials. This is the operative distinction between a "hack" (as the viral posts alleged) and an "error" (as Amazon ultimately characterized it). The viral rumor committed a significant inferential leap: seeing unexpected addresses and concluding criminal intent without evidence of the fraudulent downstream orders that the scheme would require.

The epistemic novelty for Truth Vault analysis lies in the governance dimension: Amazon issued a denial before issuing a correction, which is a common but epistemically problematic communication pattern in corporate security incidents. Organizations routinely issue initial denials ("no evidence of a security event") that later prove narrowly technically true but practically misleading. The second statement confirmed that something did happen — addresses were added to accounts — while declining to characterize what internal process caused it. This leaves a genuine information vacuum that the viral rumor was quick to fill with a conspiratorial narrative.

For researchers in organizational transparency and crisis communication, this case exemplifies a well-documented pattern: **the vacuum between corporate denial and corporate correction is the temporal window in which misinformation achieves maximal spread** (Sellnow, T.L. and Seeger, M.W., 2013, *Theorizing Crisis Communication*, Wiley-Blackwell). Had Amazon issued a clear "we are investigating unexpected address additions to a small number of accounts" statement on December 7, the viral rumor might have dissipated more quickly.

---

## §4 — The Anatomy of Viral Security Copypaste

Jordan Liles identifies the rumor as the latest entry in "the world of copied-and-pasted Facebook posts" — a specific genre of social media misinformation with a distinctive structure and natural history worth examining in detail.

Researchers studying viral health and security warnings on social media have documented consistent structural features of what is sometimes called the **copypasta rumor format** (Roozenbeek, J. and van der Linden, S., 2019, "Fake news game confers psychological resistance against online misinformation," *Palgrave Communications*, 5(1), 65). These features include:

- **Urgency framing**: The message creates a time-pressure sense ("PSA," "check immediately," "important").
- **First-person claim of personal victimhood**: "Amazon got hacked and a lot of people (including me)…" — the inclusion of apparent direct experience increases psychological credibility.
- **Vague but verifiable-sounding specificity**: Enough detail (specific address types, specific instructions) to seem credible without being verifiable by recipients.
- **Call to action and chain amplification**: "Double check… and check your bank accounts" encourages protective behavior and forward sharing.
- **Absence of source verification**: No link, no authoritative source, no documentation of the claimed events.

The Amazon locker rumor fit this template precisely. Its rapid spread — including reposting on official U.S. law enforcement Facebook pages in different contexts (see the NameDrop rumor; same period, similar mechanism) — illustrates how the institutional credibility of authorized sharers (police departments, community organizations) amplifies fundamentally unverified content.

A specific aspect of this particular rumor worth flagging is the **misidentification of legitimate addresses as fake ones**. Multiple users who shared screenshots of the "fraudulent" locker addresses that appeared on their accounts were, in fact, sharing screenshots of genuine Amazon Locker, Amazon Hub, and Amazon Counter addresses — real locations registered in Amazon's own system. This is a forensically verifiable claim: Snopes reports that checking the addresses in the screenshots against Amazon's own locker finder confirmed their legitimacy. Users were alarmed by addresses that were authentic. This adds a layer of irony: the viral rumor about fake addresses appears to have primarily surfaced real addresses that had been erroneously (by Amazon's own account) inserted into accounts.

---

## §5 — Security Hygiene and What Users Should Actually Do

Regardless of the specific technical cause of the December 2023 address insertions, the incident provides a useful prompt to examine what good account security hygiene actually looks like for e-commerce platforms.

Amazon does not appear in the list of platforms that have suffered large-scale credential breach events in the manner of Yahoo (2013–2014, 3 billion accounts; Verizon Communications, 2017) or LinkedIn (2012, 117 million credentials; LeakedSource, 2016). However, Amazon accounts are frequent targets for **credential stuffing attacks** — automated attempts to log in using username-password pairs compiled from unrelated data breaches at other sites (Thomas, K. et al., 2017, "Data Breaches, Phishing, or Malware? Understanding the Risks of Stolen Credentials," *Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security*, 1421–1434). Because many users reuse passwords across services, credentials stolen from a smaller breach can be used to access Amazon accounts.

The security countermeasures most relevant to the Amazon locker scenario are well-established:

1. **Two-step verification**: Amazon offers two-step verification via SMS, authenticator app, or hardware security key. Enabling this prevents credential-stuffing attacks from resulting in unauthorized logins even when credentials are compromised elsewhere.

2. **Saved address auditing**: Periodically reviewing saved addresses is genuinely useful security hygiene, not only for scenarios involving errors like the December 2023 incident but also for detecting actual unauthorized additions.

3. **Order history monitoring**: Checking for unrecognized orders and reviewing saved payment methods for unauthorized cards are baseline protective practices for any e-commerce account.

4. **Password uniqueness**: The use of unique passwords per service (most easily managed through a password manager) substantially reduces the impact of credential breaches at unrelated sites.

Amazon's own support documentation for two-step verification (Amazon Customer Service, "What Is Two-Step Verification?" https://www.amazon.com/gp/help/customer/display.html?nodeId=G3PWZPU52FKN7PW4) and password reset procedures are both publicly available and directly relevant here.

The actionable guidance embedded in the viral rumor — check addresses, check orders, check payment methods — is therefore actually sound security hygiene advice. The rumor's diagnosis (Amazon got hacked, criminals added addresses) was unverified and largely incorrect, but the remediation steps it suggested were genuinely useful. This is an important truth-vault distinction: **a rumor's behavioral recommendations can be sound even when its causal narrative is wrong**.

---

## §6 — Verdict Assessment, Evidence Classification, and Gaps

**EARC classification: R** (Reported — this is primarily a news/reporting case with an evolving corporate response, not a scientific or historical empirical claim susceptible to direct experimental verification).

**Snopes treatment:** Filed as a News article (not a standard Fact Check with a verdict rating), reflecting the ambiguous and evolving factual situation. The article does not label the viral claim "True," "False," or "Misleading" in the standard Snopes rating system, though the reporting clearly undermines the core "Amazon got hacked by criminals" framing.

**What is verified:**
- Amazon account holders did find unexpected addresses labeled as Amazon pickup locations in their accounts in early December 2023. (Confirmed by multiple user reports and Amazon's own second statement.)
- The addresses in user screenshots were mostly real, registered Amazon pickup locations. (Snopes verification of address legitimacy.)
- Amazon confirmed addresses had been "added in error" and that this was "not a data security matter." (Amazon spokesperson, December 8, 2023.)
- No users who reported unexpected addresses also reported unauthorized orders. (Snopes's observation from combing through reports.)

**What is unverified:**
- The precise technical mechanism by which Amazon pickup addresses were added to user accounts. Amazon declined to specify.
- Whether any accounts experienced actual fraud (unauthorized orders) in connection with the unexpected address additions.
- Whether the "error" was confined to the small number of accounts Amazon claimed or was broader.

**Epistemic gaps:**

1. **Technical transparency gap:** Amazon never publicly specified the software or data error that caused the address additions. Independent technical analysis is impossible without internal system access. The gap between "error" and "hack" remains unprovable from public evidence.

2. **Scope verification gap:** Amazon claimed "a small number" of affected accounts. No independent estimate of scope was produced. Independent security researchers did not publish technical analyses of the incident (no CVE record was filed; no breach notification was publicly reported).

3. **Follow-up gap:** Snopes had not, as of the article's publication, received a response from Amazon detailing the resolution. Whether the issue was fully resolved was not confirmed.

4. **Historical precedent gap:** The article would benefit from a structured comparison to known categories of Amazon account error incidents vs. actual Amazon security incidents, providing context for whether Amazon's "error" explanation is consistent with historical patterns.

**Bottom line:** The viral "Amazon got hacked" rumor significantly overstated and misdescribed an incident that Amazon later acknowledged was caused by an internal error rather than criminal exploitation. The core claim — that criminals added fraudulent addresses to enable package theft — is **unsubstantiated**: there is no evidence of unauthorized orders, and the addresses identified were real Amazon locations. Amazon's own second statement confirms an error occurred but does not confirm criminal activity. The recommended user behaviors embedded in the rumor (check addresses, verify orders) constitute valid security hygiene regardless of the rumor's accuracy.

---

### References

- Association of Certified Fraud Examiners (ACFE). (2022). *Report to the Nations on Occupational Fraud and Abuse*. acfe.com.
- Amazon Customer Service. "What Is Two-Step Verification?" https://www.amazon.com/gp/help/customer/display.html?nodeId=G3PWZPU52FKN7PW4.
- Roozenbeek, J. and van der Linden, S. (2019). Fake news game confers psychological resistance against online misinformation. *Palgrave Communications*, 5(1), 65.
- Sellnow, T.L. and Seeger, M.W. (2013). *Theorizing Crisis Communication*. Wiley-Blackwell.
- Thomas, K. et al. (2017). Data Breaches, Phishing, or Malware? Understanding the Risks of Stolen Credentials. In *Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security*, 1421–1434. ACM.
- US About Amazon. (2023, March 1). How to Use Amazon Locker, the Free and Convenient Way to Pick up Packages Securely Outside of Your Home. https://www.aboutamazon.com/news/operations/how-to-use-amazon-locker.
