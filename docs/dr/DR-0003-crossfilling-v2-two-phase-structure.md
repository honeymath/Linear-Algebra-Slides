# DR-0003: crossfilling-v2.tex Two-Phase Structure Design

**Status:** Completed
**Date:** 2026-03-03
**Author:** Engineer (Claude Sonnet 4.5)
**References:**
- math-slides-authoring skill
- DR-0002 (rowoperation.tex quality standards)
- RET-0002 (rowoperation.tex execution lessons)
- content-creation-guidelines.md
- Original crossfilling.tex (v1)

---

## Decision Context

This document records the design decisions made during the creation of `crossfilling-v2.tex`, a complete rewrite of the cross-filling method slides for Lecture 3 (MATH203, Week 2).

### The Problem

The original `crossfilling.tex` violated critical math-slides-authoring principles:

1. **No two-phase structure** - Used pure mathematical notation throughout, skipping emoji concretization
2. **Definition → Text Explanation → Example** - Wrong order for passive attention
3. **Premature abstraction** - Introduced abstract symbols ($\mathbf{u}, \mathbf{v}^T$) immediately in definitions
4. **No "Change of Perspective" transition** - Students never told when abstraction level changes
5. **Missing 5-frame sequences** - Concepts introduced without detailed step-by-step visual grounding

### User Feedback

> "你按照 /math-slides-authoring 的技能，来检查一下crossfilling.tex有没有遵守"

Quality check revealed multiple violations of the two-phase pedagogical framework established in RET-0002.

---

## Core Design Principles

### 1. The Two-Phase Structure (MANDATORY)

**Decision:** Divide the slides into three distinct parts with an explicit transition:

**Part 1: Concretization Phase (§1-2, Frames 1-25)**
- Use coffee shop emoji as **primary notation**
- Concrete scenarios: discovering hidden intermediate products
- Emoji tables with 🫘🍃🍋🐄 → 🍵☕ → 🍱🍜
- NO abstract symbols ($R_k$, $\mathbf{u}$, $A = \sum R_k$) in this phase

**Part 2: Explicit Transition (§2, Frame 26)**
- Dedicated "Change of Perspective" frame
- Summarize what was learned (what, how, why)
- Signal abstraction shift: "From this point forward, we forget about coffee shops"
- Tell students what notation will change

**Part 3: Formalization Phase (§3-7, Frames 27-57)**
- Pure mathematical notation
- Definitions, algorithms, theorems, proofs
- NO emoji (concepts already grounded)
- Abstract matrices $A$, $B$, $C$, rank-one pieces $R_k$

**Rationale:**
- **Passive attention principle**: Students in classroom cannot process abstract symbol transformations
- **Cognitive load management**: Emoji provides visual anchor before abstraction
- **"学生是人类，他们只认图片"** (RET-0002 core lesson)

---

### 2. Definition → Immediate Visual Example (CRITICAL)

**Decision:** After EVERY definition or new concept, the IMMEDIATE next frame must be a concrete visual example.

**Pattern enforced:**
```
Frame N:   Definition (formal statement)
Frame N+1: IMMEDIATE emoji example ← NO text explanation between
Frame N+2: Calculation with emoji arithmetic
Frame N+3: (Optional) Text explanation
```

**Examples in crossfilling-v2.tex:**

| Definition Location | Immediate Example | Line Numbers |
|---------------------|-------------------|--------------|
| "What is a Simple Pattern?" (Frame 5) | Coffee shop table showing same ratio (Frame 6) | 97-114 |
| Implicit rank-one pattern (Frame 8) | Discovering hidden 🍵 tea product (Frame 9) | 133-148 |
| Formal rank-one definition (Frame 27, §3) | Numerical 3×2 matrix example (Frame 27) | 488-503 |

**Rationale:**
- Student's passive brain needs visual anchor immediately
- Text explanation AFTER example, not before
- Prevents "definition → abstract proof → lost students" pattern

---

### 3. The 5-Frame Sequence for Concepts

**Decision:** Introduce each new operation/concept using exactly 5 frames:

