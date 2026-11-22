---
title: "Advanced Project: Test a Method Before Trusting a Proof Plan"
permalink: /posts/2026/08/agent-system/proof-sketch-system/
tags:
  - Agent System
  - Mathematics
  - Automated Reasoning
classes: agent-system-page
full_page_reading: true
---

A useful method recommendation ends with an attempted mathematical argument. This project asks Codex to compare routes, identify their decisive obligations, and work on one of those obligations. No orchestration software is required.

## The controlled mathematical task

Let X be a projective variety, L a line bundle, D an effective Cartier divisor, and s a specified section of L restricted to D. Determine whether this particular s lifts to a global section of L. Work from the exact sequence

$$0\to L(-D)\to L\to L|_D\to0.$$

The connecting map gives the exact criterion: s lifts if and only if its image under the connecting homomorphism is zero. Vanishing of the entire group H¹(X,L(-D)) is sufficient but need not be necessary for this chosen section.

There are therefore two genuinely different routes: prove a sufficient vanishing theorem, or compute the obstruction for s. Recommending vanishing without checking its hypotheses is not a method selection success.

## Build the workspace in Codex

```text
Create TARGET.md, METHODS.md, ATTEMPTS.md, and REVIEW.md.
Record X, L, D, and the specified section s exactly.
Compare two routes: sufficient cohomology vanishing and direct obstruction.
For each route list prerequisites, applicable source results, and missing steps.
Do not change 'this section lifts' into 'some section lifts'.
Choose one decisive mathematical calculation and carry it out in ATTEMPTS.md.
Keep failed attempts and distinguish supplied facts from checked arguments.
```

This small architecture has four responsibilities: preserve the target, compare applicable methods, attempt a bridge, and review the result. Files make those responsibilities inspectable; instructions alone do not enforce them.

## A worked case with a decisive answer

Take X to be the projective line over a field k, L the trivial bundle, and D the sum of two distinct k-rational points. Identify sections on D with pairs in k². Global sections of L are constants, so restriction sends c to (c,c).

Consequently (1,1) lifts and (1,0) does not. Both have the same ambient geometric data. A policy looking only at the variety, line bundle, or a broad method label cannot distinguish them. The direct restriction computation can.

```text
Carry out the two-point calculation from the stated definitions.
Explain why all global sections of the trivial bundle on the projective line
are constants, citing or supplying the needed justification.
Compute the restriction image and test both sections separately.
Then explain why failure of a sufficient vanishing condition alone would
not prove that either specified section fails to lift.
```

The mathematical answer above is the reference calculation. It is not a claim that a Codex run has already reproduced it. Save the actual response and inspect its reasoning.

## Move from the control to research

Select a lifting step in a proof you understand. Supply the actual statement and source excerpt. Require an applicability table for the vanishing route and an explicit obstruction target for the direct route. Attempt whichever unresolved step could most change the assessment within your budget.

Reject a proof plan that hides its main difficulty in 'standard arguments'. A conditional plan remains useful when its missing lemma is exact and its implication back to the target is justified.

## Evaluation and submission

Test both sections, then change the target version and present an old review. Check that the assistant preserves the chosen section and does not reuse an irrelevant verdict. Compare with an ordinary request to suggest a proof method using the same evidence and time budget.

Submit the exact target, two method cards, full attempted calculation, review findings, and remaining obligations. A persuasive method list without an attempted bridge does not pass.

[Build the base workspace](/posts/2026/08/agent-system/codex-research-studio/) · [Course roadmap](/posts/2026/12/Agent-System/)

