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

**In one sentence.** When the model is not underpowered but the representation is wrong, change the representation; chains and trees are the two shapes, and a tree pays only when partial work can be judged.

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

## Linear and branching reasoning

Two shapes cover most of what is used in practice. A **chain** decomposes the
problem into ordered steps and commits to each; it is cheap, and it fails when an
early commitment was wrong, since nothing revisits it. A **tree** maintains
several partial candidates, evaluates them against a heuristic, and expands or
abandons branches deliberately, which buys the ability to backtrack at the cost
of a search budget and an evaluation rule.

The choice is not a matter of sophistication. A tree is worth its cost only when
the problem admits a meaningful intermediate evaluation — when a partial solution
can be judged before it is complete. Where no such judgement exists, branching
multiplies cost while selecting essentially at random, and a chain with an
independent check afterwards is the better design.

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

This page synthesizes Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 17, with the reasoning and representation patterns in Lakshmanan and
Hapke, [*Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/),
Chapter 5, where chain-of-thought and tree-of-thoughts appear as Patterns 13 and
14. The two shapes have primary sources: Wei et al., [Chain-of-Thought Prompting
Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903),
and Yao et al., [Tree of Thoughts: Deliberate Problem Solving with Large Language
Models](https://arxiv.org/abs/2305.10601), which makes the state evaluator and
the search budget explicit components rather than prompting style. ReAct provides
a primary example of interleaving reasoning with information-gathering actions:
[paper](https://arxiv.org/abs/2210.03629).
