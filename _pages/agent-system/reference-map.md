---
title: "Agent Systems: Reference Books and the Pattern Taxonomy"
permalink: /posts/2026/08/agent-system/reference-map/
tags:
  - Agent System
---

This series is based primarily on four reference books in the Life and Readings
vault. They are complementary rather than interchangeable: one gives a broad
agent-pattern catalogue, one concentrates on multi-agent architecture, one
breaks generative-AI systems into fine-grained patterns, and one treats
production system design.

## Reference roles

### Antonio Gulli, *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems*

Use this book for the broad pattern catalogue: chaining, routing, parallelization, reflection, tools, planning, memory, learning, recovery, human-in-the-loop, retrieval, reasoning, evaluation, safety, prioritization, and exploration.

### Victor Dibia, *Designing Multi-Agent Systems: Principles, Patterns, and Implementation for AI Agents*

Use this book for the architectural distinction between explicit workflows and autonomous orchestration. Its important additions are computational graphs, checkpointing, termination, structured output, middleware, observability, trajectory evaluation, protocols, and human delegation.

### Valliappa Lakshmanan and Hannes Hapke, *Generative AI Design Patterns*

Use this book for fine-grained application patterns: structured generation, RAG stages, deep search, reasoning, reflection, dependency injection, tool calling, code execution, multi-agent collaboration, caching, long-term memory, degradation testing, self-check, and guardrails.

### Sampriti Mitra, *System Design for the LLM Era*

Use this book for production constraints: gateways, circuit breakers, fallbacks, synchronous versus asynchronous processing, caching, data models, golden datasets, evaluation, observability, security, latency, and cost.

## Mathematical translation

The books are written for general AI systems. This series translates their patterns into mathematical artifacts: definitions, theorem statements, proof steps, dependencies, examples, counterexamples, citations, and review decisions.

The translation is deliberately not a claim that a language-model workflow is a
mathematical proof. The books supply architectural vocabulary; mathematical
validity still comes from definitions, hypotheses, formal or computational
checks, source verification, and the researcher's judgment.

## Selection principle

Do not use every pattern at once. Choose the smallest combination that makes the mathematical uncertainty visible and the important steps verifiable.
