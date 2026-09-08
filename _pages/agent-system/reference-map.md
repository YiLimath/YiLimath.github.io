---
title: "Agent Systems: Reference Books and the Pattern Taxonomy"
permalink: /posts/2026/08/agent-system/reference-map/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

This course is organized from four complementary books in the Life and Readings
vault. The pages are a synthesis and application of their ideas, not a
framework-specific API manual.

## Four viewpoints

### Antonio Gulli — *Agentic Design Patterns*

This is the broad catalogue: prompt chaining, routing, parallelization,
reflection, tool use, planning, multi-agent systems, memory, learning,
exception recovery, human-in-the-loop, retrieval, reasoning, safety, evaluation,
prioritization, and exploration.

Publisher record: [Springer — *Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3).

### Victor Dibia — *Designing Multi-Agent Systems*

This book supplies the workflow architecture: explicit computational graphs,
autonomous orchestration, sequential/conditional/parallel workflows, handoffs,
round-robin interaction, task termination, human delegation, structured output,
tools, memory, middleware, observability, checkpointing, persistence, and
trajectory evaluation.

Author's book site and companion code: [Designing Multi-Agent Systems](https://multiagentbook.com/)
and [GitHub repository](https://github.com/victordibia/designing-multiagent-systems).

### Valliappa Lakshmanan and Hannes Hapke — *Generative AI Design Patterns*

This book gives finer-grained application patterns: constrained generation,
RAG stages, deep search, reasoning, reflection, dependency injection, tool
calling, code execution, multi-agent collaboration, caching, long-term memory,
self-check, reformatting, and guardrails.

Publisher record: [O'Reilly — *Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/).
The publisher-authorized [companion diagram collection](https://github.com/lakshmanok/generative-ai-design-patterns/tree/main/diagrams)
is especially useful for checking the original Deep Search figures; the course
redraws their logic and cites the source rather than embedding the originals.

### Sampriti Mitra — *System Design for the LLM Era*

This book adds production architecture: gateways, circuit breakers, tiered
fallbacks, synchronous versus asynchronous processing, prompt compression,
hybrid retrieval, function calling, golden datasets, evaluation, observability,
security, caching, latency, and cost.

Publisher record: [Packt — *System Design for the LLM Era*](https://www.packtpub.com/en-us/product/system-design-for-the-llm-era-9781807789923).

## Course organization

The books are translated into five design questions:

1. **Control flow:** how does work decompose, branch, route, and terminate?
2. **Knowledge and reasoning:** how is context selected and a candidate checked?
3. **Coordination:** how do agents, tools, and humans exchange responsibility?
4. **Reliability:** how are state, failure, evaluation, safety, and resources
   controlled?
5. **Architecture:** which stable interfaces allow components to be replaced?

## Part-to-source map

The table records the provenance of the course organization. Chapter numbers
refer to the editions in the Life and Readings vault; the external links point
to publisher, paper, or official project pages so that the reader can check the
source rather than relying on the course summary.

| Course part | Primary book locations | Supporting original source | What this course adds |
|---|---|---|---|
| Part I: foundations | Gulli, introduction and agent loop; Dibia, Chapter 4 | [ReAct](https://arxiv.org/abs/2210.03629) | common vocabulary and stable-interface test |
| Part II: workflow | Gulli, Chapters 1-3, 6, 21; Dibia, Chapters 2, 5-7 | Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | pattern selection by dependency, branching, and stopping rule |
| Part III: knowledge and reasoning | Gulli, Chapters 4, 5, 14, 17; Lakshmanan and Hapke, Chapters 3-7 | [RAG](https://arxiv.org/abs/2005.11401), [STORM](https://aclanthology.org/2024.naacl-long.347/) | provenance, representation change, and evidence gates |
| Part IV: coordination | Gulli, Chapters 7, 13, 15; Dibia, Chapters 2, 7, 12-13 | [AutoGen](https://arxiv.org/abs/2308.08155), [Magentic-One](https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Magentic-One.pdf) | explicit responsibility, protocol, and human handoff |
| Part V: reliability and operations | Gulli, Chapters 8, 9, 11, 12, 16, 18-20; Dibia, Chapters 10-13; Mitra, Chapters 2-6 | [MCP specification](https://modelcontextprotocol.io/specification) | operational contracts for recovery, evaluation, cost, and safety |
| Part VI: code case | Danus and Rethlas source trees | the case-study repositories supplied for this course | as-built mapping; no private research framework is exposed |
| Part VII: real problems | synthesis across the four books | [SWE-bench](https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html) and the sources above | task-level architecture templates and observable contracts |

## Reading rule

Do not use every pattern at once. Choose the smallest composition that makes the
important uncertainty observable and the important steps verifiable.

The matrix below is a crosswalk, not a claim that each book owns one category.
Read across a row to see how the books complement one design dimension; read
down a column to see the emphasis of one book. The right-hand column is the
course synthesis built from those overlapping contributions.

## Figure

![Book-informed agent pattern taxonomy](/images/agent-system/25-book-pattern-taxonomy.svg)

*Figure: a source-to-course crosswalk for control flow, knowledge and reasoning,
coordination, and reliability/operations.*

For task-level application architectures, see [Real-world architecture
templates](/posts/2026/08/agent-system/real-world-applications/).
