---
paper_id: 109
title: "Optimal foraging strategies can be learned"
year: 2023
authors: "Munoz-Gil et al."
url: "https://arxiv.org/abs/2303.06050"
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
  - "optimal foraging"
  - "reinforcement learning"
  - "random search strategies"
  - "levy-walk baselines"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Levy walks"
  - "Projective simulation"
compares_to_unresolved:
  - "Levy walks"
  - "bi-exponential policies"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper formulates non-destructive foraging as a reinforcement learning problem and shows that learned policies can outperform strong hand-designed random-search baselines such as Levy walks. It focuses on how search strategies can be learned, not only optimized analytically.

# Why It Matters
It is not explicitly a central-place foraging paper, but it is useful background because it provides a learning-based search baseline for comparison with more structured return-to-home or site-constant models.

# Method / Setup
The authors discretize random-walk foraging into an RL problem, prove that maximizing average reward is equivalent to maximizing search efficiency, and train projective-simulation agents in sparse-target environments. They compare learned strategies against Levy and bi-exponential benchmark policies.

# Key Claims
- The RL formulation gives a mechanistic learning model whose objective is exactly aligned with foraging efficiency.
- Learned policies outperform Levy-walk baselines and in most tested environments also beat the best bi-exponential benchmarks.
- The learned strategies often exhibit structured multi-scale behavior tied to environmental parameters such as cutoff length.

# Limitations
- The paper studies idealized non-destructive search rather than explicit central-place foraging with home returns.
- Results are shown in stylized sparse-target environments with a specific RL algorithm rather than across richer ecological settings.

# Connections
- [[Central-Place-Foraging]]
- `evaluates` optimal foraging
- `evaluates` reinforcement learning
- `evaluates` random search strategies
- `evaluates` levy-walk baselines
- `builds_on_unresolved` Levy walks
- `builds_on_unresolved` Projective simulation
- `compares_to_unresolved` Levy walks
- `compares_to_unresolved` bi-exponential policies
<!-- GENERATED:END -->

## My Notes

