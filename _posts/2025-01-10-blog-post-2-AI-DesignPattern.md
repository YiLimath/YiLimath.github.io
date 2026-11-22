---
title: 'Designing Reasoning Systems for Mathematical Research'
date: 2026-08-01
permalink: /posts/2026/12/Agent-System/
tags:
  - Agent System
classes: agent-system-hub
full_page_reading: true
redirect_from:
  - /posts/2026/08/Agent-System/
---

How do we build an AI system that can help with a mathematical problem over days or weeks—while keeping track of what has been proved, what is only a promising idea, and what still needs work?

This series approaches that question through **system design**. We will study how to represent a problem, organize proof attempts, use the literature, check arguments, and recover when a promising route fails. The principles should remain useful as models and tools improve.

You do not need to read every chapter in order. Start with the introduction, then follow the questions that matter to your work.

## A good place to begin

<div class="research-start-grid">
  <a class="research-start-card" href="/posts/2026/08/agent-system/design-principles/">
    <span class="research-card-step">1 · Get the big picture</span>
    <strong>What does the system need to preserve?</strong>
    <span>Meet the central ideas through a simple example: a plausible argument with a missing hypothesis.</span>
    <span class="research-card-link">Read the introduction →</span>
  </a>
  <a class="research-start-card" href="/posts/2026/08/agent-system/research-cases/">
    <span class="research-card-step">2 · See the mathematics</span>
    <strong>Follow three recurring research problems</strong>
    <span>Lifting a section, finding a uniform estimate, and organizing induction show why the design matters.</span>
    <span class="research-card-link">Explore the cases →</span>
  </a>
  <a class="research-start-card" href="/posts/2026/08/agent-system/hands-on-lab/">
    <span class="research-card-step">3 · Build something small</span>
    <strong>Try the research workbench</strong>
    <span>Run a small Python project, break its assumptions, and see what its checks can—and cannot—establish.</span>
    <span class="research-card-link">Open the hands-on lab →</span>
  </a>
</div>

**Prefer a short reading route?** After the introduction, read [representing mathematical work](/posts/2026/08/agent-system/foundations/), [planning a proof](/posts/2026/08/agent-system/plan-and-execute/), and [checking what may be reused](/posts/2026/08/agent-system/verification-gate/). Then try the lab. This gives you the central structure before you explore the specialized patterns.

## Three questions we will keep returning to

- **Can a result on a simpler object solve the original problem?** A section on a divisor still needs an argument that lifts it to the ambient space.
- **Does an estimate survive the limiting process?** A bound for each approximation is not necessarily a uniform bound.
- **Do the lemmas really support each other?** An induction needs a starting point and a well-founded order; a circle of references is not enough.

These cases connect the chapters. You will see the same problem from the perspectives of planning, retrieval, verification, and memory, rather than starting from scratch with each pattern.

## Explore the chapters

Choose a question below to open its chapters. Each chapter explains one design decision and ends with an exercise. You can keep the [laboratory](/posts/2026/08/agent-system/hands-on-lab/) open alongside your reading.

<details class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">01</span> How should the system represent mathematics?</summary>

Start here if you want to understand the basic objects that every later component works with.

- [Statements, arguments, and open questions](/posts/2026/08/agent-system/foundations/) — Keep a claim separate from the evidence supporting it.
- [What stays stable when the model changes?](/posts/2026/08/agent-system/variation-points/) — Design interfaces that preserve mathematical meaning.
- [Useful structure for mathematical records](/posts/2026/08/agent-system/structured-output/) — Understand what a schema can check and what requires reasoning.
- [Give each task the context it needs](/posts/2026/08/agent-system/context-engineering/) — Summarize without losing hypotheses or unresolved assumptions.

</details>

<details class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">02</span> How should it search for a proof?</summary>

Turn a promising idea into explicit tasks, and keep alternatives available when one route fails.

- [One useful research step](/posts/2026/08/agent-system/core-loop/) — Make each iteration change an identifiable open question.
- [Plans, premises, and alternative arguments](/posts/2026/08/agent-system/plan-and-execute/) — Represent what must be proved together and what can be tried instead.
- [Break a theorem application into stages](/posts/2026/08/agent-system/prompt-chaining/) — Inspect the source, match its hypotheses, and derive the right conclusion.
- [Choose the right kind of help](/posts/2026/08/agent-system/router/) — Separate literature questions, calculations, and proof checks.
- [Explore several routes at once](/posts/2026/08/agent-system/parallelization/) — Combine evidence without confusing agreement with correctness.
- [Use examples to learn something](/posts/2026/08/agent-system/exploration-and-discovery/) — Find obstructions and preserve the exact scope of a counterexample.
- [Change the viewpoint—and return to the target](/posts/2026/08/agent-system/reasoning/) — Track what a reduction actually proves about the original problem.
- [Decide where to spend effort](/posts/2026/08/agent-system/resource-aware-optimization/) — Work on the uncertainty most likely to change the argument.

