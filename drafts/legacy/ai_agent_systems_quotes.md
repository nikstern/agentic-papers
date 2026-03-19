
Quotes:

Therefore, in-context learning is most effective when paired with memory (summaries, persistent state), retrieval grounded in trusted sources, and strict tool interfaces that cannot be bypassed by text alone [5, 24].

Another emerging best practice is to explicitly separate planning from execution: a planner proposes a plan with explicit constraints and success criteria, while an executor carries out the plan under stricter tool permissions and validation.

Agentic finetuning is increasingly trace-centric: models are tuned on trajectories that include tool calls, intermediate checks, and corrected failures, so that the model learns not only to answer but also to operate—plan, act, verify, and recover—under constraints [53, 64]. Finally, finetuning interacts with system design: if orchestration enforces strict schemas and verifiers, finetuning can focus on high-level planning and query formulation; if schemas are weak, finetuning must implicitly learn safety and interface constraints, which is less reliable and harder to audit [5, 21].



Further References:

[44] Yujia Qin et al. 2023. ToolBench: Towards open-source benchmark for tool-augmented large language models. arXiv
[29] Ziniu Liu et al. 2023. AgentBench: Evaluating LLMs as agents. arXiv preprint arXiv:2308.03688 (2023).