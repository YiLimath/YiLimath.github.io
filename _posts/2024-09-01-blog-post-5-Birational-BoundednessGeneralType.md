---
title: 'Birational Geometry Note: Boundedness of Varieties of General Type'
date: 2025-08-13
permalink: /posts/2025/08/Boundedness-General-Type/
tags:
  - Birational geometry
  - Boundedness
  - General Type
---

The aim of this series of notes is to summarize the bounded results for the varieties of general type. 


## Part I. Birational boundedness for smooth projective varieties of general type

We will mainly focus on the classical paper by [HM08](https://link.springer.com/article/10.1007/s00222-006-0504-1) and [[Takayama08]](https://link.springer.com/article/10.1007/s00222-006-0503-2). The main result shows the effective birationality of Kodaira map for smooth projective varieties of general type. There are several essential ingredients that will appear in the proof: Techniques of Angehrn and Siu (see [here](https://yilimath.github.io/posts/2024/08/Theorem-of-Angehrn-and-Siu/)), Kawamata's subadjunction formula (see [here]()), and Hacon-Mckernan's extension theorem (see [here](https://yilimath.github.io/files/Birational/BCHM/HaconMckernanExtension.pdf)). Let us briefly sketch the idea of the proof. We divide the proof into 3 steps. In step 1, we try to reduce the problem and show that it's suffics to find a threshold of birationality of Kodaira map that only depends on the volume due to Tsuji. Step 2 we try to use the techniques of Angehrn and Siu and prove that some plurigenera is greater than 2 so that we can construct some fibration over the smooth rational curve. In step 3, we apply the same idea as [Kol86, Theorem 4.6], by induction on dimension (since the fibers have dimension n-1) and therefore find the effective birationality bound.

Once we have the effective birationality of Kodaira map, birational boundedness result is immediate by using Chow variety to parameterize the image of the Kodaira maps.

And finally we can show the boundedness result about canonical models. The idea is: pick the family in birational boundedness problem. Taking some resolution and stratification on that family, we may assume the fibers are smooth and are of general type. Then apply Siu's invariance of plurigenera, we can find a uniform finite generated index of the canonical ring of the fibers. With the proj construction thus gives the fiberwise canonical model.


[Note-1: Boundedness of pluricanonical map for variety of general type](https://yilimath.github.io/files/Birational/BoundednessGeneralType/DCCVolume.pdf)



---
## Part II. ACC Phenonmenon and Behavior of volumes

We will mainly focus on the ACC and DCC phenonmenon, we will prove DCC on volume of a log pair (see [[3]](https://annals.math.princeton.edu/2013/177-3/p06), [[4]](https://annals.math.princeton.edu/2014/180-2/p03). Let us first summarize all the knwon results about DCC of volumes. In [3], Hacon and Xu proved the DCC of volume for set of global quotients. In [4], Hacon-Mckernan-Xu proved the more general case DCC of volumes for log canonical models. Thus, in this note, we will only focus on the materials in [4]. Let us briefly sketch the idea of the proof .... We will also prove the ACC for log canonical threshold. This result can be viewed as an easy consequence of boundedness of log canonical models. We will prove it by induction assume the boundedness results in lower dimension. (the major reference of this part is [[4]](https://annals.math.princeton.edu/2014/180-2/p03)),


[Note-1: ACC of log canonical threshold](https://yilimath.github.io/files/Birational/BoundednessGeneralType/ACCLCT.pdf)

[Note-2: DCC of volume](https://yilimath.github.io/files/Birational/BoundednessGeneralType/DCCVolume.pdf)


[Note-3: Boundedness and pseudo-effective threshold](),


---
## Part III. Abundance in Families




---
## Part IV. Log birational boundedness and log boundedness for varieties of general type


We will introduce the boundedness result on set of log canonical models and semi-log canonical models with fixed dimensions and bounded volumes. We divide the proof into the following steps: Step 1. We try to reduce the boundedness for semi-log canonical pairs to log canonical pairs, thanks to the correspondence between semi-log canonical pairs and log canonical pairs equipped with involution on the double locus. Step 2. Using the DCC condition of volumes to control the number of irreducible components after normalization. Step 3. will be the most technical part of the proof. In this step, we try to find a bounded family, for which the given log canonical pairs is birationally isomorphic to some fiber of this family. Moreover we require that volume remain the same. Step 4. We try to use some results related to abundance in family (good minimal model in family). And reduce the bounded family in step 3 into a family that all the fibers have canonical models. By replacing to that canonical model, we find a bounded family for which the given canical model is fiber of this family. (The strategy of the proof can be found in Section 7 of the paper [[5]](https://ems.press/journals/jems/articles/15330)


[Note-5: Boundedness of canonical models](https://yilimath.github.io/files/Birational/BoundednessGeneralType/BoundedCanonicalModel.pdf)

[Note-6: Boundedness of semi-log canonical models](https://yilimath.github.io/files/Birational/BoundednessGeneralType/BoundedSLCM.pdf)

