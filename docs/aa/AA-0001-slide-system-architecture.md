# AA-0001: Linear Algebra Slides — System Architecture Analysis

**Status:** Reconstructed
**Date:** 2026-02-24
**Analyst:** architect
**Scope:** Full repository structure, design philosophy, pedagogical architecture, and technical infrastructure

---

## 1. System Overview

This repository contains a complete set of lecture slides for a university-level Linear Algebra course, authored by Qirui Li (ORCID: 0000-0002-6042-1291), in active use since 2018 at the University of Toronto and POSTECH (since 2023). The slides are built on LaTeX/Beamer with the Metropolis theme, compiled via `pdflatex`. The repository was published in 2025 under CC BY-NC-SA 4.0.

### 1.1 Quantitative Profile

| Metric | Value |
|--------|-------|
| Content `.tex` files | 43 |
| Shared infrastructure files | 3 (`packaga.tex`, `unicodechar.tex`, `beamer*.sty` x5) |
| Image assets | 70 files (`Pictures/`) |
| Total LaTeX content | ~580 KB across content files |
| Preview PDFs | 41 compiled outputs (`previews/`) |
| Build tooling | 1 Python script (`compile_all_tex.py`) |
| Curriculum topics | 43 discrete lecture modules |

---

## 2. Codebase Evidence: Module Hierarchy

### 2.1 Entry Point and Composition Model

The system uses a **single-entry-point, selective-inclusion model**:

```
main.tex                      ← Entry point
  └── \input{packaga}         ← Shared infrastructure (ALL packages, macros, environments)
      └── \input{unicodechar} ← Unicode math symbol mappings
  └── \input{<topic>}         ← One or more content modules (most commented out)
```

**Evidence** (`main.tex:1-126`): The file lists all 43 content modules. Only `matrix.tex` is currently uncommented (line 18). All others are commented out with `%\input{...}`. This reveals a **toggle-based composition** pattern — the instructor uncomments whichever topics are needed for a given lecture or compilation run.

**Observed consequence:** This is a flat, non-hierarchical inclusion model. There are no subdirectories, no chapter groupings, no intermediate aggregation files. Every content file lives at the repository root alongside infrastructure files.

### 2.2 Shared Infrastructure Layer: `packaga.tex`

The file `packaga.tex` (~1700 lines) is the single shared dependency for all content. Its name is intentionally misspelled (confirmed in `readme.md:22`: "The spelling of 'packaga' is intentional"). It bundles:

| Concern | Lines (approx.) | Evidence |
|---------|-----------------|----------|
| Document class & theme | 1–50 | `\documentclass[10pt]{beamer}`, `\usetheme{metropolis}` |
| Mathematical typesetting packages | 15–50 | `mathrsfs`, `tikz`, `unicode-math`, `polynom`, `xy` |
| Colored theorem environments (`tcolorbox`) | 62–197 | `defi`, `prop`, `thm`, `conj`, `lem`, `cor`, `exa`, `exap`, `exapl`, `rem`, `rema`, `summ` |
| Custom frame/slide macro system | 254–295 | `\aaa`, `\a`, `\D`, `\E`, `\BiajiBiaji`, `\Chi` — a recursive TeX macro DSL for defining slides |
| Shorthand matrix constructors | 200–230, 370–860 | `\m`, `\t`, `\bm` (comma-delimited matrix DSL); `\mm`, `\mmm`, `\mms`, `\upper`, `\loww`, `\diag` (positional argument matrices) |
| Vector/column constructors | 737–860 | `\cc`, `\ccc`, `\cccc`, `\ccccc` and variants (`h`-partitioned, `n`-naked) |
| Mathematical operator macros | 300–363 | `\End`, `\Hom`, `\GL`, `\Spec`, `\Aut`, etc. |
| Pedagogical classification system | 1107–1505 | Color-coded boxed labels: `\LI` (red), `\LS` (blue), `\SI`, `\IS`, `\inj`, `\sur`, `\iso` (purple) |
| Emoji character commands | 1519–1580 | `\apple`, `\bean`, `\milk`, `\coffee`, `\leaf`, `\tea`, `\cola`, `\bento`, `\no`, `\sinister`, `\hi`, etc. |
| TikZ grid/coordinate helpers | 1607–1684 | `\org`, `\grid`, `\wangge`, `\zbx`, `\basisspace` |
| Column layout shorthand | 1684 | `\co` — shorthand for `\column{0.N\textwidth}` |

