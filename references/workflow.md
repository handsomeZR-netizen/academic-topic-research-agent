# Modular Pre-Research Workflow

Use this workflow as a menu of modules, not a mandatory linear pipeline. The goal is to help the assistant turn an early academic idea into a supervisor-ready research plan.

## Choose Depth

- `quick`: 10-20 candidate metadata records; concise report or title/abstract advice.
- `standard`: 30-50 candidate metadata records; normal pre-research package.
- `deep`: 80-120 candidate metadata records; systematic preparation, "100 papers/PDF metadata", venue mapping, or broad literature reconnaissance.

Default to `standard`. Use `deep` when the user asks for "深入", "完整", "100 篇", "100 个 PDF 元数据", or similar wording. A depth target counts only when at least one-third of records reach `keep` or `background` status — pure `candidate` lists do not satisfy the target.

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

## Module G: v2-Style Final Report

Use for the final deliverable.

Outputs:

- `reports/final_topic_report.md`
- `reports/final_topic_report.tex`
- `reports/final_topic_report.pdf` when TeX is available
- `reports/06_final_recommendation.md` when a verdict is needed

Use `assets/report-blueprint/` as the minimal skeleton. Copy it, then fill and adapt it. The skeleton is allowed to change per topic.

The report should read like a research-plan memo, not a checklist: core judgment first, evidence and data support next, concrete cases and evaluation plan, then risks and next steps.

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
