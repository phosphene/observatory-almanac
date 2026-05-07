# Digital Navigator

### 50 Lessons for Security, Privacy, and Savvy in the Digital World

---

## PART I: PASSWORD MANAGEMENT

### Lesson 1: The Password Manager Is Non-Negotiable

The average person has 100+ accounts. No human brain can remember 100 unique, strong passwords â so people reuse them, which means one breach cascades into twenty. The solution is a **password manager**: an encrypted vault that generates, stores, and autofills strong passwords. Top options: Bitwarden (open source, free tier is excellent), 1Password ($3/month), Dashlane. Choose one. Set it up today. This is the single highest-leverage security action you can take.

### Lesson 2: Setting Up Your Password Manager Correctly

Installation steps: Download the app and browser extension. Create a master password â this is the one password you must memorize. Make it a passphrase (4â5 random words: `coffee-lamp-river-boot-7`) â long, memorable, not guessable. Enable two-factor authentication on the vault itself. Import existing passwords from your browser. Then: start replacing weak/reused passwords with generated ones, starting with email, banking, and social accounts.

### Lesson 3: The Master Password Rule

Your password manager's master password must never be: your name, a word in any dictionary, a password you've used anywhere else, or fewer than 16 characters. Treat it like a combination to a physical safe. Write it on paper and store it somewhere secure (locked drawer, safety deposit box) â not digitally. If you forget it, you may lose everything in the vault permanently.

### Lesson 4: 2FA â The Types Explained

Two-factor authentication (2FA) adds a second verification step after your password. Types, ranked by security: **Hardware key** (YubiKey â best, nearly phishing-proof), **Authenticator app** (Google Authenticator, Authy â very good, generates time-based codes), **SMS/text code** (better than nothing, but vulnerable to SIM-swap attacks), **Email code** (weakest â if your email is compromised, this does nothing). Enable 2FA on every account that offers it. Prioritize: email, bank, password manager, social media.

### Lesson 5: What To Do After a Password Breach

Go to HaveIBeenPwned.com â enter your email to see if your credentials appear in known data dumps. If they do: change the password on that account immediately, change it on any other account where you used the same password, check for suspicious activity, and enable 2FA if not already on. Sign up for breach notifications at HIBP so you're alerted automatically going forward.

---

## PART II: VPN BASICS

### Lesson 6: What a VPN Actually Does (And Doesn't Do)

A VPN (Virtual Private Network) encrypts your internet traffic and routes it through a server in a location you choose. This means: your ISP can't see what you're doing, public WiFi eavesdroppers can't intercept your traffic, and websites see the VPN server's IP, not yours. What it does **not** do: make you anonymous (your VPN provider can see your traffic), protect you from malware, or prevent tracking by cookies and fingerprinting.

### Lesson 7: When You Actually Need a VPN

**Use a VPN when:** on public WiFi (coffee shops, airports, hotels), accessing geo-restricted content, traveling to countries with heavy internet censorship, or wanting to prevent your ISP from selling your browsing data. **You probably don't need a VPN for:** general home browsing (HTTPS already encrypts most traffic), banking (banks use their own encryption), or to "be safe online" in a vague sense â a VPN doesn't protect against phishing or malware.

### Lesson 8: Choosing a VPN You Can Trust

The VPN provider sees all your traffic â so trust matters more than price. Avoid free VPNs (they monetize your data). Good paid options: Mullvad (pays with cash/crypto, no account required), ProtonVPN (Swiss-based, strong privacy record), ExpressVPN. Look for: audited no-logs policy, transparent ownership, published transparency reports, and no history of data sharing with governments.

---

## PART III: PHISHING DETECTION

### Lesson 9: The Phishing Red Flags Checklist

Before clicking any link or attachment in an email, scan for: **Urgency** ("Your account will be closed in 24 hours!"), **Mismatch** (display name says "Bank of America" but hovering the link shows a different domain), **Grammar/typos** (legitimate organizations proofread), **Suspicious sender** ([[email protected]](/cdn-cgi/l/email-protection) vs. @amazon.com), **Unexpected attachment** (invoice you didn't request, DHL package you didn't order), **Requests for login credentials or payment via email** (banks and legitimate services never do this).

### Lesson 10: How to Verify a Suspicious Link

Hover over any link before clicking â the actual URL displays in your browser's status bar. Check the domain carefully: `paypal-secure-login.com` is not PayPal; `signin.paypal.com` is. Use a link scanner: VirusTotal.com lets you paste a URL and checks it against 70+ security engines. When in doubt, don't click â navigate directly to the website by typing it in your browser.

