---
title: "Case Study: Danus and Rethlas"
permalink: /posts/2026/08/agent-system/math-research-case-study/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

## Figure 1

![Danus and Rethlas architecture](/images/agent-system/12-math-research-case-study.svg)

*Figure 1. A layered as-built view of the case study. Solid navy arrows show
control, dashed teal arrows show data or feedback, and red arrows mark the
correctness-gated path into the fact graph. The dashed teal return carries the
verifier's verdict and repair hints back to the gateway; the gateway's
`fact_submit` path contains the write gate, and only `verdict == "correct"`
leaves on the red commit path into the fact graph.*

**In one sentence.** Two real codebases read as an as-built pattern map: what the books call reflection, tool use, and evaluation appear here as concrete modules around one correctness boundary.

This case study uses two real codebases. **Rethlas** is the smaller proof-search
system: a generation agent reads a mathematical problem and drafts a proof
blueprint, while a verification agent checks the blueprint through a local HTTP
service. **Danus** builds a long-running, strategy-steered worker system on top
of that generation–verification core.

The architecture is a code-based case study. Its purpose is to show how the
patterns from the reference books appear as concrete modules and interfaces.
For a domain-specific design sketch that uses the same vocabulary for
birational-geometry research, see [A spiral-induction agent for birational
geometry](/posts/2026/08/agent-system/birational-geometry-agent/).

## Rethlas: the two-agent core

The Rethlas repository separates proof generation from proof verification.

1. A problem is stored as Markdown under the generation agent's data directory.
2. The generation agent uses explicit tools for theorem search, memory, branch
   state, and proof verification.
3. It produces a Markdown proof blueprint rather than treating a fluent answer
   as a finished proof.
4. The verification service exposes `/verify`; it starts a fresh verification
   agent and expects a structured JSON verdict.
5. A rejected blueprint returns repair hints; the generation agent revises and
   submits again.
6. A successful run produces `blueprint_verified.md`.

![Rethlas and Danus verified-proof loop](/images/agent-system/23-research-loop.svg)

*Figure 2. The upper state machine is the standalone Rethlas loop. The lower
flow is Danus's per-worker fact-admission path, where `fact_submit` reaches the
verifier before a fact can be committed.*

This is a direct instance of the books' reflection, tool-use, exception-recovery,
structured-output, and human-or-machine evaluation patterns.

## Danus: extending the core

Danus adds the system architecture needed for multiple problems, workers, and
long-running operation:

- **Orchestration:** the main agent and the `danus` CLI create projects, assign
  tasks, start workers, inspect status, and stop execution. The orchestrator
  coordinates work; it is not the correctness authority.
- **Strategy:** an elaboration is prepared, a strategy consultation is run, and
  the resulting `master_guidance` steers the next worker round.
- **Execution:** detached workers run rounds, each using the inherited Rethlas
  proving skills. Multiple workers provide parallel exploration.
- **Verification:** a cold-start verifier judges submitted statements and
  proofs. The verdict is strict: a result is correct only when there are no
  critical errors and no gaps.
- **Truth and memory:** worker-local memory, project-global memory, and a
  content-addressed fact graph have different roles. Only verifier-accepted
  facts enter the fact graph.
- **Gateway:** the role-gated MCP gateway controls the tool surface. Workers can
  submit facts; the main agent cannot call `fact_submit`; the verifier is
  read-only.
- **Outputs:** isolated authoring agents render verified material into a paper or
  a human progress summary.
- **Operations:** theorem search, observability, loopback services, configuration,
  and recovery scripts support the runtime without becoming sources of truth.

## Pattern mapping

| Book pattern | Concrete realization in Danus/Rethlas |
|---|---|
| Prompt chaining | staged problem reading, proof drafting, verification, and repair |
| Routing and planning | main-agent task assignment and strategy guidance |
| Parallelization | detached worker swarm exploring different proof directions |
| Reflection | verifier feedback and generation-agent repair loop |
| Tool use | MCP tools, theorem search, and the `/verify` HTTP interface |
| Structured output | proof Markdown, verification JSON, memory channels, and fact records |
| Memory management | worker-local logs, global findings, and verified facts |
| Multi-agent cooperation | operator, main agent, workers, verifier, and isolated authoring agents |
| Exception recovery | retry, repair hints, persisted rounds, and explicit failure states |
| Evaluation and guardrails | strict verdict schema, role permissions, and the fact write-gate |
| Resource-aware operation | configurable workers, models, transports, service timeouts, and detached execution |

## Design lessons

1. The most important pattern is the **correctness boundary**: generation may be
   broad and exploratory, but truth is introduced only through verification.
2. The **interface boundary** matters more than the agent's label. MCP tool
   schemas, the `/verify` request, the verification JSON, and fact identifiers
   make components replaceable.
3. The **workflow/autonomy distinction** is visible in the architecture. Rethlas
   is a bounded two-agent loop; Danus adds autonomous workers but keeps them
   inside explicit round, memory, permission, and termination controls.
4. The system demonstrates why design patterns are useful for mathematical
   software: they separate search, judgment, storage, and publication so that
   each can be inspected independently.

## Scope and limits

This page documents the architecture visible in the local Danus and Rethlas
code snapshots used for this case study. The linked papers and repositories
provide public provenance, but their default branches or later revisions may
differ from the snapshots inspected here. It does not claim that either system
automatically proves arbitrary mathematics. A verified artifact is a result
accepted by the system's verifier contract; mathematical interpretation and
research significance remain separate questions.

## How to read the diagrams

*The two diagrams deliberately use different forms: the first emphasizes
components and boundaries, while the second emphasizes states, decisions, and
recovery. Both describe the same code-based case study.*

## References

1. J. Liu et al., “Danus: Orchestrating Mathematical Reasoning Agents with
   Fact-Graph Memory,” arXiv:2607.06447 (2026). [Paper](https://arxiv.org/abs/2607.06447)
   and [source repository](https://github.com/frenzymath/Danus).
2. H. Ju et al., “Automated Conjecture Resolution with Formal Verification,”
   arXiv:2604.03789 (2026). [Paper](https://arxiv.org/abs/2604.03789) and
   [Rethlas source repository](https://github.com/frenzymath/Rethlas).
3. A. Gullí, *Agentic Design Patterns: A Hands-On Guide to Building Intelligent
   Systems*, Springer, 2025. [Publisher record](https://link.springer.com/book/10.1007/978-3-032-01402-3).
4. V. Dibia, *Designing Multi-Agent Systems: Principles, Patterns and
   Implementation for AI Agents*. [Author's book site](https://multiagentbook.com/).
