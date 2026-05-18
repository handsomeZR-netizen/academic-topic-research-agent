# Venue Fit Reference

Use this file inside **Module H step H4** (venue fit decision) and whenever the user asks "我应该投哪个会/期刊？" or shows uncertainty between venues. The output of using this file is `drafts/venue_fit_decision.md` plus the **Venue Strategy Table** in the final report.

## How to Use

1. From the user's `topic_input.yaml` and the construct rewrite, identify the top 2 (occasionally 3) candidate venues.
2. For each candidate, locate its row below.
3. Build the comparison: which venue's reviewer would be **most enthusiastic** given the current evidence package? Which would be most enthusiastic if Study 4 thickens? Pick the primary; declare the secondary as pivot path.
4. Write `drafts/venue_fit_decision.md` using the template at the end of this file.

The single most important diagnostic: **say in one sentence which type of reviewer will be happiest**. If you cannot, you have venue split-personality (critique angle 8) and need to rewrite construct framing before picking.

---

## HCI Mainstream

### CHI (ACM CHI Conference on Human Factors in Computing Systems)

| 字段 | 内容 |
|---|---|
| 它最关心什么 | 原创 HCI 贡献——design construct, interaction technique, empirical insight, system + evaluation; novelty + significance + validity + research quality + presentation clarity. |
| 它讨厌什么 | "Engineering project re-decorated as research"; LLM 应用文; 无对照评估; vignette-only 的部署主张; missing limitations on construct generality. |
| 本项目最强 fit 维度 | Construct contribution + system + lab/quasi-controlled evaluation. |
| 主推线写法 | Construct as a measurable design space; show that varying construct policy changes user behavior in evaluable ways; ground in 1–2 anchor neighbor concepts (appropriate reliance, mixed-initiative). |
| 备选线 / 鞋拔策略 | If quantitative study is weak but field data is strong → pivot CSCW. If construct generality is weak → demote to "design exploration" with a venue-X note. |
| 典型 reviewer attack | (a) "Is this just X re-skinned?" — answer with neighbor differentiation table. (b) "Where's the controlled comparison?" — Study 2 + Study 3. (c) "Does this generalize beyond testbed?" — explicit scope statement in conclusion. |
| 必引文献骨架 | Amershi et al. (HAI Guidelines 2019); Bansal et al. (updates); Buçinca et al. (overreliance); Vasconcelos et al. (explanations); Horvitz (mixed-initiative); 1–2 domain anchors. |
| 投稿网址 | chi2027.acm.org (or current cycle) |

### CSCW (ACM Conference on Computer-Supported Cooperative Work)

| 字段 | 内容 |
|---|---|
| 它最关心什么 | 协作、组织、社会技术系统; 工作实践; appropriation; situated action; sociomateriality; institutional/policy context. |
| 它讨厌什么 | 纯 lab study without ecological grounding; 把 AI 写成 individual cognitive tool 而忽视 collaborative work; 系统性能为主的 paper; 对工作实践不敏感的设计断言. |
| 本项目最强 fit 维度 | Fieldwork + qualitative analysis of how people negotiate, resist, or transform AI suggestions; institutional constraint analysis. |
| 主推线写法 | Construct as situated accomplishment, not system property; sociomaterial framing; appropriation / resistance / silence as collaborative actions. |
| 备选线 / 鞋拔策略 | If Study 4 thin → cannot rescue. CSCW pivot only works when field data is the strongest part. |
| 典型 reviewer attack | (a) "Where's the work-practice grounding?" — Study 1 must be deep. (b) "Is this collaboration or single-user interaction?" — frame teacher-AI-student triadic. (c) "Generalization to other institutional contexts?" — explicit boundary on schools/disciplines. |
| 必引文献骨架 | Suchman (situated action); Bardzell (humanistic HCI); Holstein et al. (Lumilo, teacher complementarity); 1–2 work-practice / appropriation classics (Mackay 1990, Dourish 2003). |
| 投稿网址 | cscw.acm.org |

### UIST (ACM Symposium on User Interface Software and Technology)

