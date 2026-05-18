---
name: academic-topic-research-agent
description: 中文默认的学术选题前置调研开发包，含 researcher-grade（CHI/CSCW 级）构念压力测试与 8 角批评-重写循环。Use when the user asks to develop a paper idea, research direction, title, abstract, LaTeX proposal, manuscript sketch, or CHI/CSCW/UIST/LAK/L@S/HCI/AIED/EDM/IJCAI/NeurIPS topic into a v2-style Chinese research-plan report — including 选题报告、开题报告、前期调研、调研开发、研究方向、学术选题、researcher-grade、深度打磨、构念压力测试、CHI 级、CSCW 转身、期刊投稿级, deep literature metadata collection, legal OA PDF handling, dataset/study feasibility, title polishing, abstract drafts, construct stress test + critique refinement loop, venue fit decision, and Markdown/LaTeX/PDF deliverables for supervisor review.
---

# Academic Topic Research Agent

## 中文快速上手

- **怎么调用**：直接告诉 assistant 你的研究想法（一句话也行），并加上"做一份调研报告"、"写一个 v2 风格的前期调研"、"帮我把选题做扎实"等触发语即可。
- **最少要给的信息**：研究主题/核心问题；目标会议或期刊；深度偏好（quick/standard/deep）。其它信息（年份、数据类型、必含/必避关键词、时间预算、已有 PDF）assistant 会主动追问。
- **你会拿到**：v2 风格中文调研报告（Markdown + LaTeX，本机有 TeX 时附 PDF）、3-8 个标题候选、1-3 段摘要候选、文献元数据矩阵、数据/研究可行性判定（Pass / Weak Pass / Fail）、下一步执行计划。
- **示例触发语**：`帮我把"用 AI 辅助高中物理老师做课堂决策"这个想法做成 CHI 风格的中文 v2 调研报告，standard 深度。`
- **想要 researcher-grade（CHI/CSCW 级）**：再加一句关键词，例如 `researcher-grade` / `深度打磨` / `构念压力测试` / `CHI 级` / `CSCW 转身` / `期刊投稿级`。`deep` 模式默认就是 researcher-grade。

## Researcher-Grade Mode

普通模式产出"OK 的调研方案"。Researcher-grade 模式产出"能直接进 CHI/CSCW 级讨论的方案"——它在 Modules A–E（调研+候选构造）之后，跑一段 **Module H：构念压力测试 + 8 角批评 + 重写循环 + venue fit 决策**，把候选写作阶段从"填 TODO 表格"推到"研究级构念"。

| 深度 | 行为 |
|---|---|
| `deep` | 默认开启。Module H 自动跑 **2 轮** critique → rewrite。14 元素全做。 |
| `standard` | 默认关。用户消息出现 `researcher-grade` / `深度打磨` / `构念压力测试` / `CHI 级` / `CSCW 转身` / `期刊投稿级` 时开启，Module H 跑 **1 轮**。14 元素做 11 项。 |
| `quick` | 跳过 Module H，但仍强制 1 张 **Neighbor Concept Differentiation Table**（3 行上限），写到 `drafts/contribution_candidates.md`。 |

Module H 检测 8 类结构性失败：headline 抢戏、构念是不是邻居概念换名、ladder 是不是偷偷压了多维、formative study 是 performance 还是 inquiry、ground-truth 是否稳定、部署成本是否被当背景隐藏、命名是否预埋答案、venue 是否人格分裂。每一角带 trigger / fail / fix，并在 ≤ 1 角失败时 early stop 避免假 critique 剧场。完整协议见 `references/construct_critique.md`；14 元素清单见 `references/researcher_grade_checklist.md`；venue 决策见 `references/venue_fit.md`（覆盖 CHI / CSCW / UIST / LAK / L@S / AIED / EDM / IJHCI / IJCAI / NeurIPS + 中文期刊代表）。

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

### Construct Stress Test and Critique Refinement Module (Module H)

