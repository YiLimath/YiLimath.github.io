# Module 8: Coordinate the work

**Deliverable:** A comparison of sequential and divided work.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/multiple-agent-cooperation/

## Segment 8.1 · Slide 23: More workers introduce a coordination problem

### Spoken script

This module is optional. A good mathematical reasoning system does not require multiple agents. Division of work becomes useful when tasks can proceed independently or require different evidence. One worker might audit a source while another explores a direct proof. But both must know the exact target and assumptions. If the target changes while a worker is running, its eventual report must be checked against the current version before reuse. More workers can increase useful coverage, duplicated effort, or both.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 8.2 · Slide 24: Reports carry evidence rather than votes

### Spoken script

A report should say what task was attempted, what evidence it produced, and what remains unresolved. Agreement among workers is not a proof rule. They may share a source error or repeat the same invalid inference. When reports disagree, preserve the underlying arguments so that the disagreement can be investigated. Start with scripted workers if the purpose is to test the protocol. Model capability can then change without changing the requirement that each report refer to an identifiable mathematical task.

**Pause question:** Why is agreement between two agents weaker than two independent mathematical justifications?

**Expected discussion:** Agreement may repeat shared errors and does not expose the inference. Independent justifications must each supply applicable premises and a valid argument.

## Segment 8.3 · Slide 25: Workshop: does the extra worker help?

### Spoken script

Run the same small task sequentially and with divided responsibilities. Fix a total effort budget rather than giving the multi-worker system twice the resources and calling the comparison fair. Record elapsed time, total cost or calls, accepted evidence, and repeated work. Then deliver a report for an outdated target and verify that the merge procedure does not silently accept it. If the extra worker brings no useful benefit for this task, simplify the architecture. That conclusion is a successful design result.

## Live demonstration

Use two manually prepared reports or scripted workers. Assign a source audit and an alternative-proof task. Change the target version before delivering one report. Record whether the merge accepts, rejects, or requests a new review. No concurrent worker implementation is supplied by the Python lab.

## Student assignment

Submit a budget-matched sequential/divided comparison, a stale-report example, and a decision about whether the extra worker is worthwhile for this task.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.
