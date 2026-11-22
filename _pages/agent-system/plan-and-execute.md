---
title: "Proof Plans as Obligations and Alternatives"
permalink: /posts/2026/08/agent-system/plan-and-execute/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

A plan for Case A exposes the exact-sequence setup and two routes: prove sufficient vanishing, or control the obstruction of the chosen section directly. “Apply vanishing and lift” is a method suggestion until its hypotheses and return inference become explicit obligations.

## AND within an inference, OR between arguments

Each argument requires all its premises. A statement may have several alternative arguments. These relationships should be represented separately. Otherwise the scheduler may mistake jointly necessary premises for competing routes or require every alternative proof to succeed.

[![Alternative arguments and their dependencies](/images/agent-system/research-alternatives.svg)](/images/agent-system/research-alternatives.svg)

*Withdrawal suspends the argument using that premise. Another complete argument can still support the same conclusion.*

## Closure is not a vote

The advanced workbench computes a least fixed point. Start with admitted premise-free arguments and explicitly assumed statements. Repeatedly add a conclusion when one reviewed argument has all its premises available. Unsupported cycles never enter the closure by themselves.

The candidate graph may contain a cyclic alternative and an independent valid proof. Rejecting the whole graph would discard useful work. What matters is that the selected justification has grounded support. The simple introductory ledger uses the more conservative policy of rejecting cycles outright; the advanced implementation makes the distinction explicit.

This finite bookkeeping does not prove an induction scheme. Case C still needs base cases, step arguments, and a well-founded order for the indexed family. A finite simulation verifies only its encoded instances.

## Replanning preserves what was learned

If a sufficient vanishing condition is unavailable, retain the exact-sequence setup and the direct-obstruction route. Do not erase the entire plan or declare lifting impossible. Replanning changes the search frontier; it does not rewrite the target.

## Build and test

Run the alternative-route test. Then encode Case C through n=3, remove its base case, and inspect closure. Write the general induction argument separately. Explain which part the program checks and which part it assumes.

Read with the [three running cases](/posts/2026/08/agent-system/research-cases/). Source provenance and the distinction between established patterns and our proposed specialization are explained in [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

---

[Series guide](/posts/2026/08/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
