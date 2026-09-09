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

**In one sentence.** Fixing the words — model, agent, context, state, tool, memory, evaluator, checkpoint — so that later pages can argue about boundaries instead of about vocabulary.

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

## The prompt level

Below the pattern vocabulary sits a smaller one for a single inference, and it is
worth fixing separately because patterns are often applied to problems that a
better-specified call would have solved. Five principles cover it: give
direction, so the model knows the role and the goal; specify format, so the
output has a shape a downstream component can consume; provide examples, which
constrain behavior more reliably than description; evaluate quality, so that
"better" is measurable before anything is tuned; and divide labor, splitting a
task into steps each of which can be checked.

The last is the hinge between the two levels. Dividing labor across separate
inferences is where prompting ends and architecture begins, and every pattern in
Part II is a disciplined way of doing it.

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

The vocabulary is anchored in Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
the introduction and Chapter 1, and Dibia, [*Designing Multi-Agent Systems*](https://multiagentbook.com/),
Chapter 4. This figure
is an original teaching redraw: it synthesizes the vocabulary of the four
course books rather than reproducing one of their illustrations. Its main loop
can be compared with Figure 1 of Yao et al., *ReAct: Synergizing
Reasoning and Acting in Language Models*, where reasoning steps and external
actions are interleaved through observations: [paper](https://arxiv.org/abs/2210.03629)
and [Google Research overview](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/).

For the surrounding component vocabulary and orchestration boundaries, see
Victor Dibia's [official *Designing Multi-Agent Systems* book site](https://multiagentbook.com/).
The five prompt-level principles — give direction, specify format, provide
examples, evaluate quality, divide labor — are Chapter 1 of James Phoenix and
Mike Taylor, *Prompt Engineering for Generative AI*, O'Reilly, first edition,
May 2024, ISBN 978-1-098-15343-4.
The broader pattern catalogues are linked directly above and in the reference
basis at the end of each pattern page.
