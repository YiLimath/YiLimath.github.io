---
title: "Research Architecture: A Proof-Sketch and Method-Recommendation System"
permalink: /posts/2026/08/agent-system/proof-sketch-system/
tags:
  - Agent System
  - Mathematics
  - Automated Reasoning
classes: agent-system-page
full_page_reading: true
---

## Figure

![Architecture of a proof-sketch and method-recommendation system](/images/agent-system/34-proof-sketch-system.svg)

*Figure. The system first constructs a portfolio of proof methods, tests their
applicability with bounded probes, and selects a small, diverse set of viable
strategies. It then compiles the leading strategy into a dependency graph of
proof obligations and submits that graph to method-specific critics. Solid navy
arrows show control or dependency, dashed teal arrows show evidence or repair,
and red marks the boundary between an admitted sketch and a proved theorem.*

> **Scope.** This is a research architecture, not a claim that a general system
> can currently discover reliable proof sketches for arbitrary research
> mathematics. The architecture says what evidence and intermediate artifacts
> such a system would need before its recommendation should be trusted.

**In one sentence.** Recommend methods whose preconditions fit the theorem,
compile the best candidates into inspectable obligation graphs, and report the
remaining bottleneck instead of converting plausibility into proof.

## 1. The task has three different outputs

A proof assistant, a proof-search engine, and a proof-sketch assistant answer
different questions. Conflating them produces impressive prose and weak
mathematics.

| Level | Question answered | Legitimate output |
|---|---|---|
| Heuristic suggestion | What might be worth trying? | ranked methods with reasons and cheap tests |
| Proof sketch | How could the theorem follow if the named obligations are discharged? | strategy, constructions, lemma graph, applicability checks, and explicit gaps |
| Proof | Have all obligations been discharged under the stated hypotheses? | complete argument or kernel-checked formal term |

The proposed system specializes in the first two levels. It may invoke formal
tools during feasibility tests, but a successful test of one branch does not
promote the whole sketch to a proof. A sketch may be *viable* or *conditional*;
it is never labelled *verified theorem*.

This boundary also explains what “professional” means here. A professional
sketch is not a shortened proof produced by deleting details. It preserves the
load-bearing structure: why this method fits, which new object must be
constructed, which lemmas are needed, how the lemmas depend on one another,
where each hypothesis is used, and what remains genuinely unresolved.

## 2. Mathematical and architectural foundations

Pólya's four phases—understand the problem, devise a plan, carry it out, and
look back—supply the outer research loop. His concrete questions supply the
method-discovery moves: retrieve a related theorem, change the unknown or the
data, introduce an auxiliary object, specialize, generalize, or solve a more
accessible related problem.

The more technical ancestor is Bundy's **proof planning**. A proof method is a
schema with explicit preconditions and expected effects; methods are composed
at the meta-level into a global plan. A **critic** recognizes a characteristic
failure and proposes a repair such as a missing lemma, a generalization, a case
split, or a different induction rule. This is stronger than asking a language
model to “think of another approach,” because the failure and its repair have a
typed relationship to the attempted method.

The course books provide the agent-system realization of this idea:

- Gulli's planning, reflection, reasoning, retrieval, evaluation, and
  exploration patterns separate method generation from criticism and bounded
  search;
- Dibia's computational workflows, structured outputs, orchestrator loop, and
  trajectory evaluation make the intermediate proof state inspectable; and
- Lakshmanan and Hapke's Chain of Thought, Tree of Thoughts, LLM-as-Judge,
  Reflection, Dependency Injection, Tool Calling, and Self-Check patterns
  provide replaceable mechanisms beneath those interfaces.

The resulting architecture is therefore book-based at the pattern level and
proof-planning-based at the mathematical level.

## 3. Stable artifacts

The system should communicate through mathematical records rather than through
untyped messages.

| Artifact | Required fields | Invariant |
|---|---|---|
| `TheoremSpec` | exact statement, hypotheses, quantifiers, definitions, domain, allowed sources | notation and hypotheses are copied without silent strengthening |
| `MethodCard` | intent, preconditions, expected effect, constructions, usual subgoals, failure signatures, critics, provenance | a method is a reusable proof schema, not a topic label |
| `StrategyCandidate` | instantiated method, precondition matrix, supporting analogues, predicted obligations, risks, probe plan | every recommendation states why it might apply here |
| `ProbeReport` | test, result, evidence, scope, failure, cost | a local success claims no more than the probe checked |
| `ProofBlueprint` | named nodes, dependency edges, node statements, discharge route, unresolved nodes | the target is reachable only through explicit obligations |
| `SketchCritique` | violated criterion, affected nodes, severity, repair operation | rejection is actionable rather than a score |
| `ProofSketch` | strategy thesis, key construction, blueprint, bottleneck, alternatives, references, status | `viable` and `conditional` remain distinct from `proved` |

