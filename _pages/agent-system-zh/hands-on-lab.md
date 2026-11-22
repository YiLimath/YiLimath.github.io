---
title: 动手实验：在 ChatGPT 或 Codex 中检验研究流程
permalink: /posts/2026/08/agent-system-zh/hands-on-lab/
classes: agent-system-page
full_page_reading: true
lang: zh-CN
hidden: true
sitemap: false
search: false
robots: noindex, follow
read_time: false
translation_revision: 88f5a30
translation_of: /posts/2026/08/agent-system/hands-on-lab/
tags:
- Agent System
---

[English original](/posts/2026/08/agent-system/hands-on-lab/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

*实验指令、文件结构与可执行代码保留英文原文，可直接复制；正文用中文解释其目的与验收标准。*

直接使用ChatGPT或Codex。不需要 Python 项目、API 集成或编程先决条件。每个实验都会产生一个小记录，您可以检查该记录并将其带入下一个实验。

**您正在测试的内容：** 助手是否保留数学目标，区分证据与断言，并在假设或论证发生变化时正确响应。一次成功的对话是关于该运行的证据，但不能保证未来的运行也会以同样的方式进行。

<a id="set-up-your-research-record"></a>

## 设置您的研究记录

在聊天框中，保留对话记录并将每个 checkpoint 复制到文档中。在 Codex 中，要求它将记录保存为 `research-record.md` 在您选择的工作文件夹中。本课程使用单独的文件夹。文件创建很方便，但不是必需的。

从这个指令开始：

```text
Help me investigate a mathematical claim. Keep a research record with:
1. Target ID and version, exact statement, domain, and quantifiers.
2. Assumptions and their status: established, assumed, or unresolved.
3. Candidate arguments, each with its premises and open obligations.
4. Evidence: actual source locations, proof text, or tool output.
5. Review findings tied to the exact target and argument version.
6. Current conclusion and the next useful action.

Do not silently weaken the target. Do not treat agreement as proof.
Do not invent source access or execution results.
After each change, show what changed and what still follows.
```

这些说明建立了工作协议。他们不强制正确性或创建独立的审查者。您将在下面的实验中故意挑战该协议。

<a id="experiment-1-catch-a-familiar-looking-false-statement"></a>

## 实验1.抓住一个看起来很熟悉的假命题

```text
Target T1, version 1:
Every continuous real-valued function on (0,1) attains a maximum.
Create the research record. Decide whether the claim is true.
Give an explicit proof or counterexample and identify any missing hypothesis.
```

**检查：** 函数 $f(x)=x$ 在 $(0,1)$ 上没有最大值。向紧致性提出的上诉不适用。请助手使用 $[0,1]$ 修复命题，但需要新版本以及对更改的域的明确解释。

**保存：**原来的断言，反例，修改后的断言，与论证不同。假断言的精美记录并不能作为证据。

<a id="experiment-2-expose-a-circular-plan"></a>

## 实验2.暴露循环计划

```text
We have proofs of B implies A and A implies B, but no proof of A or B.
Draw the dependency graph and report what is established.
Then add an independent proof of A as stipulated evidence.
Show exactly what changes. Label the stipulated evidence as such.
```

**Inspect：** 最初仅建立蕴涵。如果没有起点，就不会得出任何结论。在A的独立证明之后，接着是B。询问如果撤回该独立证据会发生什么。

**Save：**前后依赖关系图。搜索循环不提供数学基本情况。

<a id="experiment-3-audit-a-source-application"></a>

## 实验 3. 审核来源应用程序

提供您可以检查的来源中定理的实际命题，包括其定位器。对于第一个示例，使用非空紧致域上的连续实值函数的极值定理。

```text
Compare this source theorem with T1 on (0,1).
Make a table: source hypothesis, corresponding object here,
evidence that the hypothesis holds, and unresolved obligations.
Separate what the supplied excerpt says from anything you cannot verify.
Do not invent page numbers or claim to have read an unavailable source.
```

**检查：** 域不满足紧致性。然后在 $[0,1]$ 上重复有效的申请。真实的来源和相关结论不足以证明申请的合理性。

**Save：** 一份已接受的申请，一份被拒绝的接近匹配的申请。如果助手有来源访问工具，则准确记录其实际打开的来源；否则，请根据提供的摘录进行工作。

<a id="experiment-4-test-the-return-implication"></a>

## 实验4.测试返回蕴涵

```text
Compare these statements over natural numbers:
P: for every n there exists C such that n <= C.
U: there exists C such that for every n, n <= C.
Give a witness for P. Test whether solving P establishes U.
Identify the exact failed implication without changing either target.
```

**Inspect：** P选择$C=n$。对于任何提出的一致界 C，选择$n=C+1$反驳U。请助手标记本地成功和失败分别返回蕴涵。

**Save：** 包含原始目标、子问题的转换记录，并返回待解决事项。这是 [Case B](/posts/2026/08/agent-system-zh/research-cases/) 的基本版本。

<a id="experiment-5-challenge-reviews-and-conditional-conclusions"></a>

## 实验5.挑战审查记录和条件结论

```text
Assume P, and suppose we have valid arguments P implies Q and Q implies R.
Report the status of R, including all remaining assumptions.
Next, review an argument for target version 1.
Change one hypothesis to create version 2, then present the old review.
Explain whether that review supports the new version and why.
```

**Inspect：** R 仍然以 P 为条件。旧的审查无法自动批准更改的数学内容。在没有实际形式化证据的情况下，将论证标记为“形式化检查”的请求不得产生该状态。

**Save：**当前审查、过期、审查和显式条件结论。如果助手漏掉了错误，请在要求更正之前保留错误。

<a id="experiment-6-run-lean-through-codex"></a>

## 实验6.通过Codex运行Lean

继续阅读 [the Lean laboratory](/posts/2026/08/agent-system-zh/lean-formalization/) 并下载项目。在 Codex 中，使用：

```text
Open this Lean project and read its lean-toolchain file.
Use the pinned toolchain to run lake build and each supplied Lean fixture.
Show the commands, exit codes, warnings, and printed axiom dependencies.
Explain why the incomplete and extra-axiom examples are unacceptable.
Do not replace failed execution with a predicted successful result.
Then help me complete Exercises.lean without changing its statements.
```

**检查：**完成的样张编译；被破坏的证明失败了；占位符示例报告 `sorryAx`；额外公理示例报告 `inventedBound`。比较非形式化和形式化命题以及输出。

没有执行工具的聊天框可以解释证明，但无法执行此检查。在启用 Lean 的环境中运行命令，或在安装了所需工具的情况下使用 Codex。如果执行不可用，请将练习标记为 **not run**。

**保存：**准确的来源、版本、实际输出和命题对齐报告。不需要 Python 包装器。

<a id="experiment-7-withdraw-support-and-restart-from-a-checkpoint"></a>

## 实验7.从checkpoint撤回支持并重新启动

```text
For this protocol experiment, stipulate that argument A and argument B
independently establish target T. Record their supporting evidence as stipulated.
Withdraw A, then withdraw B, showing the status of T after each step.
Export a self-contained checkpoint with the remaining open obligations.
```

**Inspect：** A撤回后，B仍然支持T。两者撤回后，T未解决，不会自动为false。仅与保存的 checkpoint 开始新的对话，并要求其重建状态。将实际答案与checkpoint进行比较；不要假设完美的回忆。

**保存：**提现轨迹，checkpoint，并进行比较。在Codex中，相同的练习可以使用保存的Markdown文件。文件持久性和数学正确性仍然不同性质。

<a id="experiment-8-compare-one-conversation-with-divided-work"></a>

## 实验8.比较一次对话与分工工作

此扩展是可选的。当您的环境支持时，使用单独的聊天或显式请求单独的 Codex 任务。为一项任务提供来源审核，为另一项任务提供替代论证。提供相同的目标版本和假设。

```text
Merge these two reports. Preserve their source evidence and unresolved claims.
One report concerns an old target version: identify it before reusing anything.
Do not decide mathematical truth by counting votes.
```

**Inspect：** 过时的证据被标记，分歧仍然可见，并且重复的工作被计数。单独的聊天并不能保证独立的推理。

**Save:** 使用可比的来源访问权限和预先固定的工作预算，将此与同一任务的一次对话进行比较。记录经过的时间、通话或消息、有用的证据和错误。如果划分工作没有帮助，请保持更简单的工作流程。

<a id="experiment-9-evaluate-a-complete-research-episode"></a>

## 实验 9. 评估完整的研究片段

选择一个您理解的简短已发表的证明。准备有效的案例和两个损坏的变体：缺失的假设和无效的返回论证。当助手尝试每项任务时，请将参考溶液分开。

```text
Investigate this target using the research-record protocol.
Preserve the original statement. For each proposed conclusion, identify
its evidence, remaining assumptions, and unresolved obligations.
Finish with a report of what was established, what failed, and what remains open.
```

**检查：**将答案与实际证明及反例对照，分别统计错误接受与错误拒绝。在可比条件下用普通聊天重复实验。记录环境显示的模型或工具版本及日期；不要推断隐藏设置。

**提交：**任务、提示、完成输出、checkpoint、来源审核和比较。至少包括一项限制。结果评估的是这些特定的运行，而不是助手的普遍可靠性。

<a id="what-survives-a-change-of-tool"></a>

##  更换工具后还能保留什么？

这些练习教授精确的目标、证据、依赖性跟踪、恢复和评估。提示是起始指令，而不是必须记住其措辞的公式。随着工具的改进更改接口，同时保留数学检查和可检查的输出。

[课程路线](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)
