---
title: 'Birational Geometry Reading Seminar Note: Projectivity criterions'
date: 2024-09-07
permalink: /posts/2024/09/Projectivity/
tags:
  - Birational geometry
  - Complex Geometry
---

The aim of this note is to summarize the projectivity critera in algebraic geometry. Since a morphism is projective iff there exist an relative ample line bundle. Thus it's equivalent to find some ampleness criteria.


---
Here is the outline:

(1) [Note-1: Seshadri projectivity criterion]()

(2) [Note-2: Chow-Barlet cycle space and lower-semi continuity of Seshadri constant]

(3) [Note-3: Alternating property of projective locus, openness of projectivity]


---
### Note-1: Seshadri projectivity criterion

In 2024.9.4 reading seminar, we mainly focued on the proof of the Seshadri projectivity criterion using line bundle (and cohomology class) on a proper Moishezon space.

Let us briefly sketch the idea of the proof of line bundle version Seshadri criterion: The easy direction is ampleness implies Seshadri inequalities. We first use the ample line bundle to construct some global generated line bundle. So that there is a divisor passing through any given point. Then the intersection product of the line bundle is greater than the local intersection product, and the local intersection product is greater than multiplicity. The converse direction is more complicated. We prove it by blowing up a generic smooth point. We try to show that pull back line bundle via the blow up, and peturbed by the exceptional divisor is nef. We then apply the Kleiman's nefness criterion and showing that the top intersection number of the line bundle downstairs is positive. By induction on dimension, we can complete the proof of the theorem. (As a side remark, Kodaira lemma holds for projective variety. On a non-projective variety, the arugment style above may be helpful).


For the cohomology class version Seshadri criterion, we require additional assumption that Moishezon space has 1-rational singularity. The point is under the 1-rational singularity assumption, the homological equivalent relation is the same as the numerical equivalent relation for 1-cycles. Thus the cup product on the homology class will restrict to a linear functional on the numerical class. By duality, the linear functional can be realized as a Q-line bundle. Therefore we reduce the cohomology version problem to the line bundle version problem.



---
### Note-2: Chow-Barlet cycle space with applications to openess of projectivity problem

In 2024.9.11 reading seminar, we first complete the proof of Seshadri criterion. Then we will introduce the main technical tools in the paper, that is approximating Chow-Barlet cycle space using countable many projective morphism. We then dive into the proof of the main theorem of this paper. The result says that for a proper flat Moishezon morphism, if the special fiber is projective and generic fiber has rational singularity then there exist a Zariski open subset over which the base is stratified into locally closed subset. On each stratum the morphism is projective.

Let us sketch the idea of the proof. We first prove that there exist a Euclidean open neighborhood of 0 over which the very general fibers are projective. Thus by the Baire category theorem, the projective locus is not contained in countable union of nowhere dense subset. By the alternating property 

A remark about flatness assumption. 

---
