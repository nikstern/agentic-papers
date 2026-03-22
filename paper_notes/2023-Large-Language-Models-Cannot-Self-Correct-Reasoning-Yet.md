---
paper_id: 80
title: "Large Language Models Cannot Self-Correct Reasoning Yet"
year: 2023
authors: "Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou"
url: "https://arxiv.org/abs/2310.01798"
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
  - "intrinsic self-correction"
  - "reasoning robustness"
  - "self-consistency versus debate"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Self-Refine"
  - "Reflexion"
  - "self-consistency"
compares_to_unresolved:
  - "multi-agent debate"
  - "oracle-guided self-correction"
  - "standard prompting"
  - "self-consistency"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper re-evaluates intrinsic self-correction in large language models and argues that current models generally fail to improve their own reasoning without external guidance. Across reasoning benchmarks, self-correction often degrades performance rather than fixing errors.

# Why It Matters
It is a strong negative-result anchor for the vault because it challenges optimistic claims about self-correction and clarifies the difference between oracle-guided improvement and genuine intrinsic revision. It is especially useful as a baseline contrast for later self-evolution and self-improvement papers.

# Method / Setup
The paper evaluates GPT-3.5, GPT-4, GPT-4-Turbo, and Llama-2 on GSM8K, CommonSenseQA, and HotpotQA using a generate-feedback-refine loop without external labels. It also compares multi-agent debate against self-consistency under matched inference cost and analyzes prompt-design confounds in prior self-correction work.

# Key Claims
- Intrinsic self-correction without external feedback usually reduces reasoning performance rather than improving it.
- Many reported gains from self-correction come from oracle guidance, extra inference budget, or weak initial prompts rather than true self-repair.
- For matched compute, simple self-consistency can outperform more elaborate debate-style correction schemes.

# Limitations
- The evaluation is centered on reasoning tasks and does not establish whether self-correction works better for preference alignment or stylistic revision.
- The experiments focus on prompting-based correction rather than broader training-time self-improvement pipelines.
- The study reflects the capabilities of the evaluated 2023-era model set and may not fully characterize later reasoning-optimized models.

# Connections
- [[Agent-Evaluation]]
- `evaluates` intrinsic self-correction
- `evaluates` reasoning robustness
- `evaluates` self-consistency versus debate
- `builds_on_unresolved` Self-Refine
- `builds_on_unresolved` Reflexion
- `builds_on_unresolved` self-consistency
- `compares_to_unresolved` multi-agent debate
- `compares_to_unresolved` oracle-guided self-correction
- `compares_to_unresolved` standard prompting
- `compares_to_unresolved` self-consistency
<!-- GENERATED:END -->

## My Notes

