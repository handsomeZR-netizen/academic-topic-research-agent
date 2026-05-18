# 贡献候选

## Contribution Map

| Type | Candidate Contribution | Evidence Support | Operationalization Risk | What Remains Unknown | Safe Wording |
|---|---|---|---|---|---|
| Empirical | TODO | TODO | TODO (e.g., expert agreement instability) | TODO | TODO |
| Conceptual | TODO | TODO | TODO (e.g., neighbor concept overlap) | TODO | TODO |
| System / Method | TODO | TODO | TODO (e.g., deployment cost reshaping classroom) | TODO | TODO |
| Evaluation | TODO | TODO | TODO (e.g., ground-truth instability → switch to pairwise) | TODO | TODO |

`Operationalization Risk` 列检测每个贡献在落实到 study / measurement / data 时的潜在结构性失败——是否会撞到 ground-truth instability（角度 5）、deployment cost honesty（角度 6）、demand characteristic（角度 7）等问题。如果某一行的 Risk 列写"High"，回到 `drafts/critique_round_<N>.md` 检查对应角度是否已经被 critique 过。

## Neighbor Concept Differentiation

> **强制要求所有深度等级。** `quick` 模式至少 3 行；`standard`/`deep` 至少 5 行。

每一行：邻居概念名 / 它主要解释什么 / 本构念在哪一维与它不同。**关键：区分必须是 dimensional 的（"我们有一个 X 抓不到的维度"），不能是 definitional 的（"我们关心 Y"）。**

| 邻居概念 | 它主要解释什么 | 本构念的不同点 (dimensional, not definitional) |
|---|---|---|
| TODO (e.g., Mixed-initiative interaction) | TODO | TODO |
| TODO (e.g., Abstention / reject-option) | TODO | TODO |
| TODO (e.g., Appropriate reliance) | TODO | TODO |
| TODO (e.g., Progressive disclosure) | TODO | TODO |
| TODO (e.g., Proactive vs reactive AI) | TODO | TODO |
| TODO (e.g., Model confidence) | TODO | TODO |

**至少一行必须给一个 specific configuration**——一个本构念能描述、邻居概念不能描述的具体例子：

> TODO：用一句话写出这个 specific configuration。例如："本构念能区分 '高置信但低可见性' 与 '低置信但高可见性' 两种 commitment vector；而 model confidence 只能给出标量。"

## Unsafe Claims

- TODO：需要真实实验或数据支持，当前不能写成结论。
- TODO：声称比所有 baseline 都好，但 baseline 还没跑。
- TODO：声称跨场景泛化，但只在一个 testbed 测过。

## Recommended Contribution Package

TODO：建议最终论文主打哪 2--4 个贡献，哪些贡献放到 Discussion 或 Future Work。

For researcher-grade mode, the package should explicitly include:

1. **Conceptual contribution** — the construct itself (sourced from `construct_rewrite_<latest>.md` §2--3)
2. **System / method contribution** — the prototype that operationalizes the construct
3. **Empirical contribution** — what the evaluations show (pairwise preference results, deployment findings)
4. **Methodological contribution** — when applicable, the evaluation method itself (e.g., pairwise preference + disagreement analysis as a way to evaluate context-dependent design variables)

If any of these four cannot be sourced from current evidence, write the safe-wording variant in the Contribution Map above (e.g., `本项目拟通过 Study X 验证` rather than `we show that`).
