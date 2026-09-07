---
title: "Agent Systems: Exception Handling and Recovery"
permalink: /posts/2026/08/agent-system/exception-recovery/
tags:
  - Agent System
---

## Intent

Make failure visible and return the system to a safe, useful state.

## Outline

1. Recurring problem: tools fail, retrieval returns nothing, a model produces malformed output, or a plan becomes invalid.
2. Classify failures: transient, structural, semantic, permission-related, and mathematical uncertainty.
3. Recovery actions:
   - retry with bounded attempts;
   - repair or reformat an artifact;
   - fall back to a simpler method;
   - checkpoint and resume;
   - escalate to a human;
   - stop with an explicit incomplete result.
4. Preserve the failed artifact and error context for diagnosis.
5. Never convert an unresolved mathematical gap into a successful-looking summary.

## Design question

After failure, what information must be preserved so that the next attempt does not repeat the same mistake?

## Suggested figure

`16-exception-recovery.svg` in the Agent design pattern illustration folder.
