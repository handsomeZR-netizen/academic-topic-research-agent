# Academic Topic Research Agent

把一句话研究想法 → 一份能直接进 CHI/CSCW 级讨论的中文选题方案。

支持 Claude Code 和 OpenAI Codex 两个 runtime。默认输出中文 v2 风格报告（Markdown + LaTeX，本机有 TeX 时附 PDF），包含文献元数据矩阵、数据可行性判定（Pass / Weak Pass / Fail）、标题/摘要候选、研究设计、风险与时间表。

---

## 这个 skill 解决什么问题

普通的"帮我做调研"工作流给你一堆链接和一段总结。它告诉你**有什么**，但说不清这个方向在 CHI/CSCW 这个层面是否站得住——

- 你的核心构念是不是只是 mixed-initiative / abstention / appropriate reliance 的换名？
- 你列出的 C0–C3 ladder，到底是 1D 序列，还是偷偷塞了 3 个独立维度？
- 你的 formative study 列了 F1–F5 预期发现，每一个都会被验证——这是 inquiry 还是 performance？
- 你的评估靠专家标注 ground truth，但你的构念本身意味着上下文依赖——kappa 0.3 时怎么办？
- 你的部署声称 "low-disruption"，但每个 checkpoint 占用 8–15% 课堂时间——这成本进 limitation 还是进 findings？
- 你的系统名叫 `QuietProbe`——这名字预埋了答案，引入 demand characteristic。
- 你的论文同时强调可量化设计变量 AND 情境/质性现象——一句话说不出哪一批审稿人会最满意。

这些是参考案例 `ProbeMate_CalibratedDiagnosticCommitment_CHI_CSCW_rewrite.tex`（一个跨 4 轮 supervisor critique 才到位的方案）出现过的真实结构性失败。本 skill 把它们编码进了 **researcher-grade 模式**：8 角 critique 协议 + 14 元素结构检查 + 构念重写循环 + venue fit 决策。

---

## 两种模式

### 普通模式

给一句话想法，回一份中文 v2 调研报告。骨架：项目核心判断 / 为什么适合目标 venue / 与前人工作的差异 / 数据可行性 / 风险与时间表 / 投稿定位。

适用：导师下周要看的前期调研、临时被问到的方向初探、想知道某会议近 3 年的工作图谱。

### Researcher-Grade 模式

在普通模式之上，在候选写作阶段（标题/摘要/贡献/RQ/研究设计）之后、最终报告之前，插入 **Module H：构念压力测试 + 8 角批评 + 重写循环 + venue fit 决策**。

| 深度 | 行为 |
|---|---|
| `deep` | 默认开启。Module H 自动跑 **2 轮** critique → rewrite。14 元素结构清单全做。 |
| `standard` | 默认关。消息含关键词 `researcher-grade` / `深度打磨` / `构念压力测试` / `CHI 级` / `CSCW 转身` / `期刊投稿级` 时开启，Module H 跑 **1 轮**，14 元素做 11 项。 |
| `quick` | Module H 跳过，但 **Neighbor Concept Differentiation Table**（≥ 3 行）仍强制要求。 |

适用：CHI/CSCW/UIST/LAK/L@S/AIED/EDM/IJHCI 投稿；导师明确要求"做扎实再来"；构念听上去很厉害但说不清和 mixed-initiative / abstention 的区别。

---

## 8 角批评协议（Module H 的脊椎）

每轮 critique 跑这 8 角，每角带 trigger（怎么检测）/ fail（什么算失败）/ fix（怎么改）。完整协议见 `references/construct_critique.md`。

1. **Headline competition** — intro 和 contribution 里能数出几个互相抢戏的中心论点？
2. **Construct vs neighbor concepts** — 审稿人能不能说"这就是 [X] 换名"？区分是定义性还是维度性？
3. **Ladder vs design-space confusion** — 命名的 levels 是 1D 序列，还是偷偷压扁了多维？
4. **Formative study as performance vs inquiry** — 预期发现是否都正好确认设计？有没有可能推翻设计的发现？
5. **Ground-truth instability** — 评估是否依赖专家对类别标签达成一致？构念本身允许这种一致吗？
6. **Deployment cost hidden as feature** — 系统给课堂/工作增加了时间/工作量，但论文当 zero-cost？
7. **Demand characteristic in naming/framing** — 系统名/条件名/RQ 措辞是否预埋答案？
8. **Venue split-personality** — 能不能用一句话说哪一批审稿人会最满意？

**Pass condition：** ≤ 1 角失败时 early stop，避免假 critique 剧场。

---

## 14 元素结构检查清单（researcher-grade 报告的目标骨架）

完整说明见 `references/researcher_grade_checklist.md`。每元素都在 `ProbeMate_CalibratedDiagnosticCommitment_CHI_CSCW_rewrite.tex` 里有具体段落锚点。

