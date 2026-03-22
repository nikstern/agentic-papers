---
paper_id: 58
title: "Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach"
year: 2025
authors: "Geiping et al."
url: "https://arxiv.org/abs/2502.05171"
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
  - "latent reasoning"
  - "recurrent depth"
  - "math and coding benchmarks"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "Chain-of-Thought"
  - "fixed-depth transformers"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper introduces a recurrent-depth language model that scales reasoning by iterating a latent recurrent block at test time rather than relying on explicit chain-of-thought.

# Why It Matters
It is a major adjacent paper for the broader recursion/recurrence cluster because it proposes test-time compute scaling through latent recurrence.

# Method / Setup
The architecture has a prelude, recurrent core, and coda, is trained from scratch with randomized iteration counts and truncated backpropagation, and is evaluated on general, math, and coding benchmarks.

# Key Claims
- Increasing recurrent depth at test time improves reasoning performance.
- Latent recurrence can act as a third scaling axis besides parameter count and explicit CoT.
- Recurrent-depth models show useful emergent behaviors such as adaptive compute.

# Limitations
- The method requires specialized architecture and large-scale training.
- It is recurrence in latent space rather than exact recursive language modeling.
- The systems work is substantial and may be difficult to reproduce.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` latent reasoning
- `evaluates` recurrent depth
- `evaluates` math and coding benchmarks
- `compares_to_unresolved` Chain-of-Thought
- `compares_to_unresolved` fixed-depth transformers
<!-- GENERATED:END -->

## My Notes

