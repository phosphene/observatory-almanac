---
title: 'Image Shows 1 Cubic Millimeter Sample of Human Brain?'
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
earc_mode: "A"
gap_category: "scientific-visualization-nanoscale"
snopes_url: "https://www.snopes.com/fact-check/image-human-brain/"
snopes_verdict: "true"
summary: >
  In October 2024, a vivid 3D rendering of neural connections — described as a visualisation of 1 cubic millimetre of human brain tissue — went viral on Reddit. The image is authentic: it derives from a May 2024 collaborative project by Google Research and Harvard's Lichtman Lab, published in Science, which produced the most detailed structural map of human cerebral cortex ever completed, comprising 1.4 petabytes of data from approximately 57,000 cells and 150 million synapses.
tags:
  - truth-vault
  - neuroscience
  - connectomics
  - human-brain
  - google-research
  - harvard
  - electron-microscopy
  - neural-mapping
  - scientific-visualization
  - petabyte
---

## The Claim

In October 2024, a Reddit user posted an image described as "1 cubic millimeter of brain" — a rendering featuring wispy blue, green, and orange-hued strands against a black background, resembling an illuminated tangle of cosmic filaments. The post attracted significant engagement. One version on r/interestingasfuck carried a caption noting that the "full scan of 1 cubic millimeter of brain tissue... took 1.4 petabytes of data, equivalent to 14,000 4K movies." The image had circulated on Reddit before, appearing in a post from as early as May 2024 (r/pics), suggesting the subject material had first gained attention around the time of the original scientific publication.

Commenters responded with a mixture of wonder and humour — "Was this from a smart person's brain or from a dumb person?" was among the more remarked-upon comments — and the image spread widely alongside both accurate and inaccurate descriptions of what exactly it depicted. Snopes reporter Madison Dapcevich traced the image to its origin and confirmed its authenticity. The investigation opened onto one of the most significant achievements in the history of neuroscience imaging.

---

## What's Actually True

The image is authentic. It is a 3D rendering of neurons — brain cells and their interconnections — derived from a project by scientists at Google Research and Harvard University's Lichtman Lab, published in the peer-reviewed journal *Science* in May 2024 (Shapson-Coe et al., 2024, *Science*). The rendering visualises a subset of the cellular and synaptic connections contained within a roughly 1-cubic-millimetre fragment of human cerebral cortex.

The process of creating this dataset involved extraordinary procedural complexity. The brain sample was taken from the cortex of a 45-year-old woman who underwent surgery to treat epilepsy. The specific region was the temporal cortex — a region involved in auditory processing, language comprehension, and long-term memory consolidation. The sample was chemically fixed, stained with heavy metals to increase electron contrast, and embedded in resin. It was then cut into approximately 5,000 slices, each approximately 34 nanometres thick — each slice thinner than a single virus particle. These ultra-thin sections were imaged using electron microscopy, a technique that achieves nanometre-scale resolution by using beams of electrons rather than photons to form images.

The resulting image data was then processed using AI models developed specifically for this project to identify cellular boundaries, trace individual neurons and their processes (axons and dendrites) across thousands of slices, and assemble the entire three-dimensional landscape of the tissue volume. The total dataset comprised approximately 1.4 petabytes — 1.4 × 10^15 bytes, or roughly the equivalent of 14,000 4K movies as noted in the viral caption. All associated datasets and interactive visualisations have been made publicly available via a dedicated data release portal.

The final reconstruction, as described in the *Science* publication, covers approximately 1 cubic millimetre of cortex and contains approximately 57,000 cells, approximately 230 millimetres of blood vessels, and approximately 150 million synapses. A news article in *Nature* (Wong, 2024) described it as "the most detailed map of a cubic millimeter of the human brain ever produced." The Google blog post published on 4 May 2024 described the research as having "reconstructed nearly every cell and all of its connections within a small volume of human brain tissue about half the size of a grain of rice."

---

## Connectomics, Nanoscale Reconstruction, and the Science of Neural Wiring

The epistemic novelty in this case is layered: the claim about the image's authenticity is simple and true, but the genuine intellectual contribution of what the image represents — and what the Lichtman Lab/Google Research project achieved — is of a different order from routine viral fact-checking. This is an occasion to engage seriously with a landmark scientific result.

The field of connectomics aims to map the complete wiring diagram of nervous systems — the totality of neurons and the synaptic connections between them. The first complete connectome was produced for the nematode *Caenorhabditis elegans* in a project that took more than a decade: White et al. (1986, *Philosophical Transactions of the Royal Society B*) published the complete connectome of *C. elegans'* 302 neurons and approximately 7,000 synapses. This work, which contributed to Sydney Brenner, John Sulston, and Robert Horvitz receiving the 2002 Nobel Prize in Physiology or Medicine, established the field's foundational approach: tissue preservation, serial sectioning, electron microscopy, and computational tracing of neural architecture.

