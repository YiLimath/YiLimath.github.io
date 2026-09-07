---
title: "Agent Systems: Structured Output and Dependency Injection"
permalink: /posts/2026/08/agent-system/structured-output/
tags:
  - Agent System
---

## Intent

Make intermediate artifacts machine-readable and keep components replaceable through explicit interfaces.

## Outline

1. Recurring problem: free-form language is ambiguous at a workflow boundary.
2. Structure: `task → schema-constrained artifact → next component`.
3. Mathematical schemas:
   - theorem statement: objects, hypotheses, conclusion;
   - proof step: claim, dependencies, justification, status;
   - citation: source, location, extracted statement, provenance.
4. Dependency injection: supply the model, retriever, checker, or tool through an interface rather than embedding a concrete implementation everywhere.
5. Strength: parsing, testing, replacement, and auditing become possible.
6. Risks: a valid schema can still contain false mathematics; schema design can also become too rigid.

## Design question

What is the smallest artifact that the next stage can use without guessing?

## Suggested figure

`13-structured-output.svg` in the Agent design pattern illustration folder.
