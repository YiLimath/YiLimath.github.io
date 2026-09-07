---
title: "Agent Systems: Router Pattern"
permalink: /posts/2026/08/agent-system/router/
tags:
  - Agent System
---

## Intent

Select the smallest capable specialist for each request.

## Outline

1. Recurring problem: a single agent receives tasks with different tools, formats, or standards of evidence.
2. Structure: `request → classifier → specialist → common response`.
3. Stable interface: the request and response contract.
4. Variable implementation: the classifier and specialist selected for the request.
5. Strength: separates classification from execution.
6. Risks: misclassification, routing drift, and policy complexity.
7. Example: route a proof-checking task to retrieval, calculation, or exposition support.

## Suggested figure

`03-router.svg` in the Agent design pattern illustration folder.
