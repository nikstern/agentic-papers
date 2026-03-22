---
paper_id: 48
title: "SWE-Exp: Experience-Driven Software Issue Resolution"
year: 2025
authors: "Chen et al."
url: "https://arxiv.org/abs/2507.23361"
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
  - "software issue resolution"
  - "experience-guided reasoning"
  - "SWE-bench Verified"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "SWE-Search"
  - "SWE-Agent"
compares_to_unresolved:
  - "SWE-Agent"
  - "AutoCodeRover"
  - "CodeAct"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
SWE-Exp turns software issue resolution into an experience-driven search process by storing distilled comprehension and modification experiences from prior trajectories.

# Why It Matters
It is a strong direct hit for code investigation because it shows memory-guided issue resolution gains on a real SWE benchmark rather than only on generic long-horizon tasks.

# Method / Setup
The framework builds an experience bank from past successful and failed trajectories, retrieves stage-relevant experiences during MCTS-style issue resolution, and evaluates on SWE-bench Verified.

# Key Claims
- Experience-guided issue resolution outperforms strong same-model baselines on SWE-bench Verified.
- Comprehension experiences are especially important for strategic guidance.
- A small amount of high-quality retrieved experience works better than retrieving many memories.

# Limitations
- Performance depends on the quality of extracted and reranked experiences.
- The reported evidence focuses on one major benchmark setting.
- Too many retrieved experiences can hurt performance.

# Connections
- [[Software-Agents]]
- `evaluates` software issue resolution
- `evaluates` experience-guided reasoning
- `evaluates` SWE-bench Verified
- `builds_on_unresolved` SWE-Search
- `builds_on_unresolved` SWE-Agent
- `compares_to_unresolved` SWE-Agent
- `compares_to_unresolved` AutoCodeRover
- `compares_to_unresolved` CodeAct
<!-- GENERATED:END -->

## My Notes

