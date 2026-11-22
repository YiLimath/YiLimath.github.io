---
title: 结构化输出：格式之外的语义检查
permalink: /posts/2026/08/agent-system-zh/structured-output/
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
translation_of: /posts/2026/08/agent-system/structured-output/
---

[English original](/posts/2026/08/agent-system/structured-output/) · [中文课程总览](/posts/2026/12/Agent-System-zh/)

**模式参考。** 这是一个简短的设计说明，不是一个独立的课程。对于完整推导的论证的逐步练习和评估，请阅读 [ 完整课程章节 ](/posts/2026/08/agent-system-zh/foundations/)。下面的几何参考是案例 的可选扩展。

包含 `claim` 和 `confidence` 的记录是结构化的，但数学上很弱。有用的类型可区分命题与其论证、假设与合理前提以及证据类别与工作流程状态。

案例 需要指定 section 和精确的限制映射。情况 B 需要量词顺序并允许常量依赖性。案例 C 需要索引命题、基本案例和 rank。通用摘要字段隐藏了所有这三个字段。

<a id="four-checks-four-meanings"></a>

## 四项检查，四项含义

解析检查必填字段。引用验证检查链接对象是否存在并与其版本匹配。策略验证检查可用证据是否允许使用。数学审查检查推理是否合理。分别返回这些失败。

在当前 Markdown 实验室中，为每个审查保留确切的命题和论证版本。单独的实现可以添加内容哈希来检测文本更改，但本课程不提供自动哈希门。标签和散列都不能保证数学的正确性。

<a id="replace-components-without-erasing-evidence"></a>

## 更换组件而不擦除证据

依赖项注入通过稳定的接口提供来源适配器或审查者。当实现发生变化时它很有用。但是，非形式化审查不能满足需要形式化证书的策略，仅仅因为两者都符合相同的 JSON schema。

<a id="build-and-test"></a>

## 构建和测试

创建一个有效的记录来交换情况 B 中的量词。解析应该会成功。解释捕获错误所需的单独语义待解决事项。然后询问哪些结果满足非形式化-审查政策，哪些结果满足需要实际 Lean 证据的政策。缺少形式化执行必须保持显式。

与[一起阅读三个贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)。 来源的出处以及既定模式与我们提出的专业化之间的区别在 [ 来源和声明 ](/posts/2026/08/agent-system-zh/sources-and-claims/) 中进行了解释。

<a id="worked-design-decision-validate-meaning-after-validating-fields"></a>

## 设计决策实例：验证字段后验证含义

一条记录可以包含每个必填字段，并且仍然可以包含断言，即开区间为紧致。结构验证检查存在性和格式；数学审查检查论证和适用性。将它们存储为单独的结果。

**验收练习。** 创建一项格式错误但数学上正确的记录和一项格式良好但错误的记录。一个有用的系统可以区分它们并请求适当的修复，而不是分配一个通用的置信度分数。

---

[系列指南](/posts/2026/12/Agent-System-zh/)·[贯穿课程的案例](/posts/2026/08/agent-system-zh/research-cases/)·[实验室](/posts/2026/08/agent-system-zh/hands-on-lab/)
