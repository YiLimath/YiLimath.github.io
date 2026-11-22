---
title: 'Designing Reasoning Systems for Mathematical Research'
date: 2026-08-01
permalink: /posts/2026/08/Agent-System/
tags:
  - Agent System
classes: agent-system-hub
full_page_reading: true
---

**A reasoning system for mathematical research should preserve the meaning of its problem while it searches, transforms objects, and accumulates knowledge.** This series develops the architecture needed to do that. Its subject is not a particular model, framework, or prompting fashion.

A stronger model may change how much work a component can perform. It does not erase the distinction between a statement and an argument, a sufficient condition and a necessary one, or a useful partial result and a proof of the original target.

## Start here

1. Read the [design principles](/posts/2026/08/agent-system/design-principles/) for the central architectural boundaries.
2. Work through the [three running cases](/posts/2026/08/agent-system/research-cases/): lifting a section, obtaining a uniform estimate, and composing a well-founded induction.
3. Build the [research workbench](/posts/2026/08/agent-system/hands-on-lab/). The downloadable Python project runs without an API key and exposes both the power and the limits of dependency bookkeeping.

The elementary maximum example in the introduction is a smoke test. The three running cases carry the deeper lessons. The later birational-geometry chapter shows how the contracts scale to a proposed research architecture; it does not claim to implement a universal prover.

## How to study the series

For a first pass, follow the six parts below. For implementation, keep the laboratory open and complete its eight stages alongside the relevant chapters. For a research project, begin with a known short proof, construct damaged variants, and evaluate the system before attempting an open problem.

Each chapter starts from a mathematical design decision, explains the contract and failure modes, and ends with a concrete experiment. Read the [source and claim guide](/posts/2026/08/agent-system/sources-and-claims/) to distinguish established precedents, worked mathematical arguments, design proposals, and reported implementations.

## I. Preserve the meaning of the problem

- [The Objects a Reasoning System Must Represent](/posts/2026/08/agent-system/foundations/)
- [Stable Contracts Under Changing Models](/posts/2026/08/agent-system/variation-points/)
- [Types That Preserve Mathematical Distinctions](/posts/2026/08/agent-system/structured-output/)
- [Context as a Scoped View of Research State](/posts/2026/08/agent-system/context-engineering/)

## II. Organize search without confusing it with proof

- [A Research Loop Changes an Obligation](/posts/2026/08/agent-system/core-loop/)
- [Proof Plans as Obligations and Alternatives](/posts/2026/08/agent-system/plan-and-execute/)
- [Stage a Theorem Application](/posts/2026/08/agent-system/prompt-chaining/)
- [Route by the Evidence Required](/posts/2026/08/agent-system/router/)
- [Parallel Search Needs a Mathematical Merge Rule](/posts/2026/08/agent-system/parallelization/)
- [Explore for Information, Not Reassurance](/posts/2026/08/agent-system/exploration-and-discovery/)
- [Representation Change and the Return Argument](/posts/2026/08/agent-system/reasoning/)
- [Spend Computation Where It Can Change the Argument](/posts/2026/08/agent-system/resource-aware-optimization/)

## III. Make knowledge applicable and revisable

- [Theorem Retrieval Ends with Applicability](/posts/2026/08/agent-system/knowledge-retrieval/)
- [A Search Should Leave an Auditable Frontier](/posts/2026/08/agent-system/deep-search/)
- [Knowledge as Versioned Arguments](/posts/2026/08/agent-system/memory-management/)
- [Critique the Failed Inference](/posts/2026/08/agent-system/reflection/)
- [Agent Systems: The Verification Gate](/posts/2026/08/agent-system/verification-gate/)

## IV. Coordinate work and authority

- [Partition Evidence-Producing Work](/posts/2026/08/agent-system/multiple-agent-cooperation/)
- [Messages Carry Versioned Mathematical Work](/posts/2026/08/agent-system/inter-agent-communication/)
- [Agent Systems: Human-in-the-Loop Pattern](/posts/2026/08/agent-system/human-in-the-loop/)
- [Protect Evidence and Admission Authority](/posts/2026/08/agent-system/guardrails-safety/)

## V. Evaluate, recover, and improve

- [Completion Is Relative to the Original Target](/posts/2026/08/agent-system/goal-monitoring/)
- [Evaluate Mathematical Progress and Failure Together](/posts/2026/08/agent-system/evaluation-monitoring/)
- [Distinguish a Tool Failure from a Mathematical Obstruction](/posts/2026/08/agent-system/exception-recovery/)
- [Learn Search Preferences, Not Unproved Theorems](/posts/2026/08/agent-system/learning-and-adaptation/)
- [Durable Research State and Reproducible Recovery](/posts/2026/08/agent-system/production-architecture/)
- [Agent Systems: Architecture Views](/posts/2026/08/agent-system/architecture-views/)
- [Choose Architecture Against a Named Failure](/posts/2026/08/agent-system/choosing-patterns/)

## VI. Build a research architecture

- [Agent Systems for Mathematical Research: A Working Protocol](/posts/2026/08/agent-system/research-workflow/)
- [Research Architecture: A Proof-Sketch and Method-Recommendation System](/posts/2026/08/agent-system/proof-sketch-system/)
- [Designing a Spiraling Induction System for Birational Geometry](/posts/2026/08/agent-system/birational-geometry-agent/)
- [Case Study: Danus and Rethlas](/posts/2026/08/agent-system/math-research-case-study/)

## What you should be able to build

By the end, you should be able to represent a mathematical target precisely, expose alternative arguments and their joint premises, preserve conditional results, audit a theorem application, track a geometric return argument, and explain what the system has and has not checked. You should also be able to reproduce a failed attempt and compare a more elaborate architecture with a simpler baseline.

The practical outcome is an inspectable research episode: a target, evidence, argument graph, review record, and open frontier. The software may become more autonomous; the mathematical meaning of those artifacts should remain visible.

For a short motivation, see [why explicit architecture matters](/posts/2026/08/agent-system/why-mathematicians-need-patterns/). For books and primary references, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

> Written in cooperation with AI. Architectural proposals and teaching implementations are labelled as such; model-reviewed work is not presented as kernel-checked mathematics.
