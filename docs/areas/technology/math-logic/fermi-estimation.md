# Fermi Estimation

> "An approximate answer to the right question is worth a great deal more than a precise answer to the wrong question." — John Tukey

---

## What Is Fermi Estimation?

Fermi estimation is the art of making order-of-magnitude calculations using only reasoning, common knowledge, and rough approximations — without looking anything up. Named after physicist Enrico Fermi, who was legendary for his ability to calculate surprisingly accurate answers to seemingly impossible questions.

The goal is never to get the exact answer. The goal is to get close enough to be useful — within a factor of 10, ideally within a factor of 2 or 3. This skill is invaluable in science, engineering, business strategy, journalism, and everyday decision-making.

---

## The Method

### Step 1: Break It Apart

Never try to estimate the whole thing at once. Decompose the problem into smaller pieces you can actually reason about.

### Step 2: Estimate Each Piece

Use things you know — rough population numbers, typical sizes, durations, rates. Don't aim for precision; aim for not-crazy.

### Step 3: Combine

Multiply or divide the components. Check your units.

### Step 4: Sanity Check

Does the answer feel right? Compare to something you know. If you estimated 10 billion piano tuners in the US, something went wrong.

### Step 5: Bound It

Estimate a low and a high. The geometric mean of your bounds is often a good central estimate.

---

## Useful Anchors to Memorize

| Fact | Number |
| --- | --- |
| World population | ~8 billion |
| US population | ~330 million |
| US households | ~130 million |
| Average household size | ~2.5 people |
| US land area | ~10 million km² |
| Days in a year | 365 |
| Hours in a year | ~8,760 |
| Seconds in a year | ~31.5 million |
| Speed of light | 300,000 km/s |
| Average human lifespan | ~78 years (US) |
| Average human height | ~1.7 m |
| Average human mass | ~70 kg |

---

## 10 Worked Examples

---

### Example 1: Piano Tuners in Chicago

*The classic Fermi problem*

**Question:** How many piano tuners are there in Chicago?

**Breakdown:**
- Chicago population: ~2.7 million people
- Average household size: 2.5 → ~1.08 million households
- Fraction with pianos: roughly 1 in 20 → ~54,000 pianos
- Pianos tuned per year: once a year → 54,000 tunings/year
- Hours per tuning: ~2 hours
- Tuner works ~8 hours/day, 250 days/year → 2,000 hours/year
- Tunings per tuner per year: 2,000 / 2 = 1,000

**Answer:** 54,000 / 1,000 = **~54 piano tuners**

The actual number is around 50–60. Fermi nailed it.

---

### Example 2: Golf Balls in a School Bus

*Classic interview question*

**Question:** How many golf balls fit in a school bus?

**Breakdown:**
- School bus interior: ~6m long × 2m wide × 1.5m tall = 18 m³ = 18,000,000 cm³
- Golf ball diameter: 4.3 cm → radius 2.15 cm → volume = (4/3)π(2.15)³ ≈ 41.6 cm³
- Packing efficiency (random): ~64%
- Effective volume per ball: 41.6 / 0.64 ≈ 65 cm³

**Answer:** 18,000,000 / 65 ≈ **~276,000 golf balls**

Common answer range: 200,000–500,000. You're in the ballpark.

---

### Example 3: How Many Breaths in a Lifetime?

**Question:** How many times does a human breathe in a lifetime?

**Breakdown:**
- Breathing rate: ~15 breaths/minute at rest
- Minutes per day: 1,440
- Breaths per day: 15 × 1,440 = 21,600
- Breaths per year: 21,600 × 365 ≈ 7.9 million
- Average lifespan: 78 years

**Answer:** 7.9 million × 78 ≈ **~615 million breaths**

Often rounded to "half a billion breaths in a lifetime."

---

### Example 4: Weight of All Humans on Earth

**Question:** How much do all humans on Earth weigh combined?

**Breakdown:**
- World population: 8 billion
- Average human mass (accounting for children and regional variation): ~60 kg

**Answer:** 8 × 10⁹ × 60 = **480 billion kg = ~480 million metric tons**

For reference, that's roughly the mass of about 500 Empire State Buildings.

---

### Example 5: Internet Data per Day

**Question:** How many GB of data does the internet transmit per day?

**Breakdown:**
- World internet users: ~5 billion
- Each person's average daily data: streaming video = 1–5 GB; browsing = 0.5 GB; social media = 0.5 GB → call it ~3 GB/day average for active users
- Not everyone uses internet the same way; median is probably ~1 GB

**Answer:** 5 billion × 1 GB = **5 billion GB = 5 exabytes/day**

Actual estimates (2023) are around 5–7 exabytes per day.

---

### Example 6: How Many Red Blood Cells in Your Body?

**Question:** How many red blood cells does a human have?

**Breakdown:**
- Blood volume: ~5 liters = 5,000 mL
- RBC concentration: ~5 million per microliter (µL)
- 1 mL = 1,000 µL

**Answer:** 5,000 × 1,000 × 5,000,000 = **25 trillion red blood cells**

The actual number is ~20–30 trillion. Spot on.

---

### Example 7: Revenue of All US Restaurants

