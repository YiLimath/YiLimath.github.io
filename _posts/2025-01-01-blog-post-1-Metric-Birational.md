---
title: 'Metric method in Birational Geometry'
date: 2026-09-21
permalink: /posts/2026/05/Metric-Method/
tags:
  - Birational geometry
  - Complex Geometry
---


In this series of notes, we summarize the metric methods that have become standard tools in birational geometry. Almost every result below follows the same pattern, and it is worth stating it once at the start.

> Build a metric whose singularities are exactly as bad as the geometry allows, then feed it into an $L^2$ estimate to produce a section. The birational content is in the choice of metric; the analysis is in the estimate.

The notes are ordered so that each part uses only what comes before it. Parts I and II are the machinery: singular metrics and multiplier ideals, then the extension theorem. Parts III to VIII are the applications, arranged by how much of that machinery they need — Part III uses only the vanishing theorem, Parts IV to VII use the extension theorem, and Part VIII needs everything and is still open. Part IX collects the transcendental statements. A reader who wants one application can start at the relevant part and refer back.

Where a result also has a purely algebraic treatment we say so and point to the [BCHM notes](https://yilimath.github.io/posts/2026/05/BCHM/) or the [adjunction notes](https://yilimath.github.io/posts/2025/05/Adjunction-Theory/) rather than repeating it.


---
## Part I. Singular Metrics, Currents, and Multiplier Ideals

Positivity in this theory is carried by singular Hermitian metrics and the closed positive currents they define. The order here is: define the objects, prove the vanishing theorem, then establish the two approximation results that let one replace an arbitrary metric by a manageable one.

Note-I.1 Singular Hermitian Metrics, Closed Positive Currents, and Lelong Numbers *(in preparation)*

Note-I.2 Multiplier Ideal Sheaves and Nadel Vanishing *(in preparation)*

Note-I.3 The Dictionary with Divisorial Singularities: klt, lc, and Log Canonical Thresholds *(in preparation)*

Note-I.4 Demailly Regularization and Approximation by Analytic Singularities *(in preparation)*

Note-I.5 The Strong Openness Theorem and Its Consequences *(in preparation)*

Note-I.6 Metrics with Minimal Singularities and Equisingular Approximations *(in preparation)*


---
## Part II. The $L^2$ Extension Theorem

The Ohsawa–Takegoshi theorem is the one technical input behind Parts IV to VIII. We start from the $\bar\partial$ estimate it rests on and end with the form that the birational applications actually invoke, which is the one with a singular metric on the twisting line bundle.

Note-II.1 Hörmander's $L^2$ Estimates and the Basic Existence Machinery *(in preparation)*

[Note-II.2 The Ohsawa–Takegoshi Extension Theorem and Why It Is Useful in Birational Geometry](https://yilimath.github.io/files/Birational/MetricMethod/OTExtension.pdf) [upd 10.8]

Note-II.3 The Optimal Constant: Błocki, Guan–Zhou, and Berndtsson–Lempert *(in preparation)*

Note-II.4 Extension with Singular Metrics: the Version Used in the Minimal Model Program *(in preparation)*


---
## Part III. Effective Results from Vanishing Alone

The first application, and the only one that does not need the extension theorem. Everything here comes from Nadel vanishing applied to a metric built by hand, so it can be read directly after Part I.

Note-III.1 The Fujita Conjecture: Statement, Evidence, and What Is Known *(in preparation)*

Note-III.2 Cutting Log Canonical Centers and the Theorem of Angehrn and Siu *(in preparation)*

Note-III.3 Effective Base Point Freeness and Separation of Jets *(in preparation)*


---
## Part IV. Extension of Pluricanonical Forms and Invariance of Plurigenera

The first genuine use of Ohsawa–Takegoshi: sections of $mK_X$ on a fibre or a divisor extend to the ambient space. Invariance of plurigenera is the model case; the dlt extension theorem is the form in which the method enters the minimal model program. The part ends with the two directions in which the theorem is still open — singular families, and non-projective ones.

[Note-IV.1 Păun's Analytic Proof of Invariance of Plurigenera](https://yilimath.github.io/files/Birational/MetricMethod/InvarPluri.pdf) [upd 5.11]

Note-IV.2 The Algebraic Counterpart: Kawamata and Nakayama via Asymptotic Multiplier Ideals *(in preparation)*

Note-IV.3 Demailly–Hacon–Păun's Proof of the DLT Extension Theorem *(in preparation)*

Note-IV.4 Degeneration of Plurigenera and What Fails without Smoothness *(in preparation)*

Note-IV.5 Invariance of Plurigenera beyond the Projective Case: Moishezon and Kähler Families *(in preparation)*

The algebraic extension theorems of Nakayama, Hacon–McKernan, and de Fernex–Hacon, which run parallel to Note-IV.3, are in [Part III of the BCHM notes](https://yilimath.github.io/posts/2026/05/BCHM/).


---
## Part V. Positivity of Direct Images

The same extension theorem, applied fibrewise, puts a singular Hermitian metric on $f_* \omega_{X/Y}^{\otimes m}$ with semipositive curvature. We fix the vocabulary for what that means first, then give the two constructions, then the classification results they yield.

Note-V.1 Positivity Notions for Torsion-Free Sheaves and Singular Hermitian Vector Bundles *(in preparation)*

Note-V.2 Păun–Takayama's Construction of Singular Hermitian Metrics on Direct Images of Relative (Pluri)canonical Sheaves *(in preparation)*

[Note-V.3 Hacon–Popa–Schnell's Construction of Singular Hermitian Metrics on Direct Images of Relative (Pluri)canonical Sheaves](https://yilimath.github.io/files/Birational/MetricMethod/HPSIitaka.pdf) [upd 10.24]

Note-V.4 The Iitaka Conjecture: Subadditivity of Kodaira Dimension *(in preparation)*

Note-V.5 Viehweg Hyperbolicity and Applications to Moduli *(in preparation)*


---
## Part VI. Metric Methods in the Canonical Bundle Formula

The canonical bundle formula splits $K_X$ along a fibration into a discriminant part and a moduli part, and the moduli part is the hard one. Positivity of direct images from Part V gives it directly, without variation of Hodge structure.

Note-VI.1 Hacon–Păun's Metric Method for the Canonical Bundle Formula *(in preparation)*

Note-VI.2 Positivity of the Moduli Part: the Metric Proof beside the Hodge-Theoretic One *(in preparation)*

Note-VI.3 The Semi-ampleness Conjecture for the Moduli Part *(in preparation)*

The algebraic development of the canonical bundle formula, subadjunction, and inversion of adjunction is in the [adjunction notes](https://yilimath.github.io/posts/2025/05/Adjunction-Theory/).


---
## Part VII. Effective Birationality and Boundedness

Now the estimates are used quantitatively. The constants in Parts II and III become explicit bounds on the multiple of $K_X$ that gives a birational map, and boundedness of the family follows from that bound together with a lower bound on volume.

Note-VII.1 Volumes, the DCC Conjecture, and the Statement of Birational Boundedness *(in preparation)*

Note-VII.2 Effective Birationality of Pluricanonical Maps: the Analytic Argument *(in preparation)*

Note-VII.3 Birational Boundedness for Varieties of General Type *(in preparation)*


---
## Part VIII. Non-vanishing, Abundance, and Finite Generation

The deepest applications, and the ones still open. The difficulty is uniform across them: one needs a section of $mK_X$ with no divisor available to extend from, so the metric has to be produced first and the section extracted from it afterwards. We set up the numerical framework, then take non-vanishing, abundance, and finite generation in that order, since each is used in the next.

Note-VIII.1 Numerical Dimension, Nakayama's $\sigma$-Decomposition, and the Shape of the Abundance Conjecture *(in preparation)*

Note-VIII.2 Siu and Păun's Analytic Approach to Shokurov's Non-vanishing *(in preparation)*

Note-VIII.3 Supercanonical Metrics and the Abundance Conjecture *(in preparation)*

Note-VIII.4 The Analytic Proof of Finite Generation of the Canonical Ring *(in preparation)*


---
## Part IX. Metric Methods in the Kähler and Analytic Setting

On a Kähler variety there are no divisors to work with, so the metric method is not one tool among several but the only one. This part records the transcendental statements that the earlier parts specialise to in the projective case; the minimal model program built on them is in the [Kähler MMP notes](https://yilimath.github.io/posts/2026/04/Kahler-MMP/).

Note-IX.1 Demailly–Păun's Characterisation of the Kähler Cone and Transcendental Morse Inequalities *(in preparation)*

Note-IX.2 Non-nef Locus, Non-Kähler Locus, and the Divisorial Zariski Decomposition *(in preparation)*


---
