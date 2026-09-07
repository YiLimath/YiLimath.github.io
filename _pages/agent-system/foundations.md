---
title: "Agent Systems: Terminology and Building Blocks"
permalink: /posts/2026/08/agent-system/foundations/
tags:
  - Agent System
---

This page defines the objects used throughout the series. The reference books use
slightly different vocabularies, so the series separates the mathematical idea
of a reusable pattern from any particular framework.

## Outline

1. Define *model*, *agent*, *prompt*, *context*, *state*, *tool*, *memory*, *evaluator*, and *human checkpoint*.
2. Distinguish a model from an agent system: a model produces an output; an agent system manages a loop, state, tools, and evaluation.
3. Introduce the atomic unit used by later pages: a typed input, a bounded context, an inference step, an action, an observation, and an updated state.
4. Introduce the basic contract:
   `input → context → inference → action → observation → updated state`.
5. Explain the design-pattern vocabulary: recurring problem, stable interface, variable implementation, forces, trade-offs, and failure modes.
6. Explain why structured outputs, dependency injection, and small interfaces make components replaceable and testable.

## Design question

What should remain stable when the model, tool, prompt, retriever, or memory implementation changes?

## Suggested figure

`01-building-blocks.svg` in the Agent design pattern illustration folder.
