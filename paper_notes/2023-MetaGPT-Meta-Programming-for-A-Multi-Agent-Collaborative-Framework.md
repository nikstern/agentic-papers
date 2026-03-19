---
paper_id: 2
title: "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework"
year: 2023
authors: "Hong et al."
url: "https://arxiv.org/abs/2308.00352"
paper_type: "system"
primary_topic: "llm-multi-agent-systems"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "llm-multi-agent-systems"
evaluates:
  - "software generation"
  - "multi-agent software engineering"
  - "code benchmark performance"
builds_on: []
compares_to:
  - "[[2023-ChatDev-Communicative-Agents-for-Software-Development]]"
builds_on_unresolved:
  - "Chain-of-Thought"
  - "ReAct"
compares_to_unresolved:
  - "AutoGPT"
  - "LangChain"
relations: []
source: "manual"
---
<!-- GENERATED:START -->
# Summary
MetaGPT frames software development as a structured multi-agent workflow in which specialized agents produce requirements, architecture, task decomposition, implementation, and review artifacts through standardized handoffs.

# Why It Matters
It is a foundational systems paper for agentic software engineering because it shows how role specialization and explicit process structure can make multi-agent coding materially more reliable than ad hoc prompting.

# Method / Setup
The system models a software company with roles such as product manager, architect, project manager, engineer, and QA engineer, uses structured artifacts instead of free-form dialogue, and evaluates performance on HumanEval, MBPP, and a SoftwareDev benchmark with executable feedback loops.

# Key Claims
- Structured operating procedures improve multi-agent software generation.
- Role-specialized agents outperform looser agent collaboration baselines on coding tasks.
- Executable feedback materially improves code quality and task completion.

# Limitations
- The framework is tailored mainly to software engineering workflows.
- Its gains depend on careful workflow design and a strong underlying model.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` software generation
- `evaluates` multi-agent software engineering
- `evaluates` code benchmark performance
- `compares_to` [[2023-ChatDev-Communicative-Agents-for-Software-Development]]
- `builds_on_unresolved` Chain-of-Thought
- `builds_on_unresolved` ReAct
- `compares_to_unresolved` AutoGPT
- `compares_to_unresolved` LangChain
<!-- GENERATED:END -->

## My Notes