1. **Opening Thesis Box** — 不是项目主题，是核心构念决定
2. **Headline Competition Audit** — 备选构念表 + 选谁作 spine 的理由
3. **Reverse Pitch ("It Is Not")** — 论文不是 [3 个 misreading]
4. **3D Construct Operationalization** — 维度 + 测量；非 1D ladder
5. **Archetype Table** — 设计空间的常见落点，不是 ground-truth class
6. **Neighbor Concept Differentiation Table** — ≥ 5 行邻居概念 + 维度差异（所有深度强制）
7. **Venue Strategy Table** — 主线 + 备选 + 鞋拔策略
8. **RQ Matrix** — 行=RQ，列=study/measure/evidence target/fail condition
9. **Study 1 Alternative Outcomes Table** — 能推翻或重塑设计的发现，不是预期发现
10. **Ground-Truth Stability Check** — pairwise preference + 分歧作为结果
11. **Deployment Cost as Finding + Two Scale Tiers** — 部署成本是发现不是 limitation
12. **Reviewer Attack Table** — 5–10 条预期 reviewer 攻击 + rebuttal + 哪节回应
13. **Demand Characteristic Audit** — 命名/条件/访谈措辞的预埋审计
14. **Elevator Pitch Box** — 一段话给导师的研究方向演讲

---

## Venue 覆盖

完整决策表见 `references/venue_fit.md`。每个 venue 给出：它最关心什么 / 它讨厌什么 / 本项目最强 fit 维度 / 主推线写法 / 备选 / 典型 reviewer attack / 必引文献骨架。

- **HCI 主流**：CHI / CSCW / UIST
- **学习分析 & 教育技术**：LAK / L@S / AIED / EDM
- **HCI 期刊**：IJHCI
- **AI 顶会**：IJCAI / NeurIPS
- **中文期刊**：教育研究 / 远程教育杂志 / 自动化学报 / 计算机学报 / 中国教育学刊

---

## 安装

### Claude Code

```bash
# 进到 Claude Code 的 skills 目录
cd ~/.claude/skills                     # macOS / Linux
# Windows: cd "$env:USERPROFILE\.claude\skills"

git clone https://github.com/handsomeZR-netizen/academic-topic-research-agent.git
```

下次启动 Claude Code 自动加载。然后直接对话：

```
我在琢磨一个方向，让 AI 帮高中物理老师在课堂上做概念诊断与决策支持，
想投 CHI，researcher-grade，deep 深度。
```

它会先停下来问 3–4 件事（确认主题 / venue / 数据 / 已有材料），你回答完才开始搜文献。Module H 在写完候选之后自动触发（deep 跑 2 轮 critique，standard 看关键词）。

### OpenAI Codex

同样 clone 法。仓库自带 `agents/openai.yaml`，Codex 会读它。`policy.allow_implicit_invocation: true` 表示触发词命中时会自动调用。

### PDF 编译（可选）

默认输出 Markdown + LaTeX。PDF 只在本机有 TeX 时编——需要 `xelatex` + `ctex` + 中文字体（macOS 自带；Windows 装宋体/黑体/楷体/仿宋；Linux 装 `fonts-noto-cjk`）。Pandoc 装上 Markdown → LaTeX 转换更精细，没装也能跑（会用一个保守的 fallback 转换器）。

环境缺东西时不会装作成功：

```
PDF 跳过：本机未检测到 xelatex / latexmk。Markdown 与 LaTeX 已生成，
可以在有 TeX 环境的机器上用 xelatex 编译。
```

---

## 三档深度

| 深度 | 文献数 | 适用 | Researcher-Grade |
|---|---:|---|---|
| `quick` | 10–20 | 临时方向初探；半小时内想知道"这方向坑在哪" | 跳过 critique loop；强制 1 张 neighbor-concept 表 |
| `standard` | 30–50 | 导师下周要看的前期调研（**默认**） | 关键词触发；1 轮 critique |
| `deep` | 80–120 | 开题报告、博士选题、完整文献网 | 默认开；2 轮 critique；14 元素全做 |

数量只是表面，质量阈值是 **至少 1/3 的文献达到 `keep` 或 `background` 级别**——纯 `candidate` 列表不算数。

---

## 不可编造红线

完整规则见 `references/evidence_rules.md`。要点：

- 不编造论文、DOI、数据集、引用、参与者数、指标、结果、部署或研究发现。
- 不把"看起来 plausible"的想法转化成 factual claim。
- 不声称 global novelty，除非检索范围本身支持这个声明。
- 不静默把主题改成更容易找数据的版本（`topic_lock.yaml` 锁定主题；偏移会写到 `reports/05_topic_drift_warning.md`）。
- 不下载付费 PDF。

新颖性声明的安全句式：

