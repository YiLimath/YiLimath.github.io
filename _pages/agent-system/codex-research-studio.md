---
title: "From an Empty Folder to a Mathematical Research System in Codex"
permalink: /posts/2026/08/agent-system/codex-research-studio/
classes: agent-system-page
full_page_reading: true
---

**Birational geometry proof project:** [Uniqueness of smooth minimal surfaces](/posts/2026/08/agent-system/birational-proof-workshop/) supplies a real target, exact sources, two complete proof routes, a relative variant, and a direct-request versus assisted-workflow comparison. Use this as the shared mathematical project.


**Practice pack:** [Download seven progressively harder missions](/files/reasoning-practice-lab.zip), following the birational proof project, with baseline records, source checks, descent, hypothesis changes, and transfer tasks. Begin with one mission; preserve the first attempt before reviewing it.


**The project:** design a research workflow in Codex without first implementing an agent framework. Use instructions, Markdown records, source material, and actual mathematical tools. No Python project is required.

Danus is a useful architectural reference in this series. Our goal is to explore richer research organization, not to assert that this exercise already outperforms Danus. That would require a matched evaluation. More roles and more files are not evidence of better mathematics.

The student is the system designer. Codex helps create and operate the workspace. The learning outcome is the ability to specify what the system must preserve, expose its failures, and improve the design in response.

## 1. Start with a task you can evaluate

Use surface uniqueness and the central workshop's source packet. Preserve a direct proof attempt before adding records. If it stops at a divisor comparison, expose and complete descent. If it already succeeds, evaluate cost or move to an unfamiliar geometric lemma.

## 2. Create the workspace through a conversation

Open an empty course folder in Codex and give it this instruction:

```text
Create a mathematical research workspace here using Markdown only.
Do not create an application or write orchestration code.

Create these files:
AGENTS.md: the working rules below.
TARGET.md: exact target, version, domain, quantifiers, and success criteria.
STATE.md: current conclusions, assumptions, and unresolved obligations.
ARGUMENTS.md: alternative arguments and their dependencies.
SOURCES.md: exact source statements, locators, and applicability checks.
REVIEWS.md: findings tied to exact statement and argument versions.
EXPERIMENTS.md: test inputs, actual outputs, and observed failures.
CHECKPOINT.md: enough information to resume in a fresh conversation.

Working rules:
Never silently weaken the target or promote an assumption to a fact.
Distinguish proposed arguments, reviewed arguments, and formal evidence.
A review applies only to the content it examined.
Record failed routes and missing bridges.
Do not invent citations, source access, or tool execution.
Before a conclusion is reused, identify its supporting argument and scope.
After a revision, identify dependent conclusions that need reconsideration.
```

Inspect the files. An instruction file is a behavioral specification, not an enforcement mechanism. A model can overlook a rule. The following experiments determine whether this particular run follows it.

### Build a sandbox for the proof attempt

Make a disposable copy of the course project. Put the exact target version and authorized source packet in a read-only input directory. Give the worker a writable scratch directory and a place to submit named proof attempts. Keep the review record and accepted claims under the control of a separate admission step. For the first run, you can act as that step yourself. If the runtime supports filesystem restrictions, enforce the worker's write scope there and keep the accepted record outside it. With a shared writable folder, you can still rehearse the protocol and inspect what each role changed.

