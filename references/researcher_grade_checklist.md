# Researcher-Grade Structural Checklist

Use this checklist before declaring a final report done. It encodes the 14 structural elements that distinguish a researcher-grade deliverable (CHI/CSCW/UIST/LAK-strong) from a competent-but-shallow research package.

The reference is `ProbeMate_CalibratedDiagnosticCommitment_CHI_CSCW_rewrite.tex` — every element below is anchored to a concrete passage there.

## Depth-Tier Requirements

| Depth | Required elements |
|---|---|
| `quick` | Element 6 (Neighbor Concept Differentiation Table) only, capped at 3 rows. |
| `standard` (no researcher-grade trigger) | Elements 1, 4, 6, 8, 9, 14 (6 of 14). |
| `standard` (researcher-grade triggered) | Elements 1–9, 12, 14 (11 of 14). |
| `deep` | All 14 elements. |

If an element is required but not produced, write `TODO` plus the reason in the final report rather than silently skipping. A `TODO` is visible; a missing element is not.

## The 14 Elements

### 1. Opening Thesis Box

**What.** A paragraph (3–6 sentences) at the very top of the final report that states the **core construct decision** — not the project topic, not the contribution list. The decision is the sharpened answer to "what makes this paper's framing different from the obvious one?"

**Why.** Forces the writer (and the reviewer) to know the central claim within ten seconds. Prevents the headline-competition failure mode.

**Pattern.**
> 这版的核心决定：不再把 X 写成 [obvious framing]。真正的构念不是 [obvious thing], 而是 [sharpened claim]. 因此本文把 [construct] 定义为 [precise scope]: [dim 1], [dim 2], [dim 3]. [Named levels] 只是这个空间中的常见 archetype, 不是真值类别, 不是一维序列.

**Anchor.** `\begin{thesisbox} ... \end{thesisbox}` at the top of ProbeMate.tex.

### 2. Headline Competition Audit

**What.** A short subsection (or audit table) listing the 2–4 alternative core constructs that were considered, with a one-sentence reason each was rejected as the spine.

**Why.** Proves to the reader (and to yourself) that the chosen headline survived a real selection process. Prevents "I picked the first phrase I thought of."

**Pattern.**

| 候选 headline | 一句话内容 | 为什么不选作 spine |
|---|---|---|
| [Candidate A] | [...] | [reason: 太工程 / 抢戏 / 不够反直觉 / 已是邻居概念] |
| [Candidate B] | [...] | [...] |
| [Selected] | [...] | 入选：[reverse intuition / 跨场域拉力 / 文献空缺] |

**Anchor.** Round 1 of `参考案例.md` enumerates four competing headlines.

### 3. Reverse Pitch — "It Is Not"

**What.** A short paragraph that says, before stating what the paper is, what the paper is **not**. List 3–5 misreadings that should be ruled out — engineering system, question bank, auto-grader, student-facing tutor, dataset paper, model paper.

**Why.** A reviewer skimming the abstract can otherwise classify the work into the wrong category and reject on the wrong criteria. The reverse pitch front-loads the disambiguation.

**Pattern.**
> 本项目不是 [misreading 1]; 不是 [misreading 2]; 不是 [misreading 3]. 它研究的是 [precise object].

**Anchor.** ProbeMate's §"核心问题不是" + "真正值得研究的问题" pair.

### 4. 3D (or N-D) Construct Operationalization

**What.** The construct's **definition** in one paragraph (italicized in the .tex), then a **dimension table** (each row = one axis of the construct), then a **measurement column** for each dimension (how the dimension is observed in data / system output / interaction log).

**Why.** Forces an honest dimensionality count. Prevents the ladder-vs-design-space failure. Without this element, the construct is just a name.

**Pattern.**

> *Definition.* [Construct name] refers to the design problem of [precise scope].

| 维度 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Dim A | [low] | [mid-low] | [mid-high] | [high] |
| Dim B | ... | ... | ... | ... |
| Dim C | ... | ... | ... | ... |

Then a formal expression:
> A system output is represented as $K_t = (A_t, B_t, C_t)$ ...

**Anchor.** ProbeMate §"三维操作化" with the $(E_t, V_t, D_t)$ table.

### 5. Archetype Table

**What.** A short table naming the 3–6 common combinations of dimension values that appear most often, framed as **archetypes** (not ground-truth classes, not ordinal levels).

**Why.** Gives readers a vocabulary to discuss the construct without forcing the dimensions back into a ladder.

**Pattern.**

| Archetype | (A, B, C) vector | 界面/系统形态 | 适用情境 |
|---|---|---|---|
| [Name 1] | $(0, 0, 0)$ | [description] | [when this applies] |
| [Name 2] | $(2, 2, 2)$ | ... | ... |

