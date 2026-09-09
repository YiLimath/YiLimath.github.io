---
title: "Agent Systems: Structured Output and Dependency Injection"
permalink: /posts/2026/08/agent-system/structured-output/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Structured output pattern](/images/agent-system/13-structured-output.svg)

*Figure: a schema boundary makes intermediate artifacts parseable without claiming that they are true.*

**In one sentence.** Fix the shape of whatever crosses a boundary, so the next component can consume it instead of interpreting prose.

## Problem

Free-form language is ambiguous at a workflow boundary. A downstream component
should not have to guess whether a sentence is a claim, an error, a citation,
or a request for another action.

## Intent and structure

`task → schema-constrained artifact → parser/validator → next component`

The schema can constrain fields, types, enumerated statuses, or a grammar. It
does not make the content true; it makes missing or malformed content visible.

## Mathematical artifacts

A theorem record can contain objects, hypotheses, conclusion, source, and
status. A proof-step record can contain claim, dependencies, justification,
verification status, and repair hints. A citation record can contain source,
location, extracted statement, and provenance.

## Dependency injection

Pass the model, retriever, checker, or tool into a component through an
interface. The component then depends on a capability, not on one concrete
implementation. This permits offline tests, model replacement, and controlled
experiments.

## Forces and failure modes

Schemas improve parsing, testing, and auditing, but overly rigid schemas can
discard useful uncertainty. Validate both syntax and semantics, and preserve an
explicit `unknown`, `incomplete`, or `needs_review` status.

## Real-world application

An underwriting or compliance service can require every model response to be a
record containing decision, evidence, uncertainty, and next action. The parser
can reject malformed records before they reach a policy engine, while a valid
record still remains subject to semantic review.

## Reference basis

The interface-first treatment follows Dibia, [*Designing Multi-Agent
Systems*](https://multiagentbook.com/), Chapter 4, Section 4.5, “Enabling
Structured Output,” together with Lakshmanan and Hapke, [*Generative AI Design
Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/),
the constrained generation patterns in Chapters 1 and 2. The page treats
schema validity and truth as separate checks, as required by both sources.
