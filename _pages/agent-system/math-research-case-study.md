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

## A reference episode with expected state changes

Use the real-number rule $r(c)=(c,c)$ from Module 1. The following is a hand-derived test specification, not an observed transcript of Danus, Rethlas, or Codex.

| Event | Evidence actually available | Expected state |
|---|---|---|
| Set target V1 to producing $(1,1)$ | Rule and candidate $c=1$ | Check $r(1)=(1,1)$, then admit this solution |
| Change target to V2, producing $(1,0)$ | Old calculation still available | Old witness does not solve V2 |
| Deliver an old approving review | Review concerns V1 | Keep it with V1; do not transfer its verdict |
| Calculate every possible output | Both entries always equal | V2 impossible, with a general argument |
| Save a checkpoint and restart | Rule, targets, arguments, reviews | Recover V1 solved and V2 refuted for different reasons |

An important distinction appears in the second and fourth rows. A failed witness establishes only that this candidate does not work. The fourth row supplies a universal reason no candidate can work. A system that declares impossibility immediately after testing $c=1$ happens to reach the right answer here but has not justified it.

Test that weakness with a second rule $q(c)=(c,1-c)$. The same candidate $c=1$ now produces $(1,0)$. Changing the rule changes the problem, so the old equal-entry argument is inapplicable. A memorized negative verdict should not survive this intervention.

### Attribute an improvement to a mechanism

Compare the baseline with a version that adds only explicit target versions. If the new run catches the stale review but still mistakes candidate failure for impossibility, report exactly that. The version record addressed identity; it did not supply the missing universal argument.

Then add a review question: “Does this evidence reject one candidate, or all possible candidates?” Test both rules again, preserving first responses. If several mechanisms are added at once, you can assess the combined workflow but cannot isolate their individual effects from that experiment.

Avoid converting this five-event episode into an impressive-looking success percentage. Report the events, expected transitions, actual transitions, and mathematical reasons. More cases and repeated runs can later support a broader empirical claim.

### What to inspect in a named implementation

For a version of Danus or Rethlas you can actually inspect, trace one result through proposal, evidence, review, reuse, and revision. Ask which artifact identifies the target and argument, how conditional assumptions survive, and what happens when a previously accepted premise is withdrawn. Record code or document locations and actual run evidence separately.

If a feature cannot be found, mark it unlocated in the inspected material; do not conclude that no version has it. This project teaches an audit procedure. It does not make undocumented feature claims about either named system.

## Decide whether more coordination helps

If source checking and an alternative proof can proceed separately, try distinct Codex tasks or conversations. Fix comparable total effort and source access. Count duplicated work, elapsed time, accepted errors, missed valid arguments, and useful partial conclusions. A single-worker system is a valid outcome when coordination adds no value.

## How to make a responsible comparison with a named system

To compare directly with Danus or Rethlas, obtain an accessible, identified version and document its configuration. Run the same cases with comparable tools and resources. Separate claims supported by a paper from observations of your own run. If you cannot execute the named system, compare only architectural choices and do not claim measured superiority.

A useful final report says which failure the redesigned workflow caught, which it missed, and what the added mechanism cost. It may conclude that an ordinary chat is sufficient for a task. The objective is improved mathematical work, not a larger collection of agent roles.

[From-zero Codex setup](/posts/2026/08/agent-system/codex-research-studio/) · [Research-opportunity project](/posts/2026/08/agent-system/research-opportunity-system/) · [Course roadmap](/posts/2026/12/Agent-System/)

