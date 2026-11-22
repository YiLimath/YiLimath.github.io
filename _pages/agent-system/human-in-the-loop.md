---
title: "Agent Systems: Human-in-the-Loop Pattern"
permalink: /posts/2026/08/agent-system/human-in-the-loop/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/design-principles/).


A mathematical research system needs an explicit policy for changing its objective, spending its budget, accepting evidence, and releasing results. These responsibilities do not imply that a human must approve every action.

## Human proof checking need not be a permanent gate

For a fixed formal target, a proof-producing system can use mechanical validation as its acceptance gate. A human signature adds no missing proof term. The researcher may define the research objective and acceptance policy once, then delegate routine generation, checking, and admission without approving each lemma.

Specification design, interpretation, and research priorities can also receive increasing AI assistance. The point is to keep their authority and evidence visible, not to predict a permanent list of tasks machines cannot perform. Preserve the distinction between authorizing research and establishing a theorem. See the [automated admission exercise](/posts/2026/08/agent-system/lean-formalization/#8-build-an-admission-path-without-routine-human-proof-review).

## Control is an interface

Routine search, source checking, and bounded revision can proceed under delegated authority. Escalate when an action would change the agreed target or exceed that authority. A model can propose the decision; the policy determines who may authorize it.

For example, replacing pointwise convergence with uniform convergence may make a route work. The system should preserve the original task, create a separate strengthened statement, and explain what has and has not been achieved. It should not interrupt simply because a proof attempt failed.

## What a decision packet contains

Present the original target, the proposed change, the mathematical reason, supporting evidence, alternatives, and the work that can continue independently. Record the decision and its scope. Approval of further exploration is not approval of a theorem's correctness.

Humans can also miss errors. A signature does not replace the evidence contract. Conversely, increasingly capable agents may perform more of the design and review work; the need for explicit objectives, evidence, and authority remains.

## Hands-on practice

Write a decision packet for the open-interval example in the [introduction](/posts/2026/08/agent-system/design-principles/). Offer two distinct tasks: finish the refutation of the original conjecture, or study a repaired compact-domain theorem. Show that the first can finish without awaiting a preference about the second. Test that resuming the same decision twice does not duplicate work.

## Reference basis

Gulli, *Agentic Design Patterns*, Chapter 13, treats human involvement as a pattern. This page specializes the interface to mathematical scope changes and delegated research. It makes no claim that a particular cognitive task will remain exclusively human.

## Worked design decision: locate responsibility without predicting permanent limitations

The researcher chooses which question matters, what evidence justifies further investment, and what claim to publish. These are responsibilities of the research process, even when increasingly capable models assist with every decision. Do not base the architecture on a forecast that a specific task will always resist automation.

**Acceptance exercise.** At a decision point, present the exact options, supporting evidence, costs, and unresolved obligations. Ask for a substantive research choice rather than routine confirmation of every reversible step.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
