---
title: "Sources, Evidence, and the Limits of the Examples"
permalink: /posts/2026/08/agent-system/sources-and-claims/
classes: agent-system-page
full_page_reading: true
---

This series combines established software patterns with a proposed architecture for mathematical research. A citation to a pattern book supports the pattern's provenance; it does not establish that our mathematical specialization is effective.

## Primary sources and what they support

| Source | Use in this series | What it does not establish |
|---|---|---|
| [Bundy, Proof Planning (1996)](https://cdn.aaai.org/AIPS/1996/AIPS96-033.pdf) | Plans built from methods with preconditions; control of proof search | Reliability of a general language-model researcher |
| [Lean reference: axioms](https://lean-lang.org/doc/reference/latest/Axioms/) | Formal results depend on the encoded statement and audited axioms | Correctness of an informal-to-formal translation |
| [NIST DLMF: interpolation](https://dlmf.nist.gov/3.3) | Polynomial interpolation at distinct nodes | Solvability under an arbitrary smaller degree bound |
| [Anthropic, Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Distinction between fixed workflows and dynamically selected actions | A prescription for how many mathematical workers to use |
| [Danus, version 2](https://arxiv.org/abs/2607.06447v2) | A reported fact-graph orchestration system | A correctness guarantee for every admitted informal claim |
| [Rethlas–Archon, version 2](https://arxiv.org/abs/2604.03789v2) | Separation of informal reasoning and Lean formalization | Equivalence between an informal review verdict and kernel checking |

## Books as supporting references

Antonio Gulli's *Agentic Design Patterns* supplies a broad catalogue. The local attachment's contents identify chaining, routing, parallelization, reflection, tools, planning, and multi-agent work as Chapters 1–7, followed by memory and other operational patterns. These names organize implementation choices below the mathematical contracts.

Victor Dibia's *Designing Multi-Agent Systems* and Lakshmanan and Hapke's *Generative AI Design Patterns* provide complementary engineering perspectives. Their framework-specific mechanisms should be read as replaceable implementations. The series does not rely on a vendor SDK, a particular model generation, or practitioner claims about permanent AI limitations.

## Evidence labels used in the text

A **worked argument** has its reasoning supplied in the article. A **design proposal** specifies behavior to implement and test. A **reported system** is attributed to its source. A **historical implementation note** may describe a local snapshot and requires a pinned revision before reproduction. The laboratory is a guided ChatGPT or Codex workflow. A written protocol specifies intended behavior; its execution must be recorded and evaluated. Only the separately identified Lean exercises supply proof-assistant checks.

The three running cases are teaching examples with explicit conclusions. They do not resolve the open problems that motivate advanced mathematical research. The basic birational example is derived using coordinate formulas; every inverse comes with an explicit domain restriction.

## Source audit exercise

Select one citation, write its exact supported assertion, and copy the source locator into an evidence record. Then list the extra claims that would require additional evidence. For example, a paper describing a verifier supports the existence of that component; measuring the verifier's false-acceptance rate requires an evaluation, and asserting soundness requires a different argument altogether.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
