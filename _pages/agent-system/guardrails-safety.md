---
title: "Agent Systems: Guardrails and Safety"
permalink: /posts/2026/08/agent-system/guardrails-safety/
tags:
  - Agent System
---

## Intent

Constrain inputs, outputs, context, and actions so that the system remains within its authority and quality requirements.

## Outline

1. Guard the input: reject irrelevant, malicious, or underspecified requests.
2. Guard the context: preserve source boundaries, permissions, and provenance.
3. Guard the output: validate schema, citations, hypotheses, and forbidden claims.
4. Guard tools: use least privilege, explicit approval, sandboxing, and audit logs.
5. Mathematical safety rules:
   - label conjectures as conjectures;
   - distinguish a search result from a verified theorem;
   - preserve unresolved gaps;
   - never silently alter a hypothesis.
6. Explain that guardrails reduce risk but do not establish mathematical truth by themselves.

## Design question

What is the worst plausible failure, and which boundary can detect it before it causes harm?

## Suggested figure

`20-guardrails-safety.svg` in the Agent design pattern illustration folder.
