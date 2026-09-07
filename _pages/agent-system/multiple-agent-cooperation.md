---
title: "Agent Systems: Multiple-Agent Cooperation Pattern"
permalink: /posts/2026/08/agent-system/multiple-agent-cooperation/
tags:
  - Agent System
---

## Intent

Divide responsibilities among agents with different roles or capabilities.

## Outline

1. Recurring problem: one agent must simultaneously satisfy incompatible roles or standards.
2. Structure: `coordinator ↔ specialists ↔ shared result`.
3. Stable interface: role description, message format, and shared result schema.
4. Variable implementation: number of specialists and communication topology.
5. Strength: modularity and role-specific prompts or tools.
6. Risks: communication overhead, coordination failure, and inconsistent assumptions.
7. Example: research, reasoning, and writing specialists coordinated around one task.

## Suggested figure

`07-multi-agent-cooperation.svg` in the Agent design pattern illustration folder.
