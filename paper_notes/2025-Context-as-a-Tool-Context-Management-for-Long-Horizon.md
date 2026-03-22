---
paper_id: 51
title: "Context as a Tool: Context Management for Long-Horizon SWE-Agents"
year: 2025
authors: "Liu et al."
url: "https://arxiv.org/abs/2512.22087"
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
  - "long-horizon SWE agents"
  - "context management"
  - "SWE-Bench-Verified"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "ReAct"
compares_to_unresolved:
  - "ReAct Agent"
  - "Threshold-Compression Agent"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Context as a Tool treats context management itself as an explicit tool that an SWE agent can invoke to compress and organize long interaction histories.

# Why It Matters
It is highly relevant to code-problem investigation because long-horizon SWE failures often come from context explosion and semantic drift rather than lack of raw model capability.

# Method / Setup
CAT defines a structured workspace with fixed task semantics, long-term compressed memory, and short-term interaction state, trains a context-aware SWE-Compressor with trajectory-level supervision, and evaluates on SWE-Bench-Verified.

# Key Claims
- Tool-based context management outperforms append-only and static compression baselines.
- The method sustains long-horizon SWE reasoning under bounded context budgets.
- Performance gains are larger on harder tasks with longer trajectories.

# Limitations
- The evidence is concentrated on SWE-Bench-Verified.
- The training pipeline adds complexity through retrospective trajectory reconstruction.
- Inference-time overhead from active context operations is not deeply analyzed.

# Connections
- [[Software-Agents]]
- `evaluates` long-horizon SWE agents
- `evaluates` context management
- `evaluates` SWE-Bench-Verified
- `builds_on_unresolved` ReAct
- `compares_to_unresolved` ReAct Agent
- `compares_to_unresolved` Threshold-Compression Agent
<!-- GENERATED:END -->

## My Notes

