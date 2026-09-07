---
title: "Agent Systems: Plan-and-Execute Pattern"
permalink: /posts/2026/08/agent-system/plan-and-execute/
tags:
  - Agent System
---

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

## Figure

![Plan and execute pattern](/images/agent-system/08-plan.svg)

*Figure: planning separates high-level decomposition from execution and revision.*
