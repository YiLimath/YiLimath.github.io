---
title: "Module 1. Represent the mathematics"
permalink: /posts/2026/08/agent-system/foundations/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

An agent can produce several correct pages on a common resolution and still fail to prove that the original surfaces are isomorphic. The first design problem is therefore mathematical: represent the target and its outstanding obligations well enough that the next action addresses what is actually missing.

This module uses the [minimal-surface uniqueness problem](/posts/2026/08/agent-system/birational-proof-workshop/). Its aim is to help you recover a stalled proof without restarting the entire investigation. The proposed workflow has a cost; its benefit must be measured against a direct attempt with the same agent and sources.

## 1. Begin with the theorem you actually want

Let X and Y be smooth projective surfaces over an algebraically closed field of characteristic zero. Assume that $K_X$ and $K_Y$ are nef. Given a birational map $\phi:X\dashrightarrow Y$, prove that it extends to an isomorphism.

The first thing to keep in mind is that conversation history is not a mathematical state. A conversation may preserve every sentence while confusing this target with a statement about divisors on a third surface. A useful record lets a new reader answer four questions: **What is the exact task? What supports each current conclusion? Which assumptions remain? What would need reconsideration if an input changed?**

Here “given” matters: the required morphism must induce the specified map on the common dense open set. “Isomorphism” matters too: obtaining a rational map, a morphism in one direction, or an equality of canonical pullbacks is only part of the argument.

Write the target once, with the field, category, positivity assumptions, and requested map. Do not make the agent infer these from earlier messages. This is not additional mathematics; it is a way to stop the research process from silently substituting a nearby theorem.

## 2. Diagnose a plausible but incomplete proof

Suppose an agent returns the following sketch:

> Choose a common resolution p: W → X and q: W → Y. Compare the canonical divisors. Negativity implies equality of the exceptional errors. Hence X and Y are isomorphic.

This is a useful plan, but two phrases conceal mathematical work: “negativity implies” and “hence.” Do not reject the whole response or accept the whole response. Separate its claims.

| Claim | Evidence needed | What it does not yet give |
|---|---|---|
| A smooth common resolution exists | A resolution/factorization result in the stated category | A comparison of canonical divisors |
| Canonical divisors have effective exceptional errors | Compatible canonical choices and the blowup formula | Equality of the errors |
| The errors agree | Two correctly signed negativity applications | A descended morphism on X |
| The same curves are contracted | Positive coefficients on the full exceptional supports | Descent without a factorization argument |
| The original map extends to an isomorphism | Descent in both directions and inverse identities | Nothing further for this target |

The representation earns its place if it turns “try harder to prove uniqueness” into a bounded task such as “prove that q factors through the last point blowup of p.” The latter can be searched for, proved, and checked without regenerating the earlier comparison.

## 3. A worked state: what has actually been established?

Choose canonical divisors using the same rational two-form. On a common resolution write

$$
K_W=p^{\ast}K_X+E_p=q^{\ast}K_Y+E_q,
$$

where the error divisors are effective and supported on the respective exceptional curves. Set

$$
D=p^{\ast}K_X-q^{\ast}K_Y=E_q-E_p.
$$

For a p-contracted curve C, we have $(-D)\cdot C=q^{\ast}K_Y\cdot C\geq0$. Thus $-D$ is p-nef. Also $p_{\ast}D=p_{\ast}E_q\geq0$. Birkar's negativity lemma gives $D\geq0$.

At this exact point, the state is **not** “canonical pullbacks agree.” It is one inequality. The opposite inequality needs the symmetric application over Y, using nefness of $K_X$. Once both are proved, D=0 and the two error divisors agree. Their strictly positive exceptional coefficients then identify the contracted curves.

