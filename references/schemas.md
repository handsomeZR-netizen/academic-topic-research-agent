# Schemas

Use these schemas as defaults. Add, remove, or merge fields when the topic requires it.

## `config/topic_input.yaml`

```yaml
topic_title: ""
target_venue: ""
field: ""
year_range: ""
depth: "standard" # quick | standard | deep
must_have: []
avoid: []
dataset_requirement: ""
output_language: "中文"
source_documents: []
```

## `config/topic_lock.yaml`

```yaml
original_title: ""
source_artifacts: []
core_problem: ""
not_core_problem: []
target_user_or_population: ""
decision_context: ""
expected_contribution: []
must_have: []
avoid: []
target_venue: ""
field: ""
year_range: ""
depth: "standard"
output_language: "中文"
locked_at: ""
```

## `data/processed/metadata_candidates.csv`

Recommended columns:

```text
paper_id,title,authors,year,venue,doi,url,pdf_url,oa_status,source,
query_used,abstract,keywords,topic_cluster,relevance_score,
screening_status,reason_to_keep,reason_to_exclude,evidence_status,
manual_verification_needed
```

Allowed `screening_status` values:

- `candidate`
- `keep`
- `background`
- `exclude`
- `manual_check`

## `data/processed/paper_matrix.csv`

Recommended columns:

```text
paper_id,title,authors,year,venue,doi,url,pdf_url,source,query_used,
relevance_score,screening_status,tags,research_problem,method,
system_or_intervention,dataset_or_study,participants,task_context,
evaluation_metrics,main_findings,limitations,relevance_to_topic,
covered_dimensions,missing_dimensions,evidence_status,
manual_verification_needed
```

**Depth-specific column guidance:**

- `quick` runs may omit: `tags`, `participants`, `task_context`, `evaluation_metrics`, `main_findings`, `limitations`, `covered_dimensions`, `missing_dimensions`. Keep at minimum: `paper_id, title, authors, year, venue, doi/url, relevance_score, screening_status, relevance_to_topic, evidence_status`.
- `standard` runs should populate every column for `keep`-status rows; `candidate`/`exclude` rows can leave deep-analysis fields blank.
- `deep` runs should populate every column for any row tagged `keep` or `background`.

## `data/processed/dataset_candidates.csv`

Recommended columns:

```text
dataset_name,url,paper_or_docs_url,license,access_status,task_type,
domain,population,language,modality,sample_size,available_labels,
match_to_topic,mismatch_to_topic,usable_for,risk_level,usefulness,
ethics_notes,evidence_status,manual_verification_needed
```

## `logs/evidence_trace.jsonl`

Each line should be one JSON object:

```json
{
  "timestamp": "",
  "stage": "",
  "source": "",
  "query_or_input": "",
  "artifact": "",
  "claim_supported": "",
  "evidence_status": "Unknown",
  "notes": ""
}
```

Allowed `evidence_status` values:

- `Supported`
- `Partially Supported`
- `Unknown`
- `TODO`
- `Requires Manual Verification`

## Draft Artifacts

`drafts/title_candidates.md` should contain 3-8 title candidates with title, Chinese rendering, style, contribution focus, venue fit, evidence fit, feasibility, risk, and recommendation.

`drafts/abstract_candidates.md` should contain 1-3 abstract variants plus an evidence-binding table.

`drafts/experiment_plan.md` should contain research questions, study overview, participants/data, materials/tasks, procedure, comparisons, measures, analysis plan, expected figures/tables, risks, and evidence status.

## Final Reports

Final full packages should include:

- `reports/final_topic_report.md`
- `reports/final_topic_report.tex`
- `reports/final_topic_report.pdf` when local TeX exists

The Markdown and LaTeX reports should contain the same substantive argument, but exact section names may adapt to the topic.

