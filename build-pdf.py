#!/usr/bin/env python3
"""build-pdf.py — Convert a Markdown paper to a typeset PDF.

Usage:
    python3 build-pdf.py <paper.md>            # writes <paper.pdf> alongside the .md
    python3 build-pdf.py <paper.md> -o out.pdf # explicit output path

Requirements: pip3 install fpdf2 markdown
No system libraries required.
"""

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Markdown → structured blocks
# ---------------------------------------------------------------------------

def parse_md(text: str) -> list[dict]:
    """Parse Markdown into a flat list of block dicts.

    Block types: h1, h2, h3, hr, p, ref, italic_p, keyword_p, center_p
    """
    lines = text.splitlines()
    blocks: list[dict] = []
    i = 0
    in_header_block = True  # first paragraphs (after h1) treated as centered metadata

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("# ") and not stripped.startswith("## "):
            blocks.append({"type": "h1", "text": stripped[2:].strip()})
            in_header_block = True
            i += 1
            continue

        if stripped.startswith("## "):
            in_header_block = False
            blocks.append({"type": "h2", "text": stripped[3:].strip()})
            i += 1
            continue

        if stripped.startswith("### "):
            in_header_block = False
            blocks.append({"type": "h3", "text": stripped[4:].strip()})
            i += 1
            continue

        if stripped == "---":
            if in_header_block:
                blocks.append({"type": "hr_header"})
            else:
                blocks.append({"type": "hr"})
            i += 1
            continue

        # Paragraph — collect until blank line
        para_lines = []
        while i < len(lines) and lines[i].strip():
            para_lines.append(lines[i].strip())
            i += 1
        raw = " ".join(para_lines)

        # Strip Markdown bold/italic markers for fpdf rendering
        # (we handle bold/italic inline manually below)
        if in_header_block:
            blocks.append({"type": "center_p", "text": raw})
        elif raw.startswith("**Keywords:**") or raw.startswith("*extracted:"):
            blocks.append({"type": "keyword_p", "text": raw})
        else:
            blocks.append({"type": "p", "text": raw})

    return blocks


