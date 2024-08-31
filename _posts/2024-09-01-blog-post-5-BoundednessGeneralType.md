---
title: 'Birational Geometry Note: Boundedness of Varieties of General Type'
date: 2024-08-31
permalink: /posts/2024/08/Boundedness-General-Type/
tags:
  - Birational geometry
  - Boundedness
  - General Type
---

The aim of this series of notes is to summarize the bounded results for the varieties of general type. 

Here is the outline of this series of notes:

(1) Part I: We will mainly focus on the classical paper by Hacon and Mckernan [Boundedness of pluricanonical maps of varieties of general type](https://link.springer.com/article/10.1007/s00222-006-0504-1) and Takayama [Pluricanonical systems on algebraic varieties of general type](https://link.springer.com/article/10.1007/s00222-006-0503-2), the main result of this paper shows the effective birationality of Kodaira map for smooth projective varieties of general type. There are several essential ingredients that will appear in the proof: Techniques to cut down the LC centers (which already appears in the proof of theorem of Angehrn and Siu), Kawamata's subadjunction formula, and Hacon-Mckernan's extension theorem. Let us briefly sketch the idea of the proof. The proof is very similar to the theorem of Angehrn and Siu. We divide the proof into 3 steps. In step 1, we try to reduce the problem and show that it's suffics to find a threshold of birationality of Kodaira map that only depends on the volume. Step 2 is very similar to the proof of the theorem of Angehrn and Siu. In this step we try to construct some divisor such that the given very general point x is the isolated point of the multiplier ideal sheaf associated to this divisor. And this divisor is Q-linear equivalent to small multiple of the canonical divisor. In step 3, we will apply KV vanishing theorem to the exact sequence associated to the multiplier ideal sheaf induced by divisors constructed in step 2. Differ from theorem of Angehrn and Siu, we need to pick 2 general points in order to prove birationality. While the theorem and Angehrn and Siu requires to pick 1 points in order to prove the base point freeness.


(2) Part II: We will mainly focus on the DCC condition on volume of a log pair (see [On the birational automorphisms of varieties of general type](https://annals.math.princeton.edu/2013/177-3/p06), [ACC for log canonical thresholds](https://annals.math.princeton.edu/2014/180-2/p03). Let us first summarize all the knwon results about DCC of volumes. In the paper 

(3) Part III: We will prove the ACC for log canonical threshold. This result can be an easy consequence of boundedness of log canonical models. We will prove it by induction assume the boundedness results in lower dimension. (the major reference of this part is [ACC for log canonical thresholds](https://annals.math.princeton.edu/2014/180-2/p03)),

(4) Part IV, V: We will introduce the boundedness result on set of log canonical models and semi-log canonical models with fixed dimensions and bounded volumes. We divide the proof into the following steps: Step 1. We try to reduce the boundedness for semi-log canonical pairs to log canonical pairs, thanks to the correspondence between semi-log canonical pairs and log canonical pairs equipped with involution on the double locus after the normalization. Step 2. Using the DCC condition of volumes to control the number of irreducible components after normalization. Step 3. will be the most technical part of the proof. In this step, we try to find a bounded family, for which the given log canonical pairs is birationally isomorphic to some fiber of this family. Moreover we require that volume preserved the same. Step 4. We try to use some results related to abundance in family (good minimal model in family). And reduce the bounded family in step 3 into a family that all the fibers has canonical model. By replacing to that canonical model, we find a bounded family for which the given canical model is fiber of this family. (The strategy of the proof can be found in Section 7 of the paper [Boundedness of moduli of varieties of general type](https://ems.press/journals/jems/articles/15330).)


---
---


For more detailed information, see my lecture notes:

(1) [Part I: Boundedness of pluricanonical map for variety of general type](https://yilimath.github.io/files/Birational/BoundednessGeneralType/DCCVolume.pdf)

(2) [Part II: DCC condition of volume](https://yilimath.github.io/files/Birational/BoundednessGeneralType/DCCVolume.pdf)

(3) [Part III: ACC of log canonical threshold](https://yilimath.github.io/files/Birational/BoundednessGeneralType/ACCLCT.pdf)

(4) [Part IV: Boundedness of canonical models](https://yilimath.github.io/files/Birational/BoundednessGeneralType/BoundedCanonicalModel.pdf)

(5) [Part V: Boundedness of semi-log canonical models](https://yilimath.github.io/files/Birational/BoundednessGeneralType/BoundedSLCM.pdf)