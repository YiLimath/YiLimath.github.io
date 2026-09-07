---
title: "Agent Systems: Choosing and Composing Patterns"
permalink: /posts/2026/08/agent-system/choosing-patterns/
tags:
  - Agent System
---

## Outline

1. Start with the simplest deterministic structure that meets the task's needs.
2. Add a pattern only when it addresses a named source of complexity or uncertainty.
3. Compare patterns by latency, cost, observability, reliability, and ease of revision.
4. Discuss useful combinations: chaining + reflection; router + specialized tools; plan + memory; parallelization + aggregation + human review.
5. Include a decision table: task shape, recommended pattern, main failure mode.
6. End with three questions:
   - What is the task's main source of uncertainty?
   - Which interface makes that uncertainty observable?
   - What is the simplest pattern that provides that interface?
