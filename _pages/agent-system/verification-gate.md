---
title: "Module 5. Decide what evidence permits reuse"
permalink: /posts/2026/08/agent-system/verification-gate/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

Review should change a mathematical decision: preserve a valid argument, locate the inference blocking completion, or reject an unsupported conclusion. We use the surface uniqueness proof to make those outcomes inspectable. An approval label alone adds no proof.

## 1. Freeze the actual statement and attempt

Give the reviewer the surface assumptions, the specified birational map, the common resolution and canonical conventions, the complete candidate argument, and its sources. Preserve that exact version. Otherwise a report may approve an argument under assumptions different from those of the current task.

The [central workshop](/posts/2026/08/agent-system/birational-proof-workshop/) is the reference proof, not evidence that an agent has solved it. Keep it out of a session intended to measure independent solving.

## 2. Review a wrong-sign application

Suppose a candidate defines $D=p^{\ast}K_X-q^{\ast}K_Y$ and proves that -D is p-nef and that $p_{\ast}D$ is effective. It then concludes $D\leq0$.

The computations can be correct while the conclusion has the wrong sign. [Birkar Lemma 4.15](https://arxiv.org/pdf/1210.2670v1#page=21), applied with its divisor B equal to D, gives $D\geq0$. Preserve the computations; repair the inference. The opposite inequality requires the separate application with B=-D over Y.

A useful report names the first invalid inference, states the justified conclusion, and identifies the additional work needed. “Negativity was used incorrectly” is too vague to guide repair. Rejecting the entire proof discards valid work unnecessarily.

## 3. Review a hidden circular assumption

A candidate tries to prove D is p-exceptional by asserting that p and q have the same exceptional loci, then uses negativity to conclude those loci agree. This imports the desired relationship as a premise.

The repair is to use the version of negativity requiring an effective pushforward. Compute $p_{\ast}D=p_{\ast}E_q\geq0$ without assuming the loci agree. The reviewer has not merely detected circularity; it has identified a legitimate route around the unnecessary premise.

If the reviewer proposes this repair, record that mathematical assistance. A run rescued by a supplied decisive argument should not be described as unaided discovery.

## 4. Review the final return

Even after $E_p=E_q$ is proved, the target is unfinished unless descent is justified. Check positive support, the point-blowup factorization, and [Tag 0C5J](https://stacks.math.columbia.edu/tag/0C5J) at each contraction. Then check the inverse identities.

The report should distinguish “this step is missing” from “the conclusion is false.” For the original surface target the gap is repairable. When nefness of one canonical divisor is deleted, a blowup of an abelian surface refutes the weakened theorem. Those are different mathematical outcomes.

## 5. Admission preserves assumptions

A proof conditional on a descent lemma remains conditional until that lemma is established or validly imported. Saving it in a theorem file does not discharge the assumption. If a source application is invalidated, withdraw that route's support while retaining unaffected calculations and alternative proofs.

| Finding | Permitted conclusion |
|---|---|
| Both signed applications and descent justified | The specified isomorphism target is established informally |
| Comparison complete, descent not supplied | Intermediate divisor equality established; target open in this argument |
| Nefness of $K_X$ removed | First inequality may survive; reverse application needs reconsideration |
| A counterexample satisfies the weakened hypotheses | That weakened statement is false |
| A process times out | No mathematical verdict from the timeout |

## 6. Mechanical validation has a different role

A Lean proof is evidence for its encoded declaration under its definitions and dependencies. It does not automatically establish that the declaration expresses this surface theorem. The official [validation guide](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) distinguishes proof validity from intended meaning and describes dependency and environment checks.

An abstract formal proof that opposite coefficient inequalities imply equality verifies that component only. It does not certify the source applications or descent. Conversely, a second model's informal approval is not a kernel certificate. Future automated admission should rely on the appropriate checked evidence rather than permanently requiring a human to reread every proof step.

## 7. Evaluate the review on actual faults

Use one complete candidate and variants containing a wrong sign, an assumed equality of exceptional loci, or omitted descent. Keep these as teaching fixtures, not invented historical agent failures. Ask the reviewer to localize each issue and preserve the correct parts.

Then test the repaired argument on the relative-nef variant. The reviewer must check the common base and contracted image curves rather than accept the previous verdict unchanged.

Measure both invalid acceptance and unnecessary rejection of valid work. Count repairs, rereading, and researcher-supplied mathematics. A reviewer that blocks every result is not useful, and a reviewer that approves every fluent proof is not reliable.

**Submit:** the exact attempts, localized findings, repaired steps, and scoped conclusions. The valuable outcome is a proof completed or corrected at an acceptable cost. The informal review protocol remains a proposal until its behavior is observed.

[Next: formalization](/posts/2026/08/agent-system/lean-formalization/) · [Course roadmap](/posts/2026/12/Agent-System/)
