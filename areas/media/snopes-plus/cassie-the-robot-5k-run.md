---
title: "Cassie the Robot Made History By Completing a 5K Run"
slug: cassie-the-robot-5k-run
snopes_url: https://www.snopes.com/fact-check/cassie-the-robot-5k-run/
snopes_verdict: True
snopes_author: Nur Ibrahim
published: 2026-07-20
updated: 2026-07-20
categories:
  - science
  - robotics
  - technology
tags:
  - cassie
  - bipedal-robot
  - oregon-state-university
  - deep-reinforcement-learning
  - agility-robotics
  - darpa
epistemic_status: EARC-A
knowledge_gap: independent verification of the 53-minute run time by parties other than the OSU team; comparison benchmarks with other bipedal robot outdoor locomotion attempts at comparable distance
---

## §1 — Claim & Verdict

In late July 2021, Oregon State University (OSU) announced that Cassie, a bipedal robot developed by the university's Dynamic Robotics Laboratory, had completed a 5-kilometre run on a single battery charge, untethered, on outdoor terrain (OSU press release, 2021). The feat was completed in 53 minutes. OSU claimed this was the first time a bipedal robot had completed such a run using deep reinforcement learning on outdoor terrain. Snopes published a news article on August 9, 2021 confirming the achievement and providing context on Cassie's development history (Ibrahim, 2021).

Snopes' treatment of the claim is **True** (the article is categorised as a news report rather than a fact-check, reflecting its character as confirmed novel information rather than a rumour requiring debunking). The claim is straightforwardly accurate: OSU's own video documentation, university press materials, and corroborating reporting from TechCrunch and other technology outlets confirm the 5K run. The claim of "first bipedal robot to complete such a run using machine learning on outdoor terrain" is a significant qualifier that the university itself applied, limiting the claim appropriately to a specific combination of conditions: bipedal locomotion, machine learning, outdoor terrain, at this distance.

---

## §2 — Source Tracing & Provenance

Cassie's development history begins with a $1 million grant from the Defense Advanced Research Projects Agency (DARPA) to robotics professor Jonathan Hurst at OSU. The robot was introduced in 2017 and is the product of the Dynamic Robotics Laboratory at OSU's College of Engineering. Hurst also co-founded Agility Robotics, the startup responsible for commercialising the platform, which subsequently developed Digit — an expanded bipedal robot with arms — as the next generation product (Agility Robotics, 2021).

The July 2021 5K milestone was documented by OSU in a press release: "A bipedal robot developed by Oregon State University makes history by learning to run, completing 5K" (OSU, 2021). TechCrunch reported independently on July 27, 2021, confirming the achievement's parameters: 5 kilometres, outdoor terrain, single battery charge, untethered, 53 minutes, deep reinforcement learning algorithm (TechCrunch, 2021). A video released by OSU showed Cassie traversing outdoor paths during the run.

Critically, the OSU team was explicit about the mechanism: Cassie learned to run through deep reinforcement learning — a machine learning paradigm in which an agent learns to perform a task by receiving reward signals for successful actions and penalty signals for failures, iterating across thousands or millions of simulated training episodes until a stable policy emerges. The specific framing was that "the Dynamic Robotics Laboratory students combined expertise from biomechanics and existing robot control approaches with new machine learning tools" (Hurst, quoted in OSU press release, 2021). This interdisciplinary framing — combining biomechanical insight about how animals run with machine learning optimisation — was a key aspect of what made the achievement technically distinctive.

---

## §3 — Epistemic Novelty: Deep Reinforcement Learning for Bipedal Locomotion and the Ostrich Analogy

The epistemic novelty in the Cassie 5K story operates at the intersection of biomechanical engineering, machine learning methodology, and the problem of physically grounded robot control. Cassie's legs are designed to mimic the proportions and joint kinematics of an ostrich: digitigrade gait (walking and running on the toe-equivalent segments), long distal limb segments, and spring-loaded tendons that store and return energy with each stride. The ostrich is the world's fastest running bird and one of the most energetically efficient bipedal runners in nature. Using ostrich morphology as an engineering template reflects a deliberate application of evolutionary optimisation to robot design — a strategy known as "biomimetic" or "biorobotics" design.

