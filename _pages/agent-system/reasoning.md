---
title: "Module 4. Preserve the implication back to the target"
permalink: /posts/2026/08/agent-system/reasoning/
tags:
  - Agent System
  - Mathematics
classes: agent-system-page
full_page_reading: true
---

## Research task: close the return from the resolution

Use [the minimal-surface uniqueness workshop](/posts/2026/08/agent-system/birational-proof-workshop/) and its source packet. After E_p = E_q, prove that q descends through every point blowup in p. Locate the contraction factorization lemma and explain how the remaining contracted curves match after each step.

**Mathematical output:** Morphisms in both directions whose composites are identities, not just a divisor identity.

**Value test:** preserve the direct-request baseline. Assess whether this intervention closes a previously unresolved obligation or reaches the same checked result with less measured work. Include retries and mathematical hints. This is a proposed exercise, not a reported improvement.

**Reading order:** start with this geometric task. The elementary examples below are optional calibration material; they are not evidence that the workflow solves research problems.


A reduction is useful only if solving the new problem helps solve the original one. In mathematical research, the difficult step is often the bridge back: a limiting argument, descent from a model, removal of an auxiliary hypothesis, or recovery of uniformity. This module teaches you to expose and test that bridge before investing in the easier subproblem.

**Learning goals:** classify a transformation as an equivalence or one-way implication; track the dependence of choices; prove a return implication; and preserve useful partial progress when the bridge fails. The main worked example uses real analysis. The coordinate-change workshop gives an additional example using two-variable polynomials.

