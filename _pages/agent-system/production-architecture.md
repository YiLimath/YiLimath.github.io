---
title: "Agent Systems: Production Architecture"
permalink: /posts/2026/08/agent-system/production-architecture/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Production architecture for LLM agents](/images/agent-system/26-production-architecture.svg)

*Figure: gateways, caching, fallbacks, and evaluation surround the agent core.*

## Problem

An agent prototype may work in a notebook but fail under load, provider errors,
long latency, changing prompts, or partial tool availability. Production design
must control the whole request path, not only the model call.

## Architecture

`client → gateway → agent core → model/tools`

Around this path, add authentication and rate limits, caching and context
compression, synchronous or asynchronous execution, circuit breakers, tiered
fallbacks, traces, and evaluation. The gateway is a policy boundary; it should
not become a second source of truth.

## Reliability patterns

- **Circuit breaker:** stop repeatedly calling a failing provider.
- **Tiered fallback:** move to a cheaper or simpler method with explicit quality
  limits.
- **Checkpointing:** persist a long-running task so it can resume after failure.
- **Degradation testing:** measure behavior when models, retrieval, or tools are
  unavailable.

## Data and evaluation

Use stable request IDs, version prompts and schemas, record latency/cost/error
metrics, and maintain a golden evaluation set. Cache only when the cache key
captures all state that affects correctness.

## Mathematical caution

A fallback that returns a shorter answer must not claim the quality of a verified
proof. Degraded operation should expose reduced confidence, reduced scope, or a
human escalation.

## Real-world application

For a customer-facing agent, the gateway owns authentication, rate limits, and
request identity; the runtime owns task state; and the evaluator owns quality
signals. Keeping those responsibilities separate makes provider failures,
prompt changes, and partial tool outages observable in production.

## Reference basis

The production patterns follow Mitra, [*System Design for the LLM Era*](https://www.packtpub.com/en-us/product/system-design-for-the-llm-era-9781807789923),
Chapters 2–6, especially gateways, circuit breakers, asynchronous processing,
caching, evaluation, and security. Dibia's [*Designing Multi-Agent Systems*](https://multiagentbook.com/),
Chapters 10–13 provide complementary
references for trajectory evaluation, optimization, distributed protocols, and
responsible deployment.

## Reference architecture

This is a course synthesis of production concerns, not a copy of a vendor
reference architecture. For the production-design viewpoint used here, see
Sampriti Mitra's [*System Design for the LLM Era*](https://www.packtpub.com/en-us/product/system-design-for-the-llm-era-9781807789923).
