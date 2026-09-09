---
title: "Agent Systems: Guardrails and Safety"
permalink: /posts/2026/08/agent-system/guardrails-safety/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

## Figure

![Guardrails and safety](/images/agent-system/20-guardrails-safety.svg)

*Figure: input, context, action, and output boundaries constrain the agent and provide escalation paths.*

**In one sentence.** A language model is a non-deterministic component invited
inside a trusted system, so its inputs, its context, its actions, and its outputs
each need a control boundary that a system prompt cannot provide.

## Problem

An agent can receive malicious or ambiguous input, retrieve untrusted context,
call an overpowered tool, or produce an unsafe and unjustified output. A single
system prompt is not a sufficient control boundary, for a reason worth stating
plainly: instructions and data arrive through the same channel. Anything the
model reads — a retrieved document, a web page, a tool result, a file — is
capable of carrying text that reads like an instruction. The boundary must
therefore be enforced by the architecture around the model rather than by asking
the model to be careful.

## Four boundaries

1. **Input:** scope, validate, sanitize, and reject irrelevant requests.
2. **Context:** enforce source boundaries, permissions, provenance, and limits.
3. **Action:** use least privilege, approvals, sandboxing, and audit logs.
4. **Output:** validate schema, citations, claims, uncertainty, and policy.

## Named threats and their mitigations

Treating this as a checklist of specific failures is more useful than a general
appeal to safety.

| Threat | What goes wrong | Mitigation |
|---|---|---|
| **Prompt injection** | Text inside untrusted data is followed as an instruction | Separate trusted instructions from untrusted data using role structure and explicit delimiters; classify intent with a second, cheaper model before the primary call; filter outputs that echo system text |
| **Insecure output handling** | Model output is used directly by another system | Treat output as untrusted: never evaluate returned code, sanitize or encode before rendering, parse and schema-validate expected JSON, and parameterize rather than execute generated queries |
| **Excessive agency** | The agent takes consequential action without authority | Grant tools dynamically rather than as a static full set; use plan–approve–execute so code approves the plan before a scoped client runs it; require human approval for high-impact actions |
| **Sensitive disclosure** | Confidential or personal data leaves through the model | Scrub before ingestion, discard ultra-sensitive input rather than retaining it, and filter every retrieval by tenant or user rather than searching the whole corpus |
| **Resource exhaustion** | Expensive requests degrade or deny service | Rate-limit per user and per address, reject abusive inputs, and throttle or downgrade by cost rather than failing outright |
| **Data poisoning** | Corrupted ingested material changes behavior | Ingest only from trusted sources, track data lineage, and review fine-tuning data by hand |
| **Supply chain and plugins** | A third-party tool is the vulnerability | Give each tool the minimum capability it needs — `read_email`, not `delete_email` — treat all data passed to it as untrusted, and scan dependencies |

Prompt injection deserves first place because it is the threat with no clean
solution. Filtering reduces it and does not eliminate it, so the durable defense
is architectural: assume untrusted context may attempt to redirect the agent, and
ensure that succeeding gains it no capability worth having. That is a statement
about permissions, not about prompts.

## Interface note

The mitigations above are one design decision in different clothes: nothing the
model emits is authority. A tool call is a *request* to a gateway that
independently checks permission; a plan is a *proposal* that code approves; a
piece of output is *data* until something validates it. Wherever a component
treats model output as already-authorized, that is where the guardrail is
missing, regardless of how the prompt is worded.

## Mathematical safety

Label conjectures as conjectures; distinguish search results from verified
theorems; preserve unresolved gaps; and never silently alter a hypothesis. A
guardrail reduces risk but does not establish mathematical truth — for the
boundary that does, see [the verification gate](/posts/2026/08/agent-system/verification-gate/).

There is also a domain-specific injection surface. A retrieved paper, referee
report, or note is untrusted context, and text inside it can read as an
instruction to the agent processing it. An agent that reads sources and also has
write access to a vault or repository needs those capabilities separated.

## Forces and failure modes

Strict controls can block useful work; weak controls can make failures invisible.
Design an explicit escalation path, test adversarial and edge cases, and make
blocked actions observable so that safety does not become silent failure. A
control that fails open while reporting success is worse than no control, because
it also removes the operator's suspicion.

## Real-world application

An agent that can send messages, change records, or execute code needs input,
context, action, and output controls. Permissions, validation, redaction,
sandboxing, and human approval should sit at explicit boundaries around the
capability, not only inside a system prompt.

## Exercises

1. List every tool in one agent and mark which could cause irreversible external
   effect. For each, state whether authority is checked by the model or by code.
2. Write a prompt-injection test: a document that instructs the agent to ignore
   its task. Run it and record whether the attempt is visible in the trace.
3. Apply interface segregation to your tool surface. Which tool has capability
   beyond its purpose, and what is the narrower version?
4. Design the escalation path for a blocked action so that the block is
   observable to an operator without being bypassable by the agent.
5. Your agent reads untrusted papers and writes to a repository. Draw the
   boundary that makes a successful injection worthless.

## Reference basis

The four-boundary structure is Gulli, [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3),
Chapter 18, "Guardrails/Safety Patterns," and Lakshmanan and Hapke, [*Generative
AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/),
Chapter 9, including Self-Check and Guardrails. The named threats and their
mitigations follow the security-and-trust patterns in Mitra, [*System Design for
the LLM Era*](https://www.packtpub.com/en-us/product/system-design-for-the-llm-era-9781807789923),
Chapter 2, which treats prompt injection, insecure output handling, excessive
agency, sensitive information disclosure, model denial of service, data
poisoning, and supply-chain and plugin vulnerabilities as separate architectural
patterns with distinct mitigations, and gives the plan–approve–execute and
tenant-filtered retrieval controls used above. Anthropic's
[Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents)
provides a current engineering discussion of human control, security, and
prompt-injection risk.
