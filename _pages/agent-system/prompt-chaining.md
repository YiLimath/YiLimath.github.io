---
title: "Agent Systems: Prompt Chaining Pattern"
permalink: /posts/2026/08/agent-system/prompt-chaining/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Prompt chaining workflow](/images/agent-system/02-prompt-chaining.svg)

*Figure: specialized stages pass structured artifacts forward.*

## Problem

A single prompt must often perform incompatible jobs: interpret an input,
extract structure, reason, verify, and format a deliverable. The result is hard
to inspect and difficult to repair.

## Intent and structure

Prompt chaining divides the task into ordered stages:

`input → extraction → transformation → checking → presentation`

Each stage has a narrower responsibility and passes an intermediate artifact to
the next stage. The chain can use one model or different models.

## Stable interface

The interface is the intermediate artifact: its schema, required fields,
provenance, and error status. Natural-language instructions are implementation
details around that contract.

## When it helps

Use chaining when stages have clear dependencies, when intermediate errors need
to be localized, or when different stages require different models or tools. A
mathematical example is `paper → metadata → theorem statement → proof skeleton
→ checked exposition`.

## Forces and failure modes

Chaining improves observability and revision, but adds latency and can propagate
an early extraction error through every later stage. Validate high-value
artifacts before continuing; formatting success is not mathematical correctness.

## Real-world application

In an invoice or compliance workflow, one stage extracts fields, another
checks them against policy, and a final stage prepares a human-readable report.
Each stage can be replayed from its artifact when a supplier changes a field or
the policy is revised.

## Reference basis

This pattern follows Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 1, and Dibia, [*Designing Multi-Agent Systems*](https://multiagentbook.com/),
the explicit workflow treatment in Chapters 2
and 6. Anthropic gives an independent engineering description of prompt
chaining and its intermediate gates in [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
