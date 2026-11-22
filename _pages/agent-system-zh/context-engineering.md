---
title: 围绕下一步推理组织上下文
permalink: /posts/2026/08/agent-system-zh/context-engineering/
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
translation_of: /posts/2026/08/agent-system/context-engineering/
---

[English original](/posts/2026/08/agent-system/context-engineering/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/memory-management/)。下面的几何参考是案例 的可选扩展。

即使是巨大的上下文窗口也需要区分当前假设、拒绝的尝试、来源、命题和对照案例指令。较长的文字记录并不会自动提供这种区别。

<a id="the-contract"></a>

## 接口约定

对于情况 A，为执行单元提供准确的层、divisor、section 和开放obstruction。对于情况 B，保留参数依赖性和拓扑。仅当完整的研究记录仍然可检索并且范围经受住压缩时，摘要才可以省略详细信息。

<a id="trade-offs-and-failure-modes"></a>

## 权衡和故障模式

通过重建假设和依赖列表来评估压缩，而不是通过风格相似性。保持论证对其审查者可用。冷漠的背景应该消除事先批准的锚定，而不是消除检查数学所需的证据。

<a id="build-and-test"></a>

## 构建和测试

将案例 B 估计压缩为五行，然后重建其依赖关系。如果索引相关常量变为一致，则练习失败。

使用[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)和[工作台实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)。记录输入、预期结果、实际结果以及预期的数学原因。有关参考文献和断言边界，请参阅 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/)。

<a id="worked-design-decision-choose-context-by-the-next-inference"></a>

## 设计决策实例：通过下一个推理选择上下文

对于定理应用，优先考虑目标、相关定义、精确定理和不匹配的假设。关于相关几何的长篇大论可能会排除决定适用性的一个条件。在工作摘要之外保留完整的来源。

**接受练习。** 删除背景散文，同时保留决定性假设；然后删除该假设。只有第二个更改才能阻止合理的应用。使用这种对比来评估上下文选择是否对证据敏感。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
