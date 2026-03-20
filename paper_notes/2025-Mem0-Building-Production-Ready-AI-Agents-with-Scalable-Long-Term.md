---
paper_id: 37
title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
year: 2025
authors: "Chhikara et al."
url: "https://arxiv.org/abs/2504.19413"
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
  - "long-term conversational memory"
  - "memory latency and token efficiency"
  - "multi-hop and temporal memory retrieval"
builds_on:
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
compares_to:
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
  - "[[2025-Zep-A-Temporal-Knowledge-Graph-Architecture-for-Agent]]"
builds_on_unresolved:
  - "Retrieval-Augmented Generation"
compares_to_unresolved:
  - "LoCoMo"
  - "ReadAgent"
  - "MemoryBank"
  - "LangMem"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Mem0 introduces production-oriented long-term memory architectures for LLM agents that extract salient facts from conversations and update memory incrementally instead of relying on full context or raw-history retrieval.

# Why It Matters
It is a strong practical baseline for the vault because it emphasizes deployment trade-offs such as latency, token cost, and scalable retrieval while directly comparing against MemGPT-era memory systems.

# Method / Setup
The paper presents Mem0 and a graph-based variant Mem0g, uses LLM-based extraction and memory update operations over external memory stores, and evaluates them on the LOCOMO benchmark across single-hop, multi-hop, temporal, and open-domain question types against multiple memory baselines.

# Key Claims
- Selective memory extraction and updating can outperform raw-history and many retrieval baselines for long-term conversational memory.
- Mem0 delivers strong accuracy with substantially lower latency and token cost than full-context approaches.
- Graph-based memory improves some relational and temporal tasks but increases storage and system overhead.

# Limitations
- The full-context setting still achieves the highest overall score, showing that external memory does not fully eliminate information loss.
- The graph-based variant roughly doubles memory footprint and can introduce substantial operational overhead compared with the simpler natural-language memory.
- Performance varies by question type, with some advantages narrowing on open-domain settings.

# Connections
- [[Memory-Context]]
- `evaluates` long-term conversational memory
- `evaluates` memory latency and token efficiency
- `evaluates` multi-hop and temporal memory retrieval
- `builds_on` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `compares_to` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `compares_to` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `compares_to` [[2025-Zep-A-Temporal-Knowledge-Graph-Architecture-for-Agent]]
- `builds_on_unresolved` Retrieval-Augmented Generation
- `compares_to_unresolved` LoCoMo
- `compares_to_unresolved` ReadAgent
- `compares_to_unresolved` MemoryBank
- `compares_to_unresolved` LangMem
<!-- GENERATED:END -->

## My Notes

