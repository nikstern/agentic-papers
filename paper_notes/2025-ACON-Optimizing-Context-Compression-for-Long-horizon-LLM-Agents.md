---
paper_id: 85
title: "ACON: Optimizing Context Compression for Long-horizon LLM Agents"
year: 2025
authors: "Kang et al."
url: "https://arxiv.org/abs/2510.00615"
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
  - "AppWorld"
  - "OfficeBench"
  - "8-objective QA"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "LLMLingua"
  - "retrieval-augmented generation"
  - "dialogue memory summarization"
compares_to_unresolved:
  - "FIFO"
  - "Retrieval"
  - "LLMLingua"
  - "naive prompting"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
ACON proposes a unified framework for compressing both interaction histories and observations in long-horizon LLM agents by optimizing natural-language compression guidelines and then distilling the compressor into smaller models.

# Why It Matters
It is a strong context-engineering paper because it treats compression quality as an optimizable policy learned from task failures rather than a static summarization prompt.

# Method / Setup
ACON alternates between utility-maximizing and compression-maximizing prompt optimization for a compressor LLM, then distills the optimized compressor into smaller models and evaluates the system on AppWorld, OfficeBench, and 8-objective QA.

# Key Claims
- Natural-language compression guidelines can be optimized to preserve task performance while sharply reducing context load.
- Smaller LLM agents benefit substantially when long histories are compressed into more relevant state representations.
- A distilled compressor can retain most of the teacher compressor's gains at much lower cost.

# Limitations
- Total API cost does not always decrease because compression itself can add inference overhead, especially for history compression.
- The approach relies on LLM-based prompt optimization and evaluation rather than formal guarantees about semantic preservation.

# Connections
- [[Memory-Context]]
- `evaluates` AppWorld
- `evaluates` OfficeBench
- `evaluates` 8-objective QA
- `builds_on_unresolved` LLMLingua
- `builds_on_unresolved` retrieval-augmented generation
- `builds_on_unresolved` dialogue memory summarization
- `compares_to_unresolved` FIFO
- `compares_to_unresolved` Retrieval
- `compares_to_unresolved` LLMLingua
- `compares_to_unresolved` naive prompting
<!-- GENERATED:END -->

## My Notes

