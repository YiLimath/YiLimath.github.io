---
title: 'Birational Geometry Note: Adjunction Theory'
date: 2024-11-27
permalink: /posts/2024/11/Adjunction-Theory/
tags:
  - Birational geometry
---

In this part of note we will introduce adjunction theory in Birational Geometry. Among the techniques in birational geometry, adjunction theory is one of the most
powerful tools. It allows to relate the geometry, and in particular the singularities,
of the ambient variety with the one of appropriate subvarieites. This note is organized as follows. The first part is about adjunction formula (with varies type of singularities). The second part is about the inversion of adjunction with different variants. The third part is about subadjunction formula (which is sometimes also called adjunction on the NKLT centers). The last part is about the canonial bundle formulas (which is sometimes also called adjunction on the fibration). A nice summary about it can be found in the paper [Anti-pluricanonical systems
on Fano varieties, Chapter 3](https://annals.math.princeton.edu/2019/190-2/p01). Our note will base on this paper. And we try to give a more detailed introduction to the adjunction theory.


For detailed information see my reading notes 

(1) [Adjunction Formulas]().

(2) [Inversion of Adjunction](). 

(3) [Kawamata's subadjunction formula](https://yilimath.github.io/files/Birational/CanonicalBundleFormula/KawamataSubadjunction.pdf)

() [Hacon-Mckernan-Xu's subadjunction type theorem]()

(6) [Ambro's canonical bundle formula](https://yilimath.github.io/files/Birational/CanonicalBundleFormula/AmbroCanonicalBundle.pdf)

(5) [Fujino-Mori canonical bundle formula](https://yilimath.github.io/files/Birational/CanonicalBundleFormula/FujinoMoriCanonicalBundle.pdf)

(7) [Generalized canonical bundle formula](https://yilimath.github.io/files/Birational/CanonicalBundleFormula/GeneralizedCanonicalBundle.pdf)

(8) [Canonical bundle formula for generalized Kahler pairs](),


---
## Note-1 Adjunction formulas
---

### Easy adjunction theorem
The theorem says that discrepancy inside S can be seen outside. Thus, bad singularity inside S can be detected from outside. If the singularity of (X,B+S) is nice, then the singularity inside S can not be too bad. How to prove this? Well 


---
## Note-2 Inversion of adjunction
---


### (1) Classical version inversion of adjunction

Before going deeper into the the theory of inversion of adjunction. Let us first study the classical version inversion of adjunction (which can be found in [KM96, Theorem 5.50]). The theorem says that for a normal variety X with a normal divisor S. The pair (X,B+S) is PLT(LC) iff the restriction on S is KLT (LC). 


Let us briefly sketch the idea of the proof. We will divide the proof into several steps:

(1) Easy adjunction theorem, which already be done in Note-1. 

(2) Kollár-Shokurov connectedness theorem: 

(3) Proof of the inversion of adjunction: One direction is an immediate consequence of easy adjunction theorem. Only needs to prove the converse direction, which require the Kollár-Shokurov connectedness theorem. The idea is note that S lies over the NKLT center, if there is any exceptional with coefficint than 1 (lies over S). It must be detected by S, using connectedness principle. Now the singularity inside S is nice, thus the singularity near S must also be nice.

Let us now study the inversion of adjunction for Moishezon space (which appears in [Kol2]). The major difficulity that we will face in the Moishezon setting, will be the minimal model theory over analytic base is not known. 


### (2) Hacon's generalization of inversion of adjunction



----
## Note- Around canonical bundle formula

The main object in the canonical bundle formula is LC/KLT trivial fibration or LC/KLT fibration with Kodaira dimension 0. The motivation of the canonical bundle formula is trying to classify the geometry of the total space by the lower dimensional geometry of the base using the log canonical divisor. 

We will show that the log canonical divisor on the total space can be written as pull back of canonical divisor plus the discreminant and moduli divisors. The discreminant divisor measure singularity of the degenerate fiber while the moduli divisor measure the variation of the generic fiber. 

There are 2 central properties we will study about the discreminant and moduli divisor:

(1) The positivity on the moduli divisor (we will see this part can be hoped to be the pull back of some positive divisor from the moduli space of the fibers), the major tool to study the positivity is the variational Hodge theory (the major results already be discussed in my previous note [Hodge theory notes](https://yilimath.github.io/posts/2024/11/PVHS-and-MVHS/), in particular the semi-positivity theorems) we will briefly review them also in this note,

(2) The singularity on the discreminant divisor (as well as adjunction theory implies by this part).


### Basic properties of canonical bundle formulas
Here are more concete results we will prove in this note
(1) The KLT fibration with Kodaira dimension 0 will induce a KLT trivial fibration structure,

(2) The moduli and discreminant divisor are birational invariant, and they define b-divisors,

(3) The LC/KLT trivial fibration under generic finite base change is still LC/KLT trivial fibration,

(4) Existence of Ambro's model (under base change), such that the moduli divisor is big and nef which descents as a b-divisor,

(5) The inversion of adjunction formula for the LC trivial fibration, which shows that singularity of the total space can be determined by the discreminant divisor,

(6) 

### Applications of canonical bundle formulas

We will show the following applications of canonical bundle formula

(1) In the effective Iitaka fibration conjecture,

(2) Reduce the canonical ring to the pair with general type condition,

(3) When the log canonical divisor is numerical trivial then so it will be Q-linear equivalent trivial,

(4) 

### Why semi-stable reduction?

Semi-stable reduction is important in the canonical bundle formula theory. As semi-stable reduction gives geometric justification for good Hodge theoretic behavior. After alternation, the family has unipotent monodromy! 



----
## Note- Canonical bundle formula for generanlized Kahler pairs

In this note, we will summarize the paper [On the Canonical Bundle Formula and Adjunction for Generalized Kaehler Pairs](https://arxiv.org/abs/2404.12007).

