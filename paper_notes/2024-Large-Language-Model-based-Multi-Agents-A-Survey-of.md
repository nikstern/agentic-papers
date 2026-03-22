---
paper_id: 5
title: "Large Language Model based Multi-Agents: A Survey of Progress and Challenges"
year: 2024
authors: "Guo et al."
url: "https://arxiv.org/abs/2402.01680"
paper_type: "survey"
primary_topic: "llm-multi-agent-systems"
secondary_topics: []
status: "deep_read"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "llm-multi-agent-systems"
evaluates:
  - "llm multi-agent architectures"
  - "communication mechanisms"
  - "agent applications"
builds_on:
  - "[[2023-CAMEL-Communicative-Agents-for-Mind-Exploration-of-Large]]"
  - "[[2023-MetaGPT-Meta-Programming-for-A-Multi-Agent-Collaborative-Framework]]"
compares_to: []
builds_on_unresolved:
  - "Generative Agents"
compares_to_unresolved: []
relations: []
source: "manual"
---
<!-- GENERATED:START -->
# Summary
This survey organizes the progress of LLM-based multi-agent systems around agent environment interfaces, profiling choices, communication mechanisms, and capability acquisition strategies.

# Why It Matters
It is a useful early field map for positioning systems, surveys, and applications in the broader multi-agent literature before the taxonomy space became crowded.

# Method / Setup
The paper surveys applications in problem solving and world simulation, proposes a general architectural schema, and compares systems by environment, profiling, communication, feedback, and adaptation mechanisms.

# Key Claims
- LLM multi-agent systems should be analyzed through architecture, communication, and adaptation together.
- The field splits naturally into problem-solving systems and world-simulation systems.
- Specialization and interaction are the main reasons to use multiple agents instead of one.

# Limitations
- As an early survey, some later architectural patterns and benchmarks are not covered.
- It offers synthesis rather than direct empirical validation of any new system.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` llm multi-agent architectures
- `evaluates` communication mechanisms
- `evaluates` agent applications
- `builds_on` [[2023-CAMEL-Communicative-Agents-for-Mind-Exploration-of-Large]]
- `builds_on` [[2023-MetaGPT-Meta-Programming-for-A-Multi-Agent-Collaborative-Framework]]
- `builds_on_unresolved` Generative Agents
<!-- GENERATED:END -->

## My Notes
Useful survey for where things were at in 2023 and points in some useful other directions, but the field has likely advanced since then.

Signals importance of:
- [[2023-MetaGPT-Meta-Programming-for-A-Multi-Agent-Collaborative-Framework]]
- [[2023-CAMEL-Communicative-Agents-for-Mind-Exploration-of-Large]]
- [[2023-AgentBench-Evaluating-LLMs-as-Agents]]
- [[2023-Building-Cooperative-Embodied-Agents-Modularly-with-Large-Language]]
- [[2024-Scalable-Multi-Robot-Collaboration-with-Large-Language-Models-Centralized]]
- [[2023-RoCo-Dialectic-Multi-Robot-Collaboration-with-Large-Language-Models]]
- [[2023-A-Dynamic-LLM-Powered-Agent-Network-for-Task-Oriented-Agent]]
