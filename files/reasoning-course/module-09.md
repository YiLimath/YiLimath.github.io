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
