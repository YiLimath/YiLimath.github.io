---
title: "Agent Systems: Plan-and-Execute Pattern"
permalink: /posts/2026/08/agent-system/plan-and-execute/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Plan and execute pattern](/images/agent-system/08-plan.svg)

*Figure: planning separates high-level decomposition from execution and revision.*

## Problem

Long-horizon tasks fail when the agent treats the whole objective as one
undifferentiated generation step. Dependencies and progress become invisible.

## Intent and structure

`goal → plan → execute step → checkpoint → revise or continue`

The planner decomposes the goal; the executor performs one bounded step; an
evaluator decides whether the plan remains valid. Planning and execution may use
different models or systems.

## Stable interface

Each step needs an identifier, preconditions, expected artifact, status, and
verification result. A plan is not evidence of progress until its artifacts
exist and have been checked.

## Mathematical example

A proof search plan might separate notation, prerequisite lemmas, candidate
constructions, and final assembly. If a prerequisite fails, revise the plan
instead of continuing to execute obsolete steps.

## Forces and failure modes

Planning improves coordination and resumability, but plans can be stale,
overly detailed, or prematurely committed. Persist checkpoints, permit
replanning, and define a stopping rule before expensive execution.

## Real-world application

A software maintenance agent can turn an issue into a bounded plan, execute the
steps in a sandbox, run tests, and send the diff for review. The plan is useful
because the system can resume or repair one failed step without repeating the
whole task blindly.

## Reference basis

The planning pattern is Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 6. Dibia discusses explicit and implicit planning in [*Designing
Multi-Agent Systems*](https://multiagentbook.com/),
Chapter 5, and persistent workflow execution in Chapter 6. A published
architecture with planning, progress ledgers, and re-planning is documented in
the [Magentic-One technical report](https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Magentic-One.pdf).
