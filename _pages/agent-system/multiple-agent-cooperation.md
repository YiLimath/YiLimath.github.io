---
title: "Module 8. Divide work only when the evidence benefits"
permalink: /posts/2026/08/agent-system/multiple-agent-cooperation/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

Multiple workers are optional. The relevant question is whether dividing a mathematical task produces better evidence or saves useful time under comparable resources.

## A concrete division

For the section-lifting problem, one task can audit a proposed vanishing theorem while another computes the restriction image in an explicit example. Each task returns an artifact with a target version, assumptions, actual evidence, and remaining obligations.

| Task | Input | Required output |
|---|---|---|
| Source audit | Exact theorem and geometric objects | Hypothesis-by-hypothesis applicability table |
| Direct calculation | Specified section and restriction map | Calculation and proof of its implication |
| Merge | Both reports and current target | Applicable support, disagreements, and open obligations |

These tasks need not be different agents. Execute them sequentially first. Use separate conversations or Codex tasks only when the environment supports that arrangement and the comparison justifies it.

```text
Audit the supplied vanishing theorem for this target version.
Return the exact source, object substitution, hypothesis evidence, and gaps.
Do not treat an unavailable hypothesis as established.
```

For the calculation task, replace the source instruction with a request for the explicit restriction image and the fate of the specified section. Provide the same target version to both.

## The merge is a mathematical check

Two reports may concern different sections or twists. Compare their objects before comparing conclusions. Agreement is not a proof rule; disagreement may reveal different assumptions rather than contradictory mathematics.

Deliver an old report after changing the target. Require the merge to flag it and explain what can still be reused. Preserve the full report instead of silently overwriting it.

## Evaluate the extra work

Compare sequential and divided runs using the same source access and a total effort budget fixed in advance. Record elapsed time separately from total resource use: parallelism can reduce latency while increasing work. Count duplicate searches, invalid accepted arguments, and useful completed obligations.

## Acceptance

Submit both traces, a stale-report experiment, and a decision about whether division helped this task. Separate chats do not guarantee independent reasoning. If the simpler workflow performs as well at lower cost, retaining it is a successful design decision.

---

[Course roadmap](/posts/2026/12/Agent-System/) · [Direct experiments](/posts/2026/08/agent-system/hands-on-lab/) · [Next module](/posts/2026/08/agent-system/evaluation-monitoring/)
