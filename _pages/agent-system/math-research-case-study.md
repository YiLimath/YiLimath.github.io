---
title: "Advanced Project: Evaluate a Research Workflow Inspired by Danus and Rethlas"
permalink: /posts/2026/08/agent-system/math-research-case-study/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

Use existing research systems as sources of questions, not templates whose complexity must be copied. This chapter builds and evaluates a small Codex workflow. It does not claim to reproduce a current Danus or Rethlas implementation, and it does not treat historical local API names as a usable specification.

## The task and baseline

Choose one short mathematical argument you can check, plus two damaged versions: one missing a hypothesis and one missing a return implication. Use the lifting or blow-up experiments from the preceding projects if you need a controlled starting point.

First ask an ordinary chat to solve or review each task. Preserve its full output, source access, date, and effort budget. This is your baseline. Do not give your redesigned workflow extra source material and attribute the difference entirely to architecture.

## Build the smallest useful system

```text
Create a research workspace using Markdown only.
Use TARGET.md for exact versioned targets, ARGUMENTS.md for alternative routes,
REVIEWS.md for reviews of identified argument versions, and CHECKPOINT.md
for the state needed to resume without this conversation.
Investigate one task. Record the actual argument and remaining obligations.
Do not promote a proposal merely because it has been repeated or approved.
```

These files provide explicit interfaces: a target enters investigation, an argument enters review, and a reviewed result may support another step only within its recorded scope. You can operate all of them in one conversation before considering divided work.

## Separate proposal and review

Give a fresh review conversation the exact statement, argument, and sources. Ask it to identify failed inferences and missing premises. Preserve the report even when it disagrees with the proposal. Separate conversations are not guaranteed independent and may share the same error.

An informal review is fallible mathematical evidence. A label such as 'correct' is not a Lean certificate. If you use Lean, retain the encoded statement, environment, actual checking output, and axiom audit; also compare the encoded statement with the intended mathematics.

## Challenge the workflow

| Intervention | Behavior to inspect |
|---|---|
| Change a hypothesis after review | Old review is reconsidered against the new statement |
| Withdraw one of two independent routes | Remaining valid route still supports the target |
| Withdraw all available support | Target becomes unresolved, not automatically false |
| Deliver a delayed report | Its target version is checked before reuse |
| Restart with only a checkpoint | Target, assumptions, and open obligations survive |
| Ask for formal status without running a tool | Missing execution is reported honestly |

Run these interventions and retain the actual responses. A prompt requesting the right behavior is not evidence that the behavior occurred.

## Decide whether more coordination helps

If source checking and an alternative proof can proceed separately, try distinct Codex tasks or conversations. Fix comparable total effort and source access. Count duplicated work, elapsed time, accepted errors, missed valid arguments, and useful partial conclusions. A single-worker system is a valid outcome when coordination adds no value.

## How to make a responsible comparison with a named system

To compare directly with Danus or Rethlas, obtain an accessible, identified version and document its configuration. Run the same cases with comparable tools and resources. Separate claims supported by a paper from observations of your own run. If you cannot execute the named system, compare only architectural choices and do not claim measured superiority.

A useful final report says which failure the redesigned workflow caught, which it missed, and what the added mechanism cost. It may conclude that an ordinary chat is sufficient for a task. The objective is improved mathematical work, not a larger collection of agent roles.

[From-zero Codex setup](/posts/2026/08/agent-system/codex-research-studio/) · [Research-opportunity project](/posts/2026/08/agent-system/research-opportunity-system/) · [Course roadmap](/posts/2026/12/Agent-System/)

