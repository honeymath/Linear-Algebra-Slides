# Lecture 15: Eigenvalues & Eigenvectors — Revised Plan v3

## Big Picture (Narrative Arc)

**Emotional journey for students:**

1. "$A^n$ matters everywhere" — applications: recurrences, probability, money sharing
2. "Lecture 14's method is awkward — one step at a time" — tension
3. "Projections are easy: $P^n = P$" — comfort zone from Lectures 7–10
4. "Almost all matrices are **sums of projections**!" — reveal
5. "The weights are **eigenvalues**, the columns are **eigenvectors**" — definition
6. "Lagrange interpolation finds them — it generalizes the remainder theorem" — technique
7. "Now we get a **closed-form** for $A^n$!" — payoff

**Slogan**: *Projections are the simplest matrices. To study any matrix, decompose it into projections.*

---

## Running Example

$$A = \begin{pmatrix}1&0&1\\0&1&0\\1&0&1\end{pmatrix}, \quad \det(tI-A) = t(t-1)(t-2)$$

Eigenvalues $0, 1, 2$. All integer arithmetic throughout.

---

## Section Structure

---

### §1 — Why $A^n$? And Why We Need a Better Method (5 frames)

**Frame 1 — $A^n$ appears everywhere: Recurrences**

Classic example: $a_0 = 0,\; a_1 = 1,\; a_{n+1} = 3a_n - 2a_{n-1}$.

Rewrite as matrix power:
$$\begin{pmatrix}a_{n+1}\\a_n\end{pmatrix} = \begin{pmatrix}3&-2\\1&0\end{pmatrix}^n \begin{pmatrix}1\\0\end{pmatrix}$$

To find a formula for $a_n$, we need to compute $B^n$.

**Frame 2 — $A^n$ appears everywhere: Probability**

(From legacy `SpectralDecomposition.tex`)

Rolling a coin: face up → walk 3 meters, tail → walk 2 meters. What is the probability $p_n$ of landing exactly at the $n$-meter mark?

$$p_n = \tfrac{1}{2}p_{n-2} + \tfrac{1}{2}p_{n-3}$$

This is a recurrence → matrix power → need $A^n$.

**Frame 3 — $A^n$ appears everywhere: Money sharing**

Three cousins A, B, C each start with some money. Each round, each person gives $\frac{1}{3}$ of their money to each of the other two.

After $n$ rounds: $\vec{m}_n = M^n \vec{m}_0$ where $M = \begin{pmatrix}1/3 & 1/3 & 1/3 \\ 1/3 & 1/3 & 1/3 \\ 1/3 & 1/3 & 1/3\end{pmatrix}$.

What happens after many rounds? → need $M^n$.

All these problems reduce to computing **matrix powers**.

**Frame 4 — Lecture 14's method: step-by-step reduction (awkward)**

Lecture 14 gave us annihilating polynomials:
$$A^2 = 5A + 2I \;\implies\; A^3 = 27A + 10I \;\implies\; A^4 = 145A + 54I \;\implies\; \cdots$$

Each power needs its **own calculation**. Want $A^{100}$? Repeat 99 times.

We want a **closed-form formula**: plug in $n$, get the answer directly.

**Frame 5 — Projections: the easiest matrices to power**

Students know projections from Lectures 7–10:
$$P^2 = P \;\implies\; P^n = P \quad\text{for all } n \geq 1$$

What if we could decompose $A$ as a **weighted sum of projections**?

$$A = 2 P_1 + 3 P_2 \;\implies\; A^n = 2^n P_1 + 3^n P_2$$

A **closed form**! The dream: decompose any matrix into projections.

> **Slogan**: Projections are the simplest matrices. To understand any matrix, decompose it into projections.

**Questions we need to answer:**
1. What are the **weights** $\lambda_i$? → **eigenvalues**
2. What are the **projections** $P_i$? → their columns are **eigenvectors**
3. **How** to find the decomposition? → **Lagrange interpolation**

---

### §2 — Eigenvalues and Eigenvectors: Definition & Geometry (4 frames)

