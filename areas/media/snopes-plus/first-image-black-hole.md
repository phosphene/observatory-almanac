---
title: "1st Computer Visualization of a Black Hole Looked Eerily Like the Real Thing"
slug: "first-image-black-hole"
snopes_url: "https://www.snopes.com/fact-check/first-image-black-hole/"
snopes_verdict: "True (Informational Article)"
snopes_author: "Jack Izzo"
snopes_published: "2024-02-20"
published: "2026-07-20"
updated: "2026-07-20"
epistemic_status: "verified — peer-reviewed astrophysics, primary papers cited"
earc: "C"
gap: "computational-physics-visualization-history"
tags:
  - black-holes
  - astrophysics
  - jean-pierre-luminet
  - event-horizon-telescope
  - general-relativity
  - computational-visualization
  - m87
---

## §1 Claim & Verdict Summary

The claim under examination is that the first computer-generated visualization of a black hole, produced by French cosmologist Jean-Pierre Luminet in 1979, bore a striking resemblance to the first authentic photographic image of a black hole released in 2019. Snopes, in an informational article written by Jack Izzo (2024), confirms this as accurate and provides a thorough grounding in the underlying physics. The verdict is effectively **True**.

Luminet published his simulation in *Astronomy and Astrophysics* (Luminet, 1979), using the equations of general relativity to predict the visual appearance of a rotating black hole surrounded by an accretion disk. The result showed a bright asymmetric ring of light — gravitationally lensed photons — surrounding a shadowed central void. His paper specifically predicted that this morphology would describe "the supermassive black hole whose existence in the nucleus of M87 has been suggested recently" (Luminet, 1979, *Astronomy and Astrophysics* 75: 228–235).

Forty years later, the Event Horizon Telescope (EHT) Collaboration released the first actual image of a black hole: the supermassive object at the center of galaxy M87 (Event Horizon Telescope Collaboration, 2019, *The Astrophysical Journal Letters*). The image showed an asymmetric bright ring of emission surrounding a central brightness depression — a visual structure immediately recognizable as corresponding to Luminet's 1979 simulation. The correspondence was widely noted in both the scientific press and the popular press as a remarkable validation of theoretical prediction.

---

## §2 Evidence Inventory

**2.1 Luminet's 1979 simulation**

Jean-Pierre Luminet's paper "Image of a Spherical Black Hole with Thin Accretion Disk" (Luminet, 1979, *Astronomy and Astrophysics* 75: 228–235) was produced in an era before modern computer graphics workstations. Luminet computed photon trajectories near a Schwarzschild black hole (a non-rotating solution) analytically, using the geodesic equations of general relativity, and then used a 1970s-era computer to output a dot-matrix representation of the resulting image. The simulation accounted for Doppler boosting of the approaching side of the accretion disk (making it brighter), gravitational lensing of photons passing close to the photon sphere, and the basic geometry of an optically thin disk viewed at an angle.

The resulting image showed:
- A central dark region (the shadow), bounded approximately by the photon sphere radius
- A primary bright arc below the midplane from the directly visible disk emission
- A secondary arc above the midplane from gravitationally lensed "secondary images" of disk emission
- Asymmetric brightening due to the relativistic Doppler effect

At the CNRS, Luminet's work was recognized as a major early achievement in computational astrophysics, with the French national research agency noting the historical significance upon the EHT release in 2019 (CNRS press release, 10 April 2019).

**2.2 The Event Horizon Telescope campaign**

In April 2017, an international collaboration led by Harvard astronomer Sheperd Doeleman coordinated eight radio telescope facilities spread across the globe — from Antarctica to Spain to Hawaii — to form a single Earth-sized interferometer using a technique called Very Long Baseline Interferometry (VLBI). The target was the supermassive black hole M87*, located approximately 55 million light-years away at the center of the elliptical galaxy M87. After nearly two years of data processing, in April 2019 the EHT Collaboration published six papers in *The Astrophysical Journal Letters* presenting the first image of a black hole (Event Horizon Telescope Collaboration, 2019).

