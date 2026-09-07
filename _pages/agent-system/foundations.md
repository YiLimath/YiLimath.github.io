---
title: "Agent Systems: Terminology and Atomic Building Blocks"
permalink: /posts/2026/08/agent-system/foundations/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

This page fixes the vocabulary used by the rest of the course. The books use
different names for similar components, but the design question is the same:
which boundary should remain stable when the model or implementation changes?

## The basic objects

- A **model** maps a prompt and context to a candidate output.
- An **agent** adds a loop, state, tools, and a policy for choosing the next
  action.
- **Context** is the bounded information supplied to one inference step.
- **State** is the information that persists between steps.
- A **tool** is an external capability with a callable interface and an
  observation returned to the agent.
- **Memory** stores selected past information for later retrieval.
- An **evaluator** tests an artifact or a trajectory against a criterion.
- A **checkpoint** transfers responsibility to a human or another component.

## Pattern anatomy

For every pattern, identify the recurring problem, intent, participants, stable
interface, variable implementation, forces, failure modes, and composition with
other patterns. This prevents a framework feature from being mistaken for a
design principle.

## Atomic contract

`input → context → inference → action → observation → state update`

The contract is deliberately small. Structured artifacts, tool schemas,
messages, state records, and evaluation reports are more important than a
particular model name.

## Design test

If replacing the model requires rewriting every downstream component, the system
has exposed an implementation instead of an interface.

## Figure

![Agent system building blocks](/images/agent-system/01-building-blocks.svg)

*Figure: the basic objects and interfaces used throughout the series.*
