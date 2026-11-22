# Reasoning Systems for Mathematical Research
## Instructor and recording guide

This English teaching pack covers all nine modules. It contains 27 short scripted segments, each mapped to a slide, with demonstrations, pause questions, answers, and assignments. Module 8 is optional. The deck is a concise visual companion, not a replacement for the longer blog chapters.

Prerequisites: proof literacy and elementary Python. Module 6 introduces Lean from scratch. Use the elementary examples for the core course; reserve section lifting for an advanced group.

Suggested recording structure: one video per module, or three short clips per module. Budget roughly 6–10 minutes per module including the demonstration, excluding student work. These are planning estimates, not measured video durations. Rehearse each lesson before recording. The supplied narration is complete for the short lesson; the live demonstration and student discussion provide the rest of the session.

Record the English narration in the script blocks. Treat demonstration directions as production cues, not spoken text. Show the slide, switch to a terminal/editor for the demonstration, and return to the exercise. Keep terminal text large enough for a phone screen. Hide unrelated windows and credentials. Capture actual outputs rather than simulated terminal animations.

Before recording: install the pinned Lean toolchain, run both laboratories, choose the source theorem for Module 3, and prepare the two reports for Module 8. Do not spend the recording downloading dependencies. If a live command fails, preserve the actual error and use the included reference files to explain the expected result; do not present a prerecorded successful result as the live run.

The core laboratory uses stipulated reviews. It checks workflow behavior, not arbitrary mathematics. The Lean laboratory checks fixed, hand-inspected fixtures and is not a secure admission service for generated code.

## Course sequence

1. **Represent the mathematics** — A versioned statement and argument record.
2. **Plan and search** — A dependency plan with joint premises and alternative routes.
3. **Use the literature** — A source record and an applicability audit.
4. **Change the viewpoint** — A transformation contract with an explicit return argument.
5. **Review and admit results** — A review bound to an exact argument version.
6. **Formalize a proof with Lean** — A checked proof and a statement-alignment report.
7. **Remember and recover** — A reproducible snapshot and a withdrawal report.
8. **Coordinate the work** — A comparison of sequential and divided work.
9. **Evaluate and assemble** — An evaluated research episode with a simpler baseline.

## Assessment

For every module, assess the submitted artifact rather than pattern-name recall. Require the target, evidence, and unresolved obligations to be explicit. For the capstone, use a valid proof, two damaged variants, and a simpler baseline. Do not reward fabricated success, unverifiable citations, or a weakened target presented as the original result.

---

# Module 1: Represent the mathematics

**Deliverable:** A versioned statement and argument record.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/foundations/

## Segment 1.1 · Slide 2: A plausible claim with a missing hypothesis

### Spoken script

Consider the sentence on the screen. It sounds like a familiar theorem. Before we design an agent, decide whether it is true. For f(x) = x, every point in the open interval has a larger point still inside the interval. There is no maximum. The familiar extreme value theorem requires a compact domain. Our first design problem is therefore very concrete: how do we prevent a familiar-looking conclusion from hiding a changed hypothesis? A stronger model may make this mistake less often. We still need a representation that lets us detect it and identify exactly which statement was considered.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 1.2 · Slide 3: Statements and arguments are separate objects

### Spoken script

A statement records what is claimed. An argument records a proposed reason to believe it. Those are different objects because a true statement can have a bad argument, and several arguments can support the same statement. Write the domain and conclusion explicitly. Give the argument its own identifier and list its premises. A review then refers to an exact version of this content. If we change the open interval to the closed interval, we have changed the mathematical task. We should preserve that revision rather than silently treating the earlier review as approval of the new record. A schema checks that fields exist. It does not check that the mathematics inside them is correct.

**Pause question:** Which checks can a record schema perform, and which require mathematical evidence?

**Expected discussion:** A schema can require a domain, premises, and a version identifier. It cannot establish the extreme value theorem or validate its application merely from those fields.

## Segment 1.3 · Slide 4: Laboratory: a well-formed false claim

### Spoken script

