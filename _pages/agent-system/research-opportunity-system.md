---
title: "Advanced Project: Discover a Research Opportunity and Test Its Feasibility"
permalink: /posts/2026/08/agent-system/research-opportunity-system/
classes: agent-system-page
full_page_reading: true
---

The deliverable is a research proposal you can actually begin: an exact candidate theorem, a source audit, a plausible method, and a tested first lemma. A list of fashionable papers or a polished architecture diagram does not meet this standard.

This is a design and laboratory, not a report that a system has already discovered a new theorem. It requires access to real sources and mathematical checking. Do not assign numerical success probabilities without calibration data.

## What the system should return

For each shortlisted paper, require its exact version and theorem locator, the proposed improvement, the proof step where the original hypothesis is used, and a reason the proposed replacement could work. Preserve the original statement alongside the candidate. A weaker conclusion or a special case must be labeled accordingly.

The final recommendation must include a dependency plan, the hardest bridge, applicable known results, a concrete first experiment, and a stopping condition. It may recommend abandoning every candidate. That is preferable to inventing an achievable project.

## Architecture expressed as evidence contracts

| Stage | Input | Inspectable output | Reason to stop or return |
|---|---|---|---|
| Corpus discovery | Authorized vault, database exports, papers | Inventory with access status and exact versions | Full text unavailable |
| Mathematical extraction | Actual statement and proof | Hypothesis-use table with proof locations | Extraction cannot be checked |
| Opportunity proposal | A specific proof bottleneck | Original and proposed theorem side by side | Only a vague topic is proposed |
| Prior-art audit | Candidate and terminology variants | Search log, near-matches, verified comparisons | Already known or novelty unresolved |
| Method design | Candidate and applicable lemmas | Dependency plan with explicit return argument | Essential bridge unsupported |
| Feasibility probe | The weakest bridge | Proof attempt, counterexample, or precise obstruction | Evidence contradicts the proposal |
| Recommendation | All preceding artifacts | Ranked shortlist with reasons and limitations | No candidate survives |

Each arrow implicit in this sequence transfers an artifact, not confidence. Finding a relevant source does not establish applicability. An unsuccessful search does not establish novelty. A successful special-case calculation does not establish the general theorem.

## Build it from zero in Codex

Open a new project folder. Keep source notes read-only and write generated material here. For this researcher's setup the math vault is `D:/Source/Enotes/Math`; other readers should substitute their own authorized location. Do not upload a private vault to external services merely to search it.

```text
Create a research-opportunity workspace using Markdown, without building an app.
Create BRIEF.md, CORPUS.md, HYPOTHESIS-AUDIT.md, CANDIDATES.md,
PRIOR-ART.md, METHODS.md, PROBES.md, and DECISION.md.

First inventory only the sources I authorize. Record actual access:
full text, abstract only, metadata only, or unavailable.
Ask for the research topic and constraints if they are not supplied.
Never edit my source notes or invent citations and execution results.
Separate established facts, proposed extensions, and unresolved obligations.
```

Fill BRIEF.md with the topic, preferred generality, available time, mathematical background, and what would make a result worth pursuing. Start with three papers you understand, not an entire vault. A small auditable run is easier to improve than an opaque large search.

### Find the right source material

```text
Find notes and papers relevant to this brief in the authorized corpus.
Use exact terms and mathematical synonyms. Show the search terms used.
For each match, record the exact path or URL, version, theorem locator,
and why its statement or proof is relevant. Do not rank by title alone.
Identify missing full texts before proposing theorem-level improvements.
```

Use connected search tools when available, or local file search and supplied exports. arXiv is an additional source, not a complete account of prior work. Preserve identifiers, versions, and search dates. If no browsing or database connection is available, report that limitation and continue only with accessible material; do not simulate a search.

### Extract opportunities from proofs

```text
For these three papers, inspect selected theorem statements and proofs.
For each hypothesis, locate where it is used and what that step needs.
Suggest at most three precise improvements: a weakened hypothesis,
a broader setting, a sharper conclusion, or a simpler method.
For each, state the missing bridge and check immediate counterexamples.
Do not call a hypothesis unnecessary merely because its use is hard to find.
```

For example, a proof may invoke compactness to extract a convergent subsequence. A proposed extension must supply a replacement compactness argument, another convergence mechanism, or a different proof. Merely deleting the word “compact” is not a research method. This example illustrates the audit procedure; it is not a new research proposal.

### Check whether the improvement already exists

```text
Search for each exact candidate, including equivalent terminology and
stronger results that would imply it. Inspect relevant statements.
Record queries, dates, sources actually opened, and comparison of hypotheses.
Classify each candidate as already covered, contradicted, not found in the
searched sources, or unresolved. Never turn 'not found' into 'new'.
```

A novelty review should be repeated before committing substantial research time and before publication. References inside the closest papers often matter more than a broad keyword list.

### Require a method detailed enough to attempt

```text
For the surviving candidate, produce a proof blueprint.
List each intermediate lemma, its assumptions, and its role in the conclusion.
For every imported theorem, give an applicability check.
Identify the hardest new lemma and one alternative route.
Choose a first probe that could materially change our assessment today.
Do that probe, preserving the full argument or actual tool output.
```

Useful probes include proving a restricted version of the hardest lemma, checking boundary examples, finding a counterexample to the proposed bridge, or verifying a precise source application. A long proof sketch whose main difficulty is hidden in “standard arguments” fails this stage.

## Feasibility means evidence, not optimism

Use qualitative decisions with explicit reasons:

- **Ready for a focused attempt:** prerequisites checked, first substantive bridge tested, remaining gaps localized.
- **Needs groundwork:** plausible direction, but missing definitions, library support, or a major lemma.
- **Defer:** novelty unresolved, inaccessible sources, or difficulty not localized.
- **Reject this route:** a counterexample or failed necessary condition blocks it.

Even the first category is not a promise of success. Ask a separate review conversation to attack the weakest step using the full evidence. Distinct conversations do not guarantee independent judgments.

## Run a pilot before searching your whole corpus

Start with the lifting problem in the [method-selection project](/posts/2026/08/agent-system/proof-sketch-system/). Give the system the exact sequence and a proposed sufficient vanishing argument. Ask whether vanishing is necessary for the specified section. Require it to distinguish a weaker sufficient criterion from the exact obstruction criterion.

Use the projective line with the trivial bundle and two distinct rational points as a control. The restriction map sends a constant c to (c,c), so (1,1) lifts while (1,0) does not. Ask the system to produce that calculation before proposing a generalization. This is established elementary mathematics, not a new research opportunity; recognizing that boundary is part of the exercise.

Next select three actual papers from your authorized corpus. For one candidate, complete the hypothesis-use table, prior-art search, and first proof attempt. Save all outputs, including a rejected candidate. Compare this with an ordinary request to suggest research topics using the same material and effort budget.

Judge the system by whether its proposal is precise, its source comparisons are correct, and its first attempt materially changes your assessment. A clean negative report can outperform a confident list of untested ideas. Do not score verbosity or number of proposed projects as research progress.

## Final output to the researcher

Submit one recommended project, up to two alternatives, and rejected candidates with reasons. For the recommendation include the proposed theorem, closest prior results, proof plan, completed probe, outstanding lemmas, and the next concrete research session. If nothing survives, submit an honest negative report.

[Course roadmap](/posts/2026/12/Agent-System/) · [Build the base workspace in Codex](/posts/2026/08/agent-system/codex-research-studio/)
