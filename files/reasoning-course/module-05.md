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
