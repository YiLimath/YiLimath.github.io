---
title: "Agent Systems: Tool Use and Code Execution"
permalink: /posts/2026/08/agent-system/tool-use/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Problem

Language generation is not the right mechanism for deterministic operations,
external state, or exact computation. The agent needs a controlled way to act
and to receive an observation.

## Intent and structure

`agent → tool schema → capability → observation → agent`

Function calling, MCP-style tool protocols, HTTP services, databases, code
runners, and proof assistants are implementations of this boundary. The stable
part is the tool name, input schema, permissions, return schema, and error
behavior.

## Code execution

Use code for exact arithmetic, symbolic experiments, finite searches, plots, or
formal proof checking. Keep the program, environment, and output as inspectable
artifacts. A successful execution is evidence about the computation, not
automatically a proof of the surrounding theorem.

## Safety and reliability

Use least privilege, validate arguments, control side effects, set timeouts,
make writes idempotent where possible, and distinguish a tool error from a
negative mathematical result. An observation must be checked before it changes
the next state.

## Example

The Rethlas generation agent exposes theorem search and proof verification as
explicit tools; Danus adds a role-gated gateway so different agents see
different capabilities.

## Figure

![Tool use and code execution](/images/agent-system/06-tool-use.svg)

*Figure: the agent acts through typed tool interfaces and receives explicit observations.*
