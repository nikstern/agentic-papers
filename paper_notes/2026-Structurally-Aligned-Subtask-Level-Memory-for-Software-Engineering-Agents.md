---
paper_id: 49
title: "Structurally Aligned Subtask-Level Memory for Software Engineering Agents"
year: 2026
authors: "Shen et al."
url: "https://arxiv.org/abs/2602.21611"
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
  - "software engineering agent memory"
  - "subtask-level retrieval"
  - "SWE-bench Verified"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "SWE-Agent"
compares_to_unresolved:
  - "Reasoning-Bank"
  - "vanilla agent"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper argues that SWE-agent memory should be stored and retrieved at the subtask level rather than as coarse whole-instance episodes.

# Why It Matters
It is one of the cleanest empirical papers showing that better memory granularity materially improves software engineering agents on long-horizon tasks.

# Method / Setup
The method segments work into analyze, reproduce, edit, and verify subtasks, stores structured subtask experiences, retrieves memories by category and semantic intent, and evaluates on SWE-bench Verified across multiple LLM backbones.

# Key Claims
- Subtask-level memory consistently improves Pass@1 over vanilla agents.
- Fine-grained memory reduces reasoning interference seen in instance-level memory.
- Benefits grow on harder, longer-horizon software engineering tasks.

# Limitations
- The method has a cold-start period before enough useful memory accumulates.
- The task decomposition scheme is hand-designed around a fixed set of subtasks.
- Results are centered on SWE-bench Verified rather than diverse engineering workflows.

# Connections
- [[Software-Agents]]
- `evaluates` software engineering agent memory
- `evaluates` subtask-level retrieval
- `evaluates` SWE-bench Verified
- `builds_on_unresolved` SWE-Agent
- `compares_to_unresolved` Reasoning-Bank
- `compares_to_unresolved` vanilla agent
<!-- GENERATED:END -->

## My Notes