| 字段 | 内容 |
|---|---|
| 它最关心什么 | 新颖交互技术、系统贡献、技术实现 + 用户研究; novel input/output, novel interaction, novel system; technical depth + user study. |
| 它讨厌什么 | 纯 design space paper without working system; nothing new about the technique itself; no technical implementation novelty. |
| 本项目最强 fit 维度 | If the construct realization requires novel interaction primitives (new card UI, novel multimodal input, novel disclosure timing). |
| 主推线写法 | System and technique first; construct serves as the design rationale; small-N controlled user study validates technique. |
| 备选线 / 鞋拔策略 | If technique is incremental → not a UIST fit; pivot CHI. |
| 典型 reviewer attack | (a) "What's technically new?" — must answer concretely. (b) "Did you compare against the obvious baseline interaction?" — yes, as an ablation. |
| 必引文献骨架 | Closest UIST priors on similar interaction class; mixed-initiative + suggestion-timing classics. |
| 投稿网址 | uist.acm.org |

---

## Learning Analytics / Educational Technology

### LAK (Learning Analytics & Knowledge Conference)

| 字段 | 内容 |
|---|---|
| 它最关心什么 | Educationally grounded analytic methods; learning data; actionable insights for learners/teachers/institutions. |
| 它讨厌什么 | HCI design papers with no learning theory; analytics without educational grounding; "we have data, what do we do with it" papers. |
| 本项目最强 fit 维度 | Teacher-facing analytics; conceptual diagnostic; classroom data analysis. |
| 主推线写法 | Frame construct in terms of learning theory anchors (conceptual change, productive talk, formative assessment); the analytic dimension matters. |
| 备选线 / 鞋拔策略 | If pure HCI design without analytic novelty → pivot CHI. |
| 典型 reviewer attack | (a) "Which learning theory grounds this?" — must answer concretely. (b) "What's the analytic novelty?" — not just LLM wrapper. (c) "Does it improve learning?" — even if you can't prove, defend why this is a stepping-stone. |
| 必引文献骨架 | Suresh et al. (TalkMoves); Holstein et al. (Lumilo / teacher complementarity); Buckingham Shum (LAK foundational); domain learning theory (diSessa / Chi / Vosniadou for physics). |
| 投稿网址 | solaresearch.org/events/lak |

### L@S (ACM Conference on Learning at Scale)

| 字段 | 内容 |
|---|---|
| 它最关心什么 | Scalable learning environments — MOOCs, large classrooms, online tutoring; large-N empirical work; intervention studies at scale. |
| 它讨厌什么 | Small-N qualitative studies (less typical fit, not impossible); HCI papers with no scale story. |
| 本项目最强 fit 维度 | If the construct supports scaling teacher attention across many students or many classrooms. |
| 主推线写法 | Construct enables teacher-scale or classroom-scale leverage; quantify the scale gain. |
| 备选线 / 鞋拔策略 | If sample is small (12–16 teachers) → L@S may reject for scale; pivot LAK or CHI. |
| 典型 reviewer attack | (a) "What's the scale story?" (b) "Does it generalize across N students/teachers/classrooms?" |
| 必引文献骨架 | Koedinger et al. (intelligent tutoring); MOOCs literature; teacher-scale L@S priors. |
| 投稿网址 | learningatscale.acm.org |

### AIED (International Conference on Artificial Intelligence in Education)

| 字段 | 内容 |
|---|---|
| 它最关心什么 | AI methods applied to education; intelligent tutoring; learner modeling; educationally meaningful AI; ITS, dialogue systems, NLP-for-education. |
| 它讨厌什么 | HCI design with no learner-modeling or AI-method contribution; superficial LLM applications. |
| 本项目最强 fit 维度 | If construct is operationalized as a learner/teacher model with measurable AI behavior. |
| 主推线写法 | Construct = AI behavior policy; learner-state modeling; system architecture; controlled evaluation. |
| 备选线 / 鞋拔策略 | If HCI is the spine and AI method is incremental → pivot CHI. |
| 典型 reviewer attack | (a) "What's the AI contribution?" (b) "How does the learner model work?" (c) "Compared to ITS baselines?" |
| 必引文献骨架 | VanLehn (ITS); Heffernan (ASSISTments); recent AIED on LLMs in education. |
| 投稿网址 | aied.org |

