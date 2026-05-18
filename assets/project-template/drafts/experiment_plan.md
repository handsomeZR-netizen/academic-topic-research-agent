# 评价与实验计划

## Research Questions

> Researcher-grade 模式：以 RQ Matrix（行=RQ，列=Study/Measure/Evidence Target/Fail Condition）替代下面的扁平列表。见 `drafts/construct_rewrite_<latest>.md` 第 4 节，或直接复制到这里。

- RQ1: TODO
- RQ2: TODO
- RQ3: TODO
- RQ4: TODO

### RQ Matrix (researcher-grade)

| RQ | 研究问题 | 对应 Study | 主要 measure | 证据目标 | Fail condition |
|---|---|---|---|---|---|
| RQ1 | TODO | TODO | TODO | TODO | TODO |
| RQ2 | TODO | TODO | TODO | TODO | TODO |
| RQ3 | TODO | TODO | TODO | TODO | TODO |
| RQ4 | TODO | TODO | TODO | TODO | TODO |

## Study Overview

| Study | Goal | Method | Participants / Data | Output |
|---|---|---|---|---|
| Study 1 | TODO | Formative inquiry / observation / data audit | TODO | TODO |
| Study 2 | TODO | Technical evaluation / expert preference / benchmark | TODO | TODO |
| Study 3 | TODO | Vignette study / user study | TODO | TODO |
| Study 4 | TODO | Deployment / field study | TODO | TODO |

## Study 1: Formative Inquiry — Alternative Outcomes Design

> **关键：不写"预期发现"。写"可能推翻或重塑设计的发现"。** 见 `references/construct_critique.md` 第 4 角。

Study 1 的目的：

TODO（一句话，研究教师/用户当前如何处理这类决策；inquiry 不是 performance）。

样本与数据来源：

TODO（人数、抽样标准、招募渠道、是否需要 IRB、数据形式）。

### Alternative Outcomes Table

| 可能发现 | 它如何推翻/重塑原设计 | 设计后果 |
|---|---|---|
| TODO (strong-form opposite of design assumption) | TODO | TODO |
| TODO (different-population finding) | TODO | TODO |
| TODO (novice vs expert inversion) | TODO | TODO |
| TODO (cost-too-high finding) | TODO | TODO |
| TODO (≥ 5 rows for deep, ≥ 3 for standard) | TODO | TODO |

至少一行必须是 **设计可能完全错** 的版本（最强的"我们想错了"假设）。如果不能写出这一行，formative study 仍然是 performance。

### 访谈/观察提纲原则

- 先问实际行动（"你上次遇到 X 情境时怎么做的"），再问对 AI 的偏好。
- 避免 leading wording（不要问"你需要 AI 帮你吗"）。
- 检查每个提纲题是否预埋了答案（demand characteristic 角度 7）。

## Study 2: Evaluation — Ground-Truth Stability Decision

> 在动手设计评估前，先决定 ground truth 是否稳定。见 `references/construct_critique.md` 第 5 角。

### Decision

| 问题 | 答案 |
|---|---|
| 评估是否依赖专家对类别标签达成一致？ | TODO（Yes / No） |
| 构念本身是否意味着答案上下文依赖？ | TODO（Yes / No） |

If both Yes → 使用 **pairwise preference** 作为主指标。如果第一个 No → classification accuracy 可以作主指标。如果第二个 No 但第一个 Yes → 重新审视构念是否被低估。

### Primary Metric

TODO：选定的主指标（pairwise preference w/ Bradley-Terry / classification macro-F1 / Likert 评分 / ...）

### Secondary Technical Metrics

TODO：accuracy / kappa / latency / cost 等次要指标（即使主指标是偏好，仍可保留 accuracy 作为技术报告）。

### Disagreement Analysis (when primary metric is pairwise)

