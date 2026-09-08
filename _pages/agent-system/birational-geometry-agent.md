---
title: "Case Study Extension: A Spiral-Induction Agent for Birational Geometry"
permalink: /posts/2026/08/agent-system/birational-geometry-agent/
tags:
  - Agent System
  - Mathematics
  - Birational Geometry
classes: agent-system-page
full_page_reading: true
---

## Figure

![A spiral-induction agent architecture for birational geometry](/images/agent-system/30-birational-geometry-agent.svg)

*Figure. Design sketch, not an as-built system. The upper band is the
mathematical control state: a coupled theorem package is advanced by creating
the right lower-dimensional object, checking its hypotheses, and admitting only
verified updates. The lower band maps the agent-design patterns to the research
workflow. Solid navy arrows show control, dashed teal arrows show evidence or
repair feedback, and red arrows show a correctness or admission gate.*

> **Status of this page.** This is a domain-specific architecture sketch. It is
> not a claim that Danus, Rethlas, or any current system already implements the
> complete birational-geometry workflow shown here.

The central idea is that birational geometry should not be represented as a
single linear “question → proof” pipeline. A research episode often changes
representation: a pair may be replaced by a log-smooth model, a divisor may be
restricted by adjunction, or a fibration may expose a lower-dimensional base.
The agent must preserve those changes as explicit, typed obligations rather
than hiding them inside a long conversation.

## 1. Spiraling induction as the mathematical control policy

