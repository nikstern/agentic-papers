---
topic_id: context-engineering
tags: [topic-map]
---

# Context Engineering

## Definition

Cross-cutting hub for work on how agent systems assemble, compress, rewrite, route, and repair the context shown to an LLM during long-horizon execution.

## Core Questions

- What should count as context engineering versus memory, retrieval, or prompt engineering?
- When should agents compress context, and when should they restructure or repair it instead?
- How much of context management should be learned end-to-end versus handled by fixed heuristics?
- What makes context construction plan-aware, workflow-aware, or task-aware rather than just query-aware?
- Which benchmarks actually test durable context quality instead of only top-k retrieval quality?

## Included Papers

- [[2025-A-Survey-of-Context-Engineering-for-Large-Language]]
- [[2025-Scaling-Long-Horizon-LLM-Agent-via-Context-Folding]]
- [[2025-ACON-Optimizing-Context-Compression-for-Long-horizon-LLM-Agents]]
- [[2026-ARC-Active-and-Reflection-driven-Context-Management-for-Long-Horizon]]
- [[2025-PAACE-A-Plan-Aware-Automated-Agent-Context-Engineering-Framework]]
- [[2025-MemInsight-Autonomous-Memory-Augmentation-for-LLM-Agents]]
- [[2026-Beyond-RAG-for-Agent-Memory-Retrieval-by-Decoupling]]
- [[2026-MemWeaver-Weaving-Hybrid-Memories-for-Traceable-Long-Horizon-Agentic]]
- [[2026-Evaluating-Memory-Structure-in-LLM-Agents]]

## Suggested Clusters

### Survey and framing

- [[2025-A-Survey-of-Context-Engineering-for-Large-Language]]

### Compression and context-budget control

- [[2025-Scaling-Long-Horizon-LLM-Agent-via-Context-Folding]]
- [[2025-ACON-Optimizing-Context-Compression-for-Long-horizon-LLM-Agents]]
- [[2025-PAACE-A-Plan-Aware-Automated-Agent-Context-Engineering-Framework]]

### Active repair and context-state management

- [[2026-ARC-Active-and-Reflection-driven-Context-Management-for-Long-Horizon]]
- [[2026-Beyond-RAG-for-Agent-Memory-Retrieval-by-Decoupling]]

### Structured memory as context construction

- [[2025-MemInsight-Autonomous-Memory-Augmentation-for-LLM-Agents]]
- [[2026-MemWeaver-Weaving-Hybrid-Memories-for-Traceable-Long-Horizon-Agentic]]

### Evaluation of context quality

- [[2026-Evaluating-Memory-Structure-in-LLM-Agents]]

## Notes

- This is a synthesis overlay, not a controlled `candidate_topic`.
- It overlaps most strongly with [[Memory-Context]] and [[Search-Retrieval]].
- The strongest distinction from generic memory work is that these papers focus on what enters the active working context, in what form, and at what point in the workflow.
