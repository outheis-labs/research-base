# Compression and the Semantic Window

**Implications of Informational Distance**

*A Position Paper*

---

**Markus Schatzl**  
Independent Researcher, Munich  
technology.culture@proton.me

*April 2026 — Preprint*

---

## Starting Point

Description requires distance. A description that captures all non-redundant properties of an entity would be its identity—no longer a description, but duplication. The distance from identity, achieved through reduction, is not a disadvantage but constitutive: only this distance enables context, relation, structure.

Description is therefore necessarily compression: selection of properties while omitting others. It becomes an informational excerpt. This selection is not neutral—it implies a decision about relevance.

---

## 1. Compression and Abstraction

The degree of compression determines the distance from the actual constitution of a phenomenon. The more compression is applied, the further the description moves from the singularity of what is described, and the greater the reach of the statement becomes.

Abstraction is the limiting case: maximum compression, maximum distance, maximum reach. The price is the loss of the singular.

This structure holds regardless of medium. It applies to language, to formal notations, to visual representations. It applies to scientific categories as much as to everyday naming.

## 2. Labels, Tags, Annotations

In machine learning, annotation operates as compression. An expert perceives a signal, integrates experience, contextual knowledge, implicit heuristics—and produces a term: *bearing damage*. The entire perceptual and interpretive performance is reduced to a category assignment.

In information architecture, the tag operates identically: a document, an artifact, a dataset is furnished with descriptors that select certain properties and occlude others.

Both operations—label and tag—are structurally equivalent. They compress in order to gain simplicity, performance, comparability. The system can only process what compression leaves behind.

## 3. Formal Grammars as Maximum Compression

Structured annotation formats—coordinate systems, category codes, taxonomies—are formal languages with minimal grammar. They permit exactly one statement form: element E belongs to class C. Additionally: geometric parameters, confidence values, relations. Nothing more.

These formats maximize compression. Distance from the thing is maximal, processability optimal, expressiveness minimal.

The expert who annotates *bearing damage* knows more than the format can express: uncertainty, context-dependence, reasoning, implications for action. This knowledge exists, but it is not representable in the format. It disappears.

## 4. Natural Language as Lower Compression

Consider the difference. The label *bearing damage* versus: *Periodic knocking at approximately 120 Hz, intensifying under load, characteristic of early-stage roller bearing wear; inspection recommended within two weeks.*

The second is not merely longer. It preserves what the first discards: the phenomenal basis of the judgment, the reasoning that connects observation to conclusion, the uncertainty, the temporal horizon. It transmits not just the address but fragments of the address book.

Yet it remains compression. No description escapes this. The question is not whether to compress but how much—and that question, until now, was answered by technical constraint rather than epistemological judgment.

## 5. The Constraint Dissolves

Classical ML architectures could not read sentences. They required coordinates, codes, class indices—forcing maximum compression regardless of what was lost. The grammar of the annotation format was dictated by the grammar of the model's input layer.

Large language models dissolve this constraint. They process natural language natively. For the first time, the degree of compression becomes a design parameter rather than a given.

This is not a minor technical shift. It relocates a decision that was formerly invisible—buried in format specifications—into the space of explicit epistemological choice. How much context should survive the annotation? How much interpretation? How much uncertainty? These questions now require answers.

## 6. Implications

**For the model:** Under maximum compression, training data consists of addresses—pointers to meaning that exists only in the annotator's mind or in documentation the model never sees. Under lower compression, portions of that meaning enter the training signal directly. The model learns not just that X belongs to class Y, but why.

**For the annotator:** The role transforms. Maximum compression demands an encoder—someone who translates rich perception into sparse categories. Lower compression demands an author—someone who explicates perception, renders reasoning visible, makes implicit knowledge transmissible.

**For information theory:** Shannon's framework measures the entropy of symbols, explicitly bracketing semantics. But if description is constitutively compression, then every annotation carries semantic entropy that Shannon's formalism cannot capture. The question whether meaning has measurable information content remains open—and becomes urgent.

## 7. Open Questions

If compression ratio is now a parameter, what determines its appropriate value? Purpose, presumably—but purpose is typically left implicit in ML pipelines. Making compression ratio explicit forces the question: what is this model supposed to understand?

What exactly vanishes under maximum compression? Not only quantitative information, but possibly entire categories of statement—uncertainty, conditionality, reasoning, temporal structure—that the formal grammar cannot express. The loss may be categorical, not merely quantitative.

And what is the epistemological status of knowledge that exists in the annotator's mind but cannot pass through the format? It is real, it is relevant, it shapes the label—yet it remains invisible to the system. The model learns from a shadow cast by knowledge it never receives.

---

## References

Lu, Z. (2025). A Semantic Generalization of Shannon's Information Theory (G-Theory). *Entropy*, 27(5), 461.

Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379–423.

Tishby, N., Pereira, F. C., & Bialek, W. (1999). The Information Bottleneck Method. *Proceedings of the 37th Allerton Conference on Communication, Control, and Computing*, 368–377.

Tishby, N., & Zaslavsky, N. (2015). Deep Learning and the Information Bottleneck Principle. *IEEE Information Theory Workshop (ITW)*, 1–5.

Wand, Y., & Weber, R. (1993). On the Ontological Expressiveness of Information Systems Analysis and Design Grammars. *Information Systems Journal*, 3(4), 217–237.

---

*© 2026 Markus Schatzl. All rights reserved.*
