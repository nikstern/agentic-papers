---
paper_id: 45
title: "MemWeaver: Weaving Hybrid Memories for Traceable Long-Horizon Agentic Reasoning"
year: 2026
authors: "Ye et al."
url: "https://arxiv.org/abs/2601.18204"
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
  - "traceable long-horizon reasoning"
  - "hybrid memory retrieval"
  - "temporal and compositional QA"
builds_on:
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
compares_to:
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
builds_on_unresolved:
  - "MemoryBank"
  - "ReadAgent"
  - "knowledge graph memory"
compares_to_unresolved:
  - "LoCoMo"
  - "MemoryBank"
  - "ReadAgent"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
MemWeaver combines graph memory, experience memory, and passage memory so agents can retrieve structured facts, abstractions, and raw evidence together for long-horizon reasoning.

# Why It Matters
It is a strong hybrid-memory paper for context engineering because it focuses on traceable, compositional, and temporally grounded context assembly.

# Method / Setup
The system writes temporally grounded relations into graph memory, induces reusable abstractions into experience memory, preserves raw passages for evidence, and retrieves through dual structured and textual channels; evaluation is on LoCoMo across several backbone models.

# Key Claims
- Hybrid memory layers produce better long-term reasoning than relying on a single memory representation.
- Temporal grounding and graph structure are especially important for multi-hop and temporal questions.
- Dual-channel retrieval can improve reasoning quality while keeping inference context short.

# Limitations
- Memory construction quality still depends on LLM extraction quality for entities, relations, and abstractions.
- The current framework is primarily text-centric rather than multimodal.
- The architecture is more elaborate than simpler flat retrieval systems.

# Connections
- [[Memory-Context]]
- `evaluates` traceable long-horizon reasoning
- `evaluates` hybrid memory retrieval
- `evaluates` temporal and compositional QA
- `builds_on` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `compares_to` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `builds_on_unresolved` MemoryBank
- `builds_on_unresolved` ReadAgent
- `builds_on_unresolved` knowledge graph memory
- `compares_to_unresolved` LoCoMo
- `compares_to_unresolved` MemoryBank
- `compares_to_unresolved` ReadAgent
<!-- GENERATED:END -->

## My Notes

