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

How do we build a system that can work on a mathematical problem, explain its progress, and keep track of what remains unproved?

This course develops the answer in **nine modules**. We begin with the mathematical objects the system must represent, then add search, literature, verification, formalization, memory, coordination, and evaluation. Each module combines a design idea, a worked example, and a small implementation task.

**For self-study:** follow the modules in order on your first pass. **For teaching:** use one or two meetings per module, depending on the audience and the time available for laboratories. The modules also work as individual lessons once their prerequisites are covered.

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
    <strong>Set up the small Python workbench</strong>
    <span>The reference code runs without an API key. Its limitations are part of the lesson.</span>
    <span class="research-card-link">Open the laboratory →</span>
  </a>
</div>

**Background.** You should be comfortable reading and writing proofs. Basic Python is enough for the implementation exercises. The introductory examples need no algebraic geometry; the section-lifting case and the final birational-geometry project can be taught as advanced options.

## The rule for including a design idea

**Teach a mechanism because it solves a real problem, and test whether it helps.** Knowing a pattern's name is not a learning outcome. A useful outcome is catching a missing hypothesis, avoiding an invalid theorem application, recovering interrupted work, or finding a better proof route at an acceptable cost.

Before adding a component, answer four questions:

1. What concrete failure does the simpler system have?
2. What is the smallest change that could address it?
3. What experiment would show a benefit—and what extra cost does it introduce?
4. When should we leave it out or remove it?

The core course concerns problems any sustained mathematical workflow can encounter. Multiple workers, elaborate routing, and adaptive policies are **optional mechanisms**, not requirements for a good system. A single-worker capstone is entirely sufficient. Some mathematical specializations in this series are design proposals: students should test them rather than assume their effectiveness.

## The course at a glance

Follow the sequence to build one system progressively. Each module adds a capability to the same research workbench.

