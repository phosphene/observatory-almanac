# Statistical Literacy

*How to read data, spot manipulation, and think more clearly about numbers in the wild.*

---

## Correlation vs. Causation

The most repeated concept in statistics, and the most frequently ignored in headlines.

**Correlation** means two variables tend to move together. When ice cream sales rise, so do drowning rates. When per-capita cheese consumption increases, so do deaths by bedsheet tangling. These relationships are real statistical correlations. They are also completely meaningless as causal claims.

**Causation** means one thing actually produces another â changing A changes B. This is much harder to establish.

### Why Correlation Is Not Causation

Three alternative explanations always exist for any correlation:

1. **Reverse causation:** Maybe B causes A, not A causes B. Low self-esteem correlates with depression â but does low self-esteem cause depression, or does depression reduce self-esteem? Both directions may be true.
2. **Confounding variable (lurking variable):** A third variable C causes both A and B independently. Ice cream and drownings are both caused by hot weather (people buy ice cream AND people swim when it's hot). Remove the confounder and the correlation disappears.
3. **Coincidence:** Especially in large datasets, spurious correlations appear by chance. Nicholas Cage films per year correlates with swimming pool drownings. This is statistical noise mistaken for signal.

### What Establishes Causation

* **Randomized controlled trial (RCT):** Randomly assign subjects to treatment vs. control. Random assignment neutralizes confounders. The gold standard.
* **Temporal precedence:** A must come before B for A to cause B.
* **Plausible mechanism:** There must be a biologically or mechanically sensible explanation.
* **Dose-response relationship:** More exposure = more effect (suggests real mechanism).
* **Replication:** Multiple independent studies reach the same conclusion.

### In Practice

When you see "X linked to Y" in a headline, ask: Is there a plausible mechanism? Is this observational data or a trial? What are the confounders? Usually the study itself is far more cautious than the headline.

---

## Sample Size

The number of subjects in a study determines how much random variation can distort results.

**Small samples amplify noise.** If you flip a coin 10 times and get 7 heads, you might conclude the coin is biased. Flip it 10,000 times and 70% heads would be extraordinary evidence of bias â but 7/10 is just random variation.

### Why Sample Size Matters

With a small sample, extreme results occur by chance. A cancer cluster in a county with 1,200 people might be 6 cases vs. an expected 3 â alarming, but statistically indistinguishable from chance variation. A county with 120,000 people showing the same doubled rate is much stronger evidence.

**The Law of Large Numbers:** As sample size increases, the sample average converges to the true population average. Small samples are uncertain; large samples are more reliable.

### What "Large Enough" Means

Depends on the effect size you're trying to detect:
- Detecting a large effect (a drug that cuts mortality in half): you need a few hundred subjects
- Detecting a small effect (a 5% reduction in risk): you may need thousands or tens of thousands
- Detecting very small effects reliably: you need massive samples

**Power analysis** is the calculation researchers use to determine how many subjects they need before running a study.

### The Problem of Underpowered Studies

A study too small to reliably detect an effect produces misleading results:
- A real effect may appear absent (false negative)
- The effects that ARE detected are often exaggerated (winner's curse / publication bias)
- Results are unstable â small replication studies often fail

A study with 30 subjects proving a drug works should be taken much less seriously than a trial with 30,000 subjects.

---

## P-Values, Simply

The p-value is the probability of seeing results as extreme as these (or more extreme) if there were truly no effect.

**It is not:** The probability the hypothesis is true. Not the probability the results happened by chance. Not a measure of importance or effect size.

**A p-value of 0.05** means: if there were truly no effect, there's a 5% chance of seeing results this extreme just due to random variation. It's a threshold, not a fact.

### The Problems With P-Values in Practice

**The 0.05 cutoff is arbitrary.** Ronald Fisher proposed it in 1925 as a loose rule of thumb. It became the universal threshold for "significant" and is now the source of enormous scientific problems.

**P-hacking:** If you run enough comparisons, some will be significant by chance. Run 20 comparisons and one will achieve p < 0.05 just by luck. Researchers who keep collecting data until they hit significance, or who only report the significant result from many analyses, are exploiting this.

**Statistical significance â  practical significance.** A drug that reduces blood pressure by 1 mm Hg might achieve p < 0.0001 in a 50,000-person trial. The finding is statistically robust â and clinically irrelevant. Always ask: what is the effect size?

**What to ask instead:**
- What is the effect size (how big is the effect)?
- What are the confidence intervals (what range is plausible)?
- Has this been replicated independently?
- Was the study pre-registered?

---

## Survivorship Bias

During World War II, analysts were asked which parts of returning bombers should be reinforced â the wings, engines, or fuselage. They counted bullet holes in returning planes and proposed reinforcing the areas with the most damage. Statistician Abraham Wald pointed out the error: they should reinforce the areas with the least damage â because the planes hit there didn't survive to return.

**Survivorship bias occurs when you study only the survivors, missing the lessons in the failures.**

### Everyday Examples

**Successful entrepreneurs:** We study successful startups and conclude that dropouts who take big risks succeed. But we don't see the hundreds of thousands of dropouts who took risks and failed in obscurity.

**Investment funds:** Average returns reported by funds look good, but funds that perform badly are quietly shut down and removed from the average. The graveyard of failed funds is invisible.

**"They don't make things like they used to":** Old things that lasted long enough to still exist are the ones built well. The poorly-made ones were thrown away decades ago.

**Medical treatments before modern trials:** Patients who recovered were visible; those who died after the treatment, less so â creating false impressions of efficacy.

### Spotting It

Ask: What happened to the things that are not in this data? Is there a selection process that determines who or what appears in the sample? Are failures, dropouts, or closed cases excluded?

---

## Simpson's Paradox

A trend that appears in combined data can reverse when the data is separated into subgroups.

**Classic example:** A university was accused of gender bias in graduate school admissions. The overall acceptance rate for women was lower than for men. But when examined department by department, women had equal or higher acceptance rates than men in nearly every department.

The resolution: Women applied in higher proportions to competitive departments (low acceptance rate), while men applied in higher proportions to less competitive departments (high acceptance rate). Pooling the data created a misleading aggregate pattern.

**Medical example:** Treatment A appears better than Treatment B in combined data. But among mild cases, B is better. Among severe cases, B is better. The aggregate reversal happens because Treatment A was more often used for mild cases (which have better outcomes regardless of treatment).

### Why It Matters

* Comparative statistics across groups require controlling for the groups
* Aggregate data can actively mislead; always ask whether subgroup analysis changes the picture
* "Overall" statistics hide distribution across populations

---

## Misleading Graphs

Visual representations of data are powerful â and easily manipulated.

### Truncated Axes

The most common graph manipulation: the Y-axis doesn't start at zero.

A stock price rises from $98 to $102 over a month. On a chart from $95 to $105, this looks like explosive growth â a dramatic upward line. On a chart from $0 to $200, it looks flat. The data is identical; the impression is opposite.

**When truncated axes are legitimate:** When zero is irrelevant (e.g., body temperature changes of 0.5Â°F matter clinically; a chart from 0 to 110Â°F would hide the signal). The key is whether truncation illuminates or deceives.

**How to spot it:** Always look at the Y-axis starting value. If it doesn't start at zero, ask whether the visual slope accurately represents the magnitude of change.

### Cherry-Picked Time Frames

Any investment, policy, or trend can look good or bad depending on where you start and end the graph.

A mutual fund shows strong 5-year returns â but starting the chart from just before a crash in year 0. A crime rate "declining" since 2010 â but starting the chart at the 2008 peak.

**How to spot it:** Ask why this particular time frame was chosen. What does a longer or shorter view show?

### Other Common Graph Problems

* **Dual Y-axes:** Two scales on the same chart can make any two unrelated trends look correlated
* **3D pie charts:** The tilt exaggerates front slices
* **Area vs. linear scales:** Using area (circles or squares) to represent quantities â a circle with twice the area looks much larger than twice the linear size because our eye responds to area
* **Inconsistent intervals:** Irregular spacing on the X-axis that compresses or expands time

---

## Absolute vs. Relative Risk

This distinction is crucial for evaluating health news.

**Relative risk** describes the change as a proportion of the original risk.  
**Absolute risk** describes the actual change in probability.

**Example:** A medication reduces the risk of a disease from 2% to 1%.
- Relative risk reduction: 50% (1 is 50% of 2)
- Absolute risk reduction: 1 percentage point (2% minus 1%)
- Number needed to treat (NNT): 100 people must take the drug to prevent 1 case

The headline "Drug cuts disease risk by 50%!" is technically accurate. But if the baseline risk is 2%, the absolute benefit is tiny â 1 in 100 people benefit. The other 99 get the cost and side effects with no benefit.

**Why this matters:**
- Headlines almost always use relative risk (sounds bigger)
- Informed decisions require absolute risk
- Low baseline risk means even large relative reductions are small in absolute terms

**Always ask:** What is the baseline risk? What is the absolute change?

---

## Bayesian Thinking

The core idea: new evidence should update our existing beliefs proportionally, not override them entirely or be ignored.

**Bayes' theorem** tells us how to combine prior probability (what we thought before) with new evidence to get updated probability (what we should think now).

### The Medical Test Paradox (False Positive Paradox)

Imagine a test for a disease that affects 1% of the population. The test is 95% accurate: it correctly identifies 95% of sick people (sensitivity) and correctly rules out 95% of healthy people (specificity).

You test positive. What's the probability you actually have the disease?

Most people guess 95%. The actual answer is about 16%.

**The math:**
- 1,000 people tested
- 10 actually have the disease (1%)
- Of those 10: test correctly identifies 9.5 (sensitivity 95%) â 10 positive tests
- Of the 990 healthy people: 95% correctly test negative, but 5% (about 50) test falsely positive
- Total positive tests: approximately 60
- True positives among those: 10
- Probability of disease given positive test: 10/60 â 16%

The base rate (1% prevalence) dominates. When a disease is rare, even an accurate test produces mostly false positives because the healthy pool is so large.

**Real-world implications:**
- Screening programs for rare conditions produce many false positives
- This is why screening is not recommended for ultra-rare diseases in general populations
- This is why a positive test result on a rare condition warrants a confirmatory test

### Everyday Bayesian Thinking

* Start with prior probabilities (base rates matter)
* Update proportionally when new evidence arrives
* Extraordinary claims require extraordinary evidence (high prior improbability requires very strong evidence to overcome)
* One study doesn't overturn established science â the prior is very strong

---

## How Polls Work

A properly conducted poll doesn't ask everyone â it asks a carefully selected sample and infers the population.

### Key Concepts

**Sample size and margin of error:** A well-designed random sample of ~1,000 people yields a margin of error of roughly Â±3 percentage points (at 95% confidence). Adding more people helps at first, but the benefit decreases â going from 1,000 to 10,000 people cuts the margin of error in half, not by ten. Going from 1,000 to 1,500 barely helps.

**The margin of error only covers random sampling error** â not bias, question wording effects, or non-response issues. The stated Â±3% does not include these other sources of error.

**95% confidence interval:** If you ran the same poll 100 times with different random samples, 95 of those polls' results would fall within the stated margin of error of the true value. This means 5 out of 100 polls are simply wrong even with perfect methodology.

### What Pollsters Get Wrong (The Real Problems)

**Non-response bias:** If certain types of people are less likely to complete surveys, the sample is systematically off. People who answer polls differ from those who don't.

**Likely voter models:** Predicting who will actually vote is extremely difficult. Pollsters make assumptions about turnout that may be wrong.

**Social desirability bias:** People sometimes give answers they think are socially acceptable rather than their true opinion.

**Question wording:** "Do you support giving free health care to illegal immigrants?" vs. "Do you support providing emergency medical treatment to undocumented workers?" may get very different responses to essentially the same policy question.

**Cell phone era problems:** Traditional random-digit-dial sampling assumed everyone had a landline. Modern polling requires expensive weighting corrections.

### What Poll Results Mean

A poll showing Candidate A at 48% and Candidate B at 46% with Â±3% margin of error does NOT mean A is winning. The difference (2 points) is within the margin of error â it's statistically a toss-up. The poll only meaningfully distinguishes candidates if the gap exceeds roughly twice the margin of error.

---

## Medical Test Accuracy: Sensitivity, Specificity, and the False Positive Paradox

These three concepts are essential for understanding any diagnostic test.

**Sensitivity** (true positive rate): Of all people who actually have the disease, what proportion does the test correctly identify as positive? A highly sensitive test misses few cases (low false negative rate). Good for ruling out a disease â a negative result on a sensitive test is reassuring.

**Specificity** (true negative rate): Of all people who don't have the disease, what proportion does the test correctly identify as negative? A highly specific test rarely falsely alarms (low false positive rate). Good for ruling in a disease â a positive result on a highly specific test is meaningful.

**The trade-off:** Lowering the threshold for a positive test increases sensitivity but decreases specificity (and vice versa). Cancer screening often uses sensitive tests to catch every case, accepting false positives that require follow-up.

**Positive Predictive Value (PPV):** Of all people who test positive, what fraction actually have the disease? This depends on sensitivity, specificity, AND the base rate (prevalence) of the disease.

When disease prevalence is low, even excellent tests have low PPV â producing many false positives for each true positive. This is the false positive paradox described above in the Bayesian section.

**Negative Predictive Value (NPV):** Of all people who test negative, what fraction are truly disease-free? High NPV means a negative result is trustworthy.

### Why This Matters Clinically

* A highly sensitive test used for screening will generate false positives that require follow-up (colonoscopies, biopsies, additional imaging), with associated costs, anxiety, and harms
* A highly specific test is used to confirm a suspected diagnosis
* Understanding PPV requires knowing the prevalence in the population being tested (high-risk populations vs. general population)
* "False positive rate" and "false negative rate" alone are insufficient â the base rate is always required to calculate real-world predictive value

---

## Quick Reference: Common Statistical Mistakes to Spot

| Claim | Question to Ask |
| --- | --- |
| "Linked to" / "associated with" | What's the proposed mechanism? Is this observational? What are the confounders? |
| "Risk increased by X%" | Relative or absolute? What is the baseline risk? |
| "Significant" | Statistically or practically? What is the effect size? |
| "Study shows..." | Sample size? Replicated? Pre-registered? Peer-reviewed? |
| Graph with dramatic trend | Does the Y-axis start at zero? What time frame is shown? |
| "Average" | Mean, median, or mode? Distribution matters. |
| Success story / best practice | Who failed doing the same thing? (Survivorship bias) |
| Dramatic poll result | Sample size? Likely voter model? Margin of error? Question wording? |
| Positive test result | What is the prevalence? What is the PPV? |

---

*Statistical literacy is not about knowing advanced mathematics â it's about asking the right questions before accepting a number as meaningful. Most statistical deception is not malicious; it comes from enthusiasm, motivated reasoning, and the universal human desire for clean stories. The data is almost always messier than the headline.*