---
title: "Hands-on: Mathematical Research Experiments in ChatGPT or Codex"
permalink: /posts/2026/08/agent-system/hands-on-lab/
classes: agent-system-page
full_page_reading: true
---

**Practice pack:** [Download seven progressively harder missions](/files/reasoning-practice-lab.zip), with starter records, deliberate faults, transfer challenges, and separate reference answers. Begin with one mission; preserve the first attempt before reviewing it.


Use ChatGPT or Codex directly. No Python project, API integration, or programming prerequisite is needed. Each experiment produces a small record that you can inspect and carry into the next experiment.

**What you are testing:** whether the assistant preserves the mathematical target, distinguishes evidence from assertions, and responds correctly when assumptions or arguments change. A successful conversation is evidence about that run, not a guarantee that future runs will behave the same way.

## What hands-on means in a proof-based subject

For a birational geometer, the central practical activity is working on proofs: reconstructing a reduction, checking a theorem's hypotheses, finding the first unsupported implication, and attempting a replacement lemma. Numerical experiments are optional and are not the course's main research method. The elementary examples below are short calibration problems: their known answers make a system's mistakes visible before you trust it with unfamiliar mathematics.

**Two levels, one workflow.** First use a small example to learn the mechanism. Then take a proof you actually care about and produce mathematical work with that mechanism. You do not have to complete every interpolation or stability exercise before starting your research track.

### Research track: audit and improve an actual proof

Choose a precise theorem or reduction from a paper you know in birational geometry. Supply the statement, proof passage, and cited results; preserve their exact hypotheses. Choose one change to investigate, such as removing a positivity assumption or moving from a projective setting to a compact Kähler setting. These are candidate questions, not promised generalizations.

1. **Reconstruct:** express the argument as explicit implications. For each arrow, give the source result and the substitution that makes it apply. Separate existence, preservation of properties, and termination.
2. **Find the first break:** identify the earliest use of the hypothesis you want to change. Quote its precise role. A theorem unavailable in the new setting is a missing justification, not automatically a false conclusion.
3. **Attempt a replacement:** formulate the weakest lemma that would repair this particular step, and try to prove it. Compare a local repair with an alternative route that avoids the step. Preserve the original target when assessing both.
4. **Stress-test:** look for a counterexample after weakening an assumption. If you cannot construct one, retain “unresolved”; do not convert search failure into evidence of truth.
5. **Return to the theorem:** check whether the replacement really closes the original argument or merely proves a special case. Record every remaining dependency.
6. **Restart and revise:** remove one shared lemma or change a hypothesis. Recover which conclusions still follow from the saved record, including alternative proofs.

**Submission:** an annotated proof, an exact replacement lemma, a genuine attempted argument, and a supported conclusion about what has or has not been achieved. A rigorous explanation of why a proposed extension fails can be more valuable than an optimistic project proposal. Formalize a suitable component when useful; lack of full formalization does not justify labeling the rest mechanically checked.

## Set up your research record

In a chatbox, keep the record in the conversation and copy each checkpoint to a document. In Codex, ask it to save the record as `research-record.md` in your chosen working folder. Use a separate folder for this course. File creation is convenient, but not necessary.

Start with this instruction:

```text
Help me investigate a mathematical claim. Keep a research record with:
1. Target ID and version, exact statement, domain, and quantifiers.
2. Assumptions and their status: established, assumed, or unresolved.
3. Candidate arguments, each with its premises and open obligations.
4. Evidence: actual source locations, proof text, or tool output.
5. Review findings tied to the exact target and argument version.
6. Current conclusion and the next useful action.

Do not silently weaken the target. Do not treat agreement as proof.
Do not invent source access or execution results.
After each change, show what changed and what still follows.
```

These instructions establish a working protocol. They do not enforce correctness or create independent reviewers. You will deliberately challenge the protocol in the experiments below.

## Experiment 1. Catch a familiar-looking false statement

```text
Target T1, version 1:
Every continuous real-valued function on (0,1) attains a maximum.
Create the research record. Decide whether the claim is true.
Give an explicit proof or counterexample and identify any missing hypothesis.
```

**Inspect:** the function $f(x)=x$ has no maximum on $(0,1)$. An appeal to compactness is inapplicable. Ask the assistant to repair the statement using $[0,1]$, but require a new version and an explicit explanation of the changed domain.

**Save:** the original claim, counterexample, revised claim, and distinct argument. A polished record of the false claim is not a proof.

## Experiment 2. Expose a circular plan

```text
We have proofs of B implies A and A implies B, but no proof of A or B.
Draw the dependency graph and report what is established.
Then add an independent proof of A as stipulated evidence.
Show exactly what changes. Label the stipulated evidence as such.
```

**Inspect:** initially only the implications are established. Neither conclusion follows without a starting point. After the independent proof of A, B follows. Ask what happens if that independent proof is withdrawn.

**Save:** before-and-after dependency diagrams. A search loop supplies no mathematical base case.

## Experiment 3. Audit a source application

Provide the actual statement of a theorem from a source you can inspect, including its locator. For a first example, use the extreme value theorem for a continuous real-valued function on a nonempty compact domain.

