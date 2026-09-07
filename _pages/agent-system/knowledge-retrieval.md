---
title: "Agent Systems: Knowledge Retrieval and Provenance"
permalink: /posts/2026/08/agent-system/knowledge-retrieval/
tags:
  - Agent System
  - Mathematics
---

## Problem

Context is bounded, while a technical corpus is large. Internal model memory is
not a reliable source for domain-specific or source-sensitive claims.

## Intent and structure

`corpus → index → retrieve → rerank/postprocess → grounded generation`

The retrieval pattern includes more than a vector database. Lexical search,
semantic indexing, metadata filters, hybrid retrieval, graph traversal, and
node postprocessing solve different parts of the problem.

## Mathematical retrieval

Retrieve definitions and notation before theorems; retrieve theorem statements
with hypotheses; retrieve proof dependencies, examples, counterexamples, and
source locations. A related theorem with mismatched hypotheses is a dangerous
retrieval success, not a correct answer.

## Provenance contract

Every important generated claim should point to a source record and preserve the
retrieval query, location, and applicability judgment. Separate source text,
interpretation, and new inference. Do not silently merge duplicate or stale
statements.

## Forces and failure modes

Retrieval improves grounding but can introduce irrelevant context, ranking bias,
and citation drift. Evaluate recall and precision separately, cap context,
rerank for applicability, and allow the system to say that no adequate source
was found.

## Figure

![Knowledge retrieval and provenance](/images/agent-system/14-knowledge-retrieval.svg)

*Figure: retrieval selects evidence from a corpus before grounded generation.*
