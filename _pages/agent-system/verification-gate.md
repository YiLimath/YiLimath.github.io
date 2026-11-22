---
title: "Module 5. Decide what evidence permits reuse"
permalink: /posts/2026/08/agent-system/verification-gate/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

Review is a mathematical examination. Admission is a workflow decision about whether a result may be used as a premise. Neither repeated agreement nor a field named verified establishes truth.

## A review that does not transfer

An argument checks that (1,1) lifts in the two-point restriction example. Change the target to (1,0), retaining the same variety and line bundle. The old review cannot establish the new target: it examined a different section, and the new statement is false.

Freeze the target, argument, assumptions, and source versions before review. In a Codex workspace, identifiable versions and preserved text suffice to demonstrate the principle. They do not enforce authentication or prevent the assistant from overlooking a change.

## Three fields, three questions

| Field | Example | Meaning |
|---|---|---|
| Workflow status | Candidate, reviewed, admitted, withdrawn | What the workflow has done |
| Evidence | Source check, informal argument review, actual formal check | What procedure supplies support |
| Scope | Conditional on P; fixed target version | Where the conclusion can be used |

If P implies Q and Q implies R while P is only assumed, R remains conditional on P. Recording Q as useful must not erase this assumption.

```text
Review this exact argument and target version.
Identify each substantive inference and its supporting premises.
Report a localized error, missing justification, or accepted inference.
Keep conditional assumptions visible. Do not rewrite the target to repair it.
Then compare the report with the revised version and identify what must be rechecked.
```

Use a fresh conversation when helpful, but do not call it statistically independent. Give it the full argument and source evidence, not merely a summary of prior approval.

## What formal evidence changes

An actual Lean check addresses the encoded proposition relative to its dependencies. It does not establish that the encoded proposition matches the intended task. The next module makes this distinction concrete with working proofs, a type error, a placeholder, and an extra axiom.

## Acceptance

Test a valid argument, a missing assumption, a changed section, and a conditional chain. Save the actual reports and inspect whether the errors are localized. If you ask for formal status without execution evidence, the correct answer identifies what is missing. These are tests of the conversation's behavior, not guarantees supplied by the prompt.

---

[Course roadmap](/posts/2026/12/Agent-System/) · [Direct experiments](/posts/2026/08/agent-system/hands-on-lab/) · [Next module](/posts/2026/08/agent-system/lean-formalization/)
