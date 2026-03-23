#!/usr/bin/env python3
"""
Extract plain text from the WFRP rulebook PDF for local verification against JSON data.

Set WFRP_RULEBOOK_PDF to your PDF path (default example: z:\\gback\\wf.pdf).
Requires: pip install pypdf

Usage:
  python scripts/extract_rulebook_text.py --pages 120-140
  python scripts/extract_rulebook_text.py --out build/rulebook_snippet.txt
"""
from __future__ import annotations

import argparse
import os
import sys


def default_pdf_path() -> str:
    return os.environ.get("WFRP_RULEBOOK_PDF", r"z:\gback\wf.pdf")


def parse_pages(spec: str) -> list[int]:
    out: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return sorted(set(p - 1 for p in out if p > 0))


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text from WFRP PDF (optional helper).")
    parser.add_argument("--pdf", default=default_pdf_path(), help="Path to PDF")
    parser.add_argument("--pages", default="", help="1-based page numbers, e.g. 120-140 or 12,15,20")
    parser.add_argument("--out", default="", help="Write text to this file instead of stdout")
    args = parser.parse_args()

    if not args.pages:
        print("Provide --pages (1-based) to extract.", file=sys.stderr)
        print(f"PDF path: {args.pdf}", file=sys.stderr)
        return 1

    try:
        from pypdf import PdfReader
    except ImportError:
        print("Install pypdf: pip install pypdf", file=sys.stderr)
        return 1

    if not os.path.isfile(args.pdf):
        print(f"PDF not found: {args.pdf}", file=sys.stderr)
        return 1

    reader = PdfReader(args.pdf)
    idxs = parse_pages(args.pages)
    chunks: list[str] = []
    for i in idxs:
        if 0 <= i < len(reader.pages):
            chunks.append(reader.pages[i].extract_text() or "")
    text = "\n\n".join(chunks)
    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Wrote {args.out} ({len(text)} chars)")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
