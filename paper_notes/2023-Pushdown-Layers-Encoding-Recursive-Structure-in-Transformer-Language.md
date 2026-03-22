---
paper_id: 59
title: "Pushdown Layers: Encoding Recursive Structure in Transformer Language Models"
year: 2023
authors: "Murty et al."
url: "https://arxiv.org/abs/2310.19089"
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
  - "recursive structure modeling"
  - "syntactic generalization"
  - "Dyck languages"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "Transformer Grammars"
  - "standard Transformer LM"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Pushdown Layers adds an explicit stack-like mechanism to Transformer self-attention to better capture recursive syntactic structure.

# Why It Matters
It is a useful foundational recursion paper because it shows one way to encode recursive state explicitly inside Transformer language modeling.

# Method / Setup
The method augments self-attention with a stack tape tracking estimated token depths in an incremental parse and evaluates on Dyck strings, syntactic generalization benchmarks, and GPT-2 fine-tuning experiments.

# Key Claims
- Explicit stack-style state improves recursive syntactic generalization.
- Pushdown Layers are more sample-efficient than standard self-attention on several recursion-sensitive tasks.
- A soft structural bias can improve recursive modeling without hard attention constraints.

# Limitations
- The approach depends on parse supervision or silver parses.
- It is focused mainly on syntactic recursion rather than general long-horizon agent reasoning.
- Applicability outside parse-structured language settings is limited.

# Connections
- [[Memory-Context]]
- `evaluates` recursive structure modeling
- `evaluates` syntactic generalization
- `evaluates` Dyck languages
- `compares_to_unresolved` Transformer Grammars
- `compares_to_unresolved` standard Transformer LM
<!-- GENERATED:END -->

## My Notes

