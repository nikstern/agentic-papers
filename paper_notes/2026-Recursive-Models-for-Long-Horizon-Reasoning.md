---
paper_id: 55
title: "Recursive Models for Long-Horizon Reasoning"
year: 2026
authors: "Yang et al."
url: "https://arxiv.org/abs/2603.02112"
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
  - "long-horizon reasoning theory"
  - "recursive computation"
  - "SAT solving"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "summarization"
  - "single-context autoregressive models"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper gives a formal account of recursive models for long-horizon reasoning and argues that deep recursion is the key mechanism for overcoming bounded active context.

# Why It Matters
It provides the theoretical backbone for the exact RLM direction and clarifies why deep recursion can be exponentially more powerful than shallow context-management strategies.

# Method / Setup
The paper formalizes recursive models with call and return operations over a context stack, analyzes their computational power relative to autoregressive and summarization-based systems, and validates the approach on SAT with a recursively trained 3B model.

# Key Claims
- Deep recursion can reduce active-context requirements exponentially for some problems.
- Constant-depth recursion offers little advantage over summarization-style context management.
- Minimal recursive models are already optimally powerful within a broad recursive agentic framework.

# Limitations
- The main contribution is theoretical rather than broad application benchmarking.
- Naive recursive simulation can be computationally expensive.
- The abstractions do not map perfectly onto all practical LLM system details.

# Connections
- [[Memory-Context]]
- `evaluates` long-horizon reasoning theory
- `evaluates` recursive computation
- `evaluates` SAT solving
- `compares_to_unresolved` summarization
- `compares_to_unresolved` single-context autoregressive models
<!-- GENERATED:END -->

## My Notes

