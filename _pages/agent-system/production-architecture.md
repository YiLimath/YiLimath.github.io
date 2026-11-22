---
title: "Durable Research State and Reproducible Recovery"
permalink: /posts/2026/08/agent-system/production-architecture/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/memory-management/). Geometry references below refer to the optional extension of Case A.


After a crash, the system should recover the same target, arguments, reviews, and open obligations. Reconstructing them from a conversational summary can silently change mathematical scope.

## The contract

Use immutable artifact versions, durable writes, and explicit review bindings. Cache keys include the relevant statement, source, context, and policy versions. A hit for another sheaf or assumption set is a correctness defect.

## Trade-offs and failure modes

The current course laboratory saves Markdown records through ChatGPT or Codex. It does not implement transactional storage or automatic crash recovery. Production needs concurrency control, authenticated roles, migrations, backups, and reproducible tools. Monitor infrastructure health separately from mathematical progress.

## Build and test

Save after withdrawing one Case A route, reload, and verify that the alternative survives. Change the saved conclusion and ask the resumed session to compare it with the exact statement covered by its review. Record whether the mismatch is detected; no automatic digest check is supplied.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: separate research correctness from operational reliability

A process can recover every file correctly and still preserve a false lemma. Conversely, a correct proof can be lost by a broken save operation. Maintain separate checks for mathematical admission and storage recovery, with distinct failure reports.

**Acceptance exercise.** Interrupt a write, replay an already processed proposal, and withdraw a supporting premise. Explain which behaviors a manual workflow can demonstrate and which require an implemented transactional storage mechanism.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
