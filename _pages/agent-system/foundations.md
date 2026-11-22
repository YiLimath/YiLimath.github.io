---
title: "Module 1. Represent the mathematics"
permalink: /posts/2026/08/agent-system/foundations/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

A mathematical research system must preserve the meaning of its task while its methods, evidence, and conclusions change. This module develops a representation that makes those changes inspectable. We begin with elementary logic, work through a complete geometric example, and then construct a research record directly in Codex.

**Lesson format:** plan for 60–90 minutes of explanation and discussion, followed by a separate laboratory. These are teaching allocations, not measured recording times. Sections 1–4 form the conceptual core; Sections 5–7 connect it to research; Sections 8–10 supply practice and assessment.

**By the end, you should be able to:** distinguish a statement from an argument; track assumptions through several steps; identify a changed target; explain which evidence survives a revision; and build a checkpoint another researcher can audit. No programming is required. The geometric example is derived below and can first be read as a linear-algebra problem.

## 1. Why conversation history is not a mathematical state

Imagine a conversation that begins with “Can this section be extended?” After several attempts, the assistant reports “There is a nonzero section, so the task is solved.” Every sentence may sound relevant. The conclusion can nevertheless answer a different question.

The problem is not primarily a lack of memory. The conversation may preserve every word while failing to distinguish the chosen section from an existentially quantified section. More context does not repair an incorrectly represented target.

A research state should let a new reader answer four questions without reconstructing the entire conversation: What is the exact task? What supports each current conclusion? Which assumptions remain? What would need reconsideration if an input changed?

A transcript is still valuable as an audit trail. A state record is a structured interpretation of that trail, and can itself be wrong. Keep the source arguments available so that the interpretation can be checked.

## 2. Context, proposition, and justification

Write a mathematical judgment schematically as

$$\Gamma\vdash P.$$

Here $P$ is the proposition under consideration and $\Gamma$ contains the objects, definitions, and assumptions available to the argument. In this chapter the notation describes intended mathematical support; writing it in a Markdown file does not invoke a proof checker.

For example, Γ might specify a real-valued continuous function f on [0,1]. The proposition P says that f attains a maximum. If the domain changes to (0,1), the context changes, and the previous theorem application must be reconsidered. The function f(x)=x supplies a counterexample to the corresponding general claim on the open interval.

There are two ways to record a hypothesis. You may work in a context containing P and derive Q, or state the implication P implies Q. What you may not do is record Q as unconditional while silently dropping P.

### A chain of conditional conclusions

Suppose the available arguments establish P implies Q and Q implies R. If P is assumed, you obtain R conditional on P. If P is later proved, that assumption can be discharged using the proof. If P is withdrawn from the working context, the conditional implication may remain useful, but R no longer has the same unconditional support.

The official Lean text gives a formal treatment of propositions, proofs, implication, and assumptions. This module uses those distinctions informally; formal checking comes in Module 6. See [Propositions and Proofs](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/).

### Quantifiers are part of the task

Compare these assertions over the natural numbers:

$$\forall n\;\exists C:\ n\le C,$$

$$\exists C\;\forall n:\ n\le C.$$

The first is true by choosing C=n. The second is false: after a proposed C is fixed, choose n=C+1. A record saying only “a bound exists” loses the dependence that distinguishes a theorem from a false statement.

**Discussion checkpoint:** when a paper writes “there exists a constant C,” what variables may C depend on? A research system should preserve that dependence explicitly wherever it matters to the next inference.

## 3. A complete worked example: can one constant give two prescribed values?

The idea we need is simple: **finding an object is not enough; it must satisfy the exact conditions requested.** We will first work with ordinary real numbers. The connection to “lifting a section” comes afterward, and you can follow the system-design lesson without knowing algebraic geometry.

### Step 1. State the rules of the problem

We are allowed to choose a **constant function**. Once we choose its value $c$, the function has that value everywhere. In particular, at two different points called $p$ and $q$, its values are

$$
f(p)=c,\qquad f(q)=c.
$$

The restriction to constant functions is part of this example's rules. If we allowed arbitrary functions, assigning different values at the two points would be a different problem.

Our task is to find an allowed function with these **prescribed** values:

$$
f(p)=1,\qquad f(q)=0.
$$