The `MethodCard` is the central variation point. A general analysis library may
contain compactness, approximation, duality, contradiction, induction, and
localization cards. A birational-geometry library instead contains adjunction,
subadjunction, canonical bundle formula, MRC or Iitaka fibration, MMP with
scaling, complements, and boundedness arguments. The orchestration remains the
same while the mathematical content changes.

## 4. Architecture

### 4.1 Compile the theorem state

The state compiler extracts the target, all hypotheses, the type of each
object, ambient category, available lemmas, invariants, and prohibited moves.
It also records ambiguity. If “pair,” “positive,” or “general” has two plausible
meanings in the source, the system must resolve the ambiguity or branch the
analysis; it may not choose silently.

This stage produces features useful for retrieval and method selection, but the
original theorem statement remains immutable. A normalized representation is a
view of the theorem, not a replacement for it.

### 4.2 Generate a method portfolio

The recommender combines two sources:

1. **schema retrieval:** MethodCards whose preconditions resemble the current
   theorem state; and
2. **analogue retrieval:** previously proved theorems with a comparable goal,
   obstruction, construction, or dependency shape.

The portfolio must retain genuine diversity. Ten paraphrases of induction are
one candidate, not ten. At this stage the system is allowed to include a
speculative method, but speculation is represented as a status and never as a
high confidence score.

PaMpeR demonstrates the narrower but important case in which proof-state
features support explainable recommendations of Isabelle proof methods. A
research-sketch system extends that interface from local prover methods to
higher-level mathematical methods, where many preconditions cannot be decided
syntactically and must become proof obligations.

### 4.3 Run bounded feasibility probes

Each candidate receives a small test budget before expensive proof search:

- **hypothesis and type unification:** do the candidate theorem or method
  conditions match the current objects?
- **related-proof and premise retrieval:** is there a source-supported analogue,
  and exactly where does its argument use additional hypotheses?
- **examples and counterexamples:** does the strategy survive boundary cases,
  known obstructions, and the smallest nontrivial examples?
- **symbolic, computational, or formal smoke test:** can a central identity,
  finite case, local lemma, or formal subgoal actually be discharged?

These probes do not prove the target. They turn a vague recommendation into an
evidence-bearing `StrategyCandidate` and often expose the first real bottleneck.

### 4.4 Select promising methods without an opaque confidence score

“Promising” should mean **legally applicable, structurally progressive,
evidence-supported, testable, and recoverable when it fails**. Selection is
therefore staged:

1. reject candidates with a contradicted hard precondition;
2. mark missing but potentially provable preconditions as obligations;
3. compare the survivors on expected goal progress, support from analogous
   proofs, tractability of new obligations, verification cost, and failure risk;
4. retain a small top-$k$ set whose methods are materially different; and
5. expose the comparison and allow a mathematician to override it.

No scalar score should erase the difference between “the hypotheses fit but the
central lemma is hard” and “the central lemma looks easy but the method is not
known to apply.” Those are different research situations and require different
repairs.

### 4.5 Compile the selected strategy into a proof blueprint

The blueprint compiler expands the selected MethodCard into named obligations.
Every node has a statement, dependencies, intended discharge method, relevant
hypotheses, and status. Every edge answers: *why does this predecessor unlock
that successor?*

This graph is the professional core of the proof sketch. It supports parallel
work only on independent nodes, identifies the critical path, and provides a
meaningful stopping condition. The recent Goedel-Architect preprint implements
a formal version of this principle: an initial graph of definitions and lemmas
is refined using success and failure on its open nodes. The older
Draft–Sketch–Prove work similarly uses formal sketches to divide proof search
into easier subproblems.

### 4.6 Apply method-specific critics

The critic suite checks more than surface coherence:

- the **applicability critic** rechecks every imported theorem and method
  precondition;
- the **dependency critic** looks for circularity, unreachable nodes, and a
  conclusion stronger than its predecessors;
- the **counterexample critic** attacks new lemmas and silent generalizations;
- the **source and notation critic** checks provenance, quantifiers, domains,
  and equivalence relations; and
- the **granularity critic** detects an “obligation” that merely restates the
  original theorem or hides the hard step under words such as *standard*.

Critics may repair the blueprint by inserting a lemma, splitting a case,
changing representation, weakening an intermediate claim, or returning to the
method portfolio. They may not silently edit the theorem being proved.

