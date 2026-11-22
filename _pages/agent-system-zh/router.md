---
title: 按照所需证据分配任务
permalink: /posts/2026/08/agent-system-zh/router/
tags:
- Agent System
classes: agent-system-page
full_page_reading: true
lang: zh-CN
hidden: true
sitemap: false
search: false
robots: noindex, follow
read_time: false
translation_revision: 88f5a30
translation_of: /posts/2026/08/agent-system/router/
---

[English original](/posts/2026/08/agent-system/router/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/plan-and-execute/)。下面的几何参考是案例 的可选扩展。

在案例 B 中，找到紧致性定理、检查常数相关性以及证明达到极限是不同的任务。路由器应该检查未解决的待解决事项，而不是将包含“分析”的所有内容路由给一位专家。

<a id="the-contract"></a>

## 接口约定

来源处理程序返回来源和建议的匹配；计算处理程序返回输入和解释输出； 审查者返回推理的评估。他们共用的信封保存着不同的证据类型。路由成功并不能证明成功。

<a id="trade-offs-and-failure-modes"></a>

## 权衡和故障模式

当待解决事项未指定时允许弃权。记录路由原因并允许在有新证据后重新分配。分类是一种搜索决策；规则、模型或研究人员可以在不改变其数学状态的情况下实现它。

<a id="build-and-test"></a>

## 构建和测试

将“证明限制合理性”分为拓扑、均匀性、紧致性和标识待解决事项。指定可以结束每一项的证据。

使用[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)和[工作台实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)。记录输入、预期结果、实际结果以及预期的数学原因。有关参考文献和断言边界，请参阅 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/)。

<a id="worked-design-decision-route-an-unresolved-estimate"></a>

## 设计决策实例：路由未解决的估计

假设一个证明需要一个独立于参数的界。如果引用的定理提供了界，则路由至来源检查，并以确切的参数依赖性作为问题。如果定理不适用，则转至数学论证或反例搜索。将相同的问题发送到更多文献执行单元并不能修复失败的假设。

**验收练习。** 要求结果命名缺失的估计值、其量词以及消解所需的证据。测试一个不明确的请求，并检查路由器是否请求缺少的域而不是发明一个域。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
