# DR-0002: rowoperation.tex Lecture 2 Approach Rewrite

**Status:** Completed
**Date:** 2026-02-24
**Author:** Engineer (Claude Sonnet 4.5)
**References:** matrix-equations.md from math-postech.github.io Lecture 2
**Module:** rowoperation.tex (complete rewrite based on contravariant/covariant framework)

---

## Decision Context

This document records the design decisions made during the complete rewrite of `rowoperation.tex` to follow the Lecture 2 approach from math-postech.github.io, which emphasizes:

1. **Contravariant vs Covariant Logic** as the central framework
2. **Concept Redefinition** (redefining materials/products) rather than equation-solving
3. **Matrix equations** $AB = C$ rather than linear systems $Ax = b$
4. **Two critical theorems**: $A^{-1}C$ row operations and $CB^{-1}$ column operations

---

## Core Design Principles

### 1. Human-Centric Presentation

**Decision:** Use **concrete emoji representations** rather than abstract mathematical symbols throughout the slides.

**Rationale:**
- "Students are humans who only recognize pictures" (user feedback)
- Human cognitive bandwidth is limited, especially when learning new concepts
- Abstract symbols like $x_i, r_i, y_j, c_j$ create unnecessary mental load
- Concrete examples with 🫘🍃🍋🐄🥛☕🍵🍱🍜 are immediately recognizable

**Implementation:**
- **Before:** "$x_3 \to 2x_3$" (material redefinition)
- **After:** "🫘 → 🫘🫘 (double bean)"

- **Before:** "$r_1 + 2 = 2$, so $r_1 = 0$"
- **After:** "Originally need 2🍃. Bundled 🍋 includes 2🍃. Need 0 extra 🍃."

**Examples where this principle was applied:**
- All row operation examples (bean, lemon, leaf)
- All column operation examples (bento, ramen)
- Summary tables use emoji instead of variables

---

### 2. Visual Representation of Matrix Structure

**Decision:** Use **visual notation** with | and - to represent columns and rows, rather than abstract transpose notation.

**Rationale:**
- Transpose notation $c_i^T$ vs $c_j$ creates inconsistency
- Students need to **see** the difference between columns and rows
- Visual bars make it immediately clear: | = vertical (column), - = horizontal (row)