We will now run a test whose purpose is to demonstrate a limitation. The workbench can mark this false statement usable when supplied with a stipulated review. That behavior exposes its trust boundary: it manages evidence records but does not decide mathematical truth. Your task is to write the counterexample, revise the domain explicitly, and attach a new argument to the revised statement. Keep the rejected version. At the end, another person should be able to reconstruct both the mistake and the repair without guessing what the system originally meant.

## Live demonstration

In files/math-reasoning-lab, run: python -B -m unittest test_workbench.WorkbenchTests.test_wrong_math_can_pass_policy -v. Open the test and point to the stipulated informal review. Write f(x)=x on (0,1), then revise the domain to [0,1] in a separate statement record.

## Student assignment

Submit the false statement, its counterexample, the revised statement, and a new argument record. Explain why changing the domain changes the task.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.

---

# Module 2: Plan and search

**Deliverable:** A dependency plan with joint premises and alternative routes.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/plan-and-execute/

## Segment 2.1 · Slide 5: A circular plan supplies no starting point

### Spoken script

Suppose one task promises to prove A using B, while another promises to prove B using A. Both tasks may be well written. Both implications may even be correct. Still, we have no proof of either statement without an independent starting point. This is the difference between an execution cycle and a grounded mathematical argument. Retrying the tasks or adding another worker does not manufacture the missing premise. In a genuine induction, a base case and a decreasing parameter supply the structure that this circular plan lacks.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 2.2 · Slide 6: Joint premises and alternative arguments

### Spoken script

Represent an argument as requiring all of its premises. Represent different arguments for the same target as alternatives. If one route fails, the other may remain useful. This distinction also helps choose the next action. A short source check may unblock a route; a counterexample probe may eliminate it. The search policy decides where to spend time, but its choice is not itself a mathematical justification. We can improve that policy as models improve without changing what it means for the premises of an argument to be established.

**Pause question:** If both implications have correct proofs, why is the original circular plan still insufficient?

**Expected discussion:** The implications establish conditional statements. They do not establish either antecedent. An independent base or a valid well-founded induction is still required.

## Segment 2.3 · Slide 7: Laboratory: a cycle and an independent base

### Spoken script

The fixture first creates the two circular implications and attaches stipulated reviews. The closure remains empty. It then adds an independent argument for A. Now B can follow through the reviewed implication. Inspect this change rather than merely noticing a green test result. For your own plan, give one target two routes and put a strict budget on exploratory actions. Record the reason for each action and what it changed. A failed route that rules out a serious possibility can be useful progress, provided we record its actual scope.

## Live demonstration

Run: python -B -m unittest test_workbench.WorkbenchTests.test_unsupported_cycle_cannot_bootstrap -v. Show the assertions before and after the independent base argument. On a board, draw premises into argument nodes and argument nodes into conclusions.

## Student assignment

Create one target with two alternative arguments, one of which needs two premises. Execute at most four exploratory actions and report what each action established or ruled out.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.

---

# Module 3: Use the literature

**Deliverable:** A source record and an applicability audit.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/knowledge-retrieval/

## Segment 3.1 · Slide 8: A relevant theorem can still be inapplicable

### Spoken script

Finding a relevant theorem is only the beginning of a theorem application. Return to our maximum example. The source theorem is useful and correct, but its compactness hypothesis is not satisfied by the proposed domain. More retrieval results will not repair that mismatch. The research system must distinguish evidence about what a source says from evidence that its hypotheses hold here. Otherwise a strong retrieval engine can produce a confidently cited invalid argument.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 3.2 · Slide 9: An applicability record

### Spoken script

For each proposed application, preserve the source version and theorem location. Identify which object in our problem plays each role in the theorem. Then write a row for each hypothesis and attach its justification. A missing row is an open obligation, not an invitation to infer that the author probably intended it. Finally, write the conclusion after substituting our objects. This last step catches applications that prove something nearby but not the target. For an advanced class, repeat the exercise with a vanishing theorem and check the geometric category and positivity assumptions carefully.

**Pause question:** What evidence is still missing after we verify that the quotation is accurate?

**Expected discussion:** We still need the object mapping, justification of every hypothesis in the current setting, and confirmation that the instantiated conclusion supports the target.

## Segment 3.3 · Slide 10: Workshop: a useful rejected match

