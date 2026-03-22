---
paper_id: 86
title: "ARC: Active and Reflection-driven Context Management for Long-Horizon Information Seeking Agents"
year: 2026
authors: "Yao et al."
url: "https://arxiv.org/abs/2601.12030"
paper_type: "system"
primary_topic: "search-retrieval"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "search-retrieval"
evaluates:
  - "HotpotQA"
  - "GAIA"
  - "xBench-DeepSearch"
  - "BrowseComp"
  - "BrowseComp-ZH"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "ReAct"
  - "ReSum"
  - "Reflexion"
  - "MemGPT"
  - "MemoryBank"
compares_to_unresolved:
  - "ReAct"
  - "ReSum"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
ARC introduces active, reflection-driven context management for long-horizon information-seeking agents by treating context as a dynamic internal reasoning state that can be monitored, reorganized, and repaired.

# Why It Matters
It is directly relevant because it pushes beyond passive summarization and shows that context engineering can include explicit reflection over the agent's own internal state.

# Method / Setup
ARC separates an actor from a trainable context manager that maintains a checklist, interaction memory, and previous interaction, then uses incremental summarization and selective reflection to revise memory during long-horizon search tasks.

# Key Claims
- Long-horizon agents need active context repair, not just compression, to avoid context rot.
- Jointly revising the interaction memory and checklist outperforms raw-history and passive-summarization baselines.
- Context management is a learnable module that can be trained separately from the main actor.

# Limitations
- The approach adds a dedicated context-manager component and extra training complexity.
- The results are concentrated on information-seeking benchmarks, so generalization to other agent settings still needs testing.

# Connections
- [[Search-Retrieval]]
- `evaluates` HotpotQA
- `evaluates` GAIA
- `evaluates` xBench-DeepSearch
- `evaluates` BrowseComp
- `evaluates` BrowseComp-ZH
- `builds_on_unresolved` ReAct
- `builds_on_unresolved` ReSum
- `builds_on_unresolved` Reflexion
- `builds_on_unresolved` MemGPT
- `builds_on_unresolved` MemoryBank
- `compares_to_unresolved` ReAct
- `compares_to_unresolved` ReSum
<!-- GENERATED:END -->

## My Notes

