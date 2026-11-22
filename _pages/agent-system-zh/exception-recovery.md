---
title: 异常处理与研究状态恢复
permalink: /posts/2026/08/agent-system-zh/exception-recovery/
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
translation_of: /posts/2026/08/agent-system/exception-recovery/
---

[English original](/posts/2026/08/agent-system/exception-recovery/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/memory-management/)。下面的几何参考是案例 的可选扩展。

超时、不可访问的来源、格式错误的记录和非零连接类需要不同的响应。只有最后一个可以证明指定 section 不是提升，并且只有数学证据。

<a id="the-contract"></a>

## 接口约定

重试之前先进行分类。 界瞬时重试，修复格式错误的输入，在适当的情况下寻找另一个来源，并在数学上路由失败时重新规划。在确认工作之前，保存在研究记录边界处完成的观测。

<a id="trade-offs-and-failure-modes"></a>

## 权衡和故障模式

重新启动的执行单元应使用相同版本的输入或创建新的尝试。它不得合并来自不同层或 section 的片段。失败的方法会使目标保持打开状态，除非其失败实际上证明目标是错误的。

<a id="build-and-test"></a>

## 构建和测试

注入超时、过期审查和非零阻塞。写出三项恢复记录并证明哪一项（如果有的话）支持数学结论。

使用[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)和[工作台实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)。记录输入、预期结果、实际结果以及预期的数学原因。有关参考文献和断言边界，请参阅 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/)。

<a id="worked-design-decision-recover-without-manufacturing-evidence"></a>

## 有效设计决策：无需制造证据即可恢复

如果来源下载失败，则状态为“来源无法访问”，而不是“定理为假”。保留请求的来源、失败的操作和未完成的数学待解决事项。访问返回后从最后支持的状态恢复。

**接受练习。** 在保存建议的证明之后但在审查之前中断运行。重新启动时，提案必须保持未经审查的状态。检查重复操作是否不会创建两个独立的证据。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
