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
