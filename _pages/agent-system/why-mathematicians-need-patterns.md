---
title: "Why Mathematicians Need Agent Design Patterns"
permalink: /posts/2026/08/agent-system/why-mathematicians-need-patterns/
tags:
  - Agent System
  - Mathematics
---

Mathematical research is a composition of activities: reading, retrieving,
constructing examples, forming conjectures, searching for proofs, checking
claims, and writing exposition. An agent becomes useful when each recurring
activity has an explicit boundary.

## Translation of design principles

- **Decomposition** becomes lemmas, proof obligations, or independent searches.
- **Abstraction** becomes definitions, contracts, and representations that hide
  irrelevant implementation details.
- **Composition** becomes a proof or research workflow whose artifacts can be
  passed from one stage to the next.
- **Encapsulation** keeps a tool, model, or retrieval method replaceable.
- **Validation** uses tests, counterexamples, proof assistants, source checks,
  or human review.

## Solver loop versus research loop

A solver loop aims at an answer. A research loop must also preserve failed paths,
expose uncertainty, compare alternatives, and decide whether a result is worth
developing. Design patterns help with this organization; they do not turn a
plausible language-model explanation into a proof.

## Quality criteria

For mathematical work, correctness is necessary but not sufficient. Relevance,
provenance, reproducibility, inspectability, and failure detectability are also
architectural requirements.

## Figure

![Design patterns translated into mathematical research](/images/agent-system/24-mathematics-design-patterns.svg)

*Figure: decomposition, abstraction, composition, and validation turn recurring research activities into explicit artifacts.*
