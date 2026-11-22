---
title: 解释工具结果的数学意义
permalink: /posts/2026/08/agent-system-zh/tool-use/
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
translation_of: /posts/2026/08/agent-system/tool-use/
---

[English original](/posts/2026/08/agent-system/tool-use/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。**这是简短的设计说明，完整论证、实践和考核见 [Lean 与证据模块](/posts/2026/08/agent-system-zh/lean-formalization/)。几何例子对应案例 A 的可选扩展。

**核心观点：**通过有明确输入、输出类型的接口调用能力，获取真实 observation，使产生的外部影响可授权、可检查，而不只是由模型声称发生过。

## 要解决的问题

确定性的操作、外部状态与精确计算，不能仅靠生成语言完成。agent 需要受控的执行方式，以及可以检查的返回结果。

## 接口结构

`agent → tool schema → capability → observation → agent`

Function calling、MCP、HTTP services、databases、code runners 和 proof assistants 都可实现这条边界。长期需要保留的是：工具名、input schema、权限、return schema，以及失败时的行为。

## 执行代码意味着什么

精确算术、符号实验、有限搜索、绘图与 formal proof checking 可以交给代码。保留程序、运行环境和实际输出，使过程可检查。执行成功是关于这次计算的证据，并不自动证明外围定理。

采用最小权限，检查输入，控制外部影响，设置超时，并在可行时使写入 idempotent。区分工具错误与负面的数学结果；observation 必须经过解释，才能改变研究状态。

## 具体例子

定理检索应返回实际检查过的段落与 locator。Lean 检查应返回精确 declaration、环境与 checker 的实际输出。若讨论某个具名系统的能力，应先确认它的具体版本。

记录精确输入、arithmetic mode、软件版本，以及数学对象如何转换成代码。这使 observation 绑定到实际计算的问题，而不是相似的另一个问题。

### 动手练习

比较对 f(x)=x 的 floating-point sampling 与精确 witness 论证，说明各自确立了什么。保存输入、中间记录、预期与实际输出，并加入一个必须拒绝的负面对照。从[研究记录实验](/posts/2026/08/agent-system-zh/hands-on-lab/)开始，但不要把 bookkeeping checks 当成 proof checker。

## 参考依据

工具使用见 Gulli 的 [*Agentic Design Patterns*](https://link.springer.com/book/10.1007/978-3-032-01402-3) 第 5 章，以及 Lakshmanan 与 Hapke 的 [*Generative AI Design Patterns*](https://www.oreilly.com/library/view/generative-ai-design/9798341622654/) Patterns 21、22。[ReAct](https://arxiv.org/abs/2210.03629) 展示 reasoning/action 接口，[MCP specification](https://modelcontextprotocol.io/specification) 描述外部数据和工具的标准化访问。

Function calling 及其并行形式的实践讨论见 James Phoenix、Mike Taylor 的 *Prompt Engineering for Generative AI*（O'Reilly，2024）第 4 章。把工具与指令组织成按需加载的具名能力，见 Stephen Clear 的 *Claude AI Bible* 第 14、16 章。

## 设计决策实例：复用工具输出前先解释它

符号计算返回零，可能依赖 simplification rules、隐含假设或受限定义域。保留精确表达式、假设、命令和输出，再说明它为什么支持当前推理。

**验收练习：**输入一个超出声明假设的相近案例。即使工具仍然给出输出，解释层也应阻止无依据的结论。数值吻合可以支持继续调查，不能充当一般证明。

[课程总览](/posts/2026/12/Agent-System-zh/) · [贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)
