---
title: "Parallel Search Needs a Mathematical Merge Rule"
permalink: /posts/2026/08/agent-system/parallelization/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/multiple-agent-cooperation/).


Case A has alternative construction and compatibility-checking routes. Within either route, its setup and hypotheses are jointly necessary. Concurrency changes execution time, not this logical structure.

## The contract

Preserve each branch as an argument with its own premises. One complete route can suffice; two incomplete routes do not become complete by agreeing. A common false setup can contaminate every branch, so record shared dependencies before interpreting agreement.

## Trade-offs and failure modes

Separate execution is not statistical independence. Compare parallel work with a sequential baseline under the same total budget. Cancel redundant work when a sufficient route closes unless another route has independent mathematical value, and retain useful evidence from cancelled branches.

## Build and test

Withdraw the candidate-construction evidence in the workbench: the direct route must survive. Withdraw the common setup: both routes must stop supporting the conclusion.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: parallelize alternatives, not dependent conclusions

Two methods may independently attack the same lemma. They cannot independently declare downstream lemmas proved while their shared premise remains unresolved. Give each branch the same frozen target and source packet; preserve incompatible assumptions in separate branches.

**Acceptance exercise.** Compare elapsed time and usable mathematical evidence with a serial run under the same total effort. Include a case in which both branches repeat the same invalid premise; two copies must not count as corroboration.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
