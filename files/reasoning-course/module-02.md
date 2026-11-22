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