```text
Compare this source theorem with T1 on (0,1).
Make a table: source hypothesis, corresponding object here,
evidence that the hypothesis holds, and unresolved obligations.
Separate what the supplied excerpt says from anything you cannot verify.
Do not invent page numbers or claim to have read an unavailable source.
```

**Inspect:** the domain does not satisfy compactness. Then repeat with a valid application on $[0,1]$. A real source and a relevant conclusion are not enough to justify an application.

**Save:** one accepted application and one rejected near-match. If the assistant has source-access tools, record the exact source it actually opened; otherwise work from the supplied excerpt.

## Experiment 4. Test the return implication

```text
Compare these statements over natural numbers:
P: for every n there exists C such that n <= C.
U: there exists C such that for every n, n <= C.
Give a witness for P. Test whether solving P establishes U.
Identify the exact failed implication without changing either target.
```

**Inspect:** choose $C=n$ for P. For any proposed uniform bound C, choose $n=C+1$ to refute U. Ask the assistant to label the local success and the failed return implication separately.

**Save:** a transformation record containing the original target, subproblem, and return obligation. This is the elementary version of [Case B](/posts/2026/08/agent-system/research-cases/).

## Experiment 5. Challenge reviews and conditional conclusions

```text
Assume P, and suppose we have valid arguments P implies Q and Q implies R.
Report the status of R, including all remaining assumptions.
Next, review an argument for target version 1.
Change one hypothesis to create version 2, then present the old review.
Explain whether that review supports the new version and why.
```

**Inspect:** R remains conditional on P. The old review cannot automatically approve changed mathematical content. A request to label an argument “formal-checked” must not produce that status without actual formal evidence.

**Save:** a current review, a stale review, and an explicit conditional conclusion. If the assistant misses the error, preserve the failure before asking for a correction.

## Experiment 6. Run Lean through Codex

Continue to [the Lean laboratory](/posts/2026/08/agent-system/lean-formalization/) and download its project. In Codex, use:

```text
Open this Lean project and read its lean-toolchain file.
Use the pinned toolchain to run lake build and each supplied Lean fixture.
Show the commands, exit codes, warnings, and printed axiom dependencies.
Explain why the incomplete and extra-axiom examples are unacceptable.
Do not replace failed execution with a predicted successful result.
Then help me complete Exercises.lean without changing its statements.
```

**Inspect:** the completed proofs compile; the broken proof fails; the placeholder example reports `sorryAx`; the extra-axiom example reports `inventedBound`. Compare the informal and formal statements as well as the outputs.

A chatbox without execution tools can explain the proof, but cannot perform this check. Run the commands in a Lean-enabled environment or use Codex with the required tools installed. If execution is unavailable, label the exercise **not run**.

**Save:** the exact source, version, actual output, and statement-alignment report. No Python wrapper is required.

## Experiment 7. Withdraw support and restart from a checkpoint

```text
For this protocol experiment, stipulate that argument A and argument B
independently establish target T. Record their supporting evidence as stipulated.
Withdraw A, then withdraw B, showing the status of T after each step.
Export a self-contained checkpoint with the remaining open obligations.
```

**Inspect:** after withdrawing A, B still supports T. After withdrawing both, T is unresolved, not automatically false. Start a fresh conversation with only the saved checkpoint and ask it to reconstruct the state. Compare the actual answers with the checkpoint; do not assume perfect recall.

**Save:** the withdrawal trace, checkpoint, and comparison. In Codex, the same exercise can use a saved Markdown file. File persistence and mathematical correctness remain different properties.

## Experiment 8. Compare one conversation with divided work

This extension is optional. Use separate chats or explicitly request separate Codex tasks when your environment supports them. Give one task a source audit and another an alternative argument. Supply the same target version and assumptions.

```text
Merge these two reports. Preserve their source evidence and unresolved claims.
One report concerns an old target version: identify it before reusing anything.
Do not decide mathematical truth by counting votes.
```

**Inspect:** outdated evidence is flagged, disagreements remain visible, and duplicated work is counted. Separate chats do not guarantee independent reasoning.

**Save:** compare this with one conversation on the same task, using comparable source access and an effort budget fixed in advance. Record elapsed time, calls or messages, useful evidence, and errors. If divided work does not help, keep the simpler workflow.

## Experiment 9. Evaluate a complete research episode

Choose a short published proof you understand. Prepare the valid case and two damaged variants: a missing hypothesis and an invalid return argument. Keep your reference solution separate while the assistant attempts each task.

```text
Investigate this target using the research-record protocol.
Preserve the original statement. For each proposed conclusion, identify
its evidence, remaining assumptions, and unresolved obligations.
Finish with a report of what was established, what failed, and what remains open.
```

**Inspect:** compare each answer with the actual proof and counterexamples. Count false acceptances and false rejections separately. Repeat with a simpler ordinary chat prompt under comparable conditions. Record the model or tool version shown by your environment and the date; do not infer hidden settings.

**Submit:** the tasks, prompts, complete outputs, checkpoints, source audit, and comparison. Include at least one limitation. The result evaluates these particular runs, not the assistant's universal reliability.

## What survives a change of tool?

These exercises teach precise targets, evidence, dependency tracking, recovery, and evaluation. The prompts are starting instructions, not formulas whose wording must be memorized. Change the interface as tools improve, while retaining the mathematical checks and inspectable outputs.

[Course roadmap](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/)
