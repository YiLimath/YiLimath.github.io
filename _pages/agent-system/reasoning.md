---
title: "Agent Systems: Reasoning and Representation Change"
permalink: /posts/2026/08/agent-system/reasoning/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
---

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

## Figure

![Reasoning and representation change](/images/agent-system/05-reflection.svg)

*Figure: a candidate representation is transformed, evaluated, and revised.*
