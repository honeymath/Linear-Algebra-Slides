# Slide Plan: Normal Matrices — Revised

**Placement:** After Lecture 18, exponential functions and matrix exponentials.  
**Core correction:** Diagonalization is **not** the endpoint. The endpoint is **orthogonal spectral geometry**: eigenspaces are automatically Hermitian-orthogonal, and special normal matrices are classified by where their eigenvalues live in the complex plane.

---

## 0. Revised Thesis

A normal matrix is not merely “diagonalizable.” That is too weak and too traditional.

The right story is an **if and only if** statement, not a one-way implication:

$$
\boxed{
A\text{ is normal}
\quad\Longleftrightarrow\quad
\text{all spectral projections }P_i\text{ are Hermitian symmetric }(P_i^H=P_i)
}
$$

Equivalently:

$$
A\text{ normal}
\quad\Longleftrightarrow\quad
\text{eigenspaces are mutually Hermitian-orthogonal.}
$$

Then special normal matrices become geometry of eigenvalues:

- Hermitian symmetric $A^H=A$ $\Longleftrightarrow$ eigenvalues lie on the **real axis**.
- Skew-Hermitian symmetric $A^H=-A$ $\Longleftrightarrow$ eigenvalues lie on the **imaginary axis**.
- Unitary $A^HA=AA^H=I$ $\Longleftrightarrow$ eigenvalues lie on the **unit circle**.

This is the lecture’s real destination.

---

## 1. Key User Feedback Incorporated

1. **Define Hermitian orthogonal early.** After defining $v^Hw$, immediately define:
   $$
   v\perp_H w \quad\Longleftrightarrow\quad v^Hw=0.
   $$
   For subspaces:
   $$
   V\perp_H W \quad\Longleftrightarrow\quad v^Hw=0\text{ for all }v\in V,w\in W.
   $$

2. **Do not use the traditional eigenvector proof as the main method.** The method must follow previous lectures:
   - spectral projections are polynomials in $A$;
   - polynomials of normal matrices are normal;
   - normal projections are Hermitian projections;
   - therefore eigenspaces are automatically Hermitian-orthogonal.

3. **Normal-matrix discussion must continue after diagonalization.** Diagonalizability is only a checkpoint. The payoff is orthogonality of eigenspaces and classification of special normal matrices.

4. **Define special normal matrices near the beginning.** Hermitian, skew-Hermitian, and unitary are not late afterthoughts; they are motivating examples of normal matrices.

5. **Return to the complex-plane picture at the end.** Draw real axis, imaginary axis, unit circle. Each special class is a geometric eigenvalue restriction.

---

## 2. Legacy Ideas to Keep, with Correct Priority

From `normalOperators.tex`, keep these ideas but reorder the emphasis:

1. **Complex length failure:** $v=(1,i)^T$ gives $v^Tv=0$. This motivates $v^H$.
2. **Hermitian inner product:** $v^Hw=\overline v^T w$.
3. **Hermitian orthogonality:** $v^Hw=0$.
4. **Hermitian transpose:** $A^H=\overline{A^T}$.
5. **Normal matrix:** $AA^H=A^HA$.
6. **Projection theorem:** if $P^2=P$ and $PP^H=P^HP$, then $P=P^H$.
7. **Spectral projection payoff:** $P_i=f_i(A)$, so $P_i$ is normal; hence $P_i=P_i^H$; hence eigenspaces are orthogonal.
8. **Special normal matrices:** Hermitian, skew-Hermitian, unitary, classified by eigenvalue location.

The old “normal implies diagonalizable” theorem can appear, but it should not dominate the lecture.

---

## 3. Revised Section Plan

### §1 — Complex Length Forces Hermitian Inner Product

**Tension:** “Can a nonzero vector have length zero?”

