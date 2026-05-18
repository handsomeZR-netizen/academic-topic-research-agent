# Critique Round 1

Construct under critique: TODO (name + one-line definition)
Round started: TODO (date)
Critique angles applied: 8 (Headline / Neighbor / Ladder / Formative / Ground-truth / Deployment / Demand / Venue)

## Summary

| Angle | Fail? | Severity |
|---|---|---|
| 1 Headline competition | TODO (Yes / No) | TODO (High / Medium / Low) |
| 2 Construct vs neighbors | TODO | TODO |
| 3 Ladder vs design-space | TODO | TODO |
| 4 Formative inquiry vs performance | TODO | TODO |
| 5 Ground-truth stability | TODO | TODO |
| 6 Deployment cost honesty | TODO | TODO |
| 7 Demand characteristic | TODO | TODO |
| 8 Venue split-personality | TODO | TODO |

Failing angles: TODO (count)
Pass condition (≤ 1 failing): TODO (triggered / not triggered)

If pass condition triggered, rename this file to `critique_round_1_passed.md`, fill in the borderline angle below, and jump to H4 (venue fit decision). If failing angles ≥ 2, continue to per-angle findings and to `construct_rewrite_1.md`.

---

## Per-Angle Findings

For each failing angle, fill the four sub-fields. For angles that pass, write "Pass." in the body and leave the rest blank.

### Angle 1 — Headline Competition

**Trigger evidence (quoted from current draft):**

> TODO: quote the passage(s) showing ≥ 2 central claims competing.

**Fail finding:**

TODO: describe concretely. Name the competing headlines. State which one this critique recommends as the spine.

**Fix:**

TODO: name the chosen spine; explain how the other headlines get demoted to mechanism / operationalization / evidence layer.

**Owner section in rewrite:**

TODO: which section of `construct_rewrite_1.md` will absorb this.

---

### Angle 2 — Construct vs Neighbor Concepts

**Trigger evidence:**

> TODO

**Fail finding:**

TODO. Name the neighbor concept the reviewer would invoke. Quote the current definitional differentiation. Explain why it's definitional, not dimensional.

**Fix:**

TODO. List the new neighbor table rows; name the specific configuration the construct captures that the neighbor cannot.

**Owner section in rewrite:**

TODO

---

### Angle 3 — Ladder vs Design-Space Confusion

**Trigger evidence:**

> TODO

**Fail finding:**

TODO. List the construct's named levels and the independent dimensions each level varies. Show that ≥ 2 dimensions are silently compressed.

**Fix:**

TODO. Promote to N-D design space. Demote named levels to archetypes. State explicitly in the construct section that the levels are not ordinal.

**Owner section in rewrite:**

TODO

---

### Angle 4 — Formative Study as Performance vs Inquiry

**Trigger evidence:**

> TODO: quote the predicted-findings list or "expected themes" passage.

**Fail finding:**

TODO. Show that the F1–FN list cannot fail. Name the strongest plausible "design is wrong" outcome that's missing.

**Fix:**

TODO. Replace predicted findings with an Alternative Outcomes Table; list at least 3 (standard) or 5 (deep) outcomes that would falsify or reshape the design.

**Owner section in rewrite:**

TODO (typically the Study 1 section)

---

### Angle 5 — Ground-Truth Instability

**Trigger evidence:**

> TODO: quote the evaluation metric definition (macro-F1, kappa, classification accuracy).

**Fail finding:**

TODO. Explain why the construct's own theory implies context-dependent labels. Estimate how low expert agreement will be.

**Fix:**

TODO. Switch primary metric to pairwise preference (Bradley-Terry / Thurstone). Frame disagreement as result with high-consensus / structured-disagreement / no-consensus zones.

**Owner section in rewrite:**

TODO (typically the Study 2 / evaluation section)

---

### Angle 6 — Deployment Cost Hidden as Feature

**Trigger evidence:**

> TODO: quote the "seamless / low-disruption / lightweight" claims plus the system steps that actually take time.

**Fail finding:**

TODO. Compute the time/labor cost the paper hand-waves. Show the gap.

**Fix:**

TODO. Promote cost to Deployment Cost as Finding. Provide Two Scale Tiers (strong-eval vs thick-description). Frame the deployment reshape as part of the contribution.

**Owner section in rewrite:**

TODO (typically Study 4 / deployment section)

---

### Angle 7 — Demand Characteristic in Naming/Framing

**Trigger evidence:**

> TODO: quote the system name, condition labels, RQ wording, or interview prompts that embed the predicted answer.

**Fail finding:**

TODO. Show that renaming flips reviewer/participant expectations.

**Fix:**

TODO. Rename system to a neutral term. Rename conditions A/B or descriptive-neutral. Keep loaded wording in the narrative layer only.

**Owner section in rewrite:**

TODO

---

### Angle 8 — Venue Split-Personality

**Trigger evidence:**

> TODO: quote the construct framing that straddles two venues and the Study 3/4 emphasis split.

**Fail finding:**

TODO. State the venue uncertainty. Show that you cannot say in one sentence which reviewer will be happiest.

**Fix:**

TODO. Pick one primary venue. Rewrite construct framing to suit. Rebalance Study 3 vs Study 4 emphasis. Declare pivot path with explicit trigger condition.

**Owner section in rewrite:**

TODO (write the new venue strategy table into the construct rewrite section)

---

## Rewrite Hand-Off

The following sections of `construct_rewrite_1.md` must change:

- TODO: § name — to absorb fix from angle [list]
- TODO: ...
- TODO: ...

If topic_lock.yaml needs updating (because the rewrite changes scope, target user, or main contribution):

- [ ] Update `config/topic_lock.yaml` after writing `construct_rewrite_1.md`.
- [ ] Append a row to `reports/05_topic_drift_warning.md` linking back to which critique angle fired.