“Prescribed” means that the values are already part of the question. We cannot replace the zero by a one to make the problem easier.

### Step 2. Test a proposed answer

Suppose the assistant proposes the constant function $f(x)=1$. This is an allowed function, and it is nonzero. But we must check both requirements:

| Point | Required value | Value of the proposed function | Matches? |
|---|---|---|---|
| $p$ | $1$ | $1$ | Yes |
| $q$ | $0$ | $1$ | No |

So this candidate fails. The error would be to report “a nonzero function exists, therefore the task is solved.” Existence answers only part of the question; matching the prescribed values is essential.

Could a different constant work? To match the value at $p$, we need $c=1$. To match the value at $q$, we need $c=0$. No real number satisfies both equations. This proves that **no allowed function solves this target**, rather than merely showing that our first attempt failed.

### Step 3. Compare three questions that sound similar

Now change the second prescribed value to one. The constant function $f(x)=1$ does meet both requirements. Keep this new task separate from the original:

| Task | Exact question | Answer |
|---|---|---|
| T1 | Can a constant function have values $1$ at $p$ and $0$ at $q$? | No: its values must be equal |
| T2 | Can a constant function have values $1$ at both points? | Yes: choose the constant $1$ |
| T3 | Does any nonzero constant function exist? | Yes: choose the constant $1$ |

T2 and T3 happen to have the same answer and the same example. They still ask different questions. Neither establishes T1. A research system must preserve this distinction even when the conversation moves quickly between the three tasks.

### Step 4. Give the calculation a reusable notation

Let $r$ mean “read off the values at the two points.” Its input is the chosen constant $c$; its output is the pair of observed values:

$$
r(c)=(c,c).
$$

For example, $r(0)=(0,0)$, $r(1)=(1,1)$, and $r(2)=(2,2)$. Every output has equal entries. Conversely, any pair with equal entries, say $(a,a)$, is produced by choosing $c=a$.

The **image** of $r$ means the collection of outputs it can produce. Here that collection consists exactly of pairs with equal entries. It is sometimes called the diagonal because those pairs lie on the line $y=x$ in the plane.

Given a desired pair $s$, a **lift** is an input $c$ that produces it. The equation to check is

$$
r(c)=s.
$$

This is all “lifting” means in the calculation: work backward from prescribed output to an allowed input. The pair $s=(1,1)$ has a lift; $s=(1,0)$ does not. Finding some input without checking its output is not enough.

### Where sections enter the story

There is a geometric setting in which the allowed functions really are exactly the constants. It gives the same map $r$, so none of the answers above changes. Here is a translation guide for readers who will encounter this example in later modules:

| Language in the geometric example | Meaning in this calculation |
|---|---|
| A global section of the trivial line bundle | An allowed function on the whole space |
| A section on the two points | A prescribed pair of values $(a,b)$ |
| Restriction | Read off the function's values at those points |
| Lift the specified section | Find an allowed function producing that exact pair |

These descriptions concern this particular trivial-bundle example; sections of general bundles need not be ordinary scalar-valued functions. You do not need the following geometric justification to use the example in the course laboratory.

<details markdown="1">
<summary>Optional geometry: why the projective-line example gives exactly this map</summary>

Let $k$ be a field, let $X=\mathbb P^1_k$ be the projective line, let $L=\mathcal O_X$ be the trivial line bundle, and let $D$ consist of two distinct $k$-rational points $p,q$. A global section of this bundle is a regular function on $X$. A section on $D$ is a pair of values in $k$.

The important geometric fact is that the global regular functions on $X$ are constants. Here is the calculation for readers familiar with affine charts. Cover $X$ by its two standard affine charts with coordinates $t$ and $u$. On their overlap, $u=1/t$.

A global regular function is described by a polynomial $f(t)$ on the first chart and a polynomial $g(u)$ on the second. Because they describe the same function where the charts overlap, they must satisfy

$$
f(t)=g(t^{-1}).
$$

The left side contains only nonnegative powers of $t$. The right side contains only nonpositive powers. Equality of Laurent polynomials forces every nonconstant coefficient to vanish, so their common value is constant.

Restricting a constant $c$ to $p$ and $q$ produces $(c,c)$. Thus the geometric restriction map is precisely

