---
paper_id: 82
title: "SELF: Self-Evolution with Language Feedback"
year: 2023
authors: "Jianqiao Lu, Wanjun Zhong, Wenyong Huang, Yufei Wang, Qi Zhu, Fei Mi, Baojun Wang, Weichao Wang, Xingshan Zeng, Lifeng Shang, Xin Jiang, Qun Liu"
url: "https://arxiv.org/abs/2310.00533"
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
  - "self-evolution with language feedback"
  - "self-refinement"
  - "iterative self-training"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "RLHF"
  - "Self-Refine"
  - "self-consistency"
compares_to_unresolved:
  - "RLHF"
  - "pseudo-labeled fine-tuning"
  - "self-refinement at inference time"
  - "self-consistency"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
SELF proposes a two-stage framework in which an LLM first learns meta-skills for self-feedback and self-refinement, then uses those skills to generate, filter, and train on its own improved data. The system aims to make continuous self-evolution possible without ongoing human supervision.

# Why It Matters
It is a canonical positive self-evolution paper for the vault because it treats natural-language feedback as a training signal and shows that smaller models can acquire usable self-refinement behavior. It provides a useful counterpoint to later papers that question how faithful or robust self-evolution really is.

# Method / Setup
The framework first builds a meta-skill corpus with a stronger external annotator, then fine-tunes the base model to produce self-feedback and refined answers. In the second phase, the model iteratively generates responses on unlabeled prompts, filters them using its own feedback, and fine-tunes on the retained refinements; evaluation is on math and general instruction benchmarks.

# Key Claims
- Natural-language self-feedback can support meaningful self-evolution beyond scalar-reward style supervision.
- SELF can teach smaller language models to perform useful self-refinement at inference time.
- Iterative self-generated data curation can improve both mathematical reasoning and general instruction-following quality.

# Limitations
- The method still depends on a strong external model to bootstrap the initial meta-skill corpus.
- Performance gains are benchmark-based and do not establish robust autonomous improvement in open-world settings.
- The iterative loop can inherit errors or drift if self-generated feedback quality is poor.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` self-evolution with language feedback
- `evaluates` self-refinement
- `evaluates` iterative self-training
- `builds_on_unresolved` RLHF
- `builds_on_unresolved` Self-Refine
- `builds_on_unresolved` self-consistency
- `compares_to_unresolved` RLHF
- `compares_to_unresolved` pseudo-labeled fine-tuning
- `compares_to_unresolved` self-refinement at inference time
- `compares_to_unresolved` self-consistency
<!-- GENERATED:END -->

## My Notes

