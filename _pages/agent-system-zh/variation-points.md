---
title: 可替换的实现与稳定的研究约定
permalink: /posts/2026/08/agent-system-zh/variation-points/
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
translation_of: /posts/2026/08/agent-system/variation-points/
---

[English original](/posts/2026/08/agent-system/variation-points/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/lean-formalization/)。下面的几何参考是案例 的可选扩展。

更强的模型可能会取代多个执行单元或发现更短的证明。它仍然必须确定证明了什么、从哪些前提、在哪些假设下进行的。这些是稳定的接口约定；模型选择和提示是其背后的机制。

对于定理检索，接口约定是来源定位器、命题、假设和建议的对象替换。对于审查，它包括确切的论证版本和证据类型。兼容性是语义上的，而不仅仅是匹配的响应形状。

<a id="find-a-real-axis-of-change"></a>

## 找到真正的变化轴

指定一个可行的替代方案，并询问呼叫者仍然可以依赖什么。将方法排名与假设匹配分开；将候选生成与前提权限分开；将存储标识与显示名称分开。

不要创建隐藏调用者所需区别的抽象。返回布尔值的通用 `verify()` 隐藏了解析、测试、来源匹配和内核检查。 审查信封应注明支票及其限额。

<a id="substitution-has-conditions"></a>

## 替换有条件

形式化检查器、模型评论家和人类读者可以共享接口，而无需在每个策略下互换。将一种替代另一种可能需要更改其输出的允许用途。记录政策变化，而不是将所有输出称为“已验证”。

<a id="build-and-test"></a>

## 构建和测试

将执行单元替换为脚本化响应，并保留相同的版本和结果纳入检查。然后将证据策略更改为形式化-only。 非形式化报告不得以已纳入作为形式化证据；共享的 schema 不得升级其保证。

与[一起阅读三个贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)。 来源的出处以及既定模式与我们提出的专业化之间的区别在 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/) 中进行了解释。

<a id="worked-design-decision-replace-a-model-while-preserving-the-research-contract"></a>

## 设计决策实例：在保留研究的同时替换模型接口约定

新模型可以更快地生成候选答案，而无需改变可接受的前提。在相同任务上测试替换时，保持目标格式、证据要求和审查范围稳定。仅通过显式重新设计来更改这些接口约定。

**验收练习。** 比较同等条件下的实际输出并揭示不同的工具访问权限。更好的散文或更快的完成本身并不能显示证明可靠性的提高。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
