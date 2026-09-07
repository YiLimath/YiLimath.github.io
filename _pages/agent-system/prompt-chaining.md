---
title: "Agent Systems: Prompt Chaining Pattern"
permalink: /posts/2026/08/agent-system/prompt-chaining/
tags:
  - Agent System
---

## Intent

Replace one vague prompt with a sequence of explicit, testable transformations.

## Outline

1. Recurring problem: one prompt mixes extraction, reasoning, transformation, and presentation.
2. Structure: `input → extract → transform → reason → compose`.
3. Stable interface: each stage consumes a defined input and returns a defined output.
4. Variable implementation: the prompt, model, or tool used inside a stage.
5. Strength: inspectable intermediate results and local error handling.
6. Risks: latency, cost, and error propagation.
7. Example: paper → metadata → outline → theorem notes → proof notes.

## Suggested figure

`02-prompt-chaining.svg` in the Agent design pattern illustration folder.
