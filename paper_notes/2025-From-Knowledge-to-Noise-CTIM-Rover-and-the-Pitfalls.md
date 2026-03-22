---
paper_id: 53
title: "From Knowledge to Noise: CTIM-Rover and the Pitfalls of Episodic Memory in Software Engineering Agents"
year: 2025
authors: "Lindenbauer et al."
url: "https://arxiv.org/abs/2505.23422"
paper_type: "system"
primary_topic: "software-agents"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "software-agents"
evaluates:
  - "episodic memory for software agents"
  - "repository-level issue resolution"
  - "SWE-bench Verified subset"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "AutoCodeRover"
compares_to_unresolved:
  - "AutoCodeRover"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
CTIM-Rover adds episodic memory to a software engineering agent through cross-task-instance memory, then studies whether that improves repository-level issue resolution.

# Why It Matters
It is a useful counterexample because it shows that naive episodic memory can make SWE agents worse rather than better.

# Method / Setup
The paper extends AutoCodeRover with a memory layer distilled from prior successful trajectories and evaluates on a subset of SWE-bench Verified.

# Key Claims
- The proposed episodic memory degrades performance rather than improving it.
- Noisy or weakly relevant memory items can interfere with SWE reasoning.
- Experience-learning methods from simpler domains may not transfer cleanly to real software engineering.

# Limitations
- The evaluation covers only a subset of SWE-bench Verified.
- The negative result may partly reflect the specific retrieval and filtering design rather than the full idea space.
- Environment setup issues reduced usable benchmark coverage.

# Connections
- [[Software-Agents]]
- `evaluates` episodic memory for software agents
- `evaluates` repository-level issue resolution
- `evaluates` SWE-bench Verified subset
- `builds_on_unresolved` AutoCodeRover
- `compares_to_unresolved` AutoCodeRover
<!-- GENERATED:END -->

## My Notes