**Frame 6 — Geometric picture: what's special about eigenvectors?**

TikZ diagram showing matrix $A$ acting on several vectors in $\mathbb{R}^2$:
- A general vector $\vec{u}$: gets **rotated and stretched** → unexpected direction
- A special vector $\vec{v}$: gets **only scaled** by factor $\lambda$ → stays on the same line!

The special vectors are the ones $A$ treats simply.

**Frame 7 — Definition of eigenvalue and eigenvector**

> **Definition.** A **non-zero** vector $\vec{v}$ is an **eigenvector** of $A$ for **eigenvalue** $\lambda$ if
> $$A\vec{v} = \lambda\vec{v}$$

In words: $A$ acts on $\vec{v}$ by just multiplying by a scalar.

- $\lambda > 1$: stretched
- $0 < \lambda < 1$: shrunk
- $\lambda = 0$: killed (sent to zero)
- $\lambda < 0$: flipped and scaled

**Frame 8 — Where do eigenvalues come from?**

From Lecture 14:
$$\det(tI - A) = (t - \lambda_1)(t - \lambda_2)\cdots(t - \lambda_n)$$

The roots are the eigenvalues.

Running example: $\det(tI - A) = t(t-1)(t-2)$, eigenvalues: $0, 1, 2$.

**Frame 9 — The key question**

We know the eigenvalues from the characteristic polynomial.

But how do we find the **eigenvectors** and the **projections**?

> **Answer**: Lagrange interpolation builds the projections directly. The eigenvectors are their columns.

---

### §3 — From Remainder Theorem to Lagrange Interpolation (4 frames)

**Key pedagogical point**: Lagrange interpolation is the *natural generalization* of the Remainder Theorem from Lecture 14. When dividing by one factor $(t-a)$, the remainder is one number $g(a)$. When dividing by $m$ factors, the remainder is determined by $m$ values — and Lagrange basis polynomials assemble them.

**Frame 10 — Remainder Theorem: the 1-point case**

Recall Lecture 14: $g(t) = Q(t)(t-a) + g(a)$.

Dividing by **one** factor $(t-a)$: the remainder is determined by **one** value.

Rewrite: $g(t) = Q(t)(t-a) + g(a) \cdot \underbrace{1}_{f_a(t)}$

The "Lagrange basis" for 1 point is just the constant function $f_a(t) = 1$!

| | $f_a(t) = 1$ |
|---|---|
| $t = a$ | $1$ |

**Frame 11 — The 2-point case: dividing by $(t-1)(t-2)$**

Dividing by **two** factors: remainder has degree $\leq 1$, determined by **two** values $g(1)$ and $g(2)$.

Need basis polynomials:

| | $f_1(t) = -(t-2)$ | $f_2(t) = (t-1)$ |
|---|---|---|
| $t = 1$ | $1$ | $0$ |
| $t = 2$ | $0$ | $1$ |

$$g(t) = Q(t)(t-1)(t-2) + g(1) \cdot f_1(t) + g(2) \cdot f_2(t)$$

Same pattern as the remainder theorem, but with 2 points instead of 1!

**Frame 12 — The $m$-point case: Lagrange Interpolation**

Dividing by **$m$** factors $(t-\lambda_1)\cdots(t-\lambda_m)$: remainder determined by **$m$** values.

For eigenvalues $0, 1, 2$:

| | $f_0(t) = \frac{(t-1)(t-2)}{2}$ | $f_1(t) = -t(t-2)$ | $f_2(t) = \frac{t(t-1)}{2}$ |
|---|---|---|---|
| $t=0$ | $1$ | $0$ | $0$ |
| $t=1$ | $0$ | $1$ | $0$ |
| $t=2$ | $0$ | $0$ | $1$ |

Construction pattern: $f_{\lambda_i}(t) = \frac{\text{product of all }(t - \lambda_j)\text{ for }j \neq i}{\text{same product evaluated at }\lambda_i}$

**Frame 13 — The general theorem**

