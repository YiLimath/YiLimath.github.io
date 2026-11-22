---
title: "Three Cases That Drive the Architecture"
permalink: /posts/2026/08/agent-system/research-cases/
classes: agent-system-page
full_page_reading: true
---

The course follows one geometric argument through three versions. They have different mathematical outcomes, so they test whether an agent uses the hypotheses rather than memorizing a verdict. Full proofs and sources are in the [minimal-surface workshop](/posts/2026/08/agent-system/birational-proof-workshop/).

## Two nef canonical divisors

Let X and Y be smooth projective surfaces over an algebraically closed characteristic-zero field, and let a birational map between them be given. If both canonical divisors are nef, prove that this map extends to an isomorphism.

Compare canonical divisors on a common resolution, apply negativity with opposite signs, identify the contracted curves, and prove descent in both directions. The imported inputs are [Birkar Lemma 4.15](https://arxiv.org/pdf/1210.2670v1#page=21), [Stacks Tag 0C5S](https://stacks.math.columbia.edu/tag/0C5S), [Tag 0C5R](https://stacks.math.columbia.edu/tag/0C5R), and [Tag 0C5J](https://stacks.math.columbia.edu/tag/0C5J). Stopping at a divisor identity does not complete the target.

## Remove one nefness assumption

Keep only nefness of $K_Y$. Blow up an abelian surface Y at a point to obtain X, with exceptional curve E. Then $K_Y=0$, but $K_X=E$ and $K_X\cdot E=-1$. The blowdown is not an isomorphism, so the weakened general statement is false.

One half of the original divisor comparison survives; the other does not. The agent should retain the surviving proof and give the counterexample. Failure of a proof step alone would not establish falsity.

## Work over a common base

Let the surfaces map to a common projective base S, with the birational map over S, and assume the canonical divisors are nef over S. A p-contracted curve on a common resolution over S has q-image either a point or a curve contracted over S. Relative nefness supplies the same intersection inequalities, and descent gives an isomorphism over S.

The new applicability evidence is commutativity over the base. Repeating the absolute theorem without checking curve images is insufficient.

## Use these cases to test an intervention

Preserve a direct-agent baseline. Add a source check, precise state, or focused repair only when it addresses an observed gap. Compare complete arguments and actual resources under comparable inputs. Withhold reference solutions from independent-solving runs.

These are classical teaching cases, not discoveries or observed agent successes. Transfer the workflow to an unfamiliar proof in your research before claiming broader usefulness.

[Course roadmap](/posts/2026/12/Agent-System/)
