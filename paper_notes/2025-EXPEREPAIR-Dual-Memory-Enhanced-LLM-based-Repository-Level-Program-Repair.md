---
paper_id: 47
title: "EXPEREPAIR: Dual-Memory Enhanced LLM-based Repository-Level Program Repair"
year: 2025
authors: "Mu et al."
url: "https://arxiv.org/abs/2506.10484"
paper_type: "system"
primary_topic: "software-agents"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "software-agents"
evaluates:
  - "repository-level program repair"
  - "experience-driven bug fixing"
  - "SWE-Bench Lite"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "SWE-Agent"
  - "ReAct"
compares_to_unresolved:
  - "PatchPilot"
  - "OpenHands"
  - "Agentless"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
EXPEREPAIR introduces a repository-level program repair system that continuously learns from prior repair trajectories through a dual-memory design.

# Why It Matters
It is one of the most directly relevant papers for memory in code investigation because it shows concrete gains from reusing past repair experience on SWE tasks.

# Method / Setup
The system combines episodic demonstrations and semantic repair insights, injects them into test generation and patch generation, and evaluates on SWE-Bench Lite against strong open-source repair baselines.

# Key Claims
- Dual-memory experience reuse improves repository-level bug repair.
- Episodic demonstrations contribute more than semantic insights, but both help.
- The approach reaches state-of-the-art open-source performance with favorable cost efficiency.

# Limitations
- Evidence is concentrated on SWE-Bench Lite rather than a broader suite of repositories and languages.
- The approach depends on the quality of stored successful trajectories.
- The system still relies on strong base agents for localization and patch generation.

# Connections
- [[Software-Agents]]
- `evaluates` repository-level program repair
- `evaluates` experience-driven bug fixing
- `evaluates` SWE-Bench Lite
- `builds_on_unresolved` SWE-Agent
- `builds_on_unresolved` ReAct
- `compares_to_unresolved` PatchPilot
- `compares_to_unresolved` OpenHands
- `compares_to_unresolved` Agentless
<!-- GENERATED:END -->

## My Notes