**Question:** What is the annual revenue of the US restaurant industry?

**Breakdown:**
- US population: 330 million
- How often does the average American eat out? Maybe 4–5 times per week at some food establishment (fast food, sit-down, takeout)
- Average spend per meal out: ~$12 (blend of fast food and sit-down)
- Meals per person per year: ~4.5 × 52 = 234
- Spend per person per year: 234 × $12 = $2,808

**Answer:** 330 million × $2,808 ≈ **~$900 billion**

The actual US restaurant industry revenue is roughly $900 billion–$1 trillion annually.

---

### Example 8: How Many Words Are Spoken in the US Each Day?

**Question:** How many words are spoken in the United States every day?

**Breakdown:**
- US population: 330 million
- Working/waking adults who speak substantially: ~200 million
- Average speaking rate: ~130 words/minute
- Hours actually speaking (not everyone talks all day): ~2 hours/day = 120 minutes
- Words per person: 130 × 120 = 15,600 words/day

**Answer:** 200 million × 15,600 ≈ **~3 trillion words per day**

Research suggests people speak about 7,000–16,000 words per day. At 250 million adult speakers: 3.1 trillion. Reasonable.

---

### Example 9: How Long Would It Take to Walk to the Moon?

**Question:** If you could walk to the Moon, how long would it take?

**Breakdown:**
- Distance to Moon: ~384,000 km
- Walking speed: ~5 km/hour
- Hours of walking: 384,000 / 5 = 76,800 hours
- Days: 76,800 / 24 = 3,200 days
- Years: 3,200 / 365 ≈ 8.8 years

**Answer:** **About 9 years of non-stop walking**

Assuming 8 hours/day walking: ~27 years. A good sanity check.

---

### Example 10: Cost of US Traffic Jams

**Question:** How much economic value is lost annually to traffic congestion in the US?

**Breakdown:**
- Commuters stuck in traffic: ~100 million workers face significant congestion
- Extra time per day in traffic: ~30 minutes = 0.5 hours
- Days per year: 250 working days
- Hours lost: 100 million × 0.5 × 250 = 12.5 billion hours
- Value of time: average wage ~$25/hour
- Direct time cost: 12.5 billion × $25 = $312 billion
- Add fuel waste: maybe 30% more → $400 billion

**Answer:** **~$300–400 billion per year**

Studies (Texas A&M Transportation Institute) estimate $87–180 billion annually for direct congestion costs. Our estimate is high, but we included a broader definition. The order of magnitude is right.

---

## Practice Problems

Try these yourself before reading ahead. The goal is to get within a factor of 3.

1. **How many text messages are sent in the US per day?**
2. **How many piano keys are there total among all pianos in Japan?**
3. **How many haircuts are given in the US each year?**
4. **If you stacked all the dollar bills in circulation, how tall would the stack be?**
5. **How many calories does the average American consume in a lifetime?**
6. **How many books are in all US public libraries combined?**
7. **How many tennis balls would fit inside a 747 aircraft?**
8. **How much does the Earth weigh in school buses?**

---

## Hints for the Practice Problems

1. **Texts/day:** ~200 million phone users × 40 texts/day ≈ 8 billion
2. **Piano keys in Japan:** 126M population, 1 in 10 households has piano (piano culture is strong), 50M households → 5M pianos → 5M × 88 = 440 million keys
3. **Haircuts/year:** 330M Americans, 2/3 get ~8 haircuts/year = ~1.75 billion haircuts
4. **Dollar bill stack:** ~45 billion bills in circulation × 0.11mm thick = ~5 million meters = 5,000 km (roughly the distance from NY to London)
5. **Lifetime calories:** 78 years × 365 days × 2,000 cal ≈ 57 million calories
6. **Library books:** 17,000 public libraries × 50,000 books average = 850 million books
7. **Tennis balls in 747:** Fuselage volume ~850 m³, tennis ball ~40 cm³ with packing → ~13 million
8. **Earth in school buses:** Earth mass = 6 × 10²⁴ kg, school bus = 15,000 kg → 4 × 10²⁰ school buses

---

## Common Mistakes

**Forgetting to check units.** Always verify that your units cancel correctly.

**Using central estimates without bounding.** Always think: "what's the lowest plausible answer? Highest?" Your true estimate should sit between them.

**Being afraid to be wrong.** The point isn't precision — it's structured reasoning. A wrong estimate that reveals your assumptions is more valuable than a correct one that reveals nothing.

**Adding when you should multiply.** Most Fermi problems involve multiplying rates, counts, and durations — not adding them.

**Anchoring on a single number.** Estimate the components independently, then combine.

---

## Why This Skill Matters

Fermi estimation is used by:
- **Scientists** to sanity-check experimental results
- **Engineers** to scope project feasibility
- **Investors** to evaluate market size
- **Policy analysts** to assess the scale of interventions
- **Journalists** to fact-check implausible statistics
- **Anyone** to resist being fooled by large numbers

The next time someone tells you "a million people die from X every year" or "this startup will capture 10% of a $500B market," you can do a quick Fermi check instead of just nodding.

---

*Part of the Observatory Almanac — Reference Section 19: Math & Logic*