**Anchor.** ProbeMate §"C0--C3 不再是真值类别，而是四个 archetype."

### 6. Neighbor Concept Differentiation Table

**What.** A table with ≥ 5 rows (3 for quick mode), each listing a neighboring concept and the specific dimension(s) of your construct it cannot capture.

**Why.** The single most-skipped element in junior CHI/CSCW papers. If a reviewer can say "this is just X," you lose the contribution. The differentiation table makes the dimensional contrast unavoidable.

**Pattern.**

| 邻居概念 | 它主要解释什么 | 本构念的不同点 |
|---|---|---|
| Mixed-initiative interaction | [...] | [...] |
| Abstention / reject-option | [...] | [...] |
| Appropriate reliance | [...] | [...] |
| Progressive disclosure | [...] | [...] |
| Proactive vs reactive AI | [...] | [...] |
| Model confidence | [...] | [...] |

Required: at least one row must point to a **specific configuration** your construct can describe and the neighbor cannot.

**Anchor.** ProbeMate §"和已有概念的区分" with 6 rows.

### 7. Venue Strategy Table

**What.** A short table laying out the primary venue, the pivot venue (if data lands differently), the main difference in framing per venue, and the study-emphasis difference.

**Why.** Prevents venue split-personality. Lets the writer commit to one path while keeping the other live as a fallback.

**Pattern.**

| 路线 | 主贡献写法 | 研究重心 |
|---|---|---|
| [CHI-first] | [construct as design variable; quantifiable] | [Study 2 偏好 + Study 3 实验 + Study 4 中等部署] |
| [CSCW-pivot] | [construct as situated accomplishment] | [Study 1 + Study 4 厚描; interaction analysis] |

**Anchor.** ProbeMate §"最终建议的投稿策略" with CHI-first / CSCW-pivot.

### 8. RQ Matrix

**What.** Research questions in a **matrix**, not a flat list. Rows = RQs. Columns = study mapped / measure / evidence target / fail condition.

**Why.** A flat RQ list lets each RQ float; a matrix forces every RQ to declare what specifically would count as evidence and what would count as failure. Reviewers love this; it answers their "how would you know if you were wrong?" reflex pre-emptively.

**Pattern.**

| RQ | 研究问题 | 对应 Study | 主要 measure | 证据目标 | Fail condition |
|---|---|---|---|---|---|
| RQ1 | [...] | Study 1 | [interview themes] | [pattern X identified across ≥6 teachers] | [no pattern; high inter-participant variance] |
| RQ2 | [...] | Study 2 | [pairwise win rate] | [calibrated > over-committed at p<.05] | [no significant difference] |
| ... | ... | ... | ... | ... | ... |

Minimum 4 RQs for standard, 5+ for deep.

**Anchor.** ProbeMate §"研究问题重写" 5-row RQ table.

### 9. Study 1 Alternative Outcomes Table

**What.** Instead of "expected findings F1–F5," a table of outcomes that would **falsify or reshape** the design. Each row: possible finding / how it refutes/remixes / specific design response.

**Why.** The single fastest way to demonstrate that a formative study is inquiry rather than performance.

**Pattern.**

| 可能发现 | 它如何推翻/重塑原设计 | 设计后果 |
|---|---|---|
| [strong-form opposite of design assumption] | [...] | [...] |
| [different population finding] | [...] | [...] |
| [novice vs expert inversion] | [...] | [...] |
| [cost-too-high finding] | [...] | [...] |
| ... (≥ 5 rows for deep, ≥ 3 for standard) | ... | ... |

**Anchor.** ProbeMate §"把'可能推翻设计的发现'写进方案" 7-row table.

### 10. Ground-Truth Stability Check (Evaluation Study)

**What.** A short paragraph stating whether the evaluation hinges on a stable categorical label or on a context-dependent judgment. If context-dependent, the evaluation uses **pairwise preference** as primary metric and treats **expert disagreement as result**.

**Why.** Prevents the "kappa = 0.3, what now?" disaster. Reframes disagreement as informative.

**Pattern.**
> 评估说明：本构念的核心判断依赖 [factor list]，因此专家在 [estimated %] 的 episode 上不会有统一答案。主评估改为 pairwise preference，Bradley-Terry / Thurstone 聚合，分歧本身分为 high-consensus / structured-disagreement / no-consensus zones 并作为结果分析。Classification accuracy 仅作为次要技术指标。

Plus a table breaking down expert-disagreement zones and what each zone implies for the construct.

**Anchor.** ProbeMate §"Study 2：从'专家给真值'改为 pairwise preference + disagreement analysis."

