---
title: "Module 4. Preserve the implication back to the target"
permalink: /posts/2026/08/agent-system/reasoning/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

The surface uniqueness argument moves from X and Y to a common resolution W. Working on W makes the divisor comparison possible, but the target is still an isomorphism between X and Y. This module closes that return implication explicitly.

Use the [central birational proof](/posts/2026/08/agent-system/birational-proof-workshop/) for the complete setup. The purpose of the workflow is to help an agent finish this specific missing bridge rather than keep generating more calculations on W.

## 1. Identify what the reduction has bought

Choose compatible canonical divisors on a smooth common resolution and write

$$
K_W=p^{\ast}K_X+E_p=q^{\ast}K_Y+E_q.
$$

The two signed negativity applications establish $p^{\ast}K_X=q^{\ast}K_Y$, hence $E_p=E_q$. This is important progress, but the equality is on W. It is not yet a morphism on X or Y.

A useful proof state names both the intermediate result and the missing implication. “Comparison complete; descent open” is more informative than either “almost done” or “start another proof.” The next task should be bounded by the exact return obligation.

## 2. Prove equality of the contracted curves

For a point blowup, the canonical error is the exceptional curve with coefficient one. Under a sequence of blowups, each old error pulls back effectively and each new exceptional curve receives a positive coefficient. Thus $E_p$ and $E_q$ have positive coefficients precisely on the curves contracted by p and q respectively.

Consequently equality of these divisors gives equality of their supports and hence equality of the contracted curves. Do not omit the positivity argument. If an error divisor could have coefficient zero on an exceptional component, its support would not recover the whole exceptional locus.

The canonical calculation and its induction are written out in the workshop. Factorization into point blowups is an imported surface theorem: [Stacks Tag 0C5R](https://stacks.math.columbia.edu/tag/0C5R).

## 3. Descend one step, then repeat

Factor p and write its last blowup as $b:W\to W'$, so $p=p'\circ b$. Let C be the exceptional curve of b. It is p-contracted, hence q-contracted by the preceding comparison.

[Stacks Tag 0C5J](https://stacks.math.columbia.edu/tag/0C5J) now applies: because q maps C to a point, there is a unique morphism $q':W'\to Y$ such that

$$
q=q'\circ b.
$$

The construction has removed one blowup from p, but we still need to know that the induction can continue. For each curve on W', its strict transform on W is contracted by p precisely when the curve is contracted by $p'$, and similarly for q and $q'$. Equality of contracted curves therefore survives on W'.

Repeat along the finite factorization. At the end, q has descended to a morphism $a:X\to Y$ satisfying $q=a\circ p$. This is a proved return step, not an instruction to “descend by standard arguments.”

## 4. A morphism is not yet an isomorphism

Apply the same reasoning with p and q exchanged. Obtain $b_0:Y\to X$ such that $p=b_0\circ q$. On the common dense open set, a and $b_0$ induce inverse birational maps.

Their compositions agree with the respective identities on that dense open set. Since the surfaces are integral and separated, the equalizers are closed and contain the dense open sets, so the compositions are identities everywhere. Thus a is the required isomorphism, extending the original specified map.

This argument illustrates two distinct stops that are too early: equality of the canonical pullbacks, and a morphism in only one direction. A completion criterion must name the actual conclusion rather than a familiar intermediate milestone.

## 5. Why the same picture is not a proof in every dimension

The return step used surface-specific facts: factorization into point blowups, exceptional curves, and their contraction property. In higher dimension, divisorial information alone does not exclude small exceptional loci. A model that substitutes “variety” for “surface” has changed the proof's inputs.

The right extension question is which theorem replaces the missing implication. It may lead to an isomorphism in codimension one or to another statement, but that conclusion must be retrieved and proved under its own hypotheses. Do not silently weaken the original target and then report it solved.

## 6. Transfer to relative nefness

Let X and Y map to a common projective base S, with the birational map over S. Suppose the canonical divisors are nef over S. The comparison route still needs to check that the curves used in its intersection inequalities lie over points of S.

On a common resolution over S, a p-contracted curve maps to a point of S. If q does not contract it, its q-image is a curve contracted by $Y\to S$. Relative nefness supplies the same nonnegative intersection. The symmetric argument works over Y.

The descent and inverse construction then take place over S. The useful new input is commutativity over the base. Replacing absolute nefness by relative nefness is not justified by a notation change alone.

## 7. Test whether a focused return task helps

Keep a baseline proof that stops at $E_p=E_q$. Give the same agent the established comparison and the exact remaining target, without supplying the completed descent argument. Ask it to locate and apply the contraction property and to justify its repetition.

```text
Take the proved equality E_p=E_q as input, with positive coefficients
on all exceptional curves. The original target is an isomorphism X → Y.
Prove the one-step factorization of q through the last blowup of p.
Show why the invariant needed to repeat the step survives.
Construct the inverse and check that the given birational map is extended.
```

Count the cost of this intervention and compare it with an unrestricted request to finish the original proof. If the baseline already supplies descent correctly, no capability gain has been shown; use a harder transfer or compare resource cost.

**Exercises.** Identify the first unsupported step in a proof that knows only equality of numerical classes of the error divisors. Explain why the argument above used equality of actual divisors. Next remove the positive-support information and identify which inference becomes open. Finally state the additional evidence needed to work over S.

A successful submission supplies the missing mathematics. A dependency diagram or a correct description of the gap alone is a diagnosis, not its solution.

[Next: review and admission](/posts/2026/08/agent-system/verification-gate/) · [Course roadmap](/posts/2026/12/Agent-System/)
