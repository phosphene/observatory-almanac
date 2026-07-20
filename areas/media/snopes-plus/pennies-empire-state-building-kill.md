---
title: "A Penny Dropped from the Empire State Building Could Kill Someone"
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
earc_mode: R
gap_category: distorted-but-grounded
snopes_url: https://www.snopes.com/fact-check/pennies-empire-state-building-kill/
snopes_verdict: False
summary: >
  A penny dropped from the Empire State Building's 86th-floor observation deck reaches terminal velocity of roughly 25–40 mph due to its flat, tumbling aerodynamics, delivering an impact equivalent to a flicked coin — painful but not lethal. The myth reveals something important about intuitive physics: humans systematically overestimate the danger of falling objects while underestimating air resistance.
tags:
  - truth-vault
  - physics
  - ballistics
  - terminal-velocity
  - empire-state-building
  - urban-legends
  - air-resistance
---

# A Penny Dropped from the Empire State Building Could Kill Someone

## 1. The Claim

The story is one of the most persistent urban legends in American life: if you drop a penny from the top of the Empire State Building, it will accelerate to such terrifying speed that it could kill a pedestrian on the sidewalk below. Versions of the tale vary — some say the penny would crack the pavement, others that it would embed itself in a person's skull like a bullet. The claim circulates in schoolyard conversations, barroom physics debates, and even the occasional news segment warning tourists about the dangers of throwing coins from skyscrapers.

The myth is grounded in a real intuition. The Empire State Building's 86th-floor observation deck stands approximately 320 metres above street level (the building's roof antenna reaches 443 metres, but public access terminates much lower). That is an enormous drop. And gravity is relentless: in a vacuum, any object falling 320 metres would reach roughly 79 m/s (177 mph) at impact. At that velocity, even a small copper-plated zinc disc weighing 2.5 grams would carry meaningful kinetic energy — on the order of 7.8 joules, comparable to a low-powered air rifle pellet. The leap from "comparable to an air rifle pellet" to "lethal" is short enough that the myth feels plausible.

But there is no vacuum between the 86th floor and Fifth Avenue. There is atmosphere — thick, viscous, sea-level air that the penny must shove aside on its way down. And this is where the myth collapses.

## 2. What's Actually True

The physics of a falling penny is governed by the interplay between gravitational force and aerodynamic drag. The governing equation for terminal velocity is well established in classical fluid dynamics:

> **V_t = √(2mg / ρAC_d)**

where *m* is the object's mass, *g* is gravitational acceleration (9.81 m/s²), *ρ* is the density of air (~1.225 kg/m³ at sea level), *A* is the object's cross-sectional area projected into the airflow, and *C_d* is its drag coefficient — a dimensionless number that captures how "slippery" or "draggy" the shape is.

For a US penny: mass is approximately 2.5 grams (0.0025 kg), diameter is 19.05 mm (cross-sectional area ≈ 2.85 cm² = 2.85 × 10⁻⁴ m²), and — critically — the drag coefficient is high. A flat disc tumbling through air, which is what a penny does when dropped rather than fired, presents a C_d of approximately 1.0–1.2 (Pirie, 1956, *Quarterly Journal of the Royal Meteorological Society*; see also Hyperphysics, Georgia State University, "Terminal Velocity" resource). Using C_d ≈ 1.1 as a reasonable middle estimate for tumbling flat-coin aerodynamics, the terminal velocity calculation yields:

> V_t = √(2 × 0.0025 × 9.81 / (1.225 × 2.85 × 10⁻⁴ × 1.1))
> V_t ≈ √(0.04905 / 3.84 × 10⁻⁴)
> V_t ≈ √(127.7)
> V_t ≈ 11.3 m/s ≈ 25 mph

This is the lower bound for a penny falling perfectly flat. In practice, pennies tumble, flutter, and oscillate between broadside and edge-on orientations, and the instantaneous velocity fluctuates. Randall Munroe calculated a range of roughly 25–50 mph depending on tumbling dynamics in his rigorous treatment of the problem (Munroe, 2014, *What If? Serious Scientific Answers to Absurd Hypothetical Questions*, Houghton Mifflin Harcourt). Louis Bloomfield, a University of Virginia physicist frequently cited in popular treatments, has settled on roughly 25 mph as representative for the tumbling case (Bloomfield, 2007, *How Everything Works: Making Physics Out of the Ordinary*). Adler (1996) provided an accessible summary of such falling-object calculations in *Physics Today*, noting that common small objects reach surprisingly low terminal velocities compared to naive expectations.

