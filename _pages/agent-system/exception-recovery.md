---
title: "Distinguish a Tool Failure from a Mathematical Obstruction"
permalink: /posts/2026/08/agent-system/exception-recovery/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/memory-management/). Geometry references below refer to the optional extension of Case A.


A timeout, inaccessible source, malformed record, and nonzero connecting class require different responses. Only the last may establish that the chosen section does not lift, and only with mathematical evidence.

## The contract

Classify before retrying. Bound transient retries, repair malformed inputs, seek another source where appropriate, and replan when the route fails mathematically. Save completed observations at artifact boundaries before acknowledging work.

## Trade-offs and failure modes

A restarted worker should consume the same versioned inputs or create a new attempt. It must not merge fragments from different sheaves or sections. A failed method leaves the target open unless its failure actually proves the target false.

## Build and test

Inject a timeout, stale review, and nonzero obstruction. Write three recovery records and justify which one, if any, supports a mathematical conclusion.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
