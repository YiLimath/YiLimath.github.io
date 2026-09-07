---
title: 'Agent System Design Pattern'
date: 2026-08-01
permalink: /posts/2026/08/Agent-System/
tags:
  - Agent System
---

The aim of this series is to give a research-oriented introduction to design patterns for agent systems. The pages are independent, but they share one question:

> Where does the system need flexibility, and where does it need a stable, testable interface?

An agent system trades determinism for flexibility. A design pattern is a reusable way to buy back determinism at the boundary where the task requires it. Each page therefore describes the recurring problem, intent, structure, stable interface, variable implementation, trade-offs, failure modes, and an example.

## Part I. Foundations

1. [Terminology and atomic building blocks](/posts/2026/08/agent-system/foundations/)
2. [The core agent loop](/posts/2026/08/agent-system/core-loop/)
3. [Why mathematicians need agent design patterns](/posts/2026/08/agent-system/why-mathematicians-need-patterns/)

## Part II. Workflow and control-flow patterns

4. [Prompt chaining](/posts/2026/08/agent-system/prompt-chaining/)
5. [Router](/posts/2026/08/agent-system/router/)
6. [Parallelization](/posts/2026/08/agent-system/parallelization/)
7. [Plan and execute](/posts/2026/08/agent-system/plan-and-execute/)
8. [Exploration and discovery](/posts/2026/08/agent-system/exploration-and-discovery/)

## Part III. Knowledge and reasoning patterns

9. [Structured output and dependency injection](/posts/2026/08/agent-system/structured-output/)
10. [Tool use and code execution](/posts/2026/08/agent-system/tool-use/)
11. [Knowledge retrieval and provenance](/posts/2026/08/agent-system/knowledge-retrieval/)
12. [Deep search](/posts/2026/08/agent-system/deep-search/)
13. [Reasoning and representation change](/posts/2026/08/agent-system/reasoning/)
14. [Reflection](/posts/2026/08/agent-system/reflection/)

## Part IV. Multi-agent and human coordination

15. [Multiple-agent cooperation](/posts/2026/08/agent-system/multiple-agent-cooperation/)
16. [Inter-agent communication and protocols](/posts/2026/08/agent-system/inter-agent-communication/)
17. [Human delegation](/posts/2026/08/agent-system/human-in-the-loop/)

## Part V. Reliability and operations

18. [Memory management](/posts/2026/08/agent-system/memory-management/)
19. [Learning and adaptation](/posts/2026/08/agent-system/learning-and-adaptation/)
20. [Exception handling and recovery](/posts/2026/08/agent-system/exception-recovery/)
21. [Goal setting, prioritization, and termination](/posts/2026/08/agent-system/goal-monitoring/)
22. [Evaluation and monitoring](/posts/2026/08/agent-system/evaluation-monitoring/)
23. [Resource-aware optimization](/posts/2026/08/agent-system/resource-aware-optimization/)
24. [Guardrails and safety](/posts/2026/08/agent-system/guardrails-safety/)
25. [Choosing and composing patterns](/posts/2026/08/agent-system/choosing-patterns/)

## Part VI. Case study

26. [A mathematical research agent system](/posts/2026/08/agent-system/math-research-case-study/)
27. [Reference books and the pattern taxonomy](/posts/2026/08/agent-system/reference-map/)

The case study concerns daily research scheduling, paper encoding, and mathematical proof checking over an Obsidian vault. It identifies which patterns each component instantiates, where the system needs formal or deterministic checks, and where human mathematical judgment must remain in control.
