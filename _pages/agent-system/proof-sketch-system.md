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

A method recommendation should lead to a mathematical attempt. For surface uniqueness, compare the signed negativity proof with the last-blowup proof. Their distinction concerns actual prerequisites and costs. The [central workshop](/posts/2026/08/agent-system/birational-proof-workshop/) supplies both complete arguments.

## State each method's decisive obligation

For the negativity route, define $D=p^{\ast}K_X-q^{\ast}K_Y$. Apply [Birkar Lemma 4.15](https://arxiv.org/pdf/1210.2670v1#page=21) first to D over X, then to -D over Y. Each application needs relative nefness of the submitted divisor's negative and effectivity of its pushforward. Descent remains a separate obligation.

For the last-blowup route, minimize the number of point blowups in p. Its last exceptional curve is either q-contracted, allowing a shorter resolution, or has canonical intersection both -1 and nonnegative. The latter contradiction requires proving the curve is not a component of the effective q-error.

| Method | Decisive evidence | Return to the target |
|---|---|---|
| Negativity | Opposite coefficient inequalities | Identify contracted curves and descend |
| Last blowup | Canonical intersection contradiction | Exclude nontrivial p, then nontrivial q |

A method record needs these prerequisites and implications, not only a name and a confidence score. This distinction is related to methods in [Bundy, Proof Planning, pp. 261–262](https://cdn.aaai.org/AIPS/1996/AIPS96-033.pdf#page=1); the paper does not validate our proposed agent workflow.

## Attempt the bridge before recommending the route

If the exact negativity statement has not been inspected, check it first. If the divisor comparison is complete, finish descent rather than generate another proof tree. If the last-blowup proof assumes a curve lies outside the error support, derive that fact from minimality.

The expected output is an inequality, factorization, or contradiction with its justification. A recommendation ending “standard arguments finish” has not tested its hardest bridge.

## Transfer carefully

Relative nefness over S requires checking that the curve images are contracted over S. In higher dimension, the surface factorization and final descent need replacement; divisorial information alone does not exclude small exceptional loci. An isomorphism-in-codimension-one conclusion would be a different target with its own source and proof.

In the analytic category, inspect actual replacements for negativity and descent. Source unavailability leaves an obligation open; it does not refute the desired statement.

## Measure whether method selection helps

Ask for at most two routes, their decisive inputs, and an attempted bridge. Choose on the basis of that mathematics. Preserve useful partial arguments from an abandoned route. Compare with a direct request using the same sources and total allowance, counting preparation and discarded branches.

If planning adds overhead without improving proof quality, use a harder unfamiliar lemma or simplify the intervention. The reference proofs are not experimental results.

## Advanced assignment

Choose a source-dependent proof in your birational research and a precise hypothesis change. Locate the first failed application. Develop a local repair and an alternative route avoiding that application; attempt their decisive obligations before recommending either.

Submit the inspected statements, applicability analyses, actual proof attempts, and a supported next decision. A known consequence is not a novelty claim; a precise obstruction can be useful progress. The assignment is incomplete if it contains only possible lemmas and no attempted bridge.

[Course roadmap](/posts/2026/12/Agent-System/)
