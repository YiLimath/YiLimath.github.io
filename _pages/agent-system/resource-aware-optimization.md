---
title: "Spend Computation Where It Can Change the Argument"
permalink: /posts/2026/08/agent-system/resource-aware-optimization/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/plan-and-execute/).


A general solvability theorem may cost more than directly checking the chosen output’s compatibility conditions. Rank routes by expected information, usefulness, cost, and shared prerequisites, treating every estimate as a heuristic.

## The contract

Prioritize bottlenecks that unlock several routes or cheaply expose a false premise. Preserve some exploration budget for alternatives. Repeatedly polishing prose cannot discharge a missing hypothesis.

## Trade-offs and failure modes

Choose tools and models by measured performance on the task. Cheap parsing does not replace mathematical review. When resources run out, reduce scope honestly and export the evidence and frontier; do not lower the meaning of “proved.”

## Build and test

Allocate twelve action units across Case A’s routes. Declare predicted cost and benefit, run the schedule, and compare it with a simple sequential baseline.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: spend effort where a decision can change

A project may have ten routine checks and one unknown uniform estimate. Completing more routine checks can make the dossier longer without making the project more feasible. Allocate a bounded attempt to the estimate and specify what a positive, negative, or inconclusive result would change.

**Acceptance exercise.** Record effort and resulting decision changes. Stop when the next action merely repeats an unchanged attempt; continue when a new source, example, or reduction materially changes the unresolved obligation.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