| Zone | 定义 | 占比 (预估) | 对论文的意义 |
|---|---|---|---|
| High-consensus preference | 专家高度一致认为某输出更好 | TODO% | TODO |
| Structured disagreement | 分歧和某个 moderator（teaching stage / experience / context）相关 | TODO% | TODO |
| No-consensus zone | 专家无法稳定判断 | TODO% | TODO（这恰好支持构念预测 AI 应低承诺） |

## Study 3: Controlled / Vignette Study

### 设计

| 字段 | 内容 |
|---|---|
| 参与者 | TODO |
| 任务 | TODO |
| 主条件 | TODO（A vs B；条件名必须 demand-characteristic-neutral） |
| 错误注入 | TODO（多少 episode 包含 AI 错误？测试 appropriate rejection） |
| 盲法 | TODO |

### 主要因变量

| 变量 | 测量方式 |
|---|---|
| TODO | TODO |
| TODO | TODO |

## Study 4 (or N): Deployment — Cost as Finding

> **必须承认部署成本。** 见 `references/construct_critique.md` 第 6 角。

### 重新定位

TODO：写一段话，把 Study 4 的目的从"证明系统能用"重写成"理解系统如何被使用/抵抗/改写/延迟"。

### Two Scale Tiers

| 方案 | 规模 | 适合路线 |
|---|---|---|
| TODO ([Primary venue]-强评估版) | TODO（教师/参与者数 / 学校/机构数 / 时长 / 数据量） | TODO |
| TODO ([Pivot venue]-厚描版) | TODO | TODO |

### Deployment Cost as Finding

| Trade-off | 研究意义 |
|---|---|
| TODO (e.g., 更干净的证据 vs 更慢的节奏) | TODO |
| TODO (e.g., 更高可见性 vs 更高设备/组织成本) | TODO |
| TODO (e.g., 更低误诊风险 vs 更少即时流畅性) | TODO |

承认部署在 limitation / findings 里：

> TODO：用一段话承认本部署会改变 [user] 的 [activity rhythm]，并把这种改变本身定位为研究发现，不是 limitation。

## Participants / Dataset

TODO：说明用户样本或公开数据集从哪里来，是否需要伦理审批、授权或人工标注。

## Materials and Tasks

- TODO

## Procedure

1. TODO
2. TODO
3. TODO

## Baselines or Comparisons

- TODO：无辅助。
- TODO：通用 LLM / 现有系统 / 传统方法。
- TODO：消融版本（关键：包括 over-committed ablation——同一模型强制高承诺输出）。

## Measures

| Category | Measures |
|---|---|
| Quality | TODO |
| Efficiency | TODO |
| Cognitive Load / Burden | TODO |
| Trust / Adoption | TODO |
| Appropriate Reliance | TODO (harmful over-reliance + harmful under-reliance + helpful uptake) |
| Authorship Preservation | TODO (researcher-grade only) |
| Outcome | TODO |

## Analysis Plan

TODO：说明定量、定性或混合分析方法。不要预写不存在的显著结果。

For researcher-grade mode, also include:

- **Pairwise preference aggregation** (Bradley-Terry / Thurstone) for Study 2 if applicable
- **Interaction analysis** of how the user transforms AI suggestions (Study 4) — appropriation / deferral / resistance / authorship
- **Disagreement structuring** (which moderators predict expert disagreement zones)

## Expected Tables and Figures

- TODO：系统流程图。
- TODO：评价结果表（pairwise win rate / classification accuracy / harmful over- vs under-commitment rate）。
- TODO：风险或失败案例表（reviewer attack table 的可视化版）。
- TODO：Risk-benefit plot（横轴 episode ambiguity，纵轴 commitment strength；比较 baseline / over-committed / calibrated）。

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| TODO (e.g., expert kappa too low) | TODO (e.g., reframe disagreement as result; see Ground-Truth Stability Decision) |
| TODO (e.g., teachers reject the system in deployment) | TODO (e.g., promote rejection to finding; analyze appropriation) |
| TODO (e.g., demand characteristic in system name) | TODO (see `drafts/construct_stress_test.md` §5) |

## Evidence Status

Requires Manual Verification
