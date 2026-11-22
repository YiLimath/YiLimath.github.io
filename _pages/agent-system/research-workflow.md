---
title: "Agent Systems for Mathematical Research: A Working Protocol"
permalink: /posts/2026/08/agent-system/research-workflow/
classes: agent-system-page
full_page_reading: true
---

Use [the minimal-surface uniqueness workshop](/posts/2026/08/agent-system/birational-proof-workshop/) and its source packet. Use the surface uniqueness proof as the first complete episode, then select a cited proof in your own project. Locate the first failing application under a changed hypothesis and attempt a replacement lemma.

**Mathematical output:** A completed repair, meaningful partial theorem, or concrete obstruction; no novelty claim from a failed search.

**Value test:** preserve the direct-request baseline. Assess whether this intervention closes a previously unresolved obligation or reaches the same checked result with less measured work. Include retries and mathematical hints. This is a proposed exercise, not a reported improvement.



## Begin with a mathematical obligation

A useful research system must preserve the question while exploring ways to answer it. Consider this recurring task: a proof uses uniform convergence, but the target assumes only pointwise convergence. The assignment is to identify whether the step survives, find an applicable replacement, or isolate the missing lemma. Merely rewriting the same estimates is not progress.

Freeze the original target. Record the category, dimension, singularities, coefficient field, positivity assumptions, and whether the assertion is absolute or relative. Maintain a separate list of proposed additional hypotheses. A proof under a stronger assumption is a partial result, not completion of the original task.

## The shared artifact

Each task carries a statement version, available premises, one requested conclusion, an evidence bundle, unresolved obligations, and a stopping condition. Every derived claim names the exact versions of its premises. Literature records include theorem number, source version, exact hypotheses, and the proposed substitution of objects into the theorem.

| Pattern | Concrete research action | Required output and failure test |
|---|---|---|
| Chaining | Extract a theorem, align hypotheses, test its application | Stop when a hypothesis cannot be supplied |
| Routing | Separate source lookup, symbolic calculation, and proof review | Allow an unresolved route; do not guess a tool's competence |
| Parallel work | Search for a replacement theorem and construct obstructing examples | Merge evidence, not votes; preserve disagreement |
| Planning | Decompose the desired implication into lemmas | Expose all assumptions and detect circular dependencies |
| Retrieval | Locate the exact theorem behind a citation | A related abstract is not an applicable theorem |
| Representation change | Change coordinates, restrict a domain, or encode a formal statement | Supply both the forward construction and the return implication |
| Reflection | Challenge the weakest inference | Return a localized defect or a justified repair |
| Memory | Save a reusable result and its scope | Retrieval must retain qualifications and invalidation status |
| Recovery | Resume after a tool failure or a rejected lemma | Distinguish infrastructure failure from mathematical failure |
| Termination | Close a bounded attempt | Report proved, conditional, refuted, or unresolved separately |

## Execute one attempt

First retrieve the source and reconstruct its assumptions. Next build a table matching those assumptions to the current objects. For each unmatched row, open a proof obligation. Choose one bounded action: locate a replacement result, prove that hypothesis, or test a candidate obstruction. Save the resulting evidence even when the attempt fails.

A counterexample must satisfy every original hypothesis and violate the conclusion. Numerical tests can suggest one, but rounding and sampling cannot establish a universal assertion. An exact calculation proves only the statement encoded by that calculation; connecting it to the geometric question is a separate obligation.

Review the argument against the frozen target. A successful local lemma should be stored with its precise scope. If no route closes, return the smallest unresolved implication and the evidence ruling out attempted routes. Do not call this a solution.

## Evaluation before scaling

Build a small benchmark from problems with known arguments and deliberately damaged variants. Include a missing projectivity assumption, an unjustified descent, a circular lemma, and a source quotation with a deleted qualifier. Keep evaluation cases separate from prompts used to tune the system.

Measure correct diagnosis, false acceptance, reproducibility of citations, time to a useful partial result, and cost per independently reviewed obligation. Compare with one agent using the same tools and budget. Multiple roles are justified only if they improve these outcomes. Novel research has no known-answer benchmark: preserve the argument and arrange external mathematical review instead of reporting an automated success score.

## Reading the diagrams

A useful diagram answers a specific question: what artifact moves, what decision is made, what happens on failure, or which premises jointly imply a conclusion? Distinguish execution arrows from logical implication. A loop in search is normal; a cycle of unsupported proof dependencies is not. Decorative boxes labelled “reason”, “learn”, and “verify” do not specify these contracts.

## Sources and scope

The general workflow vocabulary follows Gulli, *Agentic Design Patterns*, Chapters 1–7 (the local attachment's contents were checked). [Anthropic's engineering account](https://www.anthropic.com/research/building-effective-agents) distinguishes predefined workflows from agent-directed execution and motivates starting with simpler compositions. The mathematical protocol and evaluation cases above are design recommendations, not empirical claims that these systems solve open problems. The [verification page](/posts/2026/08/agent-system/verification-gate/) explains the limits of model review and formal checking.

## Capstone practice

Complete one bounded research episode on a known theorem application with a deliberately removed hypothesis. Export the original target, source statement, hypothesis table, rejected routes, and final outcome. A search-budget stop must remain unresolved.

Use the [lab](/posts/2026/08/agent-system/hands-on-lab/) for record mechanics. Supply mathematical evidence separately.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
