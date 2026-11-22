---
title: "Agent Systems: Tool Use and Code Execution"
permalink: /posts/2026/08/agent-system/tool-use/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**In one sentence.** Act through typed interfaces that return explicit observations, so side effects are authorized and checkable rather than asserted.

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

## Mathematical system design: bind observations to the question actually computed

Record exact inputs, arithmetic mode, software version, and the translation from mathematical objects to code.

### Hands-on practice

Compare floating-point samples of f(x)=x with the exact witness argument. State precisely what each output establishes.

**Deliverable.** Save the input, intermediate artifacts, expected outcome, and actual outcome. Include one negative case that the system must reject. Use the [runnable ledger lab](/posts/2026/08/agent-system/hands-on-lab/) as a starting point; do not treat its bookkeeping checks as a proof checker.

## Reference basis

The tool-use pattern is Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 5, and Lakshmanan and Hapke, [*Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/),
where tool calling and code execution are Patterns 21 and 22. The
reasoning/action interface is exemplified by the [ReAct paper](https://arxiv.org/abs/2210.03629);
standardized access to external data and tools is specified by the [MCP specification](https://modelcontextprotocol.io/specification).
Function calling as an implementation, and its parallel form, are treated
practically in James Phoenix and Mike Taylor, *Prompt Engineering for Generative
AI*, O'Reilly, 2024, Chapter 4. For the packaging of tools and instructions as
named, loadable capabilities — so that a capability's detail enters context only
when it is needed — see Stephen Clear, *Claude AI Bible*, Chapters 14 and 16.

---

[Series guide](/posts/2026/08/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