### 11. Deployment Cost as Finding

**What.** In the deployment / field-study section, an explicit **trade-off table** acknowledging the resources / time / labor the deployment consumes, plus **two scale tiers** (strong-evaluation tier and thick-description tier).

**Why.** Prevents the "we deployed in K-12 classrooms" hand-wave. Treats deployment cost as research-relevant rather than a hidden cost.

**Pattern.**

| Trade-off | 研究意义 |
|---|---|
| [cleaner evidence vs slower pace] | [...] |
| [more visibility vs higher infrastructure cost] | [...] |
| [lower mis-diagnosis risk vs less spontaneity] | [...] |

And:

| 方案 | 规模 | 适合路线 |
|---|---|---|
| [CHI 强评估版] | [smaller; tighter measurement] | [...] |
| [CSCW 厚描版] | [bigger; qualitative depth] | [...] |

**Anchor.** ProbeMate §"Study 4：真实课堂部署必须更诚实、更厚" + "可行的部署规模：两档方案" + "承认课堂时间成本."

### 12. Reviewer Attack Table

**What.** A table anticipating 5–10 specific reviewer objections, with rebuttal sketches and explicit pointers to which section/study addresses each.

**Why.** Forces pre-emptive defense. A reviewer who sees their own objection already addressed is much harder to push back.

**Pattern.**

| 攻击点 | 审稿人可能怎么说 | 论文里如何预防 |
|---|---|---|
| [Construct = old idea renamed] | [...] | [neighbor table + dimensional examples in §X] |
| [Levels not 1D] | [...] | [archetype framing + N-D operationalization in §Y] |
| [Formative倒推] | [...] | [alternative outcomes table in §Z] |
| ... | ... | ... |

**Anchor.** ProbeMate §"Reviewer attack table" with 10 rows.

### 13. Demand Characteristic Audit

**What.** A short paragraph (or appendix note) auditing the system name, condition labels, interview wording, and RQ phrasing for embedded answers.

**Why.** Prevents a reviewer from killing the paper on demand-characteristic grounds at the methods stage.

**Pattern.**
> 命名审计：系统名 [neutral name]，避免暗示 [trait]。条件命名采用 A/B 或 [descriptive neutral terms]，内部记录时再标注 [internal label]。访谈先问教师实际行动，再问其对 AI 的偏好，避免 leading wording。

**Anchor.** ProbeMate §"系统名和实验命名" + the QuietProbe → ProbeMate revert.

### 14. Elevator Pitch Box

**What.** A 3–6 sentence paragraph at the report's tail (or in a sidebar) that summarizes the paper for a one-minute pitch. Must survive the headline-competition audit — only the chosen spine appears.

**Why.** What the user can read aloud to a supervisor at the start of a meeting.

**Pattern.**
> 本项目不再把重点放在 [obvious framing]，而是研究一个更基础的 [field] 问题：[sharpened question]. 在 [real setting], [phenomenon explanation]. 因此 [system / method] 不能 [naive goal]，而要 [precise goal]. 我把这个问题命名为 [construct]. 通过 [testbed], 我会先 [Study 1], 再 [Study 2/3], 最后 [Study 4]. 本论文的贡献不是 [naive thing], 而是 [precise contribution].

**Anchor.** ProbeMate §"可以直接给导师看的新版 elevator pitch" thesisbox.

## Verification Workflow

Before declaring `reports/final_topic_report.md` done, run through this list:

1. Open the final report. For each required element (per depth tier), check it is present.
2. For any element marked `TODO`, write a one-line reason in `reports/06_final_recommendation.md` so the user knows why.
3. If `researcher-grade` triggered, also check `drafts/construct_stress_test.md`, `drafts/critique_round_<N>.md`, `drafts/construct_rewrite_<N>.md`, `drafts/venue_fit_decision.md` all exist and are non-trivial.
4. Run `python assets/project-template/scripts/workflow_checklist.py --list` and confirm the artifact tree matches.

## Failure Modes This Checklist Catches

- **Headline drift** (multiple un-collapsed central claims).
- **Repackaged neighbor concepts** (definitional rather than dimensional differentiation).
- **Hidden ladder compression** (named levels secretly multi-axis).
- **Performative formative studies** (predicted findings that cannot fail).
- **Forced ground-truth labeling** (kappa-doomed classification metrics).
- **Hand-waved deployment cost** (no acknowledgment of class time / labor / infrastructure).
- **Embedded answer in naming** (system name that pre-loads the result).
- **Venue split-personality** (cannot say in one sentence which reviewer will be happiest).

If a researcher-grade report ships without catching at least the elements relevant to its specific shape, the user will hit one or more of these failures at supervisor review or peer review.