1. [Represent the mathematics](#module-1) — statements, assumptions, arguments, and open questions.
2. [Plan and search](#module-2) — turn a strategy into tasks and alternative routes.
3. [Use the literature](#module-3) — find results and check that they apply.
4. [Change the viewpoint](#module-4) — transform a problem without losing the way back.
5. [Review and admit results](#module-5) — decide what evidence permits reuse.
6. [Formalize a proof](#module-6) — use Lean and audit what a checked proof establishes.
7. [Remember and recover](#module-7) — preserve versions, alternatives, and unfinished work.
8. [Coordinate the work](#module-8) — an optional extension when one worker is not enough.
9. [Evaluate and assemble](#module-9) — test the complete system on a mathematical task.

## Module guide

Open a module for its teaching sequence and assignment. Module 1 is expanded to help you get started.

<details id="module-1" class="research-chapter-group" markdown="1" open>
<summary><span class="research-part-number">Module 1</span> Represent the mathematics</summary>

**Before this module:** None beyond the course introduction.

**By the end:** Distinguish a mathematical statement from an argument for it, and make assumptions and unresolved obligations visible.

### Teaching sequence

1. [Start with statements, arguments, and obligations](/posts/2026/08/agent-system/foundations/).
2. [Turn those distinctions into records](/posts/2026/08/agent-system/structured-output/).
3. [Decide what must stay stable as implementations change](/posts/2026/08/agent-system/variation-points/).
4. [Choose the information each task needs](/posts/2026/08/agent-system/context-engineering/).

**Work through:** Use the elementary maximum example first. Then contrast “lift this chosen section” with “find some nonzero section” in Case A. The similar wording hides different targets.

**Build:** Create versioned records for a target, two premises, and one candidate argument. Include one intentionally false argument that still fits the schema.

**Check your understanding:** Explain why a well-formed record does not establish mathematical correctness.

**Laboratory connection:** Stage 1; inspect the introductory ledger before the advanced workbench.

</details>

<details id="module-2" class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">Module 2</span> Plan and search</summary>

**Before this module:** Module 1.

**By the end:** Represent joint premises and alternative arguments, and choose the next useful research action.

### Teaching sequence

1. [Follow one obligation through a research iteration](/posts/2026/08/agent-system/core-loop/).
2. [Build a plan with AND premises and OR alternatives](/posts/2026/08/agent-system/plan-and-execute/).
3. [Separate the stages of a theorem application](/posts/2026/08/agent-system/prompt-chaining/).
4. Optional: [Choose a capability by the evidence needed](/posts/2026/08/agent-system/router/).
5. [Use probes and counterexamples to guide search](/posts/2026/08/agent-system/exploration-and-discovery/).
6. [Allocate a finite search budget](/posts/2026/08/agent-system/resource-aware-optimization/).

**Work through:** Case C exposes an unsupported cycle. Case A supplies two routes to the same target: sufficient vanishing or a direct obstruction calculation.

**Build:** Build a dependency plan and execute a bounded sequence of actions. Include a branch that fails and a decision to try an alternative.

**Check your understanding:** Show that a loop in execution cannot supply a missing logical premise.

**Laboratory connection:** Stages 1 and 4. Introduce the distinction between the simple ledger and grounded closure.

</details>

<details id="module-3" class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">Module 3</span> Use the literature</summary>

**Before this module:** Modules 1–2.

**By the end:** Turn a relevant source into an explicitly justified theorem application.

### Teaching sequence

1. [Extract a theorem and match its hypotheses](/posts/2026/08/agent-system/knowledge-retrieval/).
2. [Search systematically and preserve rejected matches](/posts/2026/08/agent-system/deep-search/).

**Work through:** Find a theorem whose conclusion looks useful but whose hypotheses do not match. Use compactness for an introductory class or a vanishing theorem in Case A for an advanced class.

**Build:** Produce a source record, a hypothesis-by-hypothesis applicability table, and a rejected near-match. Fix the search budget in advance.

**Check your understanding:** State exactly what the source establishes and what the current application still requires.

**Laboratory connection:** Prepare the source evidence used in Stage 7. The workbench does not implement a literature-search engine; this artifact can be prepared manually.

</details>

<details id="module-4" class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">Module 4</span> Change the viewpoint</summary>

**Before this module:** Modules 1–3.

**By the end:** Track a construction, its new obligations, and the implication returning to the original target.

### Teaching sequence

1. [Write a transformation and return contract](/posts/2026/08/agent-system/reasoning/).
2. [Use calculations and tools through explicit contracts](/posts/2026/08/agent-system/tool-use/).
3. [Read Sections 1–5 on methods and proof blueprints](/posts/2026/08/agent-system/proof-sketch-system/).

**Work through:** Use Case B to distinguish separate bounds from a uniform bound. For an advanced audience, use Case A to distinguish a sufficient vanishing condition from the exact obstruction to lifting.

**Build:** Write a method card with preconditions, expected subgoals, and a return argument. Leave one bridge deliberately open and label the result as partial.

**Check your understanding:** Identify what was solved on the transformed problem and why that does—or does not—solve the original problem.

**Laboratory connection:** Extend Stage 1 with a transformation record; use Stage 6 to challenge its mathematical content.

</details>

<details id="module-5" class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">Module 5</span> Review and admit results</summary>

**Before this module:** Modules 1–4.

**By the end:** Separate critique, evidence kind, conditional scope, and permission to use a result as a premise.

### Teaching sequence

1. [Localize the failed inference](/posts/2026/08/agent-system/reflection/).
2. [Define an admission policy with explicit evidence types](/posts/2026/08/agent-system/verification-gate/).

**Work through:** A reviewer catches the quantifier interchange in Case B. A changed section in Case A invalidates a review of the old lifting argument.

**Build:** Attach a report to an exact argument version. Test stale reviews, conditional conclusions, and a policy requiring formal evidence.

**Check your understanding:** Explain why a model review, a passing software test, and a kernel-checked term provide different assurances.

**Laboratory connection:** Stages 3, 5, and 6. Run the deliberately false-mathematics fixture and explain why its software test passes.

</details>

<details id="module-6" class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">Module 6</span> Formalize a proof with Lean</summary>

**Before this module:** Modules 1–5. No previous Lean knowledge is needed.

**By the end:** Read a proof state, complete an elementary proof, and distinguish compilation from acceptable formal evidence.

### Teaching sequence

1. [Translate a quantifier distinction into Lean](/posts/2026/08/agent-system/lean-formalization/).
2. Follow the witness construction and the proof that no uniform bound exists.
3. Run a type error, a `sorry` placeholder, and an extra-axiom example.
4. Compare the intended statement with the formal declaration and inspect its dependencies.

**Build:** Complete the [Lean laboratory](/files/lean-reasoning-lab.zip) and submit an admission report tied to the exact declaration and toolchain.

**Check your understanding:** Explain why a correct proof of the wrong statement, or compilation using an unapproved axiom, does not satisfy the research task.

**Laboratory connection:** This separate project supplies real formal evidence. The Python workbench's evidence labels alone do not invoke Lean or validate a proof.

</details>

<details id="module-7" class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">Module 7</span> Remember and recover</summary>

**Before this module:** Modules 1–2 and 5.

**By the end:** Retain useful evidence through revisions, withdrawals, and interrupted execution.

### Teaching sequence

1. [Store alternative arguments and conditional results](/posts/2026/08/agent-system/memory-management/).
2. [Classify failures before retrying](/posts/2026/08/agent-system/exception-recovery/).
3. [Save and restore research state](/posts/2026/08/agent-system/production-architecture/).

**Work through:** Withdraw one Case A route while leaving the other intact. Then withdraw a shared premise. Compare both with an operational timeout.

**Build:** Save a snapshot, reload it, and reproduce the same report. Change saved mathematical content and confirm that the old review no longer matches.

**Check your understanding:** Distinguish withdrawing an argument from refuting its conclusion, and a tool failure from a mathematical obstruction.

**Laboratory connection:** Stages 2, 3, and 5. Discuss the reference implementation’s single-writer and authentication limitations.

</details>

<details id="module-8" class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">Module 8 · Optional extension</span> Coordinate the work</summary>

**Before this module:** Modules 1–3 and 5–7.

**By the end:** Add collaborators only where the division of work has a clear mathematical and operational benefit.

### Teaching sequence

1. [Merge alternative routes without voting on truth](/posts/2026/08/agent-system/parallelization/).
2. [Assign evidence-producing responsibilities](/posts/2026/08/agent-system/multiple-agent-cooperation/).
3. [Exchange versioned tasks and reports](/posts/2026/08/agent-system/inter-agent-communication/).
4. [Handle changes in research direction](/posts/2026/08/agent-system/human-in-the-loop/).
5. [Separate proposals, evidence, and authority](/posts/2026/08/agent-system/guardrails-safety/).

**Work through:** Assign Case A’s source check and obstruction route to different workers. Introduce a delayed report for an outdated statement version.

**Build:** Compare a sequential workflow with two workers under the same total budget. Preserve disagreements and count duplicated work.

**Check your understanding:** Explain what the additional worker improved and what coordination cost it introduced.

**Laboratory connection:** Stage 7. A scripted worker is sufficient to test the protocol before using a model.

</details>

<details id="module-9" class="research-chapter-group" markdown="1">
<summary><span class="research-part-number">Module 9</span> Evaluate and assemble</summary>

**Before this module:** Modules 1–7. Include Module 8 only if your project needs multiple workers.

**By the end:** Judge the architecture by useful mathematical progress, reproducibility, and its treatment of invalid arguments.

### Teaching sequence

1. [Define completion against the original target](/posts/2026/08/agent-system/goal-monitoring/).
2. [Build valid and invalid evaluation cases](/posts/2026/08/agent-system/evaluation-monitoring/).
3. Optional: [Improve policies without rewriting evidence](/posts/2026/08/agent-system/learning-and-adaptation/).
4. [Draw the semantic, logical, execution, and operational views](/posts/2026/08/agent-system/architecture-views/).
5. [Remove mechanisms that do not help](/posts/2026/08/agent-system/choosing-patterns/).
6. [Assemble a complete research episode](/posts/2026/08/agent-system/research-workflow/).

**Work through:** Vary the section, constant dependence, and induction base across the three cases. Include valid controls so that rejecting everything cannot count as success.

**Build:** Complete the capstone below. Compare your system with a simpler baseline and report at least one failure honestly.

**Check your understanding:** Separate software correctness, mathematical correctness, and research usefulness in the final evaluation.

**Laboratory connection:** Stage 8. Reuse the workbench tests, then add domain-specific fixtures.

</details>

## A repeatable lesson format

Begin with a mathematical attempt that almost works, or a recorded failure from a real workflow. Ask students to locate the missing distinction or implication before introducing the architecture. Draw the relevant records or dependencies, implement the smallest useful mechanism, and test it on both a valid case and a damaged variant.

End each meeting with three questions: **What did this mechanism improve? What does it establish? What does it still trust?** If it added complexity without a useful benefit, simplify or remove it. Keep the resulting artifacts; they become inputs to the next module.

## The final project

Choose a short published proof that you understand. Build a system that records its target, theorem applications, intermediate arguments, and one substantive transformation. Then create two damaged variants: one with a missing hypothesis and one with an invalid return argument.

Submit the original mathematical task, your records and diagrams, a reproducible run, review reports, and an evaluation against a simpler baseline. The assessment should reward a correct and useful partial result, clear diagnosis, and honest uncertainty—not just a successful-looking final answer.

### Optional advanced modules

These can follow Module 9 or replace a project session for a specialist audience:

- [Method recommendation and proof-sketch systems](/posts/2026/08/agent-system/proof-sketch-system/) — develop the full architecture introduced in Module 4.
- [Birational geometry and spiraling induction](/posts/2026/08/agent-system/birational-geometry-agent/) — apply the contracts to geometric reductions and theorem packages.
- [Danus and Rethlas](/posts/2026/08/agent-system/math-research-case-study/) — audit the boundaries in reported implementations.

## Use the course modularly

For a **conceptual seminar**, emphasize Modules 1, 2, 4, 5, 6, and 9, with diagrams and written arguments replacing code. For an **implementation workshop**, follow all nine modules and carry the same workbench forward. A **reading group** can assign one module per meeting and compare solutions to its exercise.

These are teaching formats, not different standards of mathematical evidence. In every format, keep the target, assumptions, and remaining obligations visible.

### Sources and further reading

See [why explicit architecture matters](/posts/2026/08/agent-system/why-mathematicians-need-patterns/) for motivation and [books, primary sources, and claim boundaries](/posts/2026/08/agent-system/sources-and-claims/) for references.

*Written in cooperation with AI. Proposed architectures, teaching code, informal reviews, and formally checked results are distinguished throughout the series.*

<script>
(function () {
  function revealModule(hash) {
    var module = document.getElementById(hash.slice(1));
    if (module && module.matches('details.research-chapter-group')) module.open = true;
  }
  document.addEventListener('click', function (event) {
    var link = event.target.closest('a[href^="#module-"]');
    if (link) revealModule(link.getAttribute('href'));
  });
  window.addEventListener('hashchange', function () { revealModule(window.location.hash); });
  revealModule(window.location.hash);
}());
</script>
