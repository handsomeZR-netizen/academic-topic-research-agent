# Modular Pre-Research Workflow

Use this workflow as a menu of modules, not a mandatory linear pipeline. The goal is to help the assistant turn an early academic idea into a supervisor-ready research plan.

## Choose Depth

- `quick`: 10-20 candidate metadata records; concise report or title/abstract advice.
- `standard`: 30-50 candidate metadata records; normal pre-research package.
- `deep`: 80-120 candidate metadata records; systematic preparation, "100 papers/PDF metadata", venue mapping, or broad literature reconnaissance.

Default to `standard`. Use `deep` when the user asks for "深入", "完整", "100 篇", "100 个 PDF 元数据", or similar wording. A depth target counts only when at least one-third of records reach `keep` or `background` status — pure `candidate` lists do not satisfy the target.

## Researcher-Grade Mode

Researcher-grade mode runs **Module H (Construct Stress Test & Critique Refinement Loop)** between Modules E and F. It encodes the supervisor-style critique that turns an OK package into a CHI/CSCW-strong one. See `references/construct_critique.md` for the 8 critique angles and `references/researcher_grade_checklist.md` for the 14 structural elements every researcher-grade final report must carry.

| Depth | Researcher-Grade behavior |
|---|---|
| `deep` | Automatically on. Module H runs **2** critique → rewrite passes. All 14 checklist elements required in the final report. |
| `standard` | Off by default. Turns on only when the user message contains a trigger keyword: `researcher-grade` / `深度打磨` / `构念压力测试` / `CHI 级` / `CSCW 转身` / `期刊投稿级`. When on, Module H runs **1** critique → rewrite pass; checklist requires 11 of 14 elements. |
| `quick` | Module H is skipped. But the **Neighbor Concept Differentiation Table** (checklist element 6) is still mandatory — 3-row cap — and lives in `drafts/contribution_candidates.md`. |

When researcher-grade is on, also run `Module I-equivalent` (the venue fit decision) as Module H step H4, producing `drafts/venue_fit_decision.md` per `references/venue_fit.md`.

## Module A: Intake and Boundary

Use whenever the user opens a new topic or hands over a title, proposal, `.tex`, notes, or PDF.

### Required Intake Checklist

Before searching, confirm the assistant has at least three of these four core fields:

1. **研究主题 / 核心问题**
2. **目标会议或期刊** (CHI / LAK / L@S / AIED / EDM / CSCW / UIST / IJHCI / IJCAI / 中文期刊 …)
3. **深度偏好** (`quick` / `standard` / `deep`)
4. **数据 / 研究类型** (公开数据集 / 课堂数据 / 访谈 / Wizard-of-Oz / 标注 / vignette …)

Strongly-recommended follow-ups:

- 年份范围
- 必含 / 必避关键词
- 是否已有 proposal / PDF / .tex / 笔记
- 时间预算
- 输出语言（默认中文）

If three core fields are missing, **stop and ask the user in one consolidated turn** using `references/intake_questions.md`. Do not silently guess defaults and start searching.

### Outputs

- `config/topic_input.yaml` (filled with user answers, replacing the `# 例如：...` placeholders)
- `config/topic_lock.yaml` (when boundaries need to be locked)
- `reports/00_topic_lock.md`
- `reports/05_topic_drift_warning.md` — write this only when a later module's search or design clearly deviates from `topic_lock.yaml`. The drift warning should name the deviation, list its evidence, and propose either re-locking the topic or pulling back the search.

### Purpose

- identify the core research problem
- preserve user intent
- mark non-goals
- prevent the search from drifting toward easy datasets or fashionable but different topics

For quick tasks, this can be a section inside the final report instead of separate files.

## Module B: Metadata Reconnaissance

Use for literature-heavy tasks, venue mapping, and deep pre-research.

Outputs may include:

- `data/processed/metadata_candidates.csv`
- `data/processed/paper_matrix.csv`
- `logs/evidence_trace.jsonl`

