---
title: "Agent Systems: Memory Management Pattern"
permalink: /posts/2026/08/agent-system/memory-management/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Problem

Context windows are bounded, while tasks and histories are not. Copying every
past message into every step increases noise, cost, and the chance of retrieving
an obsolete instruction.

## Intent and structure

`experience → select → store → retrieve → current context`

The books distinguish short-term working context from long-term memory and from
external knowledge retrieval. A memory item needs content, scope, metadata,
provenance, and a retrieval policy.

## Memory operations

Write only information that may be useful later; retrieve by the current task;
compress or summarize under a stated policy; and expire or revise stale items.
Memory should preserve failed paths when those failures prevent repeated work.

## Mathematical design

Separate definitions and verified results from conjectures, heuristics, and
scratch reasoning. A retrieved lemma must still be checked against the current
hypotheses. Memory improves continuity; it is not a correctness certificate.

## Forces and failure modes

More memory improves recall but increases context pollution and retrieval bias.
Use scopes, provenance, ranking, limits, and explicit invalidation. Test whether
the system performs better with a memory item rather than assuming persistence
is always helpful.

## Real-world application

In case management, short-term conversation state and durable customer records
have different retention and access rules. A memory policy should decide what
to write, how to retrieve it, how to expire it, and how to correct a stale
record; storing every message is not a design.

## Reference basis

The pattern is Gulli, *Agentic Design Patterns*, Chapter 8, and Dibia,
*Designing Multi-Agent Systems*, Chapter 4, Sections 4.7 and 4.8. Long-term
memory and context management are also treated as application patterns by
Lakshmanan and Hapke in *Generative AI Design Patterns*, Chapter 8.

## Figure

![Memory management pattern](/images/agent-system/09-memory-management.svg)

*Figure: bounded working context is written to and recovered from longer-term memory.*
