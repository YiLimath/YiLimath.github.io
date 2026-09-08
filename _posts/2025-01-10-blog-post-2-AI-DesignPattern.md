---
title: 'Agent System Design Pattern'
date: 2026-08-01
permalink: /posts/2026/08/Agent-System/
tags:
  - Agent System
classes: agent-system-hub
full_page_reading: true
---

The aim of this series is to give an introduction to design patterns for agent systems. The pages are independent, but they share one question:

> Where does the system need flexibility, and where does it need a stable, testable interface?

An agent system trades determinism for flexibility. A design pattern is a reusable way to buy back determinism at the boundary where the task requires it. Each page therefore describes the recurring problem, intent, structure, stable interface, variable implementation, trade-offs, failure modes, and an example.

![Agent system system context view](/images/agent-system/00-agent-system-architecture.svg)

*Architecture figure: the system context view introduces the agent system's
external relationships; its internal containers are explained on the
architecture-views page.*

Claim. This series of blog posts are finished under the cooperation of AI.


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
25. [Production architecture](/posts/2026/08/agent-system/production-architecture/)
26. [Choosing and composing patterns](/posts/2026/08/agent-system/choosing-patterns/)
27. [Architecture views](/posts/2026/08/agent-system/architecture-views/)

## Part VI. Case study and domain-specific design

28. [Danus and Rethlas](/posts/2026/08/agent-system/math-research-case-study/)
29. [A spiral-induction agent for birational geometry](/posts/2026/08/agent-system/birational-geometry-agent/)

The case study uses the real Danus and Rethlas codebases. The new domain-specific
page then sketches how the same pattern vocabulary can be organized around the
spiraling induction that appears in birational-geometry proof architecture.
