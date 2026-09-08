---
title: "Agent Systems: Inter-Agent Communication and Protocols"
permalink: /posts/2026/08/agent-system/inter-agent-communication/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Inter-agent communication and protocols](/images/agent-system/21-inter-agent-communication.svg)

*Figure: independent agents coordinate through explicit task, evidence, status, and error messages.*

## Problem

Agents have different context, assumptions, tools, and lifetimes. An implicit
shared conversation does not provide a reliable coordination contract.

## Message contract

`sender · recipient · task id · artifact · provenance · status · requested action`

Mathematical messages should carry hypotheses, dependencies, uncertainty, and
unresolved obligations, not only conclusions. Version or identify artifacts so
that a later message cannot silently refer to changed content.

## Protocol versus orchestration

Orchestration decides who acts next and when the task ends. A protocol specifies
what is transferred between components. Tool protocols such as MCP and agent-
to-agent protocols are useful because they make the seam explicit.

## Forces and failure modes

Protocols support independent deployment and replacement, but add serialization,
schema evolution, and failure handling. Guard against inconsistent state,
duplicated work, unbounded message histories, and messages that omit assumptions.

## Design test

Could a new agent reconstruct the claim, its assumptions, evidence, and next
action from the message alone?

## Real-world application

In a multi-team service desk, agents should exchange task IDs, status, evidence,
and error types rather than free-form dialogue. A versioned message protocol
allows one worker to be replaced, retried, or audited without changing every
other worker.

## Reference basis

The pattern is Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 15, “Inter-Agent Communication (A2A),” and Dibia, [*Designing Multi-Agent
Systems*](https://multiagentbook.com/), Chapter 12,
“Protocols for Distributed Agents.” The [MCP specification](https://modelcontextprotocol.io/specification)
is a primary protocol reference for standardized access to tools and data; it
is complementary to agent-to-agent messaging.
