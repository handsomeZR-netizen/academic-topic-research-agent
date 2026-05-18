# Construct Critique Protocol

Use this protocol inside **Module H: Construct Stress Test & Critique Refinement Loop**. It encodes the supervisor-style critique that turns an OK research package into a researcher-grade one. The reference case is `参考案例.md` (the 4-round dialogue) and the final deliverable `ProbeMate_CalibratedDiagnosticCommitment_CHI_CSCW_rewrite.tex`.

The point of this file is not to "make the report look critical." It is to detect specific structural failure modes that distinguish a CHI/CSCW-strong proposal from "an engineering project re-decorated as research."

## When to Run

| Depth | Behavior |
|---|---|
| `deep` | Run automatically. N = 2 critique → rewrite passes. |
| `standard` | Run only if user message contains a trigger keyword: `researcher-grade` / `深度打磨` / `构念压力测试` / `CHI 级` / `CSCW 转身` / `期刊投稿级`. N = 1 pass. |
| `quick` | Skip the full loop, but still produce a **3-row** Neighbor Concept Differentiation table inside `contribution_candidates.md`. |

If the user explicitly says "skip critique" or "don't pressure-test," obey that and write a single-line note in `construct_stress_test.md` recording the user-requested skip.

## Loop Structure

```
H1. Write drafts/construct_stress_test.md
    (this is the input to critique; it captures the current construct package)

H2. Run critique_round_<N>.md (8 angles)
    For each angle: trigger / fail / fix.
    Count failing angles.

    If failing_angles <= 1:
      Write drafts/critique_round_<N>_passed.md
        with the one borderline angle and a "no rewrite needed" note.
      Jump to H4.
    Else:
      Continue to H3.

H3. Write drafts/construct_rewrite_<N>.md
    A snapshot of the rewritten title / construct definition / RQ matrix
    / study designs that responds to every failing angle.

    If the rewrite changes the core construct or topic scope:
      Update config/topic_lock.yaml.
      Append a row to reports/05_topic_drift_warning.md citing which
      critique angle fired and quoting the before/after.

    If N == 2: loop back to H2 with critique_round_2.md.

H4. Write drafts/venue_fit_decision.md (the final venue choice + pivot plan).

H5. Hand off to Module F (title/abstract) and Module G (v2 report);
    every artifact they produce MUST be consistent with the H4 rewrite.
```

## The 8 Critique Angles

Each angle below uses this exact shape: **Trigger** (how to detect this might apply), **Fail indicator** (what specifically counts as a fail — must be concrete enough to quote a passage from the draft), **Fix pattern** (the structural rewrite), **Reference-case anchor** (where this angle fired in the ProbeMate dialogue), **Critique entry template** (the literal sentence to write into `critique_round_<N>.md`).

---

### Angle 1 — Headline Competition

**Trigger.** Read the intro plus the contribution list. Count how many distinct "central claims" you can extract — each one a sentence of the form "this paper is about X."

**Fail indicator.** ≥ 2 central claims compete for the title slot. Common patterns: a work-practice claim, a construct claim, a design-philosophy claim, and a design-pattern claim all sitting at the same level. A reader at the end of the second read cannot answer "what should I remember from this paper?"

**Fix pattern.** Pick the sharpest claim — the one with reverse intuition, broadest pull, and tightest evidence. Demote the others to **mechanism**, **operationalization**, or **evidence** layers below the headline. The spine of the paper becomes the chosen claim; the other claims become its supporting tissue.

**Reference-case anchor.** Round 1 of `参考案例.md`: "你有 3-4 个候选 headline 在抢同一个标题" — Next-turn agency / Calibrated Conceptual Micro-Probing / When-should-classroom-AI-stay-silent / 三道门-五类状态. The supervisor picks the third as the spine.

**Critique entry template.** `Found ≥ 2 competing headlines: [headline A] (currently in §X) and [headline B] (currently in §Y). They are not compatible — A is a [work-practice / construct / pattern / philosophy] claim, B is a [...] claim. Recommend collapsing to A because [reason]; demote B to [mechanism / operationalization / evidence] layer.`

---

### Angle 2 — Construct vs Neighbor Concepts