def strip_markers(text: str) -> str:
    """Remove Markdown bold/italic markers."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    return text


def has_bold(text: str) -> bool:
    return bool(re.search(r'\*\*.+?\*\*', text))


# ---------------------------------------------------------------------------
# PDF rendering with fpdf2
# ---------------------------------------------------------------------------

def build_pdf(source: Path, output: Path) -> None:
    try:
        from fpdf import FPDF
    except ImportError:
        print("Error: fpdf2 is not installed. Run: pip3 install fpdf2", file=sys.stderr)
        sys.exit(1)

    try:
        import markdown  # noqa: F401 — just check it's available
    except ImportError:
        print("Error: markdown is not installed. Run: pip3 install markdown", file=sys.stderr)
        sys.exit(1)

    md_text = source.read_text(encoding="utf-8")
    blocks = parse_md(md_text)

    # Font paths — Georgia ships with macOS; fallback to Times (built-in, ASCII only)
    FONT_DIR = Path("/System/Library/Fonts/Supplemental")
    GEORGIA       = FONT_DIR / "Georgia.ttf"
    GEORGIA_B     = FONT_DIR / "Georgia Bold.ttf"
    GEORGIA_I     = FONT_DIR / "Georgia Italic.ttf"
    GEORGIA_BI    = FONT_DIR / "Georgia Bold Italic.ttf"
    USE_GEORGIA   = GEORGIA.exists()

    pdf = FPDF()
    pdf.set_margins(left=28, top=30, right=28)
    pdf.set_auto_page_break(auto=True, margin=28)

    if USE_GEORGIA:
        pdf.add_font("Georgia",  "",   str(GEORGIA))
        pdf.add_font("Georgia",  "B",  str(GEORGIA_B))
        pdf.add_font("Georgia",  "I",  str(GEORGIA_I))
        pdf.add_font("Georgia",  "BI", str(GEORGIA_BI))
        SERIF = "Georgia"
    else:
        SERIF = "Times"

    pdf.add_page()
    SANS  = "Helvetica"

    TEXT_W = pdf.w - pdf.l_margin - pdf.r_margin

    def write_rich(text: str, line_height: float = 6.0, align: str = "J") -> None:
        """Write text with inline bold (**) and italic (*) support."""
        # Split on ** and * markers
        parts = re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)', text)
        pdf.set_x(pdf.l_margin)
        # Use multi_cell for the full paragraph — simplest approach:
        # strip markers, handle bold paragraphs with set_font
        clean = strip_markers(text)
        if has_bold(text):
            pdf.set_font(SERIF, "B", size=11)
            pdf.multi_cell(TEXT_W, line_height, clean, align=align)
            pdf.set_font(SERIF, size=11)
        else:
            pdf.set_font(SERIF, size=11)
            pdf.multi_cell(TEXT_W, line_height, clean, align=align)

    def spacer(h: float = 3.0):
        pdf.ln(h)

    for block in blocks:
        btype = block["type"]
        text  = block.get("text", "")

        if btype == "h1":
            pdf.set_font(SERIF, "B", size=18)
            pdf.multi_cell(TEXT_W, 9, strip_markers(text), align="C")
            spacer(2)

        elif btype == "h2":
            spacer(6)
            pdf.set_font(SERIF, "B", size=12)
            pdf.multi_cell(TEXT_W, 7, strip_markers(text), align="L")
            spacer(1)

        elif btype == "h3":
            spacer(4)
            pdf.set_font(SERIF, "BI", size=11)
            pdf.multi_cell(TEXT_W, 6, strip_markers(text), align="L")
            spacer(1)

        elif btype in ("hr", "hr_header"):
            spacer(4)
            x0 = pdf.l_margin
            x1 = pdf.w - pdf.r_margin
            y  = pdf.get_y()
            pdf.set_draw_color(180, 180, 180)
            pdf.line(x0, y, x1, y)
            pdf.set_draw_color(0, 0, 0)
            spacer(4)

        elif btype == "center_p":
            clean = strip_markers(text)
            if clean.startswith("*") and clean.endswith("*"):
                clean = clean[1:-1]
                pdf.set_font(SERIF, "I", size=10)
            elif "**" in text:
                clean = re.sub(r'\*\*(.+?)\*\*', r'\1', clean)
                pdf.set_font(SERIF, "B", size=11)
            else:
                pdf.set_font(SERIF, size=11)
            pdf.multi_cell(TEXT_W, 6, clean, align="C")
            spacer(1)

        elif btype == "keyword_p":
            # Keywords line — small, italic
            pdf.set_font(SERIF, "I", size=10)
            pdf.multi_cell(TEXT_W, 5.5, strip_markers(text), align="L")
            spacer(2)

        elif btype == "p":
            clean = strip_markers(text)
            # Detect abstract (first p after ## Abstract) — indent slightly
            pdf.set_font(SERIF, size=11)
            pdf.multi_cell(TEXT_W, 6, clean, align="J")
            spacer(2)

    # Page numbers
    for page_num in range(1, pdf.page + 1):
        pdf.page = page_num
        pdf.set_y(-20)
        pdf.set_font(SANS, size=9)
        pdf.set_text_color(120, 120, 120)
        pdf.cell(TEXT_W, 5, str(page_num), align="C")
    pdf.set_text_color(0, 0, 0)

    pdf.output(str(output))
    print(f"Done: {output}", file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown paper to PDF")
    parser.add_argument("source", help="Input .md file")
    parser.add_argument("-o", "--output", help="Output .pdf path (default: alongside source)")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.exists():
        print(f"Error: {source} not found", file=sys.stderr)
        sys.exit(1)

    output = Path(args.output).expanduser().resolve() if args.output else source.with_suffix(".pdf")
    print(f"Converting {source.name} → {output.name} ...", file=sys.stderr)
    build_pdf(source, output)


if __name__ == "__main__":
    main()
