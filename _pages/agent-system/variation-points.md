---
title: "Agent Systems: Variation Points and the Stable Interface"
permalink: /posts/2026/08/agent-system/variation-points/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Variation points](/images/agent-system/32-variation-points.svg)

*Figure: the seam runs between what callers may rely on and what is free to be
replaced. The pattern lives at the seam, not on either side of it.*

**In one sentence.** Every page in this series names a stable interface; this
page gives the procedure for finding one, so that a new problem can be handled
without a matching page to copy.

## The question the series keeps asking

An agent system trades determinism for flexibility. A design pattern buys
determinism back at one boundary. That statement is only useful if you can say
*which* boundary — otherwise a pattern is applied by analogy, which is how
systems acquire indirection that protects nothing.

The classical answer predates language models by decades, and it is short.
Encapsulation means placing a boundary so that one side may change while the
other stays fixed. Identify the axis along which the system will actually vary;
put the interface across that axis; let the varying side be replaceable and the
stable side be depended upon. Applying a design pattern *is* the act of finding
where something changes and where it must not.

## The procedure

1. **Name the change.** Not "this might change some day" but a change you can
   describe: a model will be swapped, a second retrieval source will be added, a
   critic will sometimes be a human and sometimes a test.
2. **Locate the axis.** What varies along it, and what must every variant still
   provide?
3. **Write the contract** for what every variant provides: names, types, error
   behavior, guarantees. This is the stable side.
4. **Check the direction of dependence.** Callers depend on the contract, never
   on a variant. If replacing a variant edits the caller, the seam is misplaced.
5. **Test the seam** by naming the second implementation. If you cannot name a
   plausible one, you have found no axis, and the pattern is decoration.

Step 5 is the one most often skipped, and it is the cheapest guard against
over-engineering in the whole series.

## The five principles, restated for agent systems

- **Single responsibility.** A component should have one reason to change. An
  orchestrator that also judges correctness has two, and the two will conflict
  the first time a strict verdict blocks progress.
- **Open–closed.** Adding a route, a tool, or a critic should extend a registry,
  not edit the loop. If every new capability touches the control flow, the
  system is closed to extension exactly where it needs to be open.
- **Liskov substitution.** Any handler behind a router must honor the router's
  result contract. A handler that returns a different shape on failure is not a
  substitute, and the caller will grow a special case for it.
- **Interface segregation.** Expose small, complete tool surfaces. An agent given
  a tool it never needs has a capability you must reason about in every safety
  review; this is the same argument as least privilege, arrived at from design
  rather than from security.
- **Dependency inversion.** High-level policy and low-level implementation should
  both depend on an abstraction. Concretely: the orchestrator depends on
  "a critic returning a verdict", not on a particular model with a particular
  prompt.

Prefer composition to inheritance carries over unchanged, and is why this series
treats patterns as things you combine rather than a hierarchy you specialize.

## Worked application

**Router.** The change is that task classes will be added. The axis is the task
class; every variant must still return a result in one shape. The contract is
therefore the routing label, the selected capability, the confidence or
rationale, and the fallback. Note what this excludes: the classifier's
implementation is on the varying side, so a rule table today and a model
tomorrow are both admissible without touching callers.

**Reflection.** The change is who criticizes — a second model, a unit test, a
proof checker, a human. The axis is the critic; every variant must return a
named violated criterion and repairable feedback. Once that contract is written,
the argument for critic independence stops being a matter of taste: the
generator and the critic are separate variants precisely because they must be
able to differ.

**Where the procedure says no.** If a system will only ever call one model with
one prompt and no second implementation is imaginable, a "model abstraction
layer" has no axis. It adds a file and protects nothing.

## Mathematical application

The habit transfers directly. A definition is an interface: it fixes what may be
relied on and leaves the construction free. A theorem's hypotheses are the
contract; its proof is one implementation. Generalizing a theorem is finding the
axis along which the hypotheses may vary while the conclusion survives — which
is the same move as widening an interface, and fails in the same way when the
proof secretly used something the hypotheses did not promise.

This is also the sharpest available test of whether a research agent is well
designed. If replacing the theorem-search backend requires rewriting how proofs
are checked, then search and judgment were never separated, and no amount of
prompting will separate them later.

## Forces and failure modes

Every seam costs a layer. Seams placed on imagined axes produce configuration
that nobody varies and interfaces with one implementation; seams omitted on real
axes produce rewrites. The asymmetry worth knowing is that a missing seam is
usually cheaper to add later than a wrong seam is to remove, because the wrong
seam has already been depended upon.

## Exercises

1. Take three pages from Parts II–V. For each, state the axis of variation in one
   sentence and name a second implementation. Which page's contract is weakest?
2. Find an interface in your own system with exactly one implementation. Is there
   a nameable second one? If not, what would be lost by removing the interface?
3. A team proposes an "LLM provider abstraction layer" for a system that calls
   one model. Argue both sides using step 5, then decide.
4. State the contract a proof checker must satisfy for the generator to be
   indifferent to whether the checker is a model, a proof assistant, or a person.
5. Take a theorem you know well. Name the axis along which its hypotheses could
   vary, and say which step of the proof is the caller that depends on them.

## Reference basis

The principles are classical rather than recent. Information hiding — placing
boundaries so that a design decision can change behind one — is D. L. Parnas,
"On the criteria to be used in decomposing systems into modules,"
*Communications of the ACM* **15** (1972), no. 12, 1053–1058. The formulation of
a pattern as a recurring problem with a reusable solution, together with the
guidance to encapsulate what varies and to prefer composition to inheritance, is
E. Gamma, R. Helm, R. Johnson, and J. Vlissides, *Design Patterns: Elements of
Reusable Object-Oriented Software*, Addison-Wesley, 1994. The open–closed
principle is B. Meyer, *Object-Oriented Software Construction*, Prentice Hall,
1988, and the five principles are collected as SOLID in R. C. Martin, "Design
Principles and Design Patterns," 2000. The application to agent systems is this
course's synthesis: none of the
four pattern books state the selection rule in these terms, though Dibia,
[*Designing Multi-Agent Systems*](https://multiagentbook.com/), Chapter 2,
Sections 2.1–2.4, reaches a compatible conclusion from the other direction by
recommending the simplest structure that meets the requirement.
