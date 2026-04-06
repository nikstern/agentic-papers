---
paper_id: 108
title: "Diffusion with two resetting points"
year: 2024
authors: "Julian-Salgado et al."
url: "https://arxiv.org/abs/2311.11897"
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
  - "search optimization"
  - "multiple central places"
  - "first-passage time"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Diffusion with stochastic resetting"
  - "Diffusion with optimal resetting"
compares_to_unresolved:
  - "single-site resetting"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper analyzes Brownian search with stochastic resetting to two sites instead of one, revealing new optimization behavior in mean first-passage time. It motivates the setup with foragers and other agents that repeatedly return to a small set of central places such as roosts, homes, or work sites.

# Why It Matters
It is relevant to central-place foraging because it models repeated returns to multiple central places and shows that adding a second return site qualitatively changes optimal search behavior.

# Method / Setup
The authors derive the mean first-passage time analytically for one-dimensional diffusion with resetting to two fixed sites and study the resulting optimal resetting rate across parameter regimes. They also map the model to an intermittent search problem with switching diffusion coefficients.

# Key Claims
- With two resetting points, the optimal resetting rate can undergo a discontinuous transition rather than varying smoothly.
- The two-site resetting problem is equivalent to an intermittent search problem with switching diffusion modes and a shared central place.
- Critical behavior appears only in specific parameter regimes, producing phase-diagram-like structure for optimal search.

# Limitations
- The model is a minimal one-dimensional stochastic search process rather than a biologically realistic animal foraging model.
- Its relevance to central-place foraging is by abstraction and motivation, not by direct behavioral data.

# Connections
- [[Central-Place-Foraging]]
- `evaluates` stochastic resetting
- `evaluates` search optimization
- `evaluates` multiple central places
- `evaluates` first-passage time
- `builds_on_unresolved` Diffusion with stochastic resetting
- `builds_on_unresolved` Diffusion with optimal resetting
- `compares_to_unresolved` single-site resetting
<!-- GENERATED:END -->

## My Notes

