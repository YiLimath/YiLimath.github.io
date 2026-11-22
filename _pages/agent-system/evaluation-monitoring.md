---
title: "Module 9. Evaluate the mathematics and the workflow separately"
permalink: /posts/2026/08/agent-system/evaluation-monitoring/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

The course has two practical success criteria: help an agent complete mathematical work its direct attempt could not complete, or obtain an equally justified result with substantially less measured work. This module defines a comparison that can support those claims without confusing a polished answer with a proof.

## 1. Fix the mathematical acceptance criterion first

Use the [surface uniqueness workshop](/posts/2026/08/agent-system/birational-proof-workshop/) as a controlled starting task. Its reference proof depends on [Birkar Lemma 4.15](https://arxiv.org/pdf/1210.2670v1#page=21) and the factorization and descent results listed there. This is established mathematics, not a discovery benchmark.

Require a proof of the specified map extending to an isomorphism. Check common resolution, compatible canonical identities, the signed comparison or a valid alternative, and the final return to X and Y. A correct theorem statement with an incomplete proof does not meet the same standard as a complete argument.

A valid different proof should pass. Do not grade by whether the response matches the reference wording or uses the preferred architecture.

## 2. Prepare geometric controls

| Input | Reference outcome | What must be inspected |
|---|---|---|
| Smooth projective surfaces, both canonical divisors nef | The specified birational map extends to an isomorphism | All proof obligations, including descent |
| Only $K_Y$ assumed nef | General uniqueness claim is false | Blowup of an abelian surface gives the counterexample |
| Canonical divisors relatively nef over a common base S | The same conclusion over S under the workshop's assumptions | Curve images lie in fibers and the resolution commutes over S |
| First signed comparison supplied, second absent | Partial progress only for that route | No premature equality or completion |
| Equality of numerical classes supplied in place of actual error divisors | Original support argument needs further justification | The precise weaker input, not an automatic false verdict |

Withhold the reference solutions from runs intended to measure independent solving. If the student has studied the worked proof, use an unfamiliar task for a transfer assessment and disclose that training exposure.

## 3. Compare interventions fairly

A direct request and a structured workflow should have the same model, tools, source access, and declared total allowance. A better result after supplying the crucial proof is assisted solving, not evidence that file organization improved reasoning.

Record assistance in distinct forms: a source locator, diagnosis of a gap, a suggested method, or the decisive argument itself. These interventions can all be educationally useful, but they support different explanations of the result.

Change one mechanism at a time where practical. For example, test signed source-application records before also adding separate reviewers and persistent memory. If several mechanisms change together, attribute the result to the combined workflow rather than pretending to isolate a cause.

## 4. Assess capability and cost separately

For capability, retain the baseline's precise unresolved or invalid inference and the assisted run's replacement argument. Explain why the latter closes the actual target obligation. If both runs fail, clearer diagnosis can be useful partial progress but is not a solved theorem.

For cost, first establish comparable proof quality. Then record total tokens where available, elapsed time, repeated source inspections, retries, and researcher correction. Include setup and discarded branches. Report one-time preparation separately from per-problem work if reuse is the intended benefit.

A shorter final answer can conceal a much larger search. Faster parallel completion can consume more total tokens. Neither observation alone establishes overall resource savings.

## 5. Evaluate revisions and recovery

After a completed two-nef proof, remove nefness of $K_X$. Check whether the workflow retains the first inequality, reopens the reverse application, and recognizes the blowup counterexample. Then supply the relative-nef variant: it should check the new base conditions rather than reuse a blanket negative verdict about weakened assumptions.

For recovery, restart from saved mathematical evidence. Measure reconstruction fidelity and repeated work. A checkpoint that causes the agent to restore a deleted assumption has failed even if it saves context tokens.

These are concrete failure probes. Their outcomes must be recorded from actual runs; the reference expectations are not experimental results.

## 6. When the target is genuinely open

For an open birational problem, there may be no known final verdict. Assess intermediate mathematics: a valid application of an existing theorem, a proved special case, an explicit obstruction to a proposed route, or a precise reduction accompanied by an attempted missing lemma.

Distinguish obstruction to a method from refutation of the target. Lack of an applicable analytic negativity citation does not by itself disprove an analytic conclusion. An actual counterexample must satisfy the proposed hypotheses and violate the conclusion.

Novelty is also separate from correctness. A proof of a known consequence can be a successful learning outcome without being a new research result. Literature-search failure is not evidence of novelty.

## 7. Final project

Choose a proof or proposed extension from your birational research. Start with a direct-agent attempt and preserve the output. Identify one observed failure that the course's methods can plausibly address. Introduce the smallest relevant intervention, attempt the decisive lemma, and check the resulting mathematics.

The final report should include the exact target, inspected sources, baseline, intervention, complete new argument or localized remaining gap, actual assistance, and measured resources. Use an unseen variant to assess transfer when feasible.

A new theorem is welcome but not a universal grading requirement. A substantial partial result or decisive obstruction can pass. A workflow diagram with no attempted mathematical bridge cannot.

## 8. Report only what the evidence supports

A single successful comparison is evidence for that episode. Repeated runs are needed to understand variability; broader claims need a task set that represents the intended research use. Do not assign success probabilities or dramatic savings without data.

Formal admission should be evaluated separately from proof discovery. The [Lean validation guide](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) explains why the encoded statement, dependencies, and checking environment matter. A checked auxiliary declaration is not formal verification of the entire geometric proof.

The comparison procedure here is a course proposal. No collected performance results are supplied by this page. Its purpose is to make it possible to demonstrate—or reject—the practical value of a design on real mathematics.

[Course roadmap](/posts/2026/12/Agent-System/) · [Central proof project](/posts/2026/08/agent-system/birational-proof-workshop/)
