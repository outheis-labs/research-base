# Why Labels Need Language

**On the Limits of Formal Grammars in AI**

*A Position Paper on the Linguistic Foundations of Data Annotation*

---

**Markus Schatzl**  
Independent Researcher, Munich  
technology.culture@proton.me

*April 2026 — Preprint*

---

## Abstract

Modern machine learning systems require annotated training data. The dominant annotation formats—structured labels with categorical identifiers—constitute minimal formal grammars that severely constrain what can be described. We argue that this constraint is not merely technical but linguistic: the expressiveness of an annotation format determines the boundary of describable phenomena, echoing Wittgenstein's insight that the limits of language are the limits of the world. The transition from structured labels to natural language descriptions is therefore not an incremental improvement but a categorical expansion of semantic capacity. Large Language Models combined with Retrieval-Augmented Generation (RAG) offer a path to resolve the inherent ambiguity of natural language through context, enabling annotation systems that approach the full expressiveness of human description while maintaining computational tractability.

**Keywords:** annotation, description, formal grammar, expressiveness, Wittgenstein, language models, RAG

---

## 1. The Poverty of Structure

Consider any structured annotation format. In computer vision, the YOLO format reduces description to five values: a class identifier and four coordinates. In natural language processing, named entity recognition tags reduce meaning to category labels like PERSON, LOCATION, ORGANIZATION. In medical imaging, annotations are often binary masks with diagnostic codes. In document processing, labels might be INVOICE, CONTRACT, RECEIPT.

These formats share a common structure: they map regions or elements to categorical identifiers, sometimes with additional geometric or relational metadata. They are elegant in their simplicity, computationally efficient, and entirely sufficient for training models to classify within predefined categories.

Yet this simplicity comes at a cost that is rarely articulated: these formats constitute minimal formal grammars whose productive capacity is severely bounded. A structured annotation can express that element E belongs to class C. It cannot express that the classification depends on context, that the boundary between classes is contested, that what constitutes a category changed when new regulations came into effect, or that the annotator was uncertain and would have preferred to say 'probably X, but possibly Y because...'.

This is not a limitation of any specific format but of any annotation system that reduces description to categorical assignment. The grammar permits exactly one kind of statement: 'element E belongs to class C.' Every other aspect of description—context, reasoning, conditions, uncertainty, temporal dependencies, degrees of confidence—must be encoded outside the annotation itself, typically in separate documentation that the model never sees.

The problem becomes even more acute in domains where the data has no gestalt that is readily accessible to human perception—where a distance to human perceptual experience exists. Time series signals, acoustic data, sensor streams: these cannot draw on the immediate physiological structures of our senses and therefore demand a greater share of conscious cognitive processing. We construct visualizations (spectrograms, waveforms, plots) as surrogates, but these are translations, not the thing itself. Here, description is not merely useful but constitutive: language becomes the primary—sometimes the only—access to meaning. An expert assessing a machine vibration signal does not say 'anomaly at sample 24000-34000.' She says: 'bearing damage, audible as periodic knocking at approximately 120 Hz, intensifying under load.' This description is not a summary of a label—it is the information itself. The poverty of structured annotation formats is most visible precisely where the data resists immediate experience.

## 2. Labels as Utterances

We propose a reframing: an annotation is not merely metadata attached to a data element but an utterance within a language. Like any utterance, it is governed by a grammar that determines what can be said, a semantics that determines what it means, and pragmatic constraints that determine how it functions in context.

This perspective reveals that the 'annotation problem' in machine learning is fundamentally a linguistic problem. When practitioners complain that relabeling is expensive, that annotations become stale when requirements change, or that models fail to generalize across contexts, they are describing symptoms of an impoverished grammar. The annotation language lacks the expressive resources to capture what experts actually know about the domain.

Semantic Role Labeling in computational linguistics provides a relevant precedent. Fillmore's FrameNet project, initiated in 1997, demonstrated that verbs evoke semantic frames with defined roles—agent, patient, instrument, location. This insight enabled far richer annotations of natural language text than simple part-of-speech tagging. Data annotation across all domains awaits an analogous expansion.

## 3. Wittgenstein's Insight

Ludwig Wittgenstein's observation that 'the limits of my language mean the limits of my world' (Tractatus, 5.6) applies with unexpected precision to data annotation. If our annotation grammar can only express categorical membership, then our trained models inhabit a world where only categorical membership exists. They cannot learn what we cannot describe.

