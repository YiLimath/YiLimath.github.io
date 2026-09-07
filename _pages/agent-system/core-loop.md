---
title: "Agent Systems: The Core Loop"
permalink: /posts/2026/08/agent-system/core-loop/
tags:
  - Agent System
---

The core loop is the base abstraction from which the later patterns are built.

## Outline

1. **Perception:** observe, filter, and interpret the environment.
2. **Inference:** reason, plan, and choose the next action.
3. **Action:** call a tool, change state, or communicate with a user.
4. **Feedback:** feed the result back into the next iteration.
5. Explain why the loop is useful but not sufficient: the design problem is how to control state, branching, evaluation, and responsibility.

## Design question

Which part of the loop is flexible, and which boundary must be deterministic and testable?

## Suggested figure

`00-agent-system-overview.svg` in the Agent design pattern illustration folder.