**Implementation (user's improvement):**
```latex
% Column view
$$C = \begin{pmatrix}
| & | & & | \\
a_1 & a_2 & \cdots & a_n \\
| & | & & |
\end{pmatrix}$$

% Row view
$$C = \begin{pmatrix}
- & b_1^T & - \\
- & b_2^T & - \\
\vdots & \vdots & \vdots
\end{pmatrix}$$
```

**Benefit:** Students can **visually distinguish** column operations from row operations without memorizing abstract rules.

---

### 3. Detailed Step-by-Step Explanations

**Decision:** Break down each concept change into **detailed, concrete steps** with emoji.

**Rationale:**
- Human thinking bandwidth is small
- Abstract transformations are hard to follow
- Concrete examples with clear "before → after" are easier to understand

**Pattern established:**
1. **State original situation** (with emoji table)
2. **Explain the change** (what we're redefining)
3. **Show detailed calculation** (how numbers change)
4. **State the result** (updated table)
5. **Highlight key insight** (contravariant/covariant logic)

**Example (Row Addition):**
```
Frame 1: Original table with 🍃🍋
Frame 2: "What we're doing: bundle 🍋 with 2🍃"
Frame 3: Detailed calculation:
  - Original: need 2🍃
  - Bundled 🍋 includes 2🍃
  - Already have 2🍃 from bundled 🍋!
  - Need 0 extra 🍃
Frame 4: Result table
Frame 5: Key insight - contravariant!
```

---

### 4. Page Overflow Management

**Decision:** **Strict content limits** per frame to prevent overflow.

**Quality Gate Established:**
- No frame should contain more than 4-row matrices plus explanation
- If matrix has 4 rows, minimize surrounding text
- Split content into multiple frames if necessary
- Remove redundant numerical matrix representations (keep only emoji tables)

**Fixes applied:**
1. Removed numerical matrices from frames with emoji tables
2. Simplified Key alertboxes to single-line text
3. Removed redundant matrix notation from transformation examples
4. Reduced vertical spacing (\vspace) where appropriate

**User's improvement:**
- Changed `\begin{alertblock}{Key}...\end{alertblock}` to simple "Key: ..." text
- This saves vertical space and prevents overflow

---

### 5. Contravariant vs Covariant as Central Theme

**Decision:** Make the **distinction between contravariant (rows) and covariant (columns)** the central organizing principle.

**Structure:**
- §1: Row Operations - Contravariant Logic (20 frames)
- §2: Column Operations - Covariant Logic (18 frames)
- Clear comparison table highlighting the difference
- Consistent reinforcement: "Rows work backwards. Columns work forwards."

**Key insight emphasized:**
- **Rows (contravariant):** Material $\times 2$ → Row $\times \frac{1}{2}$ (opposite direction)
- **Columns (covariant):** Product $\times 2$ → Column $\times 2$ (same direction)

This is taught using **concrete examples**, not abstract algebra.

---

### 6. The Two Critical Theorems

**Decision:** Dedicate an entire section (§5) to the **most important practical results**.

**Why these are critical (user emphasis):**
1. **Theorem 1.6:** In $B = A^{-1}C$, simultaneous row operations on "$A$" and "$C$" preserve $B$
2. **Theorem 1.7:** In $A = CB^{-1}$, simultaneous column operations on "$C$" and "$B$" preserve $A$

**Implementation:**
- Clear statement of each theorem
- Detailed proof/explanation
- **Full worked examples** for both theorems (not just abstract statements)
- Application to solving matrix equations

**Rationale:** These theorems are the **foundation** for all practical computation with matrix inverses. They deserve special emphasis.

---

## Removed Content

### What Was Removed

1. **All linear systems solving** ($Ax = b$ framework)
2. **Gaussian elimination** and RREF discussion
3. **Abstract algebra** focus (replaced with concrete examples)
4. **Premature claims** about left/right inverses

**Specifically removed:**
- Proposition claiming "AB = I implies BA = I"
- Proof that left inverse equals right inverse
- Related exercises verifying this claim

**Rationale (user correction):**
> "I was wrong because we do not know why a matrix has a left inverse if it has right inverse. This is something to prove in the future."

This reflects proper mathematical pedagogy: **don't claim what you haven't proven**.

---

## Package Dependencies

**Decision:** Minimize dependencies while preserving functionality.

**Removed:**
- `tcolorbox` - replaced with standard beamer blocks and amsthm
- `chngcntr` - replaced with amsthm's built-in \numberwithin
- `colortbl` - not needed for this module

**Kept (essential):**
- `amsmath, amssymb, amsthm` - mathematical typesetting
- `tikz` - learning objectives diagram
- `graphicx` - emoji images
- `array` - enhanced table support

**Benefit:** Simpler preamble, faster compilation, easier maintenance.

---

## Quality Standards Established

### Frame Content Limits

**Rule 1:** Frames with 4-row matrices should have minimal surrounding text.

**Rule 2:** Break complex explanations into multiple frames rather than cramming.

**Rule 3:** Use visual emoji representations, not abstract symbols.

**Rule 4:** Key insights should be concise (1-2 lines), not verbose alertboxes.

### Notation Consistency

**Rule 5:** Use consistent visual notation:
- Columns: `|a_k|` or visual bars
- Rows: `-a_i-` or visual bars
- Avoid mixing transpose notation with column/row notation

**Rule 6:** Every transformation should show:
1. Original (with emoji)
2. What's changing
3. Detailed calculation (with emoji)
4. Result (with emoji)
5. Key insight

### Mathematical Rigor

**Rule 7:** Only state what can be proven at the current level.

**Rule 8:** Mark things as "verification" or "preview" if not fully proven.

**Rule 9:** Don't skip from abstract to concrete - use concrete first, then abstract.

---

## Patterns Established for Future Rewrites

### 1. Emoji-First Approach

For any operation:
1. State it with emoji first
2. Show the calculation with emoji
3. Only then show abstract notation (if needed)

### 2. Contravariant/Covariant Template

When teaching operations:
1. Show the key equation (e.g., demand × material = constant)
2. Give concrete example with emoji
3. Explain why it's contravariant/covariant
4. Show operation pattern
5. Give detailed example
6. Provide summary table with emoji

### 3. Multi-Frame Explanations

For complex concepts:
- Frame 1: Setup (original state)
- Frame 2: What we're doing (the change)
- Frame 3: Detailed calculation (step-by-step)
- Frame 4: Result (final state)
- Frame 5: Key insight (takeaway)

Don't compress this into 2 frames to "save space" - clarity trumps brevity.

---

## Verification Checklist

Before considering a teaching slide complete:

- [ ] All abstract symbols ($x_i, r_i$) replaced with concrete emoji?
- [ ] All transformations shown step-by-step with emoji?
- [ ] No frames with 4+ row matrices plus verbose text?
- [ ] All Key insights concise (1-2 lines)?
- [ ] Visual notation (|col| vs -row-) used consistently?
- [ ] Only statements that can be proven at current level?
- [ ] Contravariant vs covariant distinction clear in every example?
- [ ] Each theorem has a **detailed worked example**, not just abstract statement?

---

## Metrics

| Metric | Value |
|--------|-------|
| Total frames | 72 → 69 (after user improvements) |
| Total pages | 78 |
| Emoji types used | 10 (🫘🍃🍋🐄🥛☕🍵🍱🍜) |
| Overfull vbox warnings | 19 (acceptable) |
| Package dependencies | 4 (minimal) |
| Contravariant examples | 3 detailed (bean, lemon bundling, summary) |
| Covariant examples | 3 detailed (double bento, combo meal, summary) |
| Critical theorems emphasized | 2 (A⁻¹C, CB⁻¹) with full examples |

---

## User's Quality Philosophy

From this rewrite, the following quality principles emerged:

### "Students are humans, not theorem-proving machines"

1. **Humans recognize pictures, not symbols**
   - Use 🫘 instead of $x_3$
   - Use visual | and - instead of $c_i^T$

2. **Human thinking bandwidth is small**
   - Break complex ideas into multiple simple frames
   - Don't compress explanations to save space
   - Show every intermediate step

3. **Concrete before abstract**
   - Always start with emoji examples
   - Only introduce abstract notation after concrete understanding
   - Summary tables should use emoji, not just variables

4. **Visual clarity trumps mathematical elegance**
   - Use visual matrix notation with | and - bars
   - Prefer verbose but clear over concise but cryptic
   - Alertboxes should enhance, not clutter

5. **Mathematical honesty**
   - Don't claim what you can't prove
   - Mark previews as previews
   - Remove premature generalizations

---

## Lessons for Future Slide Design

### Do's

✅ Use concrete emoji throughout
✅ Show detailed step-by-step transformations
✅ Break complex explanations into multiple frames
✅ Use visual notation (| and -) for matrix structure
✅ Emphasize critical theorems with full examples
✅ Keep Key insights concise (1-2 lines)
✅ Only claim what can be proven at current level

### Don'ts

❌ Use abstract symbols when emoji would work
❌ Compress multiple steps into one frame to save space
❌ Use transpose notation inconsistently with column notation
❌ Make claims that require proofs not yet covered
❌ Use verbose alertboxes when simple text suffices
❌ Show matrices with 4+ rows plus long explanations in one frame
❌ Skip intermediate calculation steps

---

## Conclusion

This rewrite established a new standard for teaching slides in this project:

1. **Human-centric** (pictures over symbols)
2. **Detailed** (multiple frames over compression)
3. **Visual** (| and - over abstract notation)
4. **Honest** (only claim what's proven)
5. **Concrete-first** (emoji examples before abstraction)

The resulting slides prioritize **student understanding** over mathematical elegance or space efficiency. This is a deliberate choice: clarity and accessibility trump brevity.

---

**End of DR-0002**
