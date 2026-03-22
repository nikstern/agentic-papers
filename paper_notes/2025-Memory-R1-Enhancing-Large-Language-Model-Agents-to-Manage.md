---
paper_id: 90
title: "Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning"
year: 2025
authors: "Unknown et al."
url: "https://arxiv.org/abs/2508.19828"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "pending"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "LoCoMo"
  - "MSC"
  - "LongMemEval"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "retrieval-augmented generation"
  - "A-MEM"
  - "Mem0"
  - "MemoryOS"
  - "GRPO"
  - "PPO"
compares_to_unresolved:
  - "LoCoMo"
  - "A-MEM"
  - "Mem0"
  - "MemoryOS"
  - "Memory-SFT"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Memory-R1 trains an LLM-based memory manager and answer agent with reinforcement learning so the system learns both how to update its memory bank and how to distill retrieved memories for downstream reasoning.

# Why It Matters
It is directly relevant because it treats memory operation selection and memory utilization as learned RL problems rather than heuristic retrieval and CRUD rules.

# Method / Setup
The framework uses a Memory Manager to perform ADD, UPDATE, DELETE, and NOOP operations over an evolving memory bank and an Answer Agent to distill retrieved memories, with both agents optimized using PPO or GRPO against downstream QA rewards.

# Key Claims
- Reinforcement learning can teach LLM agents when to remember, update, or discard information more effectively than static memory heuristics.
- Learning to distill retrieved memories before answering improves long-horizon QA over naive retrieval pipelines.
- Outcome-driven RL can produce strong memory behavior with surprisingly little supervised data.

# Limitations
- The framework is evaluated mainly in multi-session dialogue and QA settings rather than broad open-ended agent environments.
- It relies on an external memory bank and multi-component architecture, which adds system complexity.

# Connections
- [[Memory-Context]]
- `evaluates` LoCoMo
- `evaluates` MSC
- `evaluates` LongMemEval
- `builds_on_unresolved` retrieval-augmented generation
- `builds_on_unresolved` A-MEM
- `builds_on_unresolved` Mem0
- `builds_on_unresolved` MemoryOS
- `builds_on_unresolved` GRPO
- `builds_on_unresolved` PPO
- `compares_to_unresolved` LoCoMo
- `compares_to_unresolved` A-MEM
- `compares_to_unresolved` Mem0
- `compares_to_unresolved` MemoryOS
- `compares_to_unresolved` Memory-SFT
<!-- GENERATED:END -->

## My Notes

