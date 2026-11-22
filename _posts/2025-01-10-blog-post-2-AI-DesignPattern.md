---
title: 'Designing Reasoning Systems for Mathematical Research'
date: 2026-12-01
permalink: /posts/2026/12/Agent-System/
tags:
  - Agent System
classes: agent-system-hub
full_page_reading: true
---

How do we build a system that can work on a mathematical problem, explain its progress, and keep track of what remains unproved?

This course develops the answer in **nine modules**. We begin with the mathematical objects the system must represent, then add search, literature, verification, formalization, memory, coordination, and evaluation. Each module combines a design idea, a worked example, and a direct experiment in ChatGPT or Codex.


## Before the first module

<div class="research-start-grid">
  <a class="research-start-card" href="/posts/2026/08/agent-system/design-principles/">
    <span class="research-card-step">Course orientation</span>
    <strong>What are we trying to design?</strong>
    <span>Start with a simple proof attempt and see why preserving the problem matters.</span>
    <span class="research-card-link">Read the introduction →</span>
  </a>
  <a class="research-start-card" href="/posts/2026/08/agent-system/research-cases/">
    <span class="research-card-step">Shared examples</span>
    <strong>Meet the three running cases</strong>
    <span>Section lifting, uniform estimates, and induction connect the modules.</span>
    <span class="research-card-link">Explore the cases →</span>
  </a>
  <a class="research-start-card" href="/posts/2026/08/agent-system/hands-on-lab/">
    <span class="research-card-step">Practical materials</span>
    <strong>Experiment in ChatGPT or Codex</strong>
    <span>Investigate real examples, preserve evidence, and challenge the results. No programming is required.</span>
    <span class="research-card-link">Open the laboratory →</span>
  </a>
</div>

**Background.** No background is needed.


## The course at a glance

Follow the sequence using one research record in ChatGPT or Codex. Each module tests another part of the same mathematical workflow.

1. [Represent the mathematics](/posts/2026/08/agent-system/foundations/) — statements, assumptions, arguments, and open questions.
2. [Plan and search](/posts/2026/08/agent-system/plan-and-execute/) — turn a strategy into tasks and alternative routes.
3. [Use the literature](/posts/2026/08/agent-system/knowledge-retrieval/) — find results and check that they apply.
4. [Change the viewpoint](/posts/2026/08/agent-system/reasoning/) — transform a problem without losing the way back.
5. [Review and admit results](/posts/2026/08/agent-system/verification-gate/) — decide what evidence permits reuse.
6. [Formalize a proof](/posts/2026/08/agent-system/lean-formalization/) — use Lean and audit what a checked proof establishes.
7. [Remember and recover](/posts/2026/08/agent-system/memory-management/) — preserve versions, alternatives, and unfinished work.
8. [Coordinate the work](/posts/2026/08/agent-system/multiple-agent-cooperation/) — an optional extension when one worker is not enough.
9. [Evaluate and assemble](/posts/2026/08/agent-system/evaluation-monitoring/) — test the complete system on a mathematical task.

## A repeatable lesson format

Begin with a mathematical attempt that almost works, or a recorded failure from a real workflow. Ask students to locate the missing distinction or implication before introducing the architecture. Draw the relevant records or dependencies, try the smallest useful change to the workflow, and test it on both a valid case and a damaged variant.

End each meeting with three questions: **What did this mechanism improve? What does it establish? What does it still trust?** If it added complexity without a useful benefit, simplify or remove it. Keep the resulting artifacts; they become inputs to the next module.

## The final project

Follow [From an empty folder to a mathematical research system in Codex](/posts/2026/08/agent-system/codex-research-studio/). Build the workflow through instructions and inspectable records, without implementing an agent framework. Use the experiments to decide whether added sophistication actually helps.


Choose a short published proof that you understand. Build a system that records its target, theorem applications, intermediate arguments, and one substantive transformation. Then create two damaged variants: one with a missing hypothesis and one with an invalid return argument.

Submit the original mathematical task, your records and diagrams, a reproducible run, review reports, and an evaluation against a simpler baseline. The assessment should reward a correct and useful partial result, clear diagnosis, and honest uncertainty—not just a successful-looking final answer.

### Optional advanced modules

Start with a concrete mathematical task, build the workflow directly in Codex, and evaluate its actual output. The linked chapters contain proposed designs and historical examples; neither a diagram nor a written protocol establishes that a system works. Each project below has a specific deliverable.

- [Find a research opportunity worth pursuing](/posts/2026/08/agent-system/research-opportunity-system/) — search your authorized vault, database, and accessible literature; identify a precise theorem to improve, check the closest prior work, and attempt the hardest new bridge. **Deliverable:** a research proposal with a completed feasibility probe, explicit gaps, and reasons to proceed or stop.
- [Turn a proposed method into a testable proof plan](/posts/2026/08/agent-system/proof-sketch-system/) — compare two methods for the same target, check their hypotheses, and attempt a decisive intermediate lemma in Codex. **Deliverable:** an inspectable proof plan, the actual lemma attempt, and a mathematically justified rejection or revision of an unsuitable route.
- [Audit a birational argument and its induction](/posts/2026/08/agent-system/birational-geometry-agent/) — reconstruct one known geometric reduction before attempting a generalization. Track the objects, theorem hypotheses, induction order, base cases, and argument returning to the original target. **Deliverable:** a checked reconstruction and a precise diagnosis of what fails when a hypothesis or base case is removed.
- [Build and evaluate a Codex research workflow](/posts/2026/08/agent-system/math-research-case-study/) — use Danus and Rethlas as architectural references, then build a small workflow with alternative arguments, versioned reviews, and recovery. **Deliverable:** complete research traces and a comparison with ordinary chat on valid and damaged cases. Claims of improvement over a named system require a direct, documented comparison.

For each project, begin with the [from-zero Codex workspace](/posts/2026/08/agent-system/codex-research-studio/). Keep prompts, source material, actual outputs, and failed attempts. Add a component only when an observed problem justifies it; label untested extensions as proposals.

## Use the course modularly

For a **conceptual seminar**, emphasize Modules 1, 2, 4, 5, 6, and 9, with diagrams and written arguments. For a **hands-on workshop**, follow all nine modules in ChatGPT or Codex and carry the same research record forward. A **reading group** can assign one module per meeting and compare solutions to its exercise.

These are teaching formats, not different standards of mathematical evidence. In every format, keep the target, assumptions, and remaining obligations visible.

### Sources and further reading

See [why explicit architecture matters](/posts/2026/08/agent-system/why-mathematicians-need-patterns/) for motivation and [books, primary sources, and claim boundaries](/posts/2026/08/agent-system/sources-and-claims/) for references.

*Written in cooperation with AI. Proposed architectures, teaching code, informal reviews, and formally checked results are distinguished throughout the series.*
