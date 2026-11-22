---
title: "Stage a Theorem Application"
permalink: /posts/2026/08/agent-system/prompt-chaining/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/knowledge-retrieval/). Geometry references below refer to the optional extension of Case A.


A theorem application has natural stages: retrieve, transcribe, instantiate, check hypotheses, and derive the requested conclusion. In Case A, a result about a nearby sheaf is not a result about the group needed by the lifting sequence.

## The contract

Each stage consumes versioned artifacts and returns its promised artifact or an obstruction. Preserve the source statement beside the extraction. The matching stage must supply evidence for positivity or retain it as open; the presentation stage cannot erase that condition.

## Trade-offs and failure modes

Chaining localizes errors but can amplify an early transcription mistake. Audit the weakest boundary. When the stages require revision, represent the feedback explicitly instead of forcing a one-way pipeline. A chain is an implementation of mathematical interfaces, not a reason to divide every task into more prompts.

## Build and test

Construct a source statement, hypothesis matrix, and conditional lifting argument. Leave positivity unresolved and confirm that no stage silently promotes it to a premise.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
