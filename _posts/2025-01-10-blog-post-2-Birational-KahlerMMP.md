---
title: 'Birational Geometry Note: Kahler minimal model program'
date: 2025-02-22
permalink: /posts/2025/02/Kahler-MMP/
tags:
  - Birational geometry
  - Complex analytic geometry
---

The aim of this note is to introduce the minimal model program for Kahler varieties. Compared with the well-known minimal model program for projective varieties, the theory of Kahler minimal model program will have the following three major difficulties: (1) Mori bend-and-break technique: Mori bend and break is not known for Kahler varieties, (2) The base point free theorem and cone theorem: Since Kahler manifold with a big line bundle is automatic projective, thus a big line bundle does not make sense on (non-projective) Kahler manifold, (3) Contraction theorem: In the classical MMP, we require the base point free theorem to produce some semi-ampleness divisor. This semi-ample divisor will induce the negative contraction morphism, and this approach is not very clear under Kaehler setting.

In general, we want to study: How far are natural geometric or sheaftheoretic constructions on compact Kähler manifolds in general from being determined by similar constructions on projective? Further structural results could provide a general machine for reducing certain questions about Kähler manifolds to the algebraic setting. 



Here is the outline:

(1) [Note-1 Overview of Kahler minimal model program](https://yilimath.github.io/files/Birational/KahlerMMP/Overview.pdf),

(2) [Note-2 Positivities in the Kahler minimal model program](),

(3) [Note-3 Fujiki's blowing down theorem, Grauert's Contractibility Theorem, Kollar-Mori's extesion of contraction](https://yilimath.github.io/files/Birational/KahlerMMP/Contraction.pdf) [Update 2.21],

(4) [Note-4 Contraction theorem for Kaehler 3-fold using deformation theoretic analysis (by Campana, Höring and Peternell)](https://yilimath.github.io/files/Birational/KahlerMMP/ContractionNefReduction.pdf),

(5) [Note-5 Divisorial constraction for Kahler 3-fold](https://yilimath.github.io/files/Birational/KahlerMMP/Kahlerdivisorialcont.pdf),

(6) [Note-6 Flipping contraction for Kahler 3-fold MMP](),

(7) [Note-6 Kaehler 4-fold MMP](),

(8) [Note-8 Finite generation problem in Kahler MMP](),

(9) [Note-9 Termination problem in Kahler MMP](),

(10) [Note-10 Base point free conjecture in Kahler MMP](),

(9) [Note-10 Rational curves on Moishezon space, Kaehler varieties](https://yilimath.github.io/files/Birational/KahlerMMP/Rationalcurve.pdf) [update 2.19]

(10) [Note-11 Cone theorem for Kahler MMP](),

(11) [Note-12 Projectivity for Kaehler morphism](),

(12) [Note-13 Canonical bundle formulas and subadjunction with applications the Kahler MMP](),

(13) [Note-14 How to use divisorial Zariski decomposition?](),

(14) [Note-15 How to use generalized pair in the Kahler setting?](),

(15) [Note-16 Properties of uniruled Kahler manifold](),

(15) [Supplementary 1: BCHM for projective morphism between complex analytic space (by Fujino)](),

(16) [Supplementary 2: Positivities in codimension 1](),

(17) [Supplementary 3: BBDP and beyond](https://yilimath.github.io/files/Birational/KahlerMMP/BDPPandBeyond.pdf) [update 2.21],

(18) [Supplementary 4: Transendental Volume](),

(19) [Supplementary 5: Tools can be used to reduce the Kahler problem to projective problem](),

(20) [Supplementary 6: Projectivity question How far Kahler structure away from the projective structure?](),

(20) [Abundance for Kahler varieties](),




---
## Note-1 Overview for Kaehler minimal model program
---


---
## Note-1 Finite generation of canonical ring for Kaehler varieties
---



---
## Note-2 Extension of contraction morphism
---

This note will study the extension problem for the contraction morphism. The most difficult part of Kahler MMP is the construction of contraction morphism. The extension of contraction morphism says that if we have contraction on the central fiber, then we also have contraction for the relative MMP. 

Fujiki's blowing down theorem will be the main tool that we use in the construction of the extension of contraction. We will package the Fujiki blowing theorem in [DH24, Theorem 1.1 and Theorem 5.8] which are more suitable for the Kaehler minimal model program. 

The idea of the proof is as follows. 


---
## Note-3 Contraction morphism in the Kahler 3-fold MMP
---

In this note, we study the contraction morphism for Kahler 3-fold MMP. The existence of contraction morphism is one of the most difficult parts of the Kahler minimal model program. 


### Flipping contraction under strong Q-factorial assumption

The proof of this part can be found in [DH24, Theorem 6.2]. The basic idea is proving it by induction on dimension, if we can find some contraction morphism for the Kaehler surface, we then try to use result in [Note-2 Extension of contraction morphism](https://yilimath.github.io/files/Birational/KahlerMMP/ExtensionContraction.pdf). Extend it to a contraction morphism on the Kahler 3-fold. 



### Divisorial contraction under the strong Q-factorial assumption

The proof of this part can be found in [DH24, Theorem 6.9]. 


### Constraction without Q-factorial assumption

The proof of this part can be found in [DH24, Theorem 1.2]. The idea is as follows Without Q-factorial assumption, we need to first take a small Q-factorial modification. On the Q-factorial model, the MMP is well established. The MMP on the Q-factorial model will terminate at some minimal model. The minimal model will induce a contraction morphism ([DH24, Lemma 6.16]). And by the rigidity lemma, we can find a contraction morphism on the original non-Q-factorial variety.


---
## Note-9 Rational curves on Kahler variety
---

In this note we will try to prove the theorem of Cao and Horing, which shows that under BDPP conjecture, if the 


---
## Note-10 Cone theorem in Kahler MMP
---




---
## Supplementary 3: Around BDPP

This note will study the classical paper: [BDPP](http://sebastien.boucksom.perso.math.cnrs.fr/publis/BDPP.pdf)and recent result of Ou [https://arxiv.org/abs/2501.18088](https://arxiv.org/abs/2501.18088). Here are the topic will be covered in this note.

(1) The duality between algebraic pseudo-effective cone and mobile cone of curves on a projective manifold,
(2) The projective manifold is uniruled iff it is not pseudo-effective.
(3) Ou's proof of BDPP conjecture for compact Kahler manifold
(4) Applications of duality of cones and BDPP theorem/conjecture.



---
## Supplementary 2: Analytic BCHM

This note will give a summary of the paper by Fujino. We will omit the preliminary part of the paper, and dive into the center part of the paper. 



---
## Note : Projectivity criteria for the Kahler morphism
---

This time we will study the paper [Projectivity criteria for Kahler morphism](https://arxiv.org/abs/2404.13927). 

