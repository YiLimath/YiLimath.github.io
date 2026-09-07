---
title: "Agent Systems: Multiple-Agent Cooperation"
permalink: /posts/2026/08/agent-system/multiple-agent-cooperation/
tags:
  - Agent System
---

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

## Figure

![Multiple-agent cooperation](/images/agent-system/07-multi-agent-cooperation.svg)

*Figure: specialized agents divide work and return artifacts to an orchestrator.*