### EDM (Educational Data Mining)

| 字段 | 内容 |
|---|---|
| 它最关心什么 | Data-mining and analytic methods on educational data; predictive modeling; knowledge tracing; sequence analysis. |
| 它讨厌什么 | Pure design / HCI papers; small-N qualitative; no data-mining method contribution. |
| 本项目最强 fit 维度 | If construct is operationalized as a predictive task on classroom/log data. |
| 主推线写法 | Predictive modeling / sequence analysis of teacher decisions or student responses; method evaluation on benchmark or own data. |
| 备选线 / 鞋拔策略 | Usually not the right home for construct-design HCI work. |
| 典型 reviewer attack | (a) "What's the method?" (b) "Compared to baselines on what dataset?" |
| 必引文献骨架 | Knowledge tracing literature; recent EDM benchmarks; sequence-modeling priors. |
| 投稿网址 | educationaldatamining.org |

---

## HCI / AI Journals

### IJHCI (International Journal of Human-Computer Interaction) / IJHCS

| 字段 | 内容 |
|---|---|
| 它最关心什么 | Comprehensive HCI research; longer-form treatment; deeper empirical work; theory-grounded contributions. |
| 它讨厌什么 | Conference-paper-thin treatment of complex topics; rushed empirical work. |
| 本项目最强 fit 维度 | If you have a full multi-study program with thicker analysis than CHI 10 pages would allow. |
| 主推线写法 | Multi-study program; construct + system + evaluation + field deployment + theoretical synthesis. |
| 备选线 / 鞋拔策略 | If only 1–2 studies done → conference first. |
| 典型 reviewer attack | (a) "What does the journal version add beyond a conference paper?" |
| 必引文献骨架 | Same anchors as CHI/CSCW plus deeper theoretical references. |
| 投稿网址 | tandfonline.com/toc/hihc20 |

### IJCAI (International Joint Conference on Artificial Intelligence)

| 字段 | 内容 |
|---|---|
| 它最关心什么 | AI method contributions across subfields; algorithmic novelty; principled evaluation. |
| 它讨厌什么 | HCI design papers without AI method; application papers without method contribution. |
| 本项目最强 fit 维度 | Only if the construct is realized via a non-trivial AI method (calibration learning, multi-objective decision-making, novel uncertainty modeling). |
| 主推线写法 | Method first; HCI motivation framed as constraint; benchmark or simulation evaluation. |
| 备选线 / 鞋拔策略 | Usually not the right home for HCI-spine work; pivot CHI/UIST. |
| 必引文献骨架 | Algorithmic priors on the specific AI method; selective prediction / calibration / decision-theoretic foundations. |
| 投稿网址 | ijcai.org |

### NeurIPS (Conference on Neural Information Processing Systems)

| 字段 | 内容 |
|---|---|
| 它最关心什么 | ML method contributions; theory; benchmarks; algorithmic novelty. |
| 它讨厌什么 | HCI design papers; application studies; small-N user studies. |
| 本项目最强 fit 维度 | Rarely a fit for teacher-facing HCI projects; possibly a fit if a dataset / benchmark contribution exists. |
| 主推线写法 | Benchmark / dataset / method contribution; HCI motivation in intro only. |
| 备选线 / 鞋拔策略 | Not the right home for design-construct papers. |
| 必引文献骨架 | ML benchmark / calibration / human-in-the-loop priors. |
| 投稿网址 | neurips.cc |

---

## Chinese Journals (中文期刊)

For Chinese authors / supervisors who want a Chinese-venue path, or for projects where the audience is the Chinese education research community.

### 教育研究

| 字段 | 内容 |
|---|---|
| 它最关心什么 | 中国教育系统、政策、改革背景下的教育研究; 教师/学生/学校层面的实证; 教育公平; 课程改革; 教师专业发展。 |
| 它讨厌什么 | 纯技术导向; 缺少教育学理论框架; 无中国教育语境讨论。 |
| 本项目最强 fit 维度 | 若 Study 4 在中国课堂场景做实, 且讨论教师专业发展、课堂教学改革。 |
| 主推线写法 | 教师专业判断 + 课堂教学改革 + 教育公平视角; AI 作为辅助工具不是主角。 |
| 备选线 / 鞋拔策略 | 若构念过偏 HCI 设计 → 转 远程教育 或 中国教育学刊. |
| 必引文献骨架 | 中国课堂研究经典 (顾泠沅, 叶澜); 教师专业发展文献; 学科教学论。 |

