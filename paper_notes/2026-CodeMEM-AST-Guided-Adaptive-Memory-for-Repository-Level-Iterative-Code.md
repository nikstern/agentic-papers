---
paper_id: 52
title: "CodeMEM: AST-Guided Adaptive Memory for Repository-Level Iterative Code Generation"
year: 2026
authors: "Wang et al."
url: "https://arxiv.org/abs/2601.02868"
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
  - "repository-level iterative code generation"
  - "AST-guided memory"
  - "instruction following"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
CodeMEM introduces AST-guided adaptive memory for repository-level iterative code generation, maintaining both evolving code context and session-level interaction memory.

# Why It Matters
It is relevant because it shows that code-aware memory representations outperform generic text-style memory for iterative repository work.

# Method / Setup
The system uses a Code Context Memory and a Code Session Memory driven by AST-based analysis and LLM operations, and evaluates on CodeIF-Bench and CoderEval.

# Key Claims
- AST-guided memory improves instruction following and session-level consistency.
- The method reduces interaction rounds compared with baselines.
- Code-structured memory is more effective than natural-language-centric memory for iterative coding.

# Limitations
- The evaluation is oriented toward iterative code generation rather than bug investigation specifically.
- The method still depends on LLM judgment for filtering and updates.
- Broader validation on more complex repositories is still limited.

# Connections
- [[Software-Agents]]
- `evaluates` repository-level iterative code generation
- `evaluates` AST-guided memory
- `evaluates` instruction following
<!-- GENERATED:END -->

## My Notes

