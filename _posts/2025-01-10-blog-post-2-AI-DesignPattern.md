---
title: 'Agent System Design Pattern'
date: 2026-04-04
permalink: /posts/2026/01/Agent-System/
tags:
  - Agent System
---

The aim of this note is to give a brief introduction to the design patterns used in building agent systems. By an *agent system* I mean a program in which a language model is placed inside a loop: it is given a goal, a set of tools it may call, and some working memory, and it decides for itself which tool to call next until the goal is met. The interesting engineering question is not "which model is best" but rather: **what should be in the model's context at each step, and who decides what happens next — the model, or the program around it?** Almost every design pattern below is an answer to one of these two questions.

We divide the note into two parts: (1) the common design patterns for agent systems, and (2) a case study of the agent system I built for my own mathematical research.

> An agent system is a way of trading determinism for flexibility. The design patterns are the tools for buying back as much determinism as the task requires.

---

## Part I. Common Design Patterns

### I.0 Terminology

Before discussing patterns we fix the vocabulary. These words are used inconsistently across the literature, so it is worth being precise.

- **Model / context window** — the language model and the finite buffer of text it sees on each call. Everything else in this list exists to control what goes into that buffer.
- **Tool** — a function the model may call (read a file, run a search, execute code). The model does not run the tool; it emits a request, the surrounding program runs it and returns the result.
- **Agentic loop** — the cycle *model proposes a tool call → program executes it → result is appended to the context → model proposes the next call*, repeated until the model stops.
- **Workflow vs. agent** — in a *workflow* the sequence of steps is fixed by the programmer and the model only fills in the content of each step; in an *agent* the model itself chooses the sequence. This is the single most important distinction in the whole subject.
- **Harness** — the program surrounding the model: it owns the loop, the tools, the permissions, and the context assembly.
- **Subagent** — a fresh model instance with its own context window, given a narrow task by a parent agent, returning only a summary.
- **Skill** — a reusable instruction document loaded into context on demand, encoding a procedure the agent should follow for a recurring kind of task.
- **MCP (Model Context Protocol)** — a standard interface for exposing tools and data sources to an agent, so the same tool server can be reused across different agents.

### I.1 The Central Constraint: Context

[to write] Why the context window, not the model's reasoning ability, is usually the binding constraint. Context is finite, and quality degrades well before the limit is reached — irrelevant material actively hurts. Every pattern in I.2 can be read as a strategy for keeping the working context small and relevant: retrieval puts in only what is needed, subagents move work into a *different* context window, checkpoints flush finished work to disk.

### I.2 The Patterns

Roughly in order of increasing autonomy given to the model.

**[P1] Prompt chaining.** A fixed pipeline: the output of step $n$ is the input of step $n+1$. No model decisions about control flow. Use when the task decomposes the same way every time.

**[P2] Routing / dispatch.** A cheap first step classifies the request and sends it to one of several specialized handlers, each with its own prompt and tools. Buys specialization without one bloated system prompt.

**[P3] Tool use and grounding.** Giving the model the ability to read the actual source of truth instead of recalling it. The key design decision is tool *granularity*: too many fine-grained tools and the model gets lost, too few and each call returns too much.

**[P4] Retrieval (RAG).** A search index over a corpus, so the agent retrieves the relevant few documents rather than being given everything. Semantic (embedding-based) retrieval finds material that lexical search misses when the vocabulary differs.

**[P5] Orchestrator–worker.** A parent agent decomposes a task and spawns subagents, each with a clean context, then synthesizes their reports. Buys parallelism and context isolation; costs coherence, since workers cannot see each other's findings.

**[P6] Parallelization.** Two variants: *sectioning* (independent subtasks run at once) and *voting* (the same task run several times, results compared). Voting is a cheap way to detect where the model is unreliable.

**[P7] Evaluator–optimizer (critic loop).** One agent produces, a second agent with different instructions criticizes, the first revises. Works when criticism is genuinely easier than production — proof checking, code review, translation.

**[P8] Reflection and self-correction.** The single-agent version of [P7]. Weaker, because a model reviewing its own output in the same context tends to defend it.

**[P9] Memory.** Distinguish *short-term* (a scratchpad within a task) from *long-term* (facts written to files and reloaded in later sessions). Long-term memory is what makes an agent improve across sessions rather than restarting cold every time.

**[P10] Progressive disclosure / skills.** Rather than loading all instructions always, keep a short index of available procedures and load the full document only when it is relevant. Directly addresses I.1.

**[P11] Checkpointing and human-in-the-loop.** Long tasks are split into phases, each writing a durable file and pausing for approval. Prevents a bad decision in phase 1 from silently propagating through phase 5, and makes rollback possible.

**[P12] Guardrails and permissions.** Which actions the harness will execute without asking. Irreversible actions (deleting, sending, publishing) should not be at the model's discretion.

### I.3 Failure Modes

[to write] The characteristic ways agent systems fail, and which pattern addresses each:

- **Context degradation** — long sessions accumulate irrelevant material and quality drops. → [P5], [P10], [P11]
- **Error compounding** — a small mistake early is treated as an established fact for the rest of the run. Ten steps at 95% reliability each is a coin flip. → [P7], [P11]
- **Confident fabrication** — plausible but wrong citations, references, or results. → [P3], [P4]
- **Over-delegation** — subagents spawned for work the parent could do directly, each paying a fresh start-up cost with no shared context. → do less of [P5]
- **Lost intent** — the agent optimizes the literal instruction rather than the goal behind it.

### I.4 When Not to Build an Agent

[to write] The honest answer is that a fixed workflow, or a plain script, beats an agent for most tasks. An agent is worth its overhead only when the task genuinely requires decisions that cannot be enumerated in advance.

---

## Part II. Agent Systems in Examples

In the second part of this note I case study the design of a concrete agent system: the one I built to support my own work in birational geometry. It runs over an Obsidian vault of roughly 11,600 mathematical notes, and it exists to do three things — keep my daily research schedule, turn papers into structured notes, and check mathematics I have written.

I will describe each component and identify which pattern from Part I it instantiates, including the places where I chose a pattern badly and had to change it.