**Source basis.** The uniform-limit theorem is classical; see Jiří Lebl, [*Basic Analysis*, §6.2](https://www.jirka.org/ra/html/sec_liminter.html). The Dini exercise below specializes Michael Müger, [*Topology for the Working Mathematician*, Proposition 7.7.37, printed p. 158](https://www.math.ru.nl/~mueger/topology.pdf#page=158), from countably compact spaces to compact metric spaces. Proofs and exercises here are course expositions. The proposed record format is a design choice, not an experimentally validated architecture.

**The mathematical deliverable:** repair a failed passage to a limit, prove a replacement implication, and identify a circular use of a genuine theorem. No numerical experiment is required.

## 1. Write the return argument before delegating the new task

Let $T$ be the target and $R$ a proposed replacement. If you prove $R\Rightarrow T$, solving $R$ is sufficient. If you only know $T\Rightarrow R$, then $R$ is a necessary condition: failure of $R$ can obstruct $T$, but success need not establish it. If both implications hold, the transformation is an equivalence.

For Module 1's rule $r(c)=(c,c)$, asking whether $(a,b)$ can be produced is equivalent to asking whether $a=b$. If an input exists, both output entries equal that input, so $a=b$. Conversely, if $a=b$, choose $c=a$. These two short arguments justify both directions of the reduction.

Requiring that **every** pair can be produced would be stronger and false. That failure does not stop the particular pair $(1,1)$ from being produced. The transformed task may demand more than the original needs.

A good system stores both the new obligation and its relation to the original. “Try a stronger general theorem” is a research action. “That theorem implies this target under these hypotheses” is a mathematical dependency. Keeping them separate lets the system change its plan without changing what has been proved.

## 2. Full example: when does approximation preserve continuity?

Suppose $f_n:[0,1]\to\mathbb R$ are continuous and converge to a function $f$. We want to prove that $f$ is continuous. This is a realistic pattern: construct easier approximants, establish properties there, and pass to a limit.

The word “converge” hides the decisive hypothesis. Pointwise convergence means that for every $x$ and every $\varepsilon>0$, a threshold may be chosen depending on $x$ and $\varepsilon$:

$$
\begin{gathered}
\forall x\;\forall\varepsilon>0\;\exists N\;\forall n\geq N:\\
|f_n(x)-f(x)|<\varepsilon.
\end{gathered}
$$

Uniform convergence puts the same threshold before the choice of $x$:

$$
\begin{gathered}
\forall\varepsilon>0\;\exists N\;\forall x\;\forall n\geq N:\\
|f_n(x)-f(x)|<\varepsilon.
\end{gathered}
$$

In both displays $x\in[0,1]$ and $n,N$ are natural numbers. The difference is a dependency: may $N$ depend on $x$? Writing that question explicitly is more useful than calling the second convergence “stronger” without explanation.

## 3. The return bridge under uniform convergence

Fix $x_0\in[0,1]$ and $\varepsilon>0$. Uniform convergence lets us choose one index $N$ such that, for every $x\in[0,1]$,

$$
|f_N(x)-f(x)|<\varepsilon/3.
$$

Continuity of this fixed function $f_N$ at $x_0$ supplies $\delta>0$ such that, for $x$ in the domain with $\vert x-x_0\vert<\delta$,

$$
|f_N(x)-f_N(x_0)|<\varepsilon/3.
$$

The triangle inequality now gives

$$
\begin{aligned}
|f(x)-f(x_0)|
&\leq |f(x)-f_N(x)|\\
&\quad+|f_N(x)-f_N(x_0)|\\
&\quad+|f_N(x_0)-f(x_0)|\\
&<\varepsilon.
\end{aligned}
$$

This proves continuity at $x_0$, including the appropriate relative-topology interpretation at an endpoint. Since $x_0$ was arbitrary, $f$ is continuous.

Notice what the proof did **not** need: one common continuity modulus for all the $f_n$. We chose $N$ first, then used continuity of that one function. Asking a worker to establish equicontinuity would introduce a stronger obligation than this proof requires. The dependency order tells us which work is necessary.

[![The uniform-limit proof separates choosing one approximant, controlling its local variation, and assembling the three error terms.](/images/agent-system/course-return-bridge.svg)](/images/agent-system/course-return-bridge.svg)

The diagram's arrows record choices and estimates used by the proof. The bottom warning identifies the exact place where a weaker convergence hypothesis stops supplying the needed evidence.

## 4. A failed bridge with useful surviving results

Take $f_n(x)=x^n$ for positive integers $n$. Each function is continuous on $[0,1]$. For $0\leq x<1$, the values tend to zero; at $x=1$, they are always one. The pointwise limit is therefore

$$
f(x)=\begin{cases}0,&0\leq x<1,\\1,&x=1.\end{cases}
$$

It is discontinuous at $1$. For instance, $x_j=1-1/j$ approaches $1$ through points with $f(x_j)=0$ while $f(1)=1$.

The convergence is not uniform. For every $n\geq1$, choose $x_n=(3/4)^{1/n}<1$. At that point,

$$
|f_n(x_n)-f(x_n)|=3/4.
$$

Thus no single threshold makes all errors less than $1/2$ across the domain. This is a direct witness against the required uniform estimate, not merely an appeal to the discontinuity of the limit.

What remains useful? The approximants are continuous, the pointwise limit has been identified, and convergence is uniform on every $[0,a]$ with $a<1$, since $0\leq x^n\leq a^n$. These are valid partial results. They do not solve the original continuity problem on the full interval. A revised target must retain its new domain explicitly.

## 5. A transformation record you can actually use

| Field | Entry for the limit example |
|---|---|
| Target | Continuity of $f$ on the specified domain |
| Proposed replacement | Continuous approximants and uniform convergence |
| Return argument | The three-term estimate above |
| Choice dependencies | $N$ depends on $\varepsilon$; $\delta$ on the fixed $N,x_0,\varepsilon$ |
| Evidence still needed | Actual uniform error control |
| Failure test | $x^n$ near $1$ |
| Surviving branch | Uniform convergence on $[0,a]$, for each fixed $a<1$ |

The record is short because the proof itself lives elsewhere. Its purpose is to prevent the system from reporting that the approximating problem solved the original merely because both use the same nouns.

For a coordinate transformation, record its formula, domain, inverse where defined, and the excluded inputs. The substitution (u,v) → (u,uv) has inverse (x,y) → (x,y/x) only when x is nonzero. The coordinate-change workshop derives this example completely. A useful substitution still needs an argument returning to the original problem.

## 6. A real proof-repair problem: can Dini's theorem close the gap?

Suppose an argument has continuous functions on a compact metric space K, converging monotonically and pointwise to f. Its author proposes:

> Apply Dini's theorem to get uniform convergence, then use the uniform-limit theorem to prove that f is continuous.

The cited theorem exists, but this argument is circular. Dini's theorem already requires continuity of f. Detecting the cycle requires reading the theorem, not recognizing its name.

**Dini's theorem, compact metric specialization.** Let K be a compact metric space, and let $f_n,f:K\to\mathbb R$ be continuous. If $f_n(x)\uparrow f(x)$ at every x, then $f_n\to f$ uniformly. The decreasing version follows by negating all the functions. The source cited above proves a more general countably compact version; we need only this specialization.

To see every assumption at work, fix $\varepsilon>0$ and set

$$
U_n=\{x\in K:f(x)-f_n(x)<\varepsilon\}.
$$

Continuity makes these sets open. Pointwise convergence makes them a cover of K. Monotonicity makes them increasing. Compactness supplies finitely many covering sets; taking the largest index gives $U_N=K$. For every $n\geq N$, the inequalities $0\leq f-f_n\leq f-f_N<\varepsilon$ hold everywhere. This is uniform convergence. The empty-space case is immediate.

The unsupported step in the proposed application is now visible: without continuity of f, those sets need not be open. More importantly, the cited theorem's premise is precisely the conclusion the author wanted to obtain. A proof planner must keep that premise open. The classical proof-planning distinction between a method and its prerequisites is described by Bundy, [“Proof Planning,” pp. 261–262, “The Nature of Proof Plans”](https://cdn.aaai.org/AIPS/1996/AIPS96-033.pdf#page=1). Our example is a teaching application of that distinction, not a result reported by Bundy.

### Repair with a genuinely different hypothesis

Suppose instead that all the approximants have the same Lipschitz constant $L\geq0$:

$$
|f_n(x)-f_n(y)|\leq Ld(x,y).
$$

For fixed x,y, pointwise convergence allows passage to the limit in this inequality. Hence f is L-Lipschitz and therefore continuous. This proof uses neither uniform convergence nor Dini's theorem. It breaks the cycle by establishing the missing premise independently.

If the sequence is also monotone and K compact, Dini now applies legitimately. But the common Lipschitz bound gives another route to uniform convergence that does not require monotonicity. The next exercise proves that route. These two arguments are worth comparing because they have different prerequisites, not because two agent reports are more convincing than one.

## 7. Proof exercises with substantive outputs

Choose the analysis track below or the [source-based birational geometry assignment](/posts/2026/08/agent-system/birational-geometry-agent/#9-a-source-based-assignment-negativity-and-uniqueness). You need a proof and a hypothesis audit; a collection of completed forms is insufficient.

### Exercise A. Derive a uniform estimate from finite information

Let K be a nonempty compact metric space, and let $f_n:K\to\mathbb R$ converge pointwise to f with a common Lipschitz constant L. Prove uniform convergence without monotonicity. Identify the exact finite object that replaces infinitely many pointwise thresholds.

<details markdown="1">
<summary>Proof checkpoint: the finite-net argument</summary>

The preceding limit argument makes f L-Lipschitz. If L=0, all functions are constant on K, so convergence at one point is uniform convergence. If L>0, fix $\varepsilon>0$ and cover K by finitely many balls of radius $r=\varepsilon/(4L)$, centered at $x_1,\ldots,x_m$. Pointwise convergence at these finitely many centers gives one N such that

$$
|f_n(x_i)-f(x_i)|<\varepsilon/2
\quad(n\geq N,\ 1\leq i\leq m).
$$

For any x choose a center with $d(x,x_i)<r$. Then

$$
\begin{aligned}
|f_n(x)-f(x)|
&\leq |f_n(x)-f_n(x_i)|\\
&\quad+|f_n(x_i)-f(x_i)|\\
&\quad+|f(x_i)-f(x)|\\
&<2Lr+\varepsilon/2=\varepsilon.
\end{aligned}
$$

The finite maximum of the thresholds works for all x. Compactness supplies the finite net; the common bound controls movement away from its centers. The estimate is a complete argument, not evidence from sampling a grid numerically.
</details>

### Exercise B. Find which hypotheses really matter

Give counterexamples to the two claims below. In each case verify every retained hypothesis and explain the precise step that fails.

1. Pointwise convergence of continuous functions on a compact space, with a continuous limit, is always uniform.
2. A common Lipschitz constant and pointwise convergence imply uniform convergence on the whole real line.

<details markdown="1">
<summary>Counterexamples and what they establish</summary>

For the first, use $g_n(x)=\max(0,1-n^2\vert x-1/n\vert)$ on $[0,1]$, $n\geq2$. At 0 the value is zero. For fixed positive x, the shrinking support eventually lies to its left, so the limit is identically zero. Each function is continuous, but $g_n(1/n)=1$. The sequence is not monotone in n. Continuity of the limit alone cannot replace monotonicity in Dini's theorem.

For the second, use $h_n(x)=\max(0,1-\vert x-n\vert)$ on $\mathbb R$. These functions are 1-Lipschitz and converge pointwise to zero. Their supremum remains one. There is no finite net for the whole domain at a fixed small radius; the finite-net proof cannot be extended globally. On each fixed compact subset, the argument still applies.
</details>

### Exercise C. Make two valid methods disagree about applicability

For the finite-net method, construct a nonmonotone sequence satisfying its hypotheses. For Dini's method, construct a monotone sequence of continuous functions with continuous limit but without a common Lipschitz constant. For each, prove that one method applies while the other's stated hypotheses are unavailable.

<details markdown="1">
<summary>One pair of examples</summary>

On $[0,1]$, $f_n(x)=(-1)^n/n$ has common Lipschitz constant zero and converges pointwise to zero, but is not monotone in n. Conversely, $g_n(x)=\sqrt{x}+1/n$ decreases to $\sqrt{x}$ and satisfies Dini's hypotheses. No $g_n$ is Lipschitz on $[0,1]$: the difference quotient between 0 and x equals $1/\sqrt{x}$ and is unbounded near zero. Failure of one method's prerequisites does not refute the target.
</details>

## 8. Use Codex to expose a mathematical dependency

Give the assistant the circular Dini argument and the exact source theorem. Ask it to locate the first unjustified application, then to repair the argument under the common Lipschitz hypothesis. Require the limit inequality and the finite-net proof, not just the names of the theorems.

```text
The target is continuity of a pointwise limit on a compact metric space.
Audit this plan: Dini gives uniform convergence; the uniform-limit
 theorem gives continuity. Read the supplied statement of Dini first.
Identify any premise that depends on the target itself.
Now add a common Lipschitz constant. Prove a noncircular repair.
Finally prove uniform convergence without assuming monotonicity.
Preserve the proof and say exactly where each assumption is used.
```

The essential output fits in one mathematical note: the invalid application, the repaired proof, and the two methods' distinct hypotheses. Split it into files or workers only if that helps you inspect the actual mathematics. The exercise does not measure research novelty or establish an advantage over ordinary mathematical practice.

**What you have learned:** a useful reasoning system must distinguish a plausible strategy from an applicable theorem and from a completed proof. The central skill is finding and proving the missing implication. The diagrams and records serve that work.

---

[Course roadmap](/posts/2026/12/Agent-System/) · [Sources and course status](/posts/2026/08/agent-system/sources-and-claims/) · [Next module](/posts/2026/08/agent-system/verification-gate/)
