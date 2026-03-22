---
paper_id: 84
title: "Scaling Long-Horizon LLM Agent via Context-Folding"
year: 2025
authors: "Sun et al."
url: "https://arxiv.org/abs/2510.11967"
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
  - "BrowseComp-Plus"
  - "SWE-Bench Verified"
  - "long-horizon agent context management"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "ReAct"
  - "summarization-based context management"
  - "multi-agent systems"
  - "GRPO"
compares_to_unresolved:
  - "ReAct"
  - "summarization-based context management"
  - "standard GRPO"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Context-Folding trains an LLM agent to actively manage its own context by branching into temporary sub-trajectories and folding them back into compact summaries, rather than passively accumulating long histories.

# Why It Matters
It is one of the strongest papers in the current set for treating context management as a learnable agent skill rather than a fixed summarization heuristic.

# Method / Setup
The framework introduces `branch` and `return` actions for temporary sub-contexts, organizes execution in a plan-execution loop, and trains the policy with FoldGRPO using dense process rewards on BrowseComp-Plus and SWE-Bench Verified.

# Key Claims
- Agents can learn active context management as an intrinsic cognitive skill through reinforcement learning.
- Context folding can match or outperform long-context ReAct baselines while using a much smaller active context.
- Specialized process rewards are important for teaching agents when to branch, summarize, and keep the main thread compact.

# Limitations
- The method depends on reinforcement learning and custom process rewards, which adds training complexity.
- Its gains are demonstrated on specific long-horizon research and software-engineering benchmarks rather than across all agent domains.

# Connections
- [[Memory-Context]]
- `evaluates` BrowseComp-Plus
- `evaluates` SWE-Bench Verified
- `evaluates` long-horizon agent context management
- `builds_on_unresolved` ReAct
- `builds_on_unresolved` summarization-based context management
- `builds_on_unresolved` multi-agent systems
- `builds_on_unresolved` GRPO
- `compares_to_unresolved` ReAct
- `compares_to_unresolved` summarization-based context management
- `compares_to_unresolved` standard GRPO
<!-- GENERATED:END -->

## My Notes

