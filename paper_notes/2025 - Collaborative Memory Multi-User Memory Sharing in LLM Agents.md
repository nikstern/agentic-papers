---
paper_id: 19
title: "Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control"
year: 2025
authors: "Rezazadeh et al."
url: "https://arxiv.org/abs/2505.18279"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "multi-user collaborative memory"
  - "dynamic access-controlled sharing"
builds_on:
  - "[[2023 - MemGPT Towards LLMs as Operating Systems]]"
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "Memory Sharing for Large Language Model based Agents"
  - "MemTree"
relations: []
source: "alphaxiv-mcp"
---

# Summary
Collaborative Memory proposes a multi-user, multi-agent memory framework with private and shared memory tiers governed by dynamic access control, enabling secure memory sharing under changing permissions.

# Why It Matters
It extends shared-memory design toward enterprise-grade constraints by making access control and provenance central to the memory substrate.

# Method / Setup
The framework uses dynamic user-agent and agent-resource access graphs, read and write policies, and provenance-aware memory fragments; it is evaluated in collaborative scenarios with unrestricted, asymmetric, and evolving access permissions.

# Key Claims
- Controlled memory sharing reduces redundant retrieval and external calls without harming accuracy.
- The system can adapt to changing permissions while preserving strict access boundaries.
- Provable auditability and policy-aware sharing are feasible within a collaborative memory substrate.

# Limitations
- The evaluation is based on controlled or synthetic scenarios rather than a live enterprise environment.
- The framework still depends on LLM components that may hallucinate or mishandle policy edge cases.

# Connections
- [[Memory Context]]
- `evaluates` multi-user collaborative memory
- `evaluates` dynamic access-controlled sharing
- `builds_on` [[2023 - MemGPT Towards LLMs as Operating Systems]]
- `compares_to_unresolved` Memory Sharing for Large Language Model based Agents
- `compares_to_unresolved` MemTree
