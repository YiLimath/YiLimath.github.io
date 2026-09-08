---
title: "Agent Systems: Learning and Adaptation"
permalink: /posts/2026/08/agent-system/learning-and-adaptation/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Problem

An agent that repeats the same failed strategy wastes resources. Yet changing
the policy after every outcome can cause instability and erase useful behavior.

## Intent and structure

`trajectory → evaluate → extract lesson → update policy or memory → test again`

Adaptation can modify prompts, routing rules, retrieval indexes, tool selection,
memory, or a model. Keep the learned artifact separate from the run that
produced it and make its scope explicit.

## What counts as a lesson?

A useful lesson identifies the task condition, the attempted action, the result,
and the evidence that a different action is preferable. A failed proof attempt
may suggest a new decomposition; it does not establish that the alternative is
correct.

## Forces and failure modes

Adaptation improves performance on recurring tasks but risks overfitting,
catastrophic forgetting, and self-reinforcing errors. Use held-out evaluation
cases, rollback, versioned policies, and human approval for high-impact changes.

## Real-world application

A support router can learn from resolved tickets, but only after feedback is
validated and evaluated against a fixed test set. Versioned prompts, routing
policies, and memories let the team roll back a change that improves one queue
while damaging another.

## Reference basis

This page follows Antonio Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3), Chapter 9, “Learning and
Adaptation.” The online/offline separation, rollback, and fixed-evaluation
requirements are course engineering safeguards, not a claim that online
learning is automatically safe.

## Figure

![Learning and adaptation pattern](/images/agent-system/10-learning-adaptation.svg)

*Figure: course architecture redraw. Online traces feed an offline adaptation
plane; only a candidate that passes held-out evaluation enters the versioned
policy registry.*
