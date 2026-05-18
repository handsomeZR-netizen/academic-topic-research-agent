# v2 Researcher-Grade Extensions (Markdown)

When **researcher-grade mode** is on (deep automatic; standard with trigger keyword), the assistant must append or interleave the 10 sections below into `reports/final_topic_report.md`. They sit *on top of* the 17-section skeleton in `v2_minimal_report.md` — not as replacements but as additions and structural tightenings.

Use this file as a copy-and-paste source. Each section is templated with TODO placeholders; the assistant fills them from `drafts/construct_rewrite_<latest>.md` and `drafts/venue_fit_decision.md`.

## How to Integrate with `v2_minimal_report.md`

| Researcher-grade section | Insert at |
|---|---|
| 1. Opening Thesis Box | **Before** `# 一句话概括` (very top of report) |
| 2. Headline Competition Audit | Inside `## 项目核心判断` |
| 3. Reverse Pitch | Inside `## 项目核心判断 → ### 核心问题不是` (this expands the existing stub) |
| 4. 3D Construct Operationalization | Inside `## 核心概念与研究问题` |
| 5. Archetype Table | Inside `## 核心概念与研究问题` (after operationalization) |
| 6. Neighbor Concept Differentiation Table | Inside `## 核心概念与研究问题` (after archetype) |
| 7. Venue Strategy Table | Inside `## 投稿定位` |
| 8. RQ Matrix | Replaces the simple RQ list inside `## 核心概念与研究问题` |
| 9. Alternative Outcomes Tables (per study) | Inside `## 研究问题与评价方案` |
| 10. Deployment Cost as Finding + Two Scale Tiers | Inside `## 研究问题与评价方案` (deployment subsection) |
| 11. Reviewer Attack Table | New section before `## 风险与应对` |
| 12. Demand Characteristic Audit | Brief subsection inside `## 风险与应对` |
| 13. Elevator Pitch Box | At the very end, before `## 最终总结` (or merge with it) |

## 1. Opening Thesis Box

```markdown
> **这版的核心决定：**TODO（3–6 句话，说明 *核心构念决定*，不是项目主题）。
> 真正的构念不是 TODO，而是 TODO。因此本文把 [construct] 定义为 TODO：
> [dim 1]、[dim 2]、[dim 3]。[Named levels] 只是这个空间中的常见 archetype，
> 不是真值类别、不是一维序列，也不是专家必须一致标注的类别。
```

## 2. Headline Competition Audit

```markdown
### 标题候选与抢戏审计

在落定 spine 前考虑过的核心构念：

| 候选 headline | 一句话内容 | 为什么不选作 spine |
|---|---|---|
| TODO | TODO | TODO |
| TODO | TODO | TODO |
| **[Selected]** | TODO | **入选：TODO** |

最终选 [Selected] 作为脊椎；其它候选降级为 [mechanism / operationalization / evidence] 层。
```

## 3. Reverse Pitch — "It Is Not"

```markdown
### 核心问题不是

本项目不是 TODO（misreading 1）；不是 TODO（misreading 2）；不是 TODO（misreading 3）。
它研究的是 TODO（precise object）。
```

## 4. 3D (or N-D) Construct Operationalization

```markdown
### 构念定义与操作化

> *Definition.* [Construct name] refers to the design problem of TODO.

| 维度 | 含义 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| Dim A | TODO | TODO | TODO | TODO | TODO |
| Dim B | TODO | TODO | TODO | TODO | TODO |
| Dim C | TODO | TODO | TODO | TODO | TODO |

形式化表示：
$$K_t = (A_t, B_t, C_t)$$
其中 $A_t$、$B_t$、$C_t$ 分别表示 TODO、TODO、TODO。
```

## 5. Archetype Table

```markdown
### 常见 archetype

| Archetype | Vector | 界面/系统形态 | 适用情境 |
|---|---|---|---|
| TODO | $(0, 0, 0)$ | TODO | TODO |
| TODO | $(2, 2, 2)$ | TODO | TODO |
| TODO | TODO | TODO | TODO |

注意：archetype 不是一维 ladder，也不是 ground-truth class。它是 design space 中常见落点的命名。
```

## 6. Neighbor Concept Differentiation Table

```markdown
### 与邻居概念的区分

| 邻居概念 | 它主要解释什么 | 本构念的不同点 |
|---|---|---|
| Mixed-initiative interaction | TODO | TODO |
| Abstention / reject-option | TODO | TODO |
| Appropriate reliance | TODO | TODO |
| Progressive disclosure | TODO | TODO |
| Proactive vs reactive AI | TODO | TODO |
| Model confidence | TODO | TODO |

具体差异化举例：本构念能描述 TODO（一个 specific configuration），而 [neighbor X] 不能。
```

## 7. Venue Strategy Table

