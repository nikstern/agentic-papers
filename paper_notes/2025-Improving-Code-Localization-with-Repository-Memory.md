---
paper_id: 50
title: "Improving Code Localization with Repository Memory"
year: 2025
authors: "Wang et al."
url: "https://arxiv.org/abs/2510.01003"
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
  - "code localization"
  - "repository memory"
  - "SWE-bench-verified"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "LocAgent"
compares_to_unresolved:
  - "LocAgent"
  - "Agentless"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
RepoMem augments code localization agents with repository memory built from commit history, combining episodic memory of past commits with semantic memory of active code functionality.

# Why It Matters
It is directly relevant to code investigation because it improves the localization stage of repository-level bug fixing by giving agents prior repository knowledge.

# Method / Setup
The system constructs commit-history memory and file-summary memory, exposes them through retrieval tools, integrates them into LocAgent, and evaluates on SWE-bench-verified and SWE-bench-live.

# Key Claims
- Repository memory improves code localization accuracy over LocAgent.
- Episodic and semantic memory provide complementary gains.
- Memory shifts agent behavior from exhaustive exploration toward hypothesis-driven investigation.

# Limitations
- Benefits depend heavily on the richness and relevance of repository commit history.
- Sparse or noisy repository memory can distract the agent and reduce performance.
- The paper focuses on localization rather than full end-to-end repair.

# Connections
- [[Software-Agents]]
- `evaluates` code localization
- `evaluates` repository memory
- `evaluates` SWE-bench-verified
- `builds_on_unresolved` LocAgent
- `compares_to_unresolved` LocAgent
- `compares_to_unresolved` Agentless
<!-- GENERATED:END -->

## My Notes