The image showed a ring-like bright emission structure with a characteristic diameter roughly consistent with the predicted shadow diameter for M87's mass — a mass of approximately 6.5 billion solar masses. The southern arc of the ring was brighter than the northern arc, exactly as predicted by relativistic Doppler boosting of an accreting plasma orbiting in the direction seen from Earth. This is precisely the asymmetric morphology that Luminet had simulated in 1979.

**2.3 The Interstellar connection**

An additional historical thread is the black hole visualization created for Christopher Nolan's film *Interstellar* (2014). Visual effects supervisor Paul Franklin and Nolan commissioned theoretical physicist Kip Thorne to provide scientifically accurate equations for a Kerr black hole (a rotating solution) surrounded by an accretion disk. The resulting simulation, rendered by the visual effects company DNEG, produced the "Gargantua" black hole. The work generated a peer-reviewed paper (James et al., 2015, *Classical and Quantum Gravity*), as the rendering process revealed previously unconsidered optical effects of gravitationally lensed disk emission around a near-maximally spinning Kerr black hole. Nolan's film thus served as an inadvertent scientific instrument, bridging entertainment visualization and astrophysical discovery.

---

## §3 Epistemic Novelty

**3.1 Predictive success of mathematical physics over observational access**

The central epistemic phenomenon this case illustrates is the capacity of mathematical theories to correctly predict the visual appearance of objects that cannot be directly observed — and to maintain that prediction for decades before empirical confirmation becomes technologically possible. Einstein's general relativity equations, written before any black hole had been observed, encoded the geodesic structure of photon orbits around a Schwarzschild or Kerr metric. Luminet extracted the visual implications of those geodesics in 1979. The EHT confirmed them in 2019. The forty-year gap between prediction and confirmation is not a weakness of the scientific method but a demonstration of its power: precise, falsifiable predictions that remain standing through multiple rounds of technological capability upgrade.

This is analogous to the prediction of gravitational waves by Einstein (1916), confirmed by LIGO in 2015 (Abbott et al., 2016, *Physical Review Letters*) — a 99-year gap between theory and observation. In both cases, the limiting factor was not the quality of the theory but the available detector sensitivity.

**3.2 The epistemology of "lookalike" evidence**

However, a subtler epistemological point deserves examination: the visual similarity between Luminet's 1979 image and the 2019 EHT image is not a coincidence, but it is also not a trivial validation. Both images depict a black hole shadow surrounded by a bright photon ring from an accretion disk — but the specific details differ. Luminet modeled a Schwarzschild (non-rotating) black hole with a geometrically thin optically thin disk at a specific inclination. M87* is actively accreting with a turbulent, magnetized plasma corona, not a simple thin disk, and it is better described by a Kerr metric with spin. The EHT Collaboration used general-relativistic magnetohydrodynamic (GRMHD) simulations — orders of magnitude more complex than Luminet's 1979 calculation — to model the full emission (Event Horizon Telescope Collaboration, 2019, Paper V).

The "eerily similar" characterization in public discourse therefore captures something real (the broad morphological agreement: dark shadow, asymmetric bright ring) while glossing over critical differences in detail. The visual similarity is robust at the level of topology — the existence of a shadow and a ring — but the quantitative properties of the ring (width, asymmetry ratio, polarization structure) required the full GRMHD machinery to correctly predict. This is a case study in the difference between qualitative confirmation (morphology consistent with GR) and quantitative confirmation (shadow diameter consistent with M = 6.5 ± 0.7 × 10^9 solar masses).

**3.3 From numerical to physical reality: the EHT imaging pipeline**

A further epistemic novelty is the nature of the 2019 "image" itself. Unlike an optical photograph, the EHT image is a reconstruction from sparse interferometric data using algorithms borrowed from radio astronomy and adapted for this purpose — specifically, the regularized maximum likelihood methods and the CLEAN algorithm family (Event Horizon Telescope Collaboration, 2019, Paper IV). The "image" is in a very real sense a model: the most parsimonious reconstruction of the source brightness distribution consistent with the observed visibility amplitudes and closure phases.

This does not undermine its validity — the EHT team validated their reconstruction against multiple independent pipeline implementations — but it means the epistemological status of the EHT image is different from that of, say, a Hubble Space Telescope photograph. It is a highly constrained inference, not a direct photograph. Luminet's 1979 simulation was also a modeled image, not a photograph. In a deep sense, both "images" of M87*'s black hole are models rendered to human-visible form: the 1979 one from analytical physics, and the 2019 one from observational data reconstruction. Their resemblance is thus a convergence of two different modeling traditions on the same physical object.