**Observed consequence:** `packaga.tex` is a **monolithic shared kernel** — every content file depends on it entirely, and it contains no internal modularization. This is a single point of coupling for the entire system.

### 2.3 Unicode Infrastructure: `unicodechar.tex`

This file (~100 lines) performs two extraordinary things:

1. **Active character redefinition** (lines 6–22): Redefines `_` and `^` as active characters that work in both math and text mode, enabling natural Unicode subscript/superscript handling.

2. **A custom parser/tokenizer** (lines 24–47): Implements `\Start`, `\Generate`, `\MatchWord`, `\ReleaseAll` — a TeX-level lexer that tokenizes Unicode mathematical symbols (blackboard bold, calligraphic, Fraktur, Greek letters) and maps them to LaTeX commands. This allows the author to write `ℝ` directly in source rather than `\mathbb{R}`.

3. **Unicode character mappings** (lines 79+): Standard `\newunicodechar` declarations for blackboard bold, calligraphic, and other symbol sets.

**Reconstructed decision:** The author chose to write mathematics using **native Unicode characters** rather than LaTeX escape sequences, then built the parsing infrastructure to support this. This is a highly unconventional and technically ambitious choice that makes the `.tex` source read closer to handwritten mathematics.

### 2.4 Content Module Structure

Each content `.tex` file follows a consistent implicit pattern:

```latex
\aaa{Topic Title}          ← Section-level title slide (via custom macro)
... content ...
\a\aa                      ← Frame continuation / new frame
... content ...
\a{Subtopic Title}         ← Named sub-frame
... content ...
\aaa                       ← Section terminator
```

**Evidence** — consistent across all sampled files:
- `matrix.tex:3`: `\aaa{Learning Objectives}`
- `vectorspace.tex:2`: `\aaa{Vector Spaces}`
- `lineartransformation.tex:4`: `\aaa{Linear Transformations}`
- `CalayHamiltonTheorem.tex:2`: `\aaa{Annihilating polynomial of matrices}`
- `SpectralDecomposition.tex:2`: `\aaa{Spectural decomposition}`

The `\aaa`/`\a` macro system (defined in `packaga.tex:274-283`) is a recursive TeX engine that auto-generates `\begin{frame}...\end{frame}` blocks. The author never writes explicit `\begin{frame}` in content files — the DSL abstracts it entirely.

---

## 3. Reconstructed Design Decisions

### 3.1 Decision: Narrative-Driven Pedagogy via Concrete Metaphor

**Codebase evidence:**

The slides introduce abstract mathematical concepts through a recurring **concrete narrative** centered on a character named "Shinchan" operating a coffee shop. This metaphor is used to ground:

- **Matrix multiplication** (`matrix.tex:36-93`): Ingredients tables for drinks become matrix factors. Combining ingredient tables *is* matrix multiplication.
- **Linear equations** (`nullspace.tex:15-49`): A customer requests a new drink — solving for how to produce it from existing drinks is a linear system.
- **Linear transformations** (`lineartransformation.tex:6-59`): Plotting drink recipes as points, then asking "how to do matrix multiplication purely geometrically."
- **Injective/surjective maps** (`injectiveAndSurjectiveLinearTransformations.tex:4-50`): A restaurant assigning food to customers. The "uniqueness problem" and "existence problem" arise naturally from trying to reverse the assignment.

The emoji infrastructure (`\milk`, `\bean`, `\coffee`, `\tea`, `\cola`, `\bento`, `\leaf`, `\lemon`, `\cow`) directly supports this narrative. There are also character emojis (`\no`, `\buxie`, `\sinister`, `\tear`, `\hi`, `\boss`, `\homework`) representing recurring personas who interact in dialogue format.

