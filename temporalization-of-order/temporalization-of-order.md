# The Temporalization of Order

## On the Structural Transformation of Information Architectures

**Author:** Markus Schatzl (technology.culture@proton.me)

**Status:** Working paper, November 2025

---

## Abstract

The current convergence of independently developed knowledge management tools—from Obsidian to GitHub to modern content management systems—suggests a structural shift in information architecture. This paper analyzes three constitutive elements of this development: plaintext-based data storage, tag-based ordering principles, and multiple relationality. The central thesis holds that this shift is not primarily a technical improvement but a fundamental change in the temporality of order: from retrospective architectures that preserve decisions made at the time of storage, to prospective architectures that keep ordering options open for future, presently unknown questions.

---

## 1. Phenomenology of Convergence

### 1.1 Observation

In recent years, a remarkable convergence has emerged in the development of knowledge management tools. Independently developed systems are converging on a common architecture characterized by three features:

1. **Plaintext data storage** with optional markup interpretation (typically Markdown)
2. **Tags and labels** as the primary ordering principle instead of hierarchical directory structures
3. **Multiple relationality** through bidirectional links and associative connections

This architecture appears in personal knowledge management tools like Obsidian, Logseq, and Roam Research; was retrofitted into platforms like Notion; increasingly shapes the organizational logic of development environments like GitHub (where labels play a central role in issue and pull request management); and underlies content management systems like Kirby, which are based on plaintext files with YAML frontmatter.

### 1.2 Significance

This convergence is remarkable because it is not the result of a coordinated movement or a dominant standard. The tools mentioned were developed for different application contexts—personal knowledge management, software development, content publishing—yet converge on the same structural solution.

This suggests that the observed architecture is not arbitrary but responds to an underlying problem equally virulent across domains: the organization of information under conditions of complexity, changeability, and multiple access perspectives.

---

## 2. The Three Elements in Detail

### 2.1 Plaintext as Data Format

#### Characteristics

The use of plaintext (ASCII/UTF-8) as the primary data format initially appears as a technical regression. Modern data formats offer richer structuring capabilities, typing, and validation. The return to plaintext deliberately forgoes these possibilities.

#### Rationale

On closer examination, this renunciation proves strategic:

**Universal readability:** Plaintext files are readable without specific software. A `cat` command in the terminal, any text editor, or a simple script suffices. This property is not trivial—it means the data is independent of its processing software.

**Long-term stability:** Plaintext files from the 1970s are easily readable today. Proprietary formats from the same period are often accessible only with archaeological effort. The simplicity of the format guarantees readability across decades.

**Operational efficiency:** Every operation on plaintext—search, transformation, versioning—benefits from the format's simplicity. Diff algorithms, regular expressions, and full-text indexing work without preprocessing.

**Liberation from processing silos:** Proprietary formats bind data to specific processing software. Plaintext allows free combination of tools. A Markdown file can be edited in Obsidian, transformed with Pandoc, versioned in a Git repository, and published with a static website generator.

#### Markdown as Compromise

The addition of Markdown syntax represents a compromise: structural information (headings, lists, emphasis) is encoded in a way that remains human-readable without an interpreter. A Markdown document is understandable as raw text—interpretation adds presentation but not meaning.

### 2.2 Tags as Ordering Principle

#### The Problem of Hierarchical Order

Conventional file systems organize information in tree structures. An object exists at exactly one location in the hierarchy. This structure implies a 1:1 relation between object and position.

This uniqueness, which at first appears as an ordering achievement, proves to be a restriction for more complex knowledge bases. A document relevant to both Project A and Project B must either be duplicated (with the familiar problems of inconsistency) or assigned to one of the two categories (with the result that it becomes invisible from the other perspective).

#### Tags as Resolution of the 1:1 Relation

Tags dissolve this restriction. An object can carry any number of tags. Category membership is no longer exclusive but cumulative. Multiple membership becomes the norm rather than the exception.

This seemingly simple change has far-reaching consequences:

**Ad-hoc hierarchies:** Directory structures can be virtually generated by filtering for tag combinations. The hierarchy exists not as a physical structure but as a computed view.

