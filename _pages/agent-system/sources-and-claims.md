---
title: "Sources, Evidence, and the Limits of the Examples"
permalink: /posts/2026/08/agent-system/sources-and-claims/
classes: agent-system-page
full_page_reading: true
---

The course is under a substantive source and exercise revision. Its criterion is practical: help an agent complete previously unfinished mathematical work, or reach the same justified result with less measured cost. This page distinguishes support for a mathematical theorem from evidence that a workflow improves performance. Neither replaces the other.

## What the first audit found

The pre-revision snapshot contained 41 public chapter pages; 29 had no direct external source link. This was a citation-coverage check, not a verdict that 29 pages were mathematically false. Many short pattern pages repeated procedural exercises without a source-based research problem. They are now optional reference cards tied to the [minimal-surface uniqueness workshop](/posts/2026/08/agent-system/birational-proof-workshop/), not independent advanced lectures.

The new workshop supplies complete proof routes relative to explicitly imported theorems. Its mathematical exposition has been checked in this editing pass, but it is not a formally verified development. No controlled agent experiment has yet established that the proposed course workflows improve capability or cost. Student runs must supply that evidence.

## Mathematical source map

| Result or input | Source and locator | Scope of the support |
|---|---|---|
| Negativity lemma | [Birkar, *Lectures on Birational Geometry*, arXiv:1210.2670v1, Lemma 4.15, p. 21](https://arxiv.org/pdf/1210.2670v1#page=21) | The specified projective birational algebraic theorem; not an automatic analytic extension |
| Common resolution of regular surfaces | [Stacks, Tag 0C5S](https://stacks.math.columbia.edu/tag/0C5S), Lemma 54.17.2 | Common point-blowup model for a birational map of proper regular surfaces |
| Factorization of surface morphisms | [Stacks, Tag 0C5R](https://stacks.math.columbia.edu/tag/0C5R), Lemma 54.17.1 | Factorization into point blowups under its regular surface hypotheses |
| Descent through a contracted exceptional curve | [Stacks, Tag 0C5J](https://stacks.math.columbia.edu/tag/0C5J), Lemma 54.16.1 | Factorization of a morphism constant on that curve |

Local calculations and consequences are written out and labeled as course exposition. They are not attributed as quotations or claimed to be new theorems. The geometric project imports the four listed results and proves the remaining comparisons and descent steps explicitly.

## Reasoning-system sources

- **Proof planning:** Bundy, [“Proof Planning” (1996), pp. 261–262, “The Nature of Proof Plans”](https://cdn.aaai.org/AIPS/1996/AIPS96-033.pdf#page=1). Methods describe tactic prerequisites and effects; critics concern failures and possible repairs. This supplies a historical basis for method applicability, not a guarantee for language-model research.
- **Dependency revision:** Doyle, [“The Ins and Outs of Reason Maintenance” (1983), opening description of reason maintenance](https://ijcai.org/proceedings/1983/82). Tracking the reasons for derived beliefs predates modern agents. Our Markdown records are a proposed manual interface, not an implementation of the paper's algorithms.
- **Formal meaning and assumptions:** the official Lean text, [“Propositions and Proofs”](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/), supplies the logical foundation used in Module 1.
- **Validation boundary:** the official [“Validating a Lean Proof”](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) distinguishes what was proved from what the statement means and describes checks of different strength. Its “Printing Axioms” and “Gold Standard” sections support the need to inspect dependencies and the validation environment. Current documentation does not imply that every tool described there exists in the older pinned teaching environment.
- **Workflow vocabulary:** [Anthropic, “Building effective agents”](https://www.anthropic.com/research/building-effective-agents), is practitioner guidance on workflow and agent patterns. It is not an empirical validation of this mathematics course.

Gulli's, Dibia's, and Lakshmanan–Hapke's books remain optional engineering background. Merely naming these books does not justify a particular mathematical claim or a performance forecast. Claims that depend on a book passage need an edition and inspected location before being treated as sourced.

## Reported systems are a separate evidence category

[Danus v2](https://arxiv.org/abs/2607.06447v2), abstract, reports fact-graph memory, planning, parallel workers, and claim checking before admission. [Rethlas–Archon v2](https://arxiv.org/abs/2604.03789v2), abstract, reports informal reasoning linked to Lean formalization. These high-level descriptions were checked against the versioned abstracts in this pass. Their experiments and artifacts were not independently reproduced here. Quantitative comparisons or claims of superiority require inspection of the relevant evaluation and matched runs.

## What must still be demonstrated

| Part of the course | Current status | Required evidence before a stronger claim |
|---|---|---|
| Geometric workshop | Source-based teaching proof with explicit imported lemmas | Actual baseline and assisted runs; localized checking of each output |
| Core modules 1–5 | Methods and examples, now attached to geometric proof obligations | Show which intervention fixes which observed proof failure |
| Module 6 | Formalization tutorial and separately scoped teaching artifacts | Actual execution and statement/dependency checks for each new formalization |
| Modules 7–8 | Proposed recovery and coordination protocols | Recovery/coordination outcomes and full resource accounting |
| Module 9 | Proposed evaluation rubric | Collected results; no invented savings or discovery rates |
| Opportunity discovery | A hypothesis-audit and prior-art workflow proposal | A real candidate, inspected neighboring results, and an attempted decisive lemma |
| Short pattern cards | Optional interventions, not standalone modules | Retain only when they improve a relevant run |

A learned method is valuable when it changes an outcome or its cost. A correct proof supplied in the lesson is a reference answer, not evidence that an agent produced it. A repaired run with a human-supplied key lemma is assisted work, not autonomous discovery. An elementary control is not a benchmark of original research.

[Start the birational proof project](/posts/2026/08/agent-system/birational-proof-workshop/) · [Course roadmap](/posts/2026/12/Agent-System/)
