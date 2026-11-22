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
