---
paper_id: 25
title: "A Survey on Agent-as-a-Judge"
year: 2026
authors: "You et al."
url: "https://arxiv.org/abs/2601.05111"
paper_type: "survey"
primary_topic: "agent-evaluation"
secondary_topics: []
status: "discarded"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "agent-evaluation"
evaluates:
  - "agentic evaluation"
  - "llm judges"
  - "evaluation system design"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "MT-Bench"
  - "G-Eval"
  - "Prometheus"
  - "JudgeLM"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This survey traces the shift from LLM-as-a-judge to Agent-as-a-Judge, where evaluation systems use planning, tools, memory, and multi-agent collaboration to produce more robust judgments.

# Why It Matters
It is a strong evaluation-layer reference for the vault because it treats judging as an agentic systems problem rather than a single-model scoring prompt.

# Method / Setup
The paper proposes a developmental taxonomy from procedural to reactive to self-evolving judge agents, organizes the space by collaboration, planning, tool use, memory, and optimization, and surveys general and professional application domains.

# Key Claims
- Agentic evaluation can mitigate weaknesses of single-pass LLM judges.
- Planning, tools, and memory make evaluation more verifiable and adaptable.
- The field is moving toward more autonomous and self-improving judge systems.

# Limitations
- It is a survey and roadmap rather than a single benchmarked evaluation system.
- Many judge-agent claims still depend on application-specific implementations.

# Connections
- [[Agent-Evaluation]]
- `evaluates` agentic evaluation
- `evaluates` llm judges
- `evaluates` evaluation system design
- `builds_on_unresolved` MT-Bench
- `builds_on_unresolved` G-Eval
- `builds_on_unresolved` Prometheus
- `builds_on_unresolved` JudgeLM
<!-- GENERATED:END -->

## My Notes