| Frame | Content |
|---|---|
| 1 | Real callback: $\|v\|^2=v^Tv$ works over $\mathbb R$ because squares are nonnegative. |
| 2 | Complex failure: $v=(1,i)^T$, so $v^Tv=1+i^2=0$. |
| 3 | Need a mirror before dot product: $i$ must become $-i$. |
| 4 | Define $v^H=\overline v^T$. Immediate example: $(1,i)^H=(1,-i)$. |
| 5 | Corrected length: $v^Hv=1+(-i)i=2$. |
| 6 | Define Hermitian inner product: $\langle v,w\rangle_H=v^Hw$. |
| 7 | **Define Hermitian orthogonal:** $v\perp_H w\Longleftrightarrow v^Hw=0$. |
| 8 | Define Hermitian-orthogonal subspaces: $V\perp_H W$ iff every vector in $V$ is Hermitian-orthogonal to every vector in $W$. |

**Key line:** Complex geometry is not $v^Tw$ geometry; it is $v^Hw$ geometry.

---

### §2 — Hermitian Conjugate of Matrices

**Tension:** “If vectors need $H$, what is the mirror of a matrix?”

| Frame | Content |
|---|---|
| 1 | Define $A^H=\overline{A^T}$. |
| 2 | Immediate example: show transpose then conjugate for a $2\times2$ complex matrix. |
| 3 | Real callback: if $A$ is real, then $A^H=A^T$. |
| 4 | Product rule: $(AB)^H=B^HA^H$. Use a concrete visual order reversal. |
| 5 | Interpretation: $A^H$ is the matrix that moves from the other side of the Hermitian inner product. |

Possible formula for Frame 5:

$$
\langle Av,w\rangle_H=(Av)^Hw=v^HA^Hw=\langle v,A^Hw\rangle_H.
$$

This explains why $A^H$ is the correct “mirror action.”

---

### §3 — Normal Means Compatible with Its Mirror

**Tension:** “When does action commute with mirror-action?”

| Frame | Content |
|---|---|
| 1 | Define normal: $A$ is normal if $AA^H=A^HA$. |
| 2 | Define Hermitian symmetric: $A^H=A$. Immediate example; automatically normal. |
| 3 | Define skew-Hermitian symmetric: $A^H=-A$. Immediate example; automatically normal. |
| 4 | Define unitary: $A^HA=AA^H=I$. Immediate example; automatically normal. |
| 5 | Non-example: $J=\begin{pmatrix}1&1\\0&1\end{pmatrix}$; compute $JJ^H\ne J^HJ$. |
| 6 | Key: Hermitian, skew-Hermitian, and unitary are special normal matrices; later we explain them by eigenvalue location. |

**Do not jump to diagonalization as the payoff.** The next section must go to projections.

---

### §4 — Spectral Projections Are the Bridge

**Tension:** “How do we see eigenspaces without solving eigenvectors traditionally?”

Use the course’s existing spectral decomposition machinery.

| Frame | Content |
|---|---|
| 1 | Callback: for distinct eigenvalues, spectral projections are Lagrange polynomials in $A$: $P_i=f_i(A)$. |
| 2 | Projection meaning: $P_i$ extracts the $\lambda_i$-eigenspace component. |
| 3 | Decomposition: $I=P_1+\cdots+P_k$, $P_iP_j=0$, $A=\sum_i\lambda_iP_i$. |
| 4 | The question: are these projections oblique or orthogonal? |
| 5 | Reveal target: for normal $A$, every $P_i$ is Hermitian: $P_i^H=P_i$. |

**This section is essential.** It prevents the lecture from falling into the traditional “find eigenvectors and dot them” route.

---

### §5 — Polynomial of a Normal Matrix Is Normal

**Tension:** “Why should $P_i=f_i(A)$ inherit normality from $A$?”

| Frame | Content |
|---|---|
| 1 | Since $A$ is normal, $A$ commutes with $A^H$. |
| 2 | Therefore any power $A^m$ commutes with any power $(A^H)^n$. |
| 3 | For a polynomial $f$, $f(A)^H=\overline f(A^H)$, where coefficients are conjugated. |
| 4 | Hence $f(A)$ commutes with $f(A)^H$. |
| 5 | Conclusion: every polynomial in a normal matrix is normal. |

So each spectral projection

