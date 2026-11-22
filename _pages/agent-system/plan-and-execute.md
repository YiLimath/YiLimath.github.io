---
title: "Module 2. Plan with joint premises and alternative routes"
permalink: /posts/2026/08/agent-system/plan-and-execute/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

A proof plan is useful when it selects an achievable next obligation and avoids work that the target does not require. We continue the surface uniqueness problem from Module 1: a given birational map between smooth projective surfaces with nef canonical divisors should extend to an isomorphism.

The task is to choose between two actual proofs, not to generate a long list of strategies. Both complete arguments are in the [central workshop](/posts/2026/08/agent-system/birational-proof-workshop/). Attempt the problem before reading them if you want an informative baseline.

## 1. Plan with implications, not job titles

A plan saying “research, reason, verify” names activities but does not explain why the target should follow. The negativity route has a mathematical chain:

$$
\begin{gathered}
\text{common resolution and canonical identities}\\
\Longrightarrow D\geq0\text{ and }D\leq0\\
\Longrightarrow E_p=E_q\\
\Longrightarrow\text{same contracted curves}\\
\Longrightarrow\text{descent and an isomorphism}.
\end{gathered}
$$

Each arrow has prerequisites. In particular, the two inequalities require different signed applications; the support step requires positive coefficients on every exceptional curve; and the final arrow needs a descent theorem. A completed task called “compare divisors” does not certify all three.

The classical distinction between proof methods and their applicability conditions is developed in [Bundy, “Proof Planning,” pp. 261–262](https://cdn.aaai.org/AIPS/1996/AIPS96-033.pdf#page=1). The source motivates this representation; it does not establish that our agent workflow will be efficient.

## 2. Compare the two routes before expanding both

| Route | Decisive move | Inputs that must be available | Characteristic failure |
|---|---|---|---|
| Negativity | Prove opposite coefficient inequalities for D | Common resolution, canonical errors, relative nefness, effective pushforwards, negativity lemma | Wrong sign or a missing descent step |
| Last blowup | Intersect the last exceptional curve with the canonical divisor | Minimal blowup count, blowup formula, descent through a contracted curve, nefness | Using a negative intersection without checking the curve is not a component of the error divisor |

The second route is especially short for surfaces. Choose a common resolution with the number of blowups in p minimal. If p is nontrivial, let C be its last exceptional curve. If q contracts C, q descends through that blowup and contradicts minimality. Otherwise C is not a component of the effective error $E_q$, and

$$
-1=K_W\cdot C=(q^{\ast}K_Y+E_q)\cdot C\geq0,
$$

a contradiction. The rest of the proof excludes a nontrivial q using nefness of $K_X$.

This is a method with a specific surface input. It is not a general recipe for arbitrary birational models. The first route may be a better starting point for a different category, but that possibility must be assessed by the actual hypotheses and missing lemmas.

## 3. Select the next action from the current obstruction

Suppose the baseline has already established the canonical identities but repeatedly mishandles the sign in negativity. The next useful action is to instantiate the exact lemma with B=D over X and B=-D over Y. Searching for further common resolutions adds no evidence to that gap.

Suppose instead the divisor comparison is complete but descent is missing. Retrieve [Stacks Tag 0C5J](https://stacks.math.columbia.edu/tag/0C5J), check that q contracts the last exceptional curve of p, and factor q. Repeating the comparison is wasted work unless a new doubt about it has appeared.

A plan should name the expected mathematical output of each action. “Read a paper” is an activity. “Locate a theorem allowing a morphism constant on the exceptional curve to factor through its contraction, then check its hypotheses” is a bounded research action.

## 4. Joint prerequisites and alternative routes

Within the negativity route, both inequalities are required. Between the two complete routes, either valid proof suffices. These are different relationships. A scheduler that treats the inequalities as alternatives can stop too early; one that insists on completing both full proofs can waste resources.

A second route is worthwhile when it supplies a cheaper proof, a genuinely different check, or information relevant to a planned extension. Do not expand it only to create the appearance of independent corroboration. Two workers invoking the same unproved descent implication still share the same gap.

Keep a plan conditional until its inputs are justified. “Assuming descent, the argument concludes” is useful progress if descent is an explicit obligation. It is not an accepted proof of the target.

## 5. Replan after mathematical evidence changes

Remove nefness of $K_X$. In the first route, $D\geq0$ still follows from nefness of $K_Y$, while the reverse inequality loses its justification. The blowup of an abelian surface supplies a counterexample to the weakened target. At this point the right action is to stop trying to prove that false statement, not to allocate more workers.

For the relative-nef variant over S, the target is not refuted. The decisive check is whether each curve used in the inequality is contracted over S. A common resolution commuting with the maps to S supplies that condition. Replanning should distinguish a demonstrated obstruction from a missing application check.

## 6. A bounded planning experiment

Start with the same theorem, source packet, model, and total allowance in two fresh sessions. Let one attempt a direct proof. In the other, request at most two routes, their decisive inputs, and a choice of one route before full expansion.

```text
Compare the negativity and last-blowup routes for this surface target.
For each, state the decisive lemma and the implication back to isomorphism.
Use the current proved state; do not redo established constructions.
Choose one route, attempt its first unresolved obligation, and revise
only when the result gives a mathematical reason to do so.
```

Preserve unsuccessful actions and source lookups. If the structured run is more expensive but no more correct, it has not demonstrated a benefit. If the baseline succeeds immediately, use an unfamiliar lemma from your research or evaluate cost rather than claiming increased capability.

## 7. Exercises and acceptance

**Find a premature stop.** A plan has proved only $D\geq0$. Explain why it cannot yet use equality of exceptional supports, then specify the next signed application.

**Audit a shortcut.** In the last-blowup route, justify why $E_q\cdot C\geq0$. The answer must establish that C is not a component of $E_q$; effectivity alone is insufficient when the curve is a component.

**Choose between further search and proof.** If Tag 0C5J has been located and its hypotheses match, complete the application before issuing broader literature searches. Record whether the intervention saves repeated lookup or closes a stalled step.

**Transfer.** Explain which part of either route is specifically two-dimensional before considering a higher-dimensional uniqueness claim. A valid surface proof does not justify changing the dimension in the target.

Submit the chosen route, its completed argument or exact remaining gap, and the action record. Measure solved obligations and total resources, not the size of the plan.

[Next: use the literature](/posts/2026/08/agent-system/knowledge-retrieval/) · [Course roadmap](/posts/2026/12/Agent-System/)