Here “spiraling induction” refers to the [BCHM-style proof organization](https://www.ams.org/jams/2010-23-02/S0894-0347-09-00649-3/viewer/)
recorded in the birational-geometry notes: several statements are proved
together in dimension $n$, while some steps manufacture an object in dimension
$n-1$, apply the lower-dimensional package, and use the result to advance the
current package. It is a mathematical proof architecture, not a standard AI
design pattern name.

For the BCHM package, the useful abstract dependency shape is:

| Dependency | Role in the package |
|---|---|
| $E_{n-1}\Rightarrow B_n$ | lower-dimensional finiteness supplies special finiteness in dimension $n$ |
| $A_n+B_n\Rightarrow C_n$ | flips plus special finiteness support the minimal-model step |
| $D_{n-1}+B_n+C_n\Rightarrow D_n$ | non-vanishing is lifted one dimension up |
| $C_n+D_n\Rightarrow E_n$ | existence and non-vanishing yield global finiteness |
| $C_n+D_n+E_n\Rightarrow F_n$ | the package closes with finite generation |

The important engineering consequence is not to encode these symbols as labels
only. Each edge needs an obligation record containing:

- the statement being attempted and its dimension;
- the object that has to be constructed before induction applies;
- the hypotheses that must be rechecked on that object;
- the evidence and proof artifact supporting the implication; and
- the next obligations unlocked by an accepted result.

The system therefore spirals in two senses: it revisits a coupled theorem
package, and it moves between dimensions or derived objects while preserving a
machine-readable ledger of what has actually been established.

## 2. The pattern is broader than BCHM

The theorem graph is not universal: BAB and the Kähler results of Hacon–Xie do
not use the same labels or the same technical objects. What recurs is the
architecture of the proof: a family of coupled claims, a representation change
that makes an induction hypothesis applicable, a hypothesis audit, and an
output that feeds a later claim.

| Proof programme | Spiral structure | Design lesson for the agent |
|---|---|---|
| BCHM | $A_n,\ldots,F_n$ are advanced together; lower-dimensional finiteness and adjacent statements close the package | the ledger must represent a dependency graph, not a single chain |
| [Birkar's BAB theorem](https://annals.math.princeton.edu/2021/193-2/p01) | lower-dimensional boundedness is used to control current-dimensional volume or birational boundedness, which is combined with complements and singularity estimates to obtain a bounded family | boundedness is an output contract, not merely a similarity score or a list of examples |
| [Hacon–Xie](https://arxiv.org/html/2607.24986) | the proof explicitly cycles through contraction, base-point-free, MMP with scaling, and non-gklt contraction results across dimensions; the paper lays out these implications in Section 1.1 | each edge must record its dimension, manufactured object, and rechecked hypotheses |

The Hacon–Xie case is particularly close to the proposed control model. Their
proof separates the big and non-big cases, uses adjunction or an MRC/Mori-fibre
space base to reach a lower-dimensional problem, and then returns the result to
the original space. The agent should therefore store the *construction of the
induction object* as a first-class artifact, rather than treating “apply
induction” as a black-box action.

## 3. Proposed architecture

Read the upper band of the figure first. The supervisor does not ask a worker
to “prove the theorem” in one shot. It selects one frontier obligation, asks
what object would make the next theorem applicable, and routes the obligation
to the appropriate specialists. The verifier then checks both the proposed
mathematical artifact and the conditions for using it.

The lower band is a composition of the patterns developed in this course:

1. **Plan-and-execute** decomposes a target into a bounded sequence of
   obligations rather than free-form subgoals.
2. **Routing** chooses between literature recovery, example construction,
   proof synthesis, formalization, counterexample search, and human review.
3. **Parallelization** runs independent searches only when their outputs can be
   normalized and compared.
4. **Structured output** makes every worker return an obligation, evidence
   packet, derivation, counterexample, or verification report with a fixed
   schema.
5. **Knowledge retrieval and provenance** preserve theorem statements,
   hypotheses, page or section information, and the exact source of a claim.
6. **Reasoning and representation change** treats adjunction, fibrations,
   restrictions, models, and numerical conditions as explicit transformations.
7. **Reflection and recovery** turn a failed hypothesis check into a repair
   task, not an unsupported revision of the conclusion.
8. **Memory management** stores accepted artifacts and dependency edges, not
   merely the raw transcript of the agent.
9. **Human-in-the-loop and guardrails** reserve mathematical interpretation,
   research significance, and final admission for an explicit checkpoint.

## 4. Typed research artifacts

The architecture becomes auditable only when its intermediate objects are
stable. A minimal artifact vocabulary is:

| Artifact | Required content | Why it matters |
|---|---|---|
| Research brief | pair, dimension, target statement, hypotheses, scope | fixes what the system is actually trying to establish |
| Obligation | claim, dependencies, target dimension, constructed object, acceptance test | makes the spiral step local and schedulable |
| Evidence packet | source, theorem/lemma, quotation or locator, applicability notes | prevents retrieved mathematics from becoming context-free text |
| Derivation | premises, transformations, conclusion, unresolved gaps | separates a proposed proof route from a verified proof |
| Verification report | checks run, failures, repair hints, status | makes rejection informative and reproducible |
| Ledger update | accepted artifact, dependency edges, newly unlocked obligations | records the state of the induction rather than the conversation |

An artifact should carry a status such as `proposed`, `needs-hypothesis-check`,
`rejected`, `verified`, or `human-accepted`. Only the last two states may unlock
the next stage, and a `verified` result should still record which verifier and
which assumptions produced that status.

## 5. One spiral episode

For one frontier obligation, the control loop is:

1. **Select the frontier.** The supervisor chooses the highest-value unresolved
   obligation under a dimension, dependency, and resource budget.
2. **Compile the obligation.** The planner writes the target statement,
   dependencies, and the object that must be manufactured before the induction
   hypothesis can be invoked.
3. **Route and explore.** Specialists search the literature, inspect examples,
   test boundary cases, and propose a proof or reduction in parallel where
   independence is genuine.
4. **Normalize.** The system converts the results into typed evidence packets
   and derivations with explicit hypotheses and provenance.
5. **Check the representation change.** A dedicated verifier checks that
   adjunction, restriction, fibration, birational modification, or dimension
   drop has been stated correctly and that the new object satisfies the needed
   assumptions.
6. **Verify and repair.** Logical, symbolic, formal, and citation checks either
   produce a repairable failure or a candidate admission report. A human may
   inspect the interpretation when the mathematical stakes require it.
7. **Commit the update.** The ledger receives the result only through an
   admission gate. The update unlocks the next obligation and starts the next
   turn of the spiral.

This gives the system a meaningful stopping rule: stop when the target package
has a verified dependency path, or stop with a precise unresolved obligation
when the evidence or hypotheses are insufficient. “The model produced a
plausible proof” is not a termination condition.

## 6. Domain-specific pattern map

| Course pattern | Birational-geometry specialization | Stable interface |
|---|---|---|
| Plan and execute | theorem package → local implication → verification task | `Obligation` |
| Router | choose flip, finiteness, non-vanishing, model, termination, or application branch | `Obligation.kind` |
| Parallelization | literature search, examples, reductions, and formal checks | `EvidencePacket[]` |
| Knowledge retrieval | recover a theorem together with hypotheses and applicability conditions | `SourceRecord` |
| Reasoning / representation change | adjunction, fibration, restriction, model change, numerical-to-linear data | `Transformation` |
| Reflection | compare a proposed step against all required hypotheses and dependencies | `VerificationReport` |
| Memory management | persist theorem statements, accepted artifacts, and dependency edges | `InductionLedger` |
| Exception recovery | classify missing hypothesis, failed reduction, contradiction, or tool failure | `RepairTask` |
| Human-in-the-loop | interpret significance and approve high-consequence admissions | `ReviewDecision` |

The interfaces are deliberately mathematical rather than framework-specific.
An implementation could change its language model, retrieval backend, or formal
checker without changing the contract of an obligation or verification report.

## 7. Reliability boundaries

The proposed system may search, compare, formalize, test, and suggest. It must
not silently:

- apply an induction hypothesis before recording the dimension drop;
- replace a pair without rechecking singularities, positivity, or coefficient
  conditions;
- confuse numerical equivalence, linear equivalence, and actual equality;
- treat a citation as evidence that its hypotheses apply to the current pair;
- promote a fluent proof sketch into the induction ledger; or
- treat an unresolved counterexample search as evidence of truth.

These boundaries are the domain equivalent of the correctness gate seen in the
[Danus and Rethlas code case study](/posts/2026/08/agent-system/math-research-case-study/):
generation and verification are separate responsibilities, and admission is an
explicit state transition.

## 8. A realistic first implementation

The safest first vertical slice is deliberately narrow:

1. define the `ResearchBrief`, `Obligation`, `EvidencePacket`, and
   `VerificationReport` schemas;
2. implement a supervisor that advances one small theorem package at a time;
3. add retrieval with source locators and hypothesis extraction;
4. add example and counterexample workers before adding many autonomous proof
   writers;
5. require a human review for every ledger update during evaluation; and
6. measure hypothesis accuracy, provenance completeness, repair usefulness,
   and false-admission rate on a fixed collection of known arguments.

Only after this slice is reliable should the system add broader exploration,
more agents, or expensive formal verification. The architectural objective is
not maximal autonomy. It is a trustworthy research instrument whose next step,
evidence, and reason for stopping can all be inspected.

## References

1. C. Birkar, P. Cascini, C. D. Hacon, and J. McKernan, “Existence of minimal
   models for varieties of log general type,” *Journal of the American
   Mathematical Society* 23 (2010), 405–468. [AMS article](https://www.ams.org/jams/2010-23-02/S0894-0347-09-00649-3/viewer/)
   and [arXiv version](https://arxiv.org/abs/math/0610203).
2. C. Birkar, “Singularities of linear systems and boundedness of Fano
   varieties,” *Annals of Mathematics* 193 (2021), 347–405. [Journal article](https://annals.math.princeton.edu/2021/193-2/p01).
3. C. Hacon and L. Xie, “On the Kähler MMP and the transcendental
   base-point-free theorem,” arXiv:2607.24986 (2026), especially Sections 1.1–1.2.
   [Paper](https://arxiv.org/abs/2607.24986) and [HTML version](https://arxiv.org/html/2607.24986).
4. J. Liu et al., “Danus: Orchestrating Mathematical Reasoning Agents with
   Fact-Graph Memory,” arXiv:2607.06447 (2026). [Paper](https://arxiv.org/abs/2607.06447)
   and [source repository](https://github.com/frenzymath/Danus).
5. H. Ju et al., “Automated Conjecture Resolution with Formal Verification,”
   arXiv:2604.03789 (2026). [Paper](https://arxiv.org/abs/2604.03789) and
   [source repository](https://github.com/frenzymath/Rethlas).
6. A. Gullí, *Agentic Design Patterns: A Hands-On Guide to Building Intelligent
   Systems*, Springer, 2025. [Publisher record](https://link.springer.com/book/10.1007/978-3-032-01402-3).
7. V. Dibia, *Designing Multi-Agent Systems: Principles, Patterns and
   Implementation for AI Agents*. [Author's book site](https://multiagentbook.com/).
