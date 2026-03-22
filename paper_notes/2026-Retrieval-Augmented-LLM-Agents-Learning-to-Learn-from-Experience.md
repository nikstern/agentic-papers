---
paper_id: 92
title: "Retrieval-Augmented LLM Agents: Learning to Learn from Experience"
year: 2026
authors: "Ferraz et al."
url: "https://arxiv.org/abs/2603.18272"
paper_type: "system"
primary_topic: "search-retrieval"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "pending"
tags:
  - "papers"
  - "search-retrieval"
evaluates:
  - "ALFWorld"
  - "ScienceWorld"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "retrieval-augmented generation"
  - "LoRA"
  - "episodic memory"
compares_to_unresolved:
  - "LoRA"
  - "training-free ExpRAG"
  - "ExpRAG-LoRA"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper studies retrieval-augmented LLM agents that learn from prior trajectories, showing that retrieval becomes much more effective when it is integrated directly into fine-tuning rather than used only at inference time.

# Why It Matters
It is important for the current thread because it gives a concrete training recipe for episodic trajectory retrieval and shows when retrieval-augmented experience actually helps generalization.

# Method / Setup
The approach builds an episodic experience bank from prior trajectories, retrieves top-k relevant trajectories into the prompt, and compares plain retrieval, standard LoRA fine-tuning, and retrieval-augmented fine-tuning (ExpRAG-LoRA) in ALFWorld and ScienceWorld.

# Key Claims
- Inference-only trajectory retrieval helps, but retrieval-augmented training is stronger for out-of-distribution generalization.
- Agents trained to use retrieved experiences generalize better than agents fine-tuned without retrieval context.
- Simple read-only episodic retrieval is a strong baseline for agent memory and should be benchmarked before more elaborate memory systems.

# Limitations
- The method depends on having a useful trajectory index, and performance degrades when the retrieved experience bank is mismatched or empty.
- It uses a fixed read-only experience bank rather than online memory writing, compression, or learned memory editing.

# Connections
- [[Search-Retrieval]]
- `evaluates` ALFWorld
- `evaluates` ScienceWorld
- `builds_on_unresolved` retrieval-augmented generation
- `builds_on_unresolved` LoRA
- `builds_on_unresolved` episodic memory
- `compares_to_unresolved` LoRA
- `compares_to_unresolved` training-free ExpRAG
- `compares_to_unresolved` ExpRAG-LoRA
<!-- GENERATED:END -->

## My Notes

