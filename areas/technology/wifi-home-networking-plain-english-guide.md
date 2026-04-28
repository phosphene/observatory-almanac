---
title: "WiFi & Home Networking — Plain English Guide"
area: technology
type: almanac
source: Observatory Almanac
source_path: docs/22-digital-life/wifi-networking.md
license: MIT
updated: 2026-04-28
summary: >
  WiFi is one of those things that works invisibly when it's working and completely dominates your day when it isn't. This guide explains what's actually going on, how to improve it, and how to fix the most common problems — without needing a degree in networking.
tags:
  - technology
  - digital
  - practical
---

# WiFi & Home Networking — Plain English Guide

WiFi is one of those things that works invisibly when it's working and completely dominates your day when it isn't. This guide explains what's actually going on, how to improve it, and how to fix the most common problems — without needing a degree in networking.

---

## WiFi Basics: What's Actually Happening

### Modem, Router, and Gateway

Three words you'll hear often. Here's what they mean:

**Modem:** The box that connects your home to the internet. It talks to your ISP (Internet Service Provider — your cable company or phone company) and brings the internet signal into your house. It usually has a coaxial cable (like a TV cable) or a phone line going into it, and an ethernet port coming out.

**Router:** The box that takes the internet from the modem and shares it to all your devices — phones, laptops, TVs, and everything else. It also creates your WiFi network. It typically has several ethernet ports plus an antenna or two.

**Gateway:** One device that does both jobs — modem and router combined. This is what most ISPs provide when you sign up for service. When someone says "restart your router," they usually mean this box.

If you have two boxes, one is the modem and one is the router. If you have one box, it's a gateway. Either setup works.

**The chain:** Internet → ISP → cable/phone line → modem (or gateway) → router → WiFi → your devices

### 2.4 GHz vs. 5 GHz

Your router probably broadcasts two different WiFi signals. You'll see them in your device's WiFi list, often named something like "HomeNetwork" and "HomeNetwork_5G" — or identical names with different signals if your router is newer.

**2.4 GHz:**
- Longer range — reaches farther through walls and floors
- Slower top speed
- More interference from neighbors (more people use 2.4 GHz)
- Better for: smart home devices, things far from the router, older devices

**5 GHz:**
- Shorter range — doesn't penetrate walls as well
- Much faster speeds when you're nearby
- Less congested (fewer neighbors use it)
- Better for: video streaming, video calls, gaming — when you're in the same room or next room as the router

