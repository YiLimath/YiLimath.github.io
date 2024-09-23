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

(1) Part I: We will mainly focus on the classical paper by Hacon and Mckernan [[1]](https://link.springer.com/article/10.1007/s00222-006-0504-1) and Takayama's paper [[2]](https://link.springer.com/article/10.1007/s00222-006-0503-2). The main result shows the effective birationality of Kodaira map for smooth projective varieties of general type. There are several essential ingredients that will appear in the proof: Techniques to cut down the LC centers (which already appears [here](https://yilimath.github.io/posts/2024/08/Theorem-of-Angehrn-and-Siu/)), Kawamata's subadjunction formula, and Hacon-Mckernan's extension theorem. Let us briefly sketch the idea of the proof. We divide the proof into 3 steps. In step 1, we try to reduce the problem and show that it's suffics to find a threshold of birationality of Kodaira map that only depends on the volume. Step 2 is very similar to the proof of the theorem of Angehrn and Siu. In this step we try to construct some divisor such that the given very general point x is the isolated point of the multiplier ideal sheaf associated to this divisor. And this divisor is Q-linear equivalent to small multiple of the canonical divisor. In step 3, we will apply KV vanishing theorem to the exact sequence induced by the multiplier ideal sheaf of the divisors constructed in step 2. Differ from the theorem of Angehrn and Siu, we need to pick 2 general points in order to prove some birationality result. While the theorem of Angehrn and Siu requires to pick only 1 point, which will be enough for the purpose of base point freeness result.

(2) Part II: We will mainly focus on the DCC condition on volume of a log pair (see [[3]](https://annals.math.princeton.edu/2013/177-3/p06), [[4]](https://annals.math.princeton.edu/2014/180-2/p03). Let us first summarize all the knwon results about DCC of volumes. In [3], Hacon and Xu proved the DCC of volume for set of global quotients. In [4], Hacon-Mckernan-Xu proved the more general case DCC of volumes for log canonical models. Thus, in this note, we will only focus on the materials in [4]. Let us briefly sketch the idea of the proof ... 


(3) Part III: We will prove the ACC for log canonical threshold. This result can be an easy consequence of boundedness of log canonical models. We will prove it by induction assume the boundedness results in lower dimension. (the major reference of this part is [[4]](https://annals.math.princeton.edu/2014/180-2/p03)),

(4) Part IV, V: We will introduce the boundedness result on set of log canonical models and semi-log canonical models with fixed dimensions and bounded volumes. We divide the proof into the following steps: Step 1. We try to reduce the boundedness for semi-log canonical pairs to log canonical pairs, thanks to the correspondence between semi-log canonical pairs and log canonical pairs equipped with involution on the double locus after the normalization. Step 2. Using the DCC condition of volumes to control the number of irreducible components after normalization. Step 3. will be the most technical part of the proof. In this step, we try to find a bounded family, for which the given log canonical pairs is birationally isomorphic to some fiber of this family. Moreover we require that volume preserved the same. Step 4. We try to use some results related to abundance in family (good minimal model in family). And reduce the bounded family in step 3 into a family that all the fibers has canonical model. By replacing to that canonical model, we find a bounded family for which the given canical model is fiber of this family. (The strategy of the proof can be found in Section 7 of the paper [[5]](https://ems.press/journals/jems/articles/15330).)


---
---


For more detailed information, see my lecture notes:

(1) [Part I: Boundedness of pluricanonical map for variety of general type](https://yilimath.github.io/files/Birational/BoundednessGeneralType/DCCVolume.pdf)

(2) [Part II: DCC condition of volume](https://yilimath.github.io/files/Birational/BoundednessGeneralType/DCCVolume.pdf)

(3) [Part III: ACC of log canonical threshold](https://yilimath.github.io/files/Birational/BoundednessGeneralType/ACCLCT.pdf)

(4) [Part IV: Boundedness of canonical models](https://yilimath.github.io/files/Birational/BoundednessGeneralType/BoundedCanonicalModel.pdf)

(5) [Part V: Boundedness of semi-log canonical models](https://yilimath.github.io/files/Birational/BoundednessGeneralType/BoundedSLCM.pdf)


(6) [Supplement: Effective Matsusaka's big theorem](https://yilimath.github.io/files/Birational/BoundednessGeneralType/BigMatsusaka.pdf)
