---
title: "The Objects a Reasoning System Must Represent"
permalink: /posts/2026/08/agent-system/foundations/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

The basic unit is a statement with a scope, not a message. In Case A, “some nonzero section exists” and “this chosen section lifts” are different statements. Treating both as a task called “nonvanishing” destroys information before reasoning begins.

## Statements, arguments, and obligations

A **statement** records a proposition and its assumptions. An **argument** records a proposed justification of one statement from other statements. An **obligation** is a missing justification or applicability condition. **Evidence** records what was checked and by what method. An **admission policy** decides which evidence permits downstream use.

These objects remain meaningful whether a worker is a language model, symbolic program, proof assistant, or mathematician. An agent is an execution mechanism around them, not the mathematical unit of knowledge.

Separate mathematical state from operational state. A task can time out while its statement remains open. A review can finish with rejection. A statement can retain a valid argument after another argument is withdrawn.

## The smallest useful contract

| Record | Required distinction |
|---|---|
| Statement | Exact target, hypotheses, domain, version |
| Argument | Conclusion, jointly required premises, justification, source |
| Review | Exact artifact digest, evidence kind, report, reviewer |
| Task | Inputs, requested artifact, budget, execution outcome |

A structured schema preserves these fields but cannot establish that their mathematical content is correct. The workbench intentionally accepts supplied reviews; it is not a proof assistant.

## Build and test

Create separate records for lifting the section (1,0) on the two-point divisor and for finding any nonzero section upstairs. Explain why the former fails while the latter succeeds. Then run the workbench's wrong-mathematics fixture: identify the trusted input that lets a false statement pass its policy.

**Design takeaway:** represent the distinctions that an argument must preserve before choosing the agents that will manipulate them.

Read with the [three running cases](/posts/2026/08/agent-system/research-cases/). Source provenance and the distinction between established patterns and our proposed specialization are explained in [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

---

[Series guide](/posts/2026/08/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