**Evidence** (`vectorspace.tex:90-100`):
```latex
\no: Are they vectors also? \fbox{\leaf\bean\bean},\; ...
\buxie: There are no arrows like ...
\no: But I'd still say --- vectors!
\sinister: Actually, you can, as long as you define the addition and
           the scalar multiplication properly!
```

**Reconstructed rationale:** The author deliberately chose a **constructivist pedagogy** — students build mathematical understanding from familiar operations (combining ingredients, assigning orders) before encountering formal definitions. The emoji characters and dialogue format lower the perceived abstraction barrier and create a distinctive, memorable learning experience.

### 3.2 Decision: Color-Coded Classification Duality System

**Codebase evidence** (`packaga.tex:1107-1505`):

The slides implement a systematic **red/blue/purple classification scheme** that pervades the entire course:

| Color | Semantic Domain | Example Macros |
|-------|----------------|----------------|
| **Red** | Uniqueness / Injective / Independence | `\LI`, `\II`, `\DI`, `\NI`, `\RI`, `\inj`, `\li`, `\un`, `\mosto`, `\nofree`, `\kn`, `\des`, `\lc`, `\lf`, `\liv` |
| **Blue** | Existence / Surjective / Spanning | `\LS`, `\SS`, `\CS`, `\DS`, `\NS`, `\RS`, `\sur`, `\exi`, `\leasto`, `\sws`, `\pa`, `\nored`, `\rc`, `\rf`, `\riv` |
| **Purple** | Isomorphism / Invertibility / Both | `\iso`, `\teun`, `\exacto`, `\bas`, `\inve`, `\np`, `\dstws`, `\same` |

The classification tags (e.g., `\LI` renders as a red boxed $L_I$) are used as **margin annotations** on definitions, propositions, and theorems throughout the slides.

**Evidence** (`imageandkernel.tex:29`):
```latex
\[defi]{\LS We define the Image of a map...}
```

**Evidence** (`injectiveAndSurjectiveLinearTransformations.tex:29`):
```latex
\item[B.] \unp: She ordered multiple foods...
\item[C.] \excp: He never order food with us?
```

**Reconstructed rationale:** This is a **grand unifying pedagogical framework** that treats the injective/surjective duality as the central organizing principle of linear algebra. Every concept is tagged by which side of this duality it belongs to:

- Red concepts relate to **uniqueness, independence, injectivity, left-side properties**
- Blue concepts relate to **existence, spanning, surjectivity, right-side properties**
- Purple concepts arise when both are satisfied simultaneously (bijectivity, invertibility, basis)

This classification system extends beyond maps to encompass: numerical properties of matrices, cancellation laws, factorization, null spaces vs. column spaces, and more. It appears to be the author's **original pedagogical contribution** — a consistent visual language that makes the deep structural parallels in linear algebra immediately visible to students.

### 3.3 Decision: Custom DSL Over Standard Beamer

**Codebase evidence:**

Rather than using standard Beamer frame syntax, the author built multiple layers of custom DSL:

1. **Frame DSL** (`\aaa`, `\a`): Recursive macro system that auto-generates frames. Content authors never write `\begin{frame}`.

2. **Matrix DSL** (`\m`, `\t`): Comma-delimited syntax where `\m 12,34.` produces a 2x2 matrix. The `\t` macro produces tables with emoji headers. This is defined via active character manipulation (`packaga.tex:200-230`).

3. **Unicode DSL** (`unicodechar.tex`): A custom tokenizer that allows writing `ℝ^{n × n}` with actual Unicode characters instead of `\mathbb{R}^{n \times n}`.

4. **Layout DSL**: `\co5` instead of `\column{0.5\textwidth}`. `\[columns]{...}`, `\[equation]{...}`, `\[itemize]{...}`.