### Spoken script

Open a textbook or paper you already have permission to use. Locate an exact theorem rather than relying on a model's paraphrase. We will prepare one successful application and one near-match that fails a hypothesis. Keeping the rejected match prevents the next search round from repeating the same error. It also documents a possible research direction: perhaps the missing hypothesis can be proved, or perhaps a different theorem is needed. Neither possibility should be recorded as a completed application until the mathematical bridge is supplied.

## Live demonstration

Open a selected source theorem and record its edition or revision and theorem number. Fill a two-column table: source hypothesis and evidence in this problem. Use the compact-domain example as the first rejected application. This is a manual evidence exercise; the Python lab does not implement retrieval.

## Student assignment

Submit a source record, one justified application, and one rejected near-match. Record the search budget and the unresolved hypothesis without inventing a citation.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.

---

# Module 4: Change the viewpoint

**Deliverable:** A transformation contract with an explicit return argument.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/reasoning/

## Segment 4.1 · Slide 11: Separate bounds do not give a uniform bound

### Spoken script

A research strategy often replaces a hard problem with simpler ones. That is useful only when we understand how the answers return to the original target. Here each individual natural number has a bound. Solving all of those individual problems does not give one common bound. The witness in the first statement may depend on n. In the second statement it must be chosen before n. This elementary distinction appears in serious arguments about uniform estimates and limiting processes. A large collection of successful local tasks can therefore leave the central research problem unresolved.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 4.2 · Slide 12: The return argument is a proof obligation

### Spoken script

A transformation record should tell us what we started with, what construction we performed, and which hypotheses permit that construction. It should then state the new problem and the implication that would return us to the target. Do not hide that implication inside a phrase such as standard reduction. Sometimes the transformation is an equivalence. Sometimes it gives only a sufficient condition. Sometimes we have only a promising analogy. Recording which situation we are in prevents partial success from being reported as completion.

**Pause question:** Does solving every transformed subproblem prove the original target?

**Expected discussion:** Only if the required return implication has been justified. In this example, independent witnesses do not supply a common witness.

## Segment 4.3 · Slide 13: Workshop: the missing uniformity bridge

### Spoken script

Write down the local witness C equals n. Next let a classmate propose a single common bound. Choose its successor and show the failure. The point is not that the calculation is difficult. The point is that we can locate exactly where the proposed transformation loses the target. Your method card should now say that the local problems are solved and the return implication is false in this example. In a research problem, the corresponding bridge may instead remain open. Those statuses must be distinguishable.

## Live demonstration

Display the two quantifier orders side by side. Ask for a proposed common natural-number bound and choose its successor. Mark the return edge as invalid, while keeping the local witness construction correct. Module 6 formalizes this same example.

## Student assignment

Write a transformation card for an argument you know. State the preconditions and return implication. Include one variant with an open or invalid bridge and label its status precisely.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.

---

# Module 5: Review and admit results

**Deliverable:** A review bound to an exact argument version.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/verification-gate/

## Segment 5.1 · Slide 14: A review applies to the argument it examined

### Spoken script

Imagine that a reviewer checks a lifting argument for a particular section. Later the system changes the section but retains the approval flag. The report may be correct about the old argument and irrelevant to the new one. This is an evidence-management failure even before we debate reviewer quality. We need to bind the review to the content it examined. A version identifier or digest helps detect changes, although a digest alone does not authenticate who performed the review.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 5.2 · Slide 15: Status, evidence, and scope

### Spoken script

One verified flag is too ambiguous. Workflow status tells us what the system has done. Evidence kind tells us what checking procedure supports the argument. Scope tells us which assumptions remain. A conditional argument can be useful, but its assumptions must remain visible in downstream conclusions. An informal review and a kernel-checked proof are different kinds of evidence. Neither an impressive reviewer name nor agreement among several models permits us to silently upgrade one kind into another.

**Pause question:** Can a conditional argument be admitted without proving its assumption?

**Expected discussion:** Yes, for explicitly conditional use. Its assumption must remain visible and must not silently become an established premise.

## Segment 5.3 · Slide 16: Laboratory: stale and conditional evidence