However, the mechanical design is only half the achievement. Prior to the application of deep reinforcement learning, controlling bipedal robots typically required hand-coded controllers: engineers specified explicit rules for how the robot should position its joints at each phase of the gait cycle. Such controllers were brittle, requiring significant manual tuning and failing gracefully to perturbations (bumps, uneven terrain) that the engineer had not explicitly anticipated. Deep reinforcement learning offers a fundamentally different paradigm: the robot learns a control policy by trying things, failing, and improving, with the learning algorithm extracting generalised locomotion strategies rather than explicit rules. The result is a controller that has intrinsic robustness to the variability of real-world terrain, because it has been trained — in simulation — on a distribution of such variabilities.

The significance of completing the 5K on outdoor terrain specifically, rather than on a laboratory treadmill or indoor flat surface, is that outdoor terrain contains variability that is difficult to hand-code for. Slight slopes, gravel, soil compaction variation, debris, crosswinds — each of these requires adaptive real-time adjustment that rule-based controllers struggle with. A deep reinforcement learning policy, trained on appropriate simulation environments, can generalise to these variations because the policy learned statistical structure rather than explicit rules. This is a general principle that has been validated across multiple robotics platforms since roughly 2016, when DeepMind's AlphaGo demonstrated the power of deep RL in a non-physical domain, and researchers began applying similar methods to locomotion (Silver, David, et al., "Mastering the game of Go with deep neural networks and tree search," *Nature*, vol. 529, 2016, pp. 484–489; for locomotion specifically: Hejna, Donald, et al., and earlier work by Lillicrap et al. and Schulman et al.).

The 5K distance is also significant as a practical benchmark. Previous bipedal robot locomotion demonstrations had typically covered shorter distances or operated under more controlled conditions. Five kilometres is a distance meaningful to humans as a fitness benchmark (the standard parkrun distance, the minimum qualifying distance for many entry-level running events), and completing it in 53 minutes — approximately a 10:36 per kilometre pace — places Cassie within the range of a slow human recreational runner. The symbolic resonance of the human-scale benchmark is deliberate: it frames the achievement in terms that non-specialist audiences can immediately contextualise, facilitating the kind of broad public dissemination the OSU communications team sought.

Peng, Xue Bin, et al. had published foundational work on deep reinforcement learning for locomotion control demonstrating that physics-based character animation and robot control could be unified under RL frameworks (*ACM Transactions on Graphics*, vol. 37, no. 4, 2018, article 41), part of a surge in academic interest in learning-based locomotion following improvements in simulation fidelity and GPU training infrastructure. Kumar, Ashish, et al., at UC Berkeley working on quadruped robots (RMA: Rapid Motor Adaptation for Legged Robots, *arXiv* 2107.04034, 2021) and Zhuang, Zhiqing, et al., working on humanoid locomotion, represent parallel research threads. The Cassie result fits within this active research landscape and represents a clear demonstration milestone — completing a human-scale endurance task on real outdoor terrain using RL — that had not been previously achieved for bipeds.

---

## §4 — Technical Context: DARPA Investment and the Broader Bipedal Robotics Landscape

DARPA's $1 million grant to Jonathan Hurst and his team at OSU reflects DARPA's longstanding interest in legged locomotion for military applications. The programme genealogy traces through the DARPA Legged Squad Support System (LS3), the BigDog and ATLAS platforms developed by Boston Dynamics under DARPA contracts, and various other initiatives aimed at developing robots capable of traversing terrain inaccessible to wheeled vehicles. Cassie's genesis in DARPA funding places it within this strategic context, though the OSU team's research has been primarily directed toward scientific and commercial applications.

Boston Dynamics' ATLAS platform is the most publicly prominent bipedal robot, known for videos demonstrating dynamic movements including running, jumping, backflips, and parkour. ATLAS uses a combination of hydraulic actuation (in earlier versions) and electric actuation (in more recent ones), with a model predictive control architecture supplemented by machine learning. The comparison between ATLAS and Cassie is instructive: ATLAS is a full-body humanoid with arms and a torso, while Cassie is only legs and a small central body chassis. The stripped-down morphology of Cassie makes it lighter, cheaper to manufacture, and more tractable as a research platform for studying fundamental locomotion — though it cannot perform manipulation tasks.

Agility Robotics commercialised the Cassie platform and subsequently developed Digit, which adds a torso, arms, and a head-mounted sensor suite. Digit has been deployed in logistics trials with Amazon and Ford, representing the pathway from research accomplishment to commercial application. The Cassie 5K milestone was thus not merely an academic demonstration; it represented a step in the development trajectory of a commercial robotics platform with real-world deployment intent.

