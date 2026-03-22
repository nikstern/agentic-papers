# RLM-Style Recursion + SWE-Specific Memory

## Core Shape

An effective design is a recursive software engineering agent with a strict memory hierarchy:

- recursion handles search depth and decomposition
- SWE-specific memory handles reuse
- retrieval is subtask-scoped and code-aware
- context is actively managed rather than appended indefinitely

This combines the main lessons from the vault:

- deep recursive decomposition is more powerful than shallow summarization for long-horizon reasoning
- memory should be treated as a hierarchy, not a flat vector store
- SWE memory works better at subtask granularity than whole-episode granularity
- code-aware and structural memory beats text-only memory for repository work
- naive episodic reuse can degrade SWE performance through interference

## System Architecture

The system has five layers:

1. Recursive executor
2. Context and memory manager
3. SWE memory stores
4. Retrieval and aggregation pipeline
5. Writeback and memory governance

## 1. Recursive Executor

Each task is represented as a node in a call tree.

Suggested node types:

- `root_issue`
- `reproduce`
- `localize`
- `inspect_symbol`
- `inspect_history`
- `design_patch`
- `edit`
- `verify`
- `summarize_return`

Each node contains:

- `goal`
- `subtask_type`
- `input_artifacts`
- `local_context_budget`
- `allowed_tools`
- `return_schema`
- `depth`
- `parent_id`

Spawn rule:

- spawn a child when the current node needs a bounded subproblem with narrower evidence scope
- do not spawn if the current node can finish with current evidence and budget

Return rule:

- every child returns a compact typed object, not a free-form transcript

Example return schema:

```json
{
  "status": "resolved|unresolved|blocked",
  "claim": "most likely faulty invariant is in cache invalidation path",
  "evidence": [
    {"kind": "file", "ref": "src/cache.py:182"},
    {"kind": "test", "ref": "tests/test_cache.py::test_eviction_order"}
  ],
  "artifacts": ["patch_candidate", "failure_signature"],
  "open_questions": ["does async path share the same invalidation hook?"],
  "confidence": 0.74
}
```

## 2. Context and Memory Manager

Treat context as a managed hierarchy, not an append-only prompt.

Per-node memory tiers:

- `L0 working set`
  - current task, active files, current hypothesis, latest tool outputs
- `L1 node cache`
  - compressed notes from this node's own exploration
- `L2 branch cache`
  - sibling-relevant summaries inside the same recursive branch
- `L3 persistent SWE memory`
  - cross-issue reusable memory
- `L4 raw repo substrate`
  - codebase, tests, commit history, docs

Core operations:

- `retrieve(subtask_type, query, constraints)`
- `compress(local_trace)`
- `promote(candidate_memory)`
- `evict(stale_or_redundant_context)`
- `snapshot(node_state)`
- `merge(child_return, parent_state)`

Policy:

- only `L0` and selected `L1/L2` items go into model context
- `L3` is queried, never dumped wholesale

## 3. SWE Memory Stores

Use separate stores with different schemas and admission rules.

### A. Episodic Subtask Store

Stores successful or high-signal partial trajectories at subtask granularity.

```json
{
  "memory_id": "ep_123",
  "subtask_type": "localize",
  "problem_signature": {
    "error_type": "AssertionError",
    "stack_symbols": ["Cache.refresh", "Index.rebuild"],
    "repo_area": ["src/cache", "src/index"]
  },
  "action_pattern": [
    "inspect failing test",
    "trace symbol writes",
    "compare sync vs async path"
  ],
  "outcome": "useful|misleading|failed",
  "evidence_refs": ["src/cache.py:182", "git:commit:abc123"],
  "quality_score": 0.88
}
```

### B. Semantic Repo Knowledge Store

Stable facts about the repository, for example:

- file and module summaries
- ownership and dependency notes
- test-to-code links
- historical bug clusters
- API invariants

### C. Structural Code Memory

Graph or index over:

- AST nodes
- symbols
- call graph edges
- imports
- test coverage links
- commit-file-function relations