> 在本次检索范围和关键词策略下，已有工作覆盖了 [A] 和 [B]，但较少看到同时结合 [A]、[B]、[C] 并落在 [specific context] 的系统或研究设计。

---

## 目录结构

```
academic-topic-research-agent/
├── SKILL.md                                  # Claude Code 入口
├── agents/openai.yaml                        # OpenAI Codex 入口
├── references/                               # skill 操作手册
│   ├── workflow.md                           # 8 模块菜单（A–G + Module H researcher-grade）
│   ├── intake_questions.md                   # 主动询问脚本（双格式）
│   ├── search_protocol.md                    # 三档检索 + 法律 PDF 政策
│   ├── dataset_protocol.md                   # 数据可行性 Pass/Weak/Fail
│   ├── report_style.md                       # v2 风格 + 环境依赖 + researcher-grade 密度
│   ├── schemas.md                            # CSV/YAML/JSONL 模板
│   ├── evidence_rules.md                     # 不可编造红线
│   ├── construct_critique.md                 # 8 角 critique 协议 + 早停 pass condition
│   ├── researcher_grade_checklist.md         # 14 元素结构检查清单
│   └── venue_fit.md                          # CHI/CSCW/UIST/LAK/L@S/AIED/EDM/IJHCI/IJCAI/NeurIPS + 中文期刊决策表
└── assets/
    ├── report-blueprint/
    │   ├── v2_minimal_report.md              # 17 节最小骨架（含 Opening Thesis Box 槽）
    │   ├── v2_minimal_report.tex             # LaTeX 版本（thesisbox/keybox/warnbox 宏）
    │   ├── v2_researcher_grade_extensions.md # 13 块结构追加（researcher-grade 时叠加到 v2）
    │   └── v2_researcher_grade_extensions.tex # LaTeX 版本（thesisbox/bluebox/redbox/greenbox 宏 + ProbeMate-style 表格）
    └── project-template/                     # 用户项目目录模板
        ├── config/                           # topic_input / topic_lock / sources / tag_schema.example
        ├── data/processed/                   # CSV 输出
        ├── reports/                          # 00–06 阶段产物
        ├── drafts/                           # 候选与 Module H 模板
        │   ├── title_candidates.md           # 含 Headline Competition Audit + Demand Characteristic Risk
        │   ├── abstract_candidates.md        # 含 Construct/Differentiation/Quantified Placeholder 字段
        │   ├── contribution_candidates.md    # 含 Neighbor Concept Differentiation Table（所有深度强制）
        │   ├── experiment_plan.md            # 含 Alternative Outcomes / Ground-Truth Stability / Deployment Cost
        │   ├── construct_stress_test.md      # Module H 输入（6 张表）
        │   ├── critique_round_1.md           # 第 1 轮 critique（8 角）
        │   ├── construct_rewrite_1.md        # 第 1 轮重写快照
        │   ├── critique_round_2.md           # 第 2 轮（deep 用）
        │   ├── construct_rewrite_2.md        # 第 2 轮快照（deep 用）
        │   └── venue_fit_decision.md         # 主投/备选/鞋拔/reviewer attack
        └── scripts/
            ├── render_report.py              # Markdown → 风格化 LaTeX/PDF
            └── workflow_checklist.py         # `python ... --list` 检查每模块预期 artifacts
```

---

## 触发语示例

```text
# 普通模式
帮我把"用 LLM 辅助高中物理老师做课堂概念诊断"做成 v2 风格调研报告，standard 深度。

# Researcher-grade 模式（关键词触发）
同上但加 researcher-grade，目标 CHI 2027。

# 自动 researcher-grade（deep 自动开）
帮我做 deep 调研：用 AI 辅助教师在课堂中调节诊断承诺强度，目标 CHI/CSCW。

# Quick 模式 + 强制 neighbor-concept 表
quick 看下"AI 校准教师诊断承诺"方向，跟现有 mixed-initiative / appropriate reliance 区别。
```

---

## 不能干啥（承认一下）

- **不能替你判断**。能告诉你"这个方向 87 篇相关文献"和"构念压力测试结果"，但"值不值得做"是你的判断。
- **冷门方向会缩水**。如果你的主题就是只有 5 个人在做，deep 模式也搜不到 80 篇，会如实告诉你上限。
- **中文期刊覆盖一般**。默认开 OpenAlex / Crossref / DBLP / Semantic Scholar；CNKI / 万方默认关。可以在 `config/sources.yaml` 自己加，但加完得真能爬到。
- **不下载付费 PDF**。只下 OA 或用户提供的文件。
- **PDF 编译是可选的**。没装 TeX 只有 Markdown + LaTeX。
- **不让 Module H 假装跑**。≤ 1 角失败时 early stop 写 `_passed.md`，不为了"好看"硬凑 critique。

---

## License

MIT。随便用、随便改、随便做你自己学科的变体。
