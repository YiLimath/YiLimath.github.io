---
title: "Case Study: A Mathematical Research Agent System"
permalink: /posts/2026/08/agent-system/math-research-case-study/
tags:
  - Agent System
  - Birational Geometry
---

The case study describes an agent system built to support mathematical research over an Obsidian vault of roughly 11,600 notes.

![Architecture of a mathematical research agent system](/images/agent-system/math-research-agent-architecture.svg)

The architecture separates research workflows from orchestration, external memory,
and human judgment. This separation is the main design-pattern lesson: each
boundary can be tested or replaced without treating the language model as the
whole system.

## System requirements

- Preserve source material and distinguish it from generated summaries.
- Expose uncertainty rather than silently inventing mathematical facts.
- Keep the researcher in control of priorities and final judgments.
- Keep dates, task status, note links, theorem statements, and proof artifacts reproducible.
- Make every stage evaluable, recoverable, and bounded by a clear termination condition.

## Workflows

### Daily research scheduling

- **Goal:** convert recent work and priorities into a manageable daily assignment.
- **Patterns:** plan-and-execute, memory management, human-in-the-loop.
- **Pipeline:** recent work → candidate tasks → prioritized plan → human adjustment → daily sheet → end-of-day evaluation.

### Paper encoding and note construction

- **Goal:** turn a paper into structured notes without losing theorem statements or raw proofs.
- **Patterns:** prompt chaining, structured output, tool use, memory management, reflection, exception recovery.
- **Pipeline:** paper → metadata → outline → theorem notes → proof notes → verification and revision, with checkpoints after each artifact.

### Mathematical proof checking

- **Goal:** check a written argument against definitions, hypotheses, and known results.
- **Patterns:** router, knowledge retrieval, tool use, reasoning, reflection, evaluation, human-in-the-loop.
- **Pipeline:** proof claim → identify dependencies → retrieve notes → check steps → classify gaps → report evidence → human decision.

### Research-loop controls

- **Goal monitoring:** state the current mathematical question and the condition for stopping or escalating.
- **Evaluation:** test retrieval quality, citation fidelity, proof-step validity, and usefulness of the final note.
- **Guardrails:** preserve quotations as source artifacts, separate conjecture from theorem, and require provenance for nontrivial claims.
- **Resource awareness:** use cheap retrieval and local computation before expensive broad search or long multi-agent deliberation.

## Redesign log

For at least two failures, record:

1. original design;
2. observed failure;
3. diagnosis of the violated interface;
4. revised pattern;
5. evidence that the revision helped.

## Final lesson

The vault is not merely a context window. It is an external memory and source of truth. The agent patterns make operations around that source of truth repeatable, inspectable, and revisable.

## Suggested figure

`12-math-research-case-study.svg` gives the system overview; `23-research-loop.svg`
shows the research-specific loop in more detail.
