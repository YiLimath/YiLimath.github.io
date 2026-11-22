---
title: "Module 8. Divide work only when the evidence benefits"
permalink: /posts/2026/08/agent-system/multiple-agent-cooperation/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

More workers are useful only if they produce mathematical evidence that can be combined, or finish equally sound work at a lower acceptable cost. The surface uniqueness proof offers a concrete comparison: source application and descent checking are distinct obligations, while many steps inside each are tightly dependent.

## 1. Start with a sequential baseline

Use the [central workshop's target and source packet](/posts/2026/08/agent-system/birational-proof-workshop/). Ask one session to prove the theorem and preserve its complete attempt. Record source access, retries, actual usage where available, and mathematical hints supplied by the researcher.

If it already succeeds cheaply, extra workers may add only overhead. If it fails, identify the gap before deciding how to divide the work. A generic team of “researcher, expert, critic” does not explain which missing mathematics anyone is responsible for.

## 2. Divide distinct obligations

One task can inspect the two signed applications of negativity. Another can develop the descent implication from equality of exceptional errors with positive support. The second task must state that equality as an explicit input, not pretend to have established it.

| Task | Inputs | Required output |
|---|---|---|
| Comparison | W, p, q, compatible canonical identities, two nefness assumptions, exact negativity lemma | Both inequalities with sign, base, and pushforward calculations |
| Return implication | Equality of error divisors and positive exceptional support | Descent through point blowups, the inverse morphism, and identity checks |
| Merge | The two complete arguments under matching hypotheses | One proof of the original specified map extending to an isomorphism |

The comparison result satisfies a premise of the return argument. That relationship is the mathematical reason they can be combined. The handoff must preserve the same morphisms and canonical conventions; two similarly named surfaces are not enough.

## 3. Work through a genuine conflict

Suppose the comparison report proves $D\geq0$ over X but the summary says $D\leq0$. A descent report assumes D=0. These reports do not combine into a proof.

The merge should retain the valid first inequality, correct the summary, and request the missing symmetric application over Y. It should not average confidence or count two positive verdicts. Once the reverse inequality is justified, the existing conditional descent argument may become applicable without being regenerated.

Now suppose the descent task requires equality of actual error divisors, while the comparison task reports only numerical equivalence. That is a different mismatch. The merge must either strengthen the comparison or prove that the weaker input suffices. It cannot silently substitute one for the other.

## 4. Test a delayed result after revision

While the tasks run, remove nefness of $K_X$. The old comparison report may still be a correct proof under the old hypotheses. Its reverse inequality no longer applies to the revised target, while the first inequality may survive.

A delayed report should therefore retain its original scope. Reapply its useful components explicitly to the new task. The blowup counterexample then refutes the weakened theorem. Changing the version label on an old result does not perform that mathematical check.

This is where a shared state can help coordination: it makes the current hypotheses and unresolved obligations visible. It cannot enforce correct reasoning by itself.

## 5. Independent work is not automatically independent evidence

Two conversations can invoke the same wrong theorem or inherit the same omitted assumption. A second vote adds little if neither supplies the missing calculation. Diverse evidence can help: one task checks the negativity route, another reconstructs the last-blowup proof, and a reviewer examines where their assumptions overlap.

But fully developing two routes costs more. Use that extra work when it addresses a concrete uncertainty or supports a planned extension, not as a ritual. A source audit and a descent proof may be a more economical division for this task.

[Danus v2](https://arxiv.org/abs/2607.06447v2) reports planning, parallel workers, and fact-graph memory. That description motivates a design question; it does not establish that our particular split outperforms the sequential baseline. The surface mathematics is supported by the sources in the central workshop.

## 6. Compare total effort and elapsed time

Give both configurations identical authorized sources and comparable total allowances. Parallel work can reduce elapsed time while increasing tokens, source lookups, and reconciliation work. Report those dimensions separately rather than collapsing them into “more efficient.”

Count every worker, retries, failed routes, merge corrections, and human hints. If usage is unavailable, report observable time and action counts without inventing token savings. Use repeated matched runs before making a general performance claim; one pair is a case study.

**Exercises:** merge a valid first inequality with a conditional descent report; resolve an actual-divisor versus numerical-equivalence mismatch; process a delayed two-nef report after the hypothesis change. In each case, supply the missing proof step or preserve its open status.

**Deliverable:** the sequential attempt, divided attempts, actual merge, resulting proof, and resource comparison. Choosing one worker is a successful design decision when the extra division does not help.

[Next: evaluate the system](/posts/2026/08/agent-system/evaluation-monitoring/) · [Course roadmap](/posts/2026/12/Agent-System/)
