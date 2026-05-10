# Slide Plan: Complex Numbers (Lecture 17)

**Lecture:** 17
**Placement:** After Lecture 16 (Eigenspaces & Diagonalization), before Exponential lecture
**Prerequisites students already have:** eigenvalues, $\det(tI-A)$, Cayley-Hamilton, diagonalization $A = PDP^{-1}$, spectral decomposition, value tables
**Core question from L14–L16:** "We assumed $\det(tI-A)$ factors into distinct linear factors. But over $\mathbb{R}$, not every polynomial factors into linear factors at all!"

---

## The Two Motivations

### Motivation 1 (Algebraic): Partially removing the restriction on Cayley-Hamilton

Throughout L14–L16, we relied on a standing assumption: the minimal polynomial factors into **distinct linear factors**. This assumption has **two** separate issues:

1. **Cannot factor into linear factors at all** — over $\mathbb{R}$, polynomials like $t^2 + 1$ don't factor into linear factors. Many real matrices (rotation matrices!) fall outside our machinery entirely.
2. **Repeated linear factors** — even after factoring, the minimal polynomial may have repeated factors like $(t-2)^2$. This prevents diagonalization (L16 §6).

**Complex numbers fix issue (1) only.** Over $\mathbb{C}$, the **Fundamental Theorem of Algebra** guarantees every degree-$n$ polynomial has exactly $n$ roots. So every polynomial factors into linear factors — possibly with multiplicities.

**Issue (2) remains open.** Repeated factors in the minimal polynomial require new tools (Jordan Canonical Form), which will be self-study material. Complex numbers do NOT solve this.

**What complex numbers give us:** Every polynomial factors into linear factors over $\mathbb{C}$. This means our Cayley-Hamilton → spectral decomposition → diagonalization pipeline works for all matrices **whose minimal polynomial has distinct roots** — we no longer lose matrices just because the characteristic polynomial is irreducible over $\mathbb{R}$.

### Motivation 2 (Physics/History): Complex numbers are unavoidable

Even when the **problem** is entirely real, the **solution** may force you through complex numbers.

The most striking example: **the cubic formula**. Cardano's formula for $ax^3 + bx^2 + cx + d = 0$ inevitably contains $\sqrt{\text{negative}}$, even when all three roots are real. For centuries mathematicians dismissed $\sqrt{-1}$ as meaningless — but Bombelli showed you **cannot avoid it**. You must compute with it to extract the real answers.

This pattern repeats throughout physics: waves, quantum mechanics, electrical engineering — complex numbers appear everywhere, even in problems stated purely in real terms.

---

## Proposed Structure for Lecture 17

### §1 — The Problem: Our Machinery Breaks Over $\mathbb{R}$

**Tension:** "We built powerful tools in L14–L16. But they have a gap."

| Frame | Content |
|-------|---------|
| 1 | **Recall the pipeline:** $\det(tI-A)$ → factor into linear factors → eigenvalues → spectral projections → value tables → diagonalization. This works beautifully when the minimal polynomial factors into distinct linear factors. |
| 2 | **Two restrictions remain.** (a) The polynomial must factor into **linear** factors. (b) Those factors must be **distinct** (no repeated roots in the minimal polynomial). Today we address restriction (a). Restriction (b) leads to Jordan Canonical Form — self-study material. |
| 3 | **The 90° rotation matrix:** $R = \begin{psmallmatrix}0 & -1 \\ 1 & 0\end{psmallmatrix}$. Compute $\det(tI - R) = t^2 + 1$. This polynomial has **no real roots**. It doesn't factor into linear factors over $\mathbb{R}$. |
| 4 | **Our entire pipeline stops.** No eigenvalues → no spectral projections → no value tables → no diagonalization. And yet $R$ is a perfectly concrete, geometrically clear matrix (it rotates by 90°). Something is wrong with the number system, not the matrix. |
| 5 | **The question:** Can we extend $\mathbb{R}$ to a larger number system where $t^2 + 1 = 0$ HAS solutions? And if so, does EVERY polynomial factor into linear factors there? |
| 6 | **Spoiler (boxed):** Yes. The **Fundamental Theorem of Algebra** says: over $\mathbb{C}$, every degree-$n$ polynomial has exactly $n$ roots (with multiplicity). Every polynomial factors into linear factors. Restriction (a) is completely removed. |

### §2 — The Cubic Formula: Complex Numbers Are Unavoidable (from `8.001.tex`)

**Tension:** "You might think $\sqrt{-1}$ is a trick we made up. History says otherwise — it was forced on mathematicians."

