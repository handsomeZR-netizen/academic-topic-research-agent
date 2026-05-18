# 标题润色方案

## 推荐排序

| Rank | Title | 中文理解 | 风格 | 核心构念 (spine) | Venue Fit | Evidence Fit | Feasibility | Demand Characteristic Risk | Recommendation |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | TODO | TODO | 稳健 / CHI-style / 方法型 / 系统型 | TODO | TODO | TODO | TODO | TODO (None / Low / Medium / High + 备选名) | TODO |
| 2 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |
| 3 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

`核心构念 (spine)` 列必须填——它强迫每个标题候选映射到唯一的中心构念。如果两个候选映射到同一个 spine，是冗余；如果三个候选映射到三个不同的 spine，则是 headline 抢戏（见下一节）。

`Demand Characteristic Risk` 列检测标题或系统名是否预埋答案。例如 `QuietProbe` → Quiet 暗示答案；`CalibratedAssistant` → Calibrated 暗示答案。这一列至少要列出当前命名的风险等级；High/Medium 时给出中性备选名。

## Headline Competition Audit

> 必填（researcher-grade 模式）。`quick` 模式可省略。

把上面 N 个候选标题映射到它们暗含的中心构念。

| 候选标题 | 暗含的中心构念 | 一句话内容 |
|---|---|---|
| TODO | TODO | TODO |
| TODO | TODO | TODO |
| TODO | TODO | TODO |

**抢戏判定：** 上面表里能数出几个 *不同* 的中心构念？

- 1 个 → 健康。所有候选只是同一脊椎的不同语气版本。
- 2 个 → 注意。可能在 spine 抉择上还没下定。
- ≥ 3 个 → **headline 抢戏**。回到 `drafts/construct_stress_test.md`，重新做 spine 选择，把没选中的标题降级到 mechanism / operationalization / evidence 层。

抢戏判定结果：TODO。

## 标题选择建议

TODO：说明最推荐哪个标题，为什么它比其他标题更稳，以及哪些词会导致过度承诺。

如果 researcher-grade 模式已开，注明：

- 当前 spine 来自 `drafts/construct_rewrite_<latest>.md` 第 1 节
- 推荐标题的 Demand Characteristic 等级是 TODO；备选中性名（若需要）是 TODO

## 避免使用的标题方向

- TODO：过度声称结果的标题（"validating X"、"proving Y"、"the first system to ..."）
- TODO：太像产品名或工程项目的标题（"-Bot"、"-Mate"、"-Assistant" 后缀；除非确实是系统贡献）
- TODO：偏离 topic lock 的标题（与 `config/topic_lock.yaml` 的 `core_problem` / `target_user_or_population` 不一致）
- TODO：预埋答案的标题（"Why Quiet Wins"、"Calibrated AI Outperforms Over-Confident Baselines"）

## 中性命名备选库

仅在 Demand Characteristic Risk 表里出现 High/Medium 时填写。

| 当前名 | 风险 | 中性备选 1 | 中性备选 2 |
|---|---|---|---|
| TODO | TODO | TODO | TODO |