The definitive popular test came in 2008. On *MythBusters* Season 6, Episode 10, hosts Adam Savage and Jamie Hyneman constructed an apparatus to fire pennies at terminal-velocity speeds. Adam Savage stood in as the target, allowing pennies accelerated to approximately 64 mph (a generous overestimate of real terminal velocity) to strike his bare skin. He reported a mild sting — comparable, he said, to being flicked. No penetration. No bruise. No injury beyond momentary discomfort. The myth was declared "Busted."

At the kinetic energy level, a 2.5-gram penny at 11 m/s carries roughly 0.15 joules. Even at the more generous 25 m/s (56 mph), the kinetic energy is only about 0.78 joules. For context, a BB gun pellet (0.35 g at 100 m/s) carries approximately 1.75 joules, and even BB guns rarely cause lethal injuries except through extraordinarily unlikely circumstances such as direct ocular penetration. The penny's energy is below the threshold commonly associated with skin penetration in ballistic wound literature (approximately 1.4 J/mm² of cross-sectional area for pointed projectiles; the penny's flat face distributes its meagre energy across a 285 mm² contact patch, yielding an areal energy density roughly 1,000 times too low for penetration).

The penny would not kill you. It would sting. You might say "ow." Life would continue.

## 3. Why Human Intuition Fails at Air Resistance

The penny myth is not merely a physics error. It is a *diagnostic* physics error — one that reveals a systematic failure mode in human intuitive reasoning about the physical world that has deep evolutionary roots.

### Ballistic Intuition vs. Aerodynamic Reality

Humans possess what cognitive scientists call "intuitive physics" — a set of implicit expectations about how objects move, fall, collide, and interact. This system is generally functional: we can catch balls, dodge thrown objects, and judge whether a falling branch will hit us. But research has established that intuitive physics is riddled with systematic errors, particularly around projectile motion and the behaviour of objects under complex force regimes.

McCloskey (1983) demonstrated in a landmark *Scientific American* article that many adults hold an implicit "impetus theory" of motion — the medieval belief that a moving object carries an internal force that gradually dissipates. When asked to predict the trajectory of a ball emerging from a curved tube, a majority of participants drew curved paths rather than the straight tangential exit that Newtonian mechanics predicts. Caramazza, McCloskey, and Green (1981) extended these findings in *Cognition*, showing that naive theories of motion are not random errors but structured misconceptions that parallel pre-Newtonian physics in predictable ways.

The penny myth is a specific instance of a broader pattern: **humans systematically neglect air resistance in their intuitive physics**. This neglect is not stupid — it is *adaptive*. The objects that mattered in our evolutionary environment were dense: rocks, spears, arrows, falling tree limbs, animal bodies. For these objects, air resistance is a secondary correction. A thrown spear, a hurled rock, a falling coconut — these are all dense enough that their trajectories are dominated by gravity, with drag as a minor perturbation. Our intuitive physics engine was calibrated by millions of years of feedback from dense-projectile environments, and within that domain it performs respectably.

But the penny is not a rock. It is a thin, flat, lightweight disc — aerodynamically, it is closer to a leaf or a dandelion seed than to a bullet. The crucial insight is that **drag force scales with cross-sectional area while gravitational force scales with mass** — and the ratio of area to mass is the key parameter that determines how much drag matters. For dense, compact objects (bullets, rocks, bowling balls), the mass-to-area ratio is high, drag is secondary, and intuitive physics gives roughly correct predictions. For light, flat objects (pennies, leaves, feathers, snowflakes), the mass-to-area ratio is low, drag dominates, and intuitive physics fails catastrophically.

This is the distinction between what we might call **ballistic intuition** and **aerodynamic reality**. Ballistic intuition is the evolved heuristic: heavy things fall fast, higher means faster at the bottom, bigger drop equals more danger. Aerodynamic reality is the full physics: terminal velocity depends on the *ratio* of gravitational to drag forces, and for objects with poor aerodynamic profiles and low mass, terminal velocity can be remarkably low.