| Frame | Content |
|-------|---------|
| 1 | **Quadratic formula:** $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$. When discriminant $< 0$, we used to say "no real solutions." Easy to dismiss $\sqrt{-1}$. |
| 2 | **The cubic equation:** $ax^3 + bx^2 + cx + d = 0$. Unsolved until 1530 (Scipione del Ferro → Antonio Fior → Cardano). Show the monstrous formula. |
| 3 | **The paradox:** Use the cubic formula on $x^3 = x$ (which clearly has solutions $x = 0, \pm 1$). The formula gives $x = \frac{1}{\sqrt{3}}(\sqrt[3]{\sqrt{-1}} + \sqrt[3]{-\sqrt{-1}})$. Looks insane — but it equals $0, 1, -1$. |
| 4 | **Bombelli's insight:** The formula WORKS if you just compute with $\sqrt{-1}$ formally. $\sqrt{-1}$ appears in the middle of the calculation but cancels out, giving real answers. You **cannot avoid** passing through complex numbers. |
| 5 | **The lesson (boxed):** Complex numbers aren't optional. Even for purely real problems, the solution path may require them. You cannot assume $\sqrt{-1}$ doesn't exist — it is meaningful and must be computed. |

### §3 — Definition & The Complex Plane (from `MANR.tex`)

| Frame | Content |
|-------|---------|
| 1 | **Definition:** Write $i = \sqrt{-1}$. A complex number: $z = a + bi$, where $a,b \in \mathbb{R}$. $a$ = real part, $b$ = imaginary part. The field $\mathbb{C}$. |
| 2 | **Complex plane:** $a + bi \leftrightarrow (a, b) \in \mathbb{R}^2$. TikZ: plot $1+2i$ with dotted projections. |
| 3 | **Addition:** $(a+bi) + (c+di) = (a+c) + (b+d)i$. Same as vector addition — parallelogram law. TikZ: $(1+2i) + (2+i) = 3+3i$. |

### §4 — Multiplication = Rotation + Scaling (from `MANR.tex`, **CORE**)

**Tension:** "Addition in $\mathbb{C}$ is just vector addition. But multiplication — that's where the magic is."

| Frame | Content |
|-------|---------|
| 1 | **Multiply by $i$:** $i(a+bi) = -b + ai$. TikZ: $i(1+2i) = -2+i$. This is **90° counterclockwise rotation**! |
| 2 | **The square:** $z$ and $zi$ are two sides of a square from the origin. TikZ: $z, zi, z(1+i)$ forming a square. |
| 3 | **General multiplication:** Multiplying by $z$ maps the blue unit square $\{0, 1, i, 1+i\}$ to the red square $\{0, z, zi, z(1+i)\}$. TikZ: blue square → red square. |
| 4 | **Step 1 — Rotate:** Rotate the blue square by $\arg(z) = \arctan(b/a)$. TikZ: blue square tilted. |
| 5 | **Step 2 — Scale:** Scale by $|z| = \sqrt{a^2 + b^2}$. TikZ: tilted square stretched to match red square. |
| 6 | **Summary (boxed):** Multiplying by $z$ = rotate by $\arg(z)$ + scale by $|z|$. This is why multiplication by $i$ is 90° rotation: $|i| = 1$ (no scaling), $\arg(i) = 90°$. |

### §5 — Polar Form, De Moivre & Roots of Unity (from `MANR.tex` + `8.0004.tex`)

| Frame | Content |
|-------|---------|
| 1 | **Polar form:** $z = |z|(\cos\theta + i\sin\theta)$, where $\theta = \arg(z)$. TikZ: triangle with $|z|$, $\theta$. |
| 2 | **Multiplication in polar form:** $z_1 z_2 = |z_1||z_2|(\cos(\theta_1+\theta_2) + i\sin(\theta_1+\theta_2))$. Absolute values multiply, arguments add. |
| 3 | **De Moivre:** $z^n = |z|^n(\cos n\theta + i\sin n\theta)$. |
| 4 | **Roots of unity:** $\zeta_n = \cos\frac{2\pi}{n} + i\sin\frac{2\pi}{n}$ satisfies $\zeta_n^n = 1$. The $n$ roots of $z^n = 1$ are equally spaced on the unit circle. |
| 5 | **TikZ: 3rd roots of unity** on unit circle. $1 + \omega + \omega^2 = 0$ visible from the diagram. |
| 6 | **TikZ: 4th roots of unity.** $1, i, -1, -i$. Note: $1 + i + i^2 + i^3 = 0$. |

