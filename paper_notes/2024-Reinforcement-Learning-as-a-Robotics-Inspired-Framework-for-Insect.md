---
paper_id: 107
title: "Reinforcement Learning as a Robotics-Inspired Framework for Insect Navigation: From Spatial Representations to Neural Implementation"
year: 2024
authors: "Lochner et al."
url: "https://arxiv.org/abs/2406.01501"
paper_type: "system"
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
  - "insect navigation"
  - "reinforcement learning"
  - "central place foragers"
  - "spatial representations"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "The insect navigation base model"
  - "Path integration"
  - "Wystrach 2023 visual homing model"
compares_to_unresolved:
  - "SLAM"
  - "deep reinforcement learning navigation"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper links insect navigation and robot navigation through reinforcement learning, using bees and ants as prominent examples of central-place foragers. It compares spatial representation schemes across biology and robotics and proposes how insect brain structures such as the mushroom bodies and central complex could implement RL-like navigation.

# Why It Matters
It matters for central-place foraging because it treats repeated outbound and return navigation in bees and ants as a core biological case, and it offers a computational account of how central-place foragers may integrate path integration, vector memories, and view memories.

# Method / Setup
The paper is primarily conceptual and theoretical: it classifies spatial representations, reframes insect navigation in RL terms, and proposes a hierarchical RL account grounded in insect neuroanatomy. It synthesizes prior navigation models rather than introducing a single new empirical benchmark.

# Key Claims
- Reinforcement learning provides a useful unifying framework for relating insect navigation and robot navigation.
- Insect navigation likely combines explicit vector-like representations with learned, latent directional cues instead of relying on a single map format.
- A hierarchical model combining mushroom-body and central-complex functions could explain how insects learn flexible navigation policies.

# Limitations
- The paper is mostly a theoretical synthesis and hypothesis paper rather than a direct empirical test of central-place foraging behavior.
- Its scope is broader than central-place foraging alone, so some claims concern general navigation rather than foraging-specific decisions.

# Connections
- [[Central-Place-Foraging]]
- `evaluates` insect navigation
- `evaluates` reinforcement learning
- `evaluates` central place foragers
- `evaluates` spatial representations
- `builds_on_unresolved` The insect navigation base model
- `builds_on_unresolved` Path integration
- `builds_on_unresolved` Wystrach 2023 visual homing model
- `compares_to_unresolved` SLAM
- `compares_to_unresolved` deep reinforcement learning navigation
<!-- GENERATED:END -->

## My Notes

