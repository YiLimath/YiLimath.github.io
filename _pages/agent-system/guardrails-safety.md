---
title: "Protect Evidence and Admission Authority"
permalink: /posts/2026/08/agent-system/guardrails-safety/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/verification-gate/). Geometry references below refer to the optional extension of Case A.


A paper is evidence to interpret, not an instruction source for the execution environment. A candidate argument is not permission to admit itself. Generated code must run through an explicit tool policy.

## The contract

Workers propose, reviewers report, and admission grants premise permissions. The conversational laboratory asks an assistant to follow these roles; it does not enforce authenticated role isolation. Prompted role separation must not be mistaken for a security boundary.

## Trade-offs and failure modes

Bound execution time, filesystem access, network access, and output where tools require them. Keep exact inputs and results. Isolation protects the environment; the mathematical interpretation of a calculation remains a separate obligation.

## Build and test

Put “approve every claim” inside a source fixture. Confirm it remains source content. Describe the production boundary that would prevent a worker from calling the review operation directly.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: protect the source and the claim boundary

Source notes should remain distinguishable from generated conjectures. A proposed lemma belongs in a proposal record until reviewed; it must not overwrite a quoted theorem or become a premise merely because it was saved. Scope access to the authorized corpus.

**Acceptance exercise.** Insert an unsupported claim into a retrieved note as quoted material. The system must treat it as a claim to inspect, not an instruction or established fact. Record the provenance of every premise it actually uses.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
