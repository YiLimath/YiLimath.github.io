---
title: "Agent Systems: The Core Loop"
permalink: /posts/2026/08/agent-system/core-loop/
tags:
  - Agent System
---

The core loop is the base abstraction from which the later patterns are built.
It is useful to distinguish an execution loop from a research loop: the former
decides the next system action, while the latter also records evidence,
uncertainty, and a stopping decision.

## Outline

1. **Perception:** observe, filter, and interpret the environment.
2. **Inference:** reason, plan, and choose the next action.
3. **Action:** call a tool, change state, or communicate with a user.
4. **Feedback:** validate the observation and feed it into the next iteration.
5. **Control:** check the goal, budget, termination condition, and escalation policy.
6. Explain why the loop is useful but not sufficient: the design problem is how to control state, branching, evaluation, and responsibility.

## Design question

Which part of the loop is flexible, and which boundary must be deterministic,
observable, and testable?

## Suggested figure

`00-agent-system-overview.svg` in the Agent design pattern illustration folder.
