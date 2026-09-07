---
title: "Agent Systems: Evaluation and Monitoring"
permalink: /posts/2026/08/agent-system/evaluation-monitoring/
tags:
  - Agent System
  - Mathematics
---

## Intent

Measure whether the system is performing the intended task, not merely producing fluent output.

## Outline

1. Evaluation-driven development: define success before optimizing the workflow.
2. Build a representative evaluation set containing ordinary cases, edge cases, and known failures.
3. Evaluate both final answers and trajectories:
   - retrieved sources;
   - tool calls;
   - intermediate artifacts;
   - failed attempts;
   - stopping decisions.
4. Mathematical metrics:
   - correctness;
   - hypothesis preservation;
   - citation and provenance accuracy;
   - proof-checker acceptance;
   - useful-gap detection;
   - human time saved.
5. Use deterministic tests where possible and human or model judges only where necessary.
6. Monitor drift, cost, latency, and recurring failure modes after deployment.

## Design question

Can the evaluation distinguish a correct proof, a plausible proof with a gap, and an irrelevant answer?

## Suggested figure

`18-evaluation-monitoring.svg` in the Agent design pattern illustration folder.
