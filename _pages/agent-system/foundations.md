---
title: "Agent Systems: Terminology and Atomic Building Blocks"
permalink: /posts/2026/08/agent-system/foundations/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Agent system building blocks](/images/agent-system/01-building-blocks.svg)

*Figure: the basic objects and interfaces used throughout the series.*

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

## Real-world application

In a production request, these objects appear as concrete boundaries: an API
request becomes bounded context, the model proposes an action, a tool returns
an observation, and an evaluator or policy decides whether state may change.
The building blocks are useful because each boundary can be logged and tested
independently.

## Reference diagrams and sources

The vocabulary is anchored in Gulli, *Agentic Design Patterns*, the introduction
and Chapter 1, and Dibia, *Designing Multi-Agent Systems*, Chapter 4. This figure
is an original teaching redraw: it synthesizes the vocabulary of the four
course books rather than reproducing one of their illustrations. Its main loop
can be compared with Figure 1 of Yao et al., *ReAct: Synergizing
Reasoning and Acting in Language Models*, where reasoning steps and external
actions are interleaved through observations: [paper](https://arxiv.org/abs/2210.03629)
and [Google Research overview](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/).

For the surrounding component vocabulary and orchestration boundaries, see
Victor Dibia's [official *Designing Multi-Agent Systems* book site](https://multiagentbook.com/).
The broader pattern catalogues used in this course are listed with publisher
and author links on the [reference map](/posts/2026/08/agent-system/reference-map/).
