---
title: 从零建立 Codex 数学研究工作区
permalink: /posts/2026/08/agent-system-zh/codex-research-studio/
classes: agent-system-page
full_page_reading: true
lang: zh-CN
hidden: true
sitemap: false
search: false
robots: noindex, follow
read_time: false
translation_revision: 88f5a30
translation_of: /posts/2026/08/agent-system/codex-research-studio/
tags:
- Agent System
---

[English original](/posts/2026/08/agent-system/codex-research-studio/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

*实验指令、文件结构与可执行代码保留英文原文，可直接复制；正文用中文解释其目的与验收标准。*

**项目：** 在 Codex 中设计研究工作流程，而无需首先实现智能体框架。使用说明、Markdown 记录、来源材料、实际数学工具。不需要 Python 项目。

Danus 是本系列中有用的架构参考。我们的目标是探索更丰富的研究组织，而不是断言这项工作已经优于 Danus。这需要匹配的评估。更多的角色和更多的文件并不是数学更好的证据。

学生是系统设计师。 Codex 帮助创建和操作工作区。学习成果是指定系统必须保留哪些内容、暴露其故障并相应改进设计的能力。

<a id="1-start-with-a-task-you-can-evaluate"></a>

## 1. 从可以评估的任务开始

首先使用这个基本目标：$(0,1)$ 上的每个连续实值函数都达到最大值。这是错误的：$f(x)=x$ 是一个反例。正确的系统应该诊断问题，而不是默默地用 $[0,1]$ 替换间隔。

然后使用贯穿课程的案例中的两个量词顺序。最后从您自己的领域选择一个简短的已发表证明，以及您理解的参考解决方案。在这些受控练习之后进行开放研究，其中失败更容易识别。

<a id="2-create-the-workspace-through-a-conversation"></a>

## 2. 通过对话创建工作区

在 Codex 中打开一个空课程文件夹并给出以下指令：

```text
Create a mathematical research workspace here using Markdown only.
Do not create an application or write orchestration code.

Create these files:
AGENTS.md: the working rules below.
TARGET.md: exact target, version, domain, quantifiers, and success criteria.
STATE.md: current conclusions, assumptions, and unresolved obligations.
ARGUMENTS.md: alternative arguments and their dependencies.
SOURCES.md: exact source statements, locators, and applicability checks.
REVIEWS.md: findings tied to exact statement and argument versions.
EXPERIMENTS.md: test inputs, actual outputs, and observed failures.
CHECKPOINT.md: enough information to resume in a fresh conversation.

Working rules:
Never silently weaken the target or promote an assumption to a fact.
Distinguish proposed arguments, reviewed arguments, and formal evidence.
A review applies only to the content it examined.
Record failed routes and missing bridges.
Do not invent citations, source access, or tool execution.
Before a conclusion is reused, identify its supporting argument and scope.
After a revision, identify dependent conclusions that need reconsideration.
```

检查文件。指令文件是行为规范，而不是执行机制。模型可以忽略规则。以下实验确定此特定运行是否遵循它。

<a id="3-run-one-complete-research-cycle"></a>

## 3. 运行一个完整的研究周期

```text
Investigate the target in TARGET.md.
First restate it exactly and identify the decisive uncertainty.
Choose one useful action: a proof attempt, counterexample, source check,
or clarification of a definition. Explain why it is worth doing.
Perform the action using the information and tools actually available.
Update the records with its evidence and remaining obligations.
Do not report completion unless the original success criteria are met.
```

对于最大的例子，检查反例和紧致性的失败。如果 Codex 提出更正的定理，请将其存储为不同的版本。成功修复附近的断言并不能证明原来的断言。

**提交成果：** 一个完整的完整研究过程，包括初始响应和任何更正。不要从实验记录中删除错误的第一个答案。

<a id="what-the-files-should-contain-after-the-first-cycle"></a>

### 第一个周期后文件应包含什么

这是最大示例的参考状态。它说明了实质性内容而不是所需的软件格式；它不是执行的助理会话的日志。

```text
TARGET.md
  T1-v1: every continuous f:(0,1)->R attains a maximum.
  A counterexample must satisfy continuity and show nonattainment.

ARGUMENTS.md
  A1 addresses T1-v1 using f(x)=x.
  This function is continuous on (0,1).
  For any proposed maximizer x, let y=(x+1)/2.
  Then x<y<1, and f(y)>f(x). Thus no maximizer exists.

REVIEWS.md
  Review A1 against T1-v1.
  Check continuity, membership of y in the domain, and strict inequality.
  If accepted, its scope is refutation of T1-v1 by this counterexample.

STATE.md
  T1-v1 is refuted by A1.
  T1-v2, with domain [0,1], is a separate proposed repair.
  A1 does not refute T1-v2: the endpoint 1 changes the argument.
```

不等式 $x<(x+1)/2<1$ 由 $x<1$ 得出。在闭区间的端点 $x=1$ 处，相同的构造给出 $y=1$，因此严格改进失败。这准确地解释了为什么反例证明没有转移到修复域。

在继续之前，请要求 Codex 从其文件中重建这些区别。如果 `STATE.md` 只说“最大定理已解决”，那么记录是不够的：它没有说明哪个版本被驳斥以及哪个版本被提议作为修复。修复此时的记录，而不是添加更多编排。

<a id="4-add-alternative-routes-without-multiplying-agents"></a>

## 4. 添加替代路线而不乘以智能体

要求两条真正不同的到达目标的路线，每条都列出共同前提、预期证据及其最弱的衔接论证。一次谈话就足以开始。

```text
Create two candidate routes for the same target version.
For each route, list the premises needed together and the return argument
to the original target. Identify what would invalidate this route.
Choose the next action under a budget of three research actions.
Preserve the other route rather than merging incompatible assumptions.
```

使用量词示例作为负对照案例：求解每个单独的界不会建立一致界。复杂的计划仍然必须揭露失败的蕴涵。 [动手实验](/posts/2026/08/agent-system-zh/hands-on-lab/)提供了额外的对照案例。

<a id="5-separate-review-from-advocacy"></a>

## 5. 将审查与宣传分开

与确切目标开始另一次对话，提出论证和来源摘录。提供完整的证据，但省略事先批准的有说服力的摘要。

```text
Review this exact argument version. Identify each inference and check
its premises. Distinguish an error, a missing justification, and a question.
Do not repair the target silently. Return a report with precise locations,
remaining assumptions, and the scope of any conclusion you accept.
```

新鲜的对话可以减少一些情境影响。它不保证独立推理或数学正确性。将报告与实际证据进行比较。对于形式化组件，使用[Lean实验室](/posts/2026/08/agent-system-zh/lean-formalization/)并保留实际执行输出。没有执行工具的聊天框可以讨论证明，但无法提供成功的工具运行。

<a id="6-test-revisions-and-recovery"></a>

## 6. 测试修改和恢复

对假设或数学对象进行受控更改。保留两个版本。要求 Codex 确定哪些论证和审查记录需要重新考虑。根据依赖性记录自行检查其列表。

接下来规定两条独立的配套路线，撤一条，然后两条。如果其他路线仍然适用，则在第一次撤回后，目标应继续受到支持。两次退出后，问题就变得悬而未决，不会自动成为错误。

最后请求一个checkpoint：

```text
Write CHECKPOINT.md for a new conversation with no access to this chat.
Include the exact target version, established and assumed premises,
surviving arguments, rejected routes, evidence locations, open obligations,
and the next action. Do not summarize away conditional assumptions.
```

使用保存的文件开始新的对话。要求它在进行新研究之前重建状态。与 checkpoint 进行重建比较。文件持久化很有用；忠实恢复是要测试的观察行为。

<a id="7-make-the-design-more-sophisticated-only-where-it-helps"></a>

## 7. 仅在有帮助的地方使设计更加复杂

| 扩展 | 数学目的 | 可以证明其合理性的实验 |
|---|---|---|
| 适用性矩阵 | 防止相关定理在其假设之外应用 | 有效的应用程序和被拒绝的近似匹配 |
| 替代论证图 | 当一个论证失败时保留有用的路由 |撤回一条路线，然后撤回一条共享前提 |
| 转换接口约定 | 使蕴涵回到可见的原始问题 | 将界与一致界 |
| 版本化审查 | 防止审批偏离已更改的数学 | 更改目标后交付旧的审查 |
| 形式化证据记录 | 区分编码证明检查和非形式化置信度 | 有效 Lean 证明、类型错误、占位符、额外公理|
| 恢复 checkpoint | 恢复而不丢失范围或打开待解决事项 | 在新对话中重建状态 |

这些是对您的工作流程的候选改进，而不是 Danus 缺乏列出的所有功能的断言。使用其案例研究提出架构问题，并在进行功能比较之前检查实际实现。

只有当目的明确时才添加分工。 来源检查和替代证明尝试可能是合适的单独任务。给每个人相同的目标版本；保留分歧；拒绝过期报告。与单个对话进行比较时，保持可比较的总工作量预算。

<a id="8-evaluate-the-resulting-system"></a>

## 8. 评估生成的系统

将普通聊天提示与相同有效证明和损坏变体上的结构化工作区进行比较。记录来源访问、日期、可见模型设置、时间、交互、接受的错误、拒绝的有效步骤和有用的部分结果。保留完整的输出，以便其他读者可以评估比较。

不要从一个有吸引力的例子中获得断言的优越性。如果与 Danus 进行比较，请在可比资源下对相同任务运行指定版本，记录其配置并报告双方的故障。如果没有这种比较，请将您的结果描述为建议的设计和经过测试的 Codex 工作流程。

**最终提交：**工作区文件、完整的研究轨迹、评估案例、基线结果、一次故障分析以及关于保留哪些机制的合理决定。

持久的技能是设计数学研究过程并测试其要求是否真正得到满足。 Codex是练习环境。学生无需编写智能体框架即可学习此技能；如果实验暴露了指令无法可靠执行的要求，请识别该限制并决定是否需要现有工具或额外的实施。

[课程路线图](/posts/2026/12/Agent-System-zh/) · [Danus 和 Rethlas 案例研究](/posts/2026/08/agent-system-zh/math-research-case-study/)
