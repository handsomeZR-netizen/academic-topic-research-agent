---
name: academic-topic-research-agent
description: 中文默认的学术选题前置调研开发包。Use when the user asks to develop a paper idea, research direction, title, abstract, LaTeX proposal, manuscript sketch, or CHI/LAK/L@S/HCI/AIED/EDM topic into a v2-style Chinese research-plan report — including 选题报告、开题报告、前期调研、调研开发、研究方向、学术选题, deep literature metadata collection, legal OA PDF handling, dataset/study feasibility, title polishing, abstract drafts, and Markdown/LaTeX/PDF deliverables for supervisor review.
---

# Academic Topic Research Agent

## 中文快速上手

- **怎么调用**：直接告诉 assistant 你的研究想法（一句话也行），并加上"做一份调研报告"、"写一个 v2 风格的前期调研"、"帮我把选题做扎实"等触发语即可。
- **最少要给的信息**：研究主题/核心问题；目标会议或期刊；深度偏好（quick/standard/deep）。其它信息（年份、数据类型、必含/必避关键词、时间预算、已有 PDF）assistant 会主动追问。
- **你会拿到**：v2 风格中文调研报告（Markdown + LaTeX，本机有 TeX 时附 PDF）、3-8 个标题候选、1-3 段摘要候选、文献元数据矩阵、数据/研究可行性判定（Pass / Weak Pass / Fail）、下一步执行计划。
- **示例触发语**：`帮我把"用 AI 辅助高中物理老师做课堂决策"这个想法做成 CHI 风格的中文 v2 调研报告，standard 深度。`

## Core Contract

Use this skill as a **research development kit**, not a closed or rigid workflow. The skill provides a reusable report skeleton, evidence standards, search depth presets, and optional modules. The assistant should choose and combine modules according to the user's goal, source material, time budget, and available tools.

Default to **Chinese final outputs** unless the user explicitly requests English. Keep paper titles, venue names, keywords, and optional academic abstract variants in English when useful.

Never fabricate papers, datasets, citations, participant counts, metrics, results, PDF files, or study findings. Record uncertain material as `Unknown`, `TODO`, or `Requires Manual Verification`.

## Platform Targets

This skill is intentionally dual-target:

- **Claude Code** reads only `SKILL.md` (this file) and the `references/` and `assets/` it points to.
- **OpenAI Codex** reads `agents/openai.yaml` for `display_name`, `short_description`, `default_prompt`, and `policy.allow_implicit_invocation`.

When editing this skill, keep the `name` field and the core capability summary in sync between `SKILL.md` (here) and `agents/openai.yaml`. Platform-specific files (`agents/openai.yaml`) may retain platform-specific wording; the shared assistant-facing docs in `references/` and `SKILL.md` should stay platform-neutral and say "the assistant" rather than naming a specific runtime.

## Intake Protocol

Before searching literature, downloading PDFs, or writing any report section, **make sure you have enough input from the user**. If the user's first message does not cover at least three of the following four core fields, **pause and ask them in one consolidated turn** — do not silently guess defaults and start searching.

Core intake fields:

1. **研究主题或核心问题** — what the project is actually about.
2. **目标会议或期刊** — venue family (CHI, LAK, L@S, AIED, EDM, CSCW, UIST, IJHCI, IJCAI, …) or journal.
3. **深度偏好** — `quick` / `standard` / `deep` (default `standard` when unclear).
4. **数据或研究类型** — public benchmark, classroom data, interview/Wizard-of-Oz, annotation, simulated vignette, etc.

Strongly-recommended follow-up fields (ask in the same turn when natural):

- 年份范围 (default last 5-7 years for fast-moving venues)
- 必含关键词 / 必避关键词
- 是否已有 proposal / .tex / PDF / 笔记
- 时间预算 (decides whether to run `deep` mode)
- 输出语言偏好 (default 中文)

Use `references/intake_questions.md` for the exact question script. It provides both a Markdown-numbered-list version (works on any platform) and an `AskUserQuestion` JSON version (Claude Code only). Pick the format that matches your runtime.

After the user answers, immediately write `config/topic_input.yaml` and (when boundaries matter) `config/topic_lock.yaml`. For quick tasks, embedding the lock as an in-report section is acceptable.

## Depth Presets

Choose a depth before searching. If the user does not specify depth, default to `standard`.

- `quick`: 10-20 candidate papers/systems/datasets. Use for rapid direction checks, title polishing, and short advisor memos.
- `standard`: 30-50 candidate metadata records. Use for normal pre-research packages with literature map, dataset feasibility, title/abstract drafts, and v2-style report.
- `deep`: 80-120 candidate metadata records. Use when the user asks for deep research, systematic preparation, "100 papers", "100 PDFs metadata", "完整前期调研", or broad venue mapping.

