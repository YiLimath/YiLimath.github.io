---
title: "Agent Systems: Context Engineering"
permalink: /posts/2026/08/agent-system/context-engineering/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Context engineering](/images/agent-system/31-context-engineering.svg)

*Figure: candidate context is assembled under an explicit policy before it
reaches a bounded window. The dashed return is the reason the policy is needed:
every step appends new material.*

**In one sentence.** Prompt engineering asks what to say in one call; context
engineering asks what the model is allowed to see across many, and it is an
architecture question rather than a wording question.

## Problem

An agent's context does not stay the size it started. Each tool call adds
arguments, results, and error messages; each retrieval injects documents; each
turn appends history. The window, meanwhile, is fixed. Two distinct failures
follow, and they are often confused.

**Context explosion** is the quantitative failure: accumulated material exceeds
the budget and the call is rejected or truncated arbitrarily.

**Context rot** is the qualitative failure, and it is the dangerous one.
Recall accuracy degrades as token count rises, with measurable degradation well
before the advertised limit — around 32K tokens in reported studies. Attention
is a finite resource distributed across all pairwise relations between tokens,
so every additional token dilutes it. The consequence is that an agent which
works on a five-step task begins to hallucinate at step eight of a ten-step
task. Nothing announces this. The model did not change; the instructions were
simply pushed out of effective attention by accumulated tool output.

An agent without a context policy therefore fails silently, and fails later
rather than sooner, which makes the failure hard to attribute.

## Intent and structure

`candidate material → selection policy → bounded window → inference`

The stable interface is the *policy*, not the prompt. It must answer four
questions explicitly: what is eligible to enter, in what priority order, what is
compressed or dropped when the budget binds, and what never leaves the window
under any pressure.

## Four management strategies

| Strategy | Mechanism | What it costs |
|---|---|---|
| **Compaction** | Trim to a token budget, preserving head and tail | Detail in the middle; too aggressive and the agent re-reads work it already did |
| **Context isolation** | Delegate to a sub-agent that returns only a summary | The coordinator cannot see the specialist's reasoning |
| **Active memory management** | The agent explicitly writes, organizes, and deletes durable notes | Requires the agent to judge relevance correctly |
| **Tool-result filtering** | Summarize or aggregate large outputs before they enter context | An aggregate may discard the row that mattered |

Compaction that keeps a head and a tail is the common default: the head
preserves *what the agent is doing* — the system instructions and the original
task — while the tail preserves *where it left off*. One constraint is
structural rather than stylistic: a tool-calling message and its result form an
atomic pair and must never be split, or the request becomes malformed.

Isolation deserves particular attention because it is architectural rather than
reactive. A specialist agent may consume thirty thousand tokens internally and
return a two-hundred-token summary; the coordinator's context grows by the
summary alone. Measured on one multi-step research task, an unmanaged run used
21,633 tokens, compaction reduced this to 7,276, and isolation to 5,892 — a
reduction achieved by *design* rather than by trimming after the fact.

## Stable interface

Record, for each inference: the token budget, what was admitted and at what
priority, what was compressed or dropped, and which items were pinned. A context
policy that cannot be inspected after a failure cannot be debugged, because the
input that produced the output no longer exists anywhere.

## Mathematical application

The distinction between admitting a source and admitting a claim matters more in
mathematics than elsewhere. Pin the statement being proved, the notation
conventions, and the hypotheses in force; these must survive every compaction,
because a proof that drifts off its own hypotheses is worse than a proof that
stops. Definitions and verified results should be admitted in preference to
scratch reasoning, and a retrieved theorem should carry its hypotheses into
context with it, since a theorem statement separated from its hypotheses is an
invitation to misapply it.

Long proof searches are the natural home of isolation. A subordinate agent can
exhaust a failed strategy across many steps and return one line — *this approach
fails because the boundary divisor is not effective* — leaving the parent's
context clean. The failure is preserved as a result; the twenty thousand tokens
that established it are not.

## Forces and failure modes

Aggressive compression loses details that a later step needs, and the symptom is
recognizable: the agent re-reads files it has already processed. Conservative
compression reclaims too little and postpones rather than prevents the problem.
Isolation is the strongest lever but hides the specialist's reasoning from the
coordinator, so a wrong summary becomes an unchallengeable premise. Every
strategy trades recoverable information for attention, and that trade should be
a recorded decision rather than a side effect of a framework default.

## Real-world application

A support agent handling a long conversation with several tool lookups needs the
current customer record and the active policy in context, but not the full text
of every earlier lookup. The design question is not *how large a window can we
afford* but *which three facts must be present at the moment the model decides*.
Answering the second question usually reduces the first.

## Exercises

1. Take an agent trace of at least ten steps and tabulate cumulative tokens by
   source: instructions, history, retrieved documents, tool results. Which
   source dominates, and at which step does it overtake the instructions?
2. Apply a head-and-tail budget to that trace. Identify the first item dropped
   that the agent later needed, and state the priority rule that would have
   retained it.
3. Take a task that currently runs in one agent and identify a sub-task whose
   intermediate work the parent never needs. Estimate the token reduction from
   isolating it, and state what the parent loses by not seeing that work.
4. Write the pinning rule for a proof-search agent: which items must survive
   every compaction, and what should happen when the pinned set alone exceeds
   the budget?

## Reference basis

The treatment here follows Victor Dibia, [*Designing Multi-Agent Systems*](https://multiagentbook.com/),
Chapter 4, Section 4.12, which defines context engineering as the management of
how context accumulates and evolves during multi-step execution — as distinct
from prompt engineering — and gives the compaction, isolation, active-memory,
and tool-filtering strategies together with the comparative token measurements
quoted above. The agents-as-tools mechanism underlying isolation is Section 4.11
of the same chapter. Sampriti Mitra, [*System Design for the LLM Era*](https://www.packtpub.com/en-us/product/system-design-for-the-llm-era-9781807789923),
Chapter 1, treats context engineering as an atomic unit of LLM system design and
states the governing principle directly: building with language models is a data
pipeline problem rather than a prompting problem, and architecture controls the
flow of context. Its decomposition into dynamic assembly, window management
(prioritization and compression), and tool orchestration is the structure
adopted above; the corresponding compression pattern appears in Chapter 2.
Dibia quotes Andrej Karpathy's formulation, which remains the most compact
statement of the idea: if the model is the processor, the context window is RAM.
