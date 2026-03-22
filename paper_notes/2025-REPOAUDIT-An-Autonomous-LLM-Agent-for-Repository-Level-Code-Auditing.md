---
paper_id: 78
title: "REPOAUDIT: An Autonomous LLM-Agent for Repository-Level Code Auditing"
year: 2025
authors: "Guo et al."
url: "https://arxiv.org/abs/2501.18160"
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
  - "repository-level code auditing"
  - "null pointer dereference detection"
  - "memory leak detection"
  - "use-after-free detection"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "LLMDFA"
  - "LLMSAN"
compares_to_unresolved:
  - "Meta INFER"
  - "Amazon CodeGuru"
  - "LLMDFA"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
RepoAudit is an autonomous LLM agent for repository-level code auditing that explores code on demand, reasons over feasible program paths, and validates bug reports before returning them. It is designed to detect non-local repository bugs without requiring compilation.

# Why It Matters
It is directly relevant to software agents because it shows how an LLM agent can navigate large repositories and do path-sensitive analysis with useful precision.

# Method / Setup
Repository-level auditing agent with an initiator, explorer, validator, agent memory, and parser, evaluated on real-world repositories for null pointer dereference, memory leak, and use-after-free bugs.

# Key Claims
- Demand-driven repository exploration makes LLM-based code auditing substantially more scalable than direct end-to-end prompting.
- Validation of inferred facts and path feasibility materially reduces hallucinated bug reports.
- The system can find real inter-procedural repository bugs without depending on compilation or heavy traditional static-analysis pipelines.

# Limitations
- The method still depends on multiple iterative LLM calls and can become expensive on very large repositories.
- Its soundness is limited by the quality of LLM reasoning and the bounded inter-procedural exploration depth.

# Connections
- [[Software-Agents]]
- `evaluates` repository-level code auditing
- `evaluates` null pointer dereference detection
- `evaluates` memory leak detection
- `evaluates` use-after-free detection
- `builds_on_unresolved` LLMDFA
- `builds_on_unresolved` LLMSAN
- `compares_to_unresolved` Meta INFER
- `compares_to_unresolved` Amazon CodeGuru
- `compares_to_unresolved` LLMDFA
<!-- GENERATED:END -->

## My Notes