$$
r:k\longrightarrow k^2,\qquad c\longmapsto(c,c).
$$

Taking $k=\mathbb R$ recovers the numerical calculation above. Over any field the same argument works, since $1\ne0$.
</details>

### What the research system should save

Keep the target, candidate, test, and conclusion distinct:

```text
Target T1: find c such that r(c) = (1,0), where r(c) = (c,c).
Candidate: c = 1.
Test: r(1) = (1,1), which is not the required pair.
Candidate decision: this witness fails.
General argument: every output has equal entries; (1,0) does not.
Target decision: no lift exists under these rules.
Reusable result: (a,b) lifts exactly when a = b.
```

Notice the two different conclusions: the test rejects one candidate; the general argument rules out every candidate. A failed attempt alone would not justify the second conclusion.

**Quick check:** does $(3,3)$ lift? Does $(3,2)$? The first lifts by choosing $c=3$; the second cannot lift because its entries differ. If you can explain those answers and why T3 does not solve T1, you have the mathematical idea needed for the next section.

## 4. The five records and their responsibilities

A minimal design uses statements, arguments, evidence, reviews, and execution tasks. They can be sections of one file. Separate files become useful only when size or coordination makes them necessary.

| Record | Essential content | Error prevented by the distinction |
|---|---|---|
| Statement | Objects, assumptions, quantifiers, conclusion, version | Answering a nearby question |
| Argument | Conclusion, joint premises, inference, open steps | Treating a claim as its own justification |
| Evidence | Proof text, source passage, calculation, actual tool output | Replacing support with a confidence label |
| Review | Exact statement and argument examined, findings, scope | Reusing approval after relevant changes |
| Task | Requested action, input versions, execution outcome | Confusing a timeout with a refutation |

For T1, the statement records the chosen pair (1,0). An argument records that every image of r has equal coordinates. Evidence includes the explicit map and its derivation. A review checks that the argument really concerns T1. A task might request the image calculation; its failure to finish says nothing by itself about liftability.

A source quotation can be evidence about what a paper states without establishing that the theorem applies here. A tool log can establish that a process ran without establishing that its output means what we intended. Evidence must have an interpretation and a scope.

[![Mathematical records and their evidence relationships](/images/agent-system/course-research-records.svg)](/images/agent-system/course-research-records.svg)

*Arrows name relationships between records, not steps that prove a theorem. The review is tied to the exact target and argument versions. A changed section requires checking that relationship again.*

### Why a single “verified” flag fails

A statement may have two arguments, only one of which has been reviewed. A review may approve a conditional argument. A formal check may concern a mistranslated proposition. A single flag collapses these situations.

Use separate fields for workflow status, evidence kind, and mathematical scope. For example: “reviewed; informal argument; conditional on P.” That record is informative without pretending that an informal review has formal assurance.

## 5. Dependencies belong to arguments

Suppose A1 proves T using P and Q together. Another argument A2 proves T using R. The support condition is: P and Q support A1, or R supports A2. It is not sufficient to establish only P, and it is not necessary to finish both routes.

| Available premises | A1 usable? | A2 usable? | Support for T |
|---|---|---|---|
| P only | No | No | None from these arguments |
| P and Q | Yes | No | Through A1 |
| R only | No | Yes | Through A2 |
| P, Q, and R | Yes | Yes | Two available routes |

This is the semantic content a dependency diagram must communicate. An unlabeled arrow from P to T would incorrectly suggest that P alone suffices. Argument nodes or explicit groups of joint premises avoid that ambiguity.

The table assumes the inferences themselves are valid. Bookkeeping cannot supply their proofs. If A1 is later found invalid, P and Q may remain true and reusable even though that route to T is lost.

Likewise, P implies Q and Q implies P do not establish either proposition without a starting point. Logical dependency and the sequence of executed tasks are different structures. A conversation may revisit a question many times without adding a premise.

## 6. Versions and identity: what changed mathematically?

Versioning is useful because reviews have a subject. Changing (1,1) to (1,0) changes that subject. Changing a notation while preserving its definition may not change the proposition, but the system must justify the correspondence rather than infer it from similar wording.

Distinguish three changes:

