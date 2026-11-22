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

