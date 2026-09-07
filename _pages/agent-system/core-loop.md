---
title: "Agent Systems: The Core Loop"
permalink: /posts/2026/08/agent-system/core-loop/
tags:
  - Agent System
---

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

## Figure

![Agent system core control loop](/images/agent-system/00-agent-system-overview.svg)

*Figure: perception, inference, action, feedback, and control form the reusable execution loop.*
