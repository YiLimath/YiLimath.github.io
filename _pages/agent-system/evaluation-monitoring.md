---
title: "Agent Systems: Evaluation and Monitoring"
permalink: /posts/2026/08/agent-system/evaluation-monitoring/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

## Figure

![Evaluation and monitoring](/images/agent-system/18-evaluation-monitoring.svg)

*Figure: evaluators inspect both the final artifact and the trajectory that produced it.*

**In one sentence.** A non-deterministic system cannot be unit-tested by string
equality, so quality has to be made measurable by other means — a fixed test
set, a judge, and metrics that describe the trajectory rather than the answer.

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

The obstacle is stated most sharply as a question about testing: how do you write
a unit test for a system whose output changes between runs? Asserting equality
against an expected string fails constantly and tells you nothing.

The standard answer has two parts. A **golden dataset** of roughly fifty to a
hundred representative inputs with their ideal outputs is run in the build
pipeline, so that a prompt change or a model upgrade cannot silently break core
behavior. Because nobody can review a hundred responses on every build, an
**LLM-as-judge** scores each response against the golden answer on named criteria
— accuracy, groundedness, tone — producing a quantity that can be tracked over
time.

The judge is itself a component with failure modes, and treating its score as
ground truth reintroduces the problem it was meant to solve. A judge sharing the
generator's model and prompt shares its blind spots; judges favor longer and more
fluent answers independently of correctness; and a score without a named
violated criterion tells an engineer nothing about what to repair. Use
deterministic checks wherever the criterion can be formalized, reserve the judge
for what cannot, and calibrate it against human labels on a sample rather than
assuming agreement.

Build the golden set — ordinary cases, edge cases, and known failures — before
optimizing prompts or architecture. Monitor drift after deployment and turn
recurring failures into regression tests.

## What to monitor in production

Conventional dashboards do not describe these systems. Alongside the usual
service metrics, track cost per query and per user with alerts on spikes; time
to first token and tokens per second at the tail rather than the mean; rate-limit
and server-error rates per provider, since these are what the fallback logic
consumes; judge scores over time; and the **escalation rate** — the fraction of
tasks the system fails to resolve and hands to a human. The last is the most
informative single number, because it moves when quality degrades for reasons no
individual metric captures.

## Real-world application

An automated report service should evaluate both the final report and the trace
that produced it: source coverage, schema validity, latency, cost, and policy
violations. A score without a retained artifact does not tell an engineer what
to repair.

## Exercises

1. Build a ten-case golden set for one task: five ordinary, three edge, two known
   failures. Which of the ten can be checked deterministically?
2. Write judging criteria for one of those cases. Have a judge score three
   responses, score them yourself, and measure the disagreement.
3. Construct a case where the artifact is correct and the trajectory is bad
   (excessive retries, irrelevant retrieval, a skipped check). Which metric
   catches it?
4. Your escalation rate rises from 4% to 9% with every other metric flat. List
   three causes and the evidence that would separate them.
5. For a proof-checking agent, state which of the mathematical metrics above are
   deterministic and which need a judge, and justify the boundary.

## Reference basis

The pattern follows Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 19, “Evaluation and Monitoring,” and Dibia, [*Designing Multi-Agent
Systems*](https://multiagentbook.com/), Chapter 10, “Evaluating Multi-Agent
Systems.” Dibia's emphasis on trajectory evaluation is especially relevant
when the final answer alone hides a failed intermediate step. The golden-dataset
and LLM-as-judge patterns, together with the production metrics above — cost per
query, time to first token, provider error rates, and escalation rate — are the
testability and observability patterns in Mitra, [*System Design for the LLM
Era*](https://www.packtpub.com/en-us/product/system-design-for-the-llm-era-9781807789923),
Chapter 2. Judging is treated as a pattern in its own right, with its calibration
problems, by Lakshmanan and Hapke, [*Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/),
Pattern 17, alongside the degradation-testing pattern for behavior under a
weakened model or a missing tool.
