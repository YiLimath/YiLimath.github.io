---
title: "Module 6: Lean Formalization and the Meaning of a Checked Proof"
permalink: /posts/2026/08/agent-system/lean-formalization/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

**The practical question:** when an agent returns Lean code, what evidence would justify using its result in another proof?

This module introduces formalization through one small mathematical mistake: exchanging two quantifiers. You will read a proof state, complete a proof, and compare a rejected argument with two files that compile but do not establish their claimed result under our policy.

**Prerequisites:** Modules 1–5 and elementary proof writing. No previous Lean knowledge is required. **Deliverable:** a completed proof file and a short report identifying the encoded statement, dependencies, and remaining trust assumptions.

[Download the complete exercise project](/files/lean-reasoning-lab.zip). It uses core Lean, without mathlib or a model API.

## 1. A statement worth getting exactly right

For every natural number $n$, there is a natural number $C$ with $n\leq C$. Choose $C=n$. But there is no single natural number bounding every natural number: given $C$, choose $n=C+1$.

$$
\forall n\in\mathbb N\;\exists C\in\mathbb N:\ n\leq C
\qquad\text{does not imply}\qquad
\exists C\in\mathbb N\;\forall n\in\mathbb N:\ n\leq C.
$$

The first witness may depend on $n$. The second must work for every $n$. This is the elementary version of the uniformity error in [Case B](/posts/2026/08/agent-system/research-cases/). Formalization makes that distinction part of the proposition the checker sees.

```lean
theorem pointwiseBound : ∀ n : Nat, ∃ C : Nat, n ≤ C := by
  intro n
  exact ⟨n, Nat.le_refl n⟩
```

Read the theorem declaration as a contract. `Nat` fixes the domain. `∀` and `∃` fix the quantifier order. The text after `by` supplies a proof.

| Position | Available information | Remaining goal |
|---|---|---|
| Before `intro n` | No chosen natural number | `∀ n : Nat, ∃ C : Nat, n ≤ C` |
| After `intro n` | An arbitrary `n : Nat` | `∃ C : Nat, n ≤ C` |
| After `exact …` | Witness `n` and proof `n ≤ n` | No remaining goal |

`intro` introduces the universally quantified variable. The pair `⟨n, Nat.le_refl n⟩` supplies both the witness and its required property. Tactics help construct a proof term; checking concerns that term and its proposition, rather than the persuasiveness of the tactic text.

## 2. A proof that the uniform version fails

```lean
theorem noUniformBound : ¬ ∃ C : Nat, ∀ n : Nat, n ≤ C := by
  intro h
  cases h with
  | intro C hC =>
    exact Nat.not_succ_le_self C (hC (Nat.succ C))
```

Assume the proposed uniform bound exists. Extract its value `C` and the assertion `hC` that every natural number is at most `C`. Apply that assertion to `Nat.succ C`. It contradicts `Nat.not_succ_le_self C`.

**Pause before running:** point to the exact expression that chooses a counterexample *after* seeing the proposed bound. It is `hC (Nat.succ C)`. This dependence explains the mathematics.

## 3. Run the laboratory