**Reconstructed rationale:** The author prioritized **source readability** and **authoring speed**. The `.tex` files read almost like pseudocode or lecture notes rather than LaTeX markup. This likely reflects years of iterative refinement for a system that one person writes and maintains extensively.

**Observed consequence:** The DSL is powerful but deeply idiosyncratic. It creates a high barrier for external contributors who must learn the custom macro language before they can contribute. The `\aaa`/`\a` frame system, in particular, uses obscure TeX primitives (`\expandafter`, `\@gobble`, `\catcode`) that would be difficult for most LaTeX users to debug.

### 3.4 Decision: Flat File Organization

**Codebase evidence:** All 43 content files live at the repository root. There are no subdirectories for topic groups, no numbering scheme in filenames, and no manifest file beyond the commented `\input` list in `main.tex`.

The ordering in `main.tex` reveals the **intended curriculum sequence**:

| Phase | Topics | Pedagogical Arc |
|-------|--------|-----------------|
| **Foundations** | `matrix`, `rowoperation`, `LUdecomposition`, `vectorspace` | Concrete computation → abstract structure |
| **Transformations** | `lineartransformation`, `lineartransformationspace`, `matrixOfLinearTransformations`, `inducedLinearTransformations`, `changeOfBasis` | Maps between spaces, representation theory |
| **Algebraic Properties** | `compositionOfLinearTransformations`, `additionOfLinearTransformations`, `powerOfLinearOperators` | Algebraic structure of operators |
| **Injectivity/Surjectivity** | `injectiveAndSurjectiveLinearTransformations`, `imageandkernel`, `leftrightinverseoflineartransformations`, `nullspace`, `leftrightinverse` | The red/blue duality framework |
| **Projections** | `projection`, `projectionoperator`, `compatibleprojections` | Idempotent operators |
| **Inner Product Spaces** | `orthogonality`, `orthogonalprojections`, `datafitting`, `orthonormalbasis` | Geometry enters the picture |
| **Determinant & Eigentheory** | `determinant`, `calculatedeterminant`, `CalayHamiltonTheorem`, `eigenvalues` | Scalar invariants of operators |
| **Spectral Theory** | `LanguarangeInterpolationPolynomial`, `SpectralDecomposition`, `Diagonalization`, `DiagonalizationByCrossFilling`, `linearODE` | Decomposition and applications |
| **Advanced Spectral** | `LagurangeInterpolationPolynomialForRepeatedRoots`, `SpecutralDecompositionForRepeatedRoots`, `normalOperators`, `positiveDefiniteMatrix`, `sigularValueDecomposition` | Repeated roots, special operators, SVD |
| **Meta/Review** | `computationalStrategies`, `proofStrategies` | Exam preparation and synthesis |

**Reconstructed rationale:** The flat structure likely reflects the organic growth of the system — the author added files as topics were taught, rather than reorganizing retroactively. The ordering in `main.tex` serves as the implicit curriculum map.

### 3.5 Decision: Independent Compilation via Preview System

**Codebase evidence** (`compile_all_tex.py`): A Python script that:
1. Takes one or more `.tex` files as arguments
2. For each, generates a temporary `main_temp.tex` that includes only `packaga.tex` + that single file
3. Compiles it via `pdflatex`
4. Moves the output to `previews/<name>.pdf`

This produces 41 standalone PDF previews, one per topic module.

**Reconstructed rationale:** Each content file is designed to be **independently compilable** — it does not depend on any other content file. This enables:
- Selective lecture preparation (compile only the topics needed)
- Preview generation for browsing/sharing
- Parallel development of multiple topics

**Observed consequence:** There are no cross-references between content files — no `\ref`, `\label`, or `\pageref` that span modules. Counter numbering (definitions, theorems, etc.) resets per compilation unit. This is a feature, not a bug: each topic is a self-contained lecture segment.

---

## 4. Regression Analysis: Motivation and Evolution

### 4.1 Authoring Timeline

The evidence suggests the following evolution:

1. **2018**: Initial creation for University of Toronto courses. The Shinchan narrative and emoji system were likely present from early on, given how deeply embedded they are in foundational topics (`matrix.tex`, `vectorspace.tex`).

