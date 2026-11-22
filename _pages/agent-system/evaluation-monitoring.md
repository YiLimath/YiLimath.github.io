---
title: "Module 9. Evaluate the mathematics and the workflow separately"
permalink: /posts/2026/08/agent-system/evaluation-monitoring/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

A system that rejects every claim is unhelpful. A system that accepts every plausible argument is unreliable. Evaluation needs valid controls, invalid variants, and explicit expected outcomes prepared before the run.

## A small reference set

| Case | Expected mathematical result | Failure exposed |
|---|---|---|
| Continuous real-valued f on [0,1] | A maximum exists | Rejecting a valid theorem application |
| f(x)=x on (0,1) | No maximum | Missing compactness |
| Two-point section (1,1) | Lifts as constant 1 | Rejecting a valid direct calculation |
| Two-point section (1,0) | Does not lift | Changing the specified section |
| Every n has a natural-number bound | True with C=n | Incorrect quantifier interpretation |
| One natural number bounds all n | False using n=C+1 | Invalid uniformity bridge |

The two-point cases use the trivial bundle on the projective line and two distinct rational points. Keep these hypotheses in the test input. The table gives reference outcomes, not measured agent performance.

## Separate the evaluation questions

Protocol fidelity asks whether the assistant preserved versions, sources, and assumptions. Mathematical correctness asks whether its actual argument is valid. Research usefulness asks whether the work advances the chosen research objective at acceptable cost. A neat record can fail the second question; a correct elementary answer can still have little research value.

```text
Investigate this target and preserve its exact statement.
Return the argument, sources actually used, remaining assumptions, and gaps.
Do not use the reference answer, which I will keep outside this conversation.
```

Save the full response before giving feedback. Evaluate the original and repaired answers separately. Otherwise an interactive correction can be mistaken for first-attempt success.

## A fair comparison

Run an ordinary prompt and the structured workspace with comparable source access and effort. Record the visible model settings, date, number of attempts, and all failures. If possible repeat runs; report their variation. Small controlled examples test specific behaviors, not general research competence, and familiar examples may be known to the model.

Report invalid arguments accepted out of invalid cases, and valid arguments rejected out of valid cases. Record abstentions separately. Do not fabricate a percentage when the classification is unresolved. Counting completed subtasks can be misleading if the hardest obligation was omitted.

## Research-level assessment

Use the challenging final project to evaluate substantive progress: a reviewed intermediate theorem, a meaningful special case, or a decisive obstruction. A failed proof does not refute its target, and failure to find prior work does not prove novelty.

Submit inputs, outputs, reference reasoning, evaluation decisions, costs, and limitations. State which design change helped which observed failure. Remove mechanisms that added no demonstrated benefit.

---

[Course roadmap](/posts/2026/12/Agent-System/) · [Direct experiments](/posts/2026/08/agent-system/hands-on-lab/)