- **Editorial:** punctuation or presentation changes without altering meaning. Check the claimed equivalence if later automation relies on it.
- **Mathematical:** the domain, section, hypotheses, or conclusion changes. Create a new statement version and reconsider affected applications.
- **Evidential:** a cited result is corrected or an argument is withdrawn. The statement can remain unchanged while its support changes.

An identifier is a reference, not a mathematical invariant. A content hash detects changes in text, not equivalence of propositions. Two equivalent statements can have different text; identical-looking text can use different definitions in different contexts. The record must preserve enough context to interpret its identifiers.

### A useful revision experiment

Review T2 using the witness 1. Then change the chosen section to (1,0) and retain the old review. Ask which parts survive. The existence of the constant section survives, as does the description of restriction. The claim that this witness lifts the newly chosen section fails. This is selective reuse rather than erasing all earlier work or carrying forward all approval.

## 7. From the example to a research reduction

**Optional on a first reading.** This section shows how the same question appears in advanced geometry. If line bundles and cohomology are unfamiliar, continue to the laboratory in Section 8. The numerical map from Section 3 is enough for the core exercises.

For an effective Cartier divisor D and a line bundle L, the restriction sequence is

$$0\longrightarrow L(-D)\longrightarrow L\longrightarrow L|_D\longrightarrow0.$$

The associated cohomology sequence identifies the liftable sections with the kernel of the connecting map $\delta$. Thus a specified $s$ lifts exactly when $\delta(s)=0$. Vanishing of $H^1(X,L(-D))$ is sufficient to make every obstruction zero, but it is stronger than the vanishing of the obstruction of one section.

In a research record, preserve the distinction between these obligations:

1. Establish that the sequence applies to the specified objects.
2. Prove a sufficient vanishing theorem, if that route is chosen.
3. Alternatively determine δ(s) for the particular s.
4. Use exactness to return to the lifting target.

The sequence follows by tensoring the ideal sequence of an effective Cartier divisor with the locally free sheaf L. The exactness-to-kernel step is the mechanism, not an appeal to the phrase “standard lifting argument.” This chapter derives the elementary case explicitly; applying the construction in a new setting requires checking its hypotheses there.

A richer research system will store source applicability, transformations, and alternative methods. They all depend on preserving the simpler distinctions introduced here. Implementing a large framework first cannot compensate for losing them.

## 8. Laboratory: build and challenge the representation

Use a fresh conversation or a dedicated folder in Codex. Save initial outputs before giving corrective hints. These instructions define an experiment; they are not evidence that Codex has already passed it.

### Round A: construct the record

```text
Create RESEARCH.md for real numbers with the given map r(c) = (c,c).
Create three distinct targets: produce (1,0), produce (1,1),
and find any nonzero input c. Supply arguments, not just verdicts.
Test each proposed input by computing its output.
Distinguish rejecting one candidate from ruling out every candidate.
Separate the given rule from the conclusions you derive.
```

**Inspect:** all three targets appear; each proposed input is checked against the required output; impossibility is justified using the equal-entry rule. **Optional extension:** add the projective-line interpretation and ask for the chart calculation explaining why its global sections are constants.

### Round B: introduce a bad witness and a stale review

```text
For the target of lifting (1,0), consider the proposed witness 1.
Check the defining equation for a lift.
Now take a review of the (1,1) argument and apply it to the revised target.
Identify exactly what survives and what requires a new justification.
Preserve the initial incorrect proposal and its diagnosis.
```

**Expected result:** restriction of 1 is (1,1). The witness fails for (1,0). The earlier computation remains valid but its approval does not solve the revised problem.

### Round C: test assumptions and alternatives

```text
For a separate logical exercise, stipulate valid implications
(P and Q) implies T, and R implies T.
Report support with P only, with P and Q, and with R only.
Then assume rather than establish R. Preserve that assumption in T's status.
Do not claim the stipulated implications were independently proved.
```

**Inspect:** the results match the dependency table and conditional scope remains explicit.

### Round D: recover from a checkpoint

Ask Codex to save the exact targets, arguments, assumptions, rejected witness, and next question. Start another conversation with only that record. Ask for the current status of T1–T3 before allowing further research. Compare the reconstruction with the saved evidence. A successful file write does not imply successful mathematical recovery.

