---
title: 人在研究系统中的职责
permalink: /posts/2026/08/agent-system-zh/human-in-the-loop/
tags:
- Agent System
classes: agent-system-page
full_page_reading: true
lang: zh-CN
read_time: false
translation_revision: 88f5a30
translation_of: /posts/2026/08/agent-system/human-in-the-loop/
---

[English original](/posts/2026/08/agent-system/human-in-the-loop/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/design-principles/)。下面的几何参考是案例 的可选扩展。

数学研究系统需要明确的政策来改变其目标、支出预算、接受证据和发布结果。这些责任并不意味着人类必须批准每项行动。

<a id="control-is-an-interface"></a>

## Control 是接口

常规检索、来源检查、有界修改可在授权下进行。当某项行动会改变商定的目标或超出该权限时升级。模型可以提出决策；该策略决定了谁可以授权它。

例如，将紧致 Kähler 假设替换为射影性可能会使路线有效。系统应保留原来的任务，创建一个单独的强化命题，并解释已经实现和尚未实现的内容。它不应该仅仅因为证明尝试失败而中断。

<a id="what-a-decision-packet-contains"></a>

## 决策包包含什么内容

提出最初的目标、提议的改变、数学原因、支持证据、替代方案以及可以独立继续的工作。记录决定及其范围。批准进一步的探索并不意味着批准定理的正确性。

人类也可能会错过错误。签名不能代替证据接口约定。相反，能力越来越强的智能体可能会执行更多的设计和审查工作；仍然需要明确的目标、证据和权威。

<a id="hands-on-practice"></a>

## 动手实践

为 [introduction](/posts/2026/08/agent-system-zh/design-principles/) 中的开区间示例编写决策数据包。提供两个不同的任务：完成对原始猜想的反驳，或者研究修复的紧致域定理。表明第一个任务可以完成，而无需等待第二个任务的偏好。测试两次恢复相同的决策不会重复工作。

<a id="reference-basis"></a>

## 参考依据

Gulli，* 代理设计模式*，第 13 章，将人类参与视为一种模式。 本页面专门介绍接口的数学范围变化和委托研究。 这里并未声称某种认知任务将永远只能由人完成。

<a id="worked-design-decision-locate-responsibility-without-predicting-permanent-limitations"></a>

## 可行的设计决策：定位责任而不预测永久限制

研究人员选择哪个问题重要、什么证据证明进一步投资是合理的以及要发布什么断言。这些都是研究过程的责任，即使能力越来越强的模型可以协助每一个决策。不要将架构建立在特定任务将始终抵制自动化的预测之上。

**验收练习。** 在决策点，提出确切的选项、支持证据、成本和未解决的待解决事项。要求进行实质性的研究选择，而不是对每个可逆步骤进行例行确认。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