### §6 — Conjugate, Division & The Philosophy of Symmetry (from `MANR.tex` + `MAN2.tex`, **MUST**)

**Tension:** "Conjugation is not just a formula — it is the fundamental symmetry of the complex numbers."

#### 6a: Conjugate & Division (3 frames)

| Frame | Content |
|-------|---------|
| 1 | **Conjugate:** $\bar{z} = a - bi$. Reflection across real axis. TikZ: $1+2i$ and $1-2i$ symmetric about the real line. |
| 2 | **Key identity:** $z\bar{z} = a^2 + b^2 = |z|^2$ (always real, always $\geq 0$). Real/imaginary extraction: $a = (z+\bar{z})/2$, $b = (z-\bar{z})/(2i)$. |
| 3 | **Division:** $\frac{3+4i}{2+i} = \frac{(3+4i)(2-i)}{(2+i)(2-i)} = \frac{10+5i}{5} = 2+i$. Multiply top and bottom by conjugate of denominator. |

#### 6b: The Philosophy of Symmetry (from `MAN2.tex`, 8 frames)

| Frame | Content |
|-------|---------|
| 4 | **What is symmetry?** In mathematics, *symmetry* means *invariant under a certain action*. The action on $\mathbb{C}$ is conjugation: $z \mapsto \bar{z}$. The **symmetric** (invariant) numbers are exactly the **real numbers**: $\bar{z} = z \iff z \in \mathbb{R}$. |
| 5 | **The principle:** If a *symmetric system* produces an *asymmetric result*, then performing the symmetry action on that result must produce another valid result. Summing all such results recovers the symmetry. This is why $z + \bar{z}$ and $z\bar{z}$ are always real. |
| 6 | **Concrete example — four villages.** Four villages at the vertices of a square (symmetric under 90° rotation). TikZ: square with vertices A, B, C, D. |
| 7 | **The shortest road network** connecting all four villages. TikZ: the Steiner tree — two interior junction points, roads forming an H-shape. This solution is **asymmetric** — it is NOT invariant under 90° rotation. |
| 8 | **Consequence:** Since the problem is symmetric but the solution is not, rotating the solution by 90° gives **another** shortest road. TikZ: the rotated Steiner tree (vertical H-shape). |
| 9 | **Symmetry recovered:** Overlay both solutions. TikZ: both Steiner trees superimposed — the combined figure IS symmetric under 90° rotation. The asymmetry of individual solutions is compensated by the existence of conjugate solutions. |
| 10 | **Application to polynomials (boxed):** A real polynomial is a *symmetric system* (invariant under conjugation). If it has a complex root $z$, then $\bar{z}$ must also be a root — the conjugate is the "rotated solution." **Complex roots of real polynomials always come in conjugate pairs.** |
| 11 | **Application to matrices:** If $A$ is a real matrix, then $\det(tI-A)$ is a real polynomial. So eigenvalues come in conjugate pairs: if $\lambda = a+bi$ is an eigenvalue, so is $\bar{\lambda} = a-bi$. And the eigenvectors also come in conjugate pairs: if $\mathbf{v}$ is an eigenvector for $\lambda$, then $\bar{\mathbf{v}}$ is an eigenvector for $\bar{\lambda}$. **The symmetry principle applies to the entire eigenstructure.** |

**Key insight frame:** "Symmetry is one of the deepest principles in mathematics. Conjugation is the symmetry of $\mathbb{C}$ over $\mathbb{R}$. Whenever a symmetric problem gives an asymmetric answer, the conjugate answer must also exist. This philosophy appears everywhere — in algebra, geometry, physics, and beyond."

### §7 — The Fundamental Theorem & Complex Eigenvalues (THE PAYOFF)

**Tension:** "Now we return to the problem from §1. Does $\mathbb{C}$ actually fix our pipeline?"

