# Intake Question Script

Use this script when the user's opening message does not cover at least three of the four core intake fields (主题、目标 venue、深度、数据/研究类型). The goal is to collect enough context in **one consolidated turn** — never spread the questions across multiple back-and-forth replies, and never silently default.

This file gives the assistant two formats. Pick by runtime:

- **Format A: Markdown numbered list** — works on every platform (Claude Code, OpenAI Codex, web chat, plain CLI). Default choice unless you know the platform supports rich interactive prompts.
- **Format B: `AskUserQuestion` tool JSON** — Claude Code only. Use when the `AskUserQuestion` tool is available; it gives the user a card-style selector. Fall back to Format A on any other platform.

Detect the runtime once. If unsure, prefer Format A.

---

## Format A — Markdown Numbered List (cross-platform)

Send a single message that opens with one short framing line, then a numbered list. Each item must include the question, why it matters, and 2-3 candidate answers in parentheses. End with one instruction line so the user knows to answer once.

### Template

```
为了把调研做扎实，我先确认几件事，你可以一次性回答下面这些（不会的项可以写"待定"或者跳过）：

1. **研究主题 / 核心问题是什么？**（一两句话即可。例如："让 AI 帮高中物理老师在课堂上做概念诊断与决策支持"。）
2. **目标会议或期刊？**（CHI / LAK / L@S / AIED / EDM / CSCW / UIST / IJHCI / IJCAI / 教育研究类中文期刊 / 其他，可填多个。）
3. **想做多深的调研？**（`quick` ≈ 10-20 篇定方向 / `standard` ≈ 30-50 篇标准前期调研 / `deep` ≈ 80-120 篇完整文献网。默认 standard。）
4. **数据或研究类型？**（公开数据集 / 课堂真实数据 / 用户研究·访谈 / Wizard-of-Oz / 标注协议 / vignette / 待定。）

如果方便，再补充以下信息会更精准：

5. **年份范围**（默认近 5-7 年；老问题可放宽）
6. **必含关键词 / 必避关键词**（各列 2-5 个）
7. **是否已有 proposal / .tex / PDF / 笔记**（有就贴路径或粘贴正文）
8. **时间预算 / 截止时间**（决定要不要进 deep 模式）
9. **输出语言偏好**（默认中文报告，英文标题/摘要按需）

回答完后我会把这些写进 `config/topic_input.yaml`，再开始正式搜文献和写报告。
```

### When to skip a question

- If the user already provided that field in earlier messages, skip the item entirely and mention what you've taken from the prior message at the top.
- If the user has a PDF/proposal attached, skip questions 1-2 and instead ask the user to confirm the inferred topic and venue.
- Never list more than 9 items at once — if more context is needed, ask the first 9, then ask the rest after the first answer.

---

## Format B — `AskUserQuestion` JSON (Claude Code only)

Use the `AskUserQuestion` tool. Send **one call** containing 3-4 questions covering the core fields. Use the `header` field for chip labels and provide concrete option labels with short descriptions.

### Template

```json
{
  "questions": [
    {
      "question": "想做多深的调研？",
      "header": "深度",
      "multiSelect": false,
      "options": [
        {"label": "standard（30-50 篇）", "description": "标准前期调研，含文献图、可行性、标题/摘要、v2 报告（推荐）"},
        {"label": "quick（10-20 篇）", "description": "快速定方向 / 标题润色 / 短备忘"},
        {"label": "deep（80-120 篇）", "description": "系统化前期调研、广 venue 扫描、'100 篇'级别"}
      ]
    },
    {
      "question": "目标会议或期刊是哪类？",
      "header": "Venue",
      "multiSelect": true,
      "options": [
        {"label": "CHI / CSCW / UIST", "description": "HCI 主流"},
        {"label": "LAK / L@S / AIED / EDM", "description": "学习分析 / 教育技术 / AIED"},
        {"label": "IJHCI / IJCAI / NeurIPS", "description": "期刊或 AI 大会"},
        {"label": "中文期刊或会议", "description": "教育研究 / 远程教育 / 中国教育学刊 等"}
      ]
    },
    {
      "question": "数据或研究类型主要是哪种？",
      "header": "数据类型",
      "multiSelect": true,
      "options": [
        {"label": "公开数据集 / 基准", "description": "ACL/NeurIPS bench、Kaggle、Hugging Face、ICPSR …"},
        {"label": "课堂或现场真实数据", "description": "需要 IRB / 学校合作 / 田野收集"},
        {"label": "访谈 / Wizard-of-Oz / vignette", "description": "形成性研究 / 设计研究 / 模拟任务"},
        {"label": "标注协议 / 基准构建", "description": "贡献本身就是数据或评测集"}
      ]
    },
    {
      "question": "是否已有 proposal、PDF、.tex 或笔记？",
      "header": "已有材料",
      "multiSelect": false,
      "options": [
        {"label": "有，我接下来贴路径或正文", "description": "assistant 会先读你已有的材料，再开始搜补充文献"},
        {"label": "没有，从零开始", "description": "从主题描述开始构建 topic_lock 与文献网"}
      ]
    }
  ]
}
```

If `multiSelect: true` is used (Venue / 数据类型), make this explicit in any follow-up Markdown so the user knows they can pick more than one.

### Required fields covered

This 4-question set covers 深度 + venue + 数据类型 + 已有材料. The user's free-text "主题是什么" is captured separately — either inferred from the prior message, or asked as a single follow-up free-text question after the JSON above.

---

## After Intake

1. Write the answers into `config/topic_input.yaml`, replacing the `# 例如：...` placeholders.
2. If boundaries matter, also fill `config/topic_lock.yaml` and write `reports/00_topic_lock.md`.
3. Briefly summarize what you understood in 2-3 lines back to the user, then start the search.
4. Do not re-ask the same questions later in the conversation unless the user changes the topic.

## Anti-Patterns

- **Do not** ask one question, wait for the answer, then ask the next. Ask all 4-9 in one turn.
- **Do not** invent default values for `target_venue` or `field` — leave the YAML field as `TODO` if the user did not answer.
- **Do not** treat "标题润色" as a complete intake. Even title polishing needs target venue + intended message + evidence boundary.
- **Do not** start searching literature while waiting for the intake answer.
