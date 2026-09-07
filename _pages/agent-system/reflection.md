---
title: "Agent Systems: Reflection Pattern"
permalink: /posts/2026/08/agent-system/reflection/
tags:
  - Agent System
classes: agent-system-page
---

## Problem

A first draft can be fluent, incomplete, or subtly inconsistent. Asking for a
single answer does not create an independent quality check.

## Intent and structure

`draft → critique → targeted revision → re-evaluation`

The critic may be another model, a deterministic test, a tool, a proof checker,
or a human. Good reflection names the violated criterion and returns repairable
feedback rather than merely a numerical score.

## Separation of roles

The generator should optimize for proposing a useful candidate; the critic
should inspect it against explicit requirements. Using the same prompt and
context for both can preserve the same blind spot, so independence matters.

## Mathematical example

A proof critique checks definitions, hypotheses, quantifiers, theorem
applications, and hidden existence claims. The revised proof should preserve the
original claim while recording which gap was addressed.

## Forces and failure modes

Reflection catches local defects but adds latency and may lead to endless
rewriting. Limit revision rounds, retain the rejected draft, and stop when a
defined quality threshold or human checkpoint is reached.

## Figure

![Reflection pattern](/images/agent-system/05-reflection.svg)

*Figure: a draft is evaluated and revised before it is passed onward.*