$$
P_i=f_i(A)
$$

is normal.

**Frame style:** keep this as a clean chain, not a dense proof.

---

### §6 — The Crucial Lemma: Normal Projection Is Hermitian

**Tension:** “A projection can be oblique. What kills obliqueness?”

This is the central proof and should be short and visual.

Let

$$
P^2=P,
\qquad
PP^H=P^HP.
$$

Then we want to prove

$$
P=P^H.
$$

Suggested proof route:

| Frame | Content |
|---|---|
| 1 | State lemma: normal projection $\Rightarrow$ Hermitian projection. |
| 2 | Start from the “difference from being Hermitian”: $M=P-P^H$. Want $M=0$. |
| 3 | Compute $MM^H=(P-P^H)(P^H-P)$. |
| 4 | Use $P^2=P$, $(P^H)^2=P^H$, and $PP^H=P^HP$ to simplify to $0$. |
| 5 | Positivity lemma: $MM^H=0\Rightarrow M=0$. Therefore $P=P^H$. |

A slightly cleaner alternative uses

$$
P-P^HP
$$

as in the legacy file. Either way, the slide should make the proof feel like:

> normality + projection identity leaves no room for obliqueness.

**Important:** This is the proof the lecture should spotlight.

---

### §7 — Main Payoff: Normality iff Hermitian Spectral Projections

**Tension:** “Where did orthogonality come from, and is this exactly normality?”

| Frame | Content |
|---|---|
| 1 | For normal $A$, each spectral projection $P_i=f_i(A)$ is normal. |
| 2 | Each $P_i$ is also a projection: $P_i^2=P_i$. |
| 3 | By the lemma, $P_i=P_i^H$. So $P_i$ is a Hermitian orthogonal projection. |
| 4 | Therefore $\operatorname{Im}(P_i)$ is Hermitian-orthogonal to $\operatorname{Im}(P_j)$ for $i\ne j$. |
| 5 | But $\operatorname{Im}(P_i)$ is exactly the $\lambda_i$-eigenspace. |
| 6 | Conclusion: eigenvectors from different eigenspaces are automatically Hermitian-orthogonal. |
| 7 | Converse direction: if all $P_i^H=P_i$, then $A=\sum_i\lambda_iP_i$ satisfies $AA^H=A^HA$ because the $P_i$ are Hermitian and mutually compatible. |
| 8 | Therefore normality is equivalent to Hermitian symmetric spectral projections. |

This should be the lecture’s main theorem:

$$
\boxed{
A\text{ normal}
\quad\Longleftrightarrow\quad
P_i^H=P_i\text{ for all spectral projections }P_i
\quad\Longleftrightarrow\quad
E_{\lambda_i}\perp_H E_{\lambda_j}.
}
$$

Then and only then mention:

$$
\Omega^HA\Omega=\Lambda
$$

by collecting orthonormal bases of those eigenspaces.

**Key phrasing:** Unitary diagonalization is a consequence of orthogonal eigenspaces, not the narrative endpoint.

---

### §8 — Worked Example via Projections, Not Traditional Eigenvectors

Use a real symmetric example so normality is visible:

$$
A=\begin{pmatrix}
-2&1&1\\
1&-2&1\\
1&1&-2
\end{pmatrix}.
$$

Correct eigenvalues:

$$
0,-3,-3.
$$

Suggested frames:

| Frame | Content |
|---|---|
| 1 | $A=A^T=A^H$, so $A$ is normal. |
| 2 | Characteristic information: eigenvalues $0$ and $-3$. |
| 3 | Projection onto the $0$-eigenspace using Lagrange formula: $P_0=\dfrac{A+3I}{3}$. |
| 4 | Projection onto the $-3$-eigenspace: $P_{-3}=I-P_0$. |
| 5 | Show $P_0^H=P_0$ and $P_{-3}^H=P_{-3}$. They are orthogonal projections. |
| 6 | Therefore every vector in $\operatorname{Im}(P_0)$ is orthogonal to every vector in $\operatorname{Im}(P_{-3})$. |

