---
paper_id: 145
title: "Sequential Multi-Dimensional Self-Supervised Learning for Clinical Time Series"
year: 2023
authors: "Raghu et al."
url: "https://proceedings.mlr.press/v202/raghu23a.html"
paper_type: "system"
primary_topic: "medical-time-series"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "medical-time-series"
evaluates:
  - "self-supervised clinical time-series representation learning"
  - "downstream fine-tuning from physiological pretraining"
  - "multimodal sequence and component-level objectives"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "SimCLR"
  - "VICReg"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper proposes sequential multi-dimensional self-supervised learning for clinical trajectories that combine structured labs and vital signs with sequences of high-dimensional physiological measurements such as ECGs.

# Why It Matters
It supports testing Toto not only as a forecaster but also as a pretrained representation model whose embeddings may improve intervention or deterioration classification.

# Method / Setup
The method applies self-supervised losses at both the full-sequence level and the level of individual high-dimensional observations. It is evaluated on two real-world clinical datasets containing structured clinical time series and high-frequency ECG information, using both contrastive and non-contrastive objectives before downstream fine-tuning.

# Key Claims
- Joint sequence-level and component-level pretraining improves downstream clinical prediction over the evaluated baselines on both datasets.
- The framework can be paired with different self-supervised objectives, including SimCLR-style contrastive learning and VICReg-style non-contrastive learning.
- Modeling multiple temporal scales and modalities can produce more useful clinical representations than unimodal pretraining.

# Limitations
- The experiments focus on multimodal trajectories that include high-frequency ECG, while JRESP may initially use only structured vital signs.
- Improved downstream benchmark performance does not establish intervention lead-time benefit or clinical deployment utility.
- The method does not directly compare forecast-assisted classification with a direct classifier under identical inputs.

# Connections
- [[Medical-Time-Series]]
- `evaluates` self-supervised clinical time-series representation learning
- `evaluates` downstream fine-tuning from physiological pretraining
- `evaluates` multimodal sequence and component-level objectives
- `compares_to_unresolved` SimCLR
- `compares_to_unresolved` VICReg
<!-- GENERATED:END -->

## My Notes

