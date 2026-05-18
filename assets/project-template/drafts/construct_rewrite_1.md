# 构念重写 — 第 1 轮 (Construct Rewrite — Round 1)

Snapshot of the construct package **after** absorbing every failing angle from `critique_round_1.md`. This file is the new authoritative source for Modules F and G — the title, abstract, RQs, and v2 report must be consistent with this rewrite.

Status: Draft / Round 1 rewrite
Revised from: `construct_stress_test.md` + `critique_round_1.md`

---

## 1. Revised Title (and Subtitle)

| | Before round 1 | After round 1 |
|---|---|---|
| Main title | TODO (quote previous) | TODO (rewritten) |
| Subtitle | TODO | TODO |
| 中文标题 | TODO | TODO |
| Working system name | TODO | TODO (must be neutral; no demand-characteristic embedding) |

Headline competition resolution (filling angle 1 fix):

- Spine: TODO (the chosen central claim)
- Demoted candidates: TODO (where each demoted headline now lives: mechanism / operationalization / evidence)

## 2. Revised Construct Definition

> *Definition.* [Construct name] refers to TODO (precise scope statement, in one sentence).

Differentiation from neighbor concepts (filling angle 2 fix):

| 邻居概念 | 它主要解释什么 | 本构念的不同点 (dimensional, not definitional) |
|---|---|---|
| TODO | TODO | TODO |
| TODO | TODO | TODO |
| TODO | TODO | TODO |
| TODO | TODO | TODO |
| TODO | TODO | TODO |
| TODO (≥ 5 rows for standard/deep, 3 for quick) | TODO | TODO |

Specific configuration this construct captures that neighbors cannot:

TODO: one concrete example.

## 3. Revised Operationalization (Dimensional)

If angle 3 fired (ladder vs design-space), promote the construct to N-D here:

| 维度 | 含义 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| TODO (Dim A) | TODO | TODO | TODO | TODO | TODO |
| TODO (Dim B) | TODO | TODO | TODO | TODO | TODO |
| TODO (Dim C) | TODO | TODO | TODO | TODO | TODO |

Formal representation (optional but recommended):

> A system output / state is represented as $K = ($TODO$)$, where TODO.

Archetypes (named common points in the design space):

| Archetype | Vector | 界面/系统形态 | 适用情境 |
|---|---|---|---|
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

Explicit note: TODO (one sentence stating the archetypes are not ordinal, not exhaustive, not ground-truth classes).

## 4. Revised RQ Matrix

| RQ | 研究问题 | 对应 Study | 主要 measure | 证据目标 | Fail condition |
|---|---|---|---|---|---|
| RQ1 | TODO | TODO | TODO | TODO | TODO |
| RQ2 | TODO | TODO | TODO | TODO | TODO |
| RQ3 | TODO | TODO | TODO | TODO | TODO |
| RQ4 | TODO | TODO | TODO | TODO | TODO |
| RQ5 (optional) | TODO | TODO | TODO | TODO | TODO |

## 5. Revised Study Designs

### Study 1 — Formative Inquiry (filling angle 4 fix)

Aim (rewritten as inquiry, not performance):

TODO.

Alternative Outcomes Table (replacing "predicted findings"):

| 可能发现 | 它如何推翻/重塑原设计 | 设计后果 |
|---|---|---|
| TODO (strong-form "design is wrong" finding) | TODO | TODO |
| TODO (different-population finding) | TODO | TODO |
| TODO (novice vs expert inversion) | TODO | TODO |
| TODO (cost-too-high finding) | TODO | TODO |
| TODO (≥ 5 rows for deep, ≥ 3 for standard) | TODO | TODO |

Interview script principles (filling angle 7 fix on prompts):

- TODO: ask about actual practice before asking about AI preferences.
- TODO: avoid leading wording.

### Study 2 — Evaluation (filling angle 5 fix if it fired)

If ground-truth stability fired:

- Primary metric: pairwise preference (Bradley-Terry / Thurstone aggregation).
- Disagreement analysis: high-consensus / structured-disagreement / no-consensus zones, each as a separate result.
- Classification accuracy retained as **secondary technical metric only**.

Otherwise, document why classification ground-truth is stable here.

### Study 3 — Controlled / Vignette (filling angle 7 fix on condition labels)

Conditions renamed (if angle 7 fired):

- Condition A: TODO (neutral)
- Condition B: TODO (neutral)
- Internal labels (paper narrative only): TODO

### Study 4 — Deployment (filling angle 6 fix)

Deployment cost trade-off table:

| Trade-off | 研究意义 |
|---|---|
| TODO | TODO |
| TODO | TODO |
| TODO | TODO |

Two Scale Tiers:

| 方案 | 规模 | 适合路线 |
|---|---|---|
| TODO ([primary-venue]-strong-eval) | TODO | TODO |
| TODO ([pivot-venue]-thick-description) | TODO | TODO |

## 6. Revised Venue Strategy (filling angle 8 fix)

Primary venue: TODO
Pivot venue: TODO
One-sentence happy-reviewer statement: TODO

| 路线 | 主贡献写法 | 研究重心 |
|---|---|---|
| [Primary] | TODO | TODO |
| [Pivot] | TODO | TODO |

Pivot trigger condition: TODO (the specific data outcome that would cause a pivot — declare it now so it can be recognized later without rationalization).

## 7. Topic Lock Update

- [ ] `config/topic_lock.yaml` updated? (Yes / No / Not needed)
- [ ] If yes, row appended to `reports/05_topic_drift_warning.md` linking to the critique angles that triggered the update? (Yes / No)

If `topic_lock.yaml` changed, note the before/after for `core_problem`, `target_user_or_population`, and `expected_contribution` here:

| Field | Before round 1 | After round 1 |
|---|---|---|
| core_problem | TODO | TODO |
| target_user_or_population | TODO | TODO |
| expected_contribution | TODO | TODO |

## 8. Round 1 Closing Statement

TODO: one short paragraph stating whether the construct is now ready for Module F / G, or whether a round 2 (deep only) is warranted.

If proceeding to round 2: list the angles you expect round 2 to bite hardest on.