For `deep`, collect metadata and OA PDF URLs first. Download only legally available open-access PDFs or user-provided PDFs. Do not treat downloading 100 PDF files as mandatory.

Quality threshold (not just count): a depth target is met only when **at least ⅓ of records reach `keep` or `background` screening status**. Fifty `candidate`-only rows do not satisfy `standard`.

## Composable Modules

Use modules flexibly. A deep task usually uses most modules; a quick task may use only a few.

### Intent and Boundary Module

- Read user-provided title, proposal, `.tex`, notes, or PDF.
- Run the Intake Protocol above when input is thin.
- Preserve the user's original research intent.
- Create `config/topic_lock.yaml` and/or a concise topic-lock section only when it helps prevent drift.
- If later search/design clearly deviates from `topic_lock.yaml`, write `reports/05_topic_drift_warning.md` flagging the deviation before continuing.

### Literature Metadata Module

- Read `references/search_protocol.md` and respect `config/sources.yaml` (only use sources with `enabled: true`).
- Build query groups and collect paper/system metadata at the selected depth.
- Write or update `data/processed/paper_matrix.csv` or `data/processed/metadata_candidates.csv`.
- Record key queries and evidence decisions in `logs/evidence_trace.jsonl`.
- Optional: copy `config/tag_schema.example.yaml` to `config/tag_schema.yaml` and replace the example T-tags with topic-specific ones before bulk coding.

### Dataset and Study Feasibility Module

- Read `references/dataset_protocol.md`.
- Search real public datasets, benchmarks, repositories, dataset papers, and study alternatives.
- Write `data/processed/dataset_candidates.csv` for standard/deep tasks.
- Classify feasibility as `Pass`, `Weak Pass`, or `Fail` when the user needs a decision.

### Research Design Module

- Turn evidence into research questions, contribution candidates, system/method scope, user study or experiment plan, risk table, and next steps.
- Keep model/data claims separate from user-facing or venue-facing contribution claims.

### Title and Abstract Module

- Generate 3-8 title candidates and 1-3 abstract variants when useful.
- Bind strong abstract claims to evidence or clearly frame them as proposed work.

### v2-Style Report Module

- Read `references/report_style.md`.
- Use `assets/report-blueprint/` as the minimal writing skeleton.
- Produce `reports/final_topic_report.md` and `reports/final_topic_report.tex`.
- Compile `reports/final_topic_report.pdf` only when a local TeX toolchain is available. See `references/report_style.md` "Environment Notes" for required components (xelatex + ctexart + CJK fonts; Pandoc optional).
- When a verdict memo is needed in addition to the full report, write `reports/06_final_recommendation.md` — a short advisor-facing decision page ("推进 / 收窄 / 重做" + 3-5 reasons).

## Final Output Standard

For a full package, produce:

- v2-style Chinese research-plan report in Markdown and LaTeX.
- PDF only when local TeX tooling exists.
- title polishing options.
- abstract candidate(s).
- metadata matrix or evidence table appropriate to the selected depth.
- dataset/study feasibility judgment.
- next-step plan and unsafe-claim list.

The final report should feel like `网页版个人调研/v2.tex`: strong core judgment, concrete examples, prior-work positioning, data feasibility, research design, risks, and a practical timeline. The section skeleton is a starting point, not a cage. Merge, rename, or omit sections when the topic demands it, as long as the final report still explains the research direction clearly.

## Resource Map

- `references/workflow.md`: modular execution guide.
- `references/intake_questions.md`: dual-format question script for the Intake Protocol.
- `references/search_protocol.md`: quick/standard/deep metadata and legal PDF protocol.
- `references/dataset_protocol.md`: dataset and study feasibility checks.
- `references/report_style.md`: v2-style Chinese report structure, writing preferences, and environment notes.
- `references/schemas.md`: configs, metadata matrices, evidence logs, and report artifacts.
- `references/evidence_rules.md`: claim safety and evidence labels.
- `assets/report-blueprint/`: copyable v2-style minimal Markdown/LaTeX report skeleton.
- `assets/project-template/`: starter project structure.
- `assets/project-template/config/sources.yaml`: per-source on/off list — respect this when searching.
- `assets/project-template/config/tag_schema.example.yaml`: illustrative T-tag set; copy to `tag_schema.yaml` and customize before use.
- `assets/project-template/scripts/render_report.py`: render Markdown to styled LaTeX/PDF.
- `assets/project-template/scripts/workflow_checklist.py`: inspect recommended artifacts by module (`python ... --list`).
