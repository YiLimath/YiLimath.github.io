---
title: "Agent Systems: Resource-Aware Optimization"
permalink: /posts/2026/08/agent-system/resource-aware-optimization/
tags:
  - Agent System
---

## Intent

Allocate models, tools, context, time, and parallel workers according to the value and difficulty of the task.

## Outline

1. Identify the resource triangle: quality, latency, and cost.
2. Match the method to the task:
   - deterministic code for exact computation;
   - small models for classification or formatting;
   - stronger models for difficult synthesis;
   - asynchronous processing for long-running work.
3. Reduce waste with caching, context pruning, batching, and early termination.
4. Use degradation testing to understand what happens when model quality, retrieval quality, or tool availability decreases.
5. Mathematical example: do not spend an expensive research pass on a task that can be answered by a verified local theorem lookup.
6. Risks: optimizing cost before correctness and allowing resource constraints to hide uncertainty.

## Design question

What is the cheapest method that preserves the required level of mathematical reliability?

## Suggested figure

`19-resource-aware-optimization.svg` in the Agent design pattern illustration folder.
