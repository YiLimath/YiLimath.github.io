---
title: "Module 3. Turn a source into a justified theorem application"
permalink: /posts/2026/08/agent-system/knowledge-retrieval/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

A search result establishes relevance at most. A theorem application needs an exact statement, a substitution of objects, and evidence for every hypothesis.

## A complete elementary application

Use the theorem that a continuous real-valued function on a nonempty compact space attains a maximum. To apply it to f:[0,1]→R, check the following:

| Source requirement | Current object | Evidence |
|---|---|---|
| Nonempty compact domain | [0,1] | Nonempty closed bounded interval |
| Real-valued function | f:[0,1]→R | Part of the target |
| Continuity | f | Supplied assumption or separate proof |

The conclusion is existence of x in [0,1] with f(y)≤f(x) for every y in [0,1]. It does not give uniqueness or an algorithm for computing x.

Replace [0,1] by (0,1). The compactness row fails; f(x)=x shows that the general conclusion also fails. The source theorem remains correct. Its application is what changed.

## Source records and application records

Keep the source version, theorem locator, statement, and relevant definitions in SOURCES.md. Keep the object substitution and hypothesis evidence in APPLICATIONS.md. A corrected source can affect many applications; a changed target can invalidate one application without changing the source.

```text
Read this supplied theorem and its locator.
Transcribe its hypotheses accurately, then instantiate them for my target.
For each hypothesis mark established, contradicted, or unresolved and explain why.
Write the exact resulting conclusion. Distinguish the excerpt I supplied
from sources you actually opened. Do not invent unavailable page numbers.
```

If source access is unavailable, request the relevant passage or report the limitation. A model's recollection can guide a search but should not masquerade as inspected text.

## Research application

For the lifting problem, a vanishing theorem must apply to L(-D), not merely L. Check the twist, category, positivity, and cohomological degree. Keep rejected near-matches with the exact failed condition; another route may later establish it.

## Acceptance

Submit an applicable source record and an inapplicable near-match, together with their complete hypothesis tables. A source citation without a justified substitution fails the exercise. A missing hypothesis is an open obligation, not evidence that the source theorem is false.

---

[Course roadmap](/posts/2026/12/Agent-System/) · [Direct experiments](/posts/2026/08/agent-system/hands-on-lab/) · [Next module](/posts/2026/08/agent-system/reasoning/)