```markdown
### 投稿策略

| 路线 | 主贡献写法 | 研究重心 |
|---|---|---|
| TODO (Primary) | TODO | TODO |
| TODO (Pivot) | TODO | TODO |

Pivot 触发条件：TODO（数据呈现什么模式会触发 pivot）。
```

## 8. RQ Matrix

```markdown
### 研究问题矩阵

| RQ | 研究问题 | 对应 Study | 主要 measure | 证据目标 | Fail condition |
|---|---|---|---|---|---|
| RQ1 | TODO | TODO | TODO | TODO | TODO |
| RQ2 | TODO | TODO | TODO | TODO | TODO |
| RQ3 | TODO | TODO | TODO | TODO | TODO |
| RQ4 | TODO | TODO | TODO | TODO | TODO |
| RQ5 | TODO | TODO | TODO | TODO | TODO |
```

## 9. Alternative Outcomes Tables (Study 1)

```markdown
### Study 1：形成性研究的可能发现 (Alternative Outcomes)

不写"预期发现"，写"可能推翻或重塑设计的发现"：

| 可能发现 | 它如何推翻/重塑原设计 | 设计后果 |
|---|---|---|
| TODO (strong-form "design is wrong") | TODO | TODO |
| TODO (different-population finding) | TODO | TODO |
| TODO (novice vs expert inversion) | TODO | TODO |
| TODO (cost-too-high finding) | TODO | TODO |
| TODO (≥ 5 rows for deep; ≥ 3 for standard) | TODO | TODO |
```

## 10. Deployment Cost as Finding + Two Scale Tiers

```markdown
### 部署的代价与两档规模 (Deployment Cost as Finding)

> **必须承认：**[deployment mechanism] 不是免费的。
> 每次 [unit of cost] 需要 TODO 时间 / 工作量 / 设备。
> 一节 TODO 分钟课做 TODO 次，占据约 TODO% 的课堂/工作时间。
> 这不是"无缝叠加"，而是"有意插入的诊断节奏"——本身就是研究发现。

| Trade-off | 研究意义 |
|---|---|
| TODO | TODO |
| TODO | TODO |
| TODO | TODO |

#### 两档可行规模

| 方案 | 规模 | 适合路线 |
|---|---|---|
| TODO ([primary]-强评估) | TODO | TODO |
| TODO ([pivot]-厚描) | TODO | TODO |
```

## 11. Reviewer Attack Table

```markdown
## 预期审稿人攻击与预防

| 攻击点 | 审稿人可能怎么说 | 论文里如何预防 |
|---|---|---|
| Construct = old idea renamed | TODO | 见 §[neighbor differentiation] |
| Levels not really 1D | TODO | 见 §[archetype framing] |
| Formative倒推 | TODO | 见 §[alternative outcomes] |
| Ground-truth instability | TODO | 见 §[pairwise preference + disagreement] |
| Deployment cost hidden | TODO | 见 §[cost as finding] |
| Demand characteristic | TODO | 见 §[naming audit] |
| Generalization beyond testbed | TODO | 见 §[scope statement] |
| TODO (≥ 5 rows for deep) | TODO | TODO |
```

## 12. Demand Characteristic Audit

```markdown
### 命名与提示的预埋审计

| Surface | Current wording | Embedded answer | Risk | Fix |
|---|---|---|---|---|
| System name | TODO | TODO | TODO | TODO |
| Condition labels | TODO | TODO | TODO | TODO |
| Main RQ wording | TODO | TODO | TODO | TODO |
| Interview prompts | TODO | TODO | TODO | TODO |
```

## 13. Elevator Pitch Box

```markdown
## 一段话电梯演讲

> 本项目不再把重点放在 TODO（obvious framing），而是研究一个更基础的 TODO（field）问题：
> TODO（sharpened question）。
>
> 在 TODO（real setting）, TODO（phenomenon explanation）。
> 因此 TODO（system / method） 不能 TODO（naive goal）, 而要 TODO（precise goal）。
> 我把这个问题命名为 TODO（construct）。
>
> 通过 TODO（testbed）, 我会先 TODO（Study 1）, 再 TODO（Study 2/3）, 最后 TODO（Study 4）。
> 本论文的贡献不是 TODO（naive thing）, 而是 TODO（precise contribution）。
```

## Anti-Patterns

- **Do not** copy this file directly into the report and leave TODOs visible. Every TODO must be filled from `construct_rewrite_<latest>.md` and `venue_fit_decision.md`.
- **Do not** insert all 13 sections regardless of depth. Use the depth-tier table at the top of `researcher_grade_checklist.md` to know which to include.
- **Do not** treat these as "decorative." The Headline Competition Audit and Neighbor Differentiation Table are the two elements most likely to surface real weaknesses; do not skip them to save space.
