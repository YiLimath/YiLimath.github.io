---
title: 监测目标是否被悄悄替换
permalink: /posts/2026/08/agent-system-zh/goal-monitoring/
tags:
- Agent System
classes: agent-system-page
full_page_reading: true
lang: zh-CN
read_time: false
translation_revision: 88f5a30
translation_of: /posts/2026/08/agent-system/goal-monitoring/
---

[English original](/posts/2026/08/agent-system/goal-monitoring/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/evaluation-monitoring/)。下面的几何参考是案例 的可选扩展。

情况 可能以提升、指定 section 的合理不可提升结果或开放obstruction结束。情况 B 可能会产生有用的估计，但不具有目标所需的一致性。这些结果应该有不同的名称。

<a id="the-contract"></a>

## 接口约定

保持目标在一次尝试中不可变。附加假设创建条件分支。最终报告确定了确切的目标版本、证据、剩余假设以及下一步的信息行动。

<a id="trade-offs-and-failure-modes"></a>

## 权衡和故障模式

预算耗尽会结束执行，而不是数学。当程序保持打开状态时，局部引理可以完成。对话练习要求您区分可用的、有条件的和未解决的结果。检查实际反应；该指令并不强制执行这些状态。

<a id="build-and-test"></a>

## 构建和测试

报告案例 B，仅提供与参数相关的估计值。陈述部分结果和缺失的一致性断言，但不声称主要问题已解决。

使用[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)和[工作台实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)。记录输入、预期结果、实际结果以及预期的数学原因。有关参考文献和断言边界，请参阅 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/)。

<a id="worked-design-decision-detect-a-solved-substitute"></a>

## 设计决策实例：检测已解决的替代品

目标是将提升指定的对 (a,b) 转换为常数函数。生成 (1,1) 的提升无法求解目标 (1,0)。监视实际的输入、输出和量词，而不是监视对话是否包含合理的解决方案。

**接受练习。** 将原始目标保留在当前子目标旁边。每个完成的子目标都需要一个指定的蕴涵返回目标。目标的改变需要明确的决定，并且使早期的任务悬而未决。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
