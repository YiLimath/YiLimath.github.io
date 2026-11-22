# Reference checkpoints — inspect after the attempt

Full worked proofs and exercises: https://yilimath.github.io/posts/2026/08/agent-system/birational-proof-workshop/

Canonical choices come from a common rational two-form. Point blowups give K_W=p* K_X+E_p=q* K_Y+E_q, with error support exactly the respective exceptional loci. For D=p* K_X-q* K_Y, -D is p-nef and p_*D=p_*E_q is effective, so D>=0. Symmetrically -D>=0. Equality of error divisors gives equality of contracted curves. Descend q through each point blowup of p using Tag 0C5J, and symmetrically obtain the inverse.

The last-blowup alternative chooses a resolution minimal in the number of blowups in p. Its last (-1)-curve cannot be q-contracted, else q descends and reduces that number. Its canonical intersection -1 contradicts q* K_Y+E_q having nonnegative intersection with it. Then p is an isomorphism; nefness of K_X excludes any blowups in q.

Without nefness of K_X, blow up an abelian surface Y at a point. Then K_Y=0 but K_X=E and K_X.E=-1. The birational blowdown is not an isomorphism. Only the first sign survives.

For the relative variant, a p-contracted curve maps to a point in S. Its q-image is either a point or a curve contracted over S. Relative nefness supplies the needed inequality. Commutativity over the base is the crucial extra check.

A coefficient lemma in Lean verifies only that lemma. It does not certify the geometry or the whole theorem. No execution result is asserted in this pack.

These are mathematical checkpoints, not evidence of agent capability or resource savings. Evaluate actual runs separately.
