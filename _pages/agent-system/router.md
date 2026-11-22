---
title: "Route by the Evidence Required"
permalink: /posts/2026/08/agent-system/router/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/plan-and-execute/). Geometry references below refer to the optional extension of Case A.


In Case B, finding a compactness theorem, checking constant dependence, and justifying passage to a limit are different tasks. A router should inspect the unresolved obligation rather than route everything containing “analysis” to one specialist.

## The contract

A source handler returns a source and proposed match; a calculation handler returns inputs and interpreted output; a reviewer returns an assessment of an inference. Their shared envelope preserves different evidence kinds. Routing success is not proof success.

## Trade-offs and failure modes

Allow abstention when the obligation is underspecified. Record the routing reason and permit reassignment after new evidence. Classification is a search decision; rules, models, or researchers may implement it without changing its mathematical status.

## Build and test

Split “justify the limit” into topology, uniformity, compactness, and identification obligations. Specify the evidence that would close each one.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: route an unresolved estimate

Suppose a proof needs a bound independent of a parameter. If a cited theorem supplies the bound, route to source inspection with the exact parameter dependence as the question. If the theorem does not apply, route to a mathematical argument or counterexample search. Sending the same question to more literature workers does not repair a failed hypothesis.

**Acceptance exercise.** Require the result to name the missing estimate, its quantifiers, and the evidence needed to discharge it. Test an ambiguous request and check that the router asks for the missing domain instead of inventing one.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
