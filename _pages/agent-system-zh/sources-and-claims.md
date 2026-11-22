---
title: 参考资料、证据与示例的适用边界
permalink: /posts/2026/08/agent-system-zh/sources-and-claims/
classes: agent-system-page
full_page_reading: true
lang: zh-CN
read_time: false
translation_revision: 88f5a30
translation_of: /posts/2026/08/agent-system/sources-and-claims/
tags:
- Agent System
---

[English original](/posts/2026/08/agent-system/sources-and-claims/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

本系列把已有软件设计模式与面向数学研究的架构提案结合起来。引用设计模式书籍说明概念的来源，并不证明这里提出的数学研究系统已经有效。

## 原始来源支持什么

| 来源 | 本课程使用的内容 | 不能由此推出什么 |
|---|---|---|
| [Bundy, Proof Planning (1996)](https://cdn.aaai.org/AIPS/1996/AIPS96-033.pdf) | 带有 preconditions 的方法与 proof-search control | 通用语言模型研究者的可靠性 |
| [Lean：axioms](https://lean-lang.org/doc/reference/latest/Axioms/) | formal result 取决于实际编码的命题与使用的 axioms | informal-to-formal translation 必然正确 |
| [Stacks Project：effective Cartier divisors](https://stacks.math.columbia.edu/tag/0C4S) | 案例 A 的 ideal-sheaf 约定 | 当前几何情境自动满足某条 vanishing theorem |
| [Anthropic, Building effective agents](https://www.anthropic.com/research/building-effective-agents) | 固定 workflow 与动态选择动作的区别 | 数学研究必须使用多少个 worker |
| [Danus v2](https://arxiv.org/abs/2607.06447v2) | 文献报告的 fact-graph orchestration | 每条被纳入的 informal claim 都正确 |
| [Rethlas–Archon v2](https://arxiv.org/abs/2604.03789v2) | informal reasoning 与 Lean formalization 的分工 | informal review 与 kernel checking 等价 |

## 参考书籍

Antonio Gulli 的 *Agentic Design Patterns* 提供广泛的模式目录。本地附件目录将 chaining、routing、parallelization、reflection、tools、planning、multi-agent work 列为第 1–7 章，之后讨论 memory 等运行模式。这些名称组织的是数学接口约定之下的实现选择。

Victor Dibia 的 *Designing Multi-Agent Systems*，以及 Lakshmanan 与 Hapke 的 *Generative AI Design Patterns*，提供互补的工程视角。与具体框架绑定的机制，应理解为可以替换的实现。本系列不依赖特定 vendor SDK、某一代模型，或对 AI 永久能力边界的预测。

## 文中证据标签的含义

**Worked argument** 表示文中给出了实际推理。**Design proposal** 指定准备实现和测试的行为。**Reported system** 把系统描述归于明确来源。**Historical implementation note** 可能只是某次本地快照，复现前需要固定版本。

实验采用 ChatGPT 或 Codex 的引导式工作流程。书面协议说明预期行为；实际执行仍需记录和评估。只有明确标识的 Lean 练习提供 proof-assistant checks。

三个贯穿课程的案例是结论明确的教学例子，不是对开放研究问题的解决。birational geometry 工作坊是专门化设计；使用来源定理前，仍须检查它的真实假设。

## 来源审查练习

选一条引用，写出它实际支持的断言，并记录精确 locator。再列出哪些额外断言还需要新证据。例如，描述 verifier 的论文可以支持这个组件的存在；测量其 false-acceptance rate 需要评估；声称 soundness 则需要另一种论证。

[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/) · [动手实验](/posts/2026/08/agent-system-zh/hands-on-lab/)
