---
title: "Module 7. Recover evidence and assumptions, not just a summary"
permalink: /posts/2026/08/agent-system/memory-management/
tags:
  - Agent System
classes: agent-system-page
full_page_reading: true
---

A long research session is useful only if its valid mathematics can be recovered without repeating the whole investigation. This module uses a genuine change in the surface uniqueness problem to distinguish preserved evidence from an obsolete conclusion.

## 1. Save the proof state, not the final mood

On a common resolution, retain the definitions of p, q, compatible canonical divisors, and

$$
D=p^{\ast}K_X-q^{\ast}K_Y=E_q-E_p.
$$

Keep the two signed applications separately. Over X, nefness of $K_Y$ supports $D\geq0$. Over Y, nefness of $K_X$ supports $D\leq0$. The remaining argument uses equality of errors, positive exceptional support, and descent.

A summary saying “negativity proves uniqueness” loses the exact dependencies. It cannot answer what happens when only one nefness assumption changes. The complete proof is in the [central workshop](/posts/2026/08/agent-system/birational-proof-workshop/); the saved state should point to the actual argument, not replace it with confidence.

## 2. Withdraw one hypothesis selectively

Remove nefness of $K_X$, keeping the other assumptions. Recompute support by the inferences actually used.

| Result | Status after the change | Reason |
|---|---|---|
| Common resolution | Retained | Construction does not use this nefness |
| Canonical error formulas | Retained | Blowup calculation is unchanged |
| $D\geq0$ over X | Retained | Uses nefness of $K_Y$ |
| $D\leq0$ over Y | Previous justification lost | Used nefness of $K_X$ |
| Equality of errors and descent | Not established by this route | Depend on the missing comparison |

Do not say the negativity lemma became false. Its statement is unchanged; an application has lost a prerequisite. Do not say the weakened target is false solely from the failed proof. That needs a counterexample.

Here a counterexample is available: blow up an abelian surface Y at a point. The source has $K_Y=0$, while on X the exceptional curve E satisfies $K_X=E$ and $K_X\cdot E=-1$. The blowdown is not an isomorphism. This separate argument settles the weakened statement negatively.

## 3. Keep alternative arguments distinct

The last-blowup route also uses the two nefness assumptions, but at different steps. Nefness of $K_Y$ rules out a nontrivial p in a resolution minimal in p's blowup count; nefness of $K_X$ then rules out a nontrivial q. Removing the latter leaves a birational morphism possible, exactly as the blowup example illustrates.

An alternative proof is not independent of a hypothesis merely because its wording differs. Record its actual assumptions before counting it as surviving support. Conversely, if another argument proves a result without the withdrawn premise, preserve that route rather than globally deleting the result.

This idea has a historical basis in [Doyle's account of reason maintenance](https://ijcai.org/proceedings/1983/82): dependencies explain which derived beliefs need revision. The Markdown workflow here is a teaching proposal, not a reproduction of those algorithms.

## 4. Compress without changing the mathematics

A useful checkpoint has three parts: the current target and hypotheses; established claims with pointers to their arguments; and the next unresolved obligation. Old attempts remain available when needed, but do not need to occupy every new working context.

```text
Current target: surface uniqueness with only K_Y assumed nef.
Survives: common resolution and canonical identities; D >= 0 over X.
Lost support: reverse inequality over Y and the old isomorphism verdict.
New evidence: blowup of an abelian surface refutes the weakened target.
Next choice: restore a hypothesis or formulate a different conclusion.
```

This is a mathematical revision, not a request to delete the earlier theorem. The original two-nef statement and proof remain valid under their original assumptions.

## 5. Test recovery before trusting it

Give a fresh session only the checkpoint, the underlying proofs, and authorized sources. Ask it to reconstruct the current conclusions before continuing. Check whether it silently restores the deleted nefness assumption, repeats completed source work, or treats an old review as current.

Then change to relative nefness over a common base S. This time the previous comparison may be recovered with new applicability evidence: a p-contracted curve has q-image contracted over S, provided the common resolution commutes over S. A system that memorizes only “weakened nefness fails” misses this legitimate variant.

Measure recovery time, duplicated source inspections, corrections, and proof fidelity. A shorter summary that causes a lost assumption is not a saving. A long checkpoint that takes more work to maintain than it saves may need simplification.

## 6. Exercises and deliverable

**Selective withdrawal:** mark every use of $K_X$ nef in both routes, then reconstruct the strongest conclusions still justified without it.

**Stale review:** deliver an old approval after the target changes. Retain its historical scope, but do not let it settle the new target.

**Transfer:** recover the relative-nef proof from the saved absolute proof by supplying only the genuinely new applicability argument.

Submit the original state, revised state, actual fresh-session output, and resource comparison. The useful achievement is continuity of mathematical work across a change—not merely persistence of files.

[Next: coordinate work](/posts/2026/08/agent-system/multiple-agent-cooperation/) · [Course roadmap](/posts/2026/12/Agent-System/)
