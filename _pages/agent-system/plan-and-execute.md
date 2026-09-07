---
title: "Agent Systems: Plan-and-Execute Pattern"
permalink: /posts/2026/08/agent-system/plan-and-execute/
tags:
  - Agent System
---

## Intent

Turn a long-horizon goal into steps with explicit checkpoints.

## Outline

1. Recurring problem: a long task is too large to execute as one undifferentiated action.
2. Structure: `goal → plan → execute steps → verify → revise plan`.
3. Stable interface: goal, step status, and verification result.
4. Variable implementation: the planner and the executor for each step.
5. Strength: makes dependencies and progress visible.
6. Risks: stale plans, premature commitment, and false progress.
7. Example: daily research scheduling from recent work to a human-adjusted daily assignment.

## Suggested figure

`08-plan.svg` in the Agent design pattern illustration folder.
