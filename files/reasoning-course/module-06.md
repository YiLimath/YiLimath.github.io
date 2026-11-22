# Module 6: Formalize a proof with Lean

**Deliverable:** A checked proof and a statement-alignment report.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/lean-formalization/

## Segment 6.1 · Slide 17: A witness in Lean

### Spoken script

We now formalize the example from Module 4. Read the statement before reading the proof. Nat fixes the domain, and the quantifiers tell us when the witness may depend on the input. After intro n, our context contains an arbitrary natural number and our goal asks for a bound for that number. The pair supplies the witness n and a proof that n is at most itself. Open the editor's proof state and follow this change one line at a time. The important learning outcome is the relation between the mathematical statement and the remaining obligation, rather than memorizing a tactic.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 6.2 · Slide 18: Compilation does not settle admission

### Spoken script

Run all three damaged examples. The first tries to use a proof of P where Q is required and fails. The second uses sorry, so compilation can succeed even though the proof is unfinished. The third contains no sorry but assumes the desired conclusion as an axiom. For these fixed examples, inspect the printed axiom dependencies. Our completed elementary proofs need no axioms. Larger developments may deliberately use standard foundations, so the general policy is to state and audit the allowed dependencies, not blindly reject every axiom. The regression script checks these fixtures only. It is not a secure verifier for arbitrary generated code.

**Pause question:** Which successful compilations in the fixtures are unacceptable under the lesson's policy, and why?

**Expected discussion:** Incomplete.lean depends on sorryAx. ExtraAxiom.lean depends on inventedBound. Neither supplies the required proof under our policy. A checked proof of a different proposition would also fail statement alignment.

## Segment 6.3 · Slide 19: The intended statement remains part of the task

### Spoken script

A correct proof of the pointwise statement does not prove a uniform bound. Formal checking therefore needs a companion task: compare the encoded proposition with the intended mathematics. Complete the exercise that uses a successor as a strict upper bound, then reconstruct the proof that there is no largest natural number. Record the exact declarations and their axiom reports. For research mathematics, begin with a small lemma supported by existing library definitions. Formalizing one fragile bridge can be useful, but it does not certify the rest of an informal paper. For unreviewed generated source, use isolation and a suitable stronger validation procedure rather than trusting displayed output alone.

## Live demonstration

In files/lean-reasoning-lab, run lake build, lake env lean Formalization.lean, and python check.py. In the editor, place the cursor after intro n. Then run each fixtures/*.lean file individually. Use Lean 4.19.0 from lean-toolchain. Open Solutions.lean only after the exercise.

## Student assignment

Complete Exercises.lean and submit the informal/formal statement comparison, version information, axiom reports, and admission decision.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.

## Source notes

- https://lean-lang.org/doc/reference/latest/Axioms/
- https://lean-lang.org/doc/reference/latest/ValidatingProofs/
- https://leanprover-community.github.io/mathematics_in_lean/
