---
paper_id: 89
title: "ExGRPO: Learning to Reason from Experience"
year: 2025
authors: "Zhan et al."
url: "https://arxiv.org/abs/2510.02245"
paper_type: "system"
primary_topic: "agent-harnesses"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "pending"
tags:
  - "papers"
  - "agent-harnesses"
evaluates:
  - "AIME"
  - "AMC"
  - "MATH-500"
  - "Minerva"
  - "OlympiadBench"
  - "ARC-c"
  - "GPQA"
  - "MMLU-Pro"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "GRPO"
  - "reinforcement learning from verifiable rewards"
  - "experience replay"
compares_to_unresolved:
  - "on-policy RLVR"
  - "standard GRPO"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
ExGRPO improves reinforcement learning from verifiable rewards by replaying and prioritizing valuable reasoning experiences instead of discarding rollouts after a single update.

# Why It Matters
It is the cleanest match for the GRPO-plus-experience-selection theme because it explicitly studies which reasoning experiences are worth replaying and bakes that into GRPO-style training.

# Method / Setup
The method analyzes reasoning trajectories by question difficulty and token-level entropy, stores successful experiences in a replay buffer, prioritizes medium-difficulty questions and low-entropy trajectories, and combines replayed experience with on-policy GRPO updates through a mixed-policy objective.

# Key Claims
- Reasoning experiences are not equally valuable: medium-difficulty questions and low-entropy successful trajectories provide the strongest learning signal.
- Principled replay of selected reasoning experiences improves both sample efficiency and training stability over pure on-policy RLVR.
- Experience management is a key ingredient for scaling reinforcement learning in large reasoning models.

# Limitations
- The framework focuses on verifiable-reward reasoning settings and may need adaptation for noisier, less objectively graded agent environments.
- Its replay strategy depends on heuristics such as entropy and correctness-rate bucketing rather than a formally optimal value metric.

# Connections
- [[Agent-Harnesses]]
- `evaluates` AIME
- `evaluates` AMC
- `evaluates` MATH-500
- `evaluates` Minerva
- `evaluates` OlympiadBench
- `evaluates` ARC-c
- `evaluates` GPQA
- `evaluates` MMLU-Pro
- `builds_on_unresolved` GRPO
- `builds_on_unresolved` reinforcement learning from verifiable rewards
- `builds_on_unresolved` experience replay
- `compares_to_unresolved` on-policy RLVR
- `compares_to_unresolved` standard GRPO
<!-- GENERATED:END -->

## My Notes