The source is [Birkar, *Lectures on Birational Geometry*, Lemma 4.15, p. 21](https://arxiv.org/pdf/1210.2670v1#page=21). The full geometric argument, including the coefficient and descent steps, is supplied in the central workshop. Here we use it to show how an intermediate result should be represented.

A compact record after the first application could be:

```text
Target: the given birational map X ⇢ Y extends to an isomorphism.
Context: smooth projective surfaces, characteristic zero; K_X and K_Y nef.
Established: common resolution; compatible canonical identities;
             -D is p-nef; p_{\ast}D is effective; therefore D >= 0.
Evidence: actual calculations and Birkar Lemma 4.15 application.
Open: reverse inequality; equality of exceptional supports; descent;
      inverse identities on X and Y.
Next action: prove D is q-nef and q_{\ast}(-D) is effective.
```

A record saying only “negativity checked” would lose the sign and the morphism. A record saying “uniqueness proved” would lose several open implications. Neither error is fixed by a longer transcript.

## 4. Separate a statement from its support

A statement can have several arguments; an argument can have several joint prerequisites. Store the dependencies of the argument, rather than attaching a single unexplained “verified” flag to the conclusion.

For the first inequality, all of the following are needed together: the defined divisor D, the correct projective birational morphism p, relative nefness of -D, and effectivity of its pushforward. A citation alone supplies none of the last two calculations. The second inequality is a different application, with a different sign and base.

This distinction has a logical foundation in Lean's [*Propositions and Proofs*](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/). Our Markdown record is informal; it does not turn these claims into kernel-checked theorems.

For this project, one note can contain the target, complete argument, inspected source locations, review findings, and next action. Separate files are useful only when they reduce confusion or repeated work. Five documents with no checked inference are not better than one well-written proof.

## 5. Revise a hypothesis without throwing away the proof

Now remove nefness of $K_X$ while retaining nefness of $K_Y$. What survives?

The common resolution and canonical identities survive. The first inequality also survives: it used nefness of $K_Y$. The reverse inequality no longer has its previous justification. Therefore the original conclusion must be reopened, while the surviving argument should remain available.

This is not just a bookkeeping example. Blow up a smooth projective abelian surface Y at a point, obtaining $q:X\to Y$ with exceptional curve E. Then $K_Y=0$, while $K_X=E$ and $K_X\cdot E=-1$. The blowdown is birational and not an isomorphism. Taking W=X and p the identity gives D=E: the first inequality is true, the reverse is false.

A useful record distinguishes three outcomes: the source theorem is still valid; one application survives; the weakened uniqueness statement is false. “The old proof failed” alone would establish only the second application's loss of support, not the counterexample.

## 6. Turn representation into a useful intervention

First ask your agent to prove the original theorem using the source packet, without providing the worked answer. Preserve the initial output. If it already gives a complete proof, this problem has not shown a capability advantage for the new representation.

If the output is incomplete, ask for a state record containing only the established conclusions, the evidence for each, and the earliest unresolved implication. Then continue from that implication. Do not automatically restart the proof or introduce several workers.

```text
Keep the surface uniqueness target and hypotheses fixed.
Read the existing attempt. Separate proved intermediate claims
from proposed steps. For each use of negativity, retain its sign,
morphism, relative-nefness calculation and pushforward calculation.
Name the first unresolved implication and work on that implication.
Do not report completion before constructing the descended isomorphism.
```

The desired improvement is concrete: a stalled proof acquires its missing argument, or an already solvable proof is completed with less repeated search and correction. Count the cost of creating the record, supplying hints, and checking the repair. This is a proposed intervention, not a claimed measured result.

## 7. Exercises that change the mathematical state

**A. Separate intermediate conclusions.** Starting with the first inequality $D\geq0$, state exactly what the symmetric application must establish. Write the required signed divisor and pushforward. A successful answer obtains the opposite inequality without assuming that the exceptional loci already agree.

**B. Recover the missing final step.** Given equality of exceptional supports, identify the theorem that makes q descend through one blowup in p. Use [Stacks Tag 0C5J](https://stacks.math.columbia.edu/tag/0C5J), and explain how to repeat the step. Merely citing the tag without checking that q contracts the exceptional curve is incomplete.

**C. Change the context.** Replace absolute nefness by relative nefness over a common base S. Before reusing the inequality, explain why the image of a p-contracted curve under q is either a point or a curve contracted over S. The new record must retain commutativity over the base.

**D. Test recovery cost.** Start a fresh session with your mathematical note and the same permitted sources, but without the conversation. Ask it to continue the unresolved descent step. Record whether it redoes earlier work, imports an unstated premise, or correctly resumes. Saving a file alone is not success.

Proof checkpoints for these tasks are in the central workshop. Keep them out of a session intended to measure an unaided attempt.

## 8. What to submit and what to measure

Submit the direct attempt, the minimal state record, the continued argument, and an account of remaining gaps. Compare the same acceptance criterion in both runs: all implications needed for the given isomorphism must be justified.

Report either a capability gain—a gap left by the baseline is closed—or the resources used to reach equal proof quality. Include actual token use when available, elapsed time, source inspections, retries, and mathematical help supplied by the researcher. Do not infer token savings from a shorter final answer. For an unfamiliar real problem, a substantive proved lemma can be progress even when the main target remains open.

This module teaches a representation only insofar as it helps complete or resume mathematics. If the extra record adds work without changing the outcome, simplify it. In the next module, the same state is used to choose between competing proof routes.

[Next: plan and search](/posts/2026/08/agent-system/plan-and-execute/) · [Course roadmap](/posts/2026/12/Agent-System/)