**Interest-driven order:** Different users or usage contexts can project different orderings onto the same data pool. The project manager sees data ordered by project affiliation, the compliance officer by retention periods, the researcher by thematic clusters.

**Explicit rather than implicit semantics:** In a hierarchy, an object's meaning derives from its position. The path `/projects/2024/client-x/proposals/` contains information about the object, but this information is stored in the container, not in the object itself. Tags make this semantics explicit and portable.

### 2.3 Multiple Relationality

#### Beyond Tags

Tags establish memberships in categories. Beyond this, modern tools enable direct linking of objects to each other—typically through bidirectional links.

A bidirectional link means: when Document A references Document B, this reference also appears in Document B as a backlink. The relation is symmetrically visible.

#### Emergent Network Structure

Through the accumulation of such links, a network structure emerges that enables two navigation modes:

**Associative navigation:** One can move from object to object along the links, following "paths" that arise from content relationships.

**Hierarchical navigation:** Through tag filtering, tree-like structures can still be generated—thematic clusters, project folders, chronological views.

The structure is thus neither purely hierarchical nor purely associative but enables both access modes on the same data pool.

---

## 3. The Asymmetry of Hierarchy and Tags

### 3.1 Two Degradation Patterns

Both hierarchical and tag-based systems undergo degradation. However, the nature of degradation differs fundamentally:

| Dimension | Hierarchical Systems | Tag-based Systems |
|-----------|---------------------|-------------------|
| **Symptom** | Information becomes unfindable | Information becomes ambiguous |
| **Mechanism** | Disappearing into depth | Blurring through inconsistency |
| **Cause** | Forgotten storage logic | Inconsistent naming |
| **Technical Problem** | Retrieval | Precision |

**Hierarchies:** With increasing depth and breadth of the structure, the probability decreases that a searcher can reconstruct the storage logic of the original filer. Information doesn't "disappear" physically but practically—it is present but not findable.

**Tags:** With increasing numbers of contributors and increasing time distance, inconsistent naming emerges. Synonyms, spelling variants, and semantic drift lead to related objects being filed under different tags. Information "blurs"—it is findable but incomplete or embedded in wrong contexts.

### 3.2 The Asymmetry of Intelligence

A fundamental structural difference concerns the localization of ordering knowledge:

**Hierarchical systems** store ordering knowledge in the container. A directory "knows" something about its contents—namely that they belong to a certain category. The object itself "knows" nothing about itself. If moved, it loses its categorical membership. The system is *externally intelligent, internally uninformed*.

**Tag-based systems** store ordering knowledge in the object. A file with tags carries its categorical membership with it. It can reside in any container—or none at all—without losing information. The system is *internally intelligent, externally agnostic*.

This asymmetry has consequences for portability and resilience: self-describing objects can be migrated between systems without losing meaning. Context-dependent objects are bound to their original environment.

### 3.3 The Cognitive Dynamic

The practical superiority of self-describing systems is amplified by a cognitive asymmetry:

**The storage context** is determined by the current project, the present question, the available time, the momentary understanding of order. The decision about where something is filed reflects this context and is frozen in the structure.

**The search context** is typically different. Different question, different time, changed understanding. The person searching is cognitively not the same as the person who filed—even if physically the same person.

Hierarchical systems demand that the search context reconstruct the storage context. Finding presupposes transposing oneself back into the logic of filing. This demand is systematically difficult to fulfill—not due to individual forgetfulness but due to the structural divergence between storage and search contexts.

Tag-based systems decouple these contexts. What is filed is a description of *what the object is*—not *where it belongs*. The "where" is computed at runtime, based on the current question.

---

## 4. Self-Description as Paradigm Shift

### 4.1 Distributed vs. Local Meaning

The preceding analysis can be condensed to a more abstract point:

> In hierarchical systems, meaning is **distributed**—it derives from position in the structure.
>
> In tag-based systems, meaning is **local**—it is fully contained in the object itself.

