---
title: "Durable Research State and Reproducible Recovery"
permalink: /posts/2026/08/agent-system/production-architecture/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

After a crash, the system should recover the same target, arguments, reviews, and open obligations. Reconstructing them from a conversational summary can silently change mathematical scope.

## The contract

Use immutable artifact versions, durable writes, and explicit review bindings. Cache keys include the relevant statement, source, context, and policy versions. A hit for another sheaf or assumption set is a correctness defect.

## Trade-offs and failure modes

The workbench uses temporary-file replacement for a single-writer snapshot. It is not a transactional multi-user database or a complete event-sourcing implementation. Production needs concurrency control, authenticated roles, migrations, backups, and reproducible tools. Monitor infrastructure health separately from mathematical progress.

## Build and test

Save after withdrawing one Case A route, reload, and verify that the alternative survives. Corrupt the saved conclusion and confirm that its review digest no longer matches.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

---

[Series guide](/posts/2026/08/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
