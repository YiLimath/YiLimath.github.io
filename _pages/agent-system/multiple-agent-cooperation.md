---
title: "Agent Systems: Multiple-Agent Cooperation"
permalink: /posts/2026/08/agent-system/multiple-agent-cooperation/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Multiple-agent cooperation](/images/agent-system/07-multi-agent-cooperation.svg)

*Figure: specialized agents return typed artifacts through a shared message
protocol; the coordinator aggregates and verifies the result.*

## Problem

A complex task may require incompatible skills, independent exploration, or
different permissions. One general agent can become a bottleneck and a single
point of failure.

## Intent and structures

The main forms are a **supervisor** that delegates to specialists, a **peer
group** that exchanges artifacts, a **pipeline** in which each agent owns a
stage, and a **debate** in which agents critique alternatives. The choice should
be driven by task dependencies, not by a desire to maximize agent count.

## Stable interface

Every subtask needs an owner, input contract, expected artifact, status, evidence
format, and completion condition. The coordinator aggregates artifacts and owns
the global termination decision.

## Mathematical example

Separate search for examples, retrieval of known results, proof construction,
and proof criticism. Specialization is useful only if the outputs can be
reconciled and checked.

## Forces and failure modes

Multiple agents improve diversity and throughput but create coordination cost,
duplicate work, inconsistent assumptions, and error amplification. Shared truth
must be guarded by an evaluator or verifier; consensus is not correctness.

## Real-world application

An incident-response system can assign log analysis, dependency lookup, and
remediation planning to separate specialists. A coordinator merges their typed
artifacts and sends only the agreed incident state to the operator; specialists
do not need to share hidden conversational context.

## Reference basis

The pattern follows Gulli, *Agentic Design Patterns*, Chapter 7, and Dibia,
*Designing Multi-Agent Systems*, Chapters 2 and 7. Published system examples
include AutoGen's [multi-agent conversation paper](https://arxiv.org/abs/2308.08155)
and Microsoft's [Magentic-One report](https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Magentic-One.pdf).

## Related systems

This figure is a teaching abstraction of supervisor-style coordination. Compare
Victor Dibia's [multi-agent systems book and companion material](https://multiagentbook.com/)
for explicit orchestration patterns. For a research system with an orchestrator
directing specialized agents, see Microsoft's [Magentic-One overview](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/)
and [technical report](https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Magentic-One.pdf).
