# research-base

Working papers and research sketches.

---

## PDF Build

Convert any Markdown paper to a typeset PDF with `build-pdf.py`.

### Requirements

- Python 3.9+
- [fpdf2](https://pyfpdf.github.io/fpdf2/) — pure Python PDF generation (no system libs)
- [markdown](https://python-markdown.github.io/) — Markdown parser

```bash
pip3 install fpdf2 markdown
```

No system libraries required. On macOS, Georgia fonts ship with the OS and are
used automatically for typesetting. On other systems the script falls back to
the built-in Times New Roman core font.

### Usage

```bash
# Output PDF alongside the source file
python3 build-pdf.py why-labels-need-language/why-labels-need-language.md

# Explicit output path
python3 build-pdf.py path/to/paper.md -o ~/Desktop/paper.pdf
```

The script reads the `.md` file and writes a `.pdf` with the same base name
in the same directory (unless `-o` is given).

### Paper format

Papers should follow standard Markdown. The expected structure:

```markdown
# Title

**Subtitle**

*Genre — e.g. Position Paper*

---

**Author Name**
Affiliation
email@example.com

*Month Year — Preprint*

---

## Abstract

...

## 1. Section

...

## References

...
```

The script handles title centering, author block, abstract indentation, and
justified body text automatically. Output is A4, Georgia 11pt, 28mm margins,
with page numbers — suitable for submission or distribution.

On macOS, Georgia ships with the OS and is used automatically. On other systems
the script falls back to the built-in Times New Roman core font. No internet
connection required.

---

## Contents

### [Temporalization of Order](https://github.com/outheis-labs/research-base/blob/main/temporalization-of-order/temporalization-of-order.md)

*On the structural transformation of information architectures*

The convergence of knowledge management tools (Obsidian, GitHub, Kirby CMS) on plaintext, tags, and bidirectional links reflects a shift in the temporality of order:

* **Retrospective architectures** (hierarchies) preserve ordering decisions made at storage time
* **Prospective architectures** (tags, self-description) keep options open for future, unknown questions

Central thesis: We are witnessing not the replacement of one organizational form by another, but the end of organization as necessity. Structure becomes computed rather than given — it arises at query time and passes with it.

The paper also argues that current tools realize the Semantic Web vision (self-describing, linkable data) through Unix means (plaintext, small tools) rather than formal ontologies (RDF, OWL) — and that LLMs enable a third path beyond the taxonomy/folksonomy dilemma through post-hoc harmonization.

---

### [Who Owns Experience?](https://github.com/outheis-labs/research-base/blob/main/who-owns-experience/who-owns-experience.md)

*On the transfer of human knowledge into neural models*

AI systems extract not just data but experience patterns — decision logics, heuristics, tacit knowledge. This extraction happens incidentally, through mere use of digital tools.

Three contexts analyzed:

* **Employees** whose experiential knowledge is preserved in enterprise systems
* **Researchers** whose unpublished ideas flow into training corpora
* **Children** whose learning processes are captured by educational platforms

Central thesis: Experience is neither private property nor common good. It is conditionally shareable — under conditions of consent and reciprocity. For this conditional shareability, no legal framework exists.

The paper argues that what is extracted is not data but capability — the cognitive signature that constitutes a person. When this is externalized and replicated, the person competes with a copy of themselves.

---

### [Compression and the Semantic Window](https://github.com/outheis-labs/research-base/blob/main/compression-and-semantic-window/compression-and-semantic-window.md)

*Implications of informational distance*

Annotation is constitutively an act of compression. Every label discards information; every tag selects while occluding. The degree of compression is not a neutral technical parameter — it determines what meaning can pass from annotator to model.

* **Maximum compression** (formal labels, category codes) transmits addresses, not meaning — reasoning, uncertainty, and context remain in the annotator's mind, invisible to the system
* **Lower compression** (natural language) retains the phenomenal basis of judgment: not just the category, but the reasoning that generated it

Central thesis: Meaning is not intrinsic to signals, nor simply preserved or destroyed by compression — it arises in the act of controlled compression itself. LLMs dissolve the architectural constraint that historically forced maximum compression: for the first time, compression ratio becomes an explicit design parameter rather than a format-dictated given. The shift toward natural language annotation is not a technical convenience but the first opportunity for systems to receive signals that carry meaning rather than pointers to it.

---

### [Why Labels Need Language](https://github.com/outheis-labs/research-base/blob/main/why-labels-need-language/why-labels-need-language.md)

*On the limits of formal grammars in AI*

Structured annotation formats — YOLO coordinates, NER tags, diagnostic codes — constitute minimal formal grammars. They permit exactly one statement form: element E belongs to class C. Context, reasoning, uncertainty, conditionality cannot be expressed.

The paper reframes annotation as utterance:

* An annotation is governed by a grammar determining what can be said
* Wittgenstein's insight applies: the limits of our annotation language are the limits of what models can learn
* The transition to natural language annotation is not incremental improvement but categorical expansion of semantic capacity

Central thesis: The constraints of data annotation are fundamentally linguistic constraints. What we can annotate is what our models can learn. LLMs and RAG provide the means to embrace natural language while managing ambiguity through context.

The research agenda implied: not only better models but richer annotation grammars — not only more data but more expressive data.

---

## Status

Working papers, not peer-reviewed. Discussion basis.

## License

CC BY 4.0
