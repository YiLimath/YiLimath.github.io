---
title: "Agent Systems: Goal Setting, Prioritization, and Termination"
permalink: /posts/2026/08/agent-system/goal-monitoring/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Goal setting, prioritization, and termination](/images/agent-system/17-goal-monitoring.svg)

*Figure: goals become operational through priorities, bounded actions, progress checks, and termination.*

## Problem

Autonomous execution can drift from the user's objective, spend resources on
low-value actions, or continue after meaningful progress has stopped.

## Intent and structure

`goal → milestones → prioritized action → progress check → continue, redirect, or stop`

A goal needs a success criterion, scope, budget, priority, dependencies, and
termination policy. Monitor artifacts and state transitions rather than
conversational confidence.

## Termination conditions

Stop when the goal is achieved, a quality threshold is met, the budget is
exhausted, no progress occurs after bounded attempts, or a human interrupts.
Distinguish semantic completion (“the agent says done”) from verified completion
(“the required artifact passed its checks”).

## Forces and failure modes

Aggressive stopping saves cost but can miss a solution; permissive stopping can
run indefinitely. Make the stopping decision observable and allow escalation or
replanning when the goal changes.

## Real-world application

For a long-running migration or investigation, a goal ledger records milestones,
dependencies, budget, and termination criteria. Monitoring can distinguish real
progress from repeated tool calls and stop or escalate when the goal becomes
infeasible.

## Reference basis

The source pattern is Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 11, “Goal Setting and Monitoring.” Dibia's orchestrator loop and
task-management
treatment appears in *Designing Multi-Agent Systems*, Chapters 2 and 7; the
task and progress ledgers are also explicit in the [Magentic-One technical report](https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Magentic-One.pdf).
