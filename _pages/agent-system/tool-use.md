---
title: "Agent Systems: Tool Use and Code Execution"
permalink: /posts/2026/08/agent-system/tool-use/
tags:
  - Agent System
---

## Intent

Expose external capabilities through a stable action–observation interface,
including deterministic mathematical computation.

## Outline

1. Recurring problem: language generation is not the right mechanism for deterministic operations or external state.
2. Structure: `agent → tool schema → capability → observation → agent`.
3. Stable interface: tool name, schema, arguments, return value, permissions, and error behavior.
4. Variable implementation: web service, database, calculator, proof assistant, code runner, or vault operation.
5. Code execution: use computation to test examples, evaluate expressions, or search a finite space; keep code and outputs as inspectable artifacts.
6. Strength: delegates deterministic operations to appropriate tools and makes observations available for verification.
7. Risks: unsafe actions, brittle schemas, side effects, and unvalidated observations.
8. Example: retrieve a theorem note, run a symbolic or Lean check, then return a structured report with provenance.

## Suggested figure

`06-tool-use.svg` in the Agent design pattern illustration folder.
