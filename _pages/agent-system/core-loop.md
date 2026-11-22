---
title: "A Research Loop Changes an Obligation"
permalink: /posts/2026/08/agent-system/core-loop/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/codex-research-studio/).


In Case A, finding an invertibility theorem is not completion: the actual matrix and its hypotheses must match. The next action may be an applicability check rather than another proof draft. A useful iteration begins with an open obligation and ends with a recorded change.

## The contract

The controller selects an action under a budget, executes it, stores the observation, and updates the frontier. Admission of a claim is a separate transition. Record target version, input artifacts, action, output, cost, and resulting status. A retry is a new attempt on the same target; changing the target creates a new task version.

## Trade-offs and failure modes

Every action should have an informative possible outcome: a usable theorem, a rejected match, a localized gap, or a new example. A failed branch returns control to the scheduler rather than restarting indefinitely. Keep infrastructure success separate from mathematical progress.

## Build and test

Replay three actions: try an invertibility criterion, discover a zero determinant, and test whether the requested vector is nevertheless in the image. Save the trace and mark the exact replanning event.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: make one iteration produce a state change

Begin with an exact unresolved obligation. Choose an action that could resolve or sharpen it, inspect the evidence returned, and update the record. A repeated suggestion with no new argument, source, or counterexample is not a productive iteration.

**Acceptance exercise.** For each iteration, write what was known before, what evidence arrived, and what changed. Permit “still unresolved” as an honest result, but require a different next action or a reason to stop.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