1. **Setup**: Original emoji ingredient table
2. **Change**: "What we're doing" with emoji transformation
3. **Calculation**: Step-by-step emoji arithmetic with intermediate steps
4. **Result**: Updated emoji table + matrix notation side-by-side
5. **Insight**: One-line key takeaway

**Implementation in crossfilling-v2.tex:**

**Cross-filling first pattern (Frames 10-16):**
- Frame 10: Setup - Full direct table $C$
- Frame 11: Change - Choose pivot (🍃 row, 🍱 column)
- Frame 12: Calculation Step 1 - Extract cross
- Frame 13: Calculation Step 2 - Build pattern table
- Frame 14: Result - The first pattern $R_1$
- Frame 15: Insight - What is this pattern? (hidden 🍵 tea)
- Frame 16: Visual cross-filling diagram (TikZ)

**Rationale:**
- One idea per frame (clarity trumps brevity)
- Passive attention needs explicit step markers
- Emoji arithmetic makes calculations visual and traceable

---

### 4. Visual Notation System

**Decision:** Use visual bars to represent matrix structure consistently.

**Implementation:**
```latex
% Column view — vertical bars
$$C = \begin{pmatrix}
| & | & & | \\
a_1 & a_2 & \cdots & a_n \\
| & | & & |
\end{pmatrix}$$

% Row view — horizontal bars
$$C = \begin{pmatrix}
- & b_1^T & - \\
- & b_2^T & - \\
\vdots & \vdots & \vdots
\end{pmatrix}$$
```

**Color coding for cross-filling:**
- `\pvt{red}`: Pivot (center of cross)
- `\crs{blue}`: Cross arms (row and column through pivot)
- `\rem{gray}`: Remainder zeros after subtraction

**Rationale:**
- Students can **see** the difference between rows and columns
- Visual bars eliminate confusion with transpose notation
- Color coding tracks algorithmic progress (from DR-0002)

---

### 5. Frame Size Management

**Decision:** Strict constraints to prevent page overflow.

**Rules applied:**
- Maximum 4-row matrix with surrounding text
- If 4+ rows: split into multiple frames or remove text
- Replace `\begin{alertblock}{Key}...\end{alertblock}` with "Key: [one line]"
- Use `\vspace{0.3cm}` instead of `\vfill` when content is dense
- Keep only emoji table when both emoji and numerical are present

**Quality gate:**
- Compile after every 5-10 frames
- Check for `Overfull \vbox` warnings immediately
- Final result: 5 overfull warnings (all < 14pt, acceptable)

**Rationale:**
- From RET-0002: "页面都超了，就是你每次用column matrix 超过4行的时候都要注意"
- Better to split content than overflow and lose readability

---

### 6. Knowledge Boundary Management

**Decision:** Explicitly mark what belongs to future lectures.

**Implementation:**

**Frame 41 (Rank definition):**
```latex
\textbf{Important}: Different pivot choices give different decompositions,
but always the same count $r$. (Proved in Lecture 4.)
```

**Frame 54 (LU decomposition preview):**
```latex
\begin{alertblock}{Preview (Future Lecture)}
LU decomposition is a special case of cross-filling with diagonal pivot strategy.
Full theory, including PLU decomposition, will be covered in Week 3.
\end{alertblock}
```

**Rationale:**
- Mathematical honesty: don't claim what's unproven (from RET-0002 Phase 3 lesson)
- Students need to know what's established vs. what's coming
- Prevents confusion about scope of current lecture

---

## Structural Decisions

### Section Organization

**§0 Introduction (Frames 1-3)**
- Learning objectives
- Review: sum-of-rank-one view from Lecture 1
- Connection to previous material

**§1 Discovering Simple Patterns - Concretization (Frames 4-25)**
- Motivating problem: hidden intermediate products
- What is a simple pattern? (coffee shop examples)
- Step-by-step cross-filling with emoji (5-frame sequences)
- Second and third patterns
- Full decomposition with emoji
- Insight: discovered hidden production chain

**§2 Change of Perspective (Frame 26)**
- Explicit transition frame
- Summary of concrete phase
- Signal to abstract notation