Wittgenstein's later work on language games offers a second insight. In the Philosophical Investigations, he argues that meaning arises from use within specific forms of life—that the same word can function differently in different language games. This maps directly to the context-dependence of expert judgment: the same pattern might be 'anomaly' in one context and 'acceptable variation' in another. The annotation format must be capable of encoding not just what is observed but in which language game the observation occurs.

The implication is that expanding annotation expressiveness is not an optimization but a categorical shift. Moving from structured labels to natural language descriptions like 'this pattern requires attention because it indicates early-stage degradation that typically progresses under continued use' is not adding parameters to an existing grammar—it is adopting an entirely different grammar with fundamentally greater productive capacity.

## 4. From Syntax to Semantics: The Role of Context

Natural language brings expressiveness but also ambiguity. Technical formats achieve precision by eliminating ambiguity, but at the cost of eliminating most of what can be said. Human language achieves expressiveness by tolerating ambiguity and resolving it through context.

This is where Retrieval-Augmented Generation (RAG) becomes linguistically significant. A RAG system does not simply 'look up information'—it provides the contextual embedding that disambiguates natural language descriptions. When an annotation says 'critical issue,' the RAG retrieval of relevant documentation, previous assessments, and domain-specific guidelines supplies the contextual frame that makes 'critical' precise.

Large Language Models complete the bridge. They can process natural language annotations and align them with the data being described, enabling the model to 'understand' not just categorical assignment but the reasoning behind it, the conditions under which it applies, and how it relates to the verbal descriptions that domain experts use. The embedding space becomes a shared semantic space between data and language.

## 5. Implications for Human-in-the-Loop Systems

If annotations are utterances, then the annotation process is a dialogue. Human-in-the-loop systems that merely ask annotators to confirm or reject model predictions are conducting a dialogue in a crippled language—yes/no responses to questions the model has already framed. A richer annotation grammar enables a richer dialogue.

Consider the difference between 'Is this category X? [Yes/No]' and 'Describe what you observe and why it matters.' The first constrains the expert to the model's existing categories; the second allows the expert to teach the model new distinctions. The first maintains the current grammar; the second expands it.

This suggests that truly adaptive annotation systems must treat expert input not as labels but as linguistic contributions to an evolving semantic model. The system learns not just which elements belong to which categories but what categories mean in context—and how that meaning might change.

## 6. Conclusion

We have argued that the constraints of data annotation are fundamentally linguistic constraints. Standard annotation formats constitute minimal grammars with bounded expressiveness. The transition to natural language annotation is not merely convenient but necessary for systems that must capture the full semantic richness of expert knowledge.

Wittgenstein's insight—that language limits determine world limits—applies directly: what we can annotate is what our models can learn. Large Language Models and RAG provide the technical means to embrace natural language while managing its inherent ambiguity through context.

The research agenda this implies is clear: we need not only better models but richer annotation grammars, not only more data but more expressive data, not only human-in-the-loop confirmation but human-in-the-loop dialogue. The grammar of description must expand to meet the complexity of the world.

---

## References

Dupré, J., & Sherrat, T. (Eds.). (2024). *Wittgenstein and Artificial Intelligence*. Cambridge University Press.

Fillmore, C. J. (1968). The Case for Case. In E. Bach & R. Harms (Eds.), *Universals in Linguistic Theory* (pp. 1-88). Holt, Rinehart & Winston.

Fillmore, C. J., & Baker, C. (2010). A Frames Approach to Semantic Analysis. In B. Heine & H. Narrog (Eds.), *The Oxford Handbook of Linguistic Analysis*.

Lu, Z. (2025). A Semantic Generalization of Shannon's Information Theory and Applications. *Entropy*, 27(5), 461.

Pustejovsky, J., & Yocum, K. (2014). Image Annotation with ISO-Space: Distinguishing Content from Structure. *Proceedings of LREC 2014*.

Tishby, N., & Zaslavsky, N. (2015). Deep Learning and the Information Bottleneck Principle. *IEEE Information Theory Workshop (ITW)*, 1-5.

Tishby, N., Pereira, F. C., & Bialek, W. (1999). The Information Bottleneck Method. *Proceedings of the 37th Annual Allerton Conference on Communication, Control and Computing*, 368-377.

Wand, Y., & Weber, R. (1993). On the Ontological Expressiveness of Information Systems Analysis and Design Grammars. *Information Systems Journal*, 3(4), 217-237.

Wittgenstein, L. (1921). *Tractatus Logico-Philosophicus*. Trans. D. Pears & B. McGuinness (1961). Routledge.

Wittgenstein, L. (1953). *Philosophical Investigations*. Trans. G.E.M. Anscombe. Blackwell.

---

*© 2026 Markus Schatzl. All rights reserved.*
