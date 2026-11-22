---
title: "Advanced Project: Audit a Birational Reduction in Codex"
permalink: /posts/2026/08/agent-system/birational-geometry-agent/
tags:
  - Agent System
  - Mathematics
  - Birational Geometry
classes: agent-system-page
full_page_reading: true
---

The aim is to test whether a geometric construction actually advances the original target. Start with a known reduction and a reference argument. Only then ask whether it survives changed hypotheses. 'Spiraling induction' is not an extra proof principle: any induction still needs explicit statements, bases, and a well-founded dependency order.

**Reading route:** start with the workshop below for the advanced design; use [First task: a blow-up and the return to the original surface](#first-task-a-blow-up-and-the-return-to-the-original-surface) as a concrete calibration when needed. Complete the research assignment after the control example.

## Research workshop C: transport theorems across models and induction stages

**Entry requirements:** divisors, line bundles, intersection theory on smooth projective surfaces, and the core course's dependency records. **Deliverable:** a theorem package with an explicit model-change argument, its admissible scope, and an induction schedule whose rank decreases at every recursive invocation. The negative blow-up control later in the chapter is only the starting test.

### 1. One modification can destroy one property and preserve another

Let $\pi:Y\to X$ be the blow-up of a point on a smooth projective surface over an algebraically closed field, with exceptional curve $E$. The later calculation shows that $K_Y\cdot E=-1$, so nefness of $K_X$ does not transfer to $K_Y$. Yet the spaces of pluricanonical sections are preserved:

$$
H^0(X,mK_X)\cong H^0(Y,mK_Y)
\quad(m\geq1).
$$

The contrast forces a useful architectural distinction. A model change is not labeled simply “safe” or “unsafe.” It has a transfer rule for a specified object and property. Section spaces and nefness require different arguments.

### 2. Derive the positive transfer

Use compatible canonical divisors, so $K_Y=\pi^*K_X+E$. For $j\geq1$, consider

$$
\begin{gathered}
0\to\mathcal O_Y((j-1)E)\to\mathcal O_Y(jE)
\\ \to\mathcal O_E(-j)\to0.
\end{gathered}
$$

Here $E\cong\mathbb P^1$ and $\mathcal O_E(E)\cong\mathcal O_{\mathbb P^1}(-1)$. The last sheaf has no global sections. Since $E$ maps to a point, its direct image under $\pi$ is zero. Left exactness of direct image therefore gives

$$
\pi_{\ast}\mathcal O_Y((j-1)E)
\cong\pi_{\ast}\mathcal O_Y(jE).
$$

Together with $\pi_{\ast}\mathcal O_Y=\mathcal O_X$ for a proper birational morphism to the smooth, hence normal, surface $X$, induction gives $\pi_{\ast}\mathcal O_Y(mE)=\mathcal O_X$. The projection formula now yields

$$
\begin{gathered}
\pi_{\ast}\mathcal O_Y(mK_Y)\\
\cong\mathcal O_X(mK_X)\otimes\pi_{\ast}\mathcal O_Y(mE)\\
\cong\mathcal O_X(mK_X).
\end{gathered}
$$

Taking global sections proves the claimed isomorphism. Notice what was not needed: vanishing of all higher direct images. Introducing that stronger obligation would complicate the proof without serving this target.

This calculation specializes the exceptional-divisor pushforward mechanism discussed in §1.2 of [Kollár's 2017 draft, *Families of varieties of general type*](https://web.math.princeton.edu/~kollar/book/modbook20170720). The surface argument above exposes the particular ingredients a source audit must check. It does not assert a transfer theorem for arbitrary singular spaces or analytic modifications.

### 3. Package the result with its interface

| Component | Required content |
|---|---|
| Input objects | Smooth projective surfaces, point blow-up, exceptional curve, integer $m\geq1$ |
| Imported facts | Canonical-divisor identity, normal-target pushforward, projection formula, negative-degree section vanishing on $E$ |
| Output | An isomorphism of the specified global section spaces |
| Forbidden inference | Nefness of $K_Y$, or a family-level base-change statement |
| Revision trigger | Change of singularities, category, center, coefficient type, or relative setting |

The last row is especially important for mathematical research. Fiberwise equality of dimensions does not alone prove a sheaf isomorphism over a parameter space. Nor does a calculation for line bundles automatically handle a non-Cartier canonical divisor. Those proposed extensions need new statement versions and new bridge lemmas.

### 4. Make a spiraling induction genuinely well founded

Suppose a theorem package contains statements $A_{d,q}$ and $B_{d,q}$, where $d,q$ are nonnegative integers. One proposed dependency is: $A_{d,q}$ uses $B_{d,q-1}$ when $q>0$ and specified lower-dimensional results; $B_{d,q}$ then uses $A_{d,q}$. At $q=0$, replace the unavailable predecessor by an explicit boundary argument.

Assign lexicographic ranks

$$
\rho(A_{d,q})=(d,q,0),\qquad
\rho(B_{d,q})=(d,q,1).
$$

Each stated predecessor has smaller rank: the lower-dimensional step lowers $d$, the predecessor $B_{d,q-1}$ lowers $q$, and $A_{d,q}$ precedes $B_{d,q}$ within the same pair. Provide the $d=0$ boundary proofs and all $q=0$ transitions. This establishes a well-founded *dependency plan*, provided every implication is separately proved.

An invocation of $B_{d,q}$ inside the proof of $A_{d,q}$ violates this order and creates a cycle. Reducing some informal “complexity” is not enough unless its values and decrease are defined. For an actual MMP proof, the ranks must match the parameters in the source; the two-index rehearsal is not a claim about a named theorem.

[![Geometric theorem packages track objects, transfer lemmas, and well-founded theorem invocations separately.](/images/agent-system/advanced-geometry.svg)](/images/agent-system/advanced-geometry.svg)

### 5. A research-level Codex assignment

Create one object record per model and one transfer record per claimed property. Reproduce both the negative nefness calculation and the positive pluricanonical calculation. Then choose an actual induction theorem from accessible literature and supply the relevant proof passages.

Require Codex to extract every theorem invocation into a row containing the caller, callee, full hypotheses, parameter substitution, and rank comparison. For a same-rank auxiliary result, give an independent earlier proof or mark the invocation unresolved. Finally change one hypothesis and attempt the first transfer or induction step that breaks.

The submission must contain mathematical proofs and the actual invocation audit. A diagram with decreasing labels does not prove the corresponding implications. A successful local transfer does not establish the whole theorem package.

## First task: a blow-up and the return to the original surface

Let X be a smooth projective surface over an algebraically closed field and let π:Y→X be the blow-up of a smooth point, with exceptional curve E. The canonical divisor formula is

$$K_Y=\pi^*K_X+E.$$

Using E²=-1 and π* K_X · E=0 gives K_Y · E=-1. Thus even if K_X is nef, K_Y is not nef. For a concrete instance choose X an abelian surface, whose canonical bundle is trivial.

This is a useful control: moving to a smooth birational model does not preserve every positivity condition. A system that stores only 'birationally equivalent' loses information essential to the argument.

The displayed calculation is a reference argument, not an automated research result. Students must justify the blow-up formula and intersection identities from a source or a proof they can inspect.

## Unpack the calculation before designing the workflow

This is an advanced module. It assumes basic divisors and intersection numbers on smooth projective surfaces. Its system-design lesson is accessible without reconstructing surface theory: **a property of a pulled-back object is not automatically a property of another object on the same model.**

On a projective surface, a divisor is nef when its intersection with every integral curve is nonnegative. To disprove nefness, one curve with negative intersection is enough. The exceptional curve $E$ is therefore a decisive test, not an arbitrary example chosen after the conclusion.

There are three divisors that the record must distinguish:

| Divisor | Space | Role |
|---|---|---|
| $K_X$ | Original surface $X$ | Object in the original positivity hypothesis |
| $\pi^*K_X$ | Blown-up surface $Y$ | Pullback of that object |
| $K_Y$ | Blown-up surface $Y$ | Canonical divisor of the new surface |

The last two live on the same surface but differ by $E$. Using the supplied canonical-divisor identity, bilinearity of intersection gives

$$
\begin{aligned}
K_Y\cdot E
&=(\pi^*K_X+E)\cdot E\\
&=(\pi^*K_X)\cdot E+E^2\\
&=0-1=-1.
\end{aligned}
$$

The pullback term has intersection zero because $E$ is contracted to a point: the projection formula pairs $K_X$ with the zero pushforward curve class. The other input, $E^2=-1$, is the exceptional-curve identity for this blow-up. A complete source reconstruction must justify these inputs and the canonical-divisor formula; the arithmetic after them is not a substitute for that audit.

If $X$ is an abelian surface, its trivial canonical bundle makes $K_X$ nef. Yet the calculation proves that $K_Y$ is not nef. The contradicted implication is specifically “nef canonical divisor remains nef after this blow-up.” Neither the smoothness of $Y$ nor the original nefness on $X$ has been disproved.

### A useful repair has a different statement

The identity gives $K_Y-E=\pi^*K_X$. That correction removes the offending exceptional term. It does not prove nefness of $K_Y$. A report that changes the object to $K_Y-E$ must label the new claim rather than announcing that the original target was repaired.

For the laboratory, require a four-line review: the exact false implication, the curve testing it, the computation giving the contradiction, and the corrected object identity that survives. Then remove the exceptional term from the submitted formula and ask the reviewer to identify the missing input. This checks whether the system understands the object change rather than memorizing the answer “blow-ups are bad.”

For a checkable source for the three blow-up identities, see Proposition 7.6, items (3)–(5), in [Sam Frengley’s algebraic-surfaces course notes](https://samfrengley.github.io/teaching/DRAFT-notes/alg-surfaces-notes.html). Match the smooth-surface and point-blow-up hypotheses before using them.

## Build from an empty Codex folder

```text
Create OBJECTS.md, TARGET.md, REDUCTIONS.md, SOURCES.md, and REVIEW.md.
Record X, Y, π, E, their assumptions, and the direction of each map.
Record divisor identities on the space where they hold.
Audit the claim: nefness of K_X implies nefness of K_Y.
Check every identity used in the intersection calculation.
Do not silently replace pullback of K_X by K_Y.
Preserve the original false claim and the corrected conclusion separately.
```

The architecture is the record of objects, the proposed implication, its evidence, and a review of that exact implication. No additional agent roles are needed to do this first experiment.

## What a successful run must show

It must identify the exceptional correction E, compute the negative intersection, and reject the proposed preservation of nefness. It must not conclude that the original X has non-nef canonical divisor. It should explain which assertion was refuted and which original hypotheses remain unchanged.

Introduce two damaged variants: omit E from the canonical divisor formula, or apply an intersection statement on Y as though it were on X. Require the review to locate the exact error, rather than simply output 'incorrect'.

## Second task: audit an actual induction package

Choose a specific theorem and proof from your own literature. Supply the relevant statement and proof passages. Do not ask Codex to reconstruct a major theorem from its name alone.

```text
Create INDUCTION.md from this source proof.
For every statement record its complete hypotheses and parameter values.
For every invocation record all premises needed together.
Specify the base cases and the order that makes dependencies well-founded.
Separate same-dimension auxiliary steps from lower-dimensional invocations.
If a parameter does not decrease, identify the earlier established statement
that permits this step. Flag any circular dependency without repairing it silently.
```

For a purely logical rehearsal, use A_n depending on B_(n-1), and B_n depending on A_n, with B_0 supplied. Order the obligations as B_0, A_1, B_1, A_2, B_2, and so on. This is a valid dependency pattern only when each implication has its own proof. Removing B_0 leaves the construction ungrounded. This rehearsal is not a theorem in birational geometry.

## Attempt a research extension only after reconstruction

Change exactly one hypothesis in the chosen geometric argument. Locate its actual use. Ask whether the failed step has a replacement and attempt that replacement. Keep the original and proposed statements side by side. A successful calculation on a divisor, fiber, or model must still have a justified implication back to the original target.

Submit the source reconstruction, object and dependency records, the changed hypothesis, the attempted replacement lemma, and a precise account of what remains open. A negative result about the proposed route can be valuable. A diagram of unproved arrows is not a proof blueprint ready for reuse.

[Method-selection laboratory](/posts/2026/08/agent-system/proof-sketch-system/) · [Course roadmap](/posts/2026/12/Agent-System/)

