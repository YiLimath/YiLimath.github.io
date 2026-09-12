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

![Agent system: system context view](/images/agent-system/00-agent-system-architecture.svg)

*Architecture figure: the system context view introduces the agent system's
external relationships; its internal containers are explained on the
architecture-views page.*

> Claim. This series of blog posts was written in cooperation with AI.


## Part I. Foundations

1. [Terminology and atomic building blocks](/posts/2026/08/agent-system/foundations/)
2. [The core agent loop](/posts/2026/08/agent-system/core-loop/)
3. [Variation points and the stable interface](/posts/2026/08/agent-system/variation-points/)


## Part II. Workflow and control-flow patterns

5. [Prompt chaining](/posts/2026/08/agent-system/prompt-chaining/)
6. [Router](/posts/2026/08/agent-system/router/)
7. [Parallelization](/posts/2026/08/agent-system/parallelization/)
8. [Plan and execute](/posts/2026/08/agent-system/plan-and-execute/)
9. [Exploration and discovery](/posts/2026/08/agent-system/exploration-and-discovery/)

## Part III. Knowledge and reasoning patterns

10. [Context engineering](/posts/2026/08/agent-system/context-engineering/)
11. [Structured output and dependency injection](/posts/2026/08/agent-system/structured-output/)
12. [Tool use and code execution](/posts/2026/08/agent-system/tool-use/)
13. [Knowledge retrieval and provenance](/posts/2026/08/agent-system/knowledge-retrieval/)
14. [Deep search](/posts/2026/08/agent-system/deep-search/)
15. [Reasoning and representation change](/posts/2026/08/agent-system/reasoning/)
16. [Reflection](/posts/2026/08/agent-system/reflection/)

## Part IV. Multi-agent and human coordination

17. [Multiple-agent cooperation](/posts/2026/08/agent-system/multiple-agent-cooperation/)
18. [Inter-agent communication and protocols](/posts/2026/08/agent-system/inter-agent-communication/)
19. [Human delegation](/posts/2026/08/agent-system/human-in-the-loop/)

## Part V. Reliability and operations

20. [Memory management](/posts/2026/08/agent-system/memory-management/)
21. [Learning and adaptation](/posts/2026/08/agent-system/learning-and-adaptation/)
22. [Exception handling and recovery](/posts/2026/08/agent-system/exception-recovery/)
23. [Goal setting, prioritization, and termination](/posts/2026/08/agent-system/goal-monitoring/)
24. [Evaluation and monitoring](/posts/2026/08/agent-system/evaluation-monitoring/)
25. [The verification gate](/posts/2026/08/agent-system/verification-gate/)
26. [Resource-aware optimization](/posts/2026/08/agent-system/resource-aware-optimization/)
27. [Guardrails and safety](/posts/2026/08/agent-system/guardrails-safety/)
28. [Production architecture](/posts/2026/08/agent-system/production-architecture/)
29. [Choosing and composing patterns](/posts/2026/08/agent-system/choosing-patterns/)
30. [Architecture views](/posts/2026/08/agent-system/architecture-views/)

## Part VI. Case study and domain-specific design

31. [Danus and Rethlas](/posts/2026/08/agent-system/math-research-case-study/)
32. [Proof-sketch and method-recommendation system](/posts/2026/08/agent-system/proof-sketch-system/)
33. [Building an agent system for birational geometry](/posts/2026/08/agent-system/birational-geometry-agent/)

The first case study uses the real Danus and Rethlas codebases. The
proof-sketch page develops a professional architecture for recommending proof
methods and compiling them into critic-tested obligation graphs. The final page
specializes that architecture to the spiraling induction that appears in
birational geometry.

## References

The series draws on six books, each covering a different altitude. Individual
pages cite chapters and sections; this is the shared basis.

1. Antonio Gulli, *Agentic Design Patterns: A Hands-On Guide to Building
   Intelligent Systems*, Springer, 2025.
   [Publisher record](https://link.springer.com/book/10.1007/978-3-032-01402-3).
   The broadest pattern catalogue, and the closest to this series' organization.
2. Victor Dibia, *Designing Multi-Agent Systems: Principles, Patterns, and
   Implementation for AI Agents*, 2025. [Book site](https://multiagentbook.com/).
   Strongest on the execution loop, context engineering, agent composition, and
   evaluation of trajectories rather than answers.
3. Valliappa Lakshmanan and Hannes Hapke, *Generative AI Design Patterns*,
   O'Reilly, first edition, October 2025.
   [Publisher record](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/).
   Thirty-two numbered patterns at the level of individual mechanisms, including
   the retrieval, judging, and guardrail patterns used here.
4. Sampriti Mitra, *System Design for the LLM Era: Patterns and Principles for
   Production-Grade AI Architecture*, Packt, first edition.
   [Publisher record](https://www.packtpub.com/en-us/product/system-design-for-the-llm-era-9781807789923).
   The production and security altitude: gateways, fallbacks, caching, cost
   control, observability, and the named security threats.
5. James Phoenix and Mike Taylor, *Prompt Engineering for Generative AI*,
   O'Reilly, first edition, May 2024, ISBN 978-1-098-15343-4. The level below the
   patterns: what a single well-specified inference should contain.
6. Stephen Clear, *Claude AI Bible: The Complete Guide to Mastering Claude,
   Claude Code, MCP, AI Agents and Automation*. A practitioner reference for
   tool protocols, packaged capabilities, and agent SDK mechanics.

Primary research papers are cited on the pages where they apply, rather than
collected here, so that each claim sits next to its source.