</details>

<details class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">03</span> What can it trust, remember, and reuse?</summary>

A growing collection of results is useful only when their assumptions and evidence remain visible.

- [Find a theorem that really applies](/posts/2026/08/agent-system/knowledge-retrieval/) — Go beyond relevance to check the exact hypotheses.
- [Search the literature systematically](/posts/2026/08/agent-system/deep-search/) — Leave a useful record of sources, rejected matches, and remaining leads.
- [Remember arguments, not just conclusions](/posts/2026/08/agent-system/memory-management/) — Keep alternative proofs and handle withdrawn evidence.
- [Make criticism actionable](/posts/2026/08/agent-system/reflection/) — Identify the failed inference and a concrete repair.
- [Decide when a result may become a premise](/posts/2026/08/agent-system/verification-gate/) — Distinguish informal review, formal checking, and conditional use.

</details>

<details class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">04</span> How should people, agents, and tools work together?</summary>

Assign clear responsibilities and make handovers preserve the mathematical task.

- [Divide the work usefully](/posts/2026/08/agent-system/multiple-agent-cooperation/) — Give each worker an evidence-producing task.
- [Exchange precise mathematical work](/posts/2026/08/agent-system/inter-agent-communication/) — Keep reports tied to the right objects and versions.
- [Keep control of the research direction](/posts/2026/08/agent-system/human-in-the-loop/) — Handle changes of scope without requiring approval at every step.
- [Protect the evidence and the workspace](/posts/2026/08/agent-system/guardrails-safety/) — Separate source text, proposed actions, and permission to act.

</details>

<details class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">05</span> How will we know whether the system works?</summary>

Test useful progress as carefully as failure, and make the work recoverable.

- [Know what “finished” means](/posts/2026/08/agent-system/goal-monitoring/) — Report partial results and remaining obligations honestly.
- [Evaluate mathematical progress](/posts/2026/08/agent-system/evaluation-monitoring/) — Measure valid work and false acceptance together.
- [Recover from the right kind of failure](/posts/2026/08/agent-system/exception-recovery/) — Distinguish a broken tool from a mathematical obstruction.
- [Improve search without changing the facts](/posts/2026/08/agent-system/learning-and-adaptation/) — Learn useful preferences while preserving evidence.
- [Resume work reliably](/posts/2026/08/agent-system/production-architecture/) — Persist the target, arguments, and reviews across interruptions.
- [Draw a diagram that answers a question](/posts/2026/08/agent-system/architecture-views/) — Separate logical dependencies from execution and deployment.
- [Choose the smallest useful design](/posts/2026/08/agent-system/choosing-patterns/) — Add a mechanism only when it addresses a concrete failure.

</details>

<details class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">06</span> How do the pieces fit into a research system?</summary>

Read these longer chapters after the foundations, or use them as reference designs for your own project.

- [A complete research workflow](/posts/2026/08/agent-system/research-workflow/) — Follow a task from its original statement to a useful outcome.
- [Recommend methods and develop proof sketches](/posts/2026/08/agent-system/proof-sketch-system/) — Turn candidate techniques into explicit obligations.
- [A system for birational geometry](/posts/2026/08/agent-system/birational-geometry-agent/) — Organize geometric reductions, induction, and return arguments.
- [Danus and Rethlas](/posts/2026/08/agent-system/math-research-case-study/) — Compare the design principles with reported systems.

</details>

## Make the ideas your own

Pick a short proof you already understand. Represent its target and intermediate claims, remove one hypothesis, and see whether your design exposes the gap. Then try a different proof route. The [eight-stage lab](/posts/2026/08/agent-system/hands-on-lab/) walks you through this process with runnable code and reference results.

The goal is a system whose work you can inspect: what it tried, why an argument works, which assumptions it needs, and where it got stuck.

### Further reading

- [Why explicit architecture matters](/posts/2026/08/agent-system/why-mathematicians-need-patterns/) — a short explanation of the motivation.
- [Books, primary sources, and claim boundaries](/posts/2026/08/agent-system/sources-and-claims/) — where the ideas come from and what the examples establish.

*Written in cooperation with AI. Proposed architectures, teaching code, informal reviews, and formally checked results are distinguished throughout the series.*
