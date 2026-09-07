---
title: "Agent Systems: Deep Search Pattern"
permalink: /posts/2026/08/agent-system/deep-search/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

## Problem

The first query is usually underspecified and retrieves only the obvious
material. A broad question needs controlled decomposition and repeated evidence
collection.

## Intent and structure

`question → subquestions → search branches → inspect sources → refine → synthesize`

Each branch should record its query, selected source, relevance judgment,
extracted claim, and unresolved question. The synthesis step must distinguish
direct support, nearby technique, contradiction, and open gap.

## Relation to ordinary retrieval

Basic retrieval answers one context-selection problem. Deep search adds a
research policy: decide what to search next based on what the last search taught
the system. It therefore composes retrieval, reflection, routing, and a stopping
rule.

## Mathematical stopping rules

Stop when the requested coverage is reached, new searches repeat known results,
the time or query budget is exhausted, or a human decides that the remaining
uncertainty is the actual research problem.

## Failure modes

Search can become a loop, confirmation bias can narrow the branches too early,
and citation count can be mistaken for mathematical relevance. Keep a search log
and preserve negative results.

## Figure

![Deep search workflow](/images/agent-system/15-deep-search.svg)

*Figure: a broad question is decomposed into evidence-producing search branches.*
