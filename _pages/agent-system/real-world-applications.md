---
title: "Agent Systems: Real-World Architecture Templates"
permalink: /posts/2026/08/agent-system/real-world-applications/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

The useful question is not “which framework has this pattern?” It is “what
real problem needs this boundary?” The figure below treats each pattern as an
architecture decision: a task enters, responsibilities cooperate through
explicit interfaces, and the system leaves behind an artifact or verdict that
can be inspected.

## Five real problems

![Real-world architecture templates for agent design patterns](/images/agent-system/29-real-world-patterns.svg)

*Figure: five application architectures. Solid navy arrows are functional
control or handoff; dashed teal arrows are state, evidence, or repair feedback;
red arrows are correctness or policy gates. The diagrams are course syntheses,
not claims that every implementation needs every component.*

### 1. Customer support triage

When many intents have different owners, the router is not merely a classifier:
it is a responsibility boundary. Specialist work and human escalation must
return a common response schema, so downstream systems do not need to know
which branch handled the request.

### 2. Literature survey

When a question is broad and sources vary in quality, decomposition and
parallel retrieval reduce blind spots. An evidence ledger makes the important
intermediate object explicit: source, claim, and supporting span. Reflection is
then a coverage check, not a vague request to “try again.”

### 3. Software maintenance

For repository changes, planning, tool use, tests, and review form a bounded
control loop. The sandbox contains side effects; the test gate turns failure
into a repair signal; the review boundary prevents a fluent but unverified
patch from becoming a merged change. The reality of this task shape is also
captured by the [SWE-bench benchmark](https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html),
which evaluates issue resolution against real repositories and tests.

### 4. Data and report generation

Parallelization is appropriate only when branches are independent and their
outputs can be normalized. A merge schema, provenance fields, and independent
validation are the architecture that turns several analyses into one auditable
deliverable.

### 5. Mathematical proof workflow

Proof generation and proof admission should have different responsibilities.
The generator may explore broadly, while the verifier emits a structured
verdict and repair hints. Only the correctness gate admits an artifact into a
fact graph or report. This is the same boundary documented in the
[Danus and Rethlas code case study](/posts/2026/08/agent-system/math-research-case-study/),
without exposing any private research framework.

## A practical selection rule

Choose a pattern from the operational problem:

- use routing when ownership, intent, or risk changes the next handler;
- use decomposition and retrieval when the initial context is incomplete;
- use planning, tools, and recovery when actions have side effects;
- use parallelization when work is independent and mergeable;
- use verification, checkpoints, or human review when an incorrect result is
  costly.

Then define the contract before choosing the model: input schema, intermediate
artifact, evidence format, evaluator, retry budget, and stopping rule. If those
items cannot be named, the “pattern” is probably only a slogan.

## Relation to the reference material

The architecture forms are teaching redraws synthesized from the course books:
Gulli’s [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Dibia’s [*Designing Multi-Agent Systems*](https://multiagentbook.com/),
Lakshmanan and Hapke’s [*Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/),
and Mitra’s [*System Design for the LLM Era*](https://www.packtpub.com/en-us/product/system-design-for-the-llm-era-9781807789923).
Their recurring structures are also visible in ReAct’s reasoning/action loop
([paper](https://arxiv.org/abs/2210.03629)), STORM’s evidence-oriented research
workflow ([paper](https://aclanthology.org/2024.naacl-long.347/)), and
Magentic-One’s orchestrator-led multi-agent workflow
([technical report](https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Magentic-One.pdf)).
The pattern vocabulary and cross-book comparison are collected on the
[reference map](/posts/2026/08/agent-system/reference-map/).

## Source rule

The named systems above are evidence for the existence of related structures;
they are not evidence that a proposed architecture will work automatically in
every domain. The five rows in this page are design templates. Any deployment
should validate its own quality, cost, safety, and failure behavior with a
domain-specific evaluation set.
