---
title: "Agent Systems: Deep Search Pattern"
permalink: /posts/2026/08/agent-system/deep-search/
tags:
  - Agent System
  - Mathematics
---

## Intent

Turn search into an iterative process of query refinement, reading, comparison, and synthesis.

## Outline

1. Recurring problem: the first query is ambiguous or retrieves only the obvious literature.
2. Structure: `query → search → inspect results → refine query → search again → synthesize`.
3. Require a search log: query, source, relevance judgment, extracted claim, and unresolved question.
4. For mathematics, distinguish:
   - a theorem that directly applies;
   - a theorem with mismatched hypotheses;
   - a nearby technique;
   - an open gap.
5. Define stopping rules: coverage reached, repeated results, time budget, or human judgment.
6. Risks: search loops without progress, confirmation bias, and confusing citation count with mathematical relevance.

## Design question

What new information did the latest search add, and which uncertainty remains unresolved?

## Suggested figure

`15-deep-search.svg` in the Agent design pattern illustration folder.
