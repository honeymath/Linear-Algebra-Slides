# AA-0001: Linear Algebra Slides — System Architecture Analysis

**Status:** Confirmed (author-interviewed)
**Date:** 2026-02-24
**Analyst:** architect
**Scope:** Full repository structure, design philosophy, pedagogical architecture, and technical infrastructure
**Validation:** Author interview conducted 2026-02-24; key design decisions confirmed and corrected

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

**Author-confirmed context:** `main.tex` serves a dual role beyond compilation. The author's vim setup compiles directly from this file and uses keybindings to jump from any `\input{...}` line into the corresponding file. The commented-out `\input` lines therefore function simultaneously as: (1) a **curriculum table of contents**, (2) a **compilation toggle** for selecting which topics to build, and (3) a **navigation index** for the author's vim workflow. This triple function explains why all 43 entries are retained even when commented out.

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

**Author-confirmed rationale:** The coffee shop metaphor is motivated by the author's conviction that **linear algebra is fundamentally about learning linear combinations**. The narrative deliberately weakens the "linear transformation" framing at the introductory stage — students should first understand combining ingredients (linear combination) before encountering the abstraction of maps between spaces. The emoji characters and dialogue format lower the perceived abstraction barrier and create a distinctive, memorable learning experience. The character dialogues (e.g., `\no`, `\buxie`, `\sinister` arguing about what counts as a vector) are considered important pedagogical content and must be preserved in any reconstruction.

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

**Author-confirmed rationale:** This system is grounded in a deep philosophical observation the author describes as **"万物都是映射" (everything is a map)**. The key insight: if a space contains $n$ vectors $v_1, \ldots, v_n$, this is really a map $\mathbb{R}^n \to V$. Under this lens:

- **Linear independence** is exactly **injectivity** of this map
- **Span** is exactly the **image** of this map
- **Basis** is exactly **bijectivity** (isomorphism)

The classification system makes this unity visible:

- **Red** (`LI` = "Language of Injective"): uniqueness, independence, injectivity, kernel, left-side properties
- **Blue** (`LS` = "Language of Surjective"): existence, spanning, surjectivity, image, right-side properties
- **Purple**: isomorphism, invertibility, basis — where both hold simultaneously

The author states: "线性代数本质是把一套相同的东西在不同的语境去说" (linear algebra is essentially saying the same thing in different contexts). The classification system exists precisely because the author **resents** this phenomenon in standard textbooks — the same structural fact appears under different names in different chapters, and students never see the unity. The `LI`/`LS` tags annotate every definition and theorem to constantly remind students that many propositions share a single source.

This classification system is further developed and systematized in the companion textbook at `../Linear-Algebra-Notes/oldtextbook`.

**This is the non-negotiable pedagogical core of the slides and must be preserved exactly in any reconstruction.**

### 3.3 Decision: Custom DSL Over Standard Beamer

**Codebase evidence:**

Rather than using standard Beamer frame syntax, the author built multiple layers of custom DSL:

1. **Frame DSL** (`\aaa`, `\a`): Recursive macro system that auto-generates frames. Content authors never write `\begin{frame}`.

2. **Matrix DSL** (`\m`, `\t`): Comma-delimited syntax where `\m 12,34.` produces a 2x2 matrix. The `\t` macro produces tables with emoji headers. This is defined via active character manipulation (`packaga.tex:200-230`).

3. **Unicode DSL** (`unicodechar.tex`): A custom tokenizer that allows writing `ℝ^{n × n}` with actual Unicode characters instead of `\mathbb{R}^{n \times n}`.

4. **Layout DSL**: `\co5` instead of `\column{0.5\textwidth}`. `\[columns]{...}`, `\[equation]{...}`, `\[itemize]{...}`.

