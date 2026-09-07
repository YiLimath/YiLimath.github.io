---
title: "Case Study: A Mathematical Research Agent System"
permalink: /posts/2026/08/agent-system/math-research-case-study/
tags:
  - Agent System
  - Birational Geometry
---

The case study describes an agent system built to support mathematical research over an Obsidian vault of roughly 11,600 notes.

## System requirements

- Preserve source material and distinguish it from generated summaries.
- Expose uncertainty rather than silently inventing mathematical facts.
- Keep the researcher in control of priorities and final judgments.
- Keep dates, task status, note links, theorem statements, and proof artifacts reproducible.

## Workflows

### Daily research scheduling

- **Goal:** convert recent work and priorities into a manageable daily assignment.
- **Patterns:** plan-and-execute, memory management, human-in-the-loop.
- **Pipeline:** recent work → candidate tasks → prioritized plan → human adjustment → daily sheet.

### Paper encoding and note construction

- **Goal:** turn a paper into structured notes without losing theorem statements or raw proofs.
- **Patterns:** prompt chaining, tool use, memory management, reflection.
- **Pipeline:** paper → metadata → outline → theorem notes → proof notes → verification and revision.

### Mathematical proof checking

- **Goal:** check a written argument against definitions, hypotheses, and known results.
- **Patterns:** router, tool use, reflection, human-in-the-loop.
- **Pipeline:** proof claim → identify dependencies → retrieve notes → check steps → report gaps → human decision.

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

`12-math-research-case-study.svg` in the Agent design pattern illustration folder.
