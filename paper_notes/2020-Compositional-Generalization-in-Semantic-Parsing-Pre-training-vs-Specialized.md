---
paper_id: 120
title: "Compositional Generalization in Semantic Parsing: Pre-training vs. Specialized Architectures"
year: 2020
authors: "Furrer et al."
url: "https://arxiv.org/abs/2007.08970"
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
  - "Masked language model (MLM) pre-training"
  - "SCAN-inspired architectures for compositional generalization"
  - "Architectures from the area of algorithm learning"
  - "Combination of MLM pre-training with intermediate representations"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "SCAN dataset benchmarks"
  - "CFQ dataset benchmarks"
compares_to_unresolved:
  - "Specialized architectures proposed for compositional generalization in SCAN"
  - "Algorithm learning architectures designed for compositional generalization"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper evaluates the effectiveness of masked language model (MLM) pre-training against specialized architectures for improving compositional generalization in semantic parsing tasks, using SCAN and CFQ datasets. Results reveal MLM pre-training significantly outperforms specialized architectures on complex compositional tasks, establishing a new state of the art on the CFQ benchmark.

# Why It Matters
Compositional generalization is critical for semantic parsing and natural language understanding, yet most methods struggle with it; this work highlights the superior impact of pre-training methods, influencing future model design.

# Method / Setup
The study compares performance of MLM-pre-trained models and architecture variants inspired by SCAN and algorithm learning on primitive and complex compositional splits of SCAN and CFQ datasets, measuring semantic parsing accuracy.

# Key Claims
- MLM pre-training rivals SCAN-inspired architectures on primitive holdout datasets.
- On complex compositional tasks, MLM pre-training significantly improves performance over comparable non-pre-trained models.
- Specialized architectures from SCAN and algorithm learning literature do not yield significant improvements on complex compositional generalization.
- Combining MLM pre-training with an intermediate representation achieves a new state of the art on the CFQ benchmark.

# Limitations
- The study focuses on SCAN and CFQ datasets, which may limit generalizability to other semantic parsing tasks.
- The paper does not explore the effect of combining pre-training with specialized architectures extensively.
- Limited analysis on why certain specialized architectures fail to improve performance.
- Results may depend on specific model configurations and hyperparameters not fully explored.

# Connections
- [[Agent-Evaluation]]
- `evaluates` Masked language model (MLM) pre-training
- `evaluates` SCAN-inspired architectures for compositional generalization
- `evaluates` Architectures from the area of algorithm learning
- `evaluates` Combination of MLM pre-training with intermediate representations
- `builds_on_unresolved` SCAN dataset benchmarks
- `builds_on_unresolved` CFQ dataset benchmarks
- `compares_to_unresolved` Specialized architectures proposed for compositional generalization in SCAN
- `compares_to_unresolved` Algorithm learning architectures designed for compositional generalization
<!-- GENERATED:END -->

## My Notes

