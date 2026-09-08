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

## Real-world application

For a market, technical, or literature investigation, the coordinator can
decompose the question, query several source types, maintain an evidence ledger,
and launch follow-up searches when coverage is weak. The final report is useful
because its claims and stopping condition remain inspectable.

## Reference basis

The figure and control logic are tied to Lakshmanan and Hapke, *Generative AI
Design Patterns*, Pattern 12, Figure 4-14, with the original-diagram link given
below. The research-oriented comparison is Shao et al.'s [STORM paper](https://aclanthology.org/2024.naacl-long.347/),
which makes perspective discovery, grounded conversations, and outline
curation explicit.

## Figure

![Deep search workflow](/images/agent-system/15-deep-search.svg)

*Figure: a teaching redraw of the Deep Search control structure. Retrieval,
generation, and thinking are separate stages; the two decisions make budget
and evidence coverage explicit; reflection produces the next subqueries.*

## Reference diagrams

This figure is a redraw for this course, not a reproduction of a book image.
Its central structure follows Figure 4-14, “Deep Search adds iteration, external
tools, and a thinking stage to traditional RAG,” in Valliappa Lakshmanan and
Hannes Hapke, *Generative AI Design Patterns*, Pattern 12. The book's public
companion repository also publishes the original diagram collection, with its
copyright notice and recommended citation: [O'Reilly book page](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/)
and [companion diagrams](https://github.com/lakshmanok/generative-ai-design-patterns/tree/main/diagrams).

For a research-oriented counterpart, compare Figure 2 of Shao et al.,
“Assisting in Writing Wikipedia-like Articles From Scratch with Large Language
Models.” STORM makes perspective discovery, simulated expert conversations,
trusted retrieval, and outline construction explicit: [paper](https://aclanthology.org/2024.naacl-long.347/)
and [official implementation](https://github.com/stanford-oval/storm).
