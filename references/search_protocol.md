# Metadata and Search Protocol

Use this protocol for scholarly search, PDF metadata collection, venue mapping, and evidence tracing.

## Depth Presets

| Depth | Candidate metadata target | Use case |
|---|---:|---|
| `quick` | 10-20 | fast direction check, title/abstract polish, short memo |
| `standard` | 30-50 | normal topic package and v2-style report |
| `deep` | 80-120 | systematic pre-research, "100 papers", "100 PDF metadata", broad venue map |

The target is metadata count, not mandatory full-text PDF downloads.

## PDF Policy

For every candidate, collect a DOI/URL and an OA PDF URL when legally available.

Download PDF files only when:

- the PDF is clearly open access,
- the user provided the file,
- or the source terms permit download.

If the user asks for "100 PDFs", interpret this as "about 100 paper/PDF metadata records plus available OA PDF links" unless they explicitly ask to download files and legal access is clear.

## Source Priority

Before any search, read `config/sources.yaml`. **Only use sources whose `enabled: true`.** Users can disable any source by editing that file (e.g., setting `ieee_xplore.enabled: false` to skip paywalled IEEE content). If `sources.yaml` is missing, fall back to the full list below and create the file with sensible defaults.

Prefer primary or stable sources:

- ACM Digital Library, IEEE Xplore, Springer, Elsevier, ACL Anthology, AAAI, NeurIPS, CHI proceedings, LAK, L@S, AIED, EDM
- Semantic Scholar, OpenAlex, Crossref, DBLP, arXiv
- official project pages, GitHub repositories, benchmark pages, dataset cards
- institutional, government, school, or standards pages when policy/context matters

Use broad web search to locate primary sources, then cite primary sources when possible.

## Query Groups

Create query groups based on the task:

- `core`: central problem and target contribution
- `user`: population, users, institutions, setting
- `method`: model, system, workflow, study, evaluation method
- `venue`: target venue plus topic terms
- `dataset`: dataset, benchmark, corpus, repository, survey, records
- `contrast`: excluded directions or adjacent approaches
- `risk`: limitations, failures, ethics, deployment friction

For `deep`, use multiple rounds: broad discovery, cluster expansion, venue-specific search, dataset search, and backward/forward related work from key papers.

## Screening Status

Use these labels in metadata files:

- `candidate`: found and plausibly relevant
- `keep`: important enough to discuss or cite
- `background`: useful context but not central
- `exclude`: off-scope after inspection
- `manual_check`: promising but metadata/source needs verification

## Recommended Metadata Fields

Record:

- `paper_id`
- `title`
- `authors`
- `year`
- `venue`
- `doi`
- `url`
- `pdf_url`
- `oa_status`
- `source`
- `query_used`
- `abstract`
- `keywords`
- `topic_cluster`
- `relevance_score`
- `screening_status`
- `reason_to_keep`
- `reason_to_exclude`
- `evidence_status`
- `manual_verification_needed`

## Deep Search Acceptance

A `deep` run is acceptable when it:

- records 80-120 candidate metadata rows, or clearly explains search/network limits,
- has at least 10-20 `keep` or high-value records (rule of thumb across all depths: at least ⅓ of rows reach `keep` or `background` — pure `candidate` lists do not satisfy the depth target),
- includes dataset/benchmark sources where relevant,
- separates metadata collection from claim-making,
- identifies what still needs full-text reading.

