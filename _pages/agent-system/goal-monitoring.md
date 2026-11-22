---
title: "Completion Is Relative to the Original Target"
permalink: /posts/2026/08/agent-system/goal-monitoring/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

**Pattern reference.** This is a short design note, not a standalone lesson. For the worked argument, step-by-step practice, and assessment, read the [full course chapter](/posts/2026/08/agent-system/evaluation-monitoring/). Geometry references below refer to the optional extension of Case A.


Case A may end with a lift, a justified non-liftability result for the chosen section, or an open obstruction. Case B may produce useful estimates without the uniformity required by the target. These outcomes deserve different names.

## The contract

Keep the target immutable within an attempt. Additional hypotheses create conditional branches. A final report identifies the exact target version, evidence, remaining assumptions, and next informative action.

## Trade-offs and failure modes

Budget exhaustion ends execution, not mathematics. A local lemma can be complete while the programme remains open. The conversational exercise asks you to distinguish usable, conditional, and unresolved outcomes. Inspect the actual responses; the instructions do not enforce these states.

## Build and test

Report Case B with only parameter-dependent estimates available. State the partial result and missing uniformity assertion without claiming the main problem solved.

Use the [running cases](/posts/2026/08/agent-system/research-cases/) and [workbench laboratory](/posts/2026/08/agent-system/hands-on-lab/). Record inputs, expected outcomes, actual outcomes, and the mathematical reason for the expectation. For references and claim boundaries, see [sources and claims](/posts/2026/08/agent-system/sources-and-claims/).

## Worked design decision: detect a solved substitute

The target is to lift a specified pair (a,b) to a constant function. Producing a lift for (1,1) does not solve the target (1,0). Monitor the actual input, output, and quantifiers, not whether the conversation contains a plausible solution.

**Acceptance exercise.** Keep the original target beside the current subgoal. Every completed subgoal needs a stated implication back to the target. A change of target requires an explicit decision and leaves the earlier task unresolved.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
