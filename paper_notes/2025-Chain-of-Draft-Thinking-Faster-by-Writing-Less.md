---
paper_id: 35
title: "Chain of Draft: Thinking Faster by Writing Less"
year: 2025
authors: "Xu et al."
url: "https://arxiv.org/abs/2502.18600"
paper_type: "application"
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
  - "reasoning efficiency"
  - "prompt compression"
  - "multi-step reasoning"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Chain-of-Thought"
compares_to_unresolved:
  - "Concise Thoughts"
  - "TALE"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Chain of Draft prompts LLMs to produce only minimal intermediate drafts during reasoning, preserving multi-step problem solving while sharply reducing verbosity.

# Why It Matters
It is a practical efficiency paper for the vault because it shows that reasoning quality and token cost do not need to move together if intermediate traces are constrained well.

# Method / Setup
The method uses a system prompt and few-shot examples to elicit very short intermediate reasoning steps, then compares that style with direct prompting and chain-of-thought across arithmetic, commonsense, and symbolic tasks.

# Key Claims
- Minimal draft-style reasoning can retain most of CoT’s benefits at much lower token cost.
- Latency and inference cost can drop dramatically without fully abandoning explicit reasoning.
- The main gains are strongest on capable models and with well-chosen examples.

# Limitations
- Performance drops more on smaller models and in zero-shot settings.
- The method still relies on carefully designed few-shot demonstrations.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` reasoning efficiency
- `evaluates` prompt compression
- `evaluates` multi-step reasoning
- `builds_on_unresolved` Chain-of-Thought
- `compares_to_unresolved` Concise Thoughts
- `compares_to_unresolved` TALE
<!-- GENERATED:END -->

## My Notes

