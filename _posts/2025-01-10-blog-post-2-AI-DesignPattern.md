---
title: 'Agent System Design Pattern'
date: 2026-08-01
permalink: /posts/2026/08/Agent-System/
tags:
  - Agent System
---

The aim of this note is to give a brief introduction to the design patterns used in building agent systems. The material is divided into independent pages so that each pattern can be read on its own and later combined with the others.

> An agent system is a way of trading determinism for flexibility. The design patterns are the tools for buying back as much determinism as the task requires.

The organizing question is:

> Where does the system need flexibility, and where does it need a stable, testable interface?

Each page uses the same template: recurring problem, intent, structure, stable interface, variable implementation, forces, trade-offs, failure modes, and example.

## Part I. Foundations

1. [Terminology and building blocks](/posts/2026/08/agent-system/foundations/)
2. [The core agent loop](/posts/2026/08/agent-system/core-loop/)

## Part II. Control-flow patterns

3. [Prompt chaining](/posts/2026/08/agent-system/prompt-chaining/)
4. [Router](/posts/2026/08/agent-system/router/)
5. [Parallelization](/posts/2026/08/agent-system/parallelization/)
6. [Plan and execute](/posts/2026/08/agent-system/plan-and-execute/)

## Part III. Reliability and boundary patterns

7. [Reflection](/posts/2026/08/agent-system/reflection/)
8. [Tool use](/posts/2026/08/agent-system/tool-use/)
9. [Memory management](/posts/2026/08/agent-system/memory-management/)
10. [Human in the loop](/posts/2026/08/agent-system/human-in-the-loop/)

## Part IV. Cooperation and adaptation

11. [Multiple-agent cooperation](/posts/2026/08/agent-system/multiple-agent-cooperation/)
12. [Learning and adaptation](/posts/2026/08/agent-system/learning-and-adaptation/)
13. [Choosing and composing patterns](/posts/2026/08/agent-system/choosing-patterns/)

## Part V. Case study

14. [A mathematical research agent system](/posts/2026/08/agent-system/math-research-case-study/)

The case study describes a system that supports daily research scheduling, paper encoding, and mathematical proof checking over an Obsidian vault. It identifies which pattern each component instantiates, including the places where a design had to be revised.