### Lesson 11: Spear Phishing â The Targeted Attack

Generic phishing casts wide nets; **spear phishing** is personalized. Attackers research your name, employer, colleagues, and recent activity (from LinkedIn and social media) to craft convincing messages: "Hi [Name] â I'm following up on the contract we discussed at [Conference]. Please review the attached NDA." These are nearly impossible to spot on surface scan. Default rule: **any unexpected attachment or link requires verification through a separate channel** (call the sender, don't reply to the email).

### Lesson 12: What To Do If You Clicked Something Suspicious

Act fast: disconnect from WiFi immediately, run a malware scan (Malwarebytes free version), change the password on any account you accessed after clicking, check for unauthorized logins in account activity, and notify your IT department if on a work device. Don't panic â clicking a link alone often does little harm; entering credentials on a fake site is where the real damage happens.

---

## PART IV: SOCIAL MEDIA PRIVACY

### Lesson 13: Facebook Privacy Settings Audit

Go to: Settings & Privacy â Privacy Checkup. Key settings to change: **Who can see your posts?** â Friends (not Public). **Who can find you by phone number/email?** â Friends or Nobody. **Off-Facebook Activity** â Clear history and disconnect data sharing. **Face recognition** â Off. **Ad preferences** â Review and restrict. Do this audit annually; Facebook resets settings after platform updates.

### Lesson 14: Instagram Privacy Essentials

Switch to Private account (Settings â Privacy â Private Account). Review â Accounts that follow you and remove unfamiliar ones. **Story controls**: remove specific followers from seeing stories. **Mention controls**: set to "Only people you follow." Disable **Activity Status**. Review **Third-party app access** â revoke anything you no longer use. The photos you post contain EXIF metadata â strip it before posting (iOS strips automatically; Android may not).

### Lesson 15: LinkedIn Privacy â The Professional Risk

LinkedIn is public by default and data-harvested aggressively. Key settings: **Profile visibility** â visible to connections, not public, for home address or phone. **Who can see your connections** â Only you (prevents competitors from mapping your network). **Profile viewing options** â Use anonymous mode when researching competitors. **Data export** â Download your data annually to know what LinkedIn has. Be aware: your LinkedIn profile is a goldmine for social engineers.

### Lesson 16: Twitter/X and Mastodon â Public by Default

Everything on public social media is indexed, archived, and potentially permanent. **Assume any tweet, post, or comment may be screenshot and shared out of context.** Review your post history annually â tools like Semiphemeral can auto-delete old tweets on a schedule. Enable login verification. Review connected apps regularly and revoke unused ones.

---

## PART V: DATA BACKUP

### Lesson 17: The 3-2-1 Backup Rule

The gold standard: **3** copies of your data, on **2** different media types, with **1** copy offsite. Example: Original (your computer) + external hard drive (different media) + cloud backup (offsite). This protects against: hardware failure, accidental deletion, fire/flood, and ransomware. A backup that hasn't been tested isn't a backup â restore a file from it annually to verify it works.

### Lesson 18: Backup Tools That Actually Work

**For cloud backup:** Backblaze ($9/month, unlimited computer backup, excellent) or Google One / iCloud (easier but more expensive per GB). **For local backup:** Time Machine (Mac, built-in) or File History (Windows, built-in) to an external drive. **For critical documents:** also store in Dropbox, Google Drive, or iCloud â free tiers cover most needs. **For photos:** Google Photos (free with compression) or iCloud Photos.

### Lesson 19: What Should Be Backed Up (And What's Irreplaceable)

Irreplaceable files requiring immediate backup: family photos and videos, personal documents (ID scans, financial records, legal documents), creative work (writing, music, art), anything that would take significant time to recreate. Apps can be reinstalled; your grandmother's digitized photos cannot be recovered. **Back up by value, not by volume.**

### Lesson 20: Ransomware-Proofing Your Backup

Ransomware encrypts your files and demands payment to restore them. It can spread to connected drives and cloud sync. Defense: Keep one backup **not continuously connected** to your computer (disconnect the external drive between backups). For cloud: enable versioning (Google Drive, Dropbox, OneDrive all support this) so you can restore pre-encryption versions. Air-gapped backups are immune to ransomware.

---

## PART VI: IDENTITY THEFT RESPONSE

### Lesson 21: The Identity Theft Response Plan

If your identity is stolen: **Step 1:** Place a fraud alert with one of the three credit bureaus (Equifax, Experian, TransUnion) â they're required to notify the others. **Step 2:** Request your free credit reports (AnnualCreditReport.com) and identify fraudulent accounts. **Step 3:** File an identity theft report at IdentityTheft.gov (FTC) â this gives you legal protections. **Step 4:** File a police report if creditors require one. **Step 5:** Dispute fraudulent accounts with creditors in writing, certified mail. **Step 6:** Consider a credit freeze (stronger than a fraud alert).

### Lesson 22: Credit Freeze â The Most Underused Protection

A credit freeze (also called a security freeze) prevents anyone from opening new credit in your name â including you. It's free at all three bureaus and can be temporarily lifted when you need new credit. This is the strongest protection against identity theft-driven credit fraud. There is no good reason not to have one if you're not actively applying for credit. Freeze: Equifax.com, Experian.com, TransUnion.com.

---

## PART VII: SMART ONLINE SHOPPING

### Lesson 23: Price Tracking Tools

Never buy anything at full price without checking: **CamelCamelCamel** (Amazon price history â shows whether the "sale" is actually a discount), **Honey** or **Capital One Shopping** (browser extensions that auto-apply coupon codes), **Keepa** (Amazon price tracker with alerts), **Google Shopping** (comparison across retailers). Set price drop alerts on items you want but aren't urgent. Most "deals" on Prime Day and Black Friday aren't deals against the 90-day price history.

### Lesson 24: Return Policy Mastery

Read the return policy before you buy, not after. Know: the return window (30, 60, 90 days?), whether returns are free or you pay shipping, whether a restocking fee applies, and whether the merchant accepts returns of opened items. Keep all packaging until you're certain you're keeping the item. For big-ticket purchases: use a credit card that extends return windows (Citi and Chase offer this). For electronics: the manufacturer warranty may supersede the retailer's return window.

### Lesson 25: Safe Online Checkout Practices

Before entering payment info: check for HTTPS (padlock icon) in the browser bar. Look for recognizable payment processors (Stripe, PayPal, Square) rather than custom forms. Use a virtual card number for one-time purchases (Privacy.com generates disposable card numbers linked to your real account). Never save your payment info on retailer websites you use rarely. For international sites: check reviews and use PayPal for purchase protection.

---

## PART VIII: DIGITAL ESTATE PLANNING

### Lesson 26: Password Vault Inheritance

When you die, your survivors may not be able to access your accounts. Solution: Create an emergency access document that includes your password manager master password and instructions for accessing the vault. Store it in a sealed envelope with your will or in a safety deposit box. Bitwarden and 1Password both have emergency access features that allow a trusted contact to request access after a waiting period (48â72 hours). Set this up.

### Lesson 27: Social Media Memorialization

Major platforms handle deceased users differently: **Facebook** allows memorialization (account stays up with "Remembering" label, no new logins) or deletion â designate a legacy contact in Settings. **Instagram** offers memorialization or removal â submit a request with proof of death. **Google** has an Inactive Account Manager that can transfer data or delete your account after a set period of inactivity. **Apple** has a Digital Legacy program for designating legacy contacts. Set these up in your accounts now; don't leave it for survivors to figure out.

### Lesson 28: Digital Asset Inventory

Make a document listing all accounts that matter: email addresses, banking/investment, subscription services with recurring charges, domain names, digital purchases (iTunes, Steam, Kindle), cryptocurrency, and any income-generating digital assets. This isn't just about death â it's useful for your own organization and for anyone helping you in an emergency. Store it securely with your estate documents.

---

## PART IX: SCAM IDENTIFICATION

### Lesson 29: Romance Scam Red Flags

Romance scams extracted $1.3 billion from victims in a single recent year. Red flags: **Never meet in person** despite extended online relationship, always have a reason (military deployment, overseas job, family emergency), **quickly move to private messaging** away from dating platform, **unusually attractive profile photos** (do a reverse image search with Google or TinEye), ask for money for emergencies, travel costs, or investment opportunities. Rule: Anyone who asks for money before you've met in person is a scam. No exceptions.

### Lesson 30: Investment Scam Anatomy

"Guaranteed returns," "risk-free," and "my cousin made $50K last month" are automatic red flags. Pig butchering scams: build a relationship over weeks/months, introduce a "investment platform," show fake profits, then disappear with your deposit when you try to withdraw. Crypto scams follow the same playbook. Rule: **Legitimate investments can lose money. Anyone guaranteeing returns is lying.** Verify any investment platform with your country's securities regulator (SEC.gov in the US).

### Lesson 31: Tech Support Scam Script

A pop-up or cold call claims your computer is infected, Microsoft has detected a virus, or your account is compromised. They ask you to download remote access software (TeamViewer, AnyDesk) or call a number. **No tech company proactively calls you about your computer.** Microsoft, Apple, and Google do not call you. Do not call numbers in browser pop-ups. If you're uncertain: call the company directly using the number from their official website. Close the browser tab; you're fine.

### Lesson 32: Employment Scam Warning Signs

Legitimate employers don't: offer jobs without interviews, ask for payment to process your application, ask for your bank account "to set up direct deposit" before you've started, send you a check to deposit and wire back a portion, or communicate exclusively through WhatsApp or Telegram with no company email domain. These are among the most sophisticated scams â they target job seekers who are already financially stressed. Verify every employer offer against the company's official website and LinkedIn presence.

---

## PART X: EMAIL SECURITY

### Lesson 33: Securing Your Email Account

Your email is the master key â it's used to reset every other password. Treat it accordingly: **Use a strong, unique password** (not used anywhere else). **Enable 2FA** (authenticator app, not SMS). **Use a separate email for high-security accounts** (banking, investment) that you don't share publicly. Consider **ProtonMail or Tutanota** for end-to-end encrypted email when privacy is paramount. Review **third-party app access** â revoke anything you no longer use.

### Lesson 34: Email Filters as Security Tools

Set up filters to automatically flag or quarantine: emails from senders outside your contacts that contain attachments, anything with "urgent" in the subject from an unknown sender, messages containing wire transfer or gift card language. Most email clients support filter rules. This doesn't replace judgment â it creates a speed bump that slows down the moment of click-and-regret.

---

## PART XI: PUBLIC WIFI SAFETY

### Lesson 35: The Public WiFi Threat Model

The primary threats on public WiFi: **Evil twin attacks** (a fake network with a convincing name, e.g., "Starbucks\_Free\_WiFi" run by an attacker), **Man-in-the-middle interception** (traffic intercepted between you and the router), **Malicious captive portals** (login pages that harvest credentials). The good news: HTTPS (which most major sites now use) encrypts your traffic even on public WiFi. The bad news: not all sites use HTTPS, and captive portals can strip it.

### Lesson 36: Public WiFi Rules of Thumb

On public WiFi: **Use a VPN** (encrypts all traffic before it leaves your device). **Avoid banking and financial transactions** (use your cellular connection for these). **Verify the exact network name** with staff before connecting. **Turn off auto-connect** for WiFi in your settings â your phone should not automatically join any available network. **Forget networks** you'll never use again (airport, hotel, coffee shop).

---

## PART XII: APP PERMISSIONS AUDIT

### Lesson 37: The App Permissions Audit Process

Every 6 months, review what your apps can access. On iPhone: Settings â Privacy & Security (review each category: Location, Contacts, Photos, Microphone, Camera, Health). On Android: Settings â Privacy â Permission Manager. For each app, ask: **Does this app actually need this permission to function?** A flashlight app that wants your contacts is suspicious. A navigation app that wants location only "while using" (not "always") is fine. Revoke anything that doesn't make functional sense.

### Lesson 38: Location Permission Strategy

Location is the most sensitive permission. **Always On** is rarely necessary â most apps work fine with "While Using." Review apps with "Always On" location access: is it a navigation or fitness tracking app? Legitimate. Is it a weather app or game? Revoke. Your location history is a detailed diary of your life â who you met, where you slept, what medical offices you visited. Treat it accordingly.

---

## PART XIII: BROWSER EXTENSION HYGIENE

### Lesson 39: Why Browser Extensions Are a Security Risk

Browser extensions run in your browser with access to every page you visit â including banking and email. A malicious extension can read passwords you type, see everything on your screen, and exfiltrate data silently. Extensions can also be acquired by malicious actors after the original developer sells them. The risk: an extension you installed 2 years ago may now be owned by someone with different intentions.

### Lesson 40: Extension Audit Protocol

Open your browser's extension manager (Chrome: chrome://extensions, Firefox: about:addons). For each extension: **Do I still use this?** If no, remove it. **Do I recognize this developer?** If no, research before keeping. **What permissions does it have?** "Access to all website data" is a broad grant â ensure the extension's function justifies it. Remove anything unused, unknown, or over-privileged. Less is more.

---

## PART XIV: ADVANCED DIGITAL HYGIENE

### Lesson 41: The Separate Email Strategy

Use three email addresses: **Public** (for signups, newsletters, anything you'd give a stranger â gets spam, you don't care), **Private** (for real relationships â friends, family, trusted contacts), **Secure** (for banking, investments, government, healthcare â never shared publicly, different from your primary). This limits the blast radius of any one breach and reduces spam to your primary inbox.

### Lesson 42: Device Encryption

If someone steals your laptop or phone, encryption prevents them from reading your files. **iPhone:** Encrypted by default when you set a passcode. **Android:** Most modern devices encrypt by default; verify in Settings â Security. **Mac:** FileVault (System Preferences â Security â FileVault â Turn On). **Windows:** BitLocker (search "BitLocker" in Start menu; Pro and Enterprise editions). Enable disk encryption on every device that holds personal data.

### Lesson 43: The Software Update Habit

Most malware exploits known vulnerabilities â vulnerabilities that are already patched in the current software version. Keeping software updated is a primary defense. Enable automatic updates for: your operating system, your browser, your phone's apps. Yes, updates sometimes break things. That tradeoff overwhelmingly favors updating. A device running two-year-old software is a target.

### Lesson 44: Secure Messaging Apps

For sensitive conversations: **Signal** is the gold standard (end-to-end encrypted, open source, audited, no metadata sold). **WhatsApp** uses Signal's encryption protocol but is owned by Meta and shares metadata. **iMessage** is end-to-end encrypted between Apple devices. **SMS** is not encrypted â treat it like a postcard. For highly sensitive matters: use Signal, enable disappearing messages, and be aware of who can see your screen.

### Lesson 45: Public Records and Data Broker Removal

Your name, address, phone number, and relatives are likely on dozens of data broker sites (Spokeo, WhitePages, Intelius, BeenVerified). These aggregate and sell personal information. Removal is tedious but possible: **Opt-out manually** from the top 20 data brokers (Privacy Bee and OptOutPrescreen.com have guides). Or use a service like DeleteMe ($129/year) to automate it. This won't remove you from government records but substantially reduces your data footprint.

### Lesson 46: The Minimal Digital Footprint Principle

Every account you create, every app you download, every service you sign up for is a potential breach vector. Ask before signing up: **Do I actually need this?** Could I use a throwaway email? Can I use a privacy-preserving login (Sign in with Apple creates unique relay email addresses for each app)? The smallest attack surface is the most secure one.

### Lesson 47: Recognizing Deepfakes and AI-Generated Content

Deepfake detection is increasingly difficult but some tells remain: **unnatural blinking**, **hair edges that blur or shimmer**, **mismatched lighting between face and background**, **hand distortion** (AI still struggles with hands), **audio sync slightly off**. For AI-generated images: look for text in the image (often garbled), reflections and symmetry errors, and background details that don't make sense. When in doubt: reverse image search, cross-reference the source, and assume high stakes content requires verification from multiple sources.

### Lesson 48: Digital Security After a Breakup or Divorce

Shared accounts, known passwords, and location sharing create vulnerabilities. Immediately after a serious relationship ends: change passwords on all accounts your partner knew, revoke shared access (streaming, banking, smart home), check for stalkerware (if your partner had physical access to your phone, they may have installed location tracking apps â look for unfamiliar apps, battery drain, data usage spikes), and review who has your Apple ID or Google account recovery access.

### Lesson 49: Child Safety Online Basics

For children using devices: use **parental controls** built into iOS Screen Time and Android Family Link. Set **search filtering** (SafeSearch in Google and Bing). Enable **privacy settings** on any games or platforms they use (assume everything is public by default). Have ongoing conversations about not sharing personal information, not talking to strangers, and coming to you if something online makes them uncomfortable. Technology controls are a layer, not a substitute for education.

### Lesson 50: Your Digital Hygiene Maintenance Schedule

**Monthly:** Check HaveIBeenPwned for your emails. Review active sessions on major accounts. Check for unfamiliar charges on cards. **Quarterly:** App permissions audit. Browser extension audit. Check credit report (rotate among the three bureaus). **Annually:** Update beneficiaries and emergency contacts on accounts. Review digital estate documents. Full password audit â any reused passwords? Any very old ones? Test your backup restoration. This takes 4 hours a year and prevents years of headaches.

---

*The Observatory Almanac | Digital Navigator | 50 Lessons*