**Author-confirmed rationale:** The DSL was built purely for **authoring speed in the pre-AI era**. The author states: "我当时写这些东西的时候没有AI...我不可能打很多 `\begin{frame}\end{frame}`" (When I wrote these there was no AI... I can't possibly type many `\begin{frame}\end{frame}`). Every shorthand exists to reduce keystrokes for a single human author working in vim.

The Unicode infrastructure (`unicodechar.tex`) was similarly motivated by the author's vim workflow — custom keybindings allowed typing `ℝ` in two keystrokes, and using standard LaTeX escapes made it impossible to visually parse the source while writing. The design was "为了对我自己友好" (to be friendly to myself).

**Author-confirmed reconstruction decision:** The entire DSL layer is now **approved for migration to standard LaTeX**. The author explicitly confirms:

| Component | Reconstruction Decision |
|-----------|----------------------|
| `\aaa`/`\a` frame system | **Migrate** to standard `\begin{frame}...\end{frame}` |
| `\m`/`\t` matrix/table DSL | **Migrate** to standard `\begin{pmatrix}`, `\begin{tabular}`, etc. |
| `unicodechar.tex` | **Remove**; convert all Unicode math to standard LaTeX notation |
| `\co` layout shorthand | **Migrate** to standard `\column{...}` |

The rationale: "现在是AI时代了，一切都变了" (Now it's the AI era, everything has changed). The maintainer is no longer a single human — it is the author plus AI tools. Standard LaTeX is what AI models understand natively, and the custom DSL **obstructs error location tracking** during compilation.

**Observed consequence:** The DSL is powerful but deeply idiosyncratic. It creates a high barrier for AI-assisted maintenance. The `\aaa`/`\a` frame system, in particular, uses obscure TeX primitives (`\expandafter`, `\@gobble`, `\catcode`) that make compilation errors extremely difficult to trace back to their source location.

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

**Author-confirmed rationale:** The matrix-first ordering is a **deliberate methodological stance**, not an accident of organic growth. The author states: "我想说所有计算必须通过matrix的等式得到，禁止那种飘忽不定的语言叙述" (I want to say all computation must be obtained through matrix equations — prohibit that vague, drifting verbal narration). Matrix computation is placed first to establish the **discipline of precise symbolic expression** before any abstraction is introduced.

The author further states: "我恨普通教材，我教了10年线性代数，就是从对普通教材的恨开始的" (I hate standard textbooks. I've taught linear algebra for 10 years, and it started from hating standard textbooks). The curriculum ordering represents a conscious rejection of the standard textbook approach (abstract definitions first, computation later).

The `computationalStrategies` and `proofStrategies` meta-modules at the end exist because "普通教材没有" (standard textbooks don't have these) — they are the author's **meta-justification** to students for why the tools taught in this course are effective and superior to the standard approach.

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

Based on author interview and codebase evidence:

1. **~2016–2018**: Earlier versions of slides existed before the current repository. The classification duality system and pedagogical philosophy were developed over years of teaching experience. The author also wrote a companion textbook (`../Linear-Algebra-Notes/oldtextbook`) which systematized the slide content; many slides were migrated into the book rather than the reverse.

2. **2018**: Current slide system established for University of Toronto courses. The Shinchan narrative, emoji system, and custom DSL were present from early on.

3. **2018–2023**: Iterative expansion. The `packaga.tex` infrastructure accumulated macros — the commented-out blocks (lines 866–916 vs. 1519–1580 for emoji definitions) show at least one major refactoring of the shared infrastructure. The author confirms the duplicated emoji block can be cleaned up; the historical reason has been forgotten.

4. **2023**: Adoption at POSTECH. The bilingual comments (Chinese characters in `compile_all_tex.py`, commented Chinese macro alternatives like `%\newcommand{\sur}{\textbf{\color{blue} 满射 }}`) reflect the slides' use across language contexts.

5. **2025**: Public release on GitHub with CC BY-NC-SA 4.0 license, QR code support (`\usepackage{qrcode}`), and ORCID identification.

6. **2026**: `2026-reconstruction` branch initiated. Goal: migrate from personal DSL to standard LaTeX for AI-assisted maintenance, while preserving all pedagogical content.

### 4.2 Pedagogical Motivation (Author-Confirmed)

The slides embody a distinctive pedagogical philosophy, confirmed and elaborated by the author:

1. **"Explain matrix multiplication to elementary school students"** (`matrix.tex:29`) — this literal directive in the slides reveals the target: make abstract algebra accessible through concrete, everyday metaphor. Linear algebra is fundamentally about **linear combinations**, and this should be graspable before any abstract framework is introduced.

2. **Matrix-first as methodological discipline** — "所有计算必须通过matrix的等式得到，禁止那种飘忽不定的语言叙述" (all computation must be obtained through matrix equations — prohibit vague verbal narration). This is a conscious rejection of standard textbooks that the author describes with the word "恨" (hate), developed over 10 years of teaching.

3. **Visual-geometric grounding** — TikZ diagrams pervade the slides. The `lineartransformation.tex` module explicitly asks students to perform matrix multiplication "purely geometrically" before introducing algebraic formulations.

4. **"万物都是映射" (Everything is a map)** — the philosophical foundation of the entire classification system. The course arc moves from introducing red/blue concepts separately, to showing how they interact, to culminating in purple (invertibility/isomorphism) as the resolution. This mirrors the mathematical structure itself, and the author's goal is to make students **see** this unity rather than memorize disconnected facts.

5. **Speed and fluency as goals** — `eigenvalues.tex:56`: "When eigenvalues are given, finding eigenvectors is extremely easy, you should able to be compute within 10 seconds in mind." The slides emphasize computational fluency as a prerequisite for theoretical understanding.

6. **Meta-justification modules** — `computationalStrategies` and `proofStrategies` exist not as review but as **advocacy**: the author argues explicitly to students why the tools taught in this course are effective, filling a gap that "普通教材没有" (standard textbooks don't have).

### 4.3 Design Principles (Author-Confirmed)

| Principle | Evidence | Author Statement |
|-----------|----------|-----------------|
| **Concrete before abstract** | Shinchan's coffee shop precedes formal definitions in every foundational module | "线性代数其实是在学习线性组合" — weaken transformation framing at entry |
| **Matrix equations as discipline** | `matrix` is first topic; all computation channeled through matrix notation | "禁止那种飘忽不定的语言叙述" — prohibit vague narration |
| **Visual before symbolic** | TikZ diagrams precede algebraic formulations; `\org`, `\grid` helpers optimized for quick diagram authoring | — |
| **万物都是映射 (Everything is a map)** | Red/blue/purple classification system; existence vs. uniqueness framing of every concept | "线性代数本质是把一套相同的东西在不同的语境去说" |
| **Each lecture is self-contained** | No cross-file references; independent compilation; modular inclusion via `main.tex` | — |
| **Informal language lowers barriers** | Character dialogue, emoji, casual phrasing ("Can you help Shinchan?") mixed with rigorous definitions | Content and characters are important to students; must be preserved |
| **Meta-justification of method** | Dedicated `computationalStrategies.tex` and `proofStrategies.tex` as final modules | "普通教材没有" — standard textbooks lack this |

### 4.4 Relationship to Companion Textbook

The author maintains a companion textbook at `../Linear-Algebra-Notes/oldtextbook`. The relationship is:

- The **slides came first**; the textbook systematized and expanded the slide content
- The classification duality system (`LI`/`LS`) is more fully developed in the textbook
- The slides and book now **evolve independently** — the current reconstruction focuses on slides only
- The textbook is not planned for reconstruction at this time

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

### 5.2 Weaknesses (Confirmed Migration Targets)

| Weakness | Detail | Reconstruction Status |
|----------|--------|----------------------|
| **Custom DSL blocks AI maintenance** | `\aaa`, `\a`, `\m`, `\t` — AI cannot generate or debug these; error tracing is broken | **Approved for migration** to standard LaTeX |
| **Unicode source blocks AI generation** | `unicodechar.tex` tokenizer means source uses non-standard character input | **Approved for removal** |
| **Monolithic infrastructure** | `packaga.tex` at ~1700 lines bundles all concerns; any change risks breaking all 43 modules | Future ADR to decide modularization |
| **Naming inconsistencies** | `CalayHamiltonTheorem` (Cayley), `LanguarangeInterpolationPolynomial` (Lagrange), `SpecutralDecompositionForRepeatedRoots` (Spectral), `sigularValueDecomposition` (Singular) | **Approved for correction** |
| **Duplicated macro blocks** | Emoji commands defined twice in `packaga.tex` (commented + active) | **Approved for cleanup** |
| **No cross-references** | Cannot reference a theorem from one module in another; no unified numbering | By design (module independence); no change planned |
| **Flat file structure** | 43 `.tex` files at root mixed with infrastructure files | No change planned at this time |

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

## 7. Reconstruction Plan (Author-Approved)

### 7.1 Immutable: Pedagogical Content Layer

The following must be **preserved exactly** during reconstruction — these are the intellectual core:

- **All slide content**: mathematical exposition, examples, exercises, proofs
- **Red/blue/purple classification system**: `\LI`, `\LS`, `\inj`, `\sur`, `\iso` and all related macros
- **Narrative elements**: Shinchan's coffee shop, emoji characters, character dialogues
- **Curriculum ordering**: the sequence in `main.tex` reflects deliberate pedagogical decisions
- **Module independence**: each topic must remain independently compilable
- **`tcolorbox` theorem environments**: `defi`, `prop`, `thm`, `lem`, `cor`, `exa`, `rem`, `summ`

### 7.2 Migrate: DSL to Standard LaTeX

The following custom syntax should be **replaced with standard LaTeX equivalents**, preserving identical PDF output:

| Component | Current | Target | Priority |
|-----------|---------|--------|----------|
| Frame system | `\aaa{Title}...\a\aa...\aaa` | `\begin{frame}{Title}...\end{frame}` | High — blocks error tracing |
| Matrix DSL | `\m 12,34.` | `\begin{pmatrix}1&2\\3&4\end{pmatrix}` | High — AI cannot generate custom syntax |
| Table DSL | `\t{}\milk\coffee,...` | `\begin{tabular}...\end{tabular}` | High |
| Unicode math | `ℝ`, `ℂ`, `×`, `∈` in source | `\mathbb{R}`, `\mathbb{C}`, `\times`, `\in` | Medium — bulk find-replace |
| Layout shorthand | `\co5` | `\column{0.5\textwidth}` | Low |
| `unicodechar.tex` | Custom tokenizer + active char redefs | **Remove entirely** | Medium — after Unicode conversion |

### 7.3 Clean Up: Infrastructure Hygiene

| Area | Action | Author Approval |
|------|--------|----------------|
| **Filename misspellings** | Rename: `CalayHamiltonTheorem` → `CayleyHamiltonTheorem`, `LanguarangeInterpolationPolynomial` → `LagrangeInterpolationPolynomial`, `SpecutralDecompositionForRepeatedRoots` → `SpectralDecompositionForRepeatedRoots`, `sigularValueDecomposition` → `SingularValueDecomposition` | Approved — no external link concerns |
| **Duplicated emoji macros** | Remove commented-out block (lines 866–916 of `packaga.tex`) | Approved — historical reason forgotten |
| **`packaga.tex` modularization** | Consider splitting into focused files | To be decided in future ADR |

### 7.4 Reconstruction Process

The author's stated approach:
1. Write a **reconstruction ADR** defining the migration strategy and standards
2. Migrate content **incrementally**, one module at a time
3. Validate each migration by comparing PDF output before and after
4. Engineering work to be delegated to AI-assisted agents after ADR is established

---

## Cross-References

- Inspired by: Initial codebase survey for `2026-reconstruction` branch
- Next action: ADR for reconstruction strategy (DSL → standard LaTeX migration)
- Related: `../Linear-Algebra-Notes/oldtextbook` — companion textbook with systematized classification theory
- Future: DA (Design Analysis) of individual module migration patterns