2. **2018–2023**: Iterative expansion. The flat file structure grew organically as new topics were added. The `packaga.tex` infrastructure accumulated macros — the commented-out blocks (lines 866–916 vs. 1519–1580 for emoji definitions) show at least one major refactoring of the shared infrastructure.

3. **2023**: Adoption at POSTECH. The bilingual comments (Chinese characters in `compile_all_tex.py`, commented Chinese macro alternatives like `%\newcommand{\sur}{\textbf{\color{blue} 满射 }}`) suggest the slides were originally used in a Chinese-speaking context and later adapted for English-language instruction.

4. **2025**: Public release on GitHub with CC BY-NC-SA 4.0 license, QR code support (`\usepackage{qrcode}`), and ORCID identification.

### 4.2 Pedagogical Motivation

The slides embody a distinctive pedagogical philosophy that can be reconstructed from the evidence:

1. **"Explain matrix multiplication to elementary school students"** (`matrix.tex:29`) — this literal directive in the slides reveals the target: make abstract algebra accessible through concrete, everyday metaphor.

2. **Computation-first, then abstraction** — topics like `proofStrategies.tex` and `computationalStrategies.tex` come *last* in the curriculum, as synthesis. The opening topics (`matrix`, `rowoperation`) start with pure computation before any formal definition appears.

3. **Visual-geometric grounding** — TikZ diagrams pervade the slides. The `lineartransformation.tex` module explicitly asks students to perform matrix multiplication "purely geometrically" before introducing algebraic formulations.

4. **The classification duality as structural backbone** — the entire course arc moves from introducing red/blue concepts separately, to showing how they interact, to culminating in purple (invertibility/isomorphism) as the resolution. This mirrors the mathematical structure itself.

5. **Speed and fluency as goals** — `eigenvalues.tex:56`: "When eigenvalues are given, finding eigenvectors is extremely easy, you should able to be compute within 10 seconds in mind." The slides emphasize computational fluency as a prerequisite for theoretical understanding.

### 4.3 Design Principles (Inferred)

| Principle | Evidence |
|-----------|----------|
| **Concrete before abstract** | Shinchan's coffee shop precedes formal definitions in every foundational module |
| **Visual before symbolic** | TikZ diagrams precede algebraic formulations; `\org`, `\grid` helpers optimized for quick diagram authoring |
| **Duality as organizing structure** | Red/blue/purple classification system; existence vs. uniqueness framing of every concept |
| **Source should read like mathematics** | Unicode math input, comma-delimited matrix DSL, minimal LaTeX boilerplate in content files |
| **Each lecture is self-contained** | No cross-file references; independent compilation; modular inclusion via `main.tex` |
| **Informal language lowers barriers** | Character dialogue, emoji, casual phrasing ("Can you help Shinchan?") mixed with rigorous definitions |
| **Exam preparation is architecture** | Dedicated `computationalStrategies.tex` and `proofStrategies.tex` as meta-modules |

---

## 5. Observed Consequences

### 5.1 Strengths

| Strength | Detail |
|----------|--------|
| **Pedagogical coherence** | The red/blue/purple system provides a consistent visual and conceptual framework across the entire course |
| **Authoring efficiency** | The DSL enables rapid slide creation — matrix expressions that would take 5+ lines in standard LaTeX take one line |
| **Module independence** | Any topic can be compiled and distributed independently |
| **Source readability** | Content files are remarkably readable for LaTeX — closer to lecture notes than markup |
| **Battle-tested** | 8+ years of classroom use across two major universities |

### 5.2 Weaknesses