Consider the comparison that makes this vivid. A bowling ball (6.8 kg, ~22 cm diameter, roughly spherical with C_d ≈ 0.47) dropped from the Empire State Building would reach a terminal velocity of approximately 72 m/s (161 mph) and deliver around 17,600 joules at impact — unambiguously lethal, roughly equivalent to being hit by a car at highway speed. Our intuitive physics correctly identifies the bowling ball as deadly. But when we scale our intuition down to the penny, we preserve the "deadly at that height" conclusion while ignoring the fact that the penny's mass-to-area ratio is roughly 75 times worse than the bowling ball's. The drag-to-weight ratio is completely different. The penny reaches terminal velocity in about 15 metres of fall — the remaining 305 metres of drop are aerodynamically irrelevant. It would hit the ground at approximately the same speed whether dropped from the Empire State Building or from a 50-foot highway overpass.

### The Evolutionary Calibration Gap

Hegarty (2004) argued in *Psychological Review* that mechanical reasoning relies on a combination of mental simulation (running a simplified "physics engine" in one's head) and analytic knowledge. The critical finding is that mental simulation operates on simplified models — models from which dissipative forces like friction and drag are often absent, because they add computational complexity that was rarely worth the metabolic cost in ancestral environments.

This creates what we can call an **evolutionary calibration gap**: our intuitive physics was never calibrated for extremely light objects falling great distances, because such scenarios had no fitness consequences in ancestral environments. No early human needed to predict whether a pebble or seed pod dropped from a cliff face would be dangerous at the bottom — the answer was always "probably not, and who cares." The scenarios that *did* matter — rockfalls, falling predators, dropped tools — involved objects dense enough that intuitive physics got the right qualitative answer.

The penny myth, then, is not a failure of human intelligence. It is an *artefact of evolutionary mismatch*: a modern question (what happens to a manufactured coin in a 320-metre urban canyon?) posed to a cognitive system optimised for ancestral questions (will that falling rock hurt me?). The system gives a confidently wrong answer because it was never designed to handle the relevant parameter regime.

This pattern — intuitive physics errors clustering around phenomena where evolution provided no calibrating feedback — extends well beyond pennies. Humans also systematically misjudge the behaviour of spinning objects (the gyroscopic precession of a bicycle wheel surprises even physics students), the trajectories of objects in rotating reference frames (Coriolis effects are deeply counterintuitive), and the dynamics of fluids (turbulence, Bernoulli effects, and viscous flow all defeat naive expectation). In each case, the failure occurs precisely where ancestral experience provided no feedback loop to correct the error.

## 4. Verdict

**Propositional Status:** FALSE. A penny dropped from the Empire State Building cannot kill a pedestrian. Its terminal velocity (~25–40 mph) and kinetic energy (~0.15–0.78 J) are far below the thresholds required for lethal injury. The penny's flat, tumbling aerodynamics ensure that drag forces dominate gravitational acceleration within the first few seconds of fall.

**Confidence:** Very High (0.97). The underlying physics is elementary and uncontested. Multiple independent analyses — theoretical calculations (Hyperphysics, Georgia State University; Munroe, 2014), popular experimental demonstration (*MythBusters*, 2008), and professional physics education literature (Bloomfield, 2007; Adler, 1996) — converge on the same conclusion. No credible counter-analysis exists.

**Epistemic Basis:** Theoretical calculation from classical fluid dynamics, confirmed by direct experimental test. The governing equations involve no contested parameters; all values (penny mass, area, air density, drag coefficient for tumbling discs) are well-characterised in the engineering and meteorological literature (Pirie, 1956; standard drag coefficient tables).

**Phenomenological Status:** The myth captures a *real* phenomenological intuition — that height equals danger for falling objects — but misapplies it to an object whose aerodynamic profile renders height irrelevant beyond the first ~15 metres of fall. The experience of standing atop a skyscraper and feeling the vertiginous sense that objects dropped from such heights must be devastating is genuine and nearly universal; the error lies in scaling this feeling to an object whose physics do not cooperate.

**Mechanistic Status:** Fully explained. The mechanism of refutation is the dominance of aerodynamic drag over gravitational acceleration for low-mass, high-drag objects. Terminal velocity is reached quickly, and the terminal velocity itself is low. No mysterious or contested physics is involved.

**Folk Wisdom Value:** Low for the specific claim (a penny is not dangerous), but **moderate-to-high as a diagnostic tool**. The myth is pedagogically valuable precisely *because* it is wrong in an instructive way. It reveals the structure of intuitive physics errors — specifically, the systematic neglect of air resistance — and provides a concrete, memorable example that physics educators have used for decades to teach drag, terminal velocity, and the limits of naive reasoning. The myth's persistence is itself data about human cognition.

## 5. The Wider Picture

The penny myth belongs to a broad family of urban legends about the hidden dangers of mundane objects at extreme scales — a genre one might call "danger scaling myths." These share a common logical structure: take something ordinary (a penny, a grain of rice, a drop of water), place it in an extraordinary situation (extreme height, extreme quantity, extreme velocity), and assert that the result is lethal or catastrophic.

Some of these scaling myths are true: a grain of dust at 99.9% the speed of light genuinely would be devastating. Others, like the penny, fail because they neglect the physical mechanisms that govern the transition from ordinary to extraordinary. The penny myth specifically fails at the aerodynamic transition — the point where drag becomes the dominant force.

The broader lesson is epistemological. When evaluating claims about physical phenomena — particularly claims that extrapolate from everyday experience to extreme conditions — it is essential to ask: *which forces dominate in the regime being described?* In everyday experience, gravity tends to dominate over drag. In the regime described by the penny myth, drag dominates over gravity. The qualitative behaviour of the system flips. Any reasoning that fails to account for this regime change will produce confident, intuitive, and completely wrong answers.

This principle applies far beyond coins and buildings. Climate science, epidemiology, nuclear physics, and financial modelling all involve parameter regimes where the dominant mechanisms shift — where the forces that matter at one scale become irrelevant at another, and forces that were negligible become overwhelming. The penny myth is, in miniature, a lesson in the danger of linear extrapolation across regime boundaries.

It is also worth noting what the myth gets *right* at the level of moral attitude, even as it gets the physics wrong. The instinct that dropping objects from tall buildings is dangerous and irresponsible is correct — not because pennies are lethal, but because many other objects are. A glass bottle, a toolbox, a piece of construction debris — these denser, more aerodynamically streamlined objects *can* reach dangerous speeds in a 320-metre fall. Construction sites on tall buildings enforce strict protocols about securing tools and materials for exactly this reason. The penny myth overstates the danger of a specific object, but the underlying caution it expresses — "don't drop things from skyscrapers" — is sound safety advice for objects generally.

## 6. How Fact-Checkers Handle It

The penny-from-a-skyscraper claim has been addressed by virtually every major fact-checking outlet and science communication channel. Snopes rated it **False**. *MythBusters* rated it **Busted**. Physics educators from Bloomfield to Munroe have debunked it in detail. The convergence across independent fact-checkers, experimentalists, and educators is complete.

The fact-checking approach to the penny myth illustrates several best practices in science-adjacent debunking:

**Quantitative specificity.** Rather than simply asserting "it's not dangerous," good treatments of the claim provide specific numbers: terminal velocity in m/s and mph, kinetic energy in joules, comparison to known impact thresholds. This transforms the debunking from an argument from authority ("scientists say it's false") into a transparent chain of reasoning that the reader can verify.

**Experimental demonstration.** The *MythBusters* test — firing pennies at a human subject at terminal velocity — provided the kind of visceral, visual evidence that no amount of calculation can match for a general audience. The sight of Adam Savage absorbing penny impacts with nothing worse than a wince is more persuasive to most people than a page of equations.

**Analogical framing.** Effective debunkings of the penny myth use comparisons: "it's like being flicked by a coin," "it's less energy than a BB gun," "it would sting but not bruise." These analogies anchor the abstract physics in embodied, familiar experience — countering the intuitive physics error with a competing intuition drawn from direct personal knowledge.

**Identification of the error mechanism.** The best treatments go beyond "the claim is false" to explain *why* people believe it — identifying the systematic neglect of air resistance as the cognitive root. This transforms the debunking into a lesson about reasoning itself, which has lasting pedagogical value beyond the specific claim.

**Retention of valid concern.** Responsible treatments acknowledge that while a penny is not dangerous, dropping objects from buildings is generally hazardous and should be discouraged. This prevents the debunking from inadvertently licensing reckless behaviour — a concern that fact-checkers must navigate carefully when debunking safety-adjacent myths.

The penny myth is, in many ways, the ideal fact-check. The physics is unambiguous, the experimental evidence is clear, the intuitive error is identifiable and instructive, and the correction leaves the audience better equipped to reason about similar problems in the future. If all misinformation were this clean, fact-checking would be a much simpler profession.

---

*Observatory Almanac · The Truth Vault · CC BY-NC-SA 4.0*
