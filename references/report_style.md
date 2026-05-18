# v2-Style Report Guide

Use this guide when writing `reports/final_topic_report.md` and `reports/final_topic_report.tex`.

## What "v2-style" Means

The report should resemble `网页版个人调研/v2.tex` in structure and argumentative feel:

- a strong one-sentence or one-paragraph judgment at the beginning
- clear distinction between what the project is and is not
- concrete classroom/system/method cases rather than abstract slogans
- prior-work positioning tables
- data or study feasibility analysis
- research questions and evaluation route
- risk table and near-term execution plan
- final judgment that says whether to proceed, narrow, or revise

Do not copy the specific ProbeMate/high-school physics content unless the user is working on that exact topic.

## Skeleton Is Not a Cage

Use `assets/report-blueprint/` as a minimal skeleton to copy from. Adapt it:

- merge sections when the task is small
- rename sections to fit the target venue or discipline
- omit impossible sections when the topic does not involve systems, datasets, or human studies
- add sections for domain-specific needs

Keep the report coherent and advisor-ready even when sections change.

## Default Tone

Default output language is Chinese.

Write like a serious advisor-facing research memo:

- direct core judgment first
- evidence-bound but not timid
- concrete examples
- careful novelty language
- practical next steps

Avoid generic literature review summaries, marketing prose, and unsupported "we prove" language.

## Recommended Sections

Use most of these for full reports:

1. 一句话概括
2. 项目核心判断
3. 为什么适合目标会议或期刊
4. 核心概念与研究问题
5. 输入模态、数据模态或研究对象边界
6. 系统方案或方法方案
7. 交互/方法设计原则
8. 算法与数据的最小可行方案
9. 典型案例或使用场景
10. 研究问题与评价方案
11. 数据集支持与可行性判断
12. 标题润色方案与摘要
13. 预期论文结构
14. 投稿定位
15. 风险与应对
16. 下一步工作
17. 最终总结

For `quick` tasks, do not force all 17 sections. Pick 5-7, prioritized roughly as: **项目核心判断 → 研究问题与评价方案 → 数据集支持与可行性判断 → 标题润色方案与摘要 → 风险与应对 → 下一步工作**. Merge or drop the rest. The argumentative pattern matters more than section count.

## LaTeX Style

The LaTeX report should use:

- `ctexart`
- 2.4 cm margins
- blue section headings
- `tcolorbox` for summary, key question, warning, and conclusion boxes
- `booktabs`, `tabularx`, and `longtable` for tables
- optional `tikz` for workflows
- `fancyhdr` for short project/report headers

Use `assets/project-template/scripts/render_report.py` to convert Markdown to styled LaTeX/PDF when convenient.

## Environment Notes

`render_report.py` is intentionally tolerant — it produces a Markdown and a LaTeX file with whatever tooling is available — but the **PDF** step depends on a real local TeX environment. Check these before promising a PDF:

- **TeX engine**: `xelatex` (preferred) or `latexmk`. Without either, no PDF is produced.
- **Document class**: `ctexart` from the `ctex` package. Install via TeX Live (`tlmgr install ctex`) or MacTeX/MikTeX with Chinese support.
- **CJK fonts**:
  - macOS: PingFang, STSong, STHeiti — usually preinstalled.
  - Windows: 宋体 / 黑体 / 楷体 / 仿宋 — needed by `ctexart` defaults; install from a Chinese Windows or via Adobe Source Han.
  - Linux: `fonts-noto-cjk` (Debian/Ubuntu) or `noto-cjk` (Arch); rerun `fc-cache -fv` after install.
- **Pandoc** *(optional but recommended)*: enables high-fidelity Markdown→LaTeX conversion (tables, code blocks, citations). Without Pandoc, the script falls back to a conservative converter that only handles headings, lists, and paragraphs — complex tables and figures may need manual editing.

If any of the above is missing, do not silently skip — use the PDF status template in `workflow.md` "Final Response to User" so the user knows exactly what to install.

## Density Standard

For standard/deep reports, include:

- at least one positioning table
- at least one closest-work comparison table
- at least one dataset/study feasibility table
- at least one evaluation plan table
- at least one risk table
- 3-8 title candidates
- 1-3 abstract variants or one recommended abstract with alternatives

For quick reports, keep the same argumentative pattern but shorten the evidence layer.

