---
title: 'Birational Geometry Note: Kahler minimal model program'
date: 2025-01-10
permalink: /posts/2025/01/Kahler-MMP/
tags:
  - Birational geometry
  - Complex analytic geometry
---

The aim of this note is to introduce the minimal model program for Kahler varieties. Compared with the well-known minimal model program for projective varieties, the theory of Kahler minimal model program will have the following 3 major difficuilties: (1) Mori bend-and-break technique: Mori bend and break is not known for Kahler varieties, (2) The base point free theorem: Since Kahler manifold with big line bundle is automatic projective, thus big line bundle does not make sense on (non-projective) Kahler manifold, (3) Contraction theorem: In the classical MMP, we require the base point free theorem to produce some semi-ampleness divisor. This semi-ample divisor will induce the negative contraction morphism, this approach is not very clear under Kaerhler setting.

For Kahler 3 fold, the minimal model program is well established (see [Minimal models for Kahler 3-fold](https://link.springer.com/article/10.1007/s00222-015-0592-x), and [Bimeromorphic geometry of Kahler threeholds](https://math.univ-cotedazur.fr/~hoering/articles/a30-kaehler-survey.pdf), and [The log minimal model program for Kahler 3-folds](https://arxiv.org/pdf/2009.05924v4)). Höring and Peternell's idea is to construct the contraction morphism in Kaehler MMP via nef reduction map, and the theory depends on the deformation theoretic analysis of negative extremal ray. They divde the problem into 3 cases based on the rigidity of the generator of that negative extremal ray. 


Here is the outline:

(1) [Note-1 Overview of Kahler minimal model program](https://yilimath.github.io/files/Birational/KahlerMMP/Overview.pdf),

(2) [Note-2 Fujiki's blowing down theorem, Grauert's Contractibility Theorem, Kollar-Mori's extesion of contraction](https://yilimath.github.io/files/Birational/KahlerMMP/ExtensionContraction.pdf),

(3) [Note-3 Cone theorem for Kahler MMP](),

(4) [Note-4 Contraction theorem for Kaehler 3-fold using deformation theoretic analysis (by Campana, Höring and Peternell)](https://yilimath.github.io/files/Birational/KahlerMMP/ContractionNefReduction.pdf),

(5) [Note-5 Constraction theorem for Kahler 3-fold using MMP method (by Das and Hacon)](https://yilimath.github.io/files/Birational/KahlerMMP/ContractionDasHacon.pdf),

(6) [Note-6 Kaehler 4-fold MMP](),

(7) [Note-7 Finite generation problem in Kahler MMP](),

(8) [Note-8 Termination problem in Kahler MMP](),

(9) [Note-9 Base point free conjecture in Kahler MMP](),

(10) [Note-10 Rational curves on Moishezon space, Kaehler varieties](https://yilimath.github.io/files/Birational/KahlerMMP/MoriBendBreakMoishezon.pdf)

(11) [Note-11 Projectivity for Kaehler morphism](),

(12) [Note-12 Canonical bundle formulas and subadjunction with applications the Kahler MMP](),

(13) [Note-13 How to use divisorial Zariski decomposition?](),

(14) [Note-14 How to use generalized pair in the Kahler setting?](),

(15) [Supplementary 1: BCHM for projective morphism between complex analytic space (by Fujino)](),

(16) [Supplementary 2: Positivities in codimension 1](),

(17) [Supplementary 3: BBDP and beyond](),

(18) [Supplementary 4: Transendental Volume](),

---
## Note-1 Overview for Kaehler minimal model program
---


---
## Note-1 Finite generation of canonical ring for Kaehler varieties
---



---
## Note-2 Extension of contraction morphism
---

This note will study the extension problem for contraction morphism. The most difficult part of Kahler MMP is the construction of contraction morphism. The extension of contraction morphism says if we have contraction on the central fiber, then we also have the contraction for the relative MMP. 

Fujiki's blowing down theorem will be the main tool that we use in the construction of the extension of contraction. We will package the Fujiki blowing theorem in [DH24, Theorem 1.1 and Theorem 5.8] which are more suitable for the Kaehler minimal model program. 

The idea of the proof is as follows. 


---
## Note-3 Contraction morphism in the Kahler 3-fold MMP
---

In this note, we will study the contraction morphism for Kahler 3-fold MMP. The existence of contraction morphism is one of the most difficult part of the Kahler minimal model program. 


### Flipping contraction under strong Q-factorial assumption

The proof of this part can be found in [DH24, Theorem 6.2]. The basic idea is proving it by induction on dimension, if we can find some contraction morphism for the Kaehler surface, we then try to use result in [Note-2 Extension of contraction morphism](https://yilimath.github.io/files/Birational/KahlerMMP/ExtensionContraction.pdf). Extend it to a contraction morphism on the Kahler 3-fold. 



### Divisorial contraction under strong Q-factorial assumption

The proof of this part can be found in [DH24, Theorem 6.9]. 


### Constraction without Q-factorial assumption

The proof of this part can be found in [DH24, Theorem 1.2]. The idea is: Without Q-factorial assumption, we need to first take a small Q-factorial modification. On the Q-factorial model, the MMP is well established. The MMP on the Q-factorial model will terminate at some minimal model. The minimal model will induce a contraction morphism ([DH24, Lemma 6.16]). And by the rigidity lemma, we can find a contraction morphism on the original non-Q-factorial variety.



---
## Supplementary 3: Around BDPP

This note will give a brief introduction to the classical paper: [BDPP](http://sebastien.boucksom.perso.math.cnrs.fr/publis/BDPP.pdf). There are 2 major achievement in this paper:

(1) The duality between algebraic pseudo-effective cone and mobile cone of curves on a projective manifold,
(2) The projective manifold is uniruled iff it's not pseudo-effective.

We will first briefly summarize the idea of the proof, and then focus on the applications of BDPP in deformation theory and minimal model theory.




---
## Supplementary 2: Analytic BCHM

This note will give a summary of the paper by Fujino. We will omit the preliminary part of the paper, and dive into the center part of the paper. 



---
## Note-1: Projectivity criteria for Kahler morphism
---

This time we will study the paper [Projectivity criteria for Kahler morphism](https://arxiv.org/abs/2404.13927). And some projective morphism occurs in the Kahler minimal model program.

