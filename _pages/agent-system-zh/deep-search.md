---
title: 围绕缺失论证开展深入检索
permalink: /posts/2026/08/agent-system-zh/deep-search/
tags:
- Agent System
- Mathematics
classes: agent-system-page
full_page_reading: true
lang: zh-CN
read_time: false
translation_revision: 88f5a30
translation_of: /posts/2026/08/agent-system/deep-search/
---

[English original](/posts/2026/08/agent-system/deep-search/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/knowledge-retrieval/)。下面的几何参考是案例 的可选扩展。

提升问题可能出现在扩展、限制、消失或障碍类别下。在扩展词汇量之前分解数学需求。分别搜索sufficient-消失和direct-obstruction路由。

<a id="the-contract"></a>

## 接口约定

保存经过检查的定理命题、稳定定位器、拒绝的匹配以及有希望的未经检查的线索。有用的报告确定了最小的剩余适用性问题。它给下一个执行单元一个前沿，而不是一堆链接。

<a id="trade-offs-and-failure-modes"></a>

## 权衡和故障模式

当找到合适的结果、预算结束或搜索重复证据时停止。在检查的语料库中未能找到定理并不能证明不存在这样的定理。新奇的断言同样需要的不仅仅是一次不成功的搜索。

<a id="build-and-test"></a>

## 构建和测试

使用十个查询的预算。返回来源、记录表、拒绝的近似匹配、剩余线索以及关于搜索的明确有界结论。

使用[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)和[工作台实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)。记录输入、预期结果、实际结果以及预期的数学原因。有关参考文献和断言边界，请参阅 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/)。

<a id="worked-design-decision-search-a-missing-bridge-not-a-broad-topic"></a>

## 设计决策实例：搜索缺失的衔接论证，不是一个广泛的主题

找到相关定理后，搜索确切的不匹配假设或比较引理。记录查询、语料库、来源版本以及每个结果更改论证的原因。关于同一主题的更多论文不一定是进步。

**接受练习。** 以有界覆盖范围命题停止：检查了哪些源，哪些源仍然无法访问，以及哪些衔接论证保持打开状态。搜索失败并不能证明定理不存在。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
