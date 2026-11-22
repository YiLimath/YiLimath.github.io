---
title: "Module 7. Recover evidence and assumptions, not just a summary"
permalink: /posts/2026/08/agent-system/memory-management/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

A checkpoint is useful when another research session can reconstruct what is supported and why. A fluent summary that drops conditional assumptions is a mathematical regression.

## A withdrawal trace

Consider two arguments for target T: argument A uses premise P; argument B uses premise Q. For this protocol exercise, stipulate that both implications are valid. Label that input as stipulated rather than pretending a theorem was proved.

| State | Available support | Status of T |
|---|---|---|
| P and Q established | A and B | Supported by either route |
| P withdrawn, Q established | B | Still supported |
| Both withdrawn | Neither route | Unresolved, not refuted |
| Q only assumed | B conditional on Q | Conditional on Q |

This explicit trace is more useful than a generic memory diagram: it specifies the state changes the workflow must reproduce.

## What the checkpoint contains

Record the exact target version, established facts with arguments, assumptions, surviving alternatives, withdrawn evidence and reasons, unresolved obligations, source locations, and the next action. Keep the full proof artifacts available; a checkpoint can link to them rather than compressing their mathematics into a confidence score.

```text
Write CHECKPOINT.md sufficient to resume without this conversation.
List each conclusion with its supporting argument and remaining assumptions.
Preserve withdrawn routes and why they were withdrawn.
Do not interpret a timeout as a counterexample or a failed search as nonexistence.
```

Start a fresh conversation with only the saved files and ask it to reconstruct the state before doing more work. Compare the result with the table and original artifacts. If an assumption disappears, record a failed recovery even if the assistant produces an attractive next plan.

## Research use

Remember that (1,0) fails to lift in the two-point example. Do not compress this into “there are no global sections”: constants provide global sections. Store the failed implication with its objects and scope.

## Acceptance

Submit the withdrawal trace, exported checkpoint, fresh-session reconstruction, and a comparison of target, dependencies, and assumptions. File persistence proves that text survived; the comparison tests whether the mathematical state survived interpretation.

---

[Course roadmap](/posts/2026/12/Agent-System/) · [Direct experiments](/posts/2026/08/agent-system/hands-on-lab/) · [Next module](/posts/2026/08/agent-system/multiple-agent-cooperation/)
