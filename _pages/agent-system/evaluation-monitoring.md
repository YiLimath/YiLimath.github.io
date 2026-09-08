---
title: "Agent Systems: Evaluation and Monitoring"
permalink: /posts/2026/08/agent-system/evaluation-monitoring/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

## Problem

Fluent output is a weak proxy for task success. A system can produce attractive
answers while retrieving irrelevant evidence, taking excessive steps, or
silently violating a constraint.

## Evaluation layers

1. **Artifact evaluation:** correctness, completeness, format, and provenance.
2. **Trajectory evaluation:** tool calls, intermediate artifacts, retries,
   latency, cost, and stopping decisions.
3. **System evaluation:** reliability, safety, user usefulness, and behavior
   under degraded models, missing tools, or empty retrieval.

## Mathematical metrics

Test hypothesis preservation, citation accuracy, proof-checker acceptance,
counterexample detection, useful-gap detection, and reproducibility. Use
deterministic tests where possible; use model judges or humans for criteria that
cannot be formalized, and record their uncertainty.

## Evaluation-driven development

Build a golden set containing ordinary cases, edge cases, and known failures
before optimizing prompts or architecture. Monitor drift after deployment and
turn recurring failures into regression tests.

## Real-world application

An automated report service should evaluate both the final report and the trace
that produced it: source coverage, schema validity, latency, cost, and policy
violations. A score without a retained artifact does not tell an engineer what
to repair.

## Reference basis

The pattern follows Gulli, *Agentic Design Patterns*, Chapter 19, “Evaluation
and Monitoring,” and Dibia, *Designing Multi-Agent Systems*, Chapter 10,
“Evaluating Multi-Agent Systems.” Dibia's emphasis on trajectory evaluation is
especially relevant when the final answer alone hides a failed intermediate
step.

## Figure

![Evaluation and monitoring](/images/agent-system/18-evaluation-monitoring.svg)

*Figure: evaluators inspect both the final artifact and the trajectory that produced it.*