**Which should you use?** Connect your phone and laptop to 5 GHz whenever possible (closer proximity, faster). Connect smart plugs, thermostats, and devices in distant rooms to 2.4 GHz (better range, they don't need speed).

**What if they have the same name?** Newer routers with "band steering" automatically assign your device to the best band. If you notice a device always connecting to 2.4 GHz when you're close to the router, you can split the bands by giving them different names in your router settings.

### WiFi 5, 6, and 7: Do You Need to Care?

These are WiFi generations — the technical standards that determine speed and efficiency.

**WiFi 5 (802.11ac):** Current in most homes. Fast enough for streaming 4K video and video calls without issue. Max real-world speed around 300-500 Mbps.

**WiFi 6 (802.11ax):** Newer, faster, and handles more devices simultaneously without slowdown. Worth getting if you're buying a new router. Most current phones and laptops support it.

**WiFi 7 (802.11be):** Very new, very fast. Overkill for most homes today. The equipment is expensive. Give it a few years.

**Bottom line:** If your router is over 5 years old and you're frustrated with WiFi, upgrading to a WiFi 6 router will likely help — especially if you have 10+ connected devices. If your router is newer, you almost certainly don't need to upgrade.

### Finding Your WiFi Name and Password

**On the router/gateway itself:** Look for a sticker on the bottom or back of the device. It usually shows "SSID" (that's the network name), "Network Key," "WiFi Password," or "WPA2 Key."

**On an iPhone already connected:** Settings → WiFi → tap the connected network name → look for password (iOS 16+) or tap the info icon. In iOS 16 and later, there's a visible password field you can tap to reveal.

**On an Android already connected:** Settings → WiFi → tap the connected network → "Share" button generates a QR code. Or Settings → WiFi → tap the network → you may see the password directly on some Android versions.

**On a Windows computer already connected:** Control Panel → Network and Sharing Center → click your WiFi network name → Wireless Properties → Security tab → check "Show Characters" next to the password field.

**On a Mac:** Use Keychain Access (search for it in Spotlight) → search for your network name → double-click → check "Show password" → enter your Mac login password.

---

## Setting Up and Improving Your WiFi

### Optimal Router Placement

Router placement is the single biggest factor in WiFi quality that most people never think about.

**Ideal placement:**
- **Central in your home** — WiFi radiates outward in all directions; a router in the corner only covers three directions effectively
- **Elevated** — On a shelf or desk, not on the floor. Signals travel horizontally and slightly downward.
- **Open space** — Not inside a cabinet, closet, or entertainment center. Every physical barrier degrades the signal.

**Avoid:**
- Next to or behind a microwave (microwaves emit 2.4 GHz radiation and cause interference)
- Near cordless phone base stations
- Surrounded by metal objects
- In the basement if you mainly use the upstairs

**The garage test:** If your WiFi works fine everywhere but the back bedroom or the back yard, you have a range problem — not a speed problem. Move the router or add an extender.

### Changing Your WiFi Name and Password

You should do this when you first set up a router. Using the default network name ("NETGEAR_5G" or "Linksys00437") broadcasts that you're using default settings, which can hint at easier-to-guess admin passwords.

1. Type your router's IP address into a web browser. Common addresses:
   - **192.168.1.1** — Try this first
   - **192.168.0.1** — Second most common
   - **10.0.0.1** — Used by Apple and some others
   The correct address is sometimes printed on the router sticker.
2. Log in with the admin credentials (also on the sticker — default is often "admin" / "admin" or "admin" / "password")
3. Look for "Wireless Settings" or "WiFi Settings"
4. Change the SSID (network name) to something you'll recognize — avoid using your address or full name
5. Change the password to something strong: 12+ characters, mix of letters and numbers
6. Save/Apply settings

After this, all your devices will disconnect and need to reconnect with the new password.

### WiFi Extenders vs. Mesh Systems

If your WiFi doesn't reach part of your home, you have two main options:

**WiFi Extender (Range Extender):**
- A single additional device plugged into a wall outlet
- Repeats your existing WiFi signal
- Cheap ($30-80)
- Downside: Creates a separate network. Your devices may not automatically switch between the main router and the extender as you move around, causing you to manually reconnect. Also, the extender has half the bandwidth because it's receiving and transmitting on the same radio.
- Best for: Small dead zones, budget-conscious, simple needs

**Mesh WiFi System:**
- Multiple units (typically 2-3) placed throughout your home
- They communicate with each other and create a single seamless network
- Your devices automatically connect to whichever node is strongest as you walk around
- More expensive ($150-500 for the set)
- Examples: Eero, Google Nest WiFi, TP-Link Deco, Netgear Orbi
- Best for: Homes over 2,000 sq ft, multiple floors, many devices

**My recommendation:** If you're already frustrated and willing to spend $150, go straight to a mesh system. You'll spend the extender money anyway and then upgrade. Eero 6 is well-reviewed and widely available.

### Guest Network

Most modern routers let you create a second "guest" network alongside your main one.

**Why you want this:**
1. Give visitors WiFi without sharing your main network password — guests get internet access but can't see your computers and other devices
2. Put IoT (Internet of Things) devices on it: smart TVs, smart speakers, doorbells, thermostats. These devices often have poor security — keeping them on a separate network means a hacked thermostat can't reach your laptop.

**How to set it up:** Router admin page → look for "Guest Network" → enable it → give it a name and separate password.

### Connecting Devices That Struggle

**Smart TVs and streaming sticks:**
- Connect to 5 GHz if within 20 feet of the router; 2.4 GHz if farther
- Some smart TVs have poor WiFi antennas — if you can run an ethernet cable, that's faster and more reliable

**Printers:**
- Most struggle with 5 GHz — put them on 2.4 GHz
- During printer WiFi setup, make sure your phone or laptop is also on 2.4 GHz so they can find each other

**IoT devices (smart plugs, cameras, etc.):**
- Many only support 2.4 GHz. If your phone is on 5 GHz during setup, the device can't connect. Temporarily switch your phone to 2.4 GHz for setup, then switch back.

---

## Security

### Change the Default Router Admin Password

This is the one security step almost nobody does. The default admin credentials (used to log into the router's settings page) are publicly documented for every router model. Anyone who can reach your router's admin page can take over your network.

**Fix it:**
1. Log into your router admin page (see above — 192.168.1.1 or similar)
2. Find "Administration" or "Settings" → "Router Password" or "Admin Password"
3. Change it to something unique and strong — not your WiFi password
4. Save this password somewhere secure (password manager)

**Who can access the router admin page?** Only people on your network (connected via WiFi or cable). But that includes guests you gave your WiFi password to.

### WPA3 vs. WPA2

WPA is the encryption standard used to protect your WiFi. The version matters.

**WPA3:** The latest standard. Provides better protection against brute-force password guessing and protects traffic even if your password is weak.

**WPA2:** The previous standard. Still reasonably secure with a strong password.

**WPA / WEP:** Old standards. If your router still uses these (WPA or WEP), any tech-savvy person nearby can break into your network. Upgrade the router.

**How to check:** Router admin page → Wireless Settings → Security Mode. Set to WPA3 if available, WPA2-AES if not. Avoid "TKIP" — it's weaker.

### Disable WPS

WPS (WiFi Protected Setup) is a feature that lets you connect a device by pressing a button or entering an 8-digit PIN. The PIN method has a known security flaw that allows it to be cracked in hours.

**Fix:** Log into router admin → Wireless Settings → find WPS → Disable.

### Check What's Connected to Your Network

Want to see every device using your WiFi?

**In your router admin page:** Look for "Connected Devices," "DHCP Client List," or "Device List." You'll see IP addresses, MAC addresses (hardware IDs), and sometimes device names.

**What to do with this:**
- Identify every device (your phone, laptop, TV, smart speakers, etc.)
- Any device you can't identify — investigate. It might be a neighbor using your network, or it might be a smart home device you forgot about.

**Third-party app:** Fing (free for iOS and Android) scans your network and gives you a clear list of connected devices with names.

### Public WiFi Safety

Free WiFi at coffee shops, airports, and hotels is genuinely convenient and genuinely risky. Here's what actually matters:

**Real risks:**
- Anyone on the same network can attempt to intercept unencrypted traffic
- Rogue access points — fake networks named "Airport_Free_WiFi" designed to intercept your data
- The network operator can see which sites you visit

**Less scary than it sounds:**
- Most modern websites use HTTPS, which encrypts your data end-to-end. Your bank is fine.
- The actual threat is lower than it was 10 years ago because of HTTPS becoming standard.

**What not to do on public WiFi:**
- Don't enter passwords for accounts that don't use HTTPS
- Don't send sensitive documents or data through unencrypted apps
- Don't do anything you'd be uncomfortable with the café owner watching

**When to use a VPN:** If you regularly use public WiFi and want to be safe: a VPN encrypts all your traffic, even on unencrypted networks. See [Laptop Setup](laptop-setup.md) for VPN recommendations.

---

## Troubleshooting

### "Connected But No Internet" — The 5-Step Fix

This is the most common network complaint. You're connected to WiFi but nothing loads.

**Step 1: Restart your phone or device.** Sounds obvious, but network stacks get confused. 30 seconds fixes it a surprising amount of the time.

**Step 2: Check if it's just one device.** Try another phone or laptop. If they all have the same problem, it's your router or ISP. If only one device, it's that device.

**Step 3: Forget and reconnect to the network.** 
- iPhone: Settings → WiFi → tap the network → "Forget This Network" → reconnect
- Android: Settings → WiFi → tap and hold the network → Forget → reconnect
This refreshes your device's IP address.

**Step 4: Restart your router.** Unplug it from power. Wait 30 seconds (count to 30). Plug back in. Wait 2 minutes for it to fully boot.

**Step 5: Check if the internet is actually out.** Call or text someone on cellular data to ask. Or check your ISP's website using cellular data on your phone. If it's an outage, there's nothing you can do but wait.

If none of these work: Call your ISP. The issue may be on their end, or there may be a configuration problem that requires their support.

### Slow WiFi Diagnosis

**Step 1: Run a speed test.** Go to fast.com or speedtest.net on your device. Note the numbers.

**Step 2: Compare to what you're paying for.** Your internet plan has a stated speed (e.g., "200 Mbps"). You should get at least 80% of that on a device close to the router via ethernet.

**Step 3: Test wired.** Plug a laptop directly into the router with an ethernet cable. Run the speed test again. If wired is fast but WiFi is slow, the problem is your WiFi, not your internet connection.

**Step 4: Test close to the router.** Put your phone right next to the router and test. If it's much faster than in the room you normally use it, it's a range problem — see extenders and mesh systems above.

**Common causes of slow WiFi:**
- **Channel congestion:** If all your neighbors are on the same WiFi channel, you're competing for bandwidth. Router admin → Wireless Settings → Channel. Try setting it manually to channels 1, 6, or 11 (for 2.4 GHz). Apps like WiFi Analyzer (Android) show which channels are crowded.
- **Interference:** Microwaves, cordless phones, baby monitors. Move the router away from them.
- **Too many devices:** Streaming 4K on three TVs while 15 other devices are active will slow things down. WiFi 6 routers handle this better.
- **Old router:** Routers over 5 years old may simply not keep up with modern speeds. ISPs also update their infrastructure, and an old router may be the bottleneck.

### Forgetting and Reconnecting to a Network

Sometimes a device gets "stuck" on wrong network settings or connects to the wrong network automatically. Forgetting and reconnecting fixes this.

**iPhone:** Settings → WiFi → tap the (i) next to the network → "Forget This Network" → confirm
**Android:** Settings → WiFi → tap and hold the network name → "Forget"
**Windows:** Click the WiFi icon in the taskbar → click the arrow next to the network → "Forget"
**Mac:** System Settings → WiFi → click the network → remove (minus button)

Then reconnect by selecting the network and re-entering the password.

### When to Restart Your Router vs. Call Your ISP

**Restart your router when:**
- Internet works but is slow or intermittent
- Devices can't connect or say "connected, no internet"
- It's been more than a few weeks since it was restarted (good habit to restart monthly)
- After a power outage

**Call your ISP when:**
- Restarting doesn't help
- You see lights on the router that aren't normally there (solid red, blinking pattern)
- The internet has been out for hours
- You're getting the right speeds at the router but your service provider is delivering less than your plan promises

**When calling your ISP:** Note the light status on your router (write down which lights are on/off/blinking). Have your account number ready. Ask specifically: "Is there an outage in my area?" — this tells you immediately if it's their problem or yours.

---

*See also: [Laptop Setup](laptop-setup.md) | [Smartphone Setup](smartphone-setup.md) | [Streaming & Entertainment](streaming-entertainment.md)*