**Trigger.** Read the construct definition. Ask: could a reviewer say "this is just X re-skinned" for any of {mixed-initiative interaction, abstention / reject-option, selective prediction, progressive disclosure, appropriate reliance, proactive AI, staged disclosure, calibrated confidence, scaffolding, adaptive feedback}?

**Fail indicator.** The differentiation is **definitional** ("our construct cares about Y") not **dimensional** ("our construct has axes that X cannot capture"). If you cannot point to a specific design configuration that your construct identifies and X cannot, the construct is repackaged.

**Fix pattern.** Build an explicit **Neighbor Concept Differentiation Table** with ≥ 5 rows. Each row: neighbor concept / what it primarily captures / which dimension(s) of our construct it cannot reach / concrete example design configuration we can describe and it cannot.

**Reference-case anchor.** Round 3: "commitment 这个 construct 还没真正区别于已有概念" — the supervisor lists mixed-initiative, proactive vs reactive, staged disclosure, progressive disclosure, Amershi Guideline #3. Forces the rewrite to add the differentiation table.

**Critique entry template.** `Construct [name] reads as a re-skin of [neighbor]. The current draft differentiates by [quoted phrase], which is definitional. Need a dimensional differentiation: show one design configuration this construct captures that [neighbor] cannot. Suggested neighbor row: [neighbor] — [primary capture] — [missed dimension].`

---

### Angle 3 — Ladder vs Design-Space Confusion

**Trigger.** Does the construct have named levels (C0–C3, low/med/high, weak/medium/strong)? Look at what each level varies.

**Fail indicator.** The "ladder" silently mixes ≥ 2 independent axes. For example: C0 is "whether the system speaks at all," C1 is "what kind of utterance," C2 is "how strong the utterance," and C3 is "how directive the utterance." Those are three orthogonal axes wearing one label. A reviewer will say "C0 to C3 is not one ordinal scale."

**Fix pattern.** Promote to an **N-dimensional design space**. Rewrite each axis as its own variable (E, V, D, …). Demote the named levels to **archetypes** — common, named points in the space — and explicitly say they are not exhaustive, not ordinal, and not ground-truth classes.

**Reference-case anchor.** Round 3: "C0--C3 不是一个由低到高的单一序列…审稿人会戳这一点。" Round 4 rewrites commitment as `(E, V, D)` 3D space with C0–C3 as archetypes only.

**Critique entry template.** `Ladder [name] with levels [list] silently compresses [N] independent axes: [axis A], [axis B], [axis C]. Promote to N-D design space; archetype the levels; explicitly state in the construct definition section that the levels are not ordinal.`

---

### Angle 4 — Formative Study as Performance vs Inquiry

**Trigger.** Read the formative-study section (Study 1 in most CHI-style proposals). Look for "expected findings," "anticipated themes," "we expect to find F1–F5," or any structure where each predicted finding maps 1:1 to a design feature.

**Fail indicator.** The predicted findings cannot fail. A skilled reader can see "if interviewees answer the leading questions plausibly, every F will be confirmed, and the design needs are validated." This is confirmation theater, not inquiry.

**Fix pattern.** Replace the predicted-findings section with an **Alternative Outcomes Table**: rows are findings that would **falsify or reshape** the design. Each row: possible finding / how it would refute or remix the proposal / specific design response. Examples from ProbeMate: teachers want AI more confident (not less); silence is always unacceptable; novices and experts have inverted preferences; written checkpoints are too costly.

**Reference-case anchor.** Round 2: "F1–F5 几乎都会被验证…把 §5.6 重写成 'alternative outcomes that would falsify or reshape the design space'." Round 3 implements this with a 7-row table.

**Critique entry template.** `Study 1 lists [N] predicted findings (F1–F[N]) that all confirm the proposed design. This is performance, not inquiry. Replace with an Alternative Outcomes Table covering at least [3 if standard / 5 if deep] findings that would refute or remix the design — including the strongest plausible "design is wrong" outcome.`

---

### Angle 5 — Ground-Truth Instability

**Trigger.** Read the evaluation-study section. Is the main metric expert-labeled classification accuracy, macro-F1, kappa, or any agreement-based score over a categorical label?

**Fail indicator.** The construct itself implies the right answer is context-dependent (depends on teaching stage, student background, classroom pacing, prior turns, etc.). If the construct's own theory says "no single ground-truth label exists," then forcing expert agreement on labels is incoherent. Expected kappa will be low; reviewers will say the ground truth is unstable.

