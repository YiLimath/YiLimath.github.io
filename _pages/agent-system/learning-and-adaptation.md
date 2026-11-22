---
title: "Learn Search Preferences, Not Unproved Theorems"
permalink: /posts/2026/08/agent-system/learning-and-adaptation/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/evaluation-monitoring/). Geometry references below refer to the optional extension of Case A.


Repeated success with vanishing can justify trying it earlier on related lifting tasks. It does not establish the positivity needed in every new case. The learned object is a scoped search preference.

## The contract

Record the task family, proposed policy change, supporting episodes, and held-out results. Keep mutable rankings separate from mathematical evidence. A policy rollback should not rewrite the theorem ledger.

## Trade-offs and failure modes

Include difficult negative cases when evaluating adaptation. A policy that improves easy examples can hide rare missing-hypothesis failures. Changing the evidence policy is a separate migration and may require rechecking old records.

## Build and test

Tune a route preference on vanishing-friendly fixtures, then evaluate it on the two-point divisor. The direct-obstruction alternative must remain available.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
