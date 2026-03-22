---
paper_id: 94
title: "Large Language Model Agents Are Not Always Faithful Self-Evolvers"
year: 2026
authors: "Zhao et al."
url: "https://arxiv.org/abs/2601.22436"
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
  - "self-evolving llm agents"
  - "experience faithfulness"
  - "raw vs condensed experience"
  - "causal intervention evaluation"
  - "agent benchmarks across qa math embodied action and web"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "ExpeL"
  - "Dynamic Cheatsheet"
  - "ReasoningBank"
  - "G-Memory"
compares_to_unresolved:
  - "ExpeL"
  - "Dynamic Cheatsheet"
  - "ReasoningBank"
  - "G-Memory"
  - "HotpotQA"
  - "FEVER"
  - "GPQA-Diamond"
  - "MMLU-Pro Eng"
  - "AIME 2024"
  - "Game of 24"
  - "ALFWorld"
  - "WebArena"
  - "WebShop"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper introduces experience faithfulness as a diagnostic lens for self-evolving LLM agents and shows that agents are generally much more faithful to raw experience traces than to condensed experience summaries.

# Why It Matters
It challenges the assumption that performance gains from memory or self-evolution imply genuine causal use of accumulated experience, and it provides a more rigorous way to evaluate agent learning mechanisms.

# Method / Setup
The authors apply causal interventions to raw and condensed experience across four self-evolving agent frameworks, multiple LLM backbones, and nine benchmarks spanning question answering, math, embodied action, and web interaction, then use integrated gradients to analyze attribution.

# Key Claims
- Self-evolving LLM agents show strong faithfulness to raw experience but often weak faithfulness to condensed experience.
- Perturbing condensed experience often causes little behavioral change even when removing it can reduce overall performance.
- The faithfulness gap persists across offline, online, and multi-agent frameworks as well as across model scales.
- Low faithfulness to condensed experience is linked to uninformative or misaligned summaries, local-context bias, and task regimes where model priors already dominate.
- Evaluating self-evolving agents should measure causal dependence on experience rather than relying only on aggregate success metrics.

# Limitations
- The paper shows that experience utility and experience faithfulness can diverge, which makes interpretation of performance gains more difficult than standard benchmark reporting suggests.
- Knowledge-intensive tasks can weaken the observed effect of external experience because strong pretrained priors already handle much of the task.
- The diagnosis is strongest for the evaluated frameworks and intervention designs, so future work is still needed on better condensed-experience representations and dynamic retrieval schemes.

# Connections
- [[Agent-Evaluation]]
- `evaluates` self-evolving llm agents
- `evaluates` experience faithfulness
- `evaluates` raw vs condensed experience
- `evaluates` causal intervention evaluation
- `evaluates` agent benchmarks across qa math embodied action and web
- `builds_on_unresolved` ExpeL
- `builds_on_unresolved` Dynamic Cheatsheet
- `builds_on_unresolved` ReasoningBank
- `builds_on_unresolved` G-Memory
- `compares_to_unresolved` ExpeL
- `compares_to_unresolved` Dynamic Cheatsheet
- `compares_to_unresolved` ReasoningBank
- `compares_to_unresolved` G-Memory
- `compares_to_unresolved` HotpotQA
- `compares_to_unresolved` FEVER
- `compares_to_unresolved` GPQA-Diamond
- `compares_to_unresolved` MMLU-Pro Eng
- `compares_to_unresolved` AIME 2024
- `compares_to_unresolved` Game of 24
- `compares_to_unresolved` ALFWorld
- `compares_to_unresolved` WebArena
- `compares_to_unresolved` WebShop
<!-- GENERATED:END -->

## My Notes