Start with the reverse negativity inequality. Give the worker the current hypotheses, the definition of $D$, and the relevant statement of the negativity lemma. Send a fresh reviewer the exact submission, its cited premises, and its target version. Keep tentative sign calculations in scratch work and send the next worker only the result that was admitted, its proof, and any open obligations it needs. Danus illustrates how separate memory and tool permissions support this handoff. [Stanford MATH 289, Agents, slides 21 and 30](https://web.stanford.edu/class/math289/agents.pdf#page=87).

Test the boundary in the disposable copy. Confirm the worker can save a scratch note. Where the runtime enforces the restriction, try writing a dummy file in the protected area and record whether the write is denied. Then remove nefness of $K_X$ from the target and deliver the old approval again. Check that the admission step preserves the old proof under its original hypotheses and leaves the reverse inequality open for the revised target.

## 3. Run one complete research cycle

```text
Investigate the target in TARGET.md.
First restate it exactly and identify the decisive uncertainty.
Choose one useful action: a proof attempt, counterexample, source check,
or clarification of a definition. Explain why it is worth doing.
Perform the action using the information and tools actually available.
Update the records with its evidence and remaining obligations.
Do not report completion unless the original success criteria are met.
```

Check whether the specified birational map has actually been extended to an isomorphism. A divisor identity is an intermediate result.

### A checkpoint with mathematical content

```text
TARGET: smooth projective surfaces; both canonical divisors nef;
        extend the given birational map to an isomorphism.
ESTABLISHED: common resolution, canonical identities,
             two signed negativity applications, E_p = E_q.
OPEN: positive exceptional support; descent; inverse identities.
NEXT: apply Stacks Tag 0C5J to the last blowup in p.
```

This is an illustrative state, not an executed run. Save only what the actual attempt has established. After removing nefness of K_X, retain the first inequality but reopen the reverse application and the final verdict.

## 4. Add alternative routes without multiplying agents

Ask for two genuinely different routes to a target, each listing joint premises, expected evidence, and its weakest bridge. One conversation is sufficient to begin.

```text
Create two candidate routes for the same target version.
For each route, list the premises needed together and the return argument
to the original target. Identify what would invalidate this route.
Choose the next action under a budget of three research actions.
Preserve the other route rather than merging incompatible assumptions.
```

Use the quantifier example as a negative control: solving each individual bound does not establish a uniform bound. A sophisticated plan must still expose that failed implication. The [hands-on experiments](/posts/2026/08/agent-system/hands-on-lab/) provide additional controls.

## 5. Separate review from advocacy

Start another conversation with the exact target, proposed argument, and source excerpts. Supply the complete evidence, but leave out persuasive summaries of prior approval.

```text
Review this exact argument version. Identify each inference and check
its premises. Distinguish an error, a missing justification, and a question.
Do not repair the target silently. Return a report with precise locations,
remaining assumptions, and the scope of any conclusion you accept.
```

A fresh conversation can reduce some contextual influence. It does not guarantee independent reasoning or mathematical correctness. Compare the report with the actual proof. For formalizable components, use the [Lean laboratory](/posts/2026/08/agent-system/lean-formalization/) and retain actual execution output. A chatbox without execution tools can discuss a proof but cannot supply a successful tool run.

## 6. Test revisions and recovery

Make a controlled change to a hypothesis or mathematical object. Preserve both versions. Ask Codex to identify which arguments and reviews require reconsideration. Check its list yourself against the dependency record.

Next stipulate two independent supporting routes, withdraw one, then both. The target should remain supported after the first withdrawal if the other route still applies. After both withdrawals it becomes unresolved, not automatically false.

Finally request a checkpoint:

```text
Write CHECKPOINT.md for a new conversation with no access to this chat.
Include the exact target version, established and assumed premises,
surviving arguments, rejected routes, evidence locations, open obligations,
and the next action. Do not summarize away conditional assumptions.
```

Start a fresh conversation using the saved files. Ask it to reconstruct the state before doing new research. Compare the reconstruction with the checkpoint. File persistence is useful; faithful recovery is an observed behavior to test.

## 7. Make the design more sophisticated only where it helps

| Extension | Mathematical purpose | Experiment that could justify it |
|---|---|---|
| Applicability matrix | Prevent a relevant theorem from being applied outside its hypotheses | A valid application and a rejected near-match |
| Alternative argument graph | Preserve useful routes when one argument fails | Withdraw one route, then a shared premise |
| Transformation contracts | Keep the implication back to the original problem visible | Separate bounds versus a uniform bound |
| Versioned review | Prevent approval from drifting onto changed mathematics | Deliver an old review after changing the target |
| Formal evidence record | Distinguish encoded proof checking from informal confidence | Valid Lean proof, type error, placeholder, extra axiom |
| Recovery checkpoint | Resume without losing scope or open obligations | Reconstruct state in a fresh conversation |

These are candidate improvements to your workflow, not claims that Danus lacks every listed capability. Use its case study to ask architectural questions, and inspect the actual implementation before making a feature comparison.

Only add divided work when it has a clear purpose. Source checking and an alternative proof attempt may be suitable separate tasks. Give each the same target version; preserve disagreements; reject stale reports. Keep a comparable total effort budget when comparing with a single conversation.

## 8. Evaluate the resulting system

Compare an ordinary chat prompt with your structured workspace on the same valid proof and damaged variants. Record source access, date, visible model settings, time, interactions, accepted errors, rejected valid steps, and useful partial results. Preserve full outputs so another reader can assess the comparison.

Do not claim superiority from one attractive example. If you compare against Danus, run a specified version on the same tasks under comparable resources, document its configuration, and report failures on both sides. Without that comparison, describe your result as a proposed design and a tested Codex workflow.

**Final submission:** workspace files, complete research traces, evaluation cases, baseline results, one failure analysis, and a justified decision about which mechanisms to keep.

The lasting skill is designing a mathematical research process and testing whether its requirements are actually met. Codex is the practice environment. Students need not program an agent framework to learn this skill; if experiments expose a requirement that instructions cannot reliably enforce, identify that limitation and decide whether existing tools or additional implementation are warranted.

[Course roadmap](/posts/2026/12/Agent-System/) · [Danus and Rethlas case study](/posts/2026/08/agent-system/math-research-case-study/)