---

## §4 Contextual Analysis

**4.1 The history of gravity theory from Newton to Einstein**

The intellectual foundations underlying Luminet's 1979 achievement stretch back through centuries of gravitational theory. Isaac Newton formulated the law of universal gravitation in 1687, describing gravitational attraction as proportional to the product of masses and inversely proportional to the square of separation distance — a formulation that successfully described planetary orbits and terrestrial gravity for over two centuries but could not account for several anomalous phenomena including the precession of Mercury's perihelion.

Albert Einstein's special theory of relativity (1905) introduced the principle of relativity (physics is identical in all inertial frames) and the constancy of the speed of light, necessitating the reconceptualization of space and time as a unified four-dimensional manifold called spacetime. His general theory of relativity (1915) extended this framework to include gravity, reconceiving it not as a force but as the curvature of spacetime induced by mass-energy distributions.

Karl Schwarzschild solved the Einstein field equations for the case of a spherically symmetric, non-rotating mass within weeks of Einstein's publication, producing what is now known as the Schwarzschild metric (Schwarzschild, 1916, *Sitzungsberichte der Preussischen Akademie der Wissenschaften*). This solution predicted an event horizon — a surface from within which nothing, not even light, can escape — at a radius now called the Schwarzschild radius, r_s = 2GM/c². The physical reality of such objects remained theoretically debated for decades, with the term "black hole" itself not coined until John Wheeler introduced it in 1967.

**4.2 The discovery of Cygnus X-1**

The first object seriously proposed as a black hole on observational grounds was Cygnus X-1, an X-ray binary system identified as a strong candidate by Thomas Bolton (1972, *Nature*) and Louise Webster and Paul Murdin (1972, *Nature*), based on the impossibly high mass inferred for the unseen compact object in the binary system — far exceeding the maximum mass for a neutron star. Cygnus X-1 established that black holes were not merely theoretical constructs but probable physical entities detectable through their gravitational effects on companion stars and their accretion-powered X-ray emission.

**4.3 The Interstellar scientific legacy**

The *Interstellar* visualization project (James et al., 2015, *Classical and Quantum Gravity* 32(6): 065001) represents an unusual instance of Hollywood production driving astrophysical research. Kip Thorne's consulting work for the film required solving, to sufficient numerical precision for photorealistic rendering, the full null geodesic equations for a near-maximally spinning Kerr black hole with an accretion disk extending to the innermost stable circular orbit. The DNEG rendering engine (called "Double Negative Gravitational Renderer" or DNGR) integrated over photon trajectories with sufficient angular resolution to reveal previously underemphasized features of the secondary and tertiary gravitationally lensed images of the accretion disk. The resulting paper described disk brightness features not previously prominently discussed in the theoretical literature and offered a new way to conceptualize what observers would actually see from different viewing angles.

---

## §5 Broader Implications

**5.1 Theory-first science and observational latency**

The black hole visualization story is emblematic of a broader pattern in modern physics: theories that outpace instrumentation. General relativity predicted gravitational lensing (confirmed: Eddington, 1919), gravitational waves (confirmed: LIGO, 2015), frame dragging (confirmed: Gravity Probe B, 2011), and black hole shadows (confirmed: EHT, 2019). In each case, the theoretical framework was sufficiently precise to make quantitative predictions decades before detection technology existed. This pattern raises epistemological questions about the nature of "confirmation": is 40-year-dormant prediction confirmation as epistemically weighty as near-simultaneous prediction and confirmation? Most philosophers of science argue it is — the key criterion is that the prediction was made on principled grounds before the confirming evidence was available.

**5.2 Public communication of probabilistic imaging**

The EHT image raised substantial public communication challenges precisely because informed critics noted its reconstructed nature. Social media discussions following the April 2019 release included commentary questioning whether the "blurry orange donut" constituted a real image or merely a model. The EHT Collaboration's communications team worked to explain the VLBI imaging process, but the conceptual bridge between "sparse interferometric data reconstructed into a brightness map" and "photograph of a black hole" remains difficult to convey to general audiences. This tension is structurally similar to challenges in communicating the nature of climate model outputs, genome composite assemblies, and other scientific products that are simultaneously empirically anchored and algorithmically constructed.