## 5. The proof-sketch output contract

A reader should be able to inspect the final sketch in this order:

1. **Exact theorem.** The statement and labelled hypotheses.
2. **Strategy thesis.** One or two sentences naming the central mechanism.
3. **Why this method.** Matched preconditions, analogues, and rejected serious
   alternatives.
4. **Key construction or representation change.** The object that makes the
   method applicable.
5. **Obligation graph.** Named lemmas and the reason for every dependency edge.
6. **Critical path.** The smallest set of obligations whose failure blocks the
   whole strategy.
7. **Hypothesis ledger.** Where each assumption enters and whether it may be
   weakened.
8. **Bottleneck and open gaps.** Precise unresolved statements, not optimistic
   placeholders.
9. **Fallback methods.** Conditions under which the system should switch.
10. **Provenance and status.** Sources, probes, critic reports, and one of
    `viable`, `conditional`, or `rejected`.

This format agrees with the layered proof template already used in the math
vault: high-level idea first, then tools, then fine-grained proof units, with the
difficult step and hypothesis usage made explicit.

## 6. Example: specializing the architecture to birational geometry

Suppose the theorem state presents a generalized pair and a current-dimensional
existence or positivity problem. The recommender should not return “try
induction” as a method. It should instantiate several domain MethodCards, for
example:

| Candidate | Preconditions to audit | Expected reduction | Characteristic risk |
|---|---|---|---|
| Adjunction or subadjunction | suitable divisor or non-klt center; induced singularities controlled | replace the problem by one on a lower-dimensional center | the induced boundary or nef part does not satisfy the required hypothesis |
| Canonical bundle formula | appropriate fibration and adjoint-trivial relation | transfer the problem to a generalized pair on the base | discriminant/moduli data or positivity is insufficient |
| MRC or Mori-fibre route | non-pseudo-effectivity or uniruled branch; lower-dimensional base | separate rationally connected fibre behavior from the base problem | the desired statement does not transfer from base and fibre |
| Iitaka fibration | finite generation, semi-ampleness, or the required abundance input | reduce along the Kodaira-dimension fibration | the fibration is invoked before its existence is established |
| Spiraling induction | a coupled theorem package with explicit cross-dimensional implications | manufacture the object needed by a lower-dimensional statement and return its conclusion | dimension, model, or theorem-package state is lost during the return step |

The generic proof-sketch system supplies recommendation, probing, blueprinting,
and criticism. The [birational-geometry research architecture](/posts/2026/08/agent-system/birational-geometry-agent/)
supplies the domain objects and geometric MethodCards. This separation lets the
same proof-planning machinery serve another field without pretending that its
mathematics is interchangeable.

## 7. Evaluation programme

Evaluation must distinguish recommendation quality from proof correctness.

| Measure | What it tests | Main danger |
|---|---|---|
| method recall@$k$ | whether a known successful method, or an expert-approved alternative, appears in the portfolio | treating the published proof as the only valid strategy |
| false-applicability rate | how often a recommended method has a contradicted precondition | rewarding attractive but illegal suggestions |
| precondition coverage | whether all method hypotheses are checked or exposed as obligations | hidden assumptions |
| blueprint closure | fraction of nodes discharged by the proposed routes | replacing a hard theorem by equally hard unnamed nodes |
| gap-localization accuracy | whether critics identify the actual load-bearing gap | verbose criticism with no repair value |
| false-closure rate | how often the system labels an incomplete sketch viable | the most serious reliability failure |
| diversity-adjusted usefulness | expert rating of whether the top-$k$ set contains distinct, actionable approaches | duplicated candidates inflating recall |
| time to first viable sketch | cost before a mathematician receives a useful plan | uncontrolled search |

Use chronological or novel-premise splits where possible. LeanDojo's
`novel_premises` split illustrates why: a random split can reward near-duplicate
proofs and memorized premise use. For research mathematics, add fresh problems
and source-ablation tests, and retain the complete recommendation trajectory so
that an expert can diagnose why a method was selected.

## 8. Relationship to real systems

The [Danus and Rethlas case study](/posts/2026/08/agent-system/math-research-case-study/)
shows real code for generation, strategy steering, theorem search, verification,
and gated fact storage. It does not by itself establish the general
method-library and blueprint architecture proposed here. This page should be
read as a next system layer that can produce a candidate proof blueprint for a
generation-and-verification system to execute.

Several implemented or reported systems validate narrower parts of the
architecture:

- PaMpeR recommends proof methods from proof-state features and explains its
  recommendations;
