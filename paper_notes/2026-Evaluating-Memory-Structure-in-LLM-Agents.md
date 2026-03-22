---
paper_id: 46
title: "Evaluating Memory Structure in LLM Agents"
year: 2026
authors: "Shutova et al."
url: "https://arxiv.org/abs/2602.11243"
paper_type: "benchmark"
primary_topic: "agent-evaluation"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "agent-evaluation"
evaluates:
  - "memory structure evaluation"
  - "state tracking"
  - "tree reasoning and counting over long-term memory"
builds_on:
  - "[[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]"
compares_to:
  - "[[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]"
builds_on_unresolved:
  - "LoCoMo"
  - "LongMemEval"
compares_to_unresolved:
  - "retrieval-augmented LLM"
  - "Mem-agent"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
StructMemEval introduces benchmark tasks that test whether an LLM agent can organize memory into useful structures rather than merely retrieve isolated facts.

# Why It Matters
It matters for context engineering because it changes the evaluation target from recall alone to memory organization quality, which is central to durable context systems.

# Method / Setup
The benchmark contains tree-structured, state-tracking, and counting problems and evaluates retrieval baselines plus memory-agent frameworks with and without explicit organization hints.

# Key Claims
- Many existing memory evaluations are too easy for simple retrieval and do not discriminate complex memory structures well.
- Current memory agents often fail not because they cannot execute structured reasoning, but because they do not spontaneously organize memory correctly.
- Providing memory-organization hints reveals a large gap between structure recognition and structure execution.

# Limitations
- The benchmark is synthetic and explicitly marked as work in progress.
- It focuses on structured organization tasks rather than broad real-world assistant behavior.
- Results may shift as the benchmark suite is expanded.

# Connections
- [[Agent-Evaluation]]
- `evaluates` memory structure evaluation
- `evaluates` state tracking
- `evaluates` tree reasoning and counting over long-term memory
- `builds_on` [[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]
- `compares_to` [[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]
- `builds_on_unresolved` LoCoMo
- `builds_on_unresolved` LongMemEval
- `compares_to_unresolved` retrieval-augmented LLM
- `compares_to_unresolved` Mem-agent
<!-- GENERATED:END -->

## My Notes

