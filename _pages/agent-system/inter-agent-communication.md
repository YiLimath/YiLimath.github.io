---
title: "Messages Carry Versioned Mathematical Work"
permalink: /posts/2026/08/agent-system/inter-agent-communication/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/multiple-agent-cooperation/).


“The system is solvable” is incomplete. Which matrix, requested vector, assumptions, and target version? Changing the degree bound in the interpolation example changes the problem even if the task title stays the same.

## The contract

Task messages name inputs, requested artifacts, evidence policy, and budget. Responses name argument versions, evidence, unresolved obligations, and execution outcome. Successful transport means delivery, not admission.

## Trade-offs and failure modes

A late review for an old argument may be retained historically but cannot approve its replacement. Deduplicate retries at the artifact boundary. Source text and worker prose must not grant themselves authority to alter the ledger.

## Build and test

Delay a review, change the requested vector, then deliver the old report. Reject its reuse. Deliver a valid report twice and specify an idempotent handling policy.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: send the mathematical dependency

A message saying “compactness checked” is unusable without the space, topology, hypotheses, and source or argument. Send the exact conclusion together with its assumptions and the version of the problem it concerns. The receiver still checks applicability.

**Acceptance exercise.** Change the topology while preserving the space name. A receiver that accepts the old message without inspection has failed the exercise. Communication should reduce ambiguity, not turn a short label into authority.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
