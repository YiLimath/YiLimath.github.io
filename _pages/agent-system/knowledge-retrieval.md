---
title: "Module 3. Turn a source into a justified theorem application"
permalink: /posts/2026/08/agent-system/knowledge-retrieval/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

A relevant theorem can be correctly quoted and incorrectly applied. In the surface uniqueness proof, the critical retrieval task is not “find something about negativity.” It is to find a version whose hypotheses support the exact signed divisor and morphism in the argument.

This module turns that distinction into a source-based proof task. The [central workshop](/posts/2026/08/agent-system/birational-proof-workshop/) supplies the full target and proof; here we focus on the applications that make the comparison legitimate.

## 1. Read the theorem before designing the search

[Birkar, *Lectures on Birational Geometry*, Lemma 4.15, p. 21](https://arxiv.org/pdf/1210.2670v1#page=21) concerns a projective birational morphism of normal varieties and an R-Cartier divisor B whose negative is relatively nef. It says that effectivity of B is equivalent to effectivity of its pushforward.

This statement is more useful here than a remembered slogan such as “exceptional nef divisors are negative.” The slogan hides both the sign convention and the hypotheses. It can also tempt the agent to demand exceptional support for a divisor before that support has been established.

Keep the actual locator, version, and statement available. A search result title is not the source statement. A retrieved theorem is not yet a premise for the current proof.

## 2. Complete the first application

On the common resolution, use compatible canonical divisors and put

$$
D=p^{\ast}K_X-q^{\ast}K_Y=E_q-E_p.
$$

To prove $D\geq0$, instantiate Birkar's lemma as follows.

| Source requirement | Current objects | Justification |
|---|---|---|
| Projective birational morphism | $p:W\to X$ | The chosen common resolution |
| Normal varieties | W and X | They are smooth |
| R-Cartier divisor | D on W | Difference of pullbacks of canonical Cartier divisors |
| Negative relatively nef | $-D$ over X | For p-contracted C, $(-D)\cdot C=q^{\ast}K_Y\cdot C\geq0$ |
| Effective pushforward | $p_{\ast}D$ | $p_{\ast}E_p=0$, so $p_{\ast}D=p_{\ast}E_q\geq0$ |

Only after all rows are justified does the conclusion follow. The intersection inequality uses the projection formula and nefness of $K_Y$. If q contracts C it gives zero; otherwise it uses the nonnegative canonical intersection with its image curve, with its positive pushforward multiplicity.

Notice what the application did not need: D was not assumed exceptional over X. The version we inspected asks for an effective pushforward. Proving a stronger unnecessary hypothesis would add work and may introduce circularity.

## 3. Do not copy the first application into the second

For the reverse inequality, the divisor submitted to the lemma is -D and the morphism is q. Its required negative is D. For a q-contracted curve C,

$$
D\cdot C=p^{\ast}K_X\cdot C\geq0,
$$

and $q_{\ast}(-D)=q_{\ast}E_p\geq0$. Thus $-D\geq0$.

The source theorem is reused, but its application is new. The two instances use different nefness assumptions. Removing nefness of $K_X$ leaves the first intact and invalidates the previous justification of the second. This is why a source record and an application record should not be the same object.

## 4. Retrieve the missing return theorem

After the two applications, the errors agree and the same curves are contracted. An answer that now says “therefore isomorphic” may still be incomplete.

[Stacks Tag 0C5R](https://stacks.math.columbia.edu/tag/0C5R) gives factorization of a proper birational morphism between regular surfaces into point blowups. [Tag 0C5J](https://stacks.math.columbia.edu/tag/0C5J) supplies the required universal property of a contraction: a morphism mapping its exceptional curve to a point factors through it.

At the last blowup in p, equality of the contracted curves tells us q maps that curve to a point. This is the applicability check. The theorem then gives a morphism on the contracted surface. Repeating the argument eventually gives a morphism from X to Y. The reverse construction supplies its inverse.

A useful search therefore begins with the missing implication: “factor a morphism through the contraction of an exceptional curve.” It does not repeatedly ask for broad surveys of minimal models.

## 5. Handle a change of category honestly

Suppose the project changes from smooth projective algebraic surfaces to compact complex spaces. Do not reuse the projective algebraic theorem merely because the word “birational” has been replaced by “bimeromorphic.” Identify the analytic result actually needed, its Cartier and positivity assumptions, and the conditions on the map.

If an appropriate theorem has not been inspected, the application remains open. That is a reason to search or prove a replacement, not a counterexample to the desired geometric statement. Conversely, an accessible theorem with a missing hypothesis does not close the gap merely because it has a familiar conclusion.

No analytic extension is claimed in this module. A serious research submission must supply the actual replacement source or an attempted lemma.

## 6. Make source use save work

Retain one inspected version of the negativity lemma with its exact scope, then attach each application separately. Reusing the statement can avoid repeated downloads and re-extraction. Reusing an old verdict without rechecking the changed objects is a different operation and can be invalid.

```text
For this proof, inspect the stated version of the negativity lemma.
Give two separate substitutions: B=D over X, and B=-D over Y.
For each, prove relative nefness of -B and effectivity of its pushforward.
Identify any condition you are assuming rather than establishing.
Then find and apply the exact descent result needed after E_p=E_q.
```

Compare this intervention with the direct attempt using the same available sources. Count source inspections, corrections, and total time or tokens where measured. A source table that merely restates the question has no demonstrated benefit.

## 7. Exercises

**Wrong-sign application.** A report concludes $D\leq0$ from the first application over X. Locate the error and state what additional argument establishes the reverse inequality. The answer must name the divisor submitted to the source theorem.

**Unnecessary premise.** A worker stops because it cannot prove D is p-exceptional. Determine whether that premise is required by the inspected version. Explain why forcing it could assume the relation between exceptional loci that the proof is intended to establish.

**Relative transfer.** Over a common base S, replace absolute nefness by relative nefness. Explain why a p-contracted curve has image under q contained in a fiber over S. Without the commuting diagram, this substitution is not justified.

**Source correction.** If a theorem passage is corrected, inspect which application rows change. Do not discard the canonical identities unless the correction affects their own evidence.

A successful submission contains usable mathematics: two sound negativity applications and one sound descent application. The workflow proposals are not themselves established by these mathematical references; their usefulness must be observed in the run.

[Next: preserve the return implication](/posts/2026/08/agent-system/reasoning/) · [Course roadmap](/posts/2026/12/Agent-System/)
