# Lean reasoning laboratory

Use Lean **4.19.0**, pinned by `lean-toolchain`. No mathlib or API key is required.

Install Lean through the [official instructions](https://lean-lang.org/install/), extract this folder, and open a terminal here:

```text
lake build
lake env lean Formalization.lean
python check.py
```

The first command builds the completed library only. The checker runs five fixed fixtures and expects some to fail or carry unapproved axioms. A successful checker run means the expected behaviors were observed, not that all fixture theorems are established.

`Solutions.lean` contains reference solutions. `fixtures/ExtraAxiom.lean` intentionally assumes a false bound; it is a demonstration of a trust-policy failure, not an acceptable mathematical dependency.

`check.py` is a small regression script for these exact files. It reads diagnostic text and is not a robust parser or a secure checker for arbitrary generated Lean code. Production admission needs statement alignment, controlled dependencies, isolated execution, and a suitable proof-validation procedure.

Complete Exercises.lean, inspect the axiom reports, and compare the informal and encoded statements. Solutions.lean contains reference solutions.
