---
paper_id: 54
title: "Recursive Language Models"
year: 2025
authors: "Zhang et al."
url: "https://arxiv.org/abs/2512.24601"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "long-context reasoning"
  - "recursive prompt processing"
  - "LongBench-v2 CodeQA"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "CodeAct"
  - "summary agent"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Recursive Language Models proposes an inference-time framework in which an LLM treats long prompts as an external environment and recursively calls itself over prompt fragments.

# Why It Matters
It is the core exact-RLM paper and a direct attempt to scale effective context and reasoning depth without retraining the base model for longer context windows.

# Method / Setup
The method places the prompt inside a REPL environment, lets the LLM write code to inspect and transform prompt slices, and supports recursive self-calls over subproblems; it is evaluated on long-context tasks such as BrowseComp-Plus, OOLONG, and LongBench-v2 CodeQA.

# Key Claims
- RLMs can process inputs far beyond the base model context window.
- Programmatic prompt access plus recursive sub-calls outperform common long-context scaffolds on several tasks.
- Inference-time recursion is a viable scaling axis for long-horizon reasoning.

# Limitations
- Inference cost can vary substantially depending on trajectory length.
- Base models can still be preferable on smaller-context tasks.
- Performance and behavior depend on the underlying model used inside the scaffold.

# Connections
- [[Memory-Context]]
- `evaluates` long-context reasoning
- `evaluates` recursive prompt processing
- `evaluates` LongBench-v2 CodeQA
- `compares_to_unresolved` CodeAct
- `compares_to_unresolved` summary agent
<!-- GENERATED:END -->

## My Notes

