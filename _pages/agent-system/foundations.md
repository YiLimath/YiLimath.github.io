---
title: "Agent Systems: Terminology and Building Blocks"
permalink: /posts/2026/08/agent-system/foundations/
tags:
  - Agent System
---

This page defines the objects used throughout the series.

## Outline

1. Define *model*, *agent*, *prompt*, *context*, *state*, *tool*, *memory*, *evaluator*, and *human checkpoint*.
2. Distinguish a model from an agent system: a model produces an output; an agent system manages a loop, state, tools, and evaluation.
3. Introduce the basic contract:
   `input → context → inference → action → observation → updated state`.
4. Explain the design-pattern vocabulary: recurring problem, stable interface, variable implementation, forces, trade-offs, and failure modes.
5. Explain why a small interface is preferable to exposing every internal detail.

## Design question

What should remain stable when the model, tool, prompt, or memory implementation changes?

## Suggested figure

`01-building-blocks.svg` in the Agent design pattern illustration folder.
