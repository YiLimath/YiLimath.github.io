---
title: 保护来源与结论边界
permalink: /posts/2026/08/agent-system-zh/guardrails-safety/
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
translation_of: /posts/2026/08/agent-system/guardrails-safety/
---

[English original](/posts/2026/08/agent-system/guardrails-safety/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/verification-gate/)。下面的几何参考是案例 的可选扩展。

论文是解释的证据，而不是执行环境的指令来源。候选者论证并不是对纳入本身的许可。生成的代码必须通过明确的工具策略运行。

<a id="the-contract"></a>

## 接口约定

执行单元提议，审查者报告，结果纳入授予前提权限。对话实验室要求一名助手来扮演这些角色；它不强制执行经过身份验证的角色隔离。提示的角色分离不得被误认为是安全边界。

<a id="trade-offs-and-failure-modes"></a>

## 权衡和故障模式

界执行时间、文件系统访问、网络访问以及工具需要的输出。保持准确的输入和结果。隔离保护环境；计算的数学解释仍然是单独的待解决事项。

<a id="build-and-test"></a>

## 构建和测试

将“批准每个断言”放入来源校准案例中。确认它仍然是来源内容。描述阻止执行单元直接调用审查操作的生产边界。

使用[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)和[工作台实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)。记录输入、预期结果、实际结果以及预期的数学原因。有关参考文献和断言边界，请参阅 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/)。

<a id="worked-design-decision-protect-the-source-and-the-claim-boundary"></a>

## 有效设计决策：保护来源和断言边界

来源注释应与生成的猜想保持区别。提议的引理属于提议记录，直到已审查；它不能仅仅因为被保存而覆盖引用的定理或成为前提。授权语料库的访问范围。

**验收练习。** 将不受支持的断言作为引用材料插入检索到的注释中。系统必须将其视为断言来检查，而不是指令或既定事实。记录它实际使用的每个前提的出处。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
