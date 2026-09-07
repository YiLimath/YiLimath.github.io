---
title: "Agent Systems: Router Pattern"
permalink: /posts/2026/08/agent-system/router/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Problem

One general agent is rarely the best implementation for every task class. A
retrieval question, a code execution request, and a proof critique need
different tools, prompts, or levels of reasoning.

## Intent and structure

`request → classify → specialized path → common output`

The router may be a deterministic rule, a small classifier, or a model-based
decision. The downstream paths should converge on a common result schema.

## Stable interface

Make the routing label, confidence or rationale, selected capability, and
fallback behavior explicit. The router must not silently discard a request it
cannot classify.

## Mathematical example

A research assistant can route a request to definition lookup, theorem search,
example construction, proof checking, or exposition. The output should state
which route was used and what evidence supports it.

## Forces and failure modes

Routing reduces prompt complexity and allows specialization, but misclassification
can be worse than using a general path. Use an abstain or human-escalation path,
monitor route distributions, and test boundary cases.

## Figure

![Router pattern](/images/agent-system/03-router.svg)

*Figure: a routing decision sends different task classes to specialized paths.*
