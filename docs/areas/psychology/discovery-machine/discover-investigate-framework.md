# The Two-Mode Assessment Framework

ð Discovery Machine â All Questionnaires

* [ð Depression Screen (PHQ-9)](../clinical-validated/#take-the-phq-9-now)
* [ð Anxiety Screen (GAD-7)](../clinical-validated/#take-the-gad-7-now)
* [ð§  Big Five Personality](../self-knowledge/#take-the-big-five-now)
* [ð¼ Career Type (RIASEC)](../vocational-personality/#holland-riasec)
* [ð Attachment Style](../relationship-social/#attachment-style)
* [ð³ï¸ Political Compass](../self-discovery-suite/#political-compass)
* [â¤ï¸ Relationship Health](../relationship-dynamics/#relationship-health)
* [ð¨ Emergency Decision Tree](../body-survival/#emergency-decision-tree)
* [ð¡ï¸ Scam Checker](../consumer-legal/#scam-checker)
* [ð Is This Dog Friendly?](../animal-nature/#dog-friendly)
* [ð  Home Safety Score](../home-environment/#home-safety)
* [ð What's That Smell/Sound?](../sensory-diagnostics/#whats-that-smell)
* [ð§ Boundary Health Check](../relational-behavioral-deep/#boundary-health)
* [ð Glossary Mad Libs Quiz](../mad-libs-learning/#glossary-quiz)

## The Discovery Machine â Design Specification

*The Observatory Almanac | Design Document v1.0*

---

## Overview

The Discovery Machine operates on a fundamental insight: there are two very different reasons someone picks up a self-assessment. The first is curiosity â a passing wonder about who they are, an invitation to play with identity. The second is genuine need â a desire to understand something real, something that might actually matter for how they live. These two motivations deserve completely different instruments.

This document defines the architecture for a dual-mode assessment system that serves both. Every assessment in the Cabinet exists in two forms: **Discover** (ð) and **Investigate** (ð¬). They are not "short" and "long" versions of the same thing â they are philosophically different instruments designed for different purposes, different moments, and different levels of user readiness.

---

## Part I: Mode Philosophy

### Mode 1: Discover ð

**The philosophy:** A Discover assessment is an invitation. It says: *Come look at this interesting thing about yourself.* It asks as few questions as needed to give someone a genuine mirror â not a precise measurement, but a reflection that provokes thought.

Discover assessments prioritize:
- **Friction reduction** â nothing that makes someone think "this is a lot of work"
- **Resonance over accuracy** â "which of these feels more like you?" is fine; we trust self-perception
- **Delight** â the process itself should feel like play, not work
- **A result that sparks** â the output should make someone say "huh, that's interesting" not just "ok"
- **An open door** â always ends with "want to go deeper?"

Discover assessments do NOT:
- Diagnose anything
- Make strong clinical claims
- Include validity checking (we trust the user to answer honestly)
- Generate severity ratings
- Try to catch bias

**Discover Question Parameters:**
- 5â10 questions maximum
- Multiple choice, "pick which resonates," or scenario-based
- No reverse scoring
- No attention checks
- Completion target: 2â3 minutes
- Reading level: casual, conversational
- Result: one or two broad categories, a brief evocative description, a question to sit with

### Mode 2: Investigate ð¬

**The philosophy:** An Investigate assessment is a serious tool. It says: *Let's actually look at this.* It earns its length by producing something worth the effort â a genuinely differentiated profile that could serve as a basis for reflection, conversation, or action.

Investigate assessments prioritize:
- **Construct validity** â measuring what they claim to measure
- **Reliability** â getting consistent results from honest responders
- **Bias detection** â catching response patterns that distort results
- **Dimensional richness** â not just a label but a profile
- **Actionability** â results that tell you something you can do with

Investigate assessments DO:
- Use reverse-scored items (acquiescence bias prevention)
- Include consistency pairs (same construct, different framing)
- Use embedded attention checks
- Include social desirability detection items
- Generate severity calibration where applicable
- Provide specific recommendations
- Include "when to seek support" thresholds where relevant

**Investigate Question Parameters:**
- 20â50 questions depending on construct complexity
- Mix of Likert scale (1â5 or 1â7), yes/no, and scenario-based
- Validity check items embedded at strategic positions
- Completion target: 8â15 minutes
- Reading level: clear but not dumbed down
- Result: multi-dimensional profile, severity calibration, specific recommendations

---

## Part II: JSON Schema Specification

### Question Object Schema

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AssessmentQuestion",
  "type": "object",
  "required": ["id", "text", "type", "mode"],
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique question identifier (e.g., 'POL-D-01', 'EMO-I-23')"
    },
    "text": {
      "type": "string",
      "description": "The question or prompt text shown to user"
    },
    "type": {
      "type": "string",
      "enum": ["multiple_choice", "likert_5", "likert_7", "yes_no", "scenario", "ranking", "free_text"],
      "description": "Response format type"
    },
    "mode": {
      "type": "string",
      "enum": ["discover", "investigate", "both"],
      "description": "Which mode(s) this question appears in"
    },
    "options": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["value", "label"],
        "properties": {
          "value": { "type": ["string", "number"] },
          "label": { "type": "string" },
          "axis_scores": {
            "type": "object",
            "description": "For multi-axis assessments: maps axis name to score contribution",
            "additionalProperties": { "type": "number" }
          }
        }
      }
    },
    "scoring": {
      "type": "object",
      "properties": {
        "dimension": { "type": "string", "description": "Which scoring dimension this contributes to" },
        "weight": { "type": "number", "default": 1.0 },
        "reverse_scored": { "type": "boolean", "default": false, "description": "If true, invert score for acquiescence bias correction" },
        "validity_role": {
          "type": "string",
          "enum": ["normal", "attention_check", "consistency_pair_a", "consistency_pair_b", "social_desirability"],
          "default": "normal"
        },
        "consistency_pair_id": {
          "type": "string",
          "description": "ID of the paired question for consistency checking"
        }
      }
    },
    "attention_check_answer": {
      "type": ["string", "number"],
      "description": "For attention_check items: the correct expected answer value"
    },
    "flags": {
      "type": "object",
      "properties": {
        "escalation_item": { 
          "type": "boolean", 
          "default": false,
          "description": "High score triggers severity escalation"
        },
        "severity_weight": {
          "type": "number",
          "description": "Multiplier for this item in severity calculation (default 1.0)"
        }
      }
    }
  }
}
```

### Assessment Object Schema

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Assessment",
  "type": "object",
  "required": ["id", "title", "modes"],
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string" },
    "section": { "type": "string" },
    "description": { "type": "string" },
    "modes": {
      "type": "object",
      "properties": {
        "discover": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "question_ids": { "type": "array", "items": { "type": "string" } },
            "estimated_minutes": { "type": "number" },
            "scoring_algorithm": { "type": "string", "enum": ["axis_map", "sum", "max_axis", "categorical"] },
            "result_categories": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": { "type": "string" },
                  "label": { "type": "string" },
                  "description": { "type": "string" },
                  "follow_up_question": { "type": "string" }
                }
              }
            }
          }
        },
        "investigate": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "question_ids": { "type": "array", "items": { "type": "string" } },
            "estimated_minutes": { "type": "number" },
            "validity_thresholds": {
              "type": "object",
              "properties": {
                "attention_checks_required": { "type": "number" },
                "consistency_tolerance": { "type": "number", "description": "Max allowed delta between consistency pairs (0-4 scale)"},
                "social_desirability_flag_threshold": { "type": "number", "description": "Score above this suggests elevated impression management" }
              }
            },
            "scoring_algorithm": { "type": "string" },
            "severity_calibration": {
              "type": "object",
              "properties": {
                "applies": { "type": "boolean" },
                "light_threshold": { "type": "number" },
                "moderate_threshold": { "type": "number" },
                "severe_threshold": { "type": "number" },
                "seek_help_threshold": { "type": "number" }
              }
            }
          }
        }
      }
    }
  }
}
```

### Validity Check Result Schema

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ValidityReport",
  "type": "object",
  "properties": {
    "overall_valid": { "type": "boolean" },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "flags": {
      "type": "object",
      "properties": {
        "failed_attention_checks": {
          "type": "array",
          "items": { "type": "string", "description": "Question IDs of failed attention checks" }
        },
        "inconsistent_pairs": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "pair_id": { "type": "string" },
              "question_a": { "type": "string" },
              "question_b": { "type": "string" },
              "delta": { "type": "number" },
              "threshold": { "type": "number" }
            }
          }
        },
        "acquiescence_bias_detected": { "type": "boolean" },
        "social_desirability_elevated": { "type": "boolean" },
        "social_desirability_score": { "type": "number" }
      }
    },
    "recommendation": {
      "type": "string",
      "enum": ["use_results", "interpret_with_caution", "retake_recommended"],
      "description": "What to do with this response set"
    }
  }
}
```

---

## Part III: Scoring Algorithms

### Algorithm 1: Axis Mapping (Multi-Dimensional Assessments)

Used for: Political Identity Compass, Cultural Identity Mapping, Cognitive Style Profile

```
For each question Q with answer value V:
  For each axis A in Q.options[V].axis_scores:
    axis_totals[A] += Q.options[V].axis_scores[A] * Q.scoring.weight

For each axis A:
  axis_position[A] = axis_totals[A] / axis_question_count[A]
  // Normalized to range [-1, 1] where -1 = one pole, +1 = other pole
  axis_normalized[A] = (axis_position[A] - axis_min) / (axis_max - axis_min) * 2 - 1

Result: Vector of axis positions
```

### Algorithm 2: Sum with Reverse Scoring (Likert-Based Assessments)

Used for: Emotional Landscape, Worldview Profile, Ancestral Echoes

```
For each question Q with answer value V:
  effective_score = Q.scoring.reverse_scored ? (max_scale + 1 - V) : V
  dimension_totals[Q.scoring.dimension] += effective_score * Q.scoring.weight

For each dimension D:
  dimension_score[D] = dimension_totals[D] / dimension_question_count[D]

Total score = sum(dimension_scores)
Normalized total = (total - min_possible) / (max_possible - min_possible) * 100
```

### Algorithm 3: Categorical Resonance (Dialect/Accent, Aesthetic Identity)

Used for: Dialect & Accent Origin, Aesthetic Identity

```
For each question Q with answer value V:
  For each category C in V.category_weights:
    category_votes[C] += V.category_weights[C]

Sort categories by total votes descending
Primary result = category with highest votes
Secondary result = category with second-highest votes (if within threshold)
Confidence = primary_votes / total_possible_votes
```

### Algorithm 4: Profile Clustering (Communication DNA, Cognitive Style)

Used for: Communication DNA, Cognitive Style Profile

```
For each dimension D:
  score[D] = normalized score 0-100

// Find dominant style
primary_dimension = argmax(score)
secondary_dimension = argmax(score excluding primary)

// Cluster assignment
If score[primary] > 65: "Strong [primary]"
Elif score[primary] > 50: "Moderate [primary] with [secondary] tendencies"
Else: "Mixed style â [primary] and [secondary] in balance"
```

---

## Part IV: Validity Check Placement Strategy

### Placement Principles

Validity checks must feel natural â embedded, not obvious. A user who notices they're being tested for honesty will feel surveilled, which distorts results. The goal is to make validity checks *disappear into* the assessment.

**Attention Checks:**
- Place at questions 8â12 and questions 25â30 in Investigate mode
- Frame as simple, clear instructions masquerading as questions
- Example: "For this item, please select 'Somewhat Agree'" [framed as a formatting question]
- Use 2 attention checks per assessment; flagging requires failing both

**Reverse-Scored Items:**
- Intersperse at minimum 1 in every 5 questions
- Cluster near middle, not at end (end-of-test fatigue affects all items equally)
- Flip the *phrasing*, not just the *polarity* â "I rarely feel understood" vs "I feel understood often" reads differently than just inverting the scale

**Consistency Pairs:**
- 2â4 pairs per Investigate assessment
- Pairs should be spaced 8â15 questions apart
- Flag if delta > 2 points on a 5-point scale (suggests random responding or misreading)
- Common pattern: concrete behavioral item + abstract belief item measuring same construct
- "I often find myself doing X" paired with "X is something I value" (different framings)

**Social Desirability Detection:**
- 3â5 items that measure a "too-good" response pattern
- Example: "I have never said something unkind about another person" â virtually no honest person answers True
- High score on social desirability items â  invalid; it means *interpret emotional/social results with caution*
- The flag is "this person may be presenting an idealized self-image"

### Validity Flag Response Matrix

| Flags Present | Recommendation | User Message |
| --- | --- | --- |
| None | Use results | Results shown normally |
| 1 attention check failed | Interpret with caution | "We noticed one response that seemed inconsistent â results are still shown but may not fully reflect you." |
| 2 attention checks failed | Retake recommended | "Some responses seemed inconsistent. For the most accurate results, we recommend retaking." |
| 2+ inconsistent pairs | Interpret with caution | "A few questions that should have similar answers looked quite different. This sometimes happens when we're answering quickly or our feelings are complicated." |
| Social desirability elevated | Interpret with caution (specific) | "Your results look very polished â which is great! But the most useful insights often come when we include our shadow sides too." |
| Multiple flags | Retake recommended | Full message explaining what was noticed |

---

## Part V: Severity Calibration

### When Severity Applies

Not all assessments require severity calibration. Self-discovery assessments about aesthetic preference or political orientation don't have a "severe" outcome. But some constructs â emotional landscape, life season, worldview â carry genuine weight, and acknowledging that matters.

**Severity applies when:** The construct being measured connects to wellbeing, distress, or the potential need for external support.

**Severity does NOT apply when:** The construct is purely descriptive or preferential (aesthetics, dialect, communication style).

### The Light / Moderate / Severe / Seek Help Framework

```
LIGHT (0â40% of max score on relevant items):
  â "This is part of the texture of being human."
  â No action recommended beyond reflection
  â Acknowledge the experience without pathologizing

MODERATE (41â65%):
  â "This is worth paying attention to."
  â Offer concrete self-care or reflection suggestions
  â May offer resources for further exploration

SEVERE (66â80%):
  â "This is significantly affecting your life."
  â Strong recommendation to discuss with a trusted person
  â Offer crisis-adjacent resources if applicable

SEEK HELP (81%+):
  â "Please don't navigate this alone."
  â Direct language about professional support
  â Include specific resource types (therapist, counselor, etc.)
  â Never gatekeep â anyone at any level can seek support
```

### Escalation Items

Some individual items carry more weight than the raw score suggests. Certain responses should *always* trigger an elevated flag regardless of overall score:

* Any response indicating active harm to self or others
* Any response indicating severe disconnection from reality
* Any response indicating acute crisis

These items are flagged with `escalation_item: true` and carry a `severity_weight` multiplier of 2.0â3.0 in the severity calculation.

---

## Part VI: Results Presentation Templates

### Discover Results Template

```
ââââââââââââââââââââââââââââ
ð YOUR [ASSESSMENT NAME] RESULT
ââââââââââââââââââââââââââââ

You are: **[RESULT LABEL]**

[2-3 sentence evocative description. Not clinical. Not diagnostic. 
Something that feels like it *sees* the person.]

What this means: [One specific, concrete observation]

Something to sit with: [A question, not an answer]

ââââââââââââââââââââââââââââ
Want to go deeper? Take the Investigate version
for a more complete picture. â [link]
```

### Investigate Results Template

```
ââââââââââââââââââââââââââââ
ð¬ YOUR [ASSESSMENT NAME] PROFILE
ââââââââââââââââââââââââââââ

[If validity flags present, show validity notice here]

YOUR PROFILE:
â¢ [Dimension 1]: [score/descriptor] â [1 sentence meaning]
â¢ [Dimension 2]: [score/descriptor] â [1 sentence meaning]
â¢ [Dimension N]: [score/descriptor] â [1 sentence meaning]

WHAT STANDS OUT:
[2-3 sentences highlighting the most distinctive features
of this specific result â not generic, not boilerplate]

PATTERNS TO NOTICE:
[What this combination means â the emergent picture from 
all dimensions together]

[IF SEVERITY APPLIES:]
ââââââââââââââââââââââââââââ
WELLBEING NOTE:
[Calibrated to severity level. See severity templates above.]
ââââââââââââââââââââââââââââ

THINGS TO EXPLORE:
â¢ [Specific, actionable reflection prompt 1]
â¢ [Specific, actionable reflection prompt 2]
â¢ [Resource or next step if applicable]

WHAT THIS DOESN'T TELL YOU:
[Honest acknowledgment of limits â what this assessment 
can't measure, what to weight more or less heavily]
```

---

## Part VII: Implementation Guidelines for Bot/App Development

### Session Architecture

Each assessment session needs to track:

```
{
  "session_id": "uuid",
  "user_id": "anonymous_or_hashed",
  "assessment_id": "string",
  "mode": "discover | investigate",
  "started_at": "timestamp",
  "responses": {
    "question_id": { "value": "answer", "timestamp": "timestamp", "duration_ms": "number" }
  },
  "validity_report": "ValidityReport object",
  "result": "computed on completion",
  "completed": false
}
```

### Response Time Tracking

Response time per question is worth tracking (but not surfacing to the user). Very fast responses (<500ms) may indicate random clicking. Very slow responses on attention checks may indicate re-reading the instructions â not a flag, but context for interpreting attention check failures.

### Dropout Points

Track question ID at session abandonment. Consistent dropout at specific questions signals:
- The question is confusing (rewrite)
- The question is too personal (reorder or add opt-out)
- The assessment is too long (consider truncation)

### Progressive Disclosure

Never show all 40 questions at once. Present one question at a time. Show progress indicator but not question numbers (question numbers encourage skipping ahead or back-filling for consistency).

### The "Want to Go Deeper?" Bridge

Every Discover result screen must offer the Investigate path. The bridge message should reference the specific result: "You got [LABEL] â the Investigate version can tell you which specific [dimensions] drive this, and where there's more complexity." Generic CTAs convert worse than specific ones.

### Accessibility Considerations

* All options available as keyboard-navigable choices
* Likert scales must have labeled poles, not just numbers
* Multiple choice options must be readable without inference from surrounding context
* Color should never be the only differentiator in results visualization

---

## Part VIII: Assessment Catalog Index

The following assessments are defined in `self-discovery-suite.md`:

| ID | Title | Mode | Dimensions | Severity |
| --- | --- | --- | --- | --- |
| POL | Political Identity Compass | Both | 6 axes | No |
| DIA | Dialect & Accent Origin | Both | Regional mapping | No |
| CUL | Cultural Identity Mapping | Both | 6 dimensions | No |
| AES | Aesthetic Identity | Both | 5 domains | No |
| COG | Cognitive Style Profile | Both | 4 dimensions | No |
| EMO | Emotional Landscape | Both | 5 dimensions | Yes |
| LIFE | Life Season Assessment | Both | 5 dimensions | Light |
| WORLD | Worldview Profile | Both | 6 axes | Light |
| COMM | Communication DNA | Both | 5 styles | No |
| ANCS | Ancestral Echoes | Both | 4 dimensions | Light |

---

*Framework Version 1.0 | The Observatory Almanac, Section XI*
*This document is a living specification. Update version number on any schema changes.*