- LeanDojo's ReProver retrieves premises for tactic generation and exposes
  formal proof-state feedback;
- Draft–Sketch–Prove converts an informal proof into a formal sketch whose
  holes become smaller proving tasks;
- the DeepInsight project organizes informal theorem-proving data into a
  hierarchy of core technique, proof sketch, and final proof, supporting the
  separation of method discovery from proof writing;
- AlphaGeometry alternates symbolic deduction with learned auxiliary
  constructions in a restricted geometry domain; and
- Goedel-Architect, currently a 2026 preprint, represents a formal proof plan as
  a lemma-dependency blueprint refined from failed nodes.

These systems demonstrate components, not a solved universal architecture for
research-level informal mathematics. That limitation should remain visible in
both the course and any implementation.

## 9. A realistic implementation sequence

1. Build a small, human-authored MethodCard library for one mathematical domain.
2. Compile exact theorem statements into `TheoremSpec` without changing
   notation or assumptions.
3. Retrieve analogues and recommend a diverse top-$k$ portfolio with an
   explicit precondition matrix.
4. Add cheap counterexample, symbolic, and formal probes.
5. Compile one selected method into a `ProofBlueprint` and expose the critical
   path.
6. Implement method-specific critics and repair operations.
7. Evaluate on hidden known proofs before attempting open problems.
8. Only then connect the blueprint nodes to autonomous proof workers and an
   independent verification gate.

The difficult research question is not whether a model can name a plausible
technique. It is whether the system can explain why the technique applies,
manufacture the right intermediate objects, predict the obligations it creates,
and localize failure when the plan breaks.

## References

1. G. Pólya, *How to Solve It: A New Aspect of Mathematical Method*, Princeton
   University Press, 1945; later editions. [Publisher catalogue](https://assets.press.princeton.edu/catalogs/math11.pdf).
2. A. Bundy, “Proof Planning,” *Proceedings of the Third International
   Conference on Artificial Intelligence Planning Systems*, 1996, 261–267.
   [AAAI paper](https://cdn.aaai.org/AIPS/1996/AIPS96-033.pdf).
3. A. Bundy, “A Critique of Proof Planning,” in *Computational Logic: Logic
   Programming and Beyond*, Lecture Notes in Computer Science 2408, Springer,
   2002, 160–177. [Author manuscript](https://www.inf.ed.ac.uk/publications/online/1311.pdf)
   and [publisher record](https://link.springer.com/book/10.1007/3-540-45632-5).
4. Y. Nagashima and Y. He, “PaMpeR: Proof Method Recommendation System for
   Isabelle/HOL,” arXiv:1806.07239, 2018. [Paper](https://arxiv.org/abs/1806.07239).
5. A. Q. Jiang et al., “Draft, Sketch, and Prove: Guiding Formal Theorem Provers
   with Informal Proofs,” *ICLR 2023*. [Paper](https://arxiv.org/abs/2210.12283)
   and [Cambridge repository record](https://www.repository.cam.ac.uk/items/b528f361-ac5b-4244-b1f7-ceeba25564f4).
6. K. Yang et al., “LeanDojo: Theorem Proving with Retrieval-Augmented Language
   Models,” *NeurIPS 2023*. [Paper](https://arxiv.org/abs/2306.15626).
7. T. Trinh et al., “Solving Olympiad Geometry without Human Demonstrations,”
   *Nature* 625 (2024), 476–482. [System and paper overview](https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/).
8. J.-H. Chung et al., “Goedel-Architect: Streamlining Formal Theorem Proving
   with Blueprint Generation and Refinement,” arXiv:2606.06468, 2026 preprint.
   [Paper](https://arxiv.org/abs/2606.06468).
9. Y. Li et al., “Learning to Reason with Insight for Informal Theorem Proving,”
   arXiv:2604.16278, 2026 preprint. [Paper](https://arxiv.org/abs/2604.16278).
10. A. Gulli, *Agentic Design Patterns: A Hands-On Guide to Building Intelligent
    Systems*, Springer, 2025, Chapters 4, 6, 14, 17, 19, and 21.
    [Publisher record](https://link.springer.com/book/10.1007/978-3-032-01402-3).
11. V. Dibia, *Designing Multi-Agent Systems: Principles, Patterns, and
    Implementation for AI Agents*, 2025, Chapters 4, 6, 7, and 10.
    [Book site](https://multiagentbook.com/).
12. V. Lakshmanan and H. Hapke, *Generative AI Design Patterns*, O'Reilly,
    2025, Patterns 13, 14, 17–19, 21, 23, and 31.
    [Publisher record](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/).
