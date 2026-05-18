"""Render v2-style final topic reports as LaTeX and PDF.

Default input/output:
  reports/final_topic_report.md
  reports/final_topic_report.tex
  reports/final_topic_report.pdf

The script converts Markdown to a LaTeX body with Pandoc when available, wraps
it in the bundled Chinese v2-style report shell, and compiles with latexmk or
xelatex when a local TeX toolchain exists. If Pandoc is unavailable, it writes
a conservative heading/list/paragraph conversion so the LaTeX artifact still
exists for manual refinement.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


STYLE_TEMPLATE = r"""\documentclass[UTF8,a4paper,11pt]{ctexart}

\usepackage[a4paper,margin=2.4cm]{geometry}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{array}
\usepackage{multirow}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage[most]{tcolorbox}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{caption}
\usepackage{float}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\newcounter{none}

\usetikzlibrary{positioning,arrows.meta,shapes.geometric,fit,calc}

\definecolor{mainblue}{RGB}{28,90,160}
\definecolor{lightblue}{RGB}{235,244,255}
\definecolor{darkgray}{RGB}{70,70,70}
\definecolor{lightgray}{RGB}{245,245,245}
\definecolor{accentorange}{RGB}{230,120,40}
\definecolor{softgreen}{RGB}{235,250,240}

\hypersetup{
  colorlinks=true,
  linkcolor=mainblue,
  urlcolor=mainblue,
  citecolor=mainblue
}

\titleformat{\section}
  {\Large\bfseries\color{mainblue}}
  {\thesection}{0.8em}{}

\titleformat{\subsection}
  {\large\bfseries\color{darkgray}}
  {\thesubsection}{0.8em}{}

\titleformat{\subsubsection}
  {\normalsize\bfseries\color{darkgray}}
  {\thesubsubsection}{0.8em}{}

\pagestyle{fancy}
\setlength{\headheight}{14pt}
\fancyhf{}
\lhead{__SHORT_TITLE__}
\rhead{研究方案报告}
\cfoot{\thepage}

\tcbset{
  mybox/.style={
    colback=lightblue,
    colframe=mainblue,
    arc=2mm,
    boxrule=0.8pt,
    left=2mm,
    right=2mm,
    top=1.5mm,
    bottom=1.5mm
  },
  keybox/.style={
    colback=softgreen,
    colframe=green!50!black,
    arc=2mm,
    boxrule=0.8pt,
    left=2mm,
    right=2mm,
    top=1.5mm,
    bottom=1.5mm
  },
  warnbox/.style={
    colback=orange!8,
    colframe=accentorange,
    arc=2mm,
    boxrule=0.8pt,
    left=2mm,
    right=2mm,
    top=1.5mm,
    bottom=1.5mm
  }
}

\title{
  \vspace{-1.5cm}
  \textbf{__TITLE__}\\[0.5em]
  \large __SUBTITLE__
}

\author{__AUTHOR__}
\date{\today}

\begin{document}

\maketitle

\begin{tcolorbox}[mybox,title=一句话概括]
本报告用于在正式写作、开发或实验前，对选题进行证据优先的可行性判断、研究定位、数据集支持、标题摘要和研究设计梳理。
\end{tcolorbox}

\vspace{0.5em}

\tableofcontents
\newpage

__BODY__

