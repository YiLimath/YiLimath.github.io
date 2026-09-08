---
title: "Agent Systems: Guardrails and Safety"
permalink: /posts/2026/08/agent-system/guardrails-safety/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Guardrails and safety](/images/agent-system/20-guardrails-safety.svg)

*Figure: input, context, action, and output boundaries constrain the agent and provide escalation paths.*

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

## Real-world application

An agent that can send messages, change records, or execute code needs input,
context, action, and output controls. Permissions, validation, redaction,
sandboxing, and human approval should sit at explicit boundaries around the
capability, not only inside a system prompt.

## Reference basis

The source pattern is Gulli, *Agentic Design Patterns*, Chapter 18,
“Guardrails/Safety Patterns,” and Lakshmanan and Hapke, *Generative AI Design
Patterns*, Chapter 9, including Self-Check and Guardrails. Anthropic's
[Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents)
provides a current engineering discussion of human control, security, and
prompt-injection risk.
