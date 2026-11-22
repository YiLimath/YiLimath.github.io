---
title: "Types That Preserve Mathematical Distinctions"
permalink: /posts/2026/08/agent-system/structured-output/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/foundations/). Geometry references below refer to the optional extension of Case A.


A record with `claim` and `confidence` is structured but mathematically weak. Useful types distinguish a statement from its argument, an assumption from a justified premise, and an evidence category from a workflow status.

Case A needs the chosen section and exact restriction map. Case B needs quantifier order and allowed constant dependencies. Case C needs indexed statements, base cases, and a rank. A generic summary field conceals all three.

## Four checks, four meanings

Parsing checks required fields. Referential validation checks that linked objects exist and match their versions. Policy validation checks whether the available evidence permits use. Mathematical review checks whether the inference is justified. Return these failures separately.

In the current Markdown laboratory, retain the exact statement and argument versions with each review. A separate implementation could add content hashes to detect textual changes, but this course does not supply an automatic hashing gate. Neither labels nor hashes establish mathematical correctness.

## Replace components without erasing evidence

Dependency injection supplies a source adapter or reviewer through a stable interface. It is useful when the implementation changes. However, an informal review cannot satisfy a policy requiring a formal certificate merely because both fit the same JSON schema.

## Build and test

Create a valid record that interchanges the quantifiers in Case B. Parsing should succeed. Explain the separate semantic obligation needed to catch the error. Then ask which results meet an informal-review policy and which meet a policy requiring actual Lean evidence. Missing formal execution must remain explicit.

Read with the [three running cases](/posts/2026/08/agent-system/research-cases/). Source provenance and the distinction between established patterns and our proposed specialization are explained in [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: validate meaning after validating fields

A record can contain every required field and still claim that an open interval is compact. Structural validation checks presence and format; mathematical review checks the argument and applicability. Store these as separate outcomes.

**Acceptance exercise.** Create one malformed but mathematically correct record and one well-formed but false record. A useful system distinguishes them and requests the appropriate repair instead of assigning one generic confidence score.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
