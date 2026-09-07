---
title: "Agent Systems: Choosing and Composing Patterns"
permalink: /posts/2026/08/agent-system/choosing-patterns/
tags:
  - Agent System
---

## Outline

1. Place the task on the workflow–autonomy spectrum: fixed workflow, bounded loop, or open-ended delegation.
2. Start with the simplest deterministic structure that meets the task's needs.
3. Add a pattern only when it addresses a named source of complexity or uncertainty.
4. Compare patterns by correctness, latency, cost, observability, reliability, reversibility, and ease of revision.
5. Discuss useful combinations: chaining + reflection; router + specialized tools; plan + memory; parallelization + aggregation + human review; retrieval + provenance + evaluation.
6. Include a decision table: task shape, recommended pattern, stable interface, and main failure mode.
7. End with three questions:
   - What is the task's main source of uncertainty?
   - Which interface makes that uncertainty observable?
   - What is the simplest pattern that provides that interface?
