---
title: "Designing a Spiraling Induction System for Birational Geometry"
permalink: /posts/2026/08/agent-system/birational-geometry-agent/
tags:
  - Agent System
  - Mathematics
  - Birational Geometry
classes: agent-system-page
full_page_reading: true
---

The goal is to build a research system whose unit of reasoning is a **geometric
induction step**: construct the right object, establish the hypotheses of an
available theorem, obtain a conclusion, and prove how that conclusion advances
the original problem. The system should eventually help solve birational
geometry problems, with an argument that a researcher can inspect, correct,
and reuse.

Birational geometry suggests a particular architecture. A proof often needs
several statements at once: existence of models, non-vanishing, finiteness, or
termination in a specified setting. Progress on one makes another accessible.
Meanwhile, adjunction or a fibration changes the object and may lower its
dimension. The proof returns to its original target with additional
information. I call this organization **spiraling induction**.

The design question is precise: **how can an agent explore this spiral while
keeping every use of induction and every transfer of a conclusion
mathematically accountable?**

> **Status.** This page proposes an architecture and an evaluation programme.
> It does not describe an implemented prover or claim that an existing agent
> can autonomously solve the problems discussed here. The mathematical examples
> motivate the design; the software contracts below are proposed interfaces.

![Spiraling induction: descend to a suitable object, return through a transfer proof, and advance an acyclic theorem ledger](/images/agent-system/30-birational-geometry-agent.svg)

*A turn of the spiral has an outward journey and a return journey. Constructing
a lower-dimensional pair is only the first half. A separate transfer argument
must connect its conclusion to the current target. Repeated exploration may
loop; accepted proof dependencies must remain well-founded.*

## 1. What makes the induction spiral?

There are three interacting movements:

1. **Advance within a theorem package.** Prove an auxiliary statement that
   unlocks another statement in the same dimension.
2. **Descend through geometry.** Construct a divisor, center, base, or fiber
   on which an available lower-dimensional statement applies.
3. **Return with a transfer argument.** Lift sections, descend a divisor,
   glue morphisms, or compare models to advance the original target.

The return is often the difficult part. Knowing something on a divisor does
not automatically prove it on the ambient variety. Nor does replacing a pair
by a better model automatically solve the original problem.

### A concrete dependency pattern: BCHM

