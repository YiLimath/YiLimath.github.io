---
title: 'Moishezon Morphism Seminar Note'
date: 2024-12-04
permalink: /posts/2024/12/Moishezon-Morphism/
tags:
  - Birational geometry
  - Moishezon morphism
---

The purpose of this reading seminar is to discuss the recent paper [Moishezon morphism](https://www.intlpress.com/site/pub/pages/journals/items/pamq/content/vols/0018/0004/a011/index.php?mode=ns) by Professor Kollár in detail. 



---
Here is the outline:

(0) [Brief summary slides (used for my PhD Dissertation Proposal Examination)](https://yilimath.github.io/files/Birational/Moishezon/MoishezonSlides.pdf) [update 12.4]

(1) [Moishezon morphism part 1: Basic properties of Moishezon varieties](https://yilimath.github.io/files/Birational/Moishezon/MoishezonVar.pdf) [TODO]

(2) [Moishezon morphism part 2: Basic properties of Moishezon morphism (1)](https://yilimath.github.io/files/Birational/Moishezon/MoishezonMorphism.pdf) [update 9.25]

(3) [Moishezon morphism part 2: Basic properties of Moishezon morphism (2)](https://yilimath.github.io/files/Birational/Moishezon/MoishezonMorphism.pdf) [update 9.10]

(4) [Moishezon morphism Part 3: General type locus and Moishezon locus](https://yilimath.github.io/files/Birational/Moishezon/GeneralTypeLocus.pdf) [update 9.10]

(5) [Note-1: Seshadri projectivity criterion](https://yilimath.github.io/files/Birational/Moishezon/SeshadriCriterion.pdf)

(6) [Note-2: Chow-Barlet cycle space and lower-semi continuity of Seshadri constant](https://yilimath.github.io/files/Birational/Moishezon/lscSeshadriConstant.pdf) [Update 9.15]

(7) [Note-3: Alternating properties of projective locus, openness of projectivity](https://yilimath.github.io/files/Birational/Moishezon/OpenesssProj.pdf) [Update 9.15]


(8) [Moishezon morphism Part 4: Fiberwise bimeromorphic morphism](https://yilimath.github.io/files/Birational/Moishezon/FiberWiseBirational.pdf) [update 9.10]

(9) [Moishezon morphism Part 5: Algebraic approximation](https://yilimath.github.io/files/Birational/Moishezon/AlgebraicApproximation.pdf) [update 12.4]

(10) [Moishezon morphism Part 6: Inversion of adjunction](https://yilimath.github.io/files/Birational/BCHM/InverAdjunc.pdf) 

(11) [Moishezon morphism Part 8: Rational curves on Moishezon spaces](https://yilimath.github.io/files/Birational/BCHM/RationalCurveMoishezon.pdf)

(12) [Minimal model program in the Moishezon category](),




---
### Note-1: Basic properties of Moishezon varieties
---

In this note, we try to prove some elementary properties about Moishezon varieties. A Moishezon variety is defined to be a complex analytic variety that is bimeromorphic to a projective variety. It has several equivalent characterization: (1) Moishezon variety is complex analytic variety that has algebraic dimension equal to the geometric dimension (intuitively this means that Moishezon variety has plenty of subvarieties), (2) Moishezon variety is complex analytic variety that equipped with a big line bundle (big line bundle can be viewed as a birational counter part of ample line bundle).

Artin proved in [[Artin 70]()] that the categeory of (smooth) Moishezon varieties is equivalent to the category of (smooth) algebraic space of finite type. Thus, sometimes we also call the Moishezon variety the algebraic space. (As a side remark, algebraic space is an important object in moduli theory, and consequently the Moishezon variety will be a very interesting object to study)

Let us now summarize the basic properties that a Moishezon variety satisfies. We first state some properties in algebraic geometric flavor. The subvarieties of a Moishezon varity is again Moishezon (it will be helpful in the induction process). The surjective morphism sends a Moishezon variety to a Moishezon variety. We can lift the Moishezon variety via a finite map so that it is still a Moishezon variety. Like the algebraic space, the Moishezon variety has an Etale cover by some quasi-projective variety (which will sometimes be helpful to reduce the Moishezon problem into a quasi-projective problem). Moishezon variety can be written as finite group quotient of an algebraic variety (this looks to have connection with the homogenuous variety, which will be important subject study by Mok, Hwang etc. ) Second, Moishezon variety has some nice moduli properties, for example, the Hilbert scheme and Chow scheme of a proper Moishezon space have algebraic space structure, the irreducible component of the Hilbert scheme and connected component of the Chow scheme are proper. Finally, despite those properties with more algebraic geometric flavor, the Moishezon variety also has some complex analytic properties. As a ddbar manifold, Moishezon manifold share the strong Hodge decomposition. Sometimes the Moishezon problem can be reduced to the projective problem if it admits the Kahler metric and the singularity is rational.


For the detailed discussion see my lecture notes: [Moishezon morphism part 1: Basic properties of the Moishezon varieties](https://yilimath.github.io/files/Birational/Moishezon/MoishezonVar.pdf)

---
### Note-2: Basic Properties of the Moishezon morphism (1)
---

This time we go to Section 3 of the paper. We first try to prove prove the equivalence of different definitions (4 definitions) of Moishezon morphisms. We then summarize the basic properties of Moishezon morphism with proofs.

Moishezon morphism is defined to be a proper morphism between complex analytic spaces that is bimeromorphic to a projective morphism. Using the Hilbert scheme arguement we can characterize it as a morphism that is bimeromorphic base change from an algebraic family. We can also define it to be a morphism that has a big rank 1 reflexive sheaf (some literatual define the Moishezon morphism to have a big line bundle, we treat professor Kollár's definition as the standard one).

Having stated the definition, we show that important properties that will useful in the later study of this subject.


---
### Note-3: Basic Properties of Moishezon morphism (2)
Today we will continue our discussion on the paper [Moishezon morphism](https://www.intlpress.com/site/pub/pages/journals/items/pamq/content/vols/0018/0004/a011/index.php?mode=ns). Last time, we proved that a Moishezon manifold admits a (strong) Hodge decomposition. We also showed that a Kähler Moishezon space with 1-rational singularity is automatically projective, and finally, we gave three different definitions for Moishezon morphism and proved that they are equivalent. 


This time:

(1) We will prove that a proper surjective morphism equipped with a relatively big line bundle is locally bimeromorphic to a projective morphism.

(2) We will prove that if the base space is Moishezon, then the total space is Moishezon if and only if the morphism is Moishezon.

(3) We will show that the restriction of the generic surjective morphism on the exceptional set is a Moishezon morphism.


For the detailed discussion see my lecture notes: [Moishezon morphism part 3](https://yilimath.github.io/files/Birational/Moishezon/MoishezonMorphism.pdf)



---
### Note-4: Very big locus, general type locus and Moishezon locus
---

We will continue our discussion on the paper [Moishezon morphism](https://www.intlpress.com/site/pub/pages/journals/items/pamq/content/vols/0018/0004/a011/index.php?mode=ns). First, we will complete the proof that the Moishezon morphism is stable under base change. Then, we will delve into today's main topic: the alternating properties of the very big locus, general type locus, and Moishezon locus, which is either nowhere dense or contains some dense open subset.

Let us first sketch the idea of how to prove the alternating property of very big locus and general type locus. 

As for the Moishezon locus, the basic idea  appears in the paper [[RT1]()] and [[RT2]()]. 

For detailed information, see my lecture notes [Moishezon part 4](https://yilimath.github.io/files/Birational/Moishezon/GeneralTypeLocus.pdf)


---
### Note-5: The flat Moishezon morphism is fiberwise bimeromorphic to a projective morphism
---


This week, we will continue our discussion on the paper [Moishezon morphism](https://www.intlpress.com/site/pub/pages/journals/items/pamq/content/vols/0018/0004/a011/index.php?mode=ns). Last time, we discussed the structure theorems for the very big locus, general type locus, and Moishezon locus. As a direct consequence, we verify Conjecture 1 in the paper when the morphism is smooth. This time, we will begin the discussion of Section 4 of the paper. The main theorem of this section is Theorem 25, which shows that Moishezon morphism is not only bimeromorphic to a projective morphism but is indeed fiberwise bimeromorphic to a projective morphism as long as the singularity is mild (and not uniruled). We will prove the theorem this time.

Let us briefly sketch the idea of the proof: 

For the detailed information, see my lecture notes [Morphism morphism part 5](https://yilimath.github.io/files/Birational/Moishezon/FiberWiseBirational.pdf)


---
### Note-6: Algebraic approximation
---

In today's reading seminar(2024.9.25). We will focus on the algebraic approximation technique. We will study the algebraic approximation for the Moishezon morphism. 


Let us first briefly sketch the idea on how to construct the algebraic envelop? We will first consider the projective morphism to an open disk D. Since the deformation functor and Picard functor are representable in this setting. We can therefore construct a universal family over some base S. By the universality there exist a morphism from the open disk D to S. We restrict our attention on the image of the disk on S. This will give us the algebraic envelop. For the Moishezon morphism to the open disk D. As usual, we try to reduce the Moishezon problem into a  projective problem via a bimeromorphic morphism. The idea here is that we first construct the algebraic envelop for the projective family and we then apply Artin's result (TODO: How it works) extend the morphism from the projective central fiber to Moishezon central fiber. We finally show that the extension on the Moishezon central fiber gives the algebraic envelop as desired.


The second part of this note introduces some applications of algebraic approximation technique.  We will first use algebraic envelop to show that MMP works for a projective family over a Riemann surface. The singularities of the minimal model and canonical model are nice. We then use the algebraic approximation techniques showing the existence of a canonical modification for the Moishezon morphism.


Let us briefly sketch the idea of the existence of canonical modification for Moishezon morphism (this part of note will also appear in [Canonical and Terminal modification](https://yilimath.github.io/files/Birational/BCHM/CanonicalTerminalModification.pdf)). We first show the result from BCHM that the canonical modification exist for quasi-projective complex variety. Since the algebraic envelop of the Moishezon family is Moishezon, thus it's a Etale cover of some quasi-projective variety. Since canonical modification commute with Etale base change, the canonical modification exists on the algebraic envelop. We then check that the pull back of the canonical modification on the algebraic envelop is indeed the canonical modification of the family that we considered. (There is a question here, why )

Finally we make a remark that canonical modification may not always exist. For more applications of canonical modification see my note: [Canonical and Terminal modification](https://yilimath.github.io/files/Birational/BCHM/CanonicalTerminalModification.pdf)

---
### Note-7: Inversion of adjunction
---




---
### Note-8: How far Moishezon away from projective?
---

This note is a further discussion about Moishezon morphism beyond the paper. The question that we want to study in this part of note is to what extent we can generalize the classical birational geometry to the Moishezon case?

We first summarize some basic tools needed in the generalization. The 1st and most useful tool is the Chow type lemma, which birational changes the Moishezon morphism to a projective morphism. The 2nd useful tool will be the algebraic approximation by Artin.


---

---



---
### Note-1: Seshadri projectivity criterion

In 2024.9.4 reading seminar, we mainly focused on the proof of the Seshadri projectivity criterion of line bundle (and cohomology class) on a proper Moishezon space.

Let us briefly sketch the idea of the proof of the (line bundle version) Seshadri criterion: The easy direction is ampleness implies Seshadri inequalities. We first use the ample line bundle to construct some global generated line bundle. So, there is a divisor passing through any given point. Then the intersection product of the line bundle is greater than the local intersection product, and the local intersection product is greater than multiplicity. The opposite direction is more complicated. We prove it by blowing up a generic smooth point. We try to show that pull back line bundle via the blow up, and perturbed by the exceptional divisor is nef. We then apply Kleiman's nefness criterion and show that the top intersection number of the line bundle downstairs is positive. By induction on dimension, we can complete the proof of the theorem. (As a side remark, the Kodaira lemma holds for projective variety. On a non-projective variety, the arugment style above may be helpful).


For the cohomology class version Seshadri criterion, we require addition assumption that Moishezon space has 1-rational singularity. The point is under the 1-rational singularity assumption, the homological equivalent relation is the same as the numerical equivalent relation for 1-cycles. Thus, the cup product on the homology class will restrict to a linear functional on the numerical class. By duality, the linear functional can be realized as a Q-line bundle. Therefore, we reduce the cohomology version problem to the line bundle version problem.



---
### Note-2: Chow-Barlet cycle space with application to openess of projectivity problem

In 2024.9.11 reading seminar, we first complete the proof of Seshadri criterion that didn't finish last time. Then we will introduce the main technical tools in the paper, that is approximating Chow-Barlet cycle space using countable many projective morphism. Using this technical tool, we try to prove that if a Moishezon morphism with generic fiber haw rational singularity and the central fiber is projective, then the very general fibers near 0 are also projective.

Let us briefly sketch the idea of the proof of this theorem. We divide the collection of projective morphisms which used to approximate the Chow-Barlet cycle space into 2 types. The first type contains those projective morphism whose image of base in S is nowhere dense. The second type are the rest. We choose any point s in the complement of the locus of the first type. By properness of the morphism into S, the origin 0 contains in the image also. Thus we can find a holomorphic curve connecting both s and 0. Using the upper semi-continuity of the multiplicity function together with the fact that the 2 points in the same component of Chow variety have the same numerical property. We can finish the proof.

For detailed information, see my note [Note-2: Chow-Barlet cycle space and lower-semi continuity of Seshadri constant](https://yilimath.github.io/files/Birational/Moishezon/lscSeshadriConstant.pdf)

---
### Note-3: Alternating properties of projective locus and proof of the main theorem

This time (2024.9.18) we will finish the proof of the main theorem of the paper [Seshadri’s criterion and openness of projectivity](https://link.springer.com/article/10.1007/s12044-022-00680-9), Theorem 2. Before proving the openness of projectivity theorem, we need another result about alternating property of projective locus of a proper (Moishezon) morphism (we already see it [here](https://yilimath.github.io/files/Birational/Moishezon/GeneralTypeLocus.pdf). Combined with the theorem about projectivity of very general fibers that we proved last time, the proof of the main theorem is immediate.

For detailed information, see my note (https://yilimath.github.io/files/Birational/Moishezon/OpenesssProj.pdf).