### D. Failure Signature Store

Compact records for recurring failure shapes, for example:

- traceback motifs
- flaky-test patterns
- config mismatch signatures
- migration and versioning issues

## 4. Retrieval Pipeline

Retrieval should be staged and filtered, not naive top-k RAG.

Pipeline:

1. route by `subtask_type`
2. filter by repo region, symbols, and artifact type
3. retrieve candidates using:
   - semantic similarity
   - structural overlap
   - signature overlap
   - recency and quality priors
4. deduplicate and diversify
5. aggregate into a compact evidence packet
6. inject only the packet and references into node context

Example retrieval packet:

```json
{
  "query_intent": "localize regression in cache invalidation",
  "subtask_type": "localize",
  "candidate_memories": [
    {
      "kind": "episodic_subtask",
      "why_relevant": "same failure signature and overlapping symbols",
      "content": "check writer path before reader cache refresh",
      "confidence": 0.81
    },
    {
      "kind": "repo_fact",
      "why_relevant": "module summary mentions delayed invalidation semantics",
      "content": "cache invalidation deferred in async mode",
      "confidence": 0.77
    }
  ],
  "omissions": ["low-quality whole-episode traces dropped for redundancy"]
}
```

## 5. Writeback and Memory Governance

Memory writeback must be selective or the system will poison itself.

Admission rules:

- store only if there is verified utility
- prefer subtask fragments over full transcripts
- attach evidence references and outcome labels
- down-rank or blacklist misleading memories
- keep source traces immutable and derived summaries separate

Writeback triggers:

- reproduction confirmed
- localization validated by edit or test result
- patch verified
- repeated retrieval utility observed across tasks

Do not store:

- speculative hypotheses without evidence
- broad natural-language summaries of full runs
- memories without repo anchors
- duplicate variants of the same trace

## Parent / Child Protocol

Parent sends:

```json
{
  "node_id": "n17",
  "subtask_type": "inspect_symbol",
  "goal": "determine whether Cache.refresh can skip invalidation in async path",
  "context_packet": "...",
  "retrieved_memory_packet": "...",
  "budget": {"tool_calls": 6, "tokens": 12000, "max_depth": 1},
  "return_schema": "inspection_result_v1"
}
```

Child returns:

```json
{
  "status": "resolved",
  "claim": "async path bypasses invalidate_if_stale",
  "evidence": ["src/cache.py:182", "src/worker.py:94"],
  "recommended_next_step": "spawn design_patch on cache refresh path",
  "confidence": 0.84
}
```

## Scheduler Heuristics

Use recursion for:

- decomposition across repo regions
- hypothesis branching
- verification branches
- history inspection versus live code inspection

Do not recurse for:

- trivial symbol lookup
- single-file edits with a clear fix
- repeated failed branching without new evidence

Budget heuristics:

- shallow wide branching for localization
- deeper narrow branching for root-cause analysis
- hard cap on depth unless each level adds new evidence

## Failure Modes To Defend Against

- `memory interference`
  - fix: subtask-scoped retrieval and strict admission
- `context drift`
  - fix: explicit compress, promote, and evict operations
- `trajectory explosion`
  - fix: typed returns, branch budgets, and kill low-yield branches
- `code/text mismatch`
  - fix: structural code memory, not text-only retrieval
- `whole-episode overfitting`
  - fix: fragment memory into reusable subtasks
- `retrieval redundancy`
  - fix: hierarchical aggregation instead of naive top-k

## Minimal MVP

The smallest defensible version:

- recursive node executor with typed child returns
- three subtask types: `localize`, `design_patch`, `verify`
- one persistent store for episodic subtask memory
- one structural index over files, symbols, and tests
- retrieval keys: `subtask_type + symbols + error signature`
- context manager with only `compress`, `retrieve`, and `promote`

## One-Line Summary

Use RLM-style recursive control over a stack of local workspaces, backed by a MemGPT-like hierarchy, with persistent SWE memory stored at subtask granularity and retrieved through code-aware, anti-redundant aggregation.