This distinction is analogous to the difference between relational databases (where a record's meaning derives from its relations) and document-oriented databases (where each document is self-describing).

### 4.2 The Semantic Web: The Right Idea, the Wrong Means

The idea of self-describing information units is not new. The Semantic Web, promoted by the W3C since the early 2000s, is based on the same fundamental idea: information should be annotated so that it is interpretable and machine-linkable without knowledge of the overarching system.

The Resource Description Framework (RDF) forms the formal foundation of this vision. Every statement is encoded as a triple—subject, predicate, object—and thus machine-readable, linkable, interoperable. Building on this, ontology languages like OWL (Web Ontology Language) enable the formal definition of concepts and their relationships.

The vision was correct. The implementation, however, proved too complex for broad adoption:

**Formal ontologies:** Defining concept hierarchies and relations in OWL requires considerable expertise and upfront planning.

**Special serialization formats:** RDF/XML, Turtle, N-Triples—formats that are neither human-readable nor editable with standard tools.

**Inference engines:** To exploit OWL's possibilities, reasoning engines are needed that derive implicit statements from explicit ones.

**Cognitive overhead:** Creating and maintaining RDF data requires an understanding of formal logic that goes beyond everyday knowledge work.

The result: the Semantic Web has arrived in specialized applications—Linked Open Data in the cultural heritage sector, Wikidata, biomedical ontologies—but never in the broad practice of knowledge organization.

### 4.3 The Current Convergence as Realization of the Semantic Web Vision

The tool generation described here achieves functionally similar effects to RDF—self-description, linkability, interoperability—but with radically lower barriers to entry:

| Semantic Web | Current Tools |
|--------------|---------------|
| RDF triples | YAML frontmatter, tags |
| OWL ontologies | Emergent tag structures |
| SPARQL queries | Full-text search + filters |
| Formal inference | LLM-assisted harmonization |

The crucial difference: the current architecture is based on plaintext and human-readable conventions rather than formal languages. A Markdown file with YAML frontmatter is readable by both humans and machines—without special tools, without prior knowledge of formal ontologies.

One could formulate: the current tool generation realizes the Semantic Web vision using the means of everyday human practice rather than formal knowledge representation. Or, from another perspective: it realizes the Semantic Web vision using the means of Unix philosophy—plaintext, small tools, composability.

### 4.4 Consequences

**Portability:** A Markdown file with YAML frontmatter works in Obsidian, in a Git repository, as input for a static website generator, or read with any text editor. The meaning is not bound to a system.

**Resilience:** When the managing system disappears, self-describing data remains understandable. Proprietary databases die with their software. Plaintext with metadata survives the software generations that process it.

**Composability:** Self-describing units can be combined into new structures not anticipated at their creation. This is the technical foundation of associativity: connections arise ad hoc, not according to plan.

**Connectivity to LOD:** Linking to Linked Open Data resources (GND, Getty AAT, Wikidata) can be added as a subsequent mapping layer—without the data needing to be modeled in RDF from the start.

### 4.5 Condensed Formulation

> Hierarchies store position. Tags store meaning. Position is fragile; meaning is portable.

---

## 5. Objections and Considerations

### 5.1 Scaling

**Objection:** With very large data volumes, flat structures with tags become inefficient—both for human navigation and machine processing.

**Consideration:** This objection confuses conceptual properties with implementation details. Scaling problems are solvable through established techniques: hashing for constant access times, indexing for efficient search, caching for frequent queries.

The relevant question is not whether flat structures can be efficiently implemented for millions of objects (they can), but whether humans can work with such volumes. Here lies the real problem—but it is not a problem of tag architecture per se, but a problem of tool design.

### 5.2 Governance and Compliance

**Objection:** Regulated industries require defined taxonomies, traceable audit trails, and legally binding versioning. An emergent tag structure cannot meet these requirements.

**Consideration:** This objection overlooks that governance requirements do not require the abolition of tags, but their discipline. Regulatory categories (retention periods, confidentiality levels, compliance relevance) can be implemented as tags—with the difference that they do not emerge but come from a controlled vocabulary.

The hierarchical perspective is thereby not abolished but becomes one of several possible views on the same data pool. The data remains in the pool; the compliance view is a projection based on specific tags.

### 5.3 Tag Drift and Inconsistency

**Objection:** With many contributors, inconsistent naming inevitably emerges: synonyms, spelling variants, semantic drift. Without ontological predefinition or elaborate governance, the data pool degrades to "tag soup."

**Consideration:** This objection holds. The folksonomy research of the 2000s (Del.icio.us, Flickr) showed that purely emergent tag systems without any governance tend toward inconsistency.

However, the alternative—hierarchical filing—is not immune to degradation. It just degrades differently: not through inconsistency but through inaccessibility. Information disappears into depth rather than blurring.

The relevant question is therefore not which system is free of degradation (neither is), but which degradation pattern is easier to compensate for—and what new compensation possibilities are available today.

---

## 6. The Question of Novelty

### 6.1 The Legitimate Objection

Information science has studied the concepts described here for decades. Faceted classification goes back to S.R. Ranganathan in the 1930s. Folksonomy research in the 2000s empirically analyzed tag systems. The Semantic Web formulated self-describing data as an architectural principle.

What, then, could be new about the current development?

### 6.2 Three Candidates for Genuine Contributions

#### 6.2.1 The Resolution of the Store-Search Asymmetry

Historically, storing and searching were separate operations with different optimization goals. Organization was necessary *because* search was expensive. One invested effort in storing to save effort in searching.

The radical cheapening of search—through full-text indexing, semantic search, and most recently through Large Language Models—fundamentally changes this economy. When search is nearly free, organization loses its instrumental justification.

**Thesis:** We are witnessing not the replacement of one organizational form by a better one, but the *end of organization as necessity*. Tags are then not an alternative to hierarchies but a description language for objects that no longer need to be "organized."

Information science has hardly systematically considered this possibility because it proceeds from the premise that organization is necessary.

#### 6.2.2 The Emergence of Structure from Description

The classical sequence in information processing is:

1. Define structure (schema, ontology, taxonomy)
2. Insert data (according to the defined structure)
3. Query (within the defined structure)

The emergent sequence is:

1. Describe data (through tags, metadata, links)
2. Query (by arbitrary criteria)
3. Generate structure (as a result of the query)

**Thesis:** Structure changes from something given to something computed. It does not exist as a persistent property of the data pool but arises at the moment of the query and passes with it.

This temporalization of structure has consequences that are perhaps not fully explicated: What does "order" mean in a system where order does not exist but happens?

#### 6.2.3 Redundancy as Optionality

Hierarchical systems enforce uniqueness: an object has one location. Redundancy is considered problematic—it creates inconsistency risks and storage costs.

In tag-based systems, multiple membership is constitutive. Each additional tag is a potential access path. Redundancy becomes a feature: it stores *optionality*—possibilities of access not used today but potentially relevant tomorrow.

**Thesis:** The information-theoretic evaluation of redundancy changes in self-describing systems. Redundancy is not noise but stored potential.

Questions that follow: Is there a formal relationship between the number of tags per object and its findability? How does the entropy of a tag-based system relate to that of a hierarchical one?

---

## 7. Synthesis: The Temporalization of Order

### 7.1 The Common Core

The three candidates for novelty can be traced to a common core:

- 6.2.1 says: Organization becomes optional because search is good enough.
- 6.2.2 says: Structure emerges at runtime, not in advance.
- 6.2.3 says: Multiple membership keeps options open.

What connects these statements?

**The displacement of order from the past into the present.**

### 7.2 Retrospective vs. Prospective Architectures

Hierarchical systems are *retrospective*: they preserve an ordering decision made at the time of storage. The structure is an artifact of past intentions. Searching means transposing oneself back into this past logic.

Tag-based, self-describing systems are *prospective*: they keep ordering options open for future, presently unknown questions. Structure emerges at the moment of the query, shaped by the present context, not the past.

### 7.3 A Different Temporality of Information

This distinction is not primarily technical. It concerns the relationship between information and time.

In retrospective architectures, order is something *given*—a state produced by past decisions and encountered in the present.

In prospective architectures, order is something *becoming*—a process that takes place in the present and is triggered by present questions.

**Central Thesis:**

> The structural core of the current transformation of information architectures is the shift from retrospective to prospective order—from structure as artifact to structure as event.

---

## 8. The Role of Large Language Models

### 8.1 The Historical Dilemma

Folksonomy research identified a dilemma:

**Top-down (Taxonomy):** Controlled vocabularies ensure consistency but require considerable governance effort and scale poorly with the number of contributors and the dynamics of the knowledge domain.

**Bottom-up (Folksonomy):** Emergent tag systems are flexible and scale well but tend toward inconsistency ("tag soup").

Neither approach fully solves the problem. Top-down is too rigid; bottom-up is too chaotic.

### 8.2 A New Possibility

Large Language Models open a third path: *post-hoc harmonization*.

LLMs can:

- Make implicit ontologies in a tag pool explicit
- Recognize and merge synonyms and spelling variants
- Suggest hierarchical relationships between tags
- Flag inconsistencies and generate correction suggestions
- Generate tagging suggestions based on content

This makes a third option conceivable:

**Emergent + harmonized:** Tags arise from contributors' practice (bottom-up) but are continuously harmonized through AI-assisted analysis (without central governance).

### 8.3 Significance for the Thesis

The combination of:

1. Flat data structure (plaintext + metadata)
2. Multiple relationality (tags, links)
3. AI-assisted consistency maintenance

could resolve the historical dilemma between taxonomy and folksonomy.

This is a contribution that could not have been formulated in 2015. The technical possibility of harmonizing emergent structures without central governance is new.

---

## 9. Application: Controlled Vocabularies in Cultural Heritage

### 9.1 The Classical Approach

Projects developing controlled vocabularies—such as thesauri for collections in the cultural heritage sector—typically follow the top-down paradigm:

1. Experts collaboratively define a vocabulary
2. The vocabulary is structured according to standards (ISO 25964)
3. Results are linked to existing authority data (GND, Getty AAT, Wikidata)
4. Collections catalog their objects using the defined vocabulary

This approach requires considerable coordination effort. Typically, workshop series over several years are organized to achieve the necessary interdisciplinary alignment.

### 9.2 The Challenge

Expertise is distributed among individual collections. Each collection has its own terminological practice arising from its history, collection profile, and disciplinary culture. The thesaurus attempts to unify this distributed practice.

The problem: unification must happen *before* cataloging. Collections can only begin standardized capture when the vocabulary is defined. This creates waiting times and friction losses.

### 9.3 An Alternative Perspective

The approach developed here suggests a different sequence:

1. Collections catalog their objects with their *own* terminological practice
2. Terminological practices are collected and analyzed
3. Synonyms, overlaps, and implicit hierarchies are identified (potentially AI-assisted)
4. The thesaurus *emerges* from practice rather than preceding it

This would mean:

- Cataloging can begin immediately without waiting for the vocabulary
- The vocabulary reflects actual terminological practice rather than normatively set categories
- Interoperability with authority data arises through mapping, not pre-fitting

### 9.4 FAIR Principles and Self-Description

The FAIR Principles (Findable, Accessible, Interoperable, Reusable) fundamentally require self-describing data. An object should be interpretable without knowledge of the overarching system.

An object whose meaning derives from its position in a collection hierarchy is less FAIR than one that explicitly carries its categorization as metadata.

Tag-based cataloging is thus not only compatible with FAIR but constitutively closer to it than hierarchical cataloging.

### 9.5 Linked Open Data as Bridge

Linking local terms to global authority data (GND, Getty AAT, Wikidata) is fundamentally a mapping problem: How is a collection's local terminological practice translated into an overarching vocabulary?

This mapping need not happen comprehensively and in advance. It can happen point-by-point and on-demand: when a collection links one of its terms to a GND entry, interoperability arises for that term. The links accumulate over time.

The pragmatic middle path: Collections work with simple, self-describing formats (plaintext, tags, YAML). Interoperability with the Linked Open Data world arises through subsequent mapping to RDF—not through upfront modeling in RDF. The complexity of the Semantic Web becomes an optional export layer, not a prerequisite for daily work.

---

## 10. Research Questions

The preceding analysis opens several research directions:

### 10.1 Empirical Questions

1. Under what conditions does a tag-based architecture outperform a hierarchical one regarding retrieval quality?
2. How does tag consistency develop over time in systems with/without AI-assisted harmonization?
3. What minimal description requirements must an object meet to remain findable for unknown future questions?

### 10.2 Theoretical Questions

1. How can the retrospective/prospective distinction be formalized in information-theoretic terms?
2. Is there a formal relationship between tag redundancy and findability?
3. What properties must a system have for structure to count as "computed" rather than "given"?

### 10.3 Design Questions

1. How must tools be designed that support prospective information architectures?
2. What forms of AI-assisted harmonization are effective without destroying the flexibility of emergent systems?
3. How can the advantages of controlled vocabularies be combined with the flexibility of emergent tags?

---

## 11. Theoretical Connections

The developed theses connect to several research traditions:

### 11.1 Cognitive Science

Prototype theory (Rosch) shows that human categorization does not work through necessary and sufficient conditions but through family resemblances and prototypical examples. Tag-based systems map this structure better than hierarchical taxonomies.

Spreading activation models of memory describe recall as associative activation in a network. The network structure created by bidirectional links corresponds to this modeling.

### 11.2 Process Philosophy

The distinction between structure as given and structure as becoming corresponds to the process-philosophical distinction between substance and event (Whitehead). Information would then be primarily not a stock but a process.

### 11.3 Information Theory

The revaluation of redundancy—not as noise but as optionality—possibly requires a revision of information-theoretic fundamentals. The entropy of a tag-based system might need to be measured differently than that of a hierarchical one.

### 11.4 Library and Information Science

The faceted classification tradition (Ranganathan) laid the foundations for non-hierarchical ordering. The development described here can be understood as a technical realization of this tradition under changed technological conditions.

---

## 12. Conclusion

The convergence of current knowledge management tools on a common architecture—plaintext, tags, multiple relationality—is no coincidence. It responds to a structural problem: the inadequacy of retrospective ordering systems for knowledge pools that must be managed under conditions of complexity, changeability, and multiple access perspectives.

The central thesis of this paper holds that the observed shift goes beyond technical improvement. It marks a change in the temporality of order: from structures that preserve past decisions to structures that emerge at the moment of the query.

This shift is enabled by the radical cheapening of search and—prospectively—by the possibility of AI-assisted harmonization of emergent structures.

The practical implications concern the design of tools, the conception of cataloging projects in the cultural heritage sector, and beyond that every domain in which information must be organized.

The theoretical implications concern the understanding of what "order" means in information systems—and possibly beyond that the relationship between information, structure, and time.

---

## References

*(Selected references for further reading)*

**Faceted Classification:**
- Ranganathan, S.R. (1967): Prolegomena to Library Classification. Asia Publishing House.

**Folksonomy Research:**
- Shirky, C. (2005): Ontology is Overrated: Categories, Links, and Tags.
- Golder, S.A. & Huberman, B.A. (2006): Usage Patterns of Collaborative Tagging Systems. Journal of Information Science.

**Semantic Web:**
- Berners-Lee, T., Hendler, J. & Lassila, O. (2001): The Semantic Web. Scientific American.
- W3C (2014): RDF 1.1 Primer. https://www.w3.org/TR/rdf11-primer/
- W3C (2012): OWL 2 Web Ontology Language Primer. https://www.w3.org/TR/owl2-primer/

**Personal Knowledge Management:**
- Matuschak, A.: Evergreen Notes. https://notes.andymatuschak.org/

**Cognitive Science:**
- Rosch, E. (1975): Cognitive Representations of Semantic Categories. Journal of Experimental Psychology.
- Lakoff, G. (1987): Women, Fire, and Dangerous Things. University of Chicago Press.

**Information Architecture:**
- Morville, P. & Rosenfeld, L. (2006): Information Architecture for the World Wide Web. O'Reilly.

**FAIR Principles:**
- Wilkinson, M.D. et al. (2016): The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data.

**Unix Philosophy:**
- Raymond, E.S. (2003): The Art of Unix Programming. Addison-Wesley.

---

*This paper is conceived as a discussion basis and does not claim completeness of argumentation or literature base.*
