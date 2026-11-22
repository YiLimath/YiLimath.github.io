---
title: "Learn Search Preferences, Not Unproved Theorems"
permalink: /posts/2026/08/agent-system/learning-and-adaptation/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/evaluation-monitoring/).


Repeated success with matrix inversion can justify trying it earlier on related linear systems. It does not establish invertibility in every new case. The learned object is a scoped search preference.

## The contract

Record the task family, proposed policy change, supporting episodes, and held-out results. Keep mutable rankings separate from mathematical evidence. A policy rollback should not rewrite the theorem ledger.

## Trade-offs and failure modes

Include difficult negative cases when evaluating adaptation. A policy that improves easy examples can hide rare missing-hypothesis failures. Changing the evidence policy is a separate migration and may require rechecking old records.

## Build and test

Tune a route preference on invertible matrices, then test a singular matrix with one solvable and one impossible requested vector. Direct compatibility checking must remain available.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: learn a method with its eligibility conditions

A successful compactness argument may suggest a reusable method: obtain uniform bounds, choose a topology, extract a subsequence, identify the limit. Store the necessary hypotheses with that sequence. “Use compactness” alone is not reusable mathematical knowledge.

**Acceptance exercise.** Test the extracted method on a nearby problem lacking the bound. It should expose a missing premise. Record failures and scope restrictions alongside successes to avoid teaching the system a false universal rule.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