Before searching, read `config/sources.yaml` and use only sources marked `enabled: true`. The user can disable any source by editing that file.

Optional but recommended for tag-heavy projects: copy `config/tag_schema.example.yaml` to `config/tag_schema.yaml` and replace the example T1-T5 tags with tags that match your own topic before bulk coding. The shipped example covers a teacher-facing classroom-decision-support study and will not fit other domains.

Collect:

- title, authors, year, venue
- DOI, URL, OA PDF URL if available
- abstract or summary
- source and query
- relevance and screening status
- reason to keep or exclude

Do not require full-text reading for every candidate. Use the metadata layer to build a map, then select key papers for deeper reading.

## Module C: Evidence Map and Gap Reasoning

Use after enough metadata exists.

Outputs may include:

- `reports/03_gap_matrix.md`
- a prior-work comparison table in the final report

Answer:

- which clusters are already well covered
- which closest systems or methods matter most
- which combination gap is plausible
- what is only background
- what cannot be claimed yet

## Module D: Dataset and Study Feasibility

Use for any topic that implies experiments, benchmarks, user data, classroom data, evaluation, or deployment.

Outputs may include:

- `data/processed/dataset_candidates.csv`
- `reports/04_dataset_feasibility.md`

Decide:

- `Pass`
- `Weak Pass`
- `Fail`

If no public dataset fits, propose a realistic study route such as formative interviews, annotation, expert review, Wizard-of-Oz, vignette study, field deployment, or benchmark construction.

## Module E: Research Design Development

Use to turn evidence into a project plan.

Outputs may include:

- `drafts/contribution_candidates.md`
- `drafts/experiment_plan.md`
- `drafts/paper_skeleton.tex`

Develop:

- research questions
- contribution package
- system or method boundary
- evaluation design
- measures and risks
- near-term execution plan

## Module H: Construct Stress Test & Critique Refinement Loop

Use when researcher-grade mode is on (deep automatic; standard with keyword). Skip for quick (but still produce the Neighbor Concept Differentiation Table in `drafts/contribution_candidates.md`).

Module H sits between E and F. It treats the construct package coming out of E as a draft to be stress-tested, not a finished plan. Modules F (title/abstract) and G (final report) must take Module H's outputs as authoritative input — not the pre-critique E drafts.

### Loop Structure

```
H1. Write drafts/construct_stress_test.md
    (capture current construct: opening thesis decision, headline competition
    audit, neighbor differentiation, ladder/design-space check, demand
    characteristic audit, venue split-personality diagnostic)

H2. Run drafts/critique_round_<N>.md applying the 8 angles in
    references/construct_critique.md:
      1 Headline competition
      2 Construct vs neighbor concepts
      3 Ladder vs design-space confusion
      4 Formative study as performance vs inquiry
      5 Ground-truth instability
      6 Deployment cost hidden as feature
      7 Demand characteristic in naming/framing
      8 Venue split-personality

    If failing angles <= 1:
      Rename critique_round_<N>.md to critique_round_<N>_passed.md,
      document the borderline angle, and jump to H4.
    Else:
      Continue to H3.

H3. Write drafts/construct_rewrite_<N>.md absorbing every failing angle.
    If scope changed: update config/topic_lock.yaml and append a row to
    reports/05_topic_drift_warning.md citing the firing angles.
    If N == 2 (deep only): loop back to H2 with critique_round_2.md.

H4. Write drafts/venue_fit_decision.md per references/venue_fit.md:
    primary venue, pivot venue, per-study rewrite implications,
    reviewer attack table, pivot trigger condition.
```

### Outputs

- `drafts/construct_stress_test.md`
- `drafts/critique_round_1.md` (or `critique_round_1_passed.md`)
- `drafts/construct_rewrite_1.md` (if round 1 had ≥ 2 fails)
- `drafts/critique_round_2.md` (deep only, if needed)
- `drafts/construct_rewrite_2.md` (deep only, if round 2 had ≥ 2 fails)
- `drafts/venue_fit_decision.md`
- `reports/05_topic_drift_warning.md` (updated row, if topic lock changed)