Scaling from *C. elegans* to a mammalian brain has required decades of methodological development. A mouse cortical connectome at comparable resolution would require an estimated petabyte to exabyte range of data for a complete brain — a computational challenge of extraordinary magnitude. The Lichtman Lab at Harvard has pioneered the scaling of connectomics methods, working progressively from invertebrate to mammalian neural tissue using increasingly powerful electron microscopy systems and AI-assisted segmentation.

The 2024 human cortex project — sometimes referred to by the researchers as the "H01" dataset, following the data release portal naming convention — represents the largest-volume high-resolution reconstruction of human neural tissue ever achieved. Its scale is appropriate to emphasise: 1 cubic millimetre sounds small, and by the standards of an organ weighing 1.3 kilograms occupying approximately 1,300 cubic centimetres, it is small — representing roughly one-millionth of the total brain volume. But the data volume required to map that millimetre at nanoscale resolution, and the AI infrastructure required to process it, were unprecedented.

Several specific findings from the dataset were highlighted in the *Science* publication. Among the most discussed was the discovery of pairs of neurons connected to each other through an unusually high number of synaptic contacts — up to 50 synapses in some cases between the same pair of neurons. This degree of multisynaptic connectivity between individual neuron pairs was higher than expected from prior models of cortical connectivity and raised fundamental questions about the functional significance of such strong bilateral connections. Standard models of cortical circuits assumed that strong neural connections were generally broadcast (one neuron connecting to many) rather than intensely bidirectional (two neurons connected very strongly and reciprocally to each other specifically). The genomics of such strongly connected pairs remains an active research question.

The dataset also provided unprecedented detail about the organisation of cortical layers, the geometries of axonal and dendritic arbors, and the distribution of different inhibitory and excitatory neuron subtypes across the tissue volume. The temporal cortex, from which the sample was take, is involved in a range of higher cognitive functions, and its columnar organisation — alternating bands of different cell types visible in the reconstruction — can now be studied at the level of individual synaptic contacts.

The H01 data has been made publicly available for re-analysis by any researcher or citizen scientist with sufficient computational resources. This open-data approach mirrors the JunoCam model in planetary science — an acknowledgement that datasets of this complexity exceed the analytical capacity of any single research group and that broader scientific engagement will accelerate discovery.

Understanding how synaptic and neural circuits are disrupted in various neuropsychiatric and neurological conditions is one of the most significant motivations for connectomics research. Alterations in synaptic circuit architecture have been implicated in schizophrenia (Glausier & Lewis, 2013, *Neuroscience*), autism spectrum disorder (Tang et al., 2014, *Neuron*), bipolar disorder (Harrison, 2002, *European Neuropsychopharmacology*), and Alzheimer's disease (Selkoe, 2002, *Science*). Mapping what "normal" human cortical connectivity looks like at nanoscale resolution is a necessary prerequisite for characterising what disrupted connectivity looks like in disease states.

---

## Why People Engaged With This

The viral spread of the 1-cubic-millimetre brain image reflects a specific cultural dynamic: the collision of the unimaginably small with the unimaginably complex. The image is compelling for reasons that transcend simple aesthetic attraction.

**The scale induces conceptual vertigo.** One cubic millimetre is easy to visualise in principle — a tiny cube, smaller than a pea. The idea that this volume contains 57,000 cells and 150 million synaptic connections, and that mapping it required 1.4 petabytes of data, produces a specific kind of cognitive dissonance. The mismatch between the intuitively comprehensible physical scale (something you could fit on a fingertip) and the statistical scale of the biological contents (more connections than there are individual neurons in the entire brain of a honeybee, crammed into a volume you could hold in your hand) is genuinely startling. This is not a misunderstanding of the science — it accurately reflects how incredibly dense the wiring of the human cortex actually is.

**The image's aesthetics are genuinely extraordinary.** The 3D renderings produced from the H01 dataset — colourised to distinguish different neural processes, illuminated to show structural relationships, and rendered with modern scientific visualisation tools — are aesthetically compelling objects. The combination of systematic structure (the ordered patterns of cortical layers and myelinated axon bundles) with apparent complexity (the tangled, organic profusion of individual dendrites and fine processes) produces visuals that resist easy categorisation. They look like neither anatomy textbooks nor abstract art, though they resemble both.

**The "humour calibration" comments reveal comfort with the subject.** The "was it from a smart person or a dumb person?" comment noted in the Snopes article is a typical social media deflection from confronting the philosophical weight of what the image represents. Looking at a rendering of human neural tissue invites the thought: "this is what thinking looks like." The physical substrate of memory, intention, emotion, perception, and consciousness is depicted, in detail, in those coloured filaments. That is genuinely unsettling to contemplate, and humour is a common response to unsettling proximity with existentially weighty matter. The comment's virality suggests it resonated precisely because it captured a shared discomfort with the image's implications.

