---
title: "Agent Systems: Inter-Agent Communication and Protocols"
permalink: /posts/2026/08/agent-system/inter-agent-communication/
tags:
  - Agent System
---

## Intent

Allow agents to exchange tasks, evidence, artifacts, and status without relying on an implicit shared conversation.

## Outline

1. Recurring problem: multiple agents may have different context, assumptions, and responsibilities.
2. Stable message contract: sender, recipient, task identifier, artifact, provenance, status, and requested action.
3. Separate communication from orchestration:
   - orchestration decides who acts next;
   - communication specifies what is transferred.
4. Mathematical messages should carry assumptions and unresolved obligations, not only conclusions.
5. Discuss protocols as interfaces between independent components, including agent-to-agent and tool protocols.
6. Risks: inconsistent state, duplicated work, hidden assumptions, and message histories that grow without bound.

## Design question

Could another agent reconstruct the claim, its assumptions, and its next action from the message alone?

## Suggested figure

`21-inter-agent-communication.svg` in the Agent design pattern illustration folder.
