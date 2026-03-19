---
paper_id: 11
title: "Position: Episodic Memory is the Missing Piece for Long-Term LLM Agents"
year: 2025
authors: "Pink et al."
url: "https://arxiv.org/abs/2502.06975"
paper_type: "position"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "episodic memory for agents"
  - "memory architecture gaps"
  - "long-term agent design"
builds_on:
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
compares_to: []
builds_on_unresolved:
  - "Complementary Learning Systems Theory"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---

# Summary
This position paper argues that episodic memory is the missing component for long-term LLM agents because it supports instance-specific, contextual, and single-shot learning that existing memory approaches only partially capture.

# Why It Matters
It sharpens the memory discussion from generic long-term storage toward a specific claim about what kinds of memory are needed for adaptive long-horizon agents.

# Method / Setup
The paper operationalizes episodic memory through properties such as long-term storage, explicit reasoning, single-shot learning, instance specificity, and contextual binding, then evaluates current in-context, external, and parametric memory approaches against that target.

# Key Claims
- Long-term LLM agents need episodic memory, not just larger context windows or static retrieval.
- Current memory approaches each cover only part of the episodic memory design space.
- A useful roadmap should center on encoding, retrieval, consolidation, and episodic evaluation benchmarks.

# Limitations
- It is a position paper rather than an implemented episodic memory system.
- The claims are conceptually strong but still await fuller end-to-end empirical validation.

# Connections
- [[Memory-Context]]
- `evaluates` episodic memory for agents
- `evaluates` memory architecture gaps
- `evaluates` long-term agent design
- `builds_on` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `builds_on_unresolved` Complementary Learning Systems Theory
