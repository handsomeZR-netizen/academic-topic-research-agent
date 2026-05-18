# Evidence Rules

## Non-Negotiable Rules

- Do not fabricate papers, citations, datasets, participant counts, metrics, results, deployments, or study findings.
- Do not convert a plausible idea into a factual claim without evidence.
- Do not claim global novelty unless the search scope supports that exact claim.
- Do not silently change the topic to match easier data or stronger literature.
- Do not cite a dataset unless its access page, paper, repository, or official documentation has been checked.
- Do not download paywalled or license-restricted PDFs.

## Evidence Labels

Use:

- `Supported`: backed by metadata, paper text, dataset documentation, official page, or user-provided source.
- `Partially Supported`: evidence supports only part of the statement.
- `Unknown`: not checked or not enough evidence.
- `TODO`: requires future implementation, study, annotation, or analysis.
- `Requires Manual Verification`: cannot be safely verified automatically.

## Metadata vs Claim

Metadata collection is not the same as evidence for a strong claim.

Acceptable:

```text
本次 deep 检索收集到约 100 条候选文献元数据，其中 18 条与教师端课堂决策支持高度相关。
```

Not acceptable:

```text
100 篇论文证明该系统有效。
```

## Safe Novelty Pattern

Use:

```text
在本次检索范围和关键词策略下，已有工作覆盖了 [A] 和 [B]，但较少看到同时结合 [A]、[B]、[C] 并落在 [specific context] 的系统或研究设计。
```

Avoid:

```text
没有人研究过这个问题。
```

## PDF and Dataset Safety

For PDFs:

- collect metadata and OA PDF URLs by default
- download only legal open-access PDFs or user-provided files
- record failed downloads as metadata notes, not task failure

For datasets:

- record official name, URL, license/access, labels, sample size if verified, match/mismatch, and risks
- if no dataset fits, propose a feasible study or annotation plan

## Abstract and Title Safety

Final title candidates may be aspirational. Abstracts must not imply completed experiments unless results exist.

Use:

- `本项目拟...`
- `可通过...评估`
- `初步可行性来自...`
- `需要通过后续...验证`

Avoid:

- `我们证明...`
- `显著提升...`
- `实验表明...`