### Spoken script

Run the stale-review and conditional-scope examples. Then ask the workbench to allow only formal evidence. The fixture's informal reviews no longer satisfy that policy. Notice that the software is enforcing a rule about supplied records; it is not invoking Lean. Your assignment is to write an admission decision that another researcher can audit. It should identify the exact argument, the evidence actually obtained, and the scope of permitted reuse. When the evidence is insufficient, an unresolved result is the correct output.

## Live demonstration

Run three tests: test_stale_review_rejected, test_assumptions_remain_visible, and test_evidence_types_are_not_interchangeable in test_workbench.WorkbenchTests. Inspect the report fields. Explain that the fixture reviews are stipulated evidence.

## Student assignment

Submit one current review, one rejected stale review, and one conditional conclusion. Specify the evidence policy under which each can be reused.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.

---

# Module 6: Formalize a proof with Lean

**Deliverable:** A checked proof and a statement-alignment report.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/lean-formalization/

## Segment 6.1 · Slide 17: A witness in Lean

### Spoken script

We now formalize the example from Module 4. Read the statement before reading the proof. Nat fixes the domain, and the quantifiers tell us when the witness may depend on the input. After intro n, our context contains an arbitrary natural number and our goal asks for a bound for that number. The pair supplies the witness n and a proof that n is at most itself. Open the editor's proof state and follow this change one line at a time. The important learning outcome is the relation between the mathematical statement and the remaining obligation, rather than memorizing a tactic.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 6.2 · Slide 18: Compilation does not settle admission

### Spoken script

Run all three damaged examples. The first tries to use a proof of P where Q is required and fails. The second uses sorry, so compilation can succeed even though the proof is unfinished. The third contains no sorry but assumes the desired conclusion as an axiom. For these fixed examples, inspect the printed axiom dependencies. Our completed elementary proofs need no axioms. Larger developments may deliberately use standard foundations, so the general policy is to state and audit the allowed dependencies, not blindly reject every axiom. The regression script checks these fixtures only. It is not a secure verifier for arbitrary generated code.

**Pause question:** Which successful compilations in the fixtures are unacceptable under the lesson's policy, and why?

**Expected discussion:** Incomplete.lean depends on sorryAx. ExtraAxiom.lean depends on inventedBound. Neither supplies the required proof under our policy. A checked proof of a different proposition would also fail statement alignment.

## Segment 6.3 · Slide 19: The intended statement remains part of the task

### Spoken script

A correct proof of the pointwise statement does not prove a uniform bound. Formal checking therefore needs a companion task: compare the encoded proposition with the intended mathematics. Complete the exercise that uses a successor as a strict upper bound, then reconstruct the proof that there is no largest natural number. Record the exact declarations and their axiom reports. For research mathematics, begin with a small lemma supported by existing library definitions. Formalizing one fragile bridge can be useful, but it does not certify the rest of an informal paper. For unreviewed generated source, use isolation and a suitable stronger validation procedure rather than trusting displayed output alone.

## Live demonstration

