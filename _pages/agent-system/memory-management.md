---
title: "Agent Systems: Memory-Management Pattern"
permalink: /posts/2026/08/agent-system/memory-management/
tags:
  - Agent System
---

## Intent

Preserve useful state without placing the whole history in every context.

## Outline

1. Recurring problem: context windows are bounded, while tasks and histories are not.
2. Structure: `experience → select → store → retrieve → current context`.
3. Stable interface: memory item, metadata, retrieval query, and provenance.
4. Variable implementation: summary, vector search, linked notes, database, or file system.
5. Strength: continuity and bounded context size.
6. Risks: stale summaries, irrelevant retrieval, false links, and context overload.
7. Example: an Obsidian vault as long-term external memory for mathematical research.

## Suggested figure

`09-memory-management.svg` in the Agent design pattern illustration folder.
