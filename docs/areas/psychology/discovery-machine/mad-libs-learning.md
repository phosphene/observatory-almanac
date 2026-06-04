# The Discovery Machine

🔍 Discovery Machine — All Questionnaires

* [📋 Depression Screen (PHQ-9)](../clinical-validated/#take-the-phq-9-now)
* [📋 Anxiety Screen (GAD-7)](../clinical-validated/#take-the-gad-7-now)
* [🧠 Big Five Personality](../self-knowledge/#take-the-big-five-now)
* [💼 Career Type (RIASEC)](../vocational-personality/#holland-riasec)
* [💕 Attachment Style](../relationship-social/#attachment-style)
* [🗳️ Political Compass](../self-discovery-suite/#political-compass)
* [❤️ Relationship Health](../relationship-dynamics/#relationship-health)
* [🚨 Emergency Decision Tree](../body-survival/#emergency-decision-tree)
* [🛡️ Scam Checker](../consumer-legal/#scam-checker)
* [🐕 Is This Dog Friendly?](../animal-nature/#dog-friendly)
* [🏠 Home Safety Score](../home-environment/#home-safety)
* [👃 What's That Smell/Sound?](../sensory-diagnostics/#whats-that-smell)
* [🚧 Boundary Health Check](../relational-behavioral-deep/#boundary-health)
* [📝 Glossary Mad Libs Quiz](../mad-libs-learning/#glossary-quiz)

*Knowledge · Questionnaires · Interactive Tools*

## Mad Libs Learning Mode — Design Document & Content

> *"Tell me and I forget. Teach me and I remember. Involve me and I learn."*

---

## Overview

The Mad Libs Learning Mode is the Observatory Almanac's interactive comprehension layer. After reading any Almanac section, users may enter **Learn Mode** — a fill-in-the-blank exercise system that transforms passive reading into active recall. Key terms are extracted from the prose and replaced with blanks. Users select the correct term from five options, only one of which is correct. The remaining four are plausible distractors drawn from the same domain glossary.

This document covers:
1. System design and UX flow
2. Difficulty scaling model
3. Scoring and mastery system
4. JSON schema for glossary entries and questions
5. Question generation and distractor selection algorithms
6. Complete glossaries and 10 sample questions per section (10 sections)
7. Bot and app integration specifications

---

## Part 1: System Design

### 1.1 User Experience Flow

```
[Read Almanac Section]
         │
         ▼
[End of Article / Section]
         │
         ▼
   ┌─────────────────────┐
   │  "Test Yourself?"   │
   │  [Start Learn Mode] │
   └─────────────────────┘
         │
         ▼
[Difficulty Selection]
   Easy / Medium / Hard / Adaptive
         │
         ▼
[Question Displayed]
  "The _____ of a wine refers to..."
  ○ terroir   ○ tannin   ○ bouquet
  ○ varietal  ○ appellation
         │
         ▼
[User Selects Answer]
         │
    ┌────┴────┐
  Correct   Wrong
    │          │
    ▼          ▼
[+1 streak] [Streak reset]
[+Points]   [Show correct]
[Next Q]    [Brief explanation]
            [Next Q]
         │
         ▼
[Session Complete — 10 questions]
         │
         ▼
[Score Summary + Badge Check]
```

### 1.2 Core Mechanics

**Question Format:**
A sentence drawn (or closely adapted) from Almanac content, with one key term replaced by a blank. The blank is always a single term or short phrase from the section's glossary.

**Answer Options:**
Five choices displayed. One is correct. Four are distractors selected by the distractor algorithm (see Part 4). Options are randomized in order each presentation.

**No time pressure by default.** Users may optionally enable a timer in settings for an additional challenge layer.

**Feedback:**
- Correct answer: Green highlight, brief reinforcement note, streak counter update.
- Wrong answer: Red highlight on selection, reveal correct answer in green, one-sentence explanation of why that term is correct.

---

## Part 2: Difficulty Scaling Model

### 2.1 Difficulty Tiers

| Tier | Distractor Logic | Example |
| --- | --- | --- |
| **Easy** | Distractors from unrelated categories, clearly wrong | `terroir` vs. `tachycardia`, `arbitration`, `mise en place`, `hexagram` |
| **Medium** | Distractors from same section, same general category but different meaning | `terroir` vs. `appellation`, `varietal`, `vintage`, `bouquet` |
| **Hard** | Distractors that are semantically adjacent — terms often confused with each other | `terroir` vs. `appellation`, `cru`, `typicity`, `provenance` |
| **Adaptive** | System tracks user's accuracy per term and increases difficulty on terms with >80% accuracy, eases off on terms <60% accuracy | Dynamic |

### 2.2 Adaptive Mode Logic

```
For each term in user history:
  accuracy = correct_answers / total_attempts

  if accuracy > 0.80 → assign Hard distractors
  if 0.60 <= accuracy <= 0.80 → assign Medium distractors
  if accuracy < 0.60 → assign Easy distractors
  if attempts == 0 → assign Medium (default)
```

Adaptive mode also weights question selection toward terms the user hasn't seen recently (spaced repetition principle) and terms the user has gotten wrong before (error-focused review).

### 2.3 Sentence Selection

Questions are drawn from a curated bank of template sentences. Each template is tagged with:
- `section` — which Almanac chapter it belongs to
- `term` — the key term being tested
- `difficulty` — Easy / Medium / Hard (referring to how ambiguous the blank is in context)
- `context_richness` — High / Medium / Low (how many context clues surround the blank)

Easy-difficulty questions have High context richness: the sentence gives the user strong hints even without the term. Hard-difficulty questions have Low context richness: the sentence provides minimal clues beyond the structural role of the blank.

---

## Part 3: Scoring and Mastery System

### 3.1 Points Structure

| Action | Points |
| --- | --- |
| Correct answer | +10 |
| Correct on Hard difficulty | +20 |
| Streak of 3 | Bonus +15 |
| Streak of 5 | Bonus +30 |
| Streak of 10 | Bonus +75 |
| Wrong answer | 0 (no penalty) |
| Perfect round (10/10) | Bonus +50 |

### 3.2 Streak Tracking

Streaks reset on any wrong answer. The streak counter is displayed prominently during the session. Users receive a visual "streak fire" animation for streaks of 5+.

### 3.3 Section Mastery Badges

Each section offers a **Mastery Badge** awarded when a user achieves:
- ≥ 85% accuracy over a minimum of 30 questions in that section
- At least one Hard-difficulty round completed

Badges are permanent and displayed on the user's profile. A section's badge turns **gold** when the user achieves 95%+ accuracy over 50+ questions.

### 3.4 Global Leaderboard (Optional)

Users may opt into a weekly leaderboard. Points reset each Monday. Top performers receive a "Scholar of the Week" acknowledgment in the Almanac newsletter.

---

## Part 4: JSON Schema

### 4.1 Glossary Entry Schema

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GlossaryEntry",
  "type": "object",
  "required": ["id", "term", "definition", "section", "difficulty", "related_terms", "distractors"],
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier, e.g. 'wine-terroir'"
    },
    "term": {
      "type": "string",
      "description": "The glossary term itself"
    },
    "definition": {
      "type": "string",
      "description": "Plain-language definition used in feedback"
    },
    "section": {
      "type": "string",
      "enum": ["wine", "medical", "legal", "cooking", "weather", "games", "psychology", "astrology", "financial", "folk"]
    },
    "difficulty": {
      "type": "string",
      "enum": ["easy", "medium", "hard"],
      "description": "Baseline difficulty of questions using this term"
    },
    "related_terms": {
      "type": "array",
      "items": { "type": "string" },
      "description": "IDs of semantically adjacent terms (used for Hard distractors)"
    },
    "distractors": {
      "type": "object",
      "properties": {
        "easy": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Term IDs from other sections for Easy distractor pool"
        },
        "medium": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Term IDs from same section, different category"
        },
        "hard": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Term IDs that are closely related and often confused"
        }
      }
    },
    "example_sentences": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "sentence": { "type": "string" },
          "context_richness": { "type": "string", "enum": ["high", "medium", "low"] },
          "blank_position": { "type": "string", "enum": ["start", "middle", "end"] }
        }
      }
    }
  }
}
```

### 4.2 Question Bank Entry Schema

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "QuestionEntry",
  "type": "object",
  "required": ["id", "section", "term_id", "sentence_with_blank", "correct_answer", "difficulty"],
  "properties": {
    "id": { "type": "string" },
    "section": { "type": "string" },
    "term_id": { "type": "string" },
    "sentence_with_blank": {
      "type": "string",
      "description": "The display sentence. Blank represented as _____"
    },
    "correct_answer": { "type": "string" },
    "difficulty": { "type": "string", "enum": ["easy", "medium", "hard"] },
    "context_richness": { "type": "string", "enum": ["high", "medium", "low"] },
    "explanation": {
      "type": "string",
      "description": "Shown after wrong answer — why this term is correct here"
    },
    "source": {
      "type": "string",
      "description": "Almanac section/article this sentence is drawn from"
    }
  }
}
```

---

## Part 5: Algorithms

### 5.1 Question Generation Algorithm

```
def generate_question(section, difficulty="medium", user_history=None):
    """
    Select a question from the bank for a given section and difficulty.
    Applies spaced repetition weighting if user_history provided.
    """
    # 1. Filter question bank by section and difficulty
    candidates = [q for q in QUESTION_BANK 
                  if q["section"] == section 
                  and q["difficulty"] == difficulty]

    if user_history:
        # 2. Weight by recency (prefer unseen/old questions)
        candidates = apply_recency_weight(candidates, user_history)

        # 3. Weight by accuracy (prefer terms with low accuracy)
        candidates = apply_accuracy_weight(candidates, user_history)

    # 4. Select question (weighted random)
    question = weighted_sample(candidates)

    # 5. Generate distractor set
    distractors = select_distractors(question["term_id"], difficulty, n=4)

    # 6. Assemble options (correct + 4 distractors, shuffled)
    options = shuffle([question["correct_answer"]] + distractors)

    return {
        "question": question,
        "options": options
    }
```

### 5.2 Distractor Selection Logic

```
def select_distractors(term_id, difficulty, n=4):
    """
    Select n plausible-but-wrong distractors for a given term.
    """
    term = GLOSSARY[term_id]

    if difficulty == "easy":
        # Pull from other sections entirely
        pool = [t for t in GLOSSARY.values() 
                if t["section"] != term["section"]]

    elif difficulty == "medium":
        # Pull from same section, different category
        pool = [t for t in GLOSSARY.values()
                if t["section"] == term["section"]
                and t["id"] != term_id]

    elif difficulty == "hard":
        # Prefer semantically adjacent terms first
        related = term.get("related_terms", [])
        related_terms = [GLOSSARY[r] for r in related if r in GLOSSARY]

        # Fill remainder from same section if related pool too small
        if len(related_terms) >= n:
            pool = related_terms
        else:
            same_section = [t for t in GLOSSARY.values()
                           if t["section"] == term["section"]
                           and t["id"] != term_id
                           and t["id"] not in related]
            pool = related_terms + same_section

    # Select n from pool (avoid repetition)
    selected = random_sample(pool, min(n, len(pool)))
    return [t["term"] for t in selected]
```

### 5.3 Spaced Repetition Weighting

```
def apply_recency_weight(candidates, user_history):
    """Reduce weight of recently seen questions."""
    now = current_timestamp()

    for q in candidates:
        last_seen = user_history.get(q["id"], {}).get("last_seen", 0)
        days_since = (now - last_seen) / 86400

        # Weight increases with time since last seen (max at 7 days)
        q["weight"] = min(days_since / 7.0, 1.0)

    return candidates

def apply_accuracy_weight(candidates, user_history):
    """Increase weight of low-accuracy terms."""
    for q in candidates:
        history = user_history.get(q["term_id"], {})
        attempts = history.get("attempts", 0)
        correct = history.get("correct", 0)

        if attempts == 0:
            accuracy = 0.5  # Unknown → neutral weight
        else:
            accuracy = correct / attempts

        # Lower accuracy → higher weight
        q["weight"] = q.get("weight", 1.0) * (1.0 - accuracy * 0.5)

    return candidates
```

---

## Part 6: Section Glossaries and Sample Questions

*Format for each question: `"sentence with _____"` → `[Correct / Distractor / Distractor / Distractor / Distractor]`*
*Correct answer always listed first; display order is randomized.*

---

### 6.1 Wine / Connoisseur

**Glossary (30 terms):**
terroir, tannin, bouquet, nose, finish, body, legs, varietal, vintage, appellation, decanting, oxidation, malolactic fermentation, sommelier, cuvée, brut, demi-sec, magnum, ullage, punt, corked, brix, must, lees, sur lie, disgorgement, négociant, residual sugar, typicity, microclimate

**10 Sample Questions:**

1. **Easy**
   "The \_\_\_\_\_ of a wine refers to the complete natural environment in which it is produced, including soil, climate, and topography."
   → `[terroir / tachycardia / mise en place / arbitration / ascendant]`
2. **Medium**
   "A wine's \_\_\_\_\_ is the complex of aromas perceived by sniffing the glass before tasting — distinct from the flavors that develop on the palate."
   → `[nose / finish / body / legs / vintage]`
3. **Medium**
   "The \_\_\_\_\_ of a Champagne refers to its sweetness level; at the driest end, a wine labeled this way contains fewer than 12 grams of residual sugar per liter."
   → `[brut / demi-sec / cuvée / magnum / disgorgement]`
4. **Hard**
   "An \_\_\_\_\_ is the legally defined geographic region whose name a wine is permitted to display on its label, governed by strict production rules."
   → `[appellation / terroir / varietal / typicity / microclimate]`
5. **Hard**
   "A wine described as having \_\_\_\_\_ is said to express characteristics typical and specific to its grape variety and place of origin — a quality prized above technical perfection."
   → `[typicity / terroir / body / finish / oxidation]`
6. **Medium**
   "The process of \_\_\_\_\_ involves pouring wine into a wide-bottomed vessel to separate it from sediment and allow volatile compounds to dissipate."
   → `[decanting / oxidation / disgorgement / sur lie / lees]`
7. **Easy**
   "A trained beverage professional who manages wine programs, advises guests, and often conducts cellar management is called a \_\_\_\_\_."
   → `[sommelier / négociant / triage / fiduciary / mirepoix]`
8. **Hard**
   "When a wine undergoes \_\_\_\_\_, harsh malic acids are converted by bacteria into softer lactic acids, giving the wine a rounder, creamier texture."
   → `[malolactic fermentation / oxidation / disgorgement / brix / must]`
9. **Medium**
   "The \_\_\_\_\_ in a wine are responsible for the dry, astringent sensation felt along the gums and the inside of the cheeks, derived primarily from grape skins and seeds."
   → `[tannins / legs / body / finish / residual sugar]`
10. **Hard**
    "The \_\_\_\_\_ is the indentation at the bottom of a wine bottle, which adds structural strength and, in sparkling wine production, helps consolidate sediment during riddling."
    → `[punt / ullage / magnum / lees / cuvée]`

---

### 6.2 Medical / Body

**Glossary (30 terms):**
referred pain, palpation, cyanosis, edema, tachycardia, bradycardia, diaphoresis, syncope, anaphylaxis, triage, contusion, laceration, abrasion, hematoma, systolic, diastolic, arrythmia, embolism, infarction, ischemia, pallor, jaundice, epistaxis, dyspnea, hemostasis, sepsis, shock, biopsy, prognosis, contraindication

**10 Sample Questions:**

1. **Easy**
   "The process of \_\_\_\_\_ involves sorting and prioritizing patients for treatment based on the severity of their condition, most commonly used in mass casualty events."
   → `[triage / embolism / mise en place / gambit / transit]`
2. **Medium**
   "A patient experiencing \_\_\_\_\_ is sweating profusely, often as a symptom of severe pain, infection, or cardiovascular distress."
   → `[diaphoresis / cyanosis / pallor / jaundice / edema]`
3. **Hard**
   "The \_\_\_\_\_ of a blood pressure reading — the lower number — represents the pressure in the arteries when the heart rests between beats."
   → `[diastolic / systolic / ischemia / arrhythmia / hemostasis]`
4. **Medium**
   "\_\_\_\_\_ is the bluish discoloration of the skin or mucous membranes, caused by insufficient oxygen in the blood."
   → `[cyanosis / pallor / jaundice / edema / diaphoresis]`
5. **Hard**
   "\_\_\_\_\_ occurs when pain is perceived at a location other than its actual site of origin — a classic example being left arm pain during a cardiac event."
   → `[referred pain / syncope / embolism / dyspnea / prognosis]`
6. **Medium**
   "A sudden loss of consciousness caused by a temporary drop in blood flow to the brain is called \_\_\_\_\_."
   → `[syncope / anaphylaxis / shock / infarction / bradycardia]`
7. **Hard**
   "\_\_\_\_\_ is a life-threatening systemic response to infection, characterized by widespread inflammation, organ dysfunction, and circulatory failure."
   → `[sepsis / anaphylaxis / shock / ischemia / embolism]`
8. **Medium**
   "\_\_\_\_\_ refers to an abnormal heart rate — specifically one that is faster than the normal resting rate of 60-100 beats per minute."
   → `[tachycardia / bradycardia / arrhythmia / syncope / infarction]`
9. **Easy**
   "The physical examination technique of \_\_\_\_\_ involves using the hands to apply pressure to the body to assess organs, detect tenderness, or locate masses."
   → `[palpation / triage / biopsy / hemostasis / diaphoresis]`
10. **Hard**
    "A \_\_\_\_\_ occurs when a blood clot or other substance travels through the bloodstream and blocks a vessel — commonly in the lungs or brain."
    → `[embolism / infarction / ischemia / sepsis / hematoma]`

---

### 6.3 Legal / Contractual

**Glossary (30 terms):**
indemnification, arbitration, lien, escrow, deposition, tort, liability, negligence, fiduciary, subpoena, statute of limitations, injunction, plaintiff, defendant, affidavit, breach, damages, warranty, jurisdiction, consideration, easement, foreclosure, garnishment, habeas corpus, intestate, liquidated damages, mediation, remedy, standing, venue

**10 Sample Questions:**

1. **Easy**
   "A \_\_\_\_\_ is a legal command requiring a person to testify or produce documents in a legal proceeding."
   → `[subpoena / tannin / edema / Beaufort scale / retrograde]`
2. **Medium**
   "An \_\_\_\_\_ is a sworn written statement made under oath, used as evidence in court proceedings."
   → `[affidavit / deposition / subpoena / warrant / injunction]`
3. **Hard**
   "A \_\_\_\_\_ is a legal claim against a property — such as a house or vehicle — that serves as security for a debt or obligation until that debt is paid."
   → `[lien / escrow / indemnification / easement / garnishment]`
4. **Medium**
   "\_\_\_\_\_ is the legal concept describing a duty of care — when a party responsible for another's interests (such as an attorney or trustee) is required to act in that person's best interest."
   → `[fiduciary / liability / negligence / indemnification / tort]`
5. **Hard**
   "In a contract, \_\_\_\_\_ is the agreed-upon value or action exchanged between parties — the 'something for something' that makes an agreement legally binding."
   → `[consideration / damages / warranty / remedy / breach]`
6. **Medium**
   "A \_\_\_\_\_ is a court order compelling or prohibiting a specific action, often issued to prevent irreparable harm while a case is ongoing."
   → `[injunction / arbitration / mediation / subpoena / standing]`
7. **Hard**
   "\_\_\_\_\_ is the legal right to use another person's land for a specific purpose — such as accessing a public road or running utilities across a neighbor's property."
   → `[easement / lien / jurisdiction / venue / foreclosure]`
8. **Medium**
   "The \_\_\_\_\_ is the time limit within which a lawsuit must be filed after an event occurs; once it expires, the claim is typically barred forever."
   → `[statute of limitations / jurisdiction / venue / standing / remedy]`
9. **Hard**
   "A civil wrong — not arising from a contract — that causes harm and for which the injured party may seek compensation in court is known as a \_\_\_\_\_."
   → `[tort / breach / negligence / liability / damages]`
10. **Medium**
    "When funds or assets are held by a neutral third party until specified conditions of a transaction are met, they are said to be held in \_\_\_\_\_."
    → `[escrow / lien / indemnification / consideration / liquidated damages]`

---

### 6.4 Cooking / Recipes

**Glossary (30 terms):**
mise en place, deglaze, emulsion, reduction, roux, mirepoix, blanch, braise, sauté, julienne, chiffonade, bain-marie, fond, dredge, temper, render, sear, fold, macerate, nappe, en papillote, baste, liaison, clarify, monter au beurre, pâte, parcook, rest, umami, zest

**10 Sample Questions:**

1. **Easy**
   "\_\_\_\_\_ is the French culinary concept of having all ingredients prepped, measured, and organized before cooking begins."
   → `[mise en place / terroir / triage / gambit / cortisol]`
2. **Medium**
   "To \_\_\_\_\_ means to pour liquid into a hot pan after cooking meat in order to dissolve and incorporate the flavorful browned bits stuck to the bottom."
   → `[deglaze / reduce / sear / baste / render]`
3. **Hard**
   "The \_\_\_\_\_ is the foundational mixture of two-thirds onion, one-third each celery and carrot, cooked slowly to build depth of flavor in stocks and braises."
   → `[mirepoix / liaison / fond / roux / reduction]`
4. **Medium**
   "A \_\_\_\_\_ is a thickening agent made by cooking equal parts fat and flour together until the raw flour taste is cooked out."
   → `[roux / emulsion / liaison / nappe / reduction]`
5. **Hard**
   "To \_\_\_\_\_ chocolate or cream means to slowly raise its temperature by adding small amounts of hot liquid, preventing the mixture from seizing or breaking."
   → `[temper / fold / render / clarify / macerate]`
6. **Medium**
   "A \_\_\_\_\_ is a stable mixture of two normally immiscible liquids — such as oil and water — achieved through the action of an emulsifying agent like egg yolk or mustard."
   → `[emulsion / reduction / liaison / nappe / fond]`
7. **Hard**
   "The technique of \_\_\_\_\_ involves cutting vegetables or other ingredients into uniform, thin matchstick shapes approximately 3mm × 3mm × 5cm."
   → `[julienne / chiffonade / brunoise / mirepoix / parcook]`
8. **Medium**
   "To \_\_\_\_\_ is to briefly immerse food in boiling water and then immediately transfer it to ice water — halting cooking while preserving color and texture."
   → `[blanch / braise / sauté / render / parcook]`
9. **Hard**
   "\_\_\_\_\_ is the concentrated, flavorful residue of caramelized proteins and sugars left on a pan's surface after searing, and is the foundation of pan sauces."
   → `[fond / reduction / nappe / liaison / umami]`
10. **Medium**
    "Cooking food sealed in parchment paper or foil — so it steams in its own aromatic juices — is called cooking \_\_\_\_\_."
    → `[en papillote / bain-marie / braise / render / parcook]`

---

### 6.5 Weather / Environment

**Glossary (30 terms):**
barometric pressure, dew point, wind shear, cumulonimbus, occluded front, isobar, inversion layer, albedo, Coriolis effect, El Niño, adiabatic, supercell, storm surge, jet stream, mesocyclone, precipitation, humidity, advection, sublimation, orographic lift, virga, CAPE, tropopause, squall line, radiosonde, haboob, waterspout, lenticular cloud, thermal, graupel

**10 Sample Questions:**

1. **Easy**
   "The \_\_\_\_\_ is the measure of atmospheric weight pressing down on a surface — a falling reading typically signals approaching bad weather."
   → `[barometric pressure / tannin / arbitration / oxytocin / retrograde]`
2. **Medium**
   "The \_\_\_\_\_ is the temperature at which air must be cooled for water vapor to condense into liquid droplets — when it equals the air temperature, fog or clouds form."
   → `[dew point / humidity / inversion layer / adiabatic / thermal]`
3. **Hard**
   "The \_\_\_\_\_ is the deflection of moving air (and ocean currents) caused by Earth's rotation — to the right in the Northern Hemisphere and to the left in the Southern."
   → `[Coriolis effect / El Niño / advection / jet stream / orographic lift]`
4. **Medium**
   "A \_\_\_\_\_ is a line on a weather map connecting points of equal atmospheric pressure, used to identify high and low pressure systems and predict wind patterns."
   → `[isobar / thermal / CAPE / radiosonde / tropopause]`
5. **Hard**
   "\_\_\_\_\_ refers to the phenomenon where air cools as it rises (or warms as it descends) at a predictable rate without exchanging heat with its surroundings."
   → `[adiabatic / inversion layer / orographic lift / CAPE / advection]`
6. **Medium**
   "An \_\_\_\_\_ occurs when a warm air mass is lifted entirely off the ground by converging cold and cool air masses, cutting off its supply of moisture."
   → `[occluded front / squall line / supercell / haboob / mesocyclone]`
7. **Hard**
   "\_\_\_\_\_ is the ratio of reflected solar energy to incoming solar energy for a surface — fresh snow has a very high value, while dark ocean water has a very low one."
   → `[albedo / CAPE / sublimation / inversion layer / jet stream]`
8. **Medium**
   "A \_\_\_\_\_ is a tall, anvil-shaped cloud associated with thunderstorms, capable of producing heavy rain, lightning, hail, and tornadoes."
   → `[cumulonimbus / lenticular cloud / virga / supercell / haboob]`
9. **Hard**
   "\_\_\_\_\_ is the horizontal transport of atmospheric properties — such as heat or moisture — by wind, as distinguished from vertical convection."
   → `[advection / adiabatic / orographic lift / sublimation / Coriolis effect]`
10. **Medium**
    "Rain or snow that falls from a cloud but evaporates before reaching the ground produces streaks visible from a distance called \_\_\_\_\_."
    → `[virga / graupel / haboob / waterspout / precipitation]`

---

### 6.6 Games / Strategy

**Glossary (30 terms):**
gambit, en passant, ko, atari, doubling cube, trump, finesse, bluff, ante, check, stalemate, zugzwang, sente, gote, meld, ruff, overtrick, sacrifice, tempo, squeeze, fork, pin, skewer, zwischenzug, initiative, pawn structure, endgame, opening theory, material advantage, compensation

**10 Sample Questions:**

1. **Easy**
   "A \_\_\_\_\_ in chess or poker refers to offering a sacrifice or making a seemingly disadvantageous move in order to gain a positional or strategic benefit later."
   → `[gambit / tannin / deposition / oxytocin / isobar]`
2. **Medium**
   "In chess, \_\_\_\_\_ is a special pawn capture that occurs immediately after an opponent moves their pawn two squares forward — the capturing pawn takes as if the opponent's pawn had only moved one square."
   → `[en passant / check / stalemate / fork / zwischenzug]`
3. **Hard**
   "The \_\_\_\_\_ is a position in chess where the player who must move has no legal moves but is not in check — resulting in a draw rather than a loss."
   → `[stalemate / zugzwang / check / pin / initiative]`
4. **Medium**
   "In Go, the \_\_\_\_\_ rule prevents immediate recapture of a single stone, preventing infinite loops of capture and recapture."
   → `[ko / atari / sente / gote / meld]`
5. **Hard**
   "A \_\_\_\_\_ in chess is a position — generally losing — where any legal move a player makes worsens their position; the obligation to move is itself the disadvantage."
   → `[zugzwang / stalemate / fork / pin / squeeze]`
6. **Medium**
   "Playing with \_\_\_\_\_ in strategy games means dictating the pace of play and forcing the opponent to react rather than act."
   → `[initiative / tempo / compensation / sente / material advantage]`
7. **Hard**
   "In bridge, a \_\_\_\_\_ play involves leading a card to force a decision from the next player before a particular card's position is revealed — a high-risk maneuver relying on uncertainty."
   → `[finesse / bluff / ruff / squeeze / overtrick]`
8. **Medium**
   "In poker, placing money into the pot before cards are dealt — typically mandatory for one or two players at the table — is called posting the \_\_\_\_\_."
   → `[ante / bluff / trump / doubling cube / check]`
9. **Hard**
   "A \_\_\_\_\_ in chess simultaneously attacks two pieces with one piece, forcing the opponent to sacrifice one of the attacked pieces."
   → `[fork / pin / skewer / zwischenzug / squeeze]`
10. **Medium**
    "In Go, a move is described as \_\_\_\_\_ when it threatens immediate capture, requiring the opponent to respond defensively rather than advance their own plans."
    → `[atari / ko / sente / gote / initiative]`

---

### 6.7 Psychology / Relationships

**Glossary (30 terms):**
attachment style, differentiation, enmeshment, projection, transference, cognitive dissonance, confirmation bias, Dunning-Kruger effect, limbic system, cortisol, oxytocin, secure attachment, avoidant attachment, anxious attachment, disorganized attachment, locus of control, gaslighting, codependency, individuation, mirror neurons, parasympathetic, sympathetic nervous system, hypervigilance, self-efficacy, schema, narcissistic supply, triangulation, dissociation, grounding, affect regulation

**10 Sample Questions:**

1. **Easy**
   "\_\_\_\_\_ is the hormone often called the 'stress hormone,' released by the adrenal glands in response to perceived threat or danger."
   → `[cortisol / oxytocin / tannin / barometric pressure / lien]`
2. **Medium**
   "\_\_\_\_\_ is the tendency to search for, interpret, and recall information in a way that confirms one's pre-existing beliefs, ignoring contradictory evidence."
   → `[confirmation bias / cognitive dissonance / Dunning-Kruger effect / projection / schema]`
3. **Hard**
   "The \_\_\_\_\_ describes the phenomenon in which people with limited knowledge in a domain overestimate their competence, while genuine experts tend to underestimate theirs."
   → `[Dunning-Kruger effect / confirmation bias / cognitive dissonance / self-efficacy / locus of control]`
4. **Medium**
   "In relational psychology, \_\_\_\_\_ refers to the blurring of personal boundaries between individuals — typically in family systems — where members struggle to maintain separate identities."
   → `[enmeshment / codependency / differentiation / individuation / transference]`
5. **Hard**
   "The psychological defense mechanism of \_\_\_\_\_ involves unconsciously attributing one's own unacceptable thoughts, emotions, or motives to another person."
   → `[projection / transference / dissociation / triangulation / gaslighting]`
6. **Medium**
   "The mental discomfort experienced when holding two contradictory beliefs simultaneously — or acting against one's stated values — is called \_\_\_\_\_."
   → `[cognitive dissonance / confirmation bias / projection / schema / hypervigilance]`
7. **Hard**
   "In family systems theory, a person who has achieved \_\_\_\_\_ can maintain a stable sense of self while remaining emotionally connected to others — neither fused with nor cut off from them."
   → `[differentiation / individuation / secure attachment / self-efficacy / affect regulation]`
8. **Medium**
   "The \_\_\_\_\_ is the brain's emotional processing center — encompassing structures like the amygdala and hippocampus — central to memory formation and threat response."
   → `[limbic system / parasympathetic nervous system / sympathetic nervous system / prefrontal cortex / mirror neurons]`
9. **Hard**
   "\_\_\_\_\_ is a pattern where feelings or behaviors originally directed toward a significant figure in one's past are redirected — often unconsciously — onto a current relationship, such as a therapist."
   → `[transference / projection / schema / enmeshment / narcissistic supply]`
10. **Medium**
    "The 'bonding hormone' released during physical touch, social connection, and childbirth — which promotes trust and reduces stress — is called \_\_\_\_\_."
    → `[oxytocin / cortisol / serotonin / dopamine / adrenaline]`

---

### 6.8 Astrology / Oracle

**Glossary (30 terms):**
ascendant, midheaven, transit, aspect, conjunction, opposition, trine, square, retrograde, decan, nakshatra, hexagram, trigram, geomantic figure, stellium, intercepted sign, chart ruler, dispositor, Lot of Fortune, antiscia, syzygy, mutual reception, fixed star, progressed chart, solar arc, profection, ingress, lunar nodes, void-of-course, angular house

**10 Sample Questions:**

1. **Easy**
   "A planet in \_\_\_\_\_ appears to move backward in the sky from Earth's perspective — in astrology, this is associated with delays, revision, and turned-inward energy."
   → `[retrograde / trine / opposition / mise en place / syncope]`
2. **Medium**
   "The \_\_\_\_\_ is the zodiac sign rising on the eastern horizon at the moment of birth, shaping a person's outward manner and first impressions."
   → `[ascendant / midheaven / chart ruler / dispositor / angular house]`
3. **Hard**
   "A \_\_\_\_\_ occurs when two or more planets occupy the same degree of the zodiac — their energies merge, intensifying the themes of both."
   → `[conjunction / opposition / trine / square / aspect]`
4. **Medium**
   "In I Ching, each \_\_\_\_\_ is a six-line figure composed of broken (yin) and unbroken (yang) lines, representing one of 64 possible states of change."
   → `[hexagram / trigram / geomantic figure / aspect / nakshatra]`
5. **Hard**
   "A \_\_\_\_\_ is a grouping of three or more planets in the same sign or a small area of the chart — intensifying that sign's energy and often indicating a focus of major life themes."
   → `[stellium / conjunction / angular house / midheaven / solar arc]`
6. **Medium**
   "When a planet makes a \_\_\_\_\_ — a 120-degree angle — to another in the natal or transit chart, the relationship is considered harmonious and flowing."
   → `[trine / sextile / square / opposition / conjunction]`
7. **Hard**
   "A \_\_\_\_\_ in Vedic astrology is one of 27 lunar mansions — a division of the zodiac based on the Moon's daily movement — each associated with specific qualities and deities."
   → `[nakshatra / decan / profection / Lot of Fortune / antiscia]`
8. **Medium**
   "The \_\_\_\_\_ in a natal chart is the highest point in the sky at the moment of birth, associated with career, public reputation, and life calling."
   → `[midheaven / ascendant / angular house / chart ruler / Lot of Fortune]`
9. **Hard**
   "In geomantic divination, a \_\_\_\_\_ is one of sixteen figures formed by dots arranged in four rows — each with specific divinatory meaning, analogous to tarot cards."
   → `[geomantic figure / hexagram / trigram / nakshatra / aspect]`
10. **Medium**
    "A \_\_\_\_\_ in astrology refers to the current movement of planets through the sky and how they interact with the positions in a natal chart, triggering events and themes."
    → `[transit / aspect / solar arc / progressed chart / ingress]`

---

### 6.9 Financial

**Glossary (30 terms):**
amortization, compound interest, diversification, liquidity, equity, collateral, deductible, premium, annuity, yield, hedge, margin, arbitrage, beta, capital gains, depreciation, dividend, fiduciary, inflation, leverage, net worth, portfolio, risk-adjusted return, solvency, tax-loss harvesting, time value of money, volatility, bear market, bull market, index fund

**10 Sample Questions:**

1. **Easy**
   "\_\_\_\_\_ is the process by which interest earns additional interest over time — often described as 'making money on your money.'"
   → `[compound interest / amortization / dividends / yield / tannin]`
2. **Medium**
   "\_\_\_\_\_ is the process of spreading investments across different asset classes, sectors, or geographies to reduce the impact of any single loss."
   → `[diversification / hedging / leverage / portfolio management / arbitrage]`
3. **Hard**
   "The \_\_\_\_\_ of an investment measures how quickly and easily it can be converted to cash without significantly affecting its price."
   → `[liquidity / solvency / yield / margin / net worth]`
4. **Medium**
   "\_\_\_\_\_ refers to the gradual repayment of a loan through scheduled payments that cover both principal and interest over the loan's life."
   → `[amortization / depreciation / compound interest / leverage / annuity]`
5. **Hard**
   "A financial \_\_\_\_\_ is a strategy or instrument used to offset potential losses in an investment — like buying a put option to protect against a stock's decline."
   → `[hedge / margin / arbitrage / beta / leverage]`
6. **Medium**
   "The \_\_\_\_\_ of a bond or savings account refers to the return expressed as a percentage of the investment — calculated annually."
   → `[yield / dividend / premium / capital gains / return]`
7. **Hard**
   "\_\_\_\_\_ is the simultaneous purchase and sale of the same asset in different markets to exploit a price discrepancy — typically fleeting, and usually automated."
   → `[arbitrage / hedge / leverage / margin / beta]`
8. **Medium**
   "An \_\_\_\_\_ is a financial product that pays out a fixed stream of income over time — commonly used to provide retirement income."
   → `[annuity / dividend / premium / yield / portfolio]`
9. **Hard**
   "A stock's \_\_\_\_\_ measures its volatility relative to the broader market — a value above 1.0 means it moves more dramatically than the index; below 1.0 means it moves less."
   → `[beta / volatility / margin / risk-adjusted return / leverage]`
10. **Medium**
    "\_\_\_\_\_ is the practice of selling losing investments before year-end to realize a capital loss, which can offset taxable gains elsewhere in a portfolio."
    → `[tax-loss harvesting / depreciation / diversification / amortization / capital gains]`

---

### 6.10 Folk Wisdom / Survival

**Glossary (30 terms):**
tonic immobility, petrichor, Beaufort scale, solunar, Rule of Twelfths, carcinization, fermentation, lye, tallow, whetstone, deadfall trap, triangulation, signal fire, lean-to, paracord, bowline, survival priorities, water purification, celestial navigation, foraging, edible indicator, cordage, tinder bundle, char cloth, reflective signaling, pemmican, dead reckoning, compass bearing, wind rose, heat index

**10 Sample Questions:**

1. **Easy**
   "The pleasant earthy scent that follows rainfall on dry soil is called \_\_\_\_\_ — caused by chemical compounds released by soil bacteria as moisture activates them."
   → `[petrichor / tannin / dew point / cortisol / indemnification]`
2. **Medium**
   "The \_\_\_\_\_ is a measurement system that classifies wind intensity on a scale from 0 (calm) to 12 (hurricane force), originally developed for maritime use."
   → `[Beaufort scale / wind shear / Coriolis effect / heat index / solunar]`
3. **Hard**
   "\_\_\_\_\_ is the convergent evolutionary tendency of crustaceans to repeatedly evolve crab-like body shapes across different lineages — a striking example of natural selection converging on a common solution."
   → `[carcinization / tonic immobility, fermentation / deadfall trap / edible indicator]`
4. **Medium**
   "\_\_\_\_\_ tables predict the times of day when fish and game are most active — based on the gravitational influence of the sun and moon — used widely by hunters and anglers."
   → `[solunar / Rule of Twelfths / celestial navigation / dead reckoning / compass bearing]`
5. **Hard**
   "The \_\_\_\_\_ is a navigational rule used to estimate tidal flow: tides don't rise and fall evenly — the middle two hours of a six-hour tidal cycle carry roughly half the total tidal volume."
   → `[Rule of Twelfths / dead reckoning / triangulation / compass bearing / solunar]`
6. **Medium**
   "\_\_\_\_\_ is the preservation and transformation of food through controlled microbial activity — the process that turns milk into cheese, cabbage into sauerkraut, and grain into beer."
   → `[fermentation / lye, tallow / pemmican / char cloth]`
7. **Hard**
   "\_\_\_\_\_ is a caustic alkaline substance historically made from wood ash and water, used in soap-making, food preservation (olives, pretzels), and processing hides."
   → `[lye / tallow / cordage / pemmican / whetstone]`
8. **Medium**
   "A \_\_\_\_\_ is an abrasive stone used to sharpen blades by removing metal along the cutting edge — available in varying grits for coarse grinding versus fine finishing."
   → `[whetstone / paracord / deadfall trap / lean-to / tinder bundle]`
9. **Hard**
   "\_\_\_\_\_ is the state of apparent paralysis in prey animals — such as rabbits or sharks — when subjected to certain physical restraint or sensory conditions, sometimes misinterpreted as death."
   → `[tonic immobility / carcinization / dead reckoning / foraging / edible indicator]`
10. **Medium**
    "The high-calorie, shelf-stable survival food made by combining rendered fat with dried meat and sometimes dried berries — historically carried by Indigenous peoples and explorers — is called \_\_\_\_\_."
    → `[pemmican / tallow / fermentation / cordage / char cloth]`

---

## Part 7: Technical Integration

### 7.1 Bot Commands (Telegram / Discord)

**`/learn [section]`**
Starts a Learn Mode session for the specified section. If no section is specified, defaults to the section of the most recently read article.

```
/learn wine       → Wine/Connoisseur glossary, 10 questions, Medium difficulty
/learn wine hard  → Hard difficulty
/learn            → Most recently read section
```

**`/quiz [section] [n]`**
Runs a quick quiz of n questions (default 5, max 20). Returns a score summary with percentage accuracy.

```
/quiz medical 10   → 10 medical questions
/quiz              → 5 questions from most recent section
```

**`/mastery`**
Displays the user's current mastery badges and accuracy statistics across all sections.

**`/streak`**
Shows the user's current streak, longest streak, and session stats.

### 7.2 App Integration (Post-Article "Test Yourself" Button)

After any article in the Observatory Almanac app, a **"Test Yourself"** card appears at the end:

```
┌─────────────────────────────────────┐
│  🧠 Test Yourself                   │
│  You just read: Wine & Connoisseur  │
│                                     │
│  [Quick Quiz — 5 Qs]  [Full Learn Mode — 10 Qs] │
│                                     │
│  Your mastery: ████░░░░░ 47%        │
│  Best streak this section: 7        │
└─────────────────────────────────────┘
```

Tapping either button launches the Learn Mode modal within the app, pre-loaded with the section's question bank filtered to the user's current difficulty tier.

### 7.3 API Endpoints

```
GET  /api/learn/question?section=wine&difficulty=medium&userId=xxx
POST /api/learn/answer { questionId, userId, selectedTerm }
GET  /api/learn/stats?userId=xxx
GET  /api/learn/badges?userId=xxx
GET  /api/glossary?section=wine
POST /api/glossary/entry  (admin only)
```

### 7.4 Data Persistence

User progress is stored per-user in a `user_learning_state` document:

```
{
  "userId": "...",
  "sections": {
    "wine": {
      "questionsAnswered": 47,
      "correctAnswers": 38,
      "accuracy": 0.809,
      "currentStreak": 4,
      "longestStreak": 12,
      "masteryBadge": "silver",
      "lastSession": "2026-04-01T14:22:00Z",
      "termHistory": {
        "wine-terroir": { "attempts": 5, "correct": 5, "lastSeen": "..." },
        "wine-tannin":  { "attempts": 3, "correct": 2, "lastSeen": "..." }
      }
    }
  }
}
```

---

## Part 8: Editorial Notes

### Content Guidelines for Question Authors

1. **Sentences must be extractable from real Almanac content.** Questions should feel like genuine excerpts, not invented definitions.
2. **The blank should be irreplaceable.** A well-crafted question makes the correct term the only plausible fit once the user knows the domain.
3. **Distractors must be tempting at the right difficulty.** A Medium distractor should make a reader pause — not immediately dismiss it. A Hard distractor should be something a person with partial knowledge might genuinely select.
4. **Explanations matter.** The one-sentence "why this term is correct" shown after a wrong answer is a teaching moment — make it count. It should add information, not just repeat the definition.
5. **Avoid definitional sentences as questions.** "A \_\_\_\_\_ is defined as..." is too easy. Prefer sentences that use the term in context, requiring understanding rather than memorization.

### Adding New Sections

When a new Almanac section is created:
1. Build a glossary of 30-50 terms with full schema entries
2. Write 20-30 template sentences (each tagged with context\_richness)
3. Assign hard distractor relationships between semantically adjacent terms
4. Seed 10 published sample questions (as documented above)
5. Update the section enum in the GlossaryEntry schema
6. Add bot command routing for the new section slug

---

*Document version: 1.0 — Observatory Almanac, The Discovery Machine*
*Next: Section XI.2 — The Self-Discovery Inventory (personality-adjacent reflection prompts)*

---

## Glossary Mad Libs Quiz