**The petabyte figure grounded the claim.** For many technically literate viewers, the data volume — 1.4 petabytes — served as an authenticating detail. The comparison to 14,000 4K movies provided accessible scale. Numbers of this magnitude are consistent with serious scientific infrastructure and inconsistent with fabricated internet content. The figure served, for much of the audience, the function that source citations serve for more research-inclined readers: a plausibility anchor that made the claim feel grounded.

---

## The Limits of the Map: What Connectomics Cannot Yet Tell Us

The H01 dataset is extraordinary, but it is worth being precise about what it does and does not show, and what questions about the brain it opens rather than closes.

The H01 reconstruction is structurally complete at nanoscale for its sampled volume — meaning every cellular membrane, every synaptic contact, every mitochondrion is in principle visible. What it is not is functionally annotated: structural connectivity maps neuron-to-neuron wiring, but does not directly reveal the strength of synaptic connections in living tissue, the patterns of neural firing that the tissue would produce, or the relationship between structural connectivity and specific cognitive processes or memories. The "wiring diagram" produced by connectomics is analogous to a wiring diagram for a computer circuit: it tells you how the components are connected but not what computation they are performing.

The cortical tissue sample was also taken from an epileptic patient undergoing surgery, meaning the tissue had already been modified by years of epileptic activity. Whether the structural features observed — including the unusual numbers of high-synapse-count neuron pairs — are representative of typical temporal cortex anatomy or reflect epilepsy-driven circuit reorganisation remains an open question noted by the researchers themselves.

These limitations do not diminish the significance of the achievement. They contextualise it. The H01 dataset is a foundation for future work, not a final answer. Its public availability means that the interpretive work will be distributed across the global neuroscience community for years, and that discoveries in the dataset are not confined to its original authors.

---

## Verdict

**True.** The image circulating on Reddit as a "picture of 1 cubic millimeter of brain" is an authentic 3D rendering derived from the H01 dataset produced by Google Research and Harvard University's Lichtman Lab, published in *Science* in May 2024. It depicts the neural architecture — neurons, axons, dendrites, synaptic connections — within a roughly 1-cubic-millimetre sample of human temporal cortex from a 45-year-old woman who underwent epilepsy surgery. The dataset comprises 1.4 petabytes of electron microscopy data assembled using AI segmentation tools, representing approximately 57,000 cells, 230 millimetres of blood vessels, and 150 million synaptic connections.

The image is not a fabrication, not an artist's impression, and not a schematic. It is a scientific visualisation of real tissue at nanoscale resolution, made possible by a decade of methodological development in the field of connectomics. It represents the most detailed structural map of human neural tissue ever produced, and the data underlying it is publicly accessible. The humour and wonder with which social media received the image were both appropriate responses to a genuinely remarkable scientific achievement.

---

## References

- Dapcevich, Madison. "Image Shows 1 Cubic Millimeter Sample of Human Brain?" *Snopes*, 18 Oct. 2024. https://www.snopes.com/fact-check/image-human-brain/
- Shapson-Coe, Alexander, et al. (2024). "A Petavoxel Fragment of Human Cerebral Cortex Reconstructed at Nanoscale Resolution." *Science*, 384(6696), eadk4858. https://doi.org/10.1126/science.adk4858
- Wong, Carissa. (2024). "Cubic Millimetre of Brain Mapped in Spectacular Detail." *Nature*, 629(8013), 739–740. https://doi.org/10.1038/d41586-024-01387-9
- White, J. G., et al. (1986). "The Structure of the Nervous System of the Nematode Caenorhabditis elegans." *Philosophical Transactions of the Royal Society B: Biological Sciences*, 314(1165), 1–340.
- Glausier, Jill R., & Lewis, David A. (2013). "Dendritic spine pathology in schizophrenia." *Neuroscience*, 251, 90–107.
- Tang, Guomei, et al. (2014). "Loss of mTOR-Dependent Macroautophagy Causes Autistic-like Synaptic Pruning Deficits." *Neuron*, 83(5), 1131–1143.
- Harrison, P. J. (2002). "The neuropathology of primary mood disorder." *Brain*, 125(7), 1428–1449. [Representative citation for synaptic alterations in bipolar disorder.]
- Selkoe, Dennis J. (2002). "Alzheimer's Disease Is a Synaptic Failure." *Science*, 298(5594), 789–791.
- Google Research. "6 Incredible Images of the Human Brain Built with the Help of Google's AI." Google Blog, 9 May 2024. https://blog.google/technology/research/google-ai-research-new-images-human-brain/
- H01 Release Dataset. https://h01-release.storage.googleapis.com/data.html