> **Theorem (Lagrange Interpolation = Generalized Remainder Theorem).**
>
> For any polynomial $g(t)$ and distinct points $\lambda_1, \ldots, \lambda_m$:
> $$g(t) = Q(t)\underbrace{(t-\lambda_1)\cdots(t-\lambda_m)}_{\text{divisor}} + \underbrace{g(\lambda_1)f_{\lambda_1}(t) + \cdots + g(\lambda_m)f_{\lambda_m}(t)}_{\text{remainder = Lagrange expansion}}$$

Progression:

| Dividing by | # of values that determine remainder | Name |
|---|---|---|
| $(t - a)$ | $1$ value: $g(a)$ | Remainder Theorem (Lecture 14) |
| $(t-a)(t-b)$ | $2$ values: $g(a), g(b)$ | Lagrange with 2 points |
| $(t-\lambda_1)\cdots(t-\lambda_m)$ | $m$ values: $g(\lambda_1), \ldots, g(\lambda_m)$ | Lagrange with $m$ points |

The Remainder Theorem is the **special case $m = 1$**.

---

### §4 — Spectral Decomposition (5 frames)

**Frame 14 — The trick: plug in $A$**

Apply Lagrange to $g(t) = t^n$ at eigenvalues $0, 1, 2$:

$$t^n = Q(t) \cdot t(t-1)(t-2) + 0^n f_0(t) + 1^n f_1(t) + 2^n f_2(t)$$

Plug in $t = A$:
$$A^n = Q(A) \cdot \underbrace{A(A-I)(A-2I)}_{= 0 \text{ (Cayley--Hamilton!)}} + 0^n f_0(A) + 1^n f_1(A) + 2^n f_2(A)$$

The quotient **vanishes**! For $n \geq 1$: $A^n = f_1(A) + 2^n f_2(A)$.

Compute $f_1(A)$ and $f_2(A)$ explicitly → closed-form $A^n$.

$$A^n = \begin{pmatrix}2^{n-1}&0&2^{n-1}\\0&1&0\\2^{n-1}&0&2^{n-1}\end{pmatrix}$$

**Frame 15 — The general principle: $g(A)$ depends only on values at eigenvalues**

> **Theorem.** If $(A - \lambda_1 I)\cdots(A - \lambda_m I) = 0$ with **distinct** $\lambda_i$, then:
> $$g(A) = g(\lambda_1) P_{\lambda_1} + g(\lambda_2) P_{\lambda_2} + \cdots + g(\lambda_m) P_{\lambda_m}$$
> where $P_{\lambda_i} = f_{\lambda_i}(A)$ are the **spectral projections**.

**Frame 16 — $P_{\lambda_i}$ are projections! Partition of identity!**

