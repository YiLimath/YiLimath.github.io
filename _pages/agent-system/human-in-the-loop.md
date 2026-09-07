---
title: "Agent Systems: Human-in-the-Loop Pattern"
permalink: /posts/2026/08/agent-system/human-in-the-loop/
tags:
  - Agent System
---

## Intent

Insert human judgment where the cost of an autonomous error is high or authority matters.

## Outline

1. Recurring problem: some decisions require responsibility, domain judgment, or explicit consent.
2. Structure: `proposal → review → approve, revise, or reject`.
3. Stable interface: evidence shown to the reviewer and the effect of each decision.
4. Variable implementation: notification, review form, conversation, or approval queue.
5. Strength: combines machine flexibility with human accountability.
6. Risks: bottlenecks, unclear authority, and approval fatigue.
7. Example: the researcher reviews a proposed schedule or a proof-checking report.

## Suggested figure

`11-human-in-loop.svg` in the Agent design pattern illustration folder.