\end{document}
"""


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def escape_tex(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def fallback_md_to_body(md_path: Path) -> str:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    in_itemize = False
    in_enumerate = False

    def close_lists() -> None:
        nonlocal in_itemize, in_enumerate
        if in_itemize:
            out.append(r"\end{itemize}")
            in_itemize = False
        if in_enumerate:
            out.append(r"\end{enumerate}")
            in_enumerate = False

    for raw in lines:
        line = raw.strip()
        if not line:
            close_lists()
            out.append("")
            continue
        if line.startswith("# "):
            close_lists()
            out.append(r"\section{" + escape_tex(line[2:].strip()) + "}")
        elif line.startswith("## "):
            close_lists()
            out.append(r"\section{" + escape_tex(line[3:].strip()) + "}")
        elif line.startswith("### "):
            close_lists()
            out.append(r"\subsection{" + escape_tex(line[4:].strip()) + "}")
        elif line.startswith("#### "):
            close_lists()
            out.append(r"\subsubsection{" + escape_tex(line[5:].strip()) + "}")
        elif line.startswith("- "):
            if in_enumerate:
                out.append(r"\end{enumerate}")
                in_enumerate = False
            if not in_itemize:
                out.append(r"\begin{itemize}[leftmargin=2em]")
                in_itemize = True
            out.append(r"\item " + escape_tex(line[2:].strip()))
        elif len(line) > 3 and line[0].isdigit() and line[1:3] == ". ":
            if in_itemize:
                out.append(r"\end{itemize}")
                in_itemize = False
            if not in_enumerate:
                out.append(r"\begin{enumerate}[leftmargin=2em]")
                in_enumerate = True
            out.append(r"\item " + escape_tex(line[3:].strip()))
        elif line.startswith("> "):
            close_lists()
            out.append(r"\begin{tcolorbox}[keybox]")
            out.append(escape_tex(line[2:].strip()))
            out.append(r"\end{tcolorbox}")
        else:
            close_lists()
            out.append(escape_tex(line) + "\n")
    close_lists()
    return "\n".join(out)


def pandoc_md_to_body(md_path: Path) -> tuple[str, str]:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return fallback_md_to_body(md_path), "fallback-no-pandoc"

    result = run(
        [
            pandoc,
            str(md_path),
            "-f",
            "gfm",
            "-t",
            "latex",
            "--top-level-division=section",
        ]
    )
    if result.returncode == 0:
        return sanitize_latex_body(result.stdout), "styled-pandoc"
    return fallback_md_to_body(md_path), "fallback-after-pandoc-failure"


def sanitize_latex_body(body: str) -> str:
    """Smooth over Pandoc snippets that need its standalone preamble."""
    return body.replace(r"\begin{longtable}[]", r"\begin{longtable}")


def write_styled_tex(
    md_path: Path,
    tex_path: Path,
    title: str,
    subtitle: str,
    author: str,
    short_title: str,
) -> str:
    body, renderer = pandoc_md_to_body(md_path)
    doc = (
        STYLE_TEMPLATE.replace("__TITLE__", escape_tex(title))
        .replace("__SUBTITLE__", escape_tex(subtitle))
        .replace("__AUTHOR__", escape_tex(author))
        .replace("__SHORT_TITLE__", escape_tex(short_title))
        .replace("__BODY__", body)
    )
    tex_path.write_text(doc, encoding="utf-8")
    return renderer


def compile_pdf(tex_path: Path, pdf_path: Path, build_dir: Path) -> str:
    build_dir.mkdir(parents=True, exist_ok=True)
    latexmk = shutil.which("latexmk")
    if latexmk:
        result = run(
            [
                latexmk,
                "-xelatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-outdir={build_dir}",
                str(tex_path),
            ]
        )
        built = build_dir / (tex_path.stem + ".pdf")
        if result.returncode == 0 and built.exists():
            shutil.copy2(built, pdf_path)
            return "latexmk"
        return "latexmk-failed"

    xelatex = shutil.which("xelatex")
    if xelatex:
        result = run(
            [
                xelatex,
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={build_dir}",
                str(tex_path),
            ]
        )
        built = build_dir / (tex_path.stem + ".pdf")
        if result.returncode == 0 and built.exists():
            shutil.copy2(built, pdf_path)
            return "xelatex"
        return "xelatex-failed"

    return "no-tex-engine"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--md", default="reports/final_topic_report.md")
    parser.add_argument("--tex", default="reports/final_topic_report.tex")
    parser.add_argument("--pdf", default="reports/final_topic_report.pdf")
    parser.add_argument("--build-dir", default="reports/build")
    parser.add_argument("--title", default="选题前置调研报告")
    parser.add_argument("--subtitle", default="Evidence-first Research Planning Package")
    parser.add_argument("--author", default="Generated by academic-topic-research-agent")
    parser.add_argument("--short-title", default="选题前置调研")
    parser.add_argument("--skip-pdf", action="store_true")
    args = parser.parse_args()

    md_path = Path(args.md)
    tex_path = Path(args.tex)
    pdf_path = Path(args.pdf)
    build_dir = Path(args.build_dir)

    if not md_path.exists():
        raise SystemExit(f"Missing Markdown report: {md_path}")

    tex_path.parent.mkdir(parents=True, exist_ok=True)
    renderer = write_styled_tex(
        md_path,
        tex_path,
        title=args.title,
        subtitle=args.subtitle,
        author=args.author,
        short_title=args.short_title,
    )
    print(f"wrote {tex_path} via {renderer}")

    if not args.skip_pdf:
        compiler = compile_pdf(tex_path, pdf_path, build_dir)
        print(f"pdf status: {compiler}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