Use the [official Lean installation instructions](https://lean-lang.org/install/) and an editor with Lean support. Extract the project and open its directory. The `lean-toolchain` file pins **Lean 4.19.0** for reproducibility; this is a teaching version, not a claim about the latest release. The first run may download it.

```text
lake build
lake env lean Formalization.lean
python check.py
```

`lake build` builds only the completed library. `Exercises.lean` and the deliberately damaged fixtures are separate. `python check.py` runs five fixed examples and compares the observed outcomes with their expected behaviors.

| File | Observed behavior on Lean 4.19.0 | What the class should conclude |
|---|---|---|
| `Formalization.lean` | Compiles; both declarations report no axioms | The two encoded statements have checked proofs in this environment |
| `Solutions.lean` | Compiles; both declarations report no axioms | Reference solutions for the exercises |
| `fixtures/Broken.lean` | Fails with a type mismatch | A proof of arbitrary `P` cannot fill a goal of arbitrary `Q` |
| `fixtures/Incomplete.lean` | Compiles with a warning; reports `sorryAx` | A placeholder remains |
| `fixtures/ExtraAxiom.lean` | Compiles; reports `inventedBound` | The result relies on the very bound that was assumed |

These outcomes were run locally with the pinned toolchain. A successful regression run means the fixtures behaved as expected. It does **not** mean every example contains an acceptable proof.

## 4. Compilation and admission answer different questions

Run these commands and compare their output:

```text
lake env lean fixtures/Broken.lean
lake env lean fixtures/Incomplete.lean
lake env lean fixtures/ExtraAxiom.lean
```

The first file supplies `hP : P` where `Q` is required. The second uses `sorry`. The third declares the desired bound as an axiom and then uses it. Merely checking the process exit code would miss both latter cases.

Lean provides `#print axioms theoremName` to expose a declaration's axiom dependencies. Our completed elementary examples need none. This does not justify a universal “reject every axiom” policy: other developments deliberately use standard foundations such as choice. State the allowed foundations for the project and audit unexpected additions. See the official [axiom reference](https://lean-lang.org/doc/reference/latest/Axioms/).

An operational record should bind the original statement, formal declaration, exact source and dependency versions, validation output, and reviewer decision. If any of those inputs change, reconsider the admission decision. A label such as `formal-checked` without this evidence is just text.

## 5. The boundary formalization does not remove

Suppose an agent formalizes the pointwise statement when you asked for a uniform bound. A correct proof of the first statement still misses your target. Compare the intended and encoded statements before accepting the result: domains, quantifier order, assumptions, definitions, and conclusion all matter.

Also distinguish these hand-inspected teaching files from arbitrary generated source. Executing generated Lean code and trusting its displayed messages is not a secure validation service. A production system needs isolated execution, controlled dependencies, and validation appropriate to its threat model. The official [proof-validation guide](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) explains stronger checking procedures and their trust boundaries. Its current tooling may differ from this pinned teaching project.

The supplied `check.py` intentionally only regression-tests these exact fixtures. It is not an implementation of those stronger procedures.

## 6. A useful first formalization project

Complete `Exercises.lean` before opening `Solutions.lean`:

1. Prove `∀ n : Nat, ∃ C : Nat, n < C` by choosing a successor. The exercise file supplies `n` as an argument.
2. Rebuild the proof that no largest natural number exists.
3. Run the file and inspect both axiom reports. Explain why an exit code of zero is insufficient while a `sorry` remains.
4. Write a two-column comparison of the informal and formal statements. Explain how the witness depends on the input.
5. Submit a short admission report: exact declaration, toolchain, dependencies, checker output, semantic alignment, and decision.

**Success criterion:** both completed proofs compile without placeholders, their axiom reports match the stated policy, and the informal/formal comparison preserves the problem. A repaired proof of a weakened target does not satisfy the assignment.

## 7. Moving toward research mathematics

For larger developments, [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/) teaches mathematical use of Lean and mathlib. Begin with a small lemma whose definitions and prerequisites already exist in the library. Pin the project toolchain and dependency revision together. Library availability and translation effort are part of project selection.

A useful progression is: read existing formal statements, fill short proofs, reuse library theorems with the right hypotheses, and then formalize one fragile bridge in a research argument. An advanced geometry theorem may require substantial missing infrastructure. A formalized local lemma is valuable partial progress, but does not certify an entire informal manuscript.

The enduring design principle is to keep **the intended proposition, encoded proposition, proof evidence, and admission decision** distinguishable. Future AI may automate more of their construction. The distinctions remain necessary for evaluating its output.

[Return to the course](/posts/2026/12/Agent-System/) · [English teaching materials](/posts/2026/08/agent-system/teaching-materials/)
