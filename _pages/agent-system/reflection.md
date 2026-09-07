---
title: "Agent Systems: Reflection Pattern"
permalink: /posts/2026/08/agent-system/reflection/
tags:
  - Agent System
---

## Intent

Separate generation from critique and revision.

## Outline

1. Recurring problem: the first output is treated as final without an explicit quality check.
2. Structure: `draft → evaluator → accept or revise`.
3. Stable interface: evaluation criteria and revision instructions.
4. Variable implementation: generator, critic, and stopping rule.
5. Strength: makes quality criteria explicit.
6. Risks: shared blind spots, endless revision, and evaluation against the wrong metric.
7. Example: review a generated theorem digest for missing hypotheses and unsupported claims.

## Suggested figure

`05-reflection.svg` in the Agent design pattern illustration folder.