**Fix pattern.** Switch the main evaluation to **pairwise preference**. Experts compare two system outputs and pick which is more appropriate. Aggregate with Bradley-Terry or Thurstone. Reframe **expert disagreement as result** — segment the data into high-consensus / structured-disagreement / no-consensus zones; argue the no-consensus zone is exactly where the construct predicts AI should hedge.

**Reference-case anchor.** Round 2: "kappa 大概率会非常低…把 inter-rater disagreement 本身当结果." Round 3 implements pairwise + disagreement analysis.

**Critique entry template.** `Evaluation hinges on expert agreement about a categorical label ([label name]). The construct itself implies the right answer is context-dependent on [factor list]. Switch primary metric to pairwise preference; reframe disagreement as result; keep classification accuracy as secondary technical metric only.`

---

### Angle 6 — Deployment Cost Hidden as Feature

**Trigger.** Read any deployment / classroom / field-study section. Look for phrases like "seamless," "low-disruption," "non-intrusive," "lightweight," combined with system steps that take real time, labor, or infrastructure (written student responses, polling devices, teacher review time, IRB processes, school coordination).

**Fail indicator.** The paper presents deployment cost as zero. Quick arithmetic shows it isn't (e.g., 2-minute checkpoints × 3 per lesson = 6/45 = 13% of class time). The reader notices the gap; the reviewer rejects on ecological validity.

**Fix pattern.** Promote cost to **Deployment Cost as Finding**. Write the trade-offs explicitly in the deployment section. Provide **two scale tiers** — a CHI-strong-evaluation tier (smaller deployment, tighter measurement) and a CSCW-thick-description tier (bigger deployment, qualitative depth). Make the cost itself a research contribution: "Inserting written checkpoints reshapes the classroom rhythm; that reshaping is part of what we study."

**Reference-case anchor.** Round 2: "你把课的 8–15% 时间让渡给了系统。这不是'低打断'，这是改造了课堂结构." Round 3 admits the cost and frames the reshape as a finding.

**Critique entry template.** `Section [§N] describes deployment as [seamless / low-disruption / etc.]. Quick calculation: [time/labor cost]. Promote cost to "Deployment Cost as Finding"; add Two Scale Tiers (strong-eval / thick-description); reframe the reshape as part of the research contribution, not a limitation.`

---

### Angle 7 — Demand Characteristic in Naming and Framing

**Trigger.** Look at the system name, experimental condition labels, interview script wording, RQ wording, and any participant-facing material.

**Fail indicator.** Renaming would flip the predicted result. The classic example from the reference case: a system called "QuietProbe" pre-loads "quiet = good" into both reviewer and participant minds before any data is collected. Other red flags: condition labels like "Calibrated vs Uncalibrated," "Smart vs Naive," "Safe vs Unsafe."

**Fix pattern.** Rename system to a neutral term (ProbeMate, SegmentAid, ClassPilot — descriptive without embedded judgment). Rename conditions A/B or descriptively (Standard Assistant vs Context-Aware Assistant). Keep the loaded word in the **paper narrative** ("our system knows when to stay silent"), but never in the **participant-facing layer**.

**Reference-case anchor.** Round 2: "QuietProbe 这个名字暗示了答案…会让你的对照实验有 demand characteristic 风险." Round 3 reverts to ProbeMate; condition labels go neutral.

**Critique entry template.** `[System name / condition label / interview question] embeds the predicted answer. Renaming to [neutral alternative] would [eliminate / preserve] the demand characteristic. Rename participant-facing material; loaded framing stays in narrative only.`

---

### Angle 8 — Venue Split-Personality

**Trigger.** Ask: in one sentence, which type of reviewer will be most enthusiastic about this paper? If the answer requires "either CHI HCI-AI reviewers or CSCW workplace-studies reviewers — depending on which study lands harder," that is split-personality.

**Fail indicator.** The proposal devotes equal weight to a quantifiable design variable (CHI-style) AND a situated/qualitative accomplishment (CSCW-style). The Study 3 (controlled experiment) and Study 4 (field deployment) have roughly equal apparent priority. The construct definition tries to satisfy both audiences and reads slippery.

