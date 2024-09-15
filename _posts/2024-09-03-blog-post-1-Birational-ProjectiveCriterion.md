---
title: 'Birational Geometry Reading Seminar Note: Projectivity criterions'
date: 2024-09-15
permalink: /posts/2024/09/Projectivity/
tags:
  - Birational geometry
  - Complex Geometry
---

The aim of this note is to summarize the projectivity critera in algebraic geometry. Since a morphism is projective iff there exist an relative ample line bundle. Thus it's equivalent to find some ampleness criteria.


---
Here is the outline:

(1) [Note-1: Seshadri projectivity criterion](https://yilimath.github.io/files/Birational/Moishezon/SeshadriCriterion.pdf)

(2) [Note-2: Chow-Barlet cycle space and lower-semi continuity of Seshadri constant](https://yilimath.github.io/files/Birational/Moishezon/lscSeshadriConstant.pdf) [Update 9.15]

(3) [Note-3: Alternating property of projective locus, openness of projectivity](https://yilimath.github.io/files/Birational/Moishezon/OpenesssProj.pdf) [Update 9.15]


---
### Note-1: Seshadri projectivity criterion

In 2024.9.4 reading seminar, we mainly focued on the proof of the Seshadri projectivity criterion of line bundle (and cohomology class) on a proper Moishezon space.

Let us briefly sketch the idea of the proof of the (line bundle version) Seshadri criterion: The easy direction is ampleness implies Seshadri inequalities. We first use the ample line bundle to construct some global generated line bundle. So that there is a divisor passing through any given point. Then the intersection product of the line bundle is greater than the local intersection product, and the local intersection product is greater than multiplicity. The converse direction is more complicated. We prove it by blowing up a generic smooth point. We try to show that pull back line bundle via the blow up, and peturbed by the exceptional divisor is nef. We then apply the Kleiman's nefness criterion and showing that the top intersection number of the line bundle downstairs is positive. By induction on dimension, we can complete the proof of the theorem. (As a side remark, Kodaira lemma holds for projective variety. On a non-projective variety, the arugment style above may be helpful).


For the cohomology class version Seshadri criterion, we require addition assumption that Moishezon space has 1-rational singularity. The point is under the 1-rational singularity assumption, the homological equivalent relation is the same as the numerical equivalent relation for 1-cycles. Thus the cup product on the homology class will restrict to a linear functional on the numerical class. By duality, the linear functional can be realized as a Q-line bundle. Therefore we reduce the cohomology version problem to the line bundle version problem.



---
### Note-2: Chow-Barlet cycle space with application to openess of projectivity problem

In 2024.9.11 reading seminar, we first complete the proof of Seshadri criterion that didn't finish last time. Then we will introduce the main technical tools in the paper, that is approximating Chow-Barlet cycle space using countable many projective morphism. Using this technical tool, we try to prove that if a Moishezon morphism with generic fiber haw rational singularity and the central fiber is projective, then the very general fibers near 0 are also projective.

Let us briefly sketch the idea of the proof of this theorem. We divide the collection of projective morphisms which used to approximate the Chow-Barlet cycle space into 2 types. The first type contains those projective morphism whose image of base in S is nowhere dense. The second type are the rest. We choose any point s in the complement of the locus of the first type. By properness of the morphism into S, the origin 0 contains in the image also. Thus we can find a holomorphic curve connect both s and 0. Using the upper semi-continuity of the multiplicity function together with that the 2 points in the same component of Chow variety has same numerical property. We can finish the proof.

For detailed information see my note [Note-2: Chow-Barlet cycle space and lower-semi continuity of Seshadri constant](https://yilimath.github.io/files/Birational/Moishezon/lscSeshadriConstant.pdf)

---
### Note-3: Alternating properties of projective locus and proof of the main theorem

This time (2024.9.18) we will finish the proof of the main theorem of the paper [Seshadri’s criterion and openness of projectivity](https://link.springer.com/article/10.1007/s12044-022-00680-9), Theorem 2. Before proving the openess of projectivity theorem, we need another result about alternating property of projective locus of a proper (Moishezon) morphism (we already see it [here](https://yilimath.github.io/files/Birational/Moishezon/GeneralTypeLocus.pdf). Combined with the theorem about projectivity of very general fibers that we proved last time, the proof of the main theorem is immediate.

For detailed information see my note (https://yilimath.github.io/files/Birational/Moishezon/OpenesssProj.pdf).


---
### Note-4: Projectivity criteria for Kahler morphism

This time we will study the paper [Projectivity criteria for Kahler morphism](https://arxiv.org/abs/2404.13927). 