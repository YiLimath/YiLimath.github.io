---
title: "Agent Systems: Reflection Pattern"
permalink: /posts/2026/08/agent-system/reflection/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Reflection pattern](/images/agent-system/05-reflection.svg)

*Figure: a draft is evaluated and revised before it is passed onward.*

## Problem

A first draft can be fluent, incomplete, or subtly inconsistent. Asking for a
single answer does not create an independent quality check.

## Intent and structure

`draft → critique → targeted revision → re-evaluation`

The critic may be another model, a deterministic test, a tool, a proof checker,
or a human. Good reflection names the violated criterion and returns repairable
feedback rather than merely a numerical score.

## Separation of roles

The generator should optimize for proposing a useful candidate; the critic
should inspect it against explicit requirements. Using the same prompt and
context for both can preserve the same blind spot, so independence matters.

## Mathematical example

A proof critique checks definitions, hypotheses, quantifiers, theorem
applications, and hidden existence claims. The revised proof should preserve the
original claim while recording which gap was addressed.

## Forces and failure modes

Reflection catches local defects but adds latency and may lead to endless
rewriting. Limit revision rounds, retain the rejected draft, and stop when a
defined quality threshold or human checkpoint is reached.

## Real-world application

In code review or report production, a generator creates a candidate and an
independent checker compares it with explicit requirements. The checker should
return localized repair instructions, so the workflow can revise one defect and
retain the rejected version for audit.

## Reference basis

The source pattern is Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 4, and Lakshmanan and Hapke, [*Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/),
Pattern 18. The
feedback-and-refinement loop is studied directly in Madaan et al., [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651).
