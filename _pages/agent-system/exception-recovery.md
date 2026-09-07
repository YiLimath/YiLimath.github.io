---
title: "Agent Systems: Exception Handling and Recovery"
permalink: /posts/2026/08/agent-system/exception-recovery/
tags:
  - Agent System
---

## Problem

Tools fail, retrieval returns nothing, output violates a schema, services time
out, and plans become invalid. Treating every failure as another prompt hides
the actual state of the system.

## Intent and structure

`action → classify failure → retry / repair / fallback / escalate / stop`

Classify failures as transient, structural, semantic, permission-related, or
mathematical uncertainty. The category determines the recovery policy.

## Recovery contract

Preserve the failed artifact, error, inputs, attempt count, and checkpoint. Retry
only when the operation is safe and bounded. Repair malformed structure without
silently changing content. Fall back to a simpler method only when its quality
limits are explicit.

## Mathematical rule

An unresolved gap is a valid terminal state. Never convert it into a successful-
looking summary merely because a later generation step is fluent.

## Forces and failure modes

Recovery improves availability but can amplify side effects, duplicate work, or
loop forever. Use idempotence, exponential backoff where appropriate, retry
limits, circuit breakers, and human escalation.

## Figure

![Exception handling and recovery](/images/agent-system/16-exception-recovery.svg)

*Figure: failures are classified and routed to bounded retry, repair, fallback, escalation, or safe stop.*