- Run when researcher-grade mode is on (deep automatic; standard with keyword trigger).
- Read `references/construct_critique.md` (8 angles), `references/researcher_grade_checklist.md` (14 elements), `references/venue_fit.md` (full venue table).
- Produce `drafts/construct_stress_test.md`, `drafts/critique_round_<N>.md` (or `_passed.md`), `drafts/construct_rewrite_<N>.md`, `drafts/venue_fit_decision.md`.
- 2 passes for `deep`, 1 pass for `standard` (when triggered); skipped for `quick`.
- Pass condition: if ≤ 1 angle fails, early-stop and write `_passed.md` rather than fake-rewriting.
- If the rewrite changes scope, update `config/topic_lock.yaml` and append to `reports/05_topic_drift_warning.md`.

### Title and Abstract Module

- Generate 3-8 title candidates and 1-3 abstract variants when useful.
- Bind strong abstract claims to evidence or clearly frame them as proposed work.
- In researcher-grade mode, use the spine chosen in `construct_rewrite_<latest>.md` as the basis for every title candidate; fill the Headline Competition Audit table in `drafts/title_candidates.md`; fill the Construct/Differentiation/Quantified-Placeholder sentence fields in `drafts/abstract_candidates.md`.

### v2-Style Report Module

- Read `references/report_style.md`.
- Use `assets/report-blueprint/` as the minimal writing skeleton.
- Produce `reports/final_topic_report.md` and `reports/final_topic_report.tex`.
- Compile `reports/final_topic_report.pdf` only when a local TeX toolchain is available. See `references/report_style.md` "Environment Notes" for required components (xelatex + ctexart + CJK fonts; Pandoc optional).
- When a verdict memo is needed in addition to the full report, write `reports/06_final_recommendation.md` — a short advisor-facing decision page ("推进 / 收窄 / 重做" + 3-5 reasons).
- In researcher-grade mode, also integrate the 13 structural blocks from `assets/report-blueprint/v2_researcher_grade_extensions.md` (and `.tex` for LaTeX) using the integration map at the top of that file. Required elements per depth tier are listed in `references/researcher_grade_checklist.md`; missing required elements should be written as visible `TODO` lines.

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

- `references/workflow.md`: modular execution guide (includes Module H for researcher-grade mode).
- `references/intake_questions.md`: dual-format question script for the Intake Protocol.
- `references/search_protocol.md`: quick/standard/deep metadata and legal PDF protocol.
- `references/dataset_protocol.md`: dataset and study feasibility checks.
- `references/report_style.md`: v2-style Chinese report structure, writing preferences, and environment notes.
- `references/schemas.md`: configs, metadata matrices, evidence logs, and report artifacts.
- `references/evidence_rules.md`: claim safety and evidence labels.
- `references/construct_critique.md`: 8-angle critique protocol for Module H, with trigger/fail/fix per angle and early-stop pass condition.
- `references/researcher_grade_checklist.md`: 14 structural elements every researcher-grade final report must carry; tiered by depth.
- `references/venue_fit.md`: full venue decision tables for CHI / CSCW / UIST / LAK / L@S / AIED / EDM / IJHCI / IJCAI / NeurIPS plus Chinese journals; templates for `drafts/venue_fit_decision.md`.
- `assets/report-blueprint/`: copyable v2-style minimal Markdown/LaTeX report skeleton.
- `assets/report-blueprint/v2_researcher_grade_extensions.md` and `.tex`: 13 additive blocks appended to the v2 report when researcher-grade mode is on (opening thesis box, headline audit, reverse pitch, 3D operationalization, archetype table, neighbor differentiation, venue strategy, RQ matrix, alternative outcomes, deployment cost, reviewer attack, demand audit, elevator pitch); LaTeX includes tcolorbox macros (thesisbox/bluebox/redbox/greenbox).
- `assets/project-template/`: starter project structure.
- `assets/project-template/config/sources.yaml`: per-source on/off list — respect this when searching.
- `assets/project-template/config/tag_schema.example.yaml`: illustrative T-tag set; copy to `tag_schema.yaml` and customize before use.
- `assets/project-template/drafts/construct_stress_test.md`, `critique_round_{1,2}.md`, `construct_rewrite_{1,2}.md`, `venue_fit_decision.md`: Module H draft templates.
- `assets/project-template/scripts/render_report.py`: render Markdown to styled LaTeX/PDF.
- `assets/project-template/scripts/workflow_checklist.py`: inspect recommended artifacts by module (`python ... --list`).
