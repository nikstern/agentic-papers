---
paper_id: 106
title: "Critical habitat size of organisms diffusing with stochastic resetting"
year: 2025
authors: "Menon Jr. et al."
url: "https://arxiv.org/abs/2505.03727"
paper_type: "application"
primary_topic: "central-place-foraging"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "central-place-foraging"
evaluates:
  - "stochastic resetting"
  - "critical patch size"
  - "homing models"
  - "central place foraging theory"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Diffusion with stochastic resetting"
  - "Diffusion with optimal resetting"
  - "Central place foraging"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper studies how stochastic resetting to a fixed location changes the critical habitat size needed for population persistence. It frames resetting as a model of homing, refuge-seeking, return to essential resources, and central-place foraging, and derives analytical results backed by agent-based simulations.

# Why It Matters
It provides a clean mathematical abstraction of central-place style return behavior and shows how repeated relocation to a home or refuge can either help or hurt persistence depending on rate, position, and environmental hostility.

# Method / Setup
The authors analyze one-dimensional reaction-diffusion models with stochastic resetting under both totally hostile and partially hostile environments, then validate the theory with agent-based simulations. They study how reset rate and reset position change the critical patch size for survival.

# Key Claims
- Stochastic resetting can either increase or decrease critical habitat size depending on reset rate, reset position, and environmental hostility.
- For some reset positions there is a core region where resetting consistently reduces habitat requirements, while for others it can worsen survival thresholds.
- Analytical predictions for the critical patch size and long-time population growth match agent-based simulations closely.

# Limitations
- The analysis is built around stylized one-dimensional reaction-diffusion models rather than realistic animal movement trajectories.
- Resetting captures return-to-home behavior abstractly but does not model richer sensory, memory, or social mechanisms of central-place foraging.

# Connections
- [[Central-Place-Foraging]]
- `evaluates` stochastic resetting
- `evaluates` critical patch size
- `evaluates` homing models
- `evaluates` central place foraging theory
- `builds_on_unresolved` Diffusion with stochastic resetting
- `builds_on_unresolved` Diffusion with optimal resetting
- `builds_on_unresolved` Central place foraging
<!-- GENERATED:END -->

## My Notes

