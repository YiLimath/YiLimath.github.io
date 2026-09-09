---
title: "Agent Systems: Exploration and Discovery"
permalink: /posts/2026/08/agent-system/exploration-and-discovery/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Exploration and discovery workflow](/images/agent-system/22-exploration-discovery.svg)

*Figure: course redraw of the pattern. The architecture makes the candidate
frontier, worker roles, evidence ledger, and termination gate explicit; it is
not a reproduction of the book's conceptual visual summary.*

**In one sentence.** Search deliberately over candidates with an explicit test and a stopping rule; exploration produces evidence, never proof.

## Problem

A single greedy line of reasoning can miss useful cases, counterexamples, or
alternative proof strategies. Open-ended exploration can also spend resources
without producing new information.

## Intent and structure

`seed → branch or mutate → test → retain evidence → select or stop`

The candidate representation, test procedure, scoring rule, and termination
condition must be explicit. Exploration is a search procedure; it is not itself
proof.

## Mathematical uses

Use the pattern to generate conjectures, search examples, compare proof
strategies, or explore neighboring definitions. Candidate records should retain
the assumptions tested, the computation or argument used, and the reason for
retaining or discarding the candidate.

## Forces and failure modes

Breadth improves discovery but creates combinatorial growth, duplicate
candidates, and selection bias. Beam limits, diversity criteria, counterexample
tests, budgets, and human review keep the process meaningful.

## Design question

What new evidence justifies expanding the search, and what evidence justifies
stopping it?

## Real-world application

For product discovery or scientific search, several candidate explanations can
be explored in parallel and tested against examples or counterexamples. The
system should preserve discarded branches and apply a budgeted selection rule,
so novelty does not replace evidence.

## Reference basis

The source pattern is Antonio Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3), Chapter 21.
The branch-evaluate-prune structure, with an explicit state evaluator and search
budget, is Pattern 14 in Lakshmanan and Hapke, [*Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/),
after Yao et al., [Tree of Thoughts](https://arxiv.org/abs/2305.10601). The
six-role decomposition in the figure follows the published description of
Google Research's [AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/): Generation,
Reflection, Ranking, Evolution, Proximity, and Meta-review coordinated by a
Supervisor. For a research workflow that makes perspective discovery, source
gathering, and outline curation concrete, compare the [STORM paper](https://aclanthology.org/2024.naacl-long.347/).