This example demonstrates the method:

> Use spectral projections first; orthogonality comes from Hermitian projection structure.

No traditional eigenvector-solving should be foregrounded.

---

### §9 — Special Normal Matrices: Eigenvalue Geometry

**Tension:** “Once a matrix is normal, what extra information do equations like $A^H=A$ impose?”

Start from the normal spectral decomposition:

$$
A=\sum_i\lambda_iP_i,
\qquad
P_i^H=P_i.
$$

Then

$$
A^H=\sum_i\overline{\lambda_i}P_i.
$$

Now each special type is just a condition on $\lambda_i$.

| Type | Matrix condition | Eigenvalue condition | Complex-plane picture |
|---|---|---|---|
| Hermitian symmetric | $A^H=A$ | $\overline\lambda=\lambda$ | real axis |
| Skew-Hermitian symmetric | $A^H=-A$ | $\overline\lambda=-\lambda$ | imaginary axis |
| Unitary | $A^HA=AA^H=I$ | $|\lambda|=1$ | unit circle |

Frame sequence:

| Frame | Content |
|---|---|
| 1 | Draw complex plane: real axis, imaginary axis, unit circle. No formulas yet. |
| 2 | Hermitian: $A^H=A$. Compare $\sum\bar\lambda_iP_i=\sum\lambda_iP_i$. So $\lambda_i\in\mathbb R$. |
| 3 | Skew-Hermitian: $A^H=-A$. Compare $\sum\bar\lambda_iP_i=-\sum\lambda_iP_i$. So $\lambda_i\in i\mathbb R$. |
| 4 | Unitary: $A^HA=I$. Spectrally: $\bar\lambda_i\lambda_i=1$. So $|\lambda_i|=1$. |
| 5 | Final visual summary: real axis = Hermitian, imaginary axis = skew-Hermitian, unit circle = unitary. |

This section is the second main payoff after orthogonal eigenspaces.

---

## 4. Revised Frame Count

| Section | Estimated Frames | Role |
|---|---:|---|
| §1 Hermitian inner product and orthogonality | 8 | Build complex geometry |
| §2 Hermitian conjugate | 5 | Define matrix mirror |
| §3 Normal condition and special examples | 6 | Define compatibility |
| §4 Spectral projections bridge | 5 | Use previous lectures |
| §5 Polynomial normality | 5 | Transfer normality to $P_i$ |
| §6 Normal projection lemma | 5 | Central proof |
| §7 Projection iff theorem | 8 | Main theorem |
| §8 Worked projection example | 6 | Method demonstration |
| §9 Special normal matrices | 5 | Eigenvalue geometry |
| Summary | 2 | Consolidation |
| **Total** | **~55** | Full lecture, projection-centered |

If this is too long, compress §2–§3, not §4–§7. The projection route is the core.

---

## 5. Implementation Priorities

1. **First priority:** Build §1–§7. This is the normal-matrix theorem in the course’s own language.
2. **Second priority:** Add §9 complex-plane classification, with a TikZ diagram of real axis, imaginary axis, and unit circle.
3. **Third priority:** Add the worked example only if time allows; it should use projections, not traditional eigenvector solving.

---

## 6. Summary Slide Target

Final summary should say:

$$
\boxed{AA^H=A^HA}
\quad\Longleftrightarrow\quad
\boxed{P_i=P_i^H\text{ for all spectral projections}}
\quad\Longleftrightarrow\quad
\boxed{E_{\lambda_i}\perp_H E_{\lambda_j}}.
$$

Then one complex-plane picture:

$$
\begin{array}{ccl}
A^H=A &\Longleftrightarrow& \lambda_i\in\mathbb R,\\
A^H=-A &\Longleftrightarrow& \lambda_i\in i\mathbb R,\\
A^HA=I &\Longleftrightarrow& |\lambda_i|=1.
\end{array}
$$

This is the correct endpoint: **normal matrices turn spectral decomposition into orthogonal geometry.**

---

Questions? {{SHELL_PREFIX}}$CALL_SESSION
