---
paper_id: 17
title: "INMS: Memory Sharing for Large Language Model based Agents"
year: 2024
authors: "Gao and Zhang"
url: "https://arxiv.org/abs/2404.09982"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "open-ended question answering"
  - "shared memory for multi-agent learning"
builds_on:
  - "[[2023 - MemGPT Towards LLMs as Operating Systems]]"
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "Retrieval-Augmented Generation"
  - "MemoryBank"
relations: []
source: "alphaxiv-mcp"
---

# Summary
INMS proposes a shared memory framework for LLM-based agents where agents generate, evaluate, retrieve, and reuse high-quality prompt-answer memories to improve collective performance on open-ended tasks.

# Why It Matters
It is the most directly relevant systems paper in the vault for shared memory across LLM agents and collective enhancement.

# Method / Setup
The framework stores high-quality prompt-answer pairs in a shared memory pool, retrieves them with a continuously trained dense retriever, and evaluates performance across literary creation, unconventional logic, and plan generation domains.

# Key Claims
- Shared memory among agents improves performance on open-ended tasks.
- Three-shot retrieval from the shared memory pool often works best.
- The framework can help open-source models outperform stronger zero-shot closed models in some settings.

# Limitations
- The evaluation focuses on a few synthetic or curated domains rather than broad real-world deployments.
- Benefits are strongest when memories are domain-relevant rather than drawn from a single global pool.

# Connections
- [[Memory Context]]
- `evaluates` open-ended question answering
- `evaluates` shared memory for multi-agent learning
- `builds_on` [[2023 - MemGPT Towards LLMs as Operating Systems]]
- `compares_to_unresolved` Retrieval-Augmented Generation
- `compares_to_unresolved` MemoryBank
