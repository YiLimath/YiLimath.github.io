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

### Victor Dibia — *Designing Multi-Agent Systems*

This book supplies the workflow architecture: explicit computational graphs,
autonomous orchestration, sequential/conditional/parallel workflows, handoffs,
round-robin interaction, task termination, human delegation, structured output,
tools, memory, middleware, observability, checkpointing, persistence, and
trajectory evaluation.

### Valliappa Lakshmanan and Hannes Hapke — *Generative AI Design Patterns*

This book gives finer-grained application patterns: constrained generation,
RAG stages, deep search, reasoning, reflection, dependency injection, tool
calling, code execution, multi-agent collaboration, caching, long-term memory,
self-check, reformatting, and guardrails.

### Sampriti Mitra — *System Design for the LLM Era*

This book adds production architecture: gateways, circuit breakers, tiered
fallbacks, synchronous versus asynchronous processing, prompt compression,
hybrid retrieval, function calling, golden datasets, evaluation, observability,
security, caching, latency, and cost.

## Course organization

The books are translated into five design questions:

1. **Control flow:** how does work decompose, branch, route, and terminate?
2. **Knowledge and reasoning:** how is context selected and a candidate checked?
3. **Coordination:** how do agents, tools, and humans exchange responsibility?
4. **Reliability:** how are state, failure, evaluation, safety, and resources
   controlled?
5. **Architecture:** which stable interfaces allow components to be replaced?

## Reading rule

Do not use every pattern at once. Choose the smallest composition that makes the
important uncertainty observable and the important steps verifiable.

## Figure

![Book-informed agent pattern taxonomy](/images/agent-system/25-book-pattern-taxonomy.svg)

*Figure: the four books contribute complementary architectural, application, orchestration, and production viewpoints.*