### 远程教育杂志 / 中国远程教育

| 字段 | 内容 |
|---|---|
| 它最关心什么 | 教育技术、在线学习、混合学习、学习分析; AI 在教育中的应用; 智慧教育。 |
| 它讨厌什么 | 与教育技术无关; 纯 HCI 论文。 |
| 本项目最强 fit 维度 | AI 辅助教学、学习分析、教师决策支持。 |
| 主推线写法 | 教育技术 + AI for education + 教师赋能。 |
| 必引文献骨架 | 国内教育技术经典; 智慧教育文献; 国际 AIED / LAK 选引。 |

### 自动化学报 / 计算机学报

| 字段 | 内容 |
|---|---|
| 它最关心什么 | 自动化 / 计算机方法贡献; 算法、系统、应用。 |
| 它讨厌什么 | 应用为主、方法不深; 没有形式化表述。 |
| 本项目最强 fit 维度 | 若构念落实到非平凡 AI 方法 (calibration, uncertainty, dialogue policy)。 |
| 主推线写法 | 方法贡献 + 应用场景验证; 教育场景作 evaluation testbed。 |
| 必引文献骨架 | 国内计算机/AI 主流方法; 国际相关方法对比. |

### 中国教育学刊 / 课程·教材·教法

| 字段 | 内容 |
|---|---|
| 它最关心什么 | 课程与教学论; 学科教学; 教育政策; 教师教育; 教学法实证。 |
| 它讨厌什么 | 技术为主; 缺乏教学法理论。 |
| 本项目最强 fit 维度 | 若 Study 1 + Study 4 偏教学法分析。 |
| 主推线写法 | 学科教学论 (例如物理教学论) + 教师决策 + 概念教学; AI 作为新工具讨论。 |
| 必引文献骨架 | 学科教学论经典; 概念转变与误概念国内文献; 教师认知与决策。 |

---

## `drafts/venue_fit_decision.md` Template

Use this exact structure:

```markdown
# Venue Fit Decision

Decision date: <date>
Construct version: round <N>

## Top-line decision

主投：[Venue]
备选：[Venue B] (pivot path)
理由 (one sentence)：[which reviewer is happiest, and why now].

## Venue Strategy Table

| 路线 | 主贡献写法 | 研究重心 |
|---|---|---|
| [Primary venue] | [framing] | [study emphasis] |
| [Pivot venue] | [framing] | [study emphasis] |

## Per-Study Rewrite Implications

For the primary venue:

| Study | 现在的写法 | 需要调整 |
|---|---|---|
| Study 1 | ... | ... |
| Study 2 | ... | ... |
| Study 3 | ... | ... |
| Study 4 | ... | ... |

For the pivot venue (deferred but possible):

| Study | 如何转 | 触发条件 |
|---|---|---|
| Study X | ... | ... |

## Reviewer Attack Table (for primary venue)

| 攻击点 | 审稿人可能怎么说 | 论文里如何预防 |
|---|---|---|
| ... | ... | ... |
| ... | ... | ... |
| ... (≥5 rows for deep, ≥3 for standard) | ... | ... |

## Anchor Citations

Primary venue must-cite skeleton (3–5):
- ...
- ...
- ...

## Pivot Trigger

If [specific data outcome], collapse to pivot venue; the trigger condition must be stated up-front so the writer can recognize it at Study 4 analysis time without rationalizing.
```

## Anti-Patterns

- **Do not** pick a venue based on which has the latest deadline.
- **Do not** pick two venues "in parallel"; that is venue split-personality, not strategy.
- **Do not** invent venue-fit reasons not grounded in the venue's actual call for papers.
- **Do not** ignore Chinese journals when the author/audience would actually benefit; this is a frequent oversight in HCI-first thinking.
- **Do not** assume the primary venue is the one with the highest impact factor — it is the one whose reviewers will be **happiest** with the current evidence package.
