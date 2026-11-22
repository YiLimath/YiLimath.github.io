---
title: "Module 1. Represent the mathematics"
permalink: /posts/2026/08/agent-system/foundations/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

A reasoning system needs to preserve what a statement means before it can manage attempts to prove it. The first design decision is therefore the identity of a mathematical task, not the number of agents.

## One example, two different tasks

Take the projective line over a field k, its trivial line bundle, and two distinct k-rational points p and q. A section on these two points is a pair (a,b). Global sections of the trivial bundle are constants, so restriction is the map c ↦ (c,c).

The section (1,0) cannot lift: no constant has both values. The section (1,1) lifts using the constant 1. There are nonzero global sections in either situation. Thus “find a nonzero global section” and “lift this specified section” are different problems.

The mathematical input includes the chosen section. Removing it from the record destroys a distinction that determines the answer.

## A minimal research record

| Record | Concrete content | Why it is separate |
|---|---|---|
| Target T1 | Lift (1,0) for the specified restriction map | Identifies the proposition |
| Argument A1 | Image of restriction is the diagonal | Supplies a reason, not a status flag |
| Evidence E1 | The calculation c ↦ (c,c) and its justification | Makes the argument inspectable |
| Review R1 | Checks A1 for T1 | Cannot automatically approve another version |
| Task J1 | Compute the image of restriction | Can fail operationally without refuting T1 |

A second argument could establish the same target. A bad argument could support a true statement. Storing statement and argument separately makes both situations representable.

## Build it in Codex

```text
Create RESEARCH.md for the two-point restriction example.
Keep separate targets for lifting (1,0), lifting (1,1), and existence
of a nonzero global section. Derive the answer to each from the restriction map.
For each answer record its argument and assumptions.
Do not use a common label such as 'nonvanishing' in place of the exact target.
```

Inspect the derivation, including why the global sections are constants. A filled table is not proof. If the assistant replaces the first target by the third, preserve that failure before requesting correction.

## Acceptance and transfer

Your record must explain why the first lifting task fails while the other two succeed. Change the chosen section and require a new target version. This habit transfers to research whenever a morphism, divisor, parameter, or quantifier is part of the claim.

The reference calculation above is mathematical content; the prompt is a proposed experiment, not a report of a completed Codex run.

---

[Course roadmap](/posts/2026/12/Agent-System/) · [Direct experiments](/posts/2026/08/agent-system/hands-on-lab/) · [Next module](/posts/2026/08/agent-system/plan-and-execute/)
