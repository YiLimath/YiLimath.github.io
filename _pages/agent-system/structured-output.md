---
title: "Types That Preserve Mathematical Distinctions"
permalink: /posts/2026/08/agent-system/structured-output/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

A record with `claim` and `confidence` is structured but mathematically weak. Useful types distinguish a statement from its argument, an assumption from a justified premise, and an evidence category from a workflow status.

Case A needs the chosen section and exact restriction map. Case B needs quantifier order and allowed constant dependencies. Case C needs indexed statements, base cases, and a rank. A generic summary field conceals all three.

## Four checks, four meanings

Parsing checks required fields. Referential validation checks that linked objects exist and match their versions. Policy validation checks whether the available evidence permits use. Mathematical review checks whether the inference is justified. Return these failures separately.

The workbench hashes the argument together with its statement and premise records. This binds a review to what it inspected. It does not authenticate the reviewer, discover missing premises, or prove equivalence between differently worded statements.

## Replace components without erasing evidence

Dependency injection supplies a source adapter or reviewer through a stable interface. It is useful when the implementation changes. However, an informal review cannot satisfy a policy requiring a formal certificate merely because both fit the same JSON schema.

## Build and test

Create a valid record that interchanges the quantifiers in Case B. Parsing should succeed. Explain the separate semantic obligation needed to catch the error. Then run the workbench under informal-only and formal-only policies and compare the outcomes.

Read with the [three running cases](/posts/2026/08/agent-system/research-cases/). Source provenance and the distinction between established patterns and our proposed specialization are explained in [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

---

[Series guide](/posts/2026/08/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