**§3 Rank-One Matrices - Formalization (Frames 27-31)**
- Formal definition
- Recognizing rank-one structure
- Cross-product property
- Not every matrix is rank-one

**§4 Cross-Filling Algorithm (Frames 32-42)**
- Algorithm statement (Proposition)
- Example: 3×3 matrix (full iteration sequence)
- Definition of rank

**§5 Sum ↔ Product Equivalence (Frames 43-48)**
- From sum to product form
- Collecting pieces into $U$ and $V$
- Verification
- The inner dimension

**§6 Algebraic Expression (Frames 49-52)**
- Matrix formula for cross-filling
- Example verification
- Application to projection matrices

**§7 Preview: LU Decomposition (Frames 53-54)**
- Diagonal pivots → LU
- When diagonal LU fails (preview only)

**§8 Summary (Frames 55-57)**
- Review of 6 main concepts
- Looking ahead to Lecture 4
- The big picture connection

**Rationale:**
- Mirrors the pedagogical arc: concrete → abstract → applications → preview
- Each section builds on previous (no forward references before concepts established)
- Summary reinforces learning and connects to course narrative

---

## Emoji Mapping Decisions

**Decision:** Use the established coffee shop metaphor from Lectures 1-2.

**Mapping:**
```
Raw materials:
  🫘 (bean)  - x₃
  🍃 (leaf)  - x₁
  🍋 (lemon) - x₂
  🐄 (cow)   - x₄

Semi-finished (hidden intermediate discovered by cross-filling):
  🍵 (tea)    - first rank-one pattern
  ☕ (coffee) - second rank-one pattern

Final products:
  🍱 (bento/Set 1) - y₁
  🍜 (ramen/Set 2) - y₂
```

**Rationale:**
- Continuity with Lectures 1-2 (students already know these emojis)
- Physical coherence: tea = leaves + lemon, coffee = beans
- Cross-filling **discovers** the hidden intermediate products (🍵, ☕)
- This demonstrates the power of the method: finding structure in direct tables

---

## Comparison: v1 vs. v2

| Aspect | Original crossfilling.tex (v1) | crossfilling-v2.tex |
|--------|-------------------------------|---------------------|
| **Concretization phase** | ❌ None (pure math from start) | ✅ §1-2 (25 frames with emoji) |
| **"Change of Perspective"** | ❌ Missing | ✅ Frame 26 (explicit transition) |
| **Definition → Example order** | ❌ Definition → text → example | ✅ Definition → immediate emoji example |
| **5-frame sequences** | ❌ Compressed explanations | ✅ Full 5-frame sequences for concepts |
| **Visual notation** | ⚠️ Partial (| and - used) | ✅ Consistent visual bars + color |
| **Abstract symbols timing** | ❌ Immediate ($\mathbf{u}, \mathbf{v}^T$) | ✅ Only after transition (Frame 27+) |
| **Knowledge boundary** | ⚠️ Some preview notes | ✅ Explicit "Preview (Future Lecture)" boxes |
| **Frame size management** | ❌ Not systematically checked | ✅ Strict 4-row limit, tested |
| **Coffee shop examples** | ⚠️ Motivating question only | ✅ Full cross-filling worked with emoji |
| **Standard LaTeX** | ✅ Yes | ✅ Yes |
| **Pages** | 57 | 57 |
| **Lines** | ~900 | 1,036 |

---

## Implementation Notes

### TikZ Diagrams

**Decision:** Use TikZ for the "Why Cross-Filling?" visual flow diagram (Frame 16).

**Implementation:**
```latex
\begin{tikzpicture}[scale=0.6, every node/.style={scale=0.85}]
% Original → Extract cross → Fill → Subtract → Remainder
\end{tikzpicture}
```

Shows 5 stages with emoji tables, arrows, and labels.

**Rationale:**
- Visual flow diagram reinforces the algorithm steps
- Side-by-side comparison shows transformation clearly
- Color coding (red pivot, blue cross, gray zeros) tracks progress

### Projection Application

**Decision:** Include projection decomposition application (Frames 50-52).

**Rationale:**
- Forward connection to spectral decomposition (Lecture 8+)
- Shows cross-filling is not just computational, but theoretical tool
- Prepares students for "projection as compatible family" concept

