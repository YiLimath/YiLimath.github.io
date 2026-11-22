# 04 — Find the quantifier error

Target: a uniform limit of continuous real-valued functions on [0,1] is continuous. Produce the proof, recording the order of choosing x0, epsilon, N, and delta.

Inject: “Pointwise convergence supplies N, and continuity of f_N supplies delta, so the same argument works for pointwise limits.” Identify the first unsupported estimate.

Use f_n(x)=x^n. Compute the pointwise limit, its discontinuity, and an x depending on n where the approximation error stays at least 3/4. Do not rely on a graph.

Deliver: the repaired three-term estimate and the counterexample.

Harder transfer: replace uniform convergence by pointwise convergence plus a common Lipschitz constant L for every f_n. Prove the limit is L-Lipschitz by passing to the limit with x,y fixed. Then prove convergence is uniform on [0,1] using a finite grid. Identify where compactness enters and test the claim on the whole real line.