| Frame | Content |
|-------|---------|
| 1 | **Fundamental Theorem of Algebra (boxed):** Every degree-$n$ polynomial with complex coefficients has exactly $n$ roots in $\mathbb{C}$ (counted with multiplicity): $p(t) = (t - z_1)(t - z_2)\cdots(t - z_n)$. Every polynomial factors into linear factors. |
| 2 | **Consequence for matrices:** For ANY $n \times n$ matrix $A$, $\det(tI - A)$ is degree $n$, so it has $n$ complex roots. **Every matrix has eigenvalues over $\mathbb{C}$.** The pipeline never stalls at "can't factor." |
| 3 | **Back to the rotation matrix:** $R = \begin{psmallmatrix}0 & -1 \\ 1 & 0\end{psmallmatrix}$. $\det(tI-R) = t^2+1 = (t-i)(t+i)$. Eigenvalues: $\lambda_1 = i$, $\lambda_2 = -i$. Two distinct eigenvalues — the pipeline works! Note: they are a conjugate pair, as the symmetry principle predicts. |
| 4 | **Another example:** $A = \begin{psmallmatrix}1&2\\-2&1\end{psmallmatrix}$. $\det(tI-A) = t^2-2t+5 = (t-(1+2i))(t-(1-2i))$. Eigenvalues $1 \pm 2i$. Eigenvectors: $\begin{psmallmatrix}1\\i\end{psmallmatrix}$ and $\begin{psmallmatrix}1\\-i\end{psmallmatrix}$ — conjugate pair of eigenvectors for conjugate pair of eigenvalues. |
| 5 | **What we've achieved (boxed):** Over $\mathbb{C}$, every polynomial factors into linear factors. This removes restriction (a) from §1 — our pipeline works for all matrices whose minimal polynomial has distinct roots, regardless of whether the eigenvalues are real or complex. **Restriction (b)** (repeated factors in the minimal polynomial) remains, and leads to Jordan Canonical Form — a topic for self-study. |

### §8 — Preview

| Frame | Content |
|-------|---------|
| 1 | **What we've gained:** Every matrix with distinct eigenvalues (over $\mathbb{C}$) can be diagonalized. Spectral decomposition, value tables, $A^n$ — all work with complex eigenvalues. |
| 2 | **Next question:** "What does $e^{\lambda}$ mean when $\lambda$ is complex? If we can make sense of $e^{i\theta}$, we can compute $e^{At}$ for ANY diagonalizable matrix — solving systems of differential equations." → Next lecture: Exponential functions. |

---

## Frame Estimate

| Section | Frames (est.) | Role |
|---------|--------------|------|
| §1 The problem: pipeline breaks over $\mathbb{R}$ | 6 | Algebraic motivation — two restrictions, today we fix one |
| §2 Cubic formula: $\sqrt{-1}$ is unavoidable | 5 | Historical/physics motivation |
| §3 Definition & complex plane | 3 | Setup |
| §4 Multiplication = rotation + scaling | 6 | Core geometry |
| §5 Polar form, De Moivre, roots of unity | 6 | Tools |
| §6 Conjugate, division & symmetry philosophy | 11 | **Deep philosophical core** — Steiner tree, conjugate pairs |
| §7 Fundamental Theorem & complex eigenvalues | 5 | **THE PAYOFF** — pipeline restored |
| §8 Preview | 2 | Bridge to exponential |
| **Total** | **~44** | |

---

## Legacy Source Mapping

| New section | Legacy source |
|-------------|---------------|
| §1 | New (connects to L14–L16 narrative, clarifies partial fix) |
| §2 | `8.001.tex` (cubic formula, Bombelli) |
| §3 | `MANR.tex` lines 1–37 |
| §4 | `MANR.tex` lines 38–201 (the blue→red square TikZ) |
| §5 | `MANR.tex` lines 203–262 + `8.0004.tex` |
| §6a | `MANR.tex` lines 295–335 |
| §6b | `MAN2.tex` lines 325–400 (four villages, symmetry philosophy) |
| §7 | `MANR.tex` lines 401–427, 546–558 (FTA) + new |
| §8 | New |

---

## Design Decisions

1. **§2 depth:** The cubic formula story is rich but can be long. Current plan: 5 frames (show the formula, show the paradox, state the lesson). Expand to include del Ferro/Fior/Tartaglia drama, or keep it tight?

2. **§6b Steiner tree depth:** Currently 8 frames covering the four-villages example + application to polynomials + application to matrices. Should we add more examples of the symmetry principle (e.g., group theory preview, or examples from physics)?

3. **How much eigenvalue computation in §7?** Currently just states the eigenvalues of $R$ and $A$. Should we fully compute spectral projections for a complex-eigenvalue matrix (showing the pipeline works end-to-end), or save that for the exponential lecture?

4. **Jordan Canonical Form reference:** §1 and §7 mention JCF as "self-study material." Should we provide a specific reference (textbook chapter, or a supplementary handout)?

---

*Legacy files: `legacy-slides/Linear3/MANR.tex`, `MAN2.tex`, `8.001.tex`, `8.0004.tex`*

*Questions? Call me back:* {{SHELL_PREFIX}}l1
