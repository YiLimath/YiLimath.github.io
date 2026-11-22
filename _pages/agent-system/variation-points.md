---
title: "Stable Contracts Under Changing Models"
permalink: /posts/2026/08/agent-system/variation-points/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/lean-formalization/). Geometry references below refer to the optional extension of Case A.


A stronger model may replace several workers or discover a shorter proof. It must still identify what was proved, from which premises, under which assumptions. These are the stable contracts; model selection and prompting are mechanisms behind them.

For theorem retrieval, the contract is a source locator, statement, hypotheses, and proposed object substitution. For review, it includes the exact argument version and evidence kind. Compatibility is semantic, not merely a matching response shape.

## Find a real axis of change

Name a plausible replacement and ask what callers must still be able to rely on. Keep method ranking separate from hypothesis matching; keep candidate generation separate from premise permissions; keep storage identity separate from display names.

Do not create an abstraction that conceals the distinction the caller needs. A universal `verify()` returning a Boolean hides parsing, testing, source matching, and kernel checking. A review envelope should name the check and its limits.

## Substitution has conditions

A formal checker, a model critic, and a human reader may share an interface without being interchangeable under every policy. Substituting one for another can require changing the permitted use of its output. Record that policy change rather than calling all outputs “verified.”

## Build and test

Replace the worker with a scripted response and retain the same version and admission checks. Then change the evidence policy to formal-only. Informal reports must not be admitted as formal evidence; a shared schema must not upgrade their assurance.

Read with the [three running cases](/posts/2026/08/agent-system/research-cases/). Source provenance and the distinction between established patterns and our proposed specialization are explained in [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