| Weakness | Detail |
|----------|--------|
| **Monolithic infrastructure** | `packaga.tex` at ~1700 lines bundles all concerns; any change risks breaking all 43 modules |
| **Contributor barrier** | The custom DSL (`\aaa`, `\a`, `\m`, `\t`, `\BiajiBiaji`) requires significant learning investment |
| **No cross-references** | Cannot reference a theorem from one module in another; no unified numbering |
| **Naming inconsistencies** | `CalayHamiltonTheorem` (misspelled Cayley), `LanguarangeInterpolationPolynomial` (misspelled Lagrange), `SpecutralDecompositionForRepeatedRoots` (misspelled Spectral), `sigularValueDecomposition` (misspelled Singular) |
| **Flat file structure** | 43 `.tex` files at root mixed with infrastructure files; no directory organization |
| **Duplicated macro blocks** | Emoji commands defined twice in `packaga.tex` (once commented at lines 866–916, once active at lines 1519–1580) |
| **Missing documentation** | No documentation of the DSL syntax, macro API, or the classification system's semantics |

---

## 6. Industry Context

### 6.1 Comparison to Standard Beamer Practices

Standard Beamer presentations use `\begin{frame}{Title}...\end{frame}` blocks, `\begin{theorem}...\end{theorem}` environments, and standard package management. This repository departs radically from convention by:

- Replacing frame syntax entirely with a recursive macro DSL
- Building a custom tokenizer for Unicode mathematics
- Implementing matrix entry via comma-delimited shorthand rather than `pmatrix`/`bmatrix` environments

This is closer to the pattern seen in advanced TeX systems like `ConTeXt` or custom exam/lecture frameworks built by power users over years of classroom use.

### 6.2 Comparison to Open Educational Resources (OER)

Most open-source lecture slide repositories (e.g., MIT OpenCourseWare LaTeX sources, various Overleaf templates) use minimal customization and rely on standard packages. This repository's depth of customization is unusual and reflects a **single-author, long-lifecycle** development pattern rather than a collaborative OER model.

### 6.3 The Classification System in Mathematical Context

The red/blue duality (injective/surjective, unique/exists, independent/spanning) is a well-known structural observation in linear algebra. However, building it into a **visual design system** with color-coded boxed tags that annotate every definition and theorem is, to our knowledge, an original contribution by the author. This approach has parallels with:

- Grothendieck's style of organizing mathematics by structural duality
- Category-theoretic "arrow-reversing" pedagogy
- But applied at the undergraduate instruction level with visual affordances

---

## 7. Recommendations

### 7.1 Preserve As-Is

- **The pedagogical architecture** (narrative metaphor, classification duality, concrete-before-abstract arc) is the core intellectual contribution and should not be altered
- **The DSL** (`\aaa`, `\m`, `\t`) is deeply embedded and battle-tested; replacing it would require rewriting all 43 content files
- **Module independence** is a valuable property that should be maintained in any restructuring

### 7.2 Candidates for Evolution

| Area | Recommendation | Rationale |
|------|---------------|-----------|
| **`packaga.tex` modularization** | Consider splitting into `theme.tex`, `math-macros.tex`, `classification.tex`, `emoji.tex`, `tikz-helpers.tex` | Reduces blast radius of changes; enables selective loading |
| **Directory organization** | Group content files into phase directories (`01-foundations/`, `02-transformations/`, etc.) | Improves navigability; makes curriculum structure visible in filesystem |
| **Filename corrections** | Fix misspellings in filenames (Cayley, Lagrange, Spectral, Singular) | Reduces confusion for external contributors |
| **DSL documentation** | Create a `docs/dsl-reference.md` documenting the macro API | Critical for onboarding contributors during reconstruction |
| **Remove duplicated macros** | Clean up the commented-out emoji block (lines 866–916) in `packaga.tex` | Reduces confusion about which definitions are active |

### 7.3 Relationship to Current Reconstruction Branch

The `2026-reconstruction` branch provides an opportunity to address the structural issues (7.2) while preserving the pedagogical architecture (7.1). Any refactoring should be validated by ensuring all 41 preview PDFs compile identically before and after changes.

---

## Cross-References

- Inspired by: Initial codebase survey for `2026-reconstruction` branch
- May inspire: ADR for `packaga.tex` modularization, ADR for directory restructuring
- Related: Future DA (Design Analysis) of the `\aaa`/`\a` frame macro system internals
