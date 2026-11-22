---
title: 数学研究的基本循环
permalink: /posts/2026/08/agent-system-zh/core-loop/
tags:
- Agent System
classes: agent-system-page
full_page_reading: true
lang: zh-CN
read_time: false
translation_revision: 88f5a30
translation_of: /posts/2026/08/agent-system/core-loop/
---

[English original](/posts/2026/08/agent-system/core-loop/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/codex-research-studio/)。下面的几何参考是案例 的可选扩展。

在情况 中，找到消失定理并不完整：确切的扭曲及其假设必须匹配。下一步行动可能是适用性检查，而不是另一份proof草稿。有用的迭代从打开的待解决事项开始，以记录的更改结束。

<a id="the-contract"></a>

## 接口约定

调度器在预算下选择一个动作，执行它，存储观察结果，并更新边界。 断言的结果纳入是单独的转换。记录目标版本，输入研究记录、操作、输出、成本和结果状态。重试是对同一目标的新尝试；更改目标会创建新的任务版本。

<a id="trade-offs-and-failure-modes"></a>

## 权衡和故障模式

每个动作都应该有一个信息丰富的可能结果：一个可用的定理、一个被拒绝的匹配、一个局部差距或一个新的例子。失败的分支会将对照案例返回给调度程序，而不是无限期地重新启动。将基础设施的成功与数学进步分开。

<a id="build-and-test"></a>

## 构建和测试

重播三个动作：找到充分的消失准则，发现不匹配的假设，然后切换到直接阻塞。保存跟踪并标记确切的重新计划事件。

使用[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)和[工作台实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)。记录输入、预期结果、实际结果以及预期的数学原因。有关参考文献和断言边界，请参阅 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/)。

<a id="worked-design-decision-make-one-iteration-produce-a-state-change"></a>

## 设计决策实例：使一次迭代产生状态变化

从确切的未解决的待解决事项开始。选择可以解决或加剧问题的行动，检查返回的证据并更新记录。没有新的论证、来源或反例的重复建议不是富有成效的迭代。

**验收练习。** 对于每次迭代，写下之前已知的内容、到达的证据以及更改的内容。允许“仍未解决”作为诚实的结果，但需要不同的下一步行动或停止的理由。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
