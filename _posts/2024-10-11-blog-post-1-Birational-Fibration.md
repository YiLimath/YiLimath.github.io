---
title: 'Fibration and Foliation in Algebraic Geometry'
date: 2026-07-03
permalink: /posts/2026/07/Fibration-in-Birational-Geometry/
tags:
  - Birational geometry
---

The aim of this series of notes is to introduce fibrations in algebraic geometry (the classification theory of complex algebraic/analytic varieties). Fibrations are among the most powerful tools for the classification of varieties, and fibration structures are particularly well suited to inductive arguments. In these notes, we focus mainly on applications of fibrations to classification results.

> In algebraic geometry (birational geometry), we understand varieties using fibrations.

The guiding philosophy of the series: every variety is built, via fibrations, out of three types of building blocks — **Fano varieties** (the $\kappa = -\infty$ direction, appearing as fibers of Mori fiber spaces), **Calabi–Yau varieties** ($\kappa = 0$, appearing as fibers of the Iitaka fibration), and **varieties of general type**. Part I constructs the canonical fibrations attached to any variety; Part II studies the fibrations produced by the minimal model program; the later parts develop the positivity theory of fibrations and apply the whole machinery to structure theorems. Foliations enter as "infinitesimal fibrations": they are the natural language when an honest fibration does not exist yet.

## Part I. Canonical Fibrations in Algebraic Geometry

This part of the notes is based on [Fibrations in Algebraic Geometry and Applications](https://smf.emath.fr/publications/fibrations-en-geometrie-algebrique-et-applications) by Professor Voisin. What is new is that we add more applications in birational geometry. The general idea is

> We try to construct fibrations for which the fibers are simpler than the total space, reducing in principle the study to phenomena on the base.

[Note-I.0 Why Fibrations? Classification of Surfaces and the General Machine]()

[Note-I.1 Iitaka Fibrations with Applications](https://yilimath.github.io/files/Birational/Fibration/iitaka.pdf) [upd 7.5]

[Note-I.2 Albanese Map with Applications](https://yilimath.github.io/files/Birational/Fibration/Albanese.pdf) [upd 10.10]

[Note-I.3 MRC Fibrations with Applications](https://yilimath.github.io/files/Birational/Fibration/MRC.pdf) [upd 10.19]

[Note-I.4 Nef Reduction with Applications]()

[Note-I.5 Algebraic Reduction with Applications]()


----
## Part II. Fibrations from the Minimal Model Program

The canonical fibrations of Part I are constructed from intrinsic invariants (pluricanonical systems, one-forms, rational curves). The minimal model program produces fibrations of a different origin: extremal contractions of fiber type. Running the MMP, every variety with $\kappa = -\infty$ (conjecturally) ends in a **Mori fiber space**, whose fibers are Fano; every variety with $0 \leq \kappa < \dim X$ carries (after passing to a minimal model) a **Calabi–Yau fibration**, its Iitaka fibration. This part studies these two classes of fibrations and the canonical bundle formula that governs them.

[Note-II.1 Cone and Contraction Theorems: Fibrations as Outputs of the MMP]()

[Note-II.2 Fano Fibrations (Mori Fiber Spaces): Conic Bundles, del Pezzo Fibrations, and Rationality Problems]()

[Note-II.3 Calabi–Yau Fibrations II: The Canonical Bundle Formula for klt-Trivial Fibrations (Fujino–Mori, Ambro), Discriminant and Moduli Parts]()

[Note-II.4 Canonical bundle formulas]()


---
## Part III. Foliation in Algebraic Geometry

[Note-IV.1 Campana–Păun's Algebraic Criterion for Foliations and Cao–Păun's Generalization]()

[Note-IV.2 Algebraically Integrable Foliations: From Foliations to Fibrations]()


---
## Part V. Beauville–Bogomolov–Yau Decomposition

In this part of the notes, I summarize recent developments on the Beauville–Bogomolov decomposition for singular (klt) Calabi–Yau varieties, in both the projective and the Kähler settings. The major reference of my note is [Beauville-Bogomolov decomposition for klt varieties](https://arxiv.org/abs/2509.10053) by Henri Guenancia.

[Note-V.1 Local Triviality of the Albanese Fibration]()

[Note-V.2 Splitting of the Tangent Sheaf]()

[Note-V.3 Proof of the Beauville–Bogomolov–Yau Decomposition (Projective klt Pair)]()

[Note-V.4 Algebraic Approximation for Kähler Calabi–Yau Manifolds]()

[Note-V.5 Proof of the Beauville–Bogomolov–Yau Decomposition (Kähler klt Pair)]()


---
## Part VI. Structure Theorems for Projective/Kähler Varieties with Nef Anti-canonical Bundle

In this part of the notes, I summarize classification results for projective/Kähler varieties with nef anti-canonical bundle. This is where the whole machinery of the series comes together: the MRC and Albanese fibrations (Part I), positivity of direct images (Part III), splitting of the tangent sheaf, and the BBY decomposition (Part V). The main references for this part are [DPS 94](https://mathscinet.ams.org/mathscinet/article?mr=1257325), [DPS 01](https://mathscinet.ams.org/mathscinet/article?mr=1875649), [CCM21](https://content.algebraicgeometry.nl/2021-4/2021-4-013.pdf), [Wang22](https://link.springer.com/article/10.1007/s00208-021-02275-7), [MW25](https://link.springer.com/article/10.1007/s00208-024-02934-5), [MW25](https://ems.press/journals/jems/articles/14299169), [MWWZ25](https://arxiv.org/pdf/2506.23218).

[Note-VI.0 Overview](https://yilimath.github.io/files/Birational/Fibration/OverviewNefAnticanonical.pdf) [4.3]

[Note-VI.1 Numerical Flatness Criteria](https://yilimath.github.io/files/Birational/Fibration/NumericalFlatness.pdf)

[Note-VI.2 Positivities of the Direct Images](https://yilimath.github.io/files/Birational/Fibration/WeaklyPositiveCurvedDirectImage.pdf) [4.4]

[Note-VI.3 Birational Geometry of the MRC/Albanese Fibration](https://yilimath.github.io/files/Birational/Fibration/BirationalMRC.pdf)

[Note-VI.4 Criteria for Fibrations to Be Locally Trivial]()

[Note-VI.5 Splitting of the Tangent Sheaf](https://yilimath.github.io/files/Birational/Fibration/SplitTangent2.pdf)

[Note-VI.6 Structure Theorem for klt Projective Varieties with Nef Anti-canonical Bundle]()

[Note-VI.7 Structure Theorem for klt Kähler Varieties with Nef Anti-canonical Bundle](https://yilimath.github.io/files/Birational/Fibration/StructureNefAntiCanonical.pdf)

[Note-VI.8 On the Hacon–McKernan Question](https://yilimath.github.io/files/Birational/Fibration/HaconMckernanQuestion.pdf)
