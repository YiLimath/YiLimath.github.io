---
title: "Three Cases That Drive the Architecture"
permalink: /posts/2026/08/agent-system/research-cases/
classes: agent-system-page
full_page_reading: true
---

The examples in this series have different jobs. The elementary maximum example is a smoke test for a missing hypothesis. The following three cases expose deeper architectural requirements: transferring a result between objects, preserving quantifiers through approximation, and organizing induction. None is offered as a new research theorem.

## Case A. Produce the specified output, not merely some output

Start with real numbers and the rule $r(c)=(c,c)$. Choosing $c=1$ produces $(1,1)$. It does not produce the requested pair $(1,0)$. Indeed, no input can produce that pair because every output has equal entries.

This separates three questions: does an input exist at all, does one produce $(1,1)$, and does one produce $(1,0)$? The first two answers are yes; the third is no. A system that substitutes one question for another can report a valid calculation as a solution to the wrong target.

Save the exact output rule, requested pair, candidate input, and comparison of actual versus requested output. Module 1 works through this example step by step. Module 4 extends this idea to limits, and the coordinate-change workshop tests what happens when a formula is not defined everywhere.

## Case B. Approximation does not manufacture a uniform bound

Suppose a method constructs quantities $u_j$ and proves $\vert u_j\vert \le C_j$ for every $j$. The target requires a single finite $C$ with $\vert u_j\vert \le C$ for all $j$. These are different quantifier structures:

$$
\forall j\;\exists C_j\quad\text{versus}\quad\exists C\;\forall j.
$$

The first gives no uniform estimate. The sequence $u_j=j$ in $\mathbb R$ is already a counterexample to that implication. If a limiting argument requires compactness, the planner must identify the topology and an actual compactness theorem; boundedness alone is not sufficient in every space and topology.

In geometric analysis, an approximation route often has exactly this shape: construct regularized objects, prove estimates, extract a limit, and identify the limit as a solution of the original problem. The architecture must record which constants depend on the approximation parameter, what converges, and which properties pass to the limit. This paragraph describes a proof obligation, not a claim that any specific analytic conjecture follows.

### Required artifacts

An estimate record names the quantity, norm or topology, domain, allowed parameter dependence, and range of parameters. A limit record names the convergence theorem and the implication that transfers the property. Sampling many values can expose bad estimates; it cannot establish an infinite uniform bound.

A useful failure report is “the estimate depends on j, and no uniform replacement is supplied.” “The approximation approach is wrong” is too broad: the route may be repairable with a different estimate.

## Case C. Mutually supporting statements need a well-founded order

Consider a schematic theorem package with statements $A_n$ and $B_n$. Assume explicit base cases $A_0,B_0$, and suppose that for every $n>0$ there are justified implications

$$
B_{n-1}\Longrightarrow A_n,\qquad
(A_n\land B_{n-1})\Longrightarrow B_n.
$$

The package is well-founded under the lexicographic order $(n,\mathrm{stage})$, with $A$ before $B$. This is an abstract dependency example, not a claimed theorem of birational geometry. The supplied implication proofs and base cases do the mathematical work; the ordering explains why their composition is legitimate.

Now replace the first implication by $B_n\Longrightarrow A_n$. The two claims can no longer justify each other from the listed base cases. More worker rounds do not repair the cycle. One needs an additional independent argument, a stronger inductive package, or a genuinely decreasing rank.

### Required artifacts

Store the statement family, quantified parameter, base cases, step implications, and a well-founded rank. A model change that preserves dimension is not automatically an induction step. Nor does checking a finite collection of indexed nodes prove the entire induction scheme.

## How the cases connect

| Design question | Case A | Case B | Case C |
|---|---|---|---|
| Meaning to preserve | Specified output and permitted inputs | Quantifier order and constant dependence | Indexed statements and full premises |
| Search choice | Vanishing or direct obstruction | Improve estimate or change topology | Reorder package or prove a new bridge |
| False completion | Downstairs result reported upstairs | Pointwise bounds reported uniform | Circular support reported induction |
| Useful partial result | A candidate plus an unchecked compatibility condition | Valid parameter-dependent estimate | A verified step with missing base case |

Use these cases throughout the [chapter route](/posts/2026/12/Agent-System/) and [project laboratory](/posts/2026/08/agent-system/hands-on-lab/). The same artifact contracts should handle all three. If an implementation only catches one example by matching its vocabulary, it has learned a fixture rather than enforced a design rule.

---

[Series guide](/posts/2026/12/Agent-System/) · [Running cases](/posts/2026/08/agent-system/research-cases/) · [Laboratory](/posts/2026/08/agent-system/hands-on-lab/)
