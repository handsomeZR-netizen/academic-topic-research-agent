# Dataset and Study Feasibility Protocol

Use this protocol to decide whether the topic can support experiments or only a design/study plan.

## Dataset Candidate Checks

For each candidate dataset, verify:

- official URL, repository, benchmark page, or dataset paper
- access status: public, request-only, restricted, unavailable
- license or terms
- domain and population match
- language match
- modality: text, logs, images, audio, interaction traces, survey, interview, classroom video, etc.
- labels and target variables
- sample size and granularity
- whether the dataset contains the context needed for the user's claim
- privacy and ethics risks

For standard/deep runs, write candidates to `data/processed/dataset_candidates.csv`. For quick runs, a concise table in the final report is enough.

## Verdicts

Use `Pass` when:

- public or accessible data fits the main task and supports the proposed evaluation, or
- a realistic study design can directly produce the required evidence within scope.

Use `Weak Pass` when:

- a dataset exists but only supports offline modeling or partial feasibility,
- additional annotation is required,
- the population or modality is close but not exact,
- a user study is feasible but not yet arranged.

Use `Fail` when:

- no data or feasible study can support the core claim,
- access restrictions block the required evaluation,
- the topic would require unsafe or unrealistic data collection,
- the contribution depends on results that cannot be obtained.

## Alternatives When No Dataset Fits

Recommend one or more:

- formative interview study
- design study
- Wizard-of-Oz study
- expert review
- annotation protocol
- simulated task/vignette study
- classroom or field micro-deployment
- benchmark construction as the first contribution

Do not invent data.

## Report Requirements

When feasibility is central to the task, include these in `reports/04_dataset_feasibility.md` and/or the final report:

- verdict
- dataset table
- what each dataset can support
- what each dataset cannot support
- recommended study path
- claims that remain unsafe
