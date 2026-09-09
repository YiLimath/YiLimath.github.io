---
title: "Agent Systems: Memory Management Pattern"
permalink: /posts/2026/08/agent-system/memory-management/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Memory management pattern](/images/agent-system/09-memory-management.svg)

*Figure: bounded working context is written to and recovered from longer-term memory.*

**In one sentence.** Decide what survives beyond the current task and under what policy; storing every message is not a design.

## Problem

Context windows are bounded, while tasks and histories are not. Copying every
past message into every step increases noise, cost, and the chance of retrieving
an obsolete instruction.

## Intent and structure

`experience → select → store → retrieve → current context`

The books distinguish short-term working context from long-term memory and from
external knowledge retrieval. A memory item needs content, scope, metadata,
provenance, and a retrieval policy.

Memory is the persistence question: what survives beyond this task, and under
what policy. It is distinct from deciding what enters a particular inference
window, which is treated separately under
[context engineering](/posts/2026/08/agent-system/context-engineering/). The two
meet at retrieval — memory decides what may be recalled, context engineering
decides what is actually admitted and at what priority.

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

The pattern is Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 8, and Dibia, [*Designing Multi-Agent Systems*](https://multiagentbook.com/),
Chapter 4, Sections 4.7 and 4.8, which distinguish application-managed retrieval
from agent-managed memory in which the agent explicitly creates and deletes its
own records. Long-term memory is Pattern 28 in Lakshmanan and Hapke,
[*Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/).
The treatment of a bounded window as a managed resource with paging between
tiers, by analogy with virtual memory, is Packer et al., [MemGPT: Towards LLMs as
Operating Systems](https://arxiv.org/abs/2310.08560).
