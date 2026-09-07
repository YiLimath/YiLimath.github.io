---
title: "Agent Systems: Human-in-the-Loop Pattern"
permalink: /posts/2026/08/agent-system/human-in-the-loop/
tags:
  - Agent System
classes: agent-system-page
---

## Problem

Some decisions are high impact, ambiguous, irreversible, or not captured by an
automated evaluator. Full autonomy would hide responsibility rather than remove
the decision.

## Intent and structure

`agent work → checkpoint → human review or correction → resume, revise, or stop`

A checkpoint should present the artifact, evidence, uncertainty, available
choices, and consequences. “Human approval” is not useful if the reviewer cannot
see what is being approved.

## Where to place checkpoints

Use them before irreversible tool actions, after ambiguous routing, when a
quality evaluator disagrees, when the budget or stopping condition is reached,
or when a result is ready for publication. Routine low-risk work can remain
automated.

## Forces and failure modes

Human review improves accountability and handles open-ended judgment, but it
adds latency and can become a rubber stamp. Escalate selectively, explain why,
record the decision, and make resumption idempotent.

## Mathematical example

The system may propose a proof direction or a literature connection, while the
mathematician decides whether it is relevant, novel, or worth pursuing.

## Figure

![Human-in-the-loop pattern](/images/agent-system/11-human-in-loop.svg)

*Figure: the system pauses at an explicit checkpoint when human judgment is required.*
