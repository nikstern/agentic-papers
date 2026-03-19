The evaluation of LLMs and Coding Agents has largely focused on metrics for overall task completion. There exist a variety of benchmarks and test suites for an Agent to submit a solution to such as [SWEBenchPro](https://labs.scale.com/leaderboard/swe_bench_pro_public), and [TerminalBench](https://www.tbench.ai/benchmarks/terminal-bench-2).

However, the practices and tooling surrounding Coding Agent has evolved beyond model prompting. [Harness Engineering](https://openai.com/index/harness-engineering/), [Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), Agent Orchestration, and Skill/MCP/CLI evaluation have emerged as critical practices beyond evaluating an LLM or default harness in isolation. However, there exists no standard experimental framework for evaluating those emerging practices. Developers are often relying on intuition and anecdotal evidence to make claims about the performance of homegrown tooling.

This paper proposes a framework for empirically evaluating those practices based on existing concepts from LLM evaluation, Multi-agent systems evaluation, and observability principles.
## 1.1 LLMs and Tokens

Despite their name, Large Language Models (LLMs) have no understanding of language as we know it. They are **trained** to represent the relationships between “tokens” through many layers of **weights**. Given a set of input tokens, the trained weights processed that input into probabilities for what output token comes next. This is called **inference**. A sampling process then chooses the next token based on those probabilities.

## 1.2 Attention

Prior to the introduction of “[attention](https://arxiv.org/abs/1706.03762)” in 2017, text generators such as [RNNs](https://www.ibm.com/think/topics/recurrent-neural-networks) needed to sequentially process each token of their input in order to start predicting their output tokens. They then needed to carry forward information from previously processed tokens in a hidden state. This had a time complexity of O(n) for its initial prompt, but it **was not possible to be done in parallel**. Furthermore, RNNs had [significant issues](https://www.superdatascience.com/blogs/recurrent-neural-networks-rnn-the-vanishing-gradient-problem) with processing relationships between tokens far apart from each other. Meaning, output would often have weak relationships to long inputs.

While RNNs required sequential processing, **attention can be done in parallel**. Attention is also much better at computing relationships between all the tokens in an long input. Those relationships mean that all of the tokens in its input are “considered” at once when determining an output. In practice, **the output of an LLM is more likely to be related to everything in the input.**

## 1.3 GPUs

Attention actually has worse time and memory complexity, both O(n^2), than precursor RNNs. **Attention is based on matrix multiplication, and in order to process large inputs, needs to be very parallelized.**

Computer hardware experts have been improving mechanisms to perform matrix operations since the 1960s because matrix multiplication is central to computer graphics rendering. As computer graphics grew more complex, specialized hardware for performing parallel graphical computations were developed: GPUs.

To deal with the amount of matrix multiplication required for training and inferring for LLMs, massive amounts of GPUs are required. This has been good news for NVIDIA, previously a leader in computer graphics hardware, and bad news for a person wanting to purchase anything with a GPU inside of it.

There is a limit to the amount of GPUs in the world, and not everyone can access them at once. It requires much more work to train a new LLM on more inputs, which is what causes delay between new models. As model creators add training tokens, it requires more power and compute to train.

Once an LLM is trained, inference (predicting output tokens from inputs) is easier, but still requires many parallel operations to be fast. When it’s not being parallelized, long inputs get very slow and memory intensive. Massive amounts of training and inference have increased the need for RAM and caused a RAM shortage.

## 1.4 Generations of Generators

The Attention mechanism was introduced in 2017. GPT-1 was introduced in 2018, with 118 million parameters. Previously, due to their sequential nature, RNNs needed to be trained on much smaller and more specific datasets. Because it could form relationships between more training data in parallel GPT-1 outperformed leading RNNs at natural language in a larger variety of language domains. However it was not transformative in daily life and mostly a useful research tool for natural language processing.

OpenAI then scaled further, [releasing GPT-2](http://arxiv.org/abs/1908.09203) in 2019 with 1.5 billion parameters. OpenAI released this model in stages, due to consideration the [possible societal impacts](https://arxiv.org/abs/1908.09203) of cheap, “fake”, and unreliable text generation.

### 1.1 Code Generation and Coding Interface History

Code turned out to be a more natural fit for LLM generation due to the strong relationships between its tokens. Unlike complex natural prose, LLMs can better predict things like a closing brace following an open brace, a declared variable being assigned after declaration, etc.

From 2021 to 2024, there was a slow progression of an LLM model's ability to generate code. IDE integration was possible using [Github Copilot](https://github.com/features/copilot?utm_source=google&utm_medium=sem&utm_campaign=copilot-brand&ef_id=_k_Cj0KCQjwsdnNBhC4ARIsAA_3hegRUZ0PepVsddyFdEyo-v6h1Xr5XMh1itPZO0aZN-TfykqjCBeVs4UaAjsmEALw_wcB_k_&OCID=AIDcmmh2h80ugd_SEM__k_Cj0KCQjwsdnNBhC4ARIsAA_3hegRUZ0PepVsddyFdEyo-v6h1Xr5XMh1itPZO0aZN-TfykqjCBeVs4UaAjsmEALw_wcB_k_&gad_source=1&gad_campaignid=23238727906&gbraid=0AAAAADcJh_uutFAdnvD_471hYM3fYtdvt&gclid=Cj0KCQjwsdnNBhC4ARIsAA_3hegRUZ0PepVsddyFdEyo-v6h1Xr5XMh1itPZO0aZN-TfykqjCBeVs4UaAjsmEALw_wcB) and [Cursor](https://cursor.com/) which provided line completion, file scaffolding, and some generation of common patterns. However, this code tended to be rudimentary, localized to common use cases, and highly prone to error. While there were syntax relationships, relationships between long chains of lines of code were more difficult to represent.

In 2024, developers still typically interacted with a browser interface such as [ChatGPT](https://chatgpt.com/), creating a layer of separation between the code generated and the developer's workspace.

Anthropic's [Claude Code](https://claude.com/product/claude-code) integrating their LLMs into the terminal with a set of tools to directly read, write, and execute code in the codebases that an engineer works in. Claude Code was not the first to do this, but the first to gain widespread popularity. These tools were called [Coding Harnesses](https://arxiv.org/html/2603.05344v1) and were quickly adopted/distributed by each of the most popular LLM providers.

2025 then saw a rapid progression in models' ability to produce quality code. Anthropic's Claude Opus 4.5's launch in November represented [a huge shift](https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point) in agents' capabilities to create not just code or files, but complex software systems. From within Claude Code, Opus 4.5 could represent relationship about implementations across thousands of lines, hold architectural context across a code base, and generate aspects such as module boundaries, memory safety, and concurrent access. [Agentic coding](https://cloud.google.com/discover/what-is-agentic-coding), the use of AI to plan, execute, and test releasable software saw a dramatic shift in feasibility.

The issue was no longer whether coding agents could write compilable code, but the limits to complexity and quality that an agent could achieve. Now that Agents could write complex codebases, the process for verifying that the codebase worked correctly and identifying became and remains a widespread problem.

### 1.3 The Agentic Loop

[Google Cloud](https://cloud.google.com/discover/what-are-ai-agents) establishes agents in the context of LLMs as “software systems that use AI to pursue goals and complete tasks on behalf of users.” While Claude Code was originally intended as a coding agent application, it’s gained rapid adoption for many aspects of knowledge work.

The primary difference between chatbots and an agent is that agents follow a looping pattern to accomplish tasks before finishing their process. The primary archetype for this is the [ReAct loop](https://www.ibm.com/think/topics/react-agent):

1. Gather and provide context
    
2. Break tasks into a series of subtasks
    
3. Takes actions to accomplish the task/subtasks
    
4. Evaluates results
    
5. Loops until it reaches a user-presentable output
    

A model can be invoked at any point in this process for varying purposes and with different prompts. The model might be asked to generate the plan, list an appropriate tool call, determine an end state through examination of tool outputs etc. Different parts of this loop can be deterministic or based on the LLM.

This depends on the definition of the harness, hence the new field of **harness engineering**, building harnesses to optimize accomplishing specific goals.

### 1.4 Agent Context/Attention

A coding harness doesn’t change anything mechanically an LLM. An LLM receives a series of tokens, then emits a series of tokens that it predicts would come after that sequence.

It’s important to understand that an LLM Model is stateless and only produces text. It takes in an input and produces output matching what it thinks would come next. It can not actually perform steps, take actions, “remember” conversation history, or perform logical reasoning. Stepping through this loop, gathering and holding context, and performing actions are the responsibility of the harness, such as Claude Code, rather than the model, such as Opus 4.6.

### 1.5 Agent Tools

Because a model only generates text, the coding harness must use some process to invoke tools based on a combination of the harnesses' definition or the output of the model. Types of tools and processes for invoking tools are changing over time.

### 1.5.1 Types of Tools

Coding harness often come with a set of built-in tools, which are provided and managed by the harness provider such as Anthropic or Open AI.

Common built-in tools include file system operations such as Read, Write, Update, and List. They also can perform more adaptive (and dangerous) behavior when given access to a Bash tool or scripting. As harnesses evolve, so do the tools and tool implementations provided to the harness.

Harness users often want to define custom tools and workflows specific to their use case. Though introduced in 2020, RAG (Retrieval Augmented Generation) gained renewed interest as a way to add context on top of a model’s training.

In 2024, [Anthropic announced MCPs](https://www.anthropic.com/news/model-context-protocol) (Model Context Protocols) as an open source API layer to connect Agents to external tool sources. This led to a race for many SaaS companies to introduce “AI-native” capabilities by announcing MCPs.