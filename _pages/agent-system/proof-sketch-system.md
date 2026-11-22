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

A useful method recommendation ends with an attempted mathematical argument. This project asks Codex to compare routes, identify their decisive obligations, and work on one of those obligations. No orchestration software is required.

## First understand the method-selection problem without geometry

Module 1 used one input $c$ to produce $(c,c)$. Here is a harder control with two unknowns and three output conditions. Let

$$
A(x,y)=(x+y,\ x-y,\ 2x).
$$

For a specified output $(a,b,c)$, determine whether an input exists. “Find a method” is not the deliverable: we need an applicable method and a calculation that settles this output.

### Route 1: solve for the input, then check the unused condition

The first two equations give $x=(a+b)/2$ and $y=(a-b)/2$. Substitute these values into the third equation. Its left side becomes $2x=a+b$, so the third requirement holds exactly when $c=a+b$.

This proves both necessity and sufficiency:

$$
(a,b,c)\text{ is obtainable}\quad\Longleftrightarrow\quad c=a+b.
$$

Necessity alone would reject incompatible outputs but would not construct a solution for compatible ones. Sufficiency is supplied by the explicit formulas for $x$ and $y$, with all three equations checked.

### Route 2: identify an obstruction before solving

Every output of $A$ satisfies “third entry equals first plus second,” since $(x+y)+(x-y)=2x$. Define the obstruction of a proposed output to be

$$
o(a,b,c)=c-a-b.
$$

If this number is nonzero, the output is impossible and there is no reason to search for inputs. If it is zero, the formulas from Route 1 establish that this is the only obstruction. The obstruction test is exact because we proved that converse; defining a quantity that must vanish would not alone prove completeness of the test.

For $(3,1,4)$ the obstruction is zero. The input $(2,1)$ works, as direct substitution gives $(3,1,4)$. For $(3,1,5)$ the obstruction is one, so no input works. Reusing $(2,1)$ after changing the final entry would solve the old task, not the new one.

### What the two method cards should contain

| Method | Decisive work | Best reason to choose it | What it cannot skip |
|---|---|---|---|
| Construct a candidate | Solve the first two equations | A concrete witness is needed | Check the third equation |
| Test compatibility | Evaluate $c-a-b$ | Many proposed outputs need quick rejection | Prove zero obstruction is sufficient before claiming an exact criterion |

The routes share mathematics. Do not advertise them as statistically independent evidence. Their value is that they expose different failure points and can be chosen for different immediate tasks.

Ask Codex to create the four files below using this example first. Give it $(3,1,4)$, then revise only the third entry to five. Require it to preserve the old witness, recompute its output, and distinguish candidate failure from a proof of impossibility. These are reference outcomes, not a record of a measured Codex run.

### From this calculation to the geometric project

In the next task, a global section plays the role of an input, restriction plays the role of $A$, and the specified section plays the role of $(a,b,c)$. A connecting homomorphism supplies the obstruction. The advanced work is proving that this machinery applies to the given geometric objects; the logical structure is the one just derived.

**Prerequisites for the geometric extension:** line bundles, effective Cartier divisors, and the cohomology sequence of a short exact sequence. If those are unfamiliar, complete the linear example and use Modules 3–5 to design and review its method cards.

## The controlled mathematical task

Let X be a projective variety, L a line bundle, D an effective Cartier divisor, and s a specified section of L restricted to D. Determine whether this particular s lifts to a global section of L. Work from the exact sequence

$$0\to L(-D)\to L\to L|_D\to0.$$

The connecting map gives the exact criterion: s lifts if and only if its image under the connecting homomorphism is zero. Vanishing of the entire group H¹(X,L(-D)) is sufficient but need not be necessary for this chosen section.

There are therefore two genuinely different routes: prove a sufficient vanishing theorem, or compute the obstruction for s. Recommending vanishing without checking its hypotheses is not a method selection success.

## Build the workspace in Codex

```text
Create TARGET.md, METHODS.md, ATTEMPTS.md, and REVIEW.md.
Record X, L, D, and the specified section s exactly.
Compare two routes: sufficient cohomology vanishing and direct obstruction.
For each route list prerequisites, applicable source results, and missing steps.
Do not change 'this section lifts' into 'some section lifts'.
Choose one decisive mathematical calculation and carry it out in ATTEMPTS.md.
Keep failed attempts and distinguish supplied facts from checked arguments.
```

This small architecture has four responsibilities: preserve the target, compare applicable methods, attempt a bridge, and review the result. Files make those responsibilities inspectable; instructions alone do not enforce them.

## A worked case with a decisive answer

Take X to be the projective line over a field k, L the trivial bundle, and D the sum of two distinct k-rational points. Identify sections on D with pairs in k². Global sections of L are constants, so restriction sends c to (c,c).

Consequently (1,1) lifts and (1,0) does not. Both have the same ambient geometric data. A policy looking only at the variety, line bundle, or a broad method label cannot distinguish them. The direct restriction computation can.

```text
Carry out the two-point calculation from the stated definitions.
Explain why all global sections of the trivial bundle on the projective line
are constants, citing or supplying the needed justification.
Compute the restriction image and test both sections separately.
Then explain why failure of a sufficient vanishing condition alone would
not prove that either specified section fails to lift.
```

The mathematical answer above is the reference calculation. It is not a claim that a Codex run has already reproduced it. Save the actual response and inspect its reasoning.

## Move from the control to research

Select a lifting step in a proof you understand. Supply the actual statement and source excerpt. Require an applicability table for the vanishing route and an explicit obstruction target for the direct route. Attempt whichever unresolved step could most change the assessment within your budget.

Reject a proof plan that hides its main difficulty in 'standard arguments'. A conditional plan remains useful when its missing lemma is exact and its implication back to the target is justified.

## Evaluation and submission

Test both sections, then change the target version and present an old review. Check that the assistant preserves the chosen section and does not reuse an irrelevant verdict. Compare with an ordinary request to suggest a proof method using the same evidence and time budget.

Submit the exact target, two method cards, full attempted calculation, review findings, and remaining obligations. A persuasive method list without an attempted bridge does not pass.

[Build the base workspace](/posts/2026/08/agent-system/codex-research-studio/) · [Course roadmap](/posts/2026/12/Agent-System/)

