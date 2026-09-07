---
title: "Why Mathematicians Need Agent Design Patterns"
permalink: /posts/2026/08/agent-system/why-mathematicians-need-patterns/
tags:
  - Agent System
  - Mathematics
---

## Central claim

Mathematical research is not one task. It is a composition of reading, retrieval, example construction, conjecture formation, proof search, computation, exposition, and review. An agent design pattern gives each recurring activity a stable boundary.

## Outline

1. Map software design principles to mathematical practice:
   - decomposition → lemmas and subtasks;
   - abstraction → definitions and interfaces;
   - composition → proof and research workflows;
   - encapsulation → hiding implementation details behind statements;
   - validation → proof checking and counterexample search.
2. Explain the difference between a solver loop and a research loop.
3. Show how patterns reduce cognitive load without replacing mathematical judgment.
4. State the risks of over-automation: false confidence, context pollution, untraceable claims, and premature abstraction.
5. Introduce the research-specific quality criteria: correctness, relevance, provenance, reproducibility, inspectability, and failure detectability.

## Research loop

`question → examples → conjecture → counterexample search → lemma decomposition → proof attempt → verification → exposition`

## Design question

Which parts of this loop can be delegated, and which parts require the mathematician's judgment?
