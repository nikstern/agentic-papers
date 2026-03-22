---
paper_id: 76
title: "FLEX: Continuous Agent Evolution via Forward Learning from Experience"
year: 2025
authors: "Cai et al."
url: "https://arxiv.org/abs/2511.06449"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "AIME25"
  - "GSM8k"
  - "USPTO50k"
  - "ProteinGym"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "ReAct"
  - "Reflexion"
  - "Self-Refine"
compares_to_unresolved:
  - "ReAct"
  - "In-Context Learning"
  - "Vanilla LLM"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
FLEX proposes a gradient-free learning paradigm where LLM agents evolve through an external experience library instead of parameter updates. The system accumulates, organizes, and reuses successful and failed reasoning traces to improve future performance and enable inheritance across agents.

# Why It Matters
It is relevant if you care about memory as an evolving experience substrate for continual agent improvement rather than just retrieval over stored context.

# Method / Setup
System built around forward learning from experience, combining exploration trajectories, critic-generated semantic feedback, a hierarchical experience library with success and warning zones, and experience retrieval during future reasoning.

# Key Claims
- Agents can improve continuously through experience-library evolution without gradient-based fine-tuning.
- Performance scales predictably with accumulated experience, suggesting a scaling law of experience.
- Experience libraries can be inherited across agents, allowing knowledge transfer without parameter sharing.

# Limitations
- The method depends on sustained exploration, reflection, and library maintenance, which adds inference-time complexity.
- It is broader than memory retrieval alone and may be less directly applicable if the goal is lightweight task-specific memory rather than continual evolution.

# Connections
- [[Memory-Context]]
- `evaluates` AIME25
- `evaluates` GSM8k
- `evaluates` USPTO50k
- `evaluates` ProteinGym
- `builds_on_unresolved` ReAct
- `builds_on_unresolved` Reflexion
- `builds_on_unresolved` Self-Refine
- `compares_to_unresolved` ReAct
- `compares_to_unresolved` In-Context Learning
- `compares_to_unresolved` Vanilla LLM
<!-- GENERATED:END -->

## My Notes

