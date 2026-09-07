---
title: "Agent Systems: Guardrails and Safety"
permalink: /posts/2026/08/agent-system/guardrails-safety/
tags:
  - Agent System
---

## Problem

An agent can receive malicious or ambiguous input, retrieve untrusted context,
call an overpowered tool, or produce an unsafe and unjustified output. A single
system prompt is not a sufficient control boundary.

## Four boundaries

1. **Input:** scope, validate, sanitize, and reject irrelevant requests.
2. **Context:** enforce source boundaries, permissions, provenance, and limits.
3. **Action:** use least privilege, approvals, sandboxing, and audit logs.
4. **Output:** validate schema, citations, claims, uncertainty, and policy.

## Mathematical safety

Label conjectures as conjectures; distinguish search results from verified
theorems; preserve unresolved gaps; and never silently alter a hypothesis. A
guardrail reduces risk but does not establish mathematical truth.

## Forces and failure modes

Strict controls can block useful work; weak controls can make failures invisible.
Design an explicit escalation path, test adversarial and edge cases, and make
blocked actions observable so that safety does not become silent failure.

## Figure

![Guardrails and safety](/images/agent-system/20-guardrails-safety.svg)

*Figure: input, context, action, and output boundaries constrain the agent and provide escalation paths.*
