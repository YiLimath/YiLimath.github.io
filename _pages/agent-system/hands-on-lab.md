---
title: "Hands-on: Build a Mathematical Obligation Ledger"
permalink: /posts/2026/08/agent-system/hands-on-lab/
classes: agent-system-page
full_page_reading: true
---

Build a small research workbench before connecting an AI worker. You will implement the contracts used throughout the series, observe their failure modes, and learn exactly what the software does not verify.

Download the [complete laboratory ZIP](/files/math-reasoning-lab.zip), extract it, and use Python 3.9 or later. No API key or external Python package is required.

```sh
python ledger.py
python workbench.py
python -m unittest -v test_workbench.py
```

The first program is the introductory ledger. The second is the reference implementation with alternative arguments, conditional results, version-bound reviews, and persistence. The third runs eight regression tests. Read the code before treating a passing test as evidence about anything beyond the behavior it exercises.

## Stage 1. Separate the statement from its proof

Read [Case A](/posts/2026/08/agent-system/research-cases/). Create statements for the exact-sequence setup, sufficient vanishing, zero obstruction of the chosen section, and lifting that section. Create two arguments for lifting: one using vanishing and another using the direct obstruction.

**Deliverable:** a diagram with an AND relationship inside each argument and an OR relationship between the two arguments. The supplied `case_a()` function is the reference fixture. Its input evidence is stipulated for testing; it does not compute cohomology or prove a vanishing theorem.

**Acceptance:** both routes must refer to the same target version. A route about another section must create another statement.

## Stage 2. Withdraw evidence without destroying valid alternatives

Run `workbench.py`. It first reports `usable` via `via-vanishing`. After withdrawal of `vanishing-evidence`, it reports `usable` via `via-obstruction`. After withdrawal of `direct-obstruction`, it reports `unresolved` and lists the missing premises of the candidate routes.

The setup remains available. The conclusion is not declared false. The reports say which arguments the policy permits, not whether an oracle has established the underlying mathematics.

**Deliverable:** the three reports and an explanation of the difference between invalidating an argument and refuting a statement.

## Stage 3. Preserve conditional conclusions

Declare P and Q and an argument from P to Q. With no evidence for P, Q stays unresolved. Call `report("Q", assumptions=["P"])`; the result is `conditional` with P still listed.

**Acceptance:** a subsequent argument from Q to R must retain P. Add this test yourself. The reference implementation records one supporting route, not every minimal set of assumptions. Explain why enumerating all minimal supports can be more expensive.

## Stage 4. Unsupported cycles cannot create evidence

Declare arguments A from B and B from A, and attach reviews to both. Closure remains empty. Add an independent admitted argument for A; both A and B can then enter closure through grounded support.

This differs from the introductory ledger, which conservatively rejects cycles at insertion. The advanced workbench allows cyclic candidate alternatives while refusing to bootstrap them. Neither implementation checks an infinite induction scheme.

**Deliverable:** a finite instance of Case C and a separate written proof of its general induction order. Removing a base case must expose the corresponding open dependency.

## Stage 5. Bind review to meaning and version

Change the section or sheaf in an argument. The old review digest must not apply. Run the stale-review and persistence tests. Save the workbench, reload it, and compare reports. Alter the saved conclusion text and observe the digest mismatch.

Now request a policy accepting only `formal-checked` evidence. The informal fixtures must remain unresolved. A common JSON envelope does not make evidence kinds interchangeable.

**Deliverable:** a version-change trace and a policy comparison. Identify which boundary would authenticate a reviewer in a real service; the teaching implementation does not provide it.

## Stage 6. Find what the software cannot catch

Run `test_wrong_math_can_pass_policy`. A false open-interval assertion is admitted because the caller supplies a review that endorses it. The test is supposed to pass: it demonstrates the trust boundary.

Write the actual mathematical rejection. Then repeat the exercise with Case B's quantifier interchange. A record validator cannot infer a missing uniform estimate merely because it knows the field names.

**Deliverable:** one software test and one mathematical review for each fixture. Label their evidence separately.

## Stage 7. Add an agent through an artifact contract

Ask a worker to return a target version, candidate argument, required premises, source locators, and open obligations. It may propose records; it may not authorize its own reviews in the production design. Use a separate review interface and preserve its report.

Start with a deterministic fixture adapter before using a model. Then test the same interface on all three cases. Compare with a single-prompt baseline using the same source access and total budget. Measure valid progress and false admissions, not merely the number of completed tool calls.

**Acceptance:** the worker cannot silently replace the target, omit a reported open premise during export, or reuse a verdict for a different argument version.

## Stage 8. A research-grade capstone

Select a short published argument from your own field. Encode its exact target, source theorem applications, one nontrivial transformation, and the return implication. Construct a valid replay and two damaged variants: one with a missing hypothesis and one with an invalid transfer.

Keep the undamaged argument hidden during method selection. Review the returned argument against the source and allow different valid methods. Publish the fixture specification, artifacts, evaluation policy, and limitations alongside your result.

A successful capstone produces an inspectable research episode, not a claim that the system solves arbitrary open problems.

## Reference implementation and limitations

| File | Purpose |
|---|---|
| [ledger.py](/files/math-reasoning-lab/ledger.py) | Introductory single-argument ledger with conservative cycle rejection |
| [workbench.py](/files/math-reasoning-lab/workbench.py) | Alternative arguments, conditional closure, review digests, snapshot persistence |
| [test_workbench.py](/files/math-reasoning-lab/test_workbench.py) | Eight regression tests, including an explicit false-mathematics trust-boundary test |

The code is a single-process, single-writer teaching implementation. It does not authenticate users, sandbox workers, verify citations, discover omitted premises, check natural-language equivalence, or run a proof kernel. Its event list is an audit aid, not a full replay protocol. Tests validate the implemented policies; they do not validate the mathematical content of supplied reviews.

---

[Series guide](/posts/2026/08/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