### Hand-Off to Modules F and G

After H4, Modules F and G must use `construct_rewrite_<latest>.md` and `venue_fit_decision.md` as their authoritative source. The 14-element researcher-grade checklist in `references/researcher_grade_checklist.md` defines which structural elements must appear in the final v2 report at each depth tier.

## Module F: Title and Abstract Development

Use when the user needs naming, framing, proposal polish, or paper direction.

Outputs may include:

- `drafts/title_candidates.md`
- `drafts/abstract_candidates.md`

Create several title styles:

- conservative evidence-first
- venue-fit / CHI-style
- ambitious but safe
- method/system-focused

Do not imply completed experiments unless results exist.

When researcher-grade mode is on, Module F must:

- Use the **spine** chosen in `drafts/construct_rewrite_<latest>.md` section 1 as the basis for every title candidate.
- Fill the **Headline Competition Audit** table inside `drafts/title_candidates.md` (no two candidates may map to the same construct spine).
- Fill the **Construct Sentence / Differentiation Sentence / Quantified Placeholder Sentence** fields inside `drafts/abstract_candidates.md`.
- Treat any candidate that re-introduces a demoted alternative headline as a failure of integration and reject it.

## Module G: v2-Style Final Report

Use for the final deliverable.

Outputs:

- `reports/final_topic_report.md`
- `reports/final_topic_report.tex`
- `reports/final_topic_report.pdf` when TeX is available
- `reports/06_final_recommendation.md` when a verdict is needed

Use `assets/report-blueprint/` as the minimal skeleton. Copy it, then fill and adapt it. The skeleton is allowed to change per topic.

The report should read like a research-plan memo, not a checklist: core judgment first, evidence and data support next, concrete cases and evaluation plan, then risks and next steps.

When researcher-grade mode is on, also append the structural elements from `assets/report-blueprint/v2_researcher_grade_extensions.md` (and `.tex` for the LaTeX version) using the integration map at the top of that file. The 14-element checklist in `references/researcher_grade_checklist.md` defines which elements are required at each depth tier; missing required elements must be written as visible `TODO` lines rather than silently omitted.

### `final_topic_report.md` vs `06_final_recommendation.md`

These are two different artifacts:

- `final_topic_report.md` / `.tex` — the full v2-style research-plan report (positioning, prior work, design, feasibility, risks, timeline). This is the main deliverable.
- `06_final_recommendation.md` — a short, advisor-facing decision memo. One page or less. Verdict (`推进` / `收窄` / `重做`), three to five reasons, and the minimum next action. Write this when the user explicitly asks for a verdict, or when the report alone would not surface the decision.

## Progress Self-Check

Run `python assets/project-template/scripts/workflow_checklist.py --list` to print the recommended artifacts for every module. Use the output as a checklist when finishing a run.

## Final Response to User

Keep the chat response short. List:

- generated report files
- title/abstract files
- metadata or dataset files if produced
- PDF status (see template below)
- key feasibility verdict and manual verification warnings

### PDF Status Template

Use one of these exact phrasings when reporting PDF state:

- 成功：`PDF: reports/final_topic_report.pdf 已生成。`
- TeX 缺失：`PDF 跳过：本机未检测到 xelatex / latexmk。Markdown 与 LaTeX 已生成，可在有 TeX 环境的机器上用 xelatex 编译。`
- Pandoc 缺失：`PDF 跳过：本机未检测到 Pandoc，已用保守回退转换生成 LaTeX；如需高保真请安装 Pandoc 后重跑 render_report.py。`
- 字体缺失：`PDF 跳过：xelatex 找不到所需 CJK 字体。请安装宋体/黑体/楷体/仿宋（Windows）或 noto-cjk（Linux）后重跑。`

Pick the line that matches reality. If multiple components are missing, list them in one line.
