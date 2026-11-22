---
title: 分阶段推理与证据衔接
permalink: /posts/2026/08/agent-system-zh/prompt-chaining/
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
translation_of: /posts/2026/08/agent-system/prompt-chaining/
---

[English original](/posts/2026/08/agent-system/prompt-chaining/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/knowledge-retrieval/)。下面的几何参考是案例 的可选扩展。

定理应用有自然的阶段：检索、转录、实例化、检查假设并得出所需的结论。在情况A中，关于附近的层的结果不是关于提升序列所需的组的结果。

<a id="the-contract"></a>

## 接口约定

每个阶段都会消耗版本化的研究记录并返回其承诺的研究记录或障碍。将来源命题保留在提取旁边。匹配阶段必须提供积极证据或将其保留为开放状态；演示阶段无法消除该条件。

<a id="trade-offs-and-failure-modes"></a>

## 权衡和故障模式

链接可以定位错误，但会放大早期的转录错误。审核最薄弱的边界。当阶段需要修改时，明确地表示反馈，而不是强制采用单向管道。链是数学接口的实现，而不是将每个任务划分为更多提示的理由。

<a id="build-and-test"></a>

## 构建和测试

构造来源命题、假设矩阵和条件提升论证。让积极性悬而未决，并确认没有任何阶段默默地将其提升为前提。

使用[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)和[工作台实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)。记录输入、预期结果、实际结果以及预期的数学原因。有关参考文献和断言边界，请参阅 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/)。

<a id="worked-design-decision-preserve-the-boundary-between-extraction-and-application"></a>

## 可行的设计决策：保留提取和应用之间的边界

第一步提取定理；第二个替换当前对象；第三个检查假设。如果提取忽略了紧致性，则后续的流畅推理无法可靠地恢复丢失的假设。将来源通道保留在提取的命题旁边。

**接受练习。** 故意从提取的记录中删除一个假设。申请步骤应通过返回来源来检测差异，而不是批准缩短的命题，因为它来自早期阶段。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
