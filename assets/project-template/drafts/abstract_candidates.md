# 摘要候选

## 必填字段 (researcher-grade 模式)

Researcher-grade 摘要在写作前必须先确定这三句话。这三句话决定了摘要的脊椎。

| 字段 | 内容 |
|---|---|
| Construct Sentence（一句话定义核心构念） | TODO |
| Differentiation Sentence（一句话说明本构念为什么不只是邻居概念 X 的换名） | TODO |
| Quantified Placeholder Sentence（一句话承诺量化结果，可以暂用占位符 `[X%]` / `[Y%]`） | TODO |

`Quantified Placeholder Sentence` 是 CHI 摘要的标志性形式承诺——例如 `we find that calibrated commitment reduced harmful over-commitment by [X%] while preserving helpful uptake [Y%] compared with an over-committed LLM baseline`. 投稿前必须把 `[X%]` 替换为真实数据；目前用占位符是允许的，但要在 Evidence Binding 表里标记 Status = TODO。

## Version A: 保守证据优先版

Status: Draft / Evidence-bound

TODO：不暗示已完成实验，强调问题、已有证据、拟议系统/方法、评估计划和预期贡献。开头点出 Construct Sentence；中间放 Differentiation Sentence；结尾不写 Quantified Placeholder（因为这一版偏证据）。

## Version B: 目标会议适配版

Status: Draft / Venue-fit

TODO：用目标会议的口吻——CHI 偏 design construct + evaluation；CSCW 偏 situated accomplishment + fieldwork；LAK 偏 learning theory grounding；UIST 偏 novel interaction technique。开头放 Construct Sentence；中间放 Differentiation Sentence；如果是 CHI/UIST 路线，必须以 Quantified Placeholder Sentence 收尾。

## Version C: 稍强但安全版

Status: Draft / Ambitious but safe

TODO：表达更有吸引力，但避免"证明""显著提升"等未验证结果。可以使用占位符量化句但要在 Evidence Binding 表里标 Status = TODO。

## Evidence Binding

| Sentence / Claim | Evidence Source | Status | Keep / Revise / Remove |
|---|---|---|---|
| Construct Sentence | `construct_rewrite_<latest>.md` §2 / topic_lock.yaml | Supported / Unknown / TODO | Keep |
| Differentiation Sentence | Neighbor Concept Differentiation Table in `contribution_candidates.md` | Supported / Unknown / TODO | Keep |
| Quantified Placeholder Sentence | Pending Study 2/3 results | TODO | Keep（占位符）/ Remove（投稿时）|
| TODO (其它句) | TODO | TODO | TODO |

## Abstract Safety Check

- [ ] 没有 "we prove" / "我们证明" 类未验证宣言
- [ ] 没有 "significantly improves" / "显著提升" 除非已经有结果
- [ ] 占位符 `[X%]` / `[Y%]` 都在 Evidence Binding 表里登记
- [ ] 与 `config/topic_lock.yaml` 的 `core_problem` 和 `expected_contribution` 一致
- [ ] 与 `construct_rewrite_<latest>.md` 选定的 spine 一致（researcher-grade 时）
- [ ] 系统名与 Demand Characteristic 审计后的中性名一致（researcher-grade 时）
