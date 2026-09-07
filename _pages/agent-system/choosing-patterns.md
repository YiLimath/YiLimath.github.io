---
title: "Agent Systems: Choosing and Composing Patterns"
permalink: /posts/2026/08/agent-system/choosing-patterns/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Start with the task shape

Place the task on the workflow–autonomy spectrum: fixed workflow, bounded loop,
or open-ended delegation. Then identify the dominant difficulty: decomposition,
specialization, uncertainty, long context, coordination, reliability, or cost.

## Selection rule

Start with the smallest deterministic structure that meets the requirement. Add
a pattern only when it addresses a named source of complexity. Compare candidate
designs by correctness, latency, cost, observability, reversibility, reliability,
and ease of revision.

## Useful compositions

- chaining + structured output for staged transformations;
- router + specialized tools for heterogeneous requests;
- plan + memory + checkpoints for long-horizon work;
- parallelization + aggregation + evaluation for independent alternatives;
- retrieval + provenance + reflection for source-sensitive answers;
- multi-agent cooperation + human delegation for high-stakes decisions.

## Anti-patterns

Do not add agents merely to sound autonomous, use retrieval without an
applicability check, or add reflection without a stopping rule. More components
increase coordination surfaces and failure modes.

## Design questions

What is uncertain? Which interface makes it observable? What is the simplest
pattern that provides that interface?

## Figure

![Reference architecture for choosing and composing patterns](/images/agent-system/00-agent-system-architecture.svg)

*Figure: pattern selection assigns responsibilities to orchestration, reasoning, knowledge, action, evaluation, and guardrails.*
