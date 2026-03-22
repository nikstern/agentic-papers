---
paper_id: 93
title: "Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design"
year: 2025
authors: "Wei et al."
url: "https://arxiv.org/abs/2505.11821"
paper_type: "system"
primary_topic: "agent-harnesses"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "pending"
tags:
  - "papers"
  - "agent-harnesses"
evaluates:
  - "NQ"
  - "TriviaQA"
  - "PopQA"
  - "HotpotQA"
  - "2WikiMultiHopQA"
  - "Musique"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "PPO"
  - "GRPO"
  - "Chain-of-Thought"
  - "reasoning-augmented search"
compares_to_unresolved:
  - "PPO-OR"
  - "PPO-MR"
  - "GRPO-OR"
  - "GRPO-MR"
  - "StepSearch"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper introduces multi-turn variants of PPO and GRPO that use turn-level intermediate rewards to train LLM agents more effectively in long-horizon interactive settings.

# Why It Matters
It is relevant because it addresses a core weakness of agent RL, namely poor credit assignment when only final outcome rewards are used, and it provides a cleaner route to shaping experience at the turn level.

# Method / Setup
The work formulates multi-turn interaction as a turn-level MDP, adds intermediate and outcome rewards to MT-PPO and MT-GRPO, and evaluates the approach on reasoning-augmented search agents with both verifiable rewards and LLM-as-judge rewards.

# Key Claims
- Turn-level rewards substantially improve training stability and convergence over trajectory-level outcome rewards.
- Fine-grained intermediate supervision helps agents learn tool use, retrieval behavior, and structured multi-turn reasoning.
- Multi-turn PPO with turn-level rewards outperforms trajectory-level PPO and GRPO baselines on search-style QA tasks.

# Limitations
- The strongest experiments focus on reasoning-augmented search agents, so broader transfer to other tool-using agent settings remains to be shown.
- Designing good turn-level rewards still requires environment-specific reward engineering.

# Connections
- [[Agent-Harnesses]]
- `evaluates` NQ
- `evaluates` TriviaQA
- `evaluates` PopQA
- `evaluates` HotpotQA
- `evaluates` 2WikiMultiHopQA
- `evaluates` Musique
- `builds_on_unresolved` PPO
- `builds_on_unresolved` GRPO
- `builds_on_unresolved` Chain-of-Thought
- `builds_on_unresolved` reasoning-augmented search
- `compares_to_unresolved` PPO-OR
- `compares_to_unresolved` PPO-MR
- `compares_to_unresolved` GRPO-OR
- `compares_to_unresolved` GRPO-MR
- `compares_to_unresolved` StepSearch
<!-- GENERATED:END -->

## My Notes

