---
title: "Agent Systems: The Verification Gate"
permalink: /posts/2026/08/agent-system/verification-gate/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

## Figure

![The verification gate](/images/agent-system/33-verification-gate.svg)

*Figure: generation is broad and may be wrong; a single gate decides what is
allowed to become something other results depend on.*

**In one sentence.** Separate the tier of things the system has *produced* from
the tier of things it may *build on*, and let nothing cross between them except
through an independent verdict.

## Problem

Reflection improves a draft. It does not answer a different question: once a
result is produced, may other work depend on it?

Without an answer, an agent's outputs form a flat pool in which a checked lemma,
an unchecked lemma, and a plausible-sounding guess are indistinguishable. The
damage compounds. A later step cites the guess, a third step cites the second,
and by the time the error surfaces there is no way to determine what is
contaminated without redoing everything. This is the characteristic failure of
long-running research systems, and no amount of care inside any single step
prevents it, because the defect is in the absence of a tier boundary rather than
in the quality of the reasoning.

## Intent and structure

`candidate → independent verifier → binary verdict → gated write → dependency graph`

Four commitments make this a pattern rather than an intention.

**The verifier is independent.** Different context, ideally a cold one, and no
access to the generator's reasoning. A critic that inherits the generator's
context inherits its blind spot, and self-assessment then measures fluency
instead of correctness.

**The verdict is binary.** A result is accepted only with zero critical errors
and zero gaps. "Correct modulo a routine argument" is not accepted. This rule
looks harsh and is the entire load-bearing element: the moment a partial verdict
can be stored, the tier distinction is gone and the store is back to being a
pool of assertions with optimistic labels.

**The write is gated by role.** The component that generates cannot be the
component that admits. If a worker can write to the store directly, the gate is
advisory, and an advisory gate is not a gate.

**Dependencies are recorded.** Each accepted result names what it was derived
from. This is what makes an error survivable: when a fact is revoked, everything
downstream is revoked with it, mechanically, without a judgment call about how
far the damage reached.

## Stable interface

An accepted record carries the statement, the argument, the verdict with its
criteria, the verifier's identity and version, the dependencies by identifier,
and a content address. Content addressing matters more than it appears to: if
the statement is edited, the identifier changes, so a silent revision cannot
masquerade as the thing that was verified.

The rejection path needs a contract too. A rejection returns the violated
criterion and repairable feedback, never a bare score, since a score tells the
generator that something is wrong without telling it what to change.

## Mathematical application

This is the pattern's home ground, and the one place where its strictness is
uncontroversial. Search over proof strategies is enormously productive and
enormously unreliable; the two facts are compatible only if the system
distinguishes what it tried from what it established.

Concretely, the tiers separate as: conjectures and heuristics, which may be
stored freely and cited as motivation; findings, which record what an
exploration observed; and facts, which have passed the gate and may be used as
lemmas. Only the third tier is citable in a proof. A retrieved theorem is not a
fact about the current problem until its hypotheses have been checked against
the current hypotheses — which is why retrieval and verification are different
patterns, and why a successful retrieval with mismatched hypotheses is the most
dangerous output the system can produce.

The discipline pays off precisely when something goes wrong. If a lemma accepted
in week two is found defective in week six, the dependency graph answers "what
else falls?" in one query, rather than by rereading six weeks of work.

## Forces and failure modes

A strict gate is slow and rejects work that is probably fine, and the pressure
to relax it is constant and reasonable-sounding. The failure modes are worth
naming because each is a specific way of keeping the gate while losing its
value: verifier capture, where the generator learns to produce what the verifier
accepts rather than what is correct; gate erosion, where a "provisional" tier is
added and gradually becomes citable; and unrecorded dependencies, which leave
the graph unable to cascade and so silently convert revocation into a manual
audit.

Independence is also expensive. A cold-context verifier re-reads material the
generator already has in context, and this cost is the price of the
independence, not an inefficiency to optimize away.

## Real-world application

The pattern generalizes past mathematics wherever a system accumulates results
over time: a compliance assistant that separates retrieved policy text from its
own interpretation, a data pipeline that separates validated records from
inferred ones, a code agent that separates tests that pass from changes that
merely compile. In each case the question is the same — what may the next step
treat as settled — and in each case the answer must be a property of the store
rather than of anyone's confidence.

## Exercises

1. In a system you have built, classify every persisted item as conjecture,
   finding, or fact. Which items are cited as if they were facts but were never
   gated?
2. Design the rejection contract for a proof checker so that a generator can act
   on it without seeing the checker's full reasoning. What is the minimum it must
   return?
3. A worker proposes a lemma the verifier accepts, and a later verifier version
   would reject it. What does the record need for this to be detectable?
4. Argue the case for a "provisional" tier, then show concretely how it becomes
   citable within six months. What control would prevent that?
5. Compare the cost of a cold-context verifier against a critic sharing the
   generator's context, on a task where the generator's premise is wrong.

## Reference basis

The pattern is a generalization of the correctness boundary in the Danus and
Rethlas case study on the [case-study page](/posts/2026/08/agent-system/math-research-case-study/),
where a role-gated write path admits only verifier-accepted results into a
content-addressed fact graph. Its components appear separately in the pattern
books: reflection and critique in Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 4, and the trustworthy-generation, LLM-as-Judge, and self-check patterns
in Lakshmanan and Hapke, [*Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/),
Patterns 11, 17, and 31. What the books treat as quality improvement on a single
output becomes, when combined with a gated write and a dependency graph, a
constraint on what the system is permitted to accumulate. Dibia,
[*Designing Multi-Agent Systems*](https://multiagentbook.com/), Chapter 10,
supplies the corresponding evaluation vocabulary, and the plan-approve-execute
control in Mitra, [*System Design for the LLM Era*](https://www.packtpub.com/en-us/product/system-design-for-the-llm-era-9781807789923),
Chapter 2, is the same separation applied to actions rather than to claims.