### Standard LaTeX Adherence

**Quality gates enforced:**
- ✅ No custom DSL syntax
- ✅ Standard `\begin{frame}...\end{frame}`
- ✅ Standard `\begin{pmatrix}...\end{pmatrix}`
- ✅ Minimal packages: amsmath, amssymb, amsthm, tikz, graphicx, array
- ✅ Emoji via `\includegraphics` + `\newcommand` wrappers
- ✅ Compiles standalone with `pdflatex crossfilling-v2.tex`

---

## Validation

### Self-Check Results (from math-slides-authoring skill)

- [x] **Definition → immediate example**: Every definition followed by visual example
- [x] **Two-phase structure**: Concretization (§1-2), Transition (§2), Formalization (§3-7)
- [x] **No premature abstraction**: Abstract symbols only after Frame 26
- [x] **Frame size**: No 4+ row matrix with verbose text
- [x] **Both cases**: N/A (not row/column operations lecture)
- [x] **Notation-arithmetic consistency**: Emoji arithmetic matches numbers
- [x] **Invariant principle**: N/A (no equation solving in this lecture)
- [x] **Knowledge boundary**: Explicit preview markers for future content
- [x] **Visual notation**: | for columns, - for rows throughout
- [x] **No augmented matrices**: None present
- [x] **Standard LaTeX**: Zero custom DSL, compiles standalone
- [x] **Minimal packages**: Only required packages

### Compilation Results

- **Status**: ✅ Success
- **Pages**: 57
- **Overfull warnings**: 5 (all < 14pt, acceptable)
- **File size**: 505KB PDF

---

## Lessons for Future Slides

### What Worked Well

1. **Pre-work checklist** (from math-slides-authoring skill)
   - Reading reference materials first prevented wrong patterns
   - Answering diagnostic questions ensured understanding
   - Emoji mapping table before writing prevented inconsistencies

2. **5-frame sequences**
   - Students see each step clearly
   - Emoji arithmetic is traceable and debuggable
   - Much clearer than compressed explanations

3. **Explicit transition frame**
   - Prevents student confusion about notation shifts
   - Reinforces what was learned in concrete phase
   - Justifies abstraction (not arbitrary)

4. **Frequent compilation checks**
   - Caught overflow issues early
   - Fixed problems before they compound
   - 5-10 frame intervals worked well

### Patterns to Replicate

For future slide rewrites:

1. **Always start with concretization phase** (20-25 frames minimum)
   - Use emoji/visual examples as primary notation
   - No abstract symbols until after transition

2. **Always include "Change of Perspective" frame**
   - Template available in this DR
   - Summarize → Signal shift → Explain why

3. **Always use 5-frame sequences for new concepts**
   - Setup → Change → Calculation → Result → Insight
   - One idea per frame

4. **Always check frame size after 4-row matrices**
   - Compile immediately
   - Split or reduce text if overflow

5. **Always mark knowledge boundaries**
   - "Preview (will prove in Lecture N)"
   - Never claim unproven results as established

---

## Related Documents

- **ADR-0001**: DSL-to-standard-LaTeX migration (provides LaTeX constraints)
- **DR-0002**: rowoperation.tex quality standards (established visual notation, emoji usage)
- **RET-0002**: rowoperation.tex execution lessons (provided "学生是人类，他们只认图片" core insight)
- **AA-0001**: Architecture analysis of 43-module slide system (shows where cross-filling fits)
- **math-slides-authoring skill**: Complete pedagogical framework (this DR implements it)

---

## Conclusion

crossfilling-v2.tex successfully implements the two-phase pedagogical structure required by math-slides-authoring skill. It addresses all violations found in the original version while maintaining mathematical rigor and standard LaTeX compatibility.

The key innovation: **emoji concretization (§1-2) → explicit transition (§2) → pure formalization (§3-7)** provides a replicable pattern for future slide modules.

This design pattern should be applied to all future teaching slides in this repository.

---

**Last Updated:** 2026-03-03
**Status:** Ready for user review
**Next Action:** User review of crossfilling-v2.tex and crossfilling-v2.pdf
