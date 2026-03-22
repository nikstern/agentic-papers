---
topic_id: repository-swe-agents
tags: [topic-map]
---

# Repository SWE Agents

## Definition

Cross-cutting hub for agent systems that operate over full code repositories for tasks such as code generation, localization, repair, auditing, and long-horizon software workflows.

## Core Questions

- How do agents localize relevant code in large repositories?
- What kinds of memory or context structures help repository-scale reasoning?
- Which systems support repair, auditing, or long-horizon software execution rather than single-file generation?
- How do orchestration choices affect cost, recovery, and scalability on repository tasks?

## Included Papers

- [[2025-EXPEREPAIR-Dual-Memory-Enhanced-LLM-based-Repository-Level-Program-Repair]]
- [[2025-SWE-Exp-Experience-Driven-Software-Issue-Resolution]]
- [[2026-Structurally-Aligned-Subtask-Level-Memory-for-Software-Engineering-Agents]]
- [[2025-Improving-Code-Localization-with-Repository-Memory]]
- [[2025-Context-as-a-Tool-Context-Management-for-Long-Horizon]]
- [[2026-CodeMEM-AST-Guided-Adaptive-Memory-for-Repository-Level-Iterative-Code]]
- [[2025-From-Knowledge-to-Noise-CTIM-Rover-and-the-Pitfalls]]
- [[2025-REPOAUDIT-An-Autonomous-LLM-Agent-for-Repository-Level-Code-Auditing]]
- [[2025-TALM-Dynamic-Tree-Structured-Multi-Agent-Framework-with-Long-Term-Memory]]

## Suggested Clusters

### Repository memory and localization

- [[2025-Improving-Code-Localization-with-Repository-Memory]]
- [[2025-Context-as-a-Tool-Context-Management-for-Long-Horizon]]
- [[2026-CodeMEM-AST-Guided-Adaptive-Memory-for-Repository-Level-Iterative-Code]]
- [[2026-Structurally-Aligned-Subtask-Level-Memory-for-Software-Engineering-Agents]]

### Repair and issue resolution

- [[2025-EXPEREPAIR-Dual-Memory-Enhanced-LLM-based-Repository-Level-Program-Repair]]
- [[2025-SWE-Exp-Experience-Driven-Software-Issue-Resolution]]

### Auditing and failure analysis

- [[2025-REPOAUDIT-An-Autonomous-LLM-Agent-for-Repository-Level-Code-Auditing]]
- [[2025-From-Knowledge-to-Noise-CTIM-Rover-and-the-Pitfalls]]

### Multi-agent orchestration for repository-scale coding

- [[2025-TALM-Dynamic-Tree-Structured-Multi-Agent-Framework-with-Long-Term-Memory]]

## Notes

- This is a cross-cutting synthesis hub layered on top of `software-agents`.
- The focus is repository-scale software work, not general coding benchmarks or single-function generation.
