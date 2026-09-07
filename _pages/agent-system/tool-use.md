---
title: "Agent Systems: Tool-Use Pattern"
permalink: /posts/2026/08/agent-system/tool-use/
tags:
  - Agent System
---

## Intent

Expose external capabilities through a stable action–observation interface.

## Outline

1. Recurring problem: language generation is not the right mechanism for deterministic operations or external state.
2. Structure: `agent → tool schema → external capability → observation → agent`.
3. Stable interface: tool name, schema, arguments, return value, and error behavior.
4. Variable implementation: web service, database, calculator, code runner, or vault operation.
5. Strength: delegates deterministic operations to appropriate tools.
6. Risks: unsafe actions, brittle schemas, and unvalidated observations.
7. Example: read and write structured notes through a vault interface.

## Suggested figure

`06-tool-use.svg` in the Agent design pattern illustration folder.
