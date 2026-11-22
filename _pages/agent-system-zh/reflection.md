---
title: 把反思变成可检验的异议
permalink: /posts/2026/08/agent-system-zh/reflection/
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
translation_of: /posts/2026/08/agent-system/reflection/
---

[English original](/posts/2026/08/agent-system/reflection/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/verification-gate/)。下面的几何参考是案例 的可选扩展。

在案例B中，“更加严格”是不可行的。 “估计允许 C 依赖于 j，但紧致性步骤需要一致界”指定了缺失的衔接论证。批评家应该找出数学缺陷。

<a id="the-contract"></a>

## 接口约定

提供完整的论证及相关证据。返回受影响的推理、违规情况、证据和可能的修复。如果修复加强了定理，则记录一个新分支而不是替换原始目标。

<a id="trade-offs-and-failure-modes"></a>

## 权衡和故障模式

审查者可以共享盲点。重复约定并不是证明凭证。 界修订循环并保留以前的草稿，以便可以将真正的修复与释义区分开来。批评本身可能是错误的，应该有可检验的推理的支持。

<a id="build-and-test"></a>

## 构建和测试

诊断交换量词的案例 B 证明。给出确切的反例 u_j=j 并区分寻求一致估计和削弱目标。

使用[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)和[工作台实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)。记录输入、预期结果、实际结果以及预期的数学原因。有关参考文献和断言边界，请参阅 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/)。

<a id="worked-design-decision-turn-criticism-into-a-falsifiable-objection"></a>

## 设计决策实例：将批评变成可证伪的反对意见

为了证明开区间上的每个连续函数都达到最小值，有用的批评家可以识别不受支持的紧致性步骤并在 (0,1) 上提供 f(x)=x。要求“认真思考”既不能提供诊断，也不能提供修复。

**验收练习。** 修复后，检查更改后的推理。添加紧致性给出不同的定理；替换论证需要新的证明。保留原来的目标，这样无声的削弱就无法通过。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