## 9. Exercises with worked answers

<details markdown="1">
<summary>Exercise 1 — Diagnose a change of target</summary>

A task asks for a section extending a specified s. The response proves only that a nonzero global section exists. What additional equation must its witness satisfy?

**Answer.** If r denotes restriction and t is the proposed global section, the missing condition is r(t)=s. Nonzeroness of t gives no such equality. In the two-point example t=1 witnesses existence but does not lift (1,0).

</details>

<details markdown="1">
<summary>Exercise 2 — Preserve conditional scope</summary>

Assume P. You have arguments P implies Q and Q implies R. A saved summary says “R established.” Repair it. What changes if an independent proof of R is later added?

**Answer.** Record R conditional on P, with the two implication arguments as support. An independent proof of R gives a second, unconditional route. Withdrawing the assumption P removes the first route's availability but does not invalidate the independent proof.

</details>

<details markdown="1">
<summary>Exercise 3 — Classify a revision</summary>

A source correction adds hypothesis H to a theorem previously used to establish Q. Must Q now be false?

**Answer.** No. The application needs reconsideration. If H is established in the current setting, the corrected theorem may still apply. Otherwise that route has an open obligation. Another argument might independently establish Q. None of these bookkeeping changes alone supplies a counterexample to Q.

</details>

<details markdown="1">
<summary>Exercise 4 — Generalize the worked calculation</summary>

Restrict constants to m distinct k-rational points on the projective line. Which value tuples lift? Treat m=1 separately, and explain why the result does not extend unchanged to a different line bundle.

**Answer.** For m≥1 the restriction sends c to (c,…,c). Its image consists of tuples with all coordinates equal; for m=1 every value lifts. For a different line bundle, its global sections and the restriction map can change. The constant-function calculation no longer describes the problem without an additional identification.

</details>

<details markdown="1">
<summary>Exercise 5 — Design a record for your own mathematics</summary>

Choose a proof step involving a specified map, divisor, section, or parameter. Write its exact target, one argument, and one tempting nearby statement. Identify a change that would invalidate the argument's current review.

**Answer guide.** There is no universal target here. A satisfactory submission names the mathematical objects and assumptions, supplies the actual inference, and gives a concrete distinction that affects the conclusion. “The model might hallucinate” is not a localized failure analysis. An example of a meaningful change is replacing the specified section, changing the divisor twist in a vanishing theorem, or interchanging the order of dependent quantifiers.

</details>

## 10. Assessment and design limits

Submit the research record, initial and corrected assistant outputs, a checkpoint comparison, and your solution to Exercise 5. Assess mathematical fidelity first. A record that solves the wrong target fails even if its formatting is perfect.

A strong submission preserves exact objects, explains every claimed conclusion, tracks assumptions across steps, diagnoses the stale review selectively, and distinguishes actual execution from an expected answer. An adequate submission may remain incomplete if it identifies the exact gap honestly. Unsupported certainty is not an improvement over an explicit open obligation.

Do not create five databases for a ten-line proof. Begin with one Markdown document. Split it when the arguments become large, sources need independent versioning, or multiple tasks repeatedly interfere with each other's state. Representation has a maintenance cost: redundant records can drift apart. Keep one authoritative statement version and refer to it from reviews.

The schemas and laboratory protocol are course design proposals. Their mathematical examples have derivations above; their behavior in a particular assistant session must be observed. This distinction remains important as AI improves: stronger generation changes how efficiently records are produced, not what makes an inference valid.

## Reading and continuation

For the logical distinction between propositions, assumptions, and proofs, read the official [Lean chapter on propositions and proofs](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/). For the role of a *specified* section in geometry, compare the Stacks Project's [correspondence between effective Cartier divisors and invertible sheaves with a regular section](https://stacks.math.columbia.edu/tag/01X0). That correspondence concerns regular sections and should not be confused with a claim that every section is regular.

The next module uses the records developed here to choose research actions and represent joint premises and alternative routes. Bring RESEARCH.md forward rather than starting a new unrelated example.

[Course roadmap](/posts/2026/12/Agent-System/) · [Next: plan and search](/posts/2026/08/agent-system/plan-and-execute/)
