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


## Design for a future without routine human proof checking

**The long-term goal is a system that discovers and constructs proofs autonomously, while acceptance rests on mechanically checkable evidence.** Human-written proofs and line-by-line human verification need not remain mandatory steps for a precisely formalized target. Stronger AI should expand what can be discovered and formalized, rather than become an authority whose assertions must be trusted.

The stable architecture separates **specification, proof generation, checking, and admission**. Fix the intended formal target and definitions; let agents explore; require a proof term or an appropriate checkable certificate; admit the result only after validation under an explicit foundation and dependency policy. This does not guarantee that proof search will succeed or finish.

Formal checking establishes the encoded theorem relative to its foundations. It does not, by itself, establish that the encoding expresses the intended research question. Semantic alignment and the trusted computing base remain explicit boundaries; they are not an assertion that humans must personally inspect every future proof. Once a formal specification is established, routine checking and admission can be automated. [Module 6](/posts/2026/08/agent-system/lean-formalization/#8-build-an-admission-path-without-routine-human-proof-review) develops this architecture and its failure tests.

The early informal exercises teach these distinctions with accessible mathematics. They are stepping stones toward proof-producing systems, not a permanent requirement for human sign-off.

### What to learn for stronger future models

| Likely to change with capabilities | Design knowledge that remains useful |
|---|---|
| How much proof construction, formalization, and coordination can be delegated | How to specify the exact task and preserve its meaning across transformations |
| Which model, agent framework, or prover interface performs the work | How to bind evidence to a target, its definitions, dependencies, and checking environment |
| How much routine human reading is practical or necessary | How to define an acceptance policy, automate checking, and measure actual mathematical progress |

A future system may produce proofs too numerous or lengthy for routine human inspection. Explanations can still support understanding and research choice, while acceptance relies on validated proof evidence. Learn to design that separation. Today's ChatGPT, Codex, and Lean exercises are concrete ways to learn it; their interfaces are not the curriculum's endpoint.

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
    <span>Prescribed outputs, uniform estimates, and induction connect the modules.</span>
    <span class="research-card-link">Explore the cases →</span>
  </a>
  <a class="research-start-card" href="/posts/2026/08/agent-system/hands-on-lab/">
    <span class="research-card-step">Practical materials</span>
    <strong>Experiment in ChatGPT or Codex</strong>
    <span>Investigate real examples, preserve evidence, and challenge the results. No programming is required.</span>
    <span class="research-card-link">Open the laboratory →</span>
  </a>
</div>

**Background.** Begin with equations, functions, and basic logical reasoning. Linear algebra and introductory analysis are recalled where needed. No algebraic geometry is assumed.


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

## The final project: design and run a research programme

Choose a research direction supported by papers you can actually inspect. Build a Codex workspace from zero and use it to select a precise candidate theorem, investigate competing proof routes, and produce a reviewed mathematical result or a substantive obstruction. No Python framework is required.

1. **Discover and justify the target.** Audit at least three relevant sources, compare two possible improvements, and explain why one deserves investigation. Record the limits of the novelty search.
2. **Reconstruct a known argument.** Reproduce the source proof step your extension depends on. Locate exactly where the changed hypothesis matters.
3. **Develop competing routes.** Give two distinct proof plans with applicability conditions, dependency records, and return arguments. Attempt a decisive lemma for each before choosing a route to pursue.
4. **Produce substantive mathematics.** Establish a nontrivial intermediate result, a meaningful special case, or a counterexample or obstruction that decisively changes the proposal. A list of potential lemmas is insufficient.
5. **Test the research system.** Introduce a stale review, withdraw a premise, and restart from a checkpoint. Compare the actual behavior with an ordinary-chat baseline using comparable evidence and effort.
6. **Defend the outcome.** Submit a short research report, source audit, full experiment traces, reviewed arguments, remaining gaps, and a concrete next research session. Include one failure and explain the design change it motivates.

Use [the from-zero Codex workspace](/posts/2026/08/agent-system/codex-research-studio/) and select the advanced projects below as needed. Formalize one useful local lemma when suitable definitions and tools are available; document the actual execution and its limited scope. Do not force a toy formalization unrelated to the research bottleneck.

The project is challenging because it requires mathematical progress and an evaluated workflow, not because it has many agents. A new publishable theorem is an ambitious outcome, not a guaranteed grading requirement. A rigorous partial result or decisive negative result can pass; an unsupported claim of novelty or a weakened target presented as solved cannot.

### Optional advanced modules

These four research workshops extend the core course. Each introduces a distinct technical problem, a worked mathematical analysis, a Codex construction exercise, and a research-level assessment. Classroom controls establish that the workflow is understandable; the final submission must also engage with an actual paper.

| Workshop | Technical core | Research submission |
|---|---|---|
| **A. [Research opportunity discovery](/posts/2026/08/agent-system/research-opportunity-system/)** | Compare theorem changes; maintain competing candidates; design probes that change a research decision | Three source-grounded candidates, a prior-art audit, an attempted new lemma, and justified pursue/defer/reject decisions |
| **B. [Method recommendation and proof search](/posts/2026/08/agent-system/proof-sketch-system/)** | Positive and negative witnesses; complete finite-dimensional obstruction analysis; interpolation compatibility and sharp perturbation bounds | Two eligible methods for a source-dependent target, checked evidence, and an attempted decisive bridge |
| **C. [Coordinate changes and well-founded reductions](/posts/2026/08/agent-system/birational-geometry-agent/)** | Track an inverse with a restricted domain; parametrize a plane curve; audit a decreasing induction rank | A complete coordinate calculation, explicit exceptional cases, and a tested reduction protocol |
| **D. [Persistent research systems: Danus and Rethlas](/posts/2026/08/agent-system/math-research-case-study/)** | Version-sensitive admission, stale results, recovery, and controlled removal of components | A reproducible research trace, failure experiments, and a budget-matched comparison with ordinary chat |

**Preparation:** A and B use Modules 3–5 and 9; C uses two-variable polynomial algebra and elementary induction; D uses Modules 5–9. Begin with the [from-zero Codex workspace](/posts/2026/08/agent-system/codex-research-studio/). No separate orchestration program is required for the manual exercises. Untested architectures remain proposals, and a claimed improvement over a named system needs a direct comparison.

**Combined capstone:** select a candidate from three papers, reconstruct its nearest known proof, attempt its hardest new lemma through two methods, and maintain the evolving evidence through a target revision and recovery test. Submit the unsuccessful routes as well as the strongest surviving result. An exact obstruction or a well-supported decision to stop can be a successful research outcome; a polished proposal without a substantive attempt cannot.

## Use the course modularly

For a **conceptual seminar**, emphasize Modules 1, 2, 4, 5, 6, and 9, with diagrams and written arguments. For a **hands-on workshop**, follow all nine modules in ChatGPT or Codex and carry the same research record forward. A **reading group** can assign one module per meeting and compare solutions to its exercise.

These are teaching formats, not different standards of mathematical evidence. In every format, keep the target, assumptions, and remaining obligations visible.

### Sources and further reading

See [why explicit architecture matters](/posts/2026/08/agent-system/why-mathematicians-need-patterns/) for motivation and [books, primary sources, and claim boundaries](/posts/2026/08/agent-system/sources-and-claims/) for references.

*Written in cooperation with AI. Proposed architectures, teaching code, informal reviews, and formally checked results are distinguished throughout the series.*


### Practice that tests the design

[Download the English practice pack](/files/reasoning-practice-lab.zip): seven missions progress from exact targets to sharp stability bounds, quantifier repairs, exceptional-coordinate analysis, formal admission, and a source-based research capstone. Every mission asks for an initial attempt, a deliberate fault, a repair, and a fresh transfer case. Reference answers are separate so the first attempt remains meaningful.


**For birational geometry researchers:** the elementary examples are calibration tasks, not the research endpoint. Follow the [proof-based research track](/posts/2026/08/agent-system/hands-on-lab/#what-hands-on-means-in-a-proof-based-subject): audit an actual proof, identify the first failed hypothesis, attempt a replacement lemma, and reconstruct the dependencies of a theorem package. Numerical experimentation is optional. The advanced project is assessed by mathematical proof progress and the precision of its unresolved obligations.
