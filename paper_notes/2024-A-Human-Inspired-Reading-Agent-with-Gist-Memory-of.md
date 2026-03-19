---
paper_id: 16
title: "A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts"
year: 2024
authors: "Lee et al."
url: "https://arxiv.org/abs/2402.09727"
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
  - "long-document reading"
  - "gist memory"
  - "interactive retrieval"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "NarrativeQA"
  - "QuALITY"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
ReadAgent is a human-inspired reading system that builds gist memory for long documents and then selectively looks up raw passages when more detail is needed.

# Why It Matters
It offers a practical memory-and-retrieval design for long-context reading that is more agentic than simple chunk retrieval and more efficient than feeding whole documents repeatedly.

# Method / Setup
The method paginates documents into natural episodes, compresses them into gist summaries, and lets an LLM iteratively retrieve raw pages from the source text while answering long-context questions.

# Key Claims
- Gist memory plus targeted lookup can outperform both direct long-context prompting and standard retrieval baselines.
- LLM-guided retrieval is better aligned with long-document reasoning than simple chunk similarity.
- Interactive long-context reading can be implemented without model fine-tuning.

# Limitations
- Compression can increase hallucination risk if the model over-trusts gist summaries.
- Performance still depends on the underlying model’s reading and retrieval judgment.

# Connections
- [[Memory-Context]]
- `evaluates` long-document reading
- `evaluates` gist memory
- `evaluates` interactive retrieval
- `compares_to_unresolved` NarrativeQA
- `compares_to_unresolved` QuALITY
<!-- GENERATED:END -->

## My Notes

