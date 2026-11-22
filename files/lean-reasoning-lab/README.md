# Lean reasoning laboratory

Use Lean **4.19.0**, pinned by `lean-toolchain`. No mathlib or API key is required.

Install Lean through the [official instructions](https://lean-lang.org/install/), extract this folder, and open a terminal here:

```text
lake build
lake env lean Formalization.lean
lake env lean fixtures/Broken.lean
lake env lean fixtures/Incomplete.lean
lake env lean fixtures/ExtraAxiom.lean
```

Run these commands yourself or ask Codex to execute them and retain actual output. Broken.lean should fail with a type mismatch. Incomplete.lean compiles with sorryAx; ExtraAxiom.lean compiles with inventedBound. Neither meets the lesson's admission policy.

Complete Exercises.lean, run `lake env lean Exercises.lean`, and inspect both axiom reports. Compare the encoded propositions with the intended statements. Solutions.lean contains reference solutions.

No Python is needed. These hand-inspected examples demonstrate specific behaviors; they are not a secure validation service for arbitrary generated code.
