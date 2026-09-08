---
title: "Agent Systems: Choosing and Composing Patterns"
permalink: /posts/2026/08/agent-system/choosing-patterns/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figures

![Agent system system context view](/images/agent-system/00-agent-system-architecture.svg)

*Figure: the context view shows the agent system as one unit and labels its
external relationships.*

![Agent system container view](/images/agent-system/28-agent-system-container.svg)

*Figure: the container view expands the boundary into replaceable
responsibilities and labels the interfaces between them.*

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

## Read the architecture at multiple levels

Do not ask one diagram to answer every architecture question. Read the views in
order:

1. **Context:** who exchanges responsibility with the agent system?
2. **Container:** which internal responsibilities own orchestration, runtime,
   knowledge, action, evaluation, and persistence?
3. **Dynamic:** in what order do messages, decisions, parallel branches, and
   feedback occur? The sequence and workflow pages provide these views.
4. **Operations:** which gateways, fallbacks, checkpoints, and evaluators make
   the design reliable in production?

The same system can therefore be structurally complicated without becoming
conceptually muddled. Keep the visual language stable, but choose the diagram
form that matches the relation being explained.

## Real-world application

For a customer-support or repository-maintenance system, begin with the
failure that matters: misrouting, unsafe side effects, missing evidence, or an
unreviewed result. Select the smallest composition that exposes that failure,
then add parallel workers, memory, or reflection only when the workflow needs
their contract.

## Reference basis

The selection principle follows Dibia, *Designing Multi-Agent Systems*, Chapter
2, Sections 2.1–2.4, and Anthropic's [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents),
which recommends simple composable workflows before adding autonomous
complexity.
