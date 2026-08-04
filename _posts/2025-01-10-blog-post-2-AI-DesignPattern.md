---
title: 'Agent System Design Pattern'
date: 2026-04-04
permalink: /posts/2026/01/Agent-System/
tags:
  - Agent System
---

The aim of this note is to give a brief introduction to the design patterns used in building agent systems. By an *agent system* I mean a program in which a language model is placed inside a loop: it is given a goal, a set of tools it may call, and some working memory, and it decides for itself which tool to call next until the goal is met. The interesting engineering question is not "which model is best" but rather: **what should be in the model's context at each step, and who decides what happens next — the model, or the program around it?** Almost every design pattern below is an answer to one of these two questions.

We divide the note into two parts: (1) the common design patterns for agent systems, and (2) a case study of the agent system I built for my own mathematical research.

> An agent system is a way of trading determinism for flexibility. The design patterns are the tools for buying back as much determinism as the task requires.

---

## Part I. Common Design Patterns

[I.0 Terminology]

[I.1 Prompt chaining pattern]

[I.2 Router pattern]

[I.3 Parallelization pattern]

[I.4 Reflection pattern] 

[I.5 Tool use pattern]

[I.6 Multiple agent cooperation pattern]

[I.7 Plan pattern]

[I.8 Memory management pattern]

[I.9 Learning and adapdation pattern]

[I.10 Human in the loop pattern]



---

## Part II. Agent Systems in Examples

In the second part of this note I case study the design of a concrete agent system: the one I built to support my own work in birational geometry. It runs over an Obsidian vault of roughly 11,600 mathematical notes, and it exists to do three things — keep my daily research schedule, turn papers into structured notes, and check mathematics I have written.

I will describe each component and identify which pattern from Part I it instantiates, including the places where I chose a pattern badly and had to change it.