In files/lean-reasoning-lab, run lake build, lake env lean Formalization.lean, and python check.py. In the editor, place the cursor after intro n. Then run each fixtures/*.lean file individually. Use Lean 4.19.0 from lean-toolchain. Open Solutions.lean only after the exercise.

## Student assignment

Complete Exercises.lean and submit the informal/formal statement comparison, version information, axiom reports, and admission decision.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.

## Source notes

- https://lean-lang.org/doc/reference/latest/Axioms/
- https://lean-lang.org/doc/reference/latest/ValidatingProofs/
- https://leanprover-community.github.io/mathematics_in_lean/

---

# Module 7: Remember and recover

**Deliverable:** A reproducible snapshot and a withdrawal report.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/memory-management/

## Segment 7.1 · Slide 20: Losing an argument need not lose the conclusion

### Spoken script

Suppose a source audit invalidates one argument. It is tempting to mark the conclusion false, but that does not follow. Another argument may still establish it. Conversely, retaining the conclusion merely because it was once approved is also wrong. We must recompute what the remaining evidence supports. In the section-lifting case, a sufficient vanishing route and a direct obstruction calculation can support the same target. Withdrawing one route need not remove the other.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 7.2 · Slide 21: Recovery preserves mathematical state

### Spoken script

A saved conversation is not always enough to restore a research state. We need the target, current versions, dependencies, evidence records, and open obligations. Operational failures need separate treatment. A timeout tells us that an execution did not complete within its limit. It does not refute the lemma. A counterexample has mathematical content. A reproducible snapshot should let us recover these distinctions and obtain the same report from the same state. Our teaching implementation assumes one writer and does not provide database transactions or authenticated reviews.

**Pause question:** What can we conclude when the only currently usable argument is withdrawn?

**Expected discussion:** The target is no longer supported by the available admitted evidence. It is unresolved in this state, not automatically false.

## Segment 7.3 · Slide 22: Laboratory: withdrawal and replay

### Spoken script

Run the alternative-route test and inspect the report after each withdrawal. Then run the save-and-reload test. The restored report should agree with the saved one. The final mutation deliberately changes mathematical content and should invalidate the old digest relationship. This demonstrates a useful integrity check, but it is not a security guarantee against a party that can rewrite all records and digests. In your report, separate reproducibility, content integrity, and authentication. They solve related but different problems.

## Live demonstration

Run test_alternative_survives_then_both_fail and test_save_reload_and_tamper in test_workbench.WorkbenchTests. Inspect the withdrawal reasons and compare the saved and loaded target reports.

## Student assignment

Save a state with two routes, withdraw each route in turn, and replay the reports. Add a separate simulated timeout and explain why its status differs from a refutation.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.

---

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

---

# Module 9: Evaluate and assemble

**Deliverable:** An evaluated research episode with a simpler baseline.

**Reading:** https://yilimath.github.io/posts/2026/08/agent-system/evaluation-monitoring/

## Segment 9.1 · Slide 26: Rejecting everything is not success

### Spoken script

A system that rejects every argument can look safe on a collection containing only bad proofs. It is not useful for research. Our evaluation therefore needs valid controls as well as damaged variants. Start with a short proof you understand. Remove a necessary hypothesis in one variant and break a return implication in another. Measure whether the system preserves the valid case and diagnoses the damaged ones. A correct partial result can be useful, but it must not be counted as a completed proof of the original target.

**Visual cue:** let students read the mathematical example before beginning the explanation.

## Segment 9.2 · Slide 27: Three evaluation questions

### Spoken script

These questions require different evidence. Unit tests can check version handling and withdrawal behavior. They cannot establish every mathematical assertion placed in a record. Mathematical review or suitable formal checking addresses proof content. Research usefulness asks whether the architecture improves progress relative to a simpler baseline, taking cost and maintenance into account. Do not combine these into one impressive score that hides which property was actually tested. Report the failures and the task conditions under which the result was obtained.

**Pause question:** What evidence would justify removing a component from the system?

**Expected discussion:** A task-relevant comparison shows no useful benefit, or the benefit does not justify its resource and maintenance costs. Preserve necessary correctness requirements while simplifying their implementation.

## Segment 9.3 · Slide 28: The capstone research episode

### Spoken script

For the capstone, assemble the artifacts from the earlier modules around one mathematical problem. Include the original target, source applications, proposed arguments, reviews, and remaining obligations. Compare against a simpler workflow. Explain which component caught a real failure or saved useful work, and which component did not justify its cost. As AI improves, rerun this evaluation and replace mechanisms that no longer help. What persists is the discipline of defining the task, preserving evidence, and evaluating actual mathematical progress. We do not need a prediction that any particular activity will remain exclusively human in order to teach those requirements.

## Live demonstration

Run python -B -m unittest discover -s files/math-reasoning-lab -p test_workbench.py -v from the repository root. Explain what the eight tests cover. Then evaluate the chosen proof and two damaged variants separately; do not count the fixture suite as a mathematical benchmark.

## Student assignment

Submit the complete episode, valid and damaged cases, baseline comparison, resource record, and one documented failure. State which conclusions are proved, conditional, or unresolved.

## Closing line

What did this mechanism improve, what does its evidence establish, and what does it still trust? Keep your artifact for the next module.

---