**Fix pattern.** Pick **one primary venue**. Rewrite the construct's framing to that venue (CHI: design variable, measurable; CSCW: sensitizing concept, situated). Rewrite Study 3 vs Study 4 emphasis. **Declare a pivot path**: if data lands differently than expected, here is the alternate venue and what stays / what changes. Document this in `venue_fit_decision.md`.

**Reference-case anchor.** Round 2: "你确定要投 CHI Papers 而不是 CSCW？" Round 3: explicit CHI-first / CSCW-pivot table with per-study implication.

**Critique entry template.** `Cannot say in one sentence which venue this serves. Study 3 (quantifiable) and Study 4 (situated) receive equal weight; construct definition straddles. Pick [CHI-first / CSCW-pivot / venue-X]. Rewrite construct framing to suit; rebalance study emphasis; write pivot path into venue_fit_decision.md.`

---

## Critique Output Format

`drafts/critique_round_<N>.md` must use this shape:

```markdown
# Critique Round <N>

Construct under critique: [name + one-line definition]
Round started: [date]
Critique angles applied: 8 (Headline / Neighbor / Ladder / Formative / Ground-truth / Deployment / Demand / Venue)

## Summary

| Angle | Fail? | Severity |
|---|---|---|
| 1 Headline competition | Yes / No | High / Medium / Low |
| 2 Construct vs neighbors | ... | ... |
| 3 Ladder vs design-space | ... | ... |
| 4 Formative inquiry | ... | ... |
| 5 Ground-truth stability | ... | ... |
| 6 Deployment cost | ... | ... |
| 7 Demand characteristic | ... | ... |
| 8 Venue split-personality | ... | ... |

Failing angles: <count>
Pass condition (≤1 failing): triggered / not triggered.

## Per-Angle Findings

### Angle 1: Headline competition

**Trigger evidence (quoted from draft):**
> [quoted passage from current draft]

**Fail finding:**
[concrete description of the fail]

**Fix:**
[what the rewrite will do]

**Owner section in rewrite:**
[which section of construct_rewrite_<N>.md will absorb this]

### Angle 2: ...

(repeat for each angle that fails or borderline-fails)

## Rewrite Hand-Off

The following sections of construct_rewrite_<N>.md must change:

- [§ name] — to absorb fix from angle [list]
- ...
```

## Pass Condition Document

If ≤ 1 angle fails, write `critique_round_<N>_passed.md`:

```markdown
# Critique Round <N> — Passed

Failing angles: <0 or 1>
The borderline angle (if any) and why no rewrite is needed.

[Quote of borderline finding, plus a 1–3 sentence explanation for why
the construct is strong enough that this single soft finding does not
warrant a full rewrite. Note any small edit that *is* warranted —
adding a single sentence somewhere — and do that edit inline rather
than triggering H3.]

The construct stress test is closed. Proceed to Module H4 (venue fit
decision).
```

## Topic-Lock Update Protocol

If H3 changes the core research question, target population, or main contribution beyond what's in `config/topic_lock.yaml`:

1. Update `topic_lock.yaml` directly — change `core_problem`, `target_user_or_population`, `expected_contribution`, and `locked_at` (set `locked_at` to current date plus "; updated by Module H round <N>").
2. Append a row to `reports/05_topic_drift_warning.md`:
   ```markdown
   ## <date> — Module H round <N> rewrite
   
   Triggered by critique angle: <name>
   Before (quoted from previous topic_lock):
   > [quote]
   After:
   > [quote]
   Reason: [one sentence].
   ```
3. Continue. The drift warning here is a positive update record, not a problem flag — it documents that the assistant deliberately retuned the lock based on critique evidence.

## Anti-Patterns

- **Do not** generate fake fails to fill all 8 angles. The pass condition exists for a reason; honest "≤ 1 fail" runs are normal for already-tight constructs.
- **Do not** quote the draft passively ("the draft seems to suggest..."). Quote the actual sentence and name what fails about it.
- **Do not** silently apply a fix without writing the critique entry. The critique log is the audit trail; it lets the user see *why* a rewrite happened.
- **Do not** chain angle 4 (formative inquiry) and angle 5 (ground-truth stability) into the same fix — they target different studies and need separate rewrite sections.
- **Do not** rewrite the construct without updating `topic_lock.yaml` when scope changes. Silent scope drift is the failure mode this protocol is designed to prevent.