In [BCHM, Section 2](https://arxiv.org/html/math/0610203#S2), the labels denote
pl-flips ($A$), special finiteness ($B$), log terminal models with an effective
representative ($C$), non-vanishing ($D$), finiteness of models ($E$), and the
finite-generation package ($F$). Their inductive dependencies are:

| Available premises | Next conclusion |
|---|---|
| $F_{n-1}$ | $A_n$ |
| $E_{n-1}$ | $B_n$ |
| $A_n$ and $B_n$ | $C_n$ |
| $D_{n-1}$, $B_n$, and $C_n$ | $D_n$ |
| $C_n$ and $D_n$ | $E_n$ |
| $C_n$, $D_n$, and $E_n$ | $F_n$ |

These summarize dependencies, not unrestricted theorem statements. Each node
must retain the source's full hypotheses, including its relative setting and
boundary conditions. The first implication uses the external pl-flip result
cited there. In particular, $C_n$ assumes an effective representative; using
$D_n$ to supply it cannot be hidden inside a purported independent proof of
$C_n$.

**Store implications with all their premises.** An edge from three premises to
one conclusion is a single inference requiring all three, not three independent
routes. Base cases and external theorems must be listed explicitly.

### A spiral is not a circular proof

After indexing statements by dimension and proof stage, the accepted graph
must be acyclic. For the schematic package above, one can order nodes by

$$
\rho(T_n)=(n,\operatorname{stage}(T)),
\qquad A<B<C<D<E<F,
$$

with lexicographic order. Inductive calls use a smaller dimension; dependencies
in the same dimension use an earlier stage. This is a scheduling order for
this package, not a universal invariant of birational geometry. An induction
on another complexity requires its own well-founded order and a proof of
strict decrease.

Maintain two graphs: a **search graph**, which may revisit failed ideas, and an
**accepted dependency graph**, which cannot use its own conclusion as a premise.
A proposed cycle becomes a diagnostic: split a statement, find an independent
lemma, strengthen the induction hypothesis, or abandon the route. Renaming a
claim or changing its model does not break a logical cycle.

## 2. The research state must carry the mathematics

A transcript is useful history, but it is not sufficient proof state. The
system needs the following records:

| Record | Mathematical content |
|---|---|
| Problem | Exact target, quantifiers, hypotheses, and allowed external results |
| Geometric object | Variety or space, dimension, base, boundary, nef data if present, and current model |
| Theorem instance | Source version and locator, full statement, substitution of variables, and evidence for each hypothesis |
| Obligation | One missing claim, its scope, prerequisites, and required output |
| Reduction | Source and target objects, construction, adjoint relation, dimension or complexity change, and return obligation |
| Proof artifact | Argument, exact premises, conclusion, unresolved assumptions, and review evidence |
| Ledger | Versioned artifacts, accepted dependencies, blocked branches, and invalidated descendants |

The object record distinguishes projective from compact Kähler geometry,
absolute from relative statements, ordinary from generalized pairs, and
$\mathbb Q$-divisors from $\mathbb R$-divisors or transcendental classes.
Singularity and positivity properties carry evidence; they are not inherited
merely because a predecessor object had them.

A theorem lookup must return more than a relevant paragraph. It should produce
an applicability table:

| Required hypothesis | Evidence on this object | Result |
|---|---|---|
| Dimension below the current induction level | Construction and dimension calculation | Discharged or open |
| Required singularities | Applicable adjunction theorem and its inputs | Discharged or open |
| Required positivity over the specified base | Separate positivity argument | Discharged or open |
| Permitted coefficient set | Calculation after transformation | Discharged or open |

An open row creates a new obligation. It never disappears into “the hypotheses
are standard.” In a boundedness problem, track uniformity as well: which
constants depend only on dimension, coefficients, or a fixed $\epsilon$, and
which still depend on the individual variety.

## 3. Geometric reductions need a return contract

Every reduction answers four questions: **What is constructed? Why is the next
theorem applicable? What does it give? How does that help the original target?**

### Adjunction and subadjunction

For a suitable plt pair $(X,S+B)$ with $S$ a coefficient-one prime divisor,
divisorial adjunction produces

$$
(K_X+S+B)|_S=K_S+B_S.
$$

Record normality, the different $B_S$, the induced singularities, and
$\dim S=\dim X-1$. Subadjunction on a higher-codimension center is a separate
operation: ordinary and generalized formulations have different inputs and
outputs. A generic “non-klt center” is not enough to select one. See the
[adjunction discussion in the Hacon–McKernan–Xu notes, §3.2](https://www.claymath.org/wp-content/uploads/2022/03/Hacon-AG2015.pdf).

The return contract might ask for extension of sections, control near $S$, or
gluing across strata. None follows from the adjunction identity alone.

### Canonical bundle formula

In a suitable ordinary lc-trivial fibration, the relevant formula has the form

$$
K_X+B\sim_{\mathbb Q}f^*(K_Z+B_Z+M_Z).
$$

First justify the fibration hypotheses, then record the discriminant and
moduli b-divisor and the model on which the required positivity holds. Nefness
of the moduli part must not be silently upgraded to semiampleness. Generalized
or Kähler versions require their own contracts; the displayed formula is not
an automatic identity for every fibration.
[Ambro's paper](https://arxiv.org/abs/math/0308143) provides a foundational
reference for the moduli b-divisor.

If the lower-dimensional conclusion is semiampleness, the return contract must
identify an actual pullback relation of the appropriate kind. Numerical
equivalence cannot substitute for a relation of line bundles when transporting
sections.

### MRC and Iitaka fibrations

An MRC fibration separates rationally connected directions from a base problem;
an Iitaka fibration organizes a linear series of nonnegative Iitaka dimension.
The latter can be constructed birationally without first proving semiampleness.
Distinguish this rational-map construction from a morphism defined by a
semiample divisor, and check whether the base is actually lower-dimensional.
A big divisor gives no such dimension drop. See Lazarsfeld's
[*Positivity I*](https://link.springer.com/book/10.1007/978-3-642-18808-4)
for the linear-series setting.

Neither fibration automatically equips the base with the adjoint structure
needed for induction. Constructing that structure and proving a transfer
statement are additional tasks.

### Birational modifications and MMP steps

A log resolution, dlt modification, contraction, or flip usually preserves
dimension. These operations prepare a reduction or improve a model. Record
discrepancies, exceptional divisors, and the precise pullback or pushforward
comparison needed later.

“Run the MMP” must resolve into an applicable existence and termination result,
or remain an obligation. A software iteration limit is not a mathematical
termination proof. Not every model change decreases an induction rank.

## 4. A worked turn: returning from a divisor

Here is a deliberately elementary test of the full contract. It exercises
adjunction, a lower-dimensional input, and a return argument without pretending
to reproduce the harder extension steps of the MMP.

Let $X$ be a smooth projective variety over $\mathbb C$, let $S$ be a smooth
prime divisor, and let $B$ be an effective $\mathbb Q$-divisor such that
$S+\operatorname{Supp}B$ has simple normal crossings, $S$ is not a component of
$B$, and every coefficient of $B$ is less than one. Put

$$
D=K_X+S+B.
$$

Fix a positive integer $m$ such that $mD$ is Cartier. Suppose the available
lower-dimensional input gives
$H^0(S,\mathcal O_S(mD|_S))\ne0$, and suppose separately that

$$
H^1(X,\mathcal O_X(mD-S))=0.
$$

**Local target:** prove $H^0(X,\mathcal O_X(mD))\ne0$.

| Step | Artifact produced | What remains |
|---|---|---|
| Construct | $(S,B|_S)$ with $D|_S=K_S+B|_S$ | Check the lower-dimensional theorem |
| Check | Smooth $S$, dimension $n-1$, klt induced pair | Match any positivity and divisibility assumptions |
| Invoke | A nonzero section $s_S$ at this particular multiple $m$ | Lift it to $X$ |
| Transfer | Surjectivity of the restriction map below | Choose a lift of $s_S$ |
| Record | A nonzero section upstairs | Admit only this stated conclusion |

The transfer uses the exact sequence

$$
0\longrightarrow\mathcal O_X(mD-S)
\longrightarrow\mathcal O_X(mD)
\longrightarrow\mathcal O_S(mD|_S)
\longrightarrow0.
$$

The assumed $H^1$-vanishing makes restriction on global sections surjective.
A lift of the nonzero $s_S$ is nonzero, proving the target.

This exposes three common failures. A lower-dimensional theorem that gives a
section at *some* multiple does not automatically give one at the chosen $m$.
A section on $S$ does not lift without a transfer argument. And one nonzero
section does not establish semiampleness or finite generation.

If vanishing is unproved, the correct output is a conditional lemma and an
open transfer obligation. The system may seek a vanishing or extension theorem,
or change its route. It must not invent the missing positivity. This is the
basic behaviour the first prototype should demonstrate.

## 5. A controller for one turn of the spiral

The supervisor works on a **frontier of unresolved obligations**. Prefer an
obligation that unlocks several needed claims, has a plausible geometric
construction, and has a manageable verification cost. This is a search
heuristic, not evidence that the chosen branch is true.

```text
while budget remains and the target is unresolved:
    choose a frontier obligation
    propose a theorem application or geometric reduction
    reject circular dependencies and illegal inductive calls
    record construction, applicability, and transfer obligations
    work on prerequisites whose own inputs are available
    check the candidate against exact object and premise versions
    if the admission policy is satisfied:
        commit the artifact and its full dependencies
        refresh the frontier
    else:
        preserve the failure and queue a repair or alternative route
return the argument, its assurance level, and the unresolved frontier
```

A conditional derivation may be stored before its premises are proved, but its
conclusion cannot become an unconditional fact. External results also need an
audit for hidden dependence on the target. In proof-replay evaluation, exclude
the target theorem and downstream corollaries as shortcuts.

Stopping outcomes are explicit: **target discharged under the declared trust
policy**, **checked counterexample**, **blocked by named obligations**, or
**budget exhausted**. Exhausting a search proves neither truth nor falsity.
The controller can stop reliably without claiming that mathematical research
must terminate.

## 6. Agents have bounded responsibilities

Agent patterns become useful once each role has a mathematical input and
output contract:

| Role | Responsibility | Output |
|---|---|---|
| Planner | Decompose the target and maintain legal dependencies | Obligation graph |
| Literature worker | Recover exact statements and compare hypotheses | Theorem instances with locators |
| Geometry worker | Propose a model, center, divisor, or fibration | Reduction and return contract |
| Example worker | Test boundary cases and seek counterexamples | Computations and their scope |
| Proof worker | Derive one local claim from declared premises | Candidate argument with gaps exposed |
| Verifier | Check applicability, inference, transfer, and provenance | Review report with failed checks |
| Ledger controller | Enforce admission and propagate revisions | Versioned proof state |

These are responsibilities, not a requirement for seven separate language
models. Start with a small implementation. Independent literature searches or
example checks can run in parallel, but their outputs must refer to compatible
object and statement versions before being merged.

The [Danus and Rethlas case study](/posts/2026/08/agent-system/math-research-case-study/)
connects this proposal to the course's agent-design patterns. The distinctive
requirement here is the geometric reduction contract and its place in a
well-founded theorem package.

## 7. Admission, trust, and mathematical memory

“Verified” is too ambiguous to be a single status. Keep workflow state separate
from the kind of evidence supporting an artifact.

| Field | Example values |
|---|---|
| Workflow | Proposed, checking, blocked, admitted, rejected, invalidated |
| Evidence | Source-backed, machine-checked calculation, model-reviewed, expert-reviewed, formally checked |
| Scope | Exact statement, object version, assumptions, theorem versions |
| Admission | Policy used, reviewer or checker, timestamp, dependencies |

Evidence labels can coexist. Formal checking applies only to the encoded
statement and its declared axioms; it does not automatically verify the
translation from the research problem. A source-backed theorem still needs
an applicability argument. Agreement between models is review evidence, not
a proof certificate.

During the first evaluation stage, an expert should approve every new
mathematical inference admitted to the ledger. Automated checks can enforce
required fields, dependency order, version consistency, and the presence of
hypothesis evidence. Schema validation alone cannot establish that an informal
proof is correct.

Admission requires all of the following:

1. The exact claimed conclusion is supported by the argument.
2. Every premise is admitted at the required assurance level, or explicitly
   retained as an assumption of a conditional statement.
3. The theorem application and geometric transfer have no undisclosed gaps.
4. The dependency graph remains well-founded.
5. The designated review policy has been satisfied.

If a premise is corrected or withdrawn, affected descendants become stale and
must be rechecked before reuse. Search history and failed attempts remain
available, but cannot function as accepted facts. Reusable memory stores the
scope of a lemma and its failure conditions alongside its successful argument.

## 8. Extending the architecture beyond one package

BCHM supplies an unusually explicit dependency skeleton. It should be the first
package to encode, not a universal template into which all proofs are forced.

For **boundedness**, [Birkar's BAB theorem](https://annals.math.princeton.edu/2021/193-2/p01)
motivates a different output contract: a bound must be uniform in the declared
parameters. Checking many examples cannot establish boundedness of a family.
Track quantifiers and dependence of constants through every reduction.

For **Kähler geometry**, [Hacon–Xie, §§1.1–1.2](https://arxiv.org/html/2607.24986)
organize contraction, base-point-free, MMP, and non-gklt results across dimensions.
Their discussion separates big and non-big cases and uses lower-dimensional
objects together with gluing or transfer arguments. This motivates additional
object types for transcendental classes and analytic spaces. A projective
theorem cannot be imported solely because its conclusion sounds similar.

For **new research**, the theorem package itself may be unknown. The system
must be able to propose an auxiliary lemma or a stronger inductive statement.
That proposal remains a conjectural node until justified. Changing the package
requires checking its base cases and rebuilding the dependency order; it is
not permission to assume the stronger statement.

## 9. Build and evaluate the smallest complete spiral

The first implementation should replay a small collection of known arguments
from a fixed source corpus. It needs a theorem registry, an obligation ledger,
a reduction interface, an admission gate, and a readable proof export. It does
not need a large autonomous agent population.

**Milestone 1: represent the package.** Encode the six BCHM dependency shapes,
their full source statements, explicit base cases, and permitted external
inputs. Demonstrate that a missing premise or circular invocation is blocked.

**Milestone 2: complete a local turn.** Implement the divisor example above,
including a successful transfer and variants with missing vanishing or a
mismatched multiple. Produce a readable argument and its obligation trace.

**Milestone 3: replay a substantive reduction.** Choose one published adjunction
or canonical-bundle-formula argument. Recover its construction, applicability
checks, and return step with expert review. Test the same interface on a second
argument without changing the schema to fit the answer.

**Milestone 4: attempt a bounded research task.** Fill a specified missing step
or explore a special case under a fixed budget. Report conditional results and
remaining obstacles as carefully as successful proofs.

Evaluation must include deliberately invalid steps:

| Test case | Required behaviour |
|---|---|
| Missing bigness or wrong singularity class | Block the application and name the missing evidence |
| Numerical equivalence substituted for linear equivalence | Reject unsupported transport of sections |
| A dimension-preserving model change called induction | Demand another justified induction order or treat it as preparation |
| Lower-dimensional conclusion with no return proof | Keep the original target open |
| Unproved target reused under another name | Detect the dependency cycle |
| Premise corrected after admission | Invalidate dependent artifacts and recheck them |
| No counterexample found within budget | Report an inconclusive search |

Measure false admissions among injected invalid steps, successful admission of
valid steps, completeness of hypothesis and transfer records, and expert time
needed to repair an argument. Track cost per completed obligation as well.
A system that rejects everything has low false-admission counts but does not
help research; useful progress and sound rejection must be measured together.

The desired deliverable from a research episode is a precise statement, a
readable argument, its dependency graph, the geometric constructions and return
proofs, and an honest account of unresolved assumptions. The spiral advances
when one of those mathematical obligations is discharged—not when another
round of discussion has finished.

## References

1. C. Birkar, P. Cascini, C. D. Hacon, and J. McKernan, *Existence of minimal
   models for varieties of log general type*, JAMS 23 (2010), 405–468.
   [Paper, especially §2](https://arxiv.org/html/math/0610203#S2).
2. C. Birkar, *Singularities of linear systems and boundedness of Fano
   varieties*, Annals of Mathematics 193 (2021), 347–405.
   [Journal article](https://annals.math.princeton.edu/2021/193-2/p01).
3. C. Hacon and L. Xie, *On the Kähler MMP and the transcendental
   base-point-free theorem*, arXiv:2607.24986 (2026).
   [Paper](https://arxiv.org/html/2607.24986).
4. F. Ambro, *The moduli b-divisor of an lc-trivial fibration*.
   [arXiv:math/0308143](https://arxiv.org/abs/math/0308143).
5. C. D. Hacon, J. McKernan, and C. Xu, *Boundedness of varieties of log
   general type*, expository notes, §3.2.
   [Notes](https://www.claymath.org/wp-content/uploads/2022/03/Hacon-AG2015.pdf).
6. R. Lazarsfeld, *Positivity in Algebraic Geometry I: Classical Setting:
   Line Bundles and Linear Series*, Springer, 2004.
   [Publisher record](https://link.springer.com/book/10.1007/978-3-642-18808-4).
