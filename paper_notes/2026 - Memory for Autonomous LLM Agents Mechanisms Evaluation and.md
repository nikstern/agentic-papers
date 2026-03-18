---
paper_id: 28
title: Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers
year: 2026
authors: Du
url: https://arxiv.org/abs/2603.07670
paper_type: survey
primary_topic: memory-context
secondary_topics: []
status: ingested
tags: [papers, memory-context]
evaluates:
  - agent memory mechanisms
  - memory evaluation
  - memory engineering trade-offs
builds_on: []
compares_to: []
builds_on_unresolved:
  - ReAct
  - Reflexion
  - Generative Agents
  - Memory Networks
  - Neural Turing Machines
  - Differentiable Neural Computers
  - RAG
  - RETRO
  - Voyager
compares_to_unresolved:
  - MemBench
  - MemoryAgentBench
  - MemoryArena
  - LoCoMo
  - Agentic Memory
relations: []
source: alphaxiv-mcp
---

# Summary
This survey studies memory as the central module that turns stateless LLMs into adaptive agents, proposing a structured taxonomy for temporal scope, representational substrate, control policy, and evaluation.

# Why It Matters
It is one of the strongest new memory overviews for the vault because it connects design mechanisms, engineering trade-offs, and agent-level evaluation in one place.

# Method / Setup
The paper formalizes memory in the agent loop, surveys context-resident memory, retrieval-augmented memory, reflective memory, hierarchical memory, and learned memory control, and reviews recent memory benchmarks and deployment concerns.

# Key Claims
- Memory should be treated as a first-class systems module rather than as a minor add-on to prompting.
- Long context alone is not a substitute for explicit memory design and retrieval control.
- Agent memory should be evaluated through downstream agent performance, efficiency, and governance, not only retrieval quality.

# Limitations
- As a survey, it organizes and interprets the field but does not directly validate a new memory architecture.
- The paper also notes that memory evaluation remains fragmented and that standardized cross-paper comparisons are still immature.

# Connections
- [[Memory Context]]
- `evaluates` agent memory mechanisms
- `evaluates` memory evaluation
- `evaluates` memory engineering trade-offs
- `builds_on_unresolved` ReAct
- `builds_on_unresolved` Reflexion
- `builds_on_unresolved` Generative Agents
- `builds_on_unresolved` Memory Networks
- `builds_on_unresolved` Neural Turing Machines
- `builds_on_unresolved` Differentiable Neural Computers
- `builds_on_unresolved` RAG
- `builds_on_unresolved` RETRO
- `builds_on_unresolved` Voyager
- `compares_to_unresolved` MemBench
- `compares_to_unresolved` MemoryAgentBench
- `compares_to_unresolved` MemoryArena
- `compares_to_unresolved` LoCoMo
- `compares_to_unresolved` Agentic Memory
