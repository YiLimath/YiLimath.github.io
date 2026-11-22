---
title: 数学研究为什么需要显式的系统设计
permalink: /posts/2026/08/agent-system-zh/why-mathematicians-need-patterns/
tags:
- Agent System
- Mathematics
classes: agent-system-page
full_page_reading: true
lang: zh-CN
hidden: true
sitemap: false
search: false
robots: noindex, follow
read_time: false
translation_revision: 88f5a30
translation_of: /posts/2026/08/agent-system/why-mathematicians-need-patterns/
---

[English original](/posts/2026/08/agent-system/why-mathematicians-need-patterns/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**核心观点：**数学研究本来就是一组反复出现的活动。设计模式的价值，在于让研究循环保留失败路线并显露不确定性；普通 proof search 也需要这些机制。

数学研究包括阅读、检索、构造例子、提出猜想、寻找证明、检查断言和撰写论述。只有明确这些活动的边界，agent 才能成为有用的协作者。

## 把设计原则转化为数学工作

- **Decomposition：**拆成 lemmas、proof obligations 或可独立开展的检索。
- **Abstraction：**通过 definitions、contracts 和 representations，隐藏与当前问题无关的实现细节。
- **Composition：**组成证明或研究流程，使上一步的结果可以成为下一步的输入。
- **Encapsulation：**保持工具、模型和检索方法可替换。
- **Validation：**使用测试、反例、proof assistants、来源检查或人工审查。

## 求解循环与研究循环

求解和研究都受益于保留失败路线。开放研究还需明确不确定性、比较替代方法，并判断某项结果是否值得继续发展。设计模式帮助组织这些活动，却不会把听起来合理的模型解释变成证明。

## 质量标准

对数学工作，正确性必要但不充分。相关性、provenance、可复现性、可检查性，以及能否发现失败，也都是架构要求。

## 参考依据

这里将 Gulli 的[设计模式目录](https://link.springer.com/book/10.1007/978-3-032-01402-3)，以及 Dibia 在 [*Designing Multi-Agent Systems*](https://multiagentbook.com/) 中关于任务分解、workflow architecture、评估和 responsible AI 的讨论，转化为课程中的数学研究设计。各页末尾列出相应参考资料。

[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/) · [动手实验](/posts/2026/08/agent-system-zh/hands-on-lab/)
