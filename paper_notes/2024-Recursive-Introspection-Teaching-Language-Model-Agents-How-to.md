---
paper_id: 57
title: "Recursive Introspection: Teaching Language Model Agents How to Self-Improve"
year: 2024
authors: "Qu et al."
url: "https://arxiv.org/abs/2407.18219"
paper_type: "system"
primary_topic: "llm-multi-agent-systems"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "llm-multi-agent-systems"
evaluates:
  - "recursive self-improvement"
  - "multi-turn reasoning"
  - "math reasoning"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "Self-Refine"
  - "single-turn prompting"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Recursive Introspection trains language model agents to improve their own answers over multiple turns through iterative self-critique and correction.

# Why It Matters
It is a strong adjacent recursion paper for agents because it focuses on recursive self-improvement rather than recursive prompt processing.

# Method / Setup
RISE frames single-turn tasks as multi-turn MDPs, collects on-policy rollouts with self-distillation or teacher distillation, and fine-tunes models with reward-weighted regression on math reasoning tasks.

# Key Claims
- Iterative fine-tuning can teach LLMs to improve answers over multiple turns.
- The self-improvement behavior generalizes beyond the training distribution.
- Sequential self-correction can outperform parallel first-turn sampling.

# Limitations
- The evidence is concentrated on math-style reasoning tasks.
- Self-distillation can require multiple iterations to become strong.
- Scaling the full training loop can be computationally expensive.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` recursive self-improvement
- `evaluates` multi-turn reasoning
- `evaluates` math reasoning
- `compares_to_unresolved` Self-Refine
- `compares_to_unresolved` single-turn prompting
<!-- GENERATED:END -->

## My Notes

