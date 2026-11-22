---
title: "Module 2. Plan with joint premises and alternative routes"
permalink: /posts/2026/08/agent-system/plan-and-execute/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

Planning means deciding which missing mathematical justification to pursue next. A task list alone does not express which results actually imply the target.

## Two routes to one lifting target

For a line bundle L and effective Cartier divisor D, the restriction sequence gives a connecting map δ. Exactness says that a specified section s lifts precisely when δ(s)=0.

| Route | Premises needed together | Conclusion |
|---|---|---|
| Vanishing | Correct restriction sequence; H¹(X,L(-D))=0 | Every section on D lifts |
| Direct obstruction | Correct restriction sequence; δ(s)=0 | This section s lifts |

Within each row the premises are joint requirements. Between rows there are alternatives for proving that s lifts. Failure of the vanishing route leaves the direct route available; it does not refute liftability.

For the two-point example on the projective line, direct calculation distinguishes (1,1) from (1,0). A plan that merely says “apply vanishing” has not done that work.

## The dependency rule

A conclusion becomes supported when at least one justified argument has all its premises supported or explicitly assumed. If P implies Q and Q implies P, neither P nor Q follows without a starting point. Repeated execution does not add a logical premise.

For an indexed argument, a finite dependency trace is not a proof of induction. State the base and the well-founded order separately. For example, B₀, A₁, B₁, A₂, B₂ is a valid order if Aₙ uses Bₙ₋₁ and Bₙ uses Aₙ, and each implication is proved.

## Decide the next action

Prefer an action that can change the assessment: check a missing positivity assumption, calculate δ(s), or seek a counterexample to a proposed bridge. Record the expected information and a stopping budget. A heuristic ranking is a search decision, not evidence for its chosen conclusion.

```text
Plan the lifting task using the two routes above.
List the joint premises of each route, their current status, and the next
useful action. Allow three actions. Preserve failed routes and their reasons.
If a premise is unavailable, do not mark it false without evidence.
```

## Test the plan

Use both (1,1) and (1,0). Then remove the evidence for one route and ask which alternatives remain. Separately test the circular P/Q example. Submit the actual plan, actions, and revised status; compare with the mathematical reference rather than accepting a confident completion label.

---

[Course roadmap](/posts/2026/12/Agent-System/) · [Direct experiments](/posts/2026/08/agent-system/hands-on-lab/) · [Next module](/posts/2026/08/agent-system/knowledge-retrieval/)
