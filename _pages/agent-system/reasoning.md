---
title: "Agent Systems: Reasoning and Representation Change"
permalink: /posts/2026/08/agent-system/reasoning/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

## Figure

![Reasoning and representation change](/images/agent-system/27-reasoning-representation.svg)

*Figure: a course architecture for changing representations when the current
view hides the next useful inference. Read it left to right; the dashed loop
means that a failed check triggers revision rather than a more confident claim.*

## Problem

Some tasks fail because the chosen representation hides the next obstruction,
not because the model needs a longer response.

## Intent and structure

`current representation → transform or decompose → candidate reasoning → check`

The system may use linear decomposition, multiple candidate paths, program-aided
reasoning, abstraction, analogy, or example generation. The output should be an
artifact or proof obligation, not an unbounded private monologue.

## Mathematical representation changes

- prose → definitions, claims, and hypotheses;
- geometric picture → invariant, diagram, or coordinate model;
- conjecture → examples and counterexample tests;
- proof idea → lemmas and dependency graph;
- symbolic expression → computer algebra or formal code.

## Forces and failure modes

More search can improve coverage but increases cost and distracts from the
obstruction. Tree-style exploration can explode; linear reasoning can miss a
branch. Use a budget, a verifier, and a criterion for changing representation.

## Design test

Which representation makes the next mathematical obstruction visible, and what
independent check can reject the resulting candidate?

## Real-world application

In root-cause analysis, the same incident can be represented as a timeline, a
dependency graph, and a set of competing hypotheses. Representation change is
valuable when one view hides a dependency; each proposed explanation still
needs tests or evidence before it is accepted.

## Reference basis

This page synthesizes Gulli, *Agentic Design Patterns*, Chapter 17, with the
reasoning and representation patterns in Lakshmanan and Hapke, *Generative AI
Design Patterns*, Chapter 5. ReAct provides a primary example of interleaving
reasoning with information-gathering actions: [paper](https://arxiv.org/abs/2210.03629).
