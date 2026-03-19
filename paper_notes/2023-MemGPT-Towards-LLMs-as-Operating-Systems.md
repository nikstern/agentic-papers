---
paper_id: 15
title: "MemGPT: Towards LLMs as Operating Systems"
year: 2023
authors: "Packer et al."
url: "https://arxiv.org/abs/2310.08560"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "long-horizon dialogue"
  - "document question answering"
  - "memory-managed llm agents"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Retrieval-Augmented Generation"
  - "virtual memory"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---

# Summary
MemGPT treats the LLM context window as a managed memory hierarchy, letting the model move information between working context and external storage much like an operating system handles virtual memory.

# Why It Matters
It is a foundational systems paper for long-term memory in agents because it reframes context management as an explicit memory-management problem rather than a larger-window problem.

# Method / Setup
The system divides memory into system instructions, working context, message history, and external archival stores, exposes memory-management functions to the model, and evaluates long conversations and document tasks.

# Key Claims
- Fixed-context LLMs can simulate effectively unbounded context through explicit memory management.
- Self-managed external memory improves long-term consistency and retrieval.
- Operating-system analogies are useful for designing LLM agent memory.

# Limitations
- The method adds orchestration complexity and depends on reliable memory-control behavior.
- Its gains depend on external storage and retrieval quality rather than model weights alone.

# Connections
- [[Memory-Context]]
- `evaluates` long-horizon dialogue
- `evaluates` document question answering
- `evaluates` memory-managed llm agents
- `builds_on_unresolved` Retrieval-Augmented Generation
- `builds_on_unresolved` virtual memory