---

## §5 — Social Reception and the Science Communication of Robot Milestones

Robot performance milestones occupy a peculiar position in public science communication: they are genuinely significant to the technical community while simultaneously eliciting reactions ranging from wonder to anxiety in general audiences. Robot capability demonstrations consistently generate headlines with "historic," "first," and "milestone" qualifiers that the underlying technical community itself typically presents more cautiously in peer-reviewed publications.

The Cassie 5K story was presented by OSU's communications team with the "makes history" framing that Snopes' article title directly reflected. This is a common move in institutional science communication: the team states a specific superlative ("first bipedal robot to complete such a run using machine learning on outdoor terrain"), which is technically defensible because of the precision of its conditions, but which journalists and general audiences will likely receive as a broader generality ("robots can run now"). Gieryn, Thomas F., described the "boundary work" that scientists and their institutions perform in drawing lines between scientific achievement and popular interpretation (*American Sociological Review*, vol. 48, no. 6, 1983, pp. 781–795); the Cassie coverage illustrates how institutional communications are themselves a form of boundary work that shapes what the public is invited to believe about the significance of a result.

The anxiety dimension of bipedal robot coverage — the fear that humanoid robots represent a threat to human employment, autonomy, or safety — was largely absent from the Cassie coverage, probably because Cassie is just legs and lacks the humanoid visual cues (face, arms, head) that trigger anthropomorphic anxiety responses. Cassie looks like an ostrich, not like a Terminator. This morphological choice — accidental as a product of the biomimetic design strategy — may have made the achievement more purely wondrous and less threatening in popular reception. Research on the "uncanny valley" effect (Mori, Masahiro, "The uncanny valley," *Energy*, vol. 7, no. 4, 1970, pp. 33–35, as translated and reprinted in *IEEE Robotics & Automation Magazine*, 2012) suggests that human-like robots that fail to fully achieve human appearance trigger aversion responses, while non-human-appearing robots do not. Cassie, being bird-like, escapes the uncanny valley entirely and sits comfortably in the zone of technological wonder.

---

## §6 — Verdict Calibration & Research Gaps

Snopes' implicit "True" treatment (as a confirmed news report rather than a debunked rumour) is accurate. The 5K run was real, documented by video and university press materials, and corroborated by independent technology press coverage. The OSU claim of "first bipedal robot to complete such a run using machine learning on outdoor terrain" is appropriately specific and is not contradicted by any documented prior achievement.

**EARC-A designation rationale:** The evidence is fully documented (OSU press release, TechCrunch, institutional video); the rating/framing is accurate; the claim is stable. The primary knowledge gap is the absence of independent third-party verification of the 53-minute run time and the absence of a comparative survey definitively establishing that no other bipedal machine learning system had achieved comparable outdoor endurance prior to this demonstration — but neither gap undermines the core claim, which is not that Cassie is definitively and forever the record-holder but that it completed this specific feat for the apparent first time under the specified conditions.

**Key sources:**
- OSU Today. "Bipedal Robot Developed by Oregon State Makes History by Learning to Run, Completing 5K." Oregon State University, 2021. https://today.oregonstate.edu/news/bipedal-robot-developed-oregon-state-makes-history-learning-run-completing-5k
- TechCrunch. "Cassie the Bipedal Robot Runs a 5K." July 27, 2021. https://techcrunch.com/2021/07/27/cassie-the-bipedal-robot-runs-a-5k/
- Agility Robotics. About. https://www.agilityrobotics.com/about#company
- Silver, David, et al. "Mastering the game of Go with deep neural networks and tree search." *Nature*, vol. 529, 2016, pp. 484–489.
- Peng, Xue Bin, et al. "DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills." *ACM Transactions on Graphics*, vol. 37, no. 4, 2018, article 41.
- Mori, Masahiro. "The uncanny valley." *Energy*, vol. 7, no. 4, 1970, pp. 33–35 (reprinted in *IEEE Robotics & Automation Magazine*, vol. 19, no. 2, 2012, pp. 98–100).
- Gieryn, Thomas F. "Boundary-Work and the Demarcation of Science from Non-Science: Strains and Interests in Professional Ideologies of Scientists." *American Sociological Review*, vol. 48, no. 6, 1983, pp. 781–795.
- Ibrahim, Nur. "Cassie the Robot Made History By Completing a 5K Run." *Snopes.com*, 9 August 2021.
