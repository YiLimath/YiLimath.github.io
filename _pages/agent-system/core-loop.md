---
title: "Agent Systems: The Core Loop"
permalink: /posts/2026/08/agent-system/core-loop/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Agent system core control loop](/images/agent-system/00-agent-system-overview.svg)

*Figure: course architecture redraw. Read the center from left to right: the
execution cycle is surrounded by goal and termination policy, context and
memory, action policy, trace and evaluation, and bounded tools. The control
gate decides whether another action is justified.*

**In one sentence.** Perceive, infer, act, observe, control: the five stages every agent shares, and the question of which one is allowed to be probabilistic.

The core loop is the common denominator behind workflow agents and autonomous
agents. It should be treated as an execution abstraction, not as an excuse for
unbounded improvisation.

## Five stages

1. **Perceive:** collect and filter the current observation.
2. **Infer:** select a response, plan, or next action.
3. **Act:** call a tool, emit an artifact, update state, or communicate.
4. **Observe:** validate the result and record errors as data.
5. **Control:** check goal progress, budget, permissions, and termination.

## Workflow versus autonomy

In an explicit workflow, the next node is chosen by a predefined graph. In an
autonomous loop, the model chooses more of the next action. The multi-agent
architecture literature treats this as a spectrum, not a binary distinction.
Keep high-risk transitions explicit even when local reasoning remains flexible.

## What belongs in the trace?

Record the input, selected context, action, tool result, evaluator result, and
state transition. A final answer without this trajectory cannot distinguish a
correct result from a lucky or irreproducible one.

## Design test

Which step is allowed to be probabilistic, and which boundary must be
deterministic, observable, and testable?

## Real-world application

Consider an operations agent diagnosing a failed service. It reads a metric,
forms a hypothesis, runs a read-only command, observes the result, and either
tries a bounded next step or escalates. The loop is real only when those
observations and control decisions are retained as an operational trace.

## Reference basis

The five-stage loop is the introductory agent loop in Antonio Gulli,
[*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
and the execution-loop treatment in Victor Dibia,
[*Designing Multi-Agent Systems*](https://multiagentbook.com/), Chapter 4,
Section 4.2. ReAct gives a primary research example of interleaving reasoning,
actions, and observations: [paper](https://arxiv.org/abs/2210.03629).