**5.3 Cross-generational scientific continuity**

Jean-Pierre Luminet was alive and celebrated when the EHT image was released in 2019. His 1979 paper was explicitly cited in the historical context provided by the EHT Collaboration and in press coverage worldwide. This represents an unusual case of a scientist witnessing, within one career, the observational confirmation of a prediction made during that career. By contrast, many of Einstein's predictions were confirmed only posthumously. The continuity of scientific knowledge across the Luminet-EHT forty-year arc illustrates both the durability of well-specified theoretical predictions and the accelerating pace of observational capability enabled by coordinated international infrastructure.

**5.4 The shadow diameter as Mass probe**

One of the most consequential scientific outputs of the EHT M87* images was a direct angular measurement of the shadow diameter, which yields the black hole mass almost independently of assumptions about the accretion physics. The EHT Collaboration measured a shadow diameter of approximately 42 microarcseconds, yielding a mass estimate of (6.5 ± 0.7) × 10^9 solar masses (Event Horizon Telescope Collaboration, 2019, Paper VI). This measurement agreed within errors with previous estimates based on stellar gas dynamics, providing a powerful multi-method validation. It also demonstrated that the shadow-based mass measurement technique — first theorized in detail by Falcke, Melia, & Agol (2000, *The Astrophysical Journal Letters*) — was observationally practical, opening a new direct probe of black hole masses in active galactic nuclei.

---

## §6 References

- Abbott, B.P., et al. (LIGO Scientific Collaboration and Virgo Collaboration). "Observation of Gravitational Waves from a Binary Black Hole Merger." *Physical Review Letters* 116, no. 6 (2016): 061102. https://doi.org/10.1103/PhysRevLett.116.061102
- Bolton, C.T. "Identification of Cygnus X-1 with HDE 226868." *Nature* 235 (1972): 271–273. https://doi.org/10.1038/235271b0
- CNRS. "First Ever Image of a Black Hole: A CNRS Researcher Had Simulated It as Early as 1979." Press release, 10 April 2019. https://www.cnrs.fr/en/press/first-ever-image-black-hole-cnrs-researcher-had-simulated-it-early-1979
- Event Horizon Telescope Collaboration. "First M87 Event Horizon Telescope Results. I–VI." *The Astrophysical Journal Letters* 875 (2019). https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole
- Falcke, Heino, Fulvio Melia, and Eric Agol. "Viewing the Shadow of the Black Hole at the Galactic Center." *The Astrophysical Journal Letters* 528, no. 1 (2000): L13–L16. https://doi.org/10.1086/312423
- Izzo, Jack. "1st Computer Visualization of a Black Hole Looked Eerily Like the Real Thing." *Snopes*, 20 Feb. 2024. https://www.snopes.com/fact-check/first-image-black-hole/
- James, Oliver, Eugénie von Tunzelmann, Paul Franklin, and Kip S. Thorne. "Gravitational Lensing by Spinning Black Holes in Astrophysics and in the Movie Interstellar." *Classical and Quantum Gravity* 32, no. 6 (2015): 065001. https://doi.org/10.1088/0264-9381/32/6/065001
- Luminet, J.-P. "Image of a Spherical Black Hole with Thin Accretion Disk." *Astronomy and Astrophysics* 75 (1979): 228–235. https://ui.adsabs.harvard.edu/abs/1979A%26A....75..228L
- Schwarzschild, Karl. "Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie." *Sitzungsberichte der Preussischen Akademie der Wissenschaften* (1916): 189–196.
- Webster, B. Louise, and Paul Murdin. "Cygnus X-1 — a Spectroscopic Binary with a Heavy Companion?" *Nature* 235 (1972): 37–38. https://doi.org/10.1038/235037a0
- Wired. "How Building a Black Hole for 'Interstellar' Led to an Amazing Scientific Discovery." *Wired*, Oct. 2014. https://www.wired.com/2014/10/astrophysics-interstellar-black-hole/
