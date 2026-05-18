"""Checklist CLI for the modular academic topic workflow.

This helper does not perform scholarly search. It prints recommended artifacts
for each module so the assistant or a user can inspect progress without
treating the workflow as rigid.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Module:
    name: str
    purpose: str
    artifacts: tuple[str, ...]


MODULES: dict[str, Module] = {
    "intake": Module(
        "intake",
        "Capture user intent, source artifacts, topic boundaries, and depth.",
        ("config/topic_input.yaml", "config/topic_lock.yaml", "reports/00_topic_lock.md"),
    ),
    "metadata": Module(
        "metadata",
        "Collect paper/system metadata at quick, standard, or deep depth.",
        ("data/processed/metadata_candidates.csv", "data/processed/paper_matrix.csv"),
    ),
    "evidence-map": Module(
        "evidence-map",
        "Cluster relevant work and reason about gaps without overclaiming novelty.",
        ("reports/03_gap_matrix.md", "logs/evidence_trace.jsonl"),
    ),
    "dataset": Module(
        "dataset",
        "Check public datasets, benchmarks, OA sources, and feasible study alternatives.",
        ("data/processed/dataset_candidates.csv", "reports/04_dataset_feasibility.md"),
    ),
    "design": Module(
        "design",
        "Develop research questions, contribution package, and evaluation plan.",
        ("drafts/contribution_candidates.md", "drafts/experiment_plan.md"),
    ),
    "construct-stress-test": Module(
        "construct-stress-test",
        "Module H (researcher-grade): stress-test construct, run 8-angle critique, rewrite, choose venue. Runs 2 passes on deep, 1 on standard with trigger keyword, skipped on quick.",
        (
            "drafts/construct_stress_test.md",
            "drafts/critique_round_1.md",
            "drafts/construct_rewrite_1.md",
            "drafts/critique_round_2.md",
            "drafts/construct_rewrite_2.md",
            "drafts/venue_fit_decision.md",
        ),
    ),
    "title-abstract": Module(
        "title-abstract",
        "Create title candidates and evidence-bound abstract variants. Researcher-grade mode requires Headline Competition Audit + Demand Characteristic Risk + Construct/Differentiation/Quantified Placeholder sentence fields.",
        ("drafts/title_candidates.md", "drafts/abstract_candidates.md"),
    ),
    "report": Module(
        "report",
        "Render the v2-style Markdown, LaTeX, and optional PDF reports. Researcher-grade mode appends the 13 blocks from assets/report-blueprint/v2_researcher_grade_extensions.{md,tex}.",
        ("reports/final_topic_report.md", "reports/final_topic_report.tex", "reports/final_topic_report.pdf"),
    ),
}


def print_module(module: Module) -> None:
    print(f"{module.name}: {module.purpose}")
    print("Recommended artifacts:")
    for artifact in module.artifacts:
        print(f"- {artifact}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Academic topic modular workflow checklist")
    parser.add_argument("module", nargs="?", choices=sorted(MODULES), help="Module name")
    parser.add_argument("--list", action="store_true", help="List all modules")
    args = parser.parse_args()

    if args.list or not args.module:
        for module in MODULES.values():
            print_module(module)
            print()
        return 0

    print_module(MODULES[args.module])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