Value table argument:
- $f_{\lambda_i}(\lambda_j)^2 = f_{\lambda_i}(\lambda_j)$ (values are $0$ or $1$, so squaring doesn't change them) → $P_i^2 = P_i$
- Set $g = 1$: $I = P_1 + P_2 + \cdots + P_m$

Verify: $P_0 + P_1 + P_2 = I$ ✓

The dream from §1 is coming true: the identity is a sum of projections!

**Frame 17 — Spectral Decomposition: $A = \lambda_1 P_1 + \cdots + \lambda_m P_m$**

Set $g(t) = t$:
$$A = \lambda_1 P_{\lambda_1} + \lambda_2 P_{\lambda_2} + \cdots + \lambda_m P_{\lambda_m}$$

Verify: $0 \cdot P_0 + 1 \cdot P_1 + 2 \cdot P_2 = A$ ✓

**This is spectral decomposition**: any matrix (satisfying a simple-root annihilating polynomial) is a weighted sum of projections!

**Frame 18 — Eigenvectors from projections**

From the Lagrange construction: $(t - \lambda_i) \cdot f_{\lambda_i}(t)$ contains the full product $(t-\lambda_1)\cdots(t-\lambda_m)$.

Plug in $A$: $(A - \lambda_i I) P_{\lambda_i} = 0$, so $AP_{\lambda_i} = \lambda_i P_{\lambda_i}$.

Column by column: $A\vec{v}_j = \lambda_i \vec{v}_j$ for every non-zero column $\vec{v}_j$ of $P_{\lambda_i}$.

They are **eigenvectors**!

| Eigenvalue | $P_{\lambda_i}$ | Eigenvector | Verify |
|---|---|---|---|
| $\lambda = 0$ | $\frac{1}{2}\begin{pmatrix}1&0&-1\\0&0&0\\-1&0&1\end{pmatrix}$ | $\begin{pmatrix}1\\0\\-1\end{pmatrix}$ | $A\vec{v} = \vec{0} = 0\vec{v}$ ✓ |
| $\lambda = 1$ | $\begin{pmatrix}0&0&0\\0&1&0\\0&0&0\end{pmatrix}$ | $\begin{pmatrix}0\\1\\0\end{pmatrix}$ | $A\vec{v} = \vec{v} = 1\vec{v}$ ✓ |
| $\lambda = 2$ | $\frac{1}{2}\begin{pmatrix}1&0&1\\0&0&0\\1&0&1\end{pmatrix}$ | $\begin{pmatrix}1\\0\\1\end{pmatrix}$ | $A\vec{v} = 2\vec{v}$ ✓ |

---

### §5 — Applications (3 frames)

**Frame 19 — Solving the recurrence from §1**

$a_0 = 0, a_1 = 1, a_{n+1} = 3a_n - 2a_{n-1}$. Matrix: $B = \begin{pmatrix}3&-2\\1&0\end{pmatrix}$, char poly $(t-1)(t-2)$.

Lagrange at $1, 2$: $B^n = 1^n \cdot (-(B-2I)) + 2^n \cdot (B-I)$

$$\begin{pmatrix}a_{n+1}\\a_n\end{pmatrix} = B^n\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}2^{n+1}-1\\2^n-1\end{pmatrix}$$

$$\boxed{a_n = 2^n - 1}$$

**Frame 20 — Solving the probability problem from §1**

The coin-rolling problem: $p_n = \frac{1}{2}p_{n-2} + \frac{1}{2}p_{n-3}$

Matrix: $C = \begin{pmatrix}0&1/2&1/2\\1&0&0\\0&1&0\end{pmatrix}$, char poly $(t-1)(t^2+t/2+1/2)$.

Since char poly has one real root $t = 1$ and complex roots, spectral decomposition applies. (Or simplify: steady-state probability as $n \to \infty$.)

**Frame 21 — The power of spectral decomposition (summary)**

> **Spectral Decomposition** $A = \lambda_1 P_1 + \cdots + \lambda_m P_m$ gives:
> - **Closed-form** $A^n = \lambda_1^n P_1 + \cdots + \lambda_m^n P_m$
> - **Eigenvectors** = columns of $P_i$ (no equation solving needed!)
> - **Long-term behavior**: as $n \to \infty$, the largest $|\lambda_i|^n$ dominates

---

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| §1 opens with 3 application problems (recurrence, probability, money) | User: "search for like 3 cousin separate money problem, and other probability problems" |
| Lecture 14 contrast: awkward step-by-step vs closed form | User: "last lecture we have way to compute $A^n$, but awkwardly, this time we will give a close formula powerful!" |
| §2 gives definition + geometry BEFORE technique | User: "you even do not give motivation and definition" |
| §3 frames Lagrange as generalization of Remainder Theorem | User: "make the remainder theorem in this framework, where the Lagrange interpolation is just $m=1$" |
| Progression table: $m=1$ → $m=2$ → general $m$ | User: "Make people see it is a general generalization" |
| Eigenvectors from projection columns, never from $(A-\lambda I)\vec{v}=0$ | Forbidden: equation solving |

## What's NOT Included (Scope Boundary)

- Repeated roots / Jordan form → future lecture
- Solving $(A - \lambda I)\vec{v} = 0$ by row reduction → forbidden; use projections
- Left eigenvectors → secondary
- Diagonalizability criterion → future lecture

## Estimated Size

~21 frames across 5 sections.

---

Questions? {{SHELL_PREFIX}}el
