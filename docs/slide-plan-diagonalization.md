# Slide Plan: Eigenspaces, Diagonalization & the Two-Factor Decomposition

**Lecture:** 16  
**Placement:** After Lecture 15 (Spectral Decomposition & Value Tables)  
**Prerequisites students already have:** spectral decomposition $A = \lambda_1 P_1 + \cdots + \lambda_m P_m$, value table method, compatible projections and partition of $I$ (L08), cross-filling and two-factor decomposition $P = UV$ with $VU = I$ (L08), Lagrange interpolation for projections  
**Promise from L15's last frame:** "What subspace does each $P_i$ project onto? These subspaces are the eigenspaces of $A$."

### Standing Assumption (stated explicitly at the start of the lecture)

Throughout this lecture: $\det(tI - A)$ factors into **distinct** linear factors:

$$\det(tI - A) = (t - \lambda_1)(t - \lambda_2)\cdots(t - \lambda_m), \qquad \lambda_i \text{ all distinct}$$

This is the same assumption we used in L15 for spectral decomposition. We will revisit what this restriction really means at the end (§6).

---

## The Core Idea

L15 built the spectral projections $P_i$ as *polynomials of $A$* and used them to compute $A^n$. But the audience never SAW what these projections do geometrically. This lecture answers: **$P_i$ projects onto the subspace where $A$ acts like multiplication by $\lambda_i$ — that subspace is the eigenspace $E_{\lambda_i} = \operatorname{Col}(P_i)$.**

The column space is the central object. Matrix → column space → vectors.

Then we cross-fill each $P_i$ into its two-factor decomposition $P_i = U_i V_i$. The columns of $U_i$ are **(right) eigenvectors**, the rows of $V_i$ are **left eigenvectors**. Both matter. Stacking all the $U_i$ and $V_i$ gives $A = PDP^{-1}$ — not as a "change of basis" (we never use that concept), but as a purely algebraic consequence of cross-filling the spectral projections.

**Macro narrative:** Value tables verify everything, column space gives the geometry, cross-filling gives the algebra. Never mention change of basis.

---

## §1 — What Does $P_i$ Project Onto? (The Eigenspace)

**Tension:** "We found $P_1, P_3, P_5$ as matrices. But where do they send vectors?"

### Running Example (carried from L15)

$$A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{pmatrix}, \qquad P_1 = \begin{pmatrix}1&-1&0\\0&0&0\\0&0&0\end{pmatrix}, \quad P_3 = \begin{pmatrix}0&1&0\\0&1&0\\0&0&0\end{pmatrix}, \quad P_5 = \begin{pmatrix}0&0&0\\0&0&0\\0&0&1\end{pmatrix}$$

| Frame | Content |
|-------|---------|
| 1 | **Recall from L15:** $A = 1 \cdot P_1 + 3 \cdot P_3 + 5 \cdot P_5$. We know HOW to find $P_i$. But WHAT does $P_1$ do to a vector? |
| 2 | Pick a generic vector $\mathbf{v} = (5, 3, 7)^T$. Compute $P_1 \mathbf{v} = (2, 0, 0)^T$, $P_3 \mathbf{v} = (3, 3, 0)^T$, $P_5 \mathbf{v} = (0, 0, 7)^T$. |
| 3 | **Check:** $P_1 \mathbf{v} + P_3 \mathbf{v} + P_5 \mathbf{v} = (2,0,0) + (3,3,0) + (0,0,7) = (5,3,7) = \mathbf{v}$. Every vector splits into 3 pieces! |
| 4 | **TikZ diagram (3D):** Show $\mathbf{v}$ decomposed as the vector sum of 3 colored arrows lying in 3 different subspaces. Dashed lines for vector-sum construction. |
| 5 | **Key question:** What happens when $A$ acts on each piece? $A \cdot P_1\mathbf{v} = A(2,0,0)^T = (2,0,0)^T = 1 \cdot P_1\mathbf{v}$. The piece just gets scaled by $\lambda_1 = 1$! |
| 6 | Similarly: $A \cdot P_3\mathbf{v} = (9,9,0)^T = 3 \cdot (3,3,0)^T = 3 \cdot P_3\mathbf{v}$! And $A \cdot P_5\mathbf{v} = (0,0,35)^T = 5 \cdot P_5\mathbf{v}$. |
| 7 | **Reveal with underbrace:** $A\mathbf{v} = \underbrace{1}_{\lambda_1} \cdot P_1\mathbf{v} + \underbrace{3}_{\lambda_3} \cdot P_3\mathbf{v} + \underbrace{5}_{\lambda_5} \cdot P_5\mathbf{v}$. **$A$ scales each piece by its eigenvalue.** |
| 8 | **TikZ diagram (3D, before/after):** Same 3 arrows as Frame 4. Now each arrow is stretched by its eigenvalue. |

### Why does $AP_i = \lambda_i P_i$? — Value Table Proof (2 frames)

| Frame | Content |
|-------|---------|
| 9 | **Value table reasoning:** $A$ has value table $(1, 3, 5)$. $P_1$ has value table $(1, 0, 0)$. Multiply entry-wise: value table of $AP_1$ is $(1 \cdot 1,\; 3 \cdot 0,\; 5 \cdot 0) = (1, 0, 0)$. But $\lambda_1 P_1 = 1 \cdot P_1$ also has value table $1 \cdot (1,0,0) = (1,0,0)$. **Same value table → same matrix: $AP_1 = \lambda_1 P_1$.** |
| 10 | **Left multiplication too:** $P_1 A$ has the same value table (multiplication is entry-wise in value tables, so order doesn't matter): $(1,0,0) \cdot (1,3,5) = (1,0,0)$. So $P_1 A = \lambda_1 P_1 = AP_1$. **$A$ commutes with each $P_i$, and the value table proves it instantly.** |

### Eigenspace Definition (2 frames)

| Frame | Content |
|-------|---------|
| 11 | **From $AP_i = \lambda_i P_i$ to eigenvectors:** If $\mathbf{x} \in \operatorname{Col}(P_i)$, then $P_i \mathbf{x} = \mathbf{x}$ (projection fixes its column space), so $A\mathbf{x} = AP_i\mathbf{x} = \lambda_i P_i \mathbf{x} = \lambda_i \mathbf{x}$. Every vector in $\operatorname{Col}(P_i)$ is scaled by $\lambda_i$. |
| 12 | **Definition (boxed):** $E_{\lambda_i} = \operatorname{Col}(P_i)$ = the **eigenspace** of $\lambda_i$. Equivalently: $E_\lambda = \{\mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \lambda\mathbf{x}\}$. Check: $\operatorname{Col}(P_1) = \operatorname{span}\{(1,0,0)^T\}$, verify $A(1,0,0)^T = 1 \cdot (1,0,0)^T$ ✓. $\operatorname{Col}(P_3) = \operatorname{span}\{(1,1,0)^T\}$, verify $A(1,1,0)^T = 3(1,1,0)^T$ ✓. $\operatorname{Col}(P_5) = \operatorname{span}\{(0,0,1)^T\}$, verify $A(0,0,1)^T = 5(0,0,1)^T$ ✓. |

**Key insight frame:** "The value table makes $AP_i = \lambda_i P_i$ obvious. The column space of $P_i$ is the eigenspace — the place where $A$ just scales."

---

## §2 — Compatible Projections Revisited: Value Tables Verify Everything

**Tension:** "We claimed these $P_i$ partition space. Let's verify with value tables and connect to what we already know."

This section uses value tables to re-verify the compatible projection properties, then links to the compatible projections theory from L08 to give the geometric meaning.

| Frame | Content |
|-------|---------|
| 1 | **Value table review.** Recall the value tables: $P_1: (1,0,0)$, $P_3: (0,1,0)$, $P_5: (0,0,1)$. These are the "standard basis vectors" in value-table space. |
| 2 | **Projections?** Square each value table entry-wise: $(1,0,0)^2 = (1,0,0)$, $(0,1,0)^2 = (0,1,0)$, $(0,0,1)^2 = (0,0,1)$. Same value tables → $P_i^2 = P_i$ ✓. Each is a projection. |
| 3 | **Compatible?** Multiply value tables entry-wise across different $P_i$: $(1,0,0) \cdot (0,1,0) = (0,0,0) \implies P_1 P_3 = 0$ ✓. $(1,0,0) \cdot (0,0,1) = (0,0,0) \implies P_1 P_5 = 0$ ✓. $(0,1,0) \cdot (0,0,1) = (0,0,0) \implies P_3 P_5 = 0$ ✓. Different projections annihilate each other. |
| 4 | **Partition of $I$?** Add value tables: $(1,0,0) + (0,1,0) + (0,0,1) = (1,1,1)$. Value table $(1,1,1)$ = value table of $I$. So $P_1 + P_3 + P_5 = I$ ✓. |
| 5 | **Connect to L08 (boxed):** These are exactly the **compatible projections** from Lecture 8! Recall: compatible projections that partition $I$ decompose every vector uniquely — $\mathbf{v} = P_1\mathbf{v} + P_3\mathbf{v} + P_5\mathbf{v}$, with each piece in $\operatorname{Col}(P_i)$. The value table method from L15 automatically produces compatible projections. |
| 6 | **Corollary — eigenvectors with different eigenvalues are linearly independent.** If $\mathbf{x}_1 + \mathbf{x}_2 + \mathbf{x}_3 = 0$ with $\mathbf{x}_i \in E_{\lambda_i}$, apply $P_1$: $P_1\mathbf{x}_1 + 0 + 0 = 0 \implies \mathbf{x}_1 = 0$. Same for each. |
| 7 | **The big picture (boxed):** Under our standing assumption, the eigenspaces span $\mathbb{R}^n$: every vector decomposes as a sum of eigenvectors, one from each eigenspace, and this decomposition is **unique**. |
| 8 | **TikZ diagram (2D version for clarity):** $\mathbb{R}^2$ split into two lines (eigenspaces). Show 3–4 different vectors, each decomposed into colored components along the two eigenspace directions. Parallelogram construction with dashed lines. Every vector has a unique decomposition. |

**Key insight frame:** "Value tables verify the compatible projection properties instantly. Compatible projections guarantee the unique decomposition of every vector into eigenspace pieces."

---

## §3 — Cross-Filling the Spectral Projections: Eigenvectors and Left Eigenvectors

**Tension:** "We know the eigenspaces as column spaces. What do we get when we cross-fill each $P_i$?"

### New Example With a Non-Trivial Cross-Fill

The L15 running example has all rank-1 projections (each eigenvalue appears once) — cross-filling is trivial. For a richer example, use a matrix with a **repeated eigenvalue**, so that one projection has rank $> 1$ and genuinely needs cross-filling.

$$B = \begin{pmatrix} 2 & 0 & 3 \\ 0 & 2 & 3 \\ 0 & 0 & 5 \end{pmatrix}, \qquad \det(tI - B) = (t-2)^2(t-5)$$

Eigenvalues: $\lambda_1 = 2$ (appears twice), $\lambda_2 = 5$ (appears once).

**Note:** The characteristic polynomial has a REPEATED factor $(t-2)^2$. But the minimal polynomial is $(t-2)(t-5)$ — distinct factors. Our standing assumption is satisfied.

| Frame | Content |
|-------|---------|
| 1 | **Find projections by value tables.** Only 2 distinct eigenvalues, so value tables live in $\mathbb{R}^2$. $P_5$: value table $(0, 1)$ at eigenvalues $(2, 5)$. $P_5 = \frac{B - 2I}{5 - 2} = \frac{1}{3}\begin{pmatrix}0&0&3\\0&0&3\\0&0&3\end{pmatrix} = \begin{pmatrix}0&0&1\\0&0&1\\0&0&1\end{pmatrix}$. $P_2 = I - P_5 = \begin{pmatrix}1&0&-1\\0&1&-1\\0&0&0\end{pmatrix}$. |
| 2 | **Value table check:** $P_2$: value table $(1,0)$. $P_5$: value table $(0,1)$. $(1,0)^2 = (1,0)$ ✓. $(0,1)^2 = (0,1)$ ✓. $(1,0)(0,1) = (0,0)$ ✓. $(1,0)+(0,1) = (1,1)$ ✓. Compatible projections that partition $I$. |
| 3 | **Key observation:** $P_2$ has **rank 2**. Its eigenspace $E_2 = \operatorname{Col}(P_2)$ is a **plane** in $\mathbb{R}^3$, not just a line. This is a non-trivial projection — we need cross-filling to decompose it. |

### 3a: Cross-Fill $P_2$ (Rank 2 — Two Steps)

| Frame | Content |
|-------|---------|
| 4 | **Cross-fill $P_2 = \begin{pmatrix}1&0&-1\\0&1&-1\\0&0&0\end{pmatrix}$:** Pivot at $(1,1)$, value $= 1$. Column $\div$ pivot: $(1,0,0)^T$. Row: $(1,0,-1)$. Rank-1 piece: $R_1 = \begin{pmatrix}1\\0\\0\end{pmatrix}(1,0,-1) = \begin{pmatrix}1&0&-1\\0&0&0\\0&0&0\end{pmatrix}$. |
| 5 | **Remainder:** $P_2 - R_1 = \begin{pmatrix}0&0&0\\0&1&-1\\0&0&0\end{pmatrix}$. Pivot at $(2,2)$, value $= 1$. Column $\div$ pivot: $(0,1,0)^T$. Row: $(0,1,-1)$. $R_2 = \begin{pmatrix}0\\1\\0\end{pmatrix}(0,1,-1) = \begin{pmatrix}0&0&0\\0&1&-1\\0&0&0\end{pmatrix}$. |
| 6 | **Two-factor form:** $P_2 = U_2 V_2 = \begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}\begin{pmatrix}1&0&-1\\0&1&-1\end{pmatrix}$. Check: $V_2 U_2 = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2$ ✓. |

### 3b: Cross-Fill $P_5$ (Rank 1 — One Step)

| Frame | Content |
|-------|---------|
| 7 | **Cross-fill $P_5 = \begin{pmatrix}0&0&1\\0&0&1\\0&0&1\end{pmatrix}$:** Pivot at $(1,3)$, value $= 1$. Column $\div$ pivot: $(1,1,1)^T$. Row: $(0,0,1)$. $P_5 = U_5 V_5 = \begin{pmatrix}1\\1\\1\end{pmatrix}(0,0,1)$. Check: $V_5 U_5 = 1$ ✓. |

### 3c: What Are the Columns and Rows?

| Frame | Content |
|-------|---------|
| 8 | **Columns = right eigenvectors.** Columns of $U_2$: $(1,0,0)^T$ and $(0,1,0)^T$. These live in $\operatorname{Col}(P_2) = E_2$, so $B\mathbf{u} = 2\mathbf{u}$. Verify: $B(1,0,0)^T = (2,0,0)^T = 2(1,0,0)^T$ ✓. $B(0,1,0)^T = (0,2,0)^T = 2(0,1,0)^T$ ✓. Column of $U_5$: $(1,1,1)^T \in E_5$. $B(1,1,1)^T = (5,5,5)^T = 5(1,1,1)^T$ ✓. |
| 9 | **Rows = left eigenvectors.** They satisfy $\mathbf{v}^T B = \lambda \mathbf{v}^T$ (right-multiply $B$ gives $\lambda$). Rows of $V_2$: $(1,0,-1)B = (2,0,-2) = 2(1,0,-1)$ ✓. $(0,1,-1)B = (0,2,-2) = 2(0,1,-1)$ ✓. Row of $V_5$: $(0,0,1)B = (0,0,5) = 5(0,0,1)$ ✓. |
| 10 | **Both matter (boxed):** Cross-filling a spectral projection $P_i = U_i V_i$ gives right eigenvectors (columns of $U_i$) and left eigenvectors (rows of $V_i$). The cross-filling produces BOTH simultaneously. |

### 3d: The Cross Products — $VU = I$ Across Eigenspaces

| Frame | Content |
|-------|---------|
| 11 | **Within the same eigenspace:** $V_2 U_2 = I_2$ and $V_5 U_5 = 1$. Left eigenvectors "recognize" their own right eigenvectors. |
| 12 | **Across different eigenspaces:** $V_2 U_5 = \begin{pmatrix}1&0&-1\\0&1&-1\end{pmatrix}\begin{pmatrix}1\\1\\1\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}$. $V_5 U_2 = (0,0,1)\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix} = (0,0)$. Left eigenvectors "ignore" right eigenvectors from other eigenspaces. This comes from $P_2 P_5 = 0$: $U_2 (V_2 U_5) V_5 = 0 \implies V_2 U_5 = 0$. |

---

## §4 — Diagonalization: Stacking the Cross-Fillings

**Tension:** "We cross-filled each $P_i$ separately. What if we stack everything together?"

### 4a: Build $P$ and $P^{-1}$ by Stacking

| Frame | Content |
|-------|---------|
| 1 | **Stack the columns (right eigenvectors):** $P = \begin{pmatrix}U_2 & U_5\end{pmatrix} = \begin{pmatrix}1&0&1\\0&1&1\\0&0&1\end{pmatrix}$. |
| 2 | **Stack the rows (left eigenvectors):** $Q = \begin{pmatrix}V_2\\V_5\end{pmatrix} = \begin{pmatrix}1&0&-1\\0&1&-1\\0&0&1\end{pmatrix}$. |
| 3 | **Compute $QP$:** The $(i,j)$ entry of $QP$ is a dot product of a left eigenvector with a right eigenvector. Within same eigenspace: $V_i U_i = I$. Across eigenspaces: $V_i U_j = 0$. So $QP = I_3$. Therefore $Q = P^{-1}$! **The left eigenvector matrix IS the inverse of the right eigenvector matrix. This is the big $VU = I$ from all cross-fillings combined.** |

### 4b: The Diagonalization Formula

| Frame | Content |
|-------|---------|
| 4 | **Rebuild $B$ from the pieces:** $B = 2 P_2 + 5 P_5 = 2\, U_2 V_2 + 5\, U_5 V_5$ |
| 5 | **Factor (with underbrace):** $B = \underbrace{\begin{pmatrix}1&0&1\\0&1&1\\0&0&1\end{pmatrix}}_{P\text{ (right eigenvectors)}} \underbrace{\begin{pmatrix}2&&\\&2&\\&&5\end{pmatrix}}_{D\text{ (eigenvalues on diagonal)}} \underbrace{\begin{pmatrix}1&0&-1\\0&1&-1\\0&0&1\end{pmatrix}}_{P^{-1}\text{ (left eigenvectors)}}$ |
| 6 | **Verify:** $PDP^{-1} = \begin{pmatrix}1&0&1\\0&1&1\\0&0&1\end{pmatrix}\begin{pmatrix}2&&\\&2&\\&&5\end{pmatrix}\begin{pmatrix}1&0&-1\\0&1&-1\\0&0&1\end{pmatrix} = \begin{pmatrix}2&0&3\\0&2&3\\0&0&5\end{pmatrix} = B$ ✓ |

### 4c: The Cancellation Algebra — Why $PDP^{-1}$ Is Powerful

| Frame | Content |
|-------|---------|
| 7 | **What happens when you multiply $B \cdot B$?** $B^2 = (PDP^{-1})(PDP^{-1}) = PD\underbrace{(P^{-1}P)}_{= I}DP^{-1} = PD^2P^{-1}$. The $P^{-1}P$ in the middle cancels! |
| 8 | **Powers:** $B^n = \underbrace{(PDP^{-1})(PDP^{-1})\cdots(PDP^{-1})}_{n \text{ times}}$. Every adjacent $P^{-1}P$ cancels: $B^n = PD^nP^{-1}$. And $D^n = \begin{pmatrix}2^n&&\\&2^n&\\&&5^n\end{pmatrix}$ — diagonal matrices are trivial to exponentiate. |
| 9 | **Any polynomial (boxed):** If $B = PDP^{-1}$, then for ANY polynomial $g$: $g(B) = Pg(D)P^{-1}$. All the middle terms cancel. Computing $g$ on a diagonal matrix is trivial: $g(D) = \begin{pmatrix}g(2)&&\\&g(2)&\\&&g(5)\end{pmatrix}$. **The similarity $B = PDP^{-1}$ reduces every polynomial computation to plugging eigenvalues into $g$.** |
| 10 | **Connection to value tables:** This is the SAME thing as the value table method! $g(B)$ has value table $(g(2), g(5))$. The spectral formula says $g(B) = g(2) P_2 + g(5) P_5$. And $PDP^{-1}$ says $g(B) = Pg(D)P^{-1}$. These are two notations for the same machine. The cancellation algebra is WHY the value table method works. |

---

## §5 — Eigenspace Geometry: What Does $A$ Look Like?

**Tension:** "We've been computing. Let's DRAW what $A$ does to space."

Use a **2×2 example** for clearer pictures.

$$C = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}, \qquad \det(tI - C) = (t-2)(t-5)$$

Eigenvalues $2, 5$. Eigenvectors: $\mathbf{u}_1 = (1,-1)^T$ for $\lambda = 2$, $\mathbf{u}_2 = (2,1)^T$ for $\lambda = 5$.

| Frame | Content |
|-------|---------|
| 1 | **TikZ diagram (2D):** Two eigenspace lines through origin — $E_2$ along $(1,-1)$ and $E_5$ along $(2,1)$. Show 3–4 different vectors, each decomposed into colored components along the two directions. Parallelogram construction with dashed lines. |
| 2 | **TikZ diagram (2D, before/after):** Same vectors. $C$ acts: the $E_2$ component scales by 2, the $E_5$ component scales by 5. The total vector changes direction and length — but the PIECES just scale. |
| 3 | **TikZ diagram ($C^n$ iteration):** Show what happens when you apply $C$ repeatedly. The $E_5$ component grows $5\times$ each step, the $E_2$ component only $2\times$. After many steps, EVERY vector (except those exactly in $E_2$) aligns with $E_5$. **"The dominant eigenvalue wins."** |
| 4 | **Connection to value tables:** This is WHY the $5^n$ term dominates in $B^n$ for large $n$. The eigenspace of the largest eigenvalue eventually "swallows" everything. |

**Key insight frame:** "Eigenvalues tell you HOW MUCH each direction stretches. Eigenspaces tell you WHICH directions. Together, they completely describe what $A$ does."

---

## §6 — Our Restriction and the Minimal Polynomial

**Tension:** "We assumed distinct eigenvalues in $\det(tI - A)$. But $B$ from §3 had $(t-2)^2(t-5)$ — a REPEATED root — and everything still worked. What is our real restriction?"

| Frame | Content |
|-------|---------|
| 1 | **Review our philosophy:** We used $\det(tI - A)$ to find eigenvalues. But from L14 (Cayley-Hamilton): $\det(tI - A)$ is an ANNIHILATING polynomial. The characteristic polynomial is not special; it's just ONE annihilating polynomial that we know exists. |
| 2 | **Definition (boxed):** The **minimal polynomial** $m(t)$ is the lowest-degree monic polynomial such that $m(A) = 0$. It divides every annihilating polynomial (including $\det(tI-A)$). |
| 3 | **Our real restriction (boxed):** Everything in L15–L16 works as long as there exists an annihilating polynomial that factors into **distinct linear factors**: $m(t) = (t - \lambda_1)(t - \lambda_2)\cdots(t - \lambda_m)$, all $\lambda_i$ distinct. The characteristic polynomial may have repeats — like $\det(tI - B) = (t-2)^2(t-5)$ — and that's fine, because the MINIMAL polynomial $m(t) = (t-2)(t-5)$ has distinct factors. |
| 4 | **Example — $B$ from §3 again:** $\det(tI-B) = (t-2)^2(t-5)$. Repeated char. poly. root! But check: $(B-2I)(B-5I) = \begin{pmatrix}0&0&3\\0&0&3\\0&0&3\end{pmatrix}\begin{pmatrix}-3&0&3\\0&-3&3\\0&0&0\end{pmatrix} = 0$. So $m(t) = (t-2)(t-5)$ — distinct factors ✓. Everything works. |
| 5 | **Another example:** $A = \begin{pmatrix}3&0\\0&3\end{pmatrix}$. $\det(tI-A) = (t-3)^2$ (repeated!). But $A - 3I = 0$ already, so $m(t) = t - 3$ (degree 1). One distinct factor. Spectral decomposition: $A = 3I$, just one projection $P_1 = I$. The whole space is one eigenspace. Fine. |
| 6 | **What we cannot yet handle:** When the minimal polynomial itself has a repeated factor. Example: $A = \begin{pmatrix}2&1\\0&2\end{pmatrix}$. Check: $A - 2I = \begin{pmatrix}0&1\\0&0\end{pmatrix} \ne 0$, so $m(t) \ne t-2$. But $(A-2I)^2 = 0$, so $m(t) = (t-2)^2$. The repeated factor means there aren't enough eigenvectors. |
| 7 | **TikZ diagram:** $A = \begin{pmatrix}2&1\\0&2\end{pmatrix}$ acting on $\mathbb{R}^2$. The eigenspace $E_2$ is a single line ($\operatorname{span}\{(1,0)^T\}$). Vectors ON the line scale by 2. Vectors OFF the line scale by 2 AND shear — they don't stay on their own line. The shear comes from the $(t-2)^2$ factor in the minimal polynomial. |
| 8 | **Looking ahead:** When the minimal polynomial has repeated factors, we need new tools. That's a topic for a future lecture. For now: **distinct factors in the minimal polynomial = everything works.** |

**Key insight frame:** "The characteristic polynomial CAN repeat — that's fine. The minimal polynomial is what matters. Distinct factors → diagonalizable. Repeated factors → future topic."

---

## Summary & Preview

| Frame | Content |
|-------|---------|
| 1 | **Summary (boxed):** (1) $E_{\lambda_i} = \operatorname{Col}(P_i)$ — eigenspace = column space of spectral projection. (2) $P_i$ are compatible projections (value tables verify instantly); eigenvectors with different eigenvalues are linearly independent; every vector decomposes uniquely. (3) Cross-fill each $P_i = U_i V_i$: columns = right eigenvectors, rows = left eigenvectors, $V_i U_j = \delta_{ij} I$. (4) Stack: $A = PDP^{-1}$, and the cancellation $g(A) = Pg(D)P^{-1}$ reduces every computation to plugging eigenvalues into $g$. |
| 2 | **Preview:** "We can compute $A^n$ and soon $e^A$ via eigenvalues. Next: what if the matrix represents a RATE of change? → Matrix exponential and differential equations." |

---

## Section Summary

| Section | Frames (est.) | Phase | Role |
|---------|--------------|-------|------|
| §1 What does $P_i$ project onto? | 12 | Concretization | Eigenspace = Col($P_i$), value table proof of $AP_i = \lambda_i P_i$ |
| §2 Compatible projections revisited | 8 | Value table bridge | Re-verify via value tables, connect to L08 theory |
| §3 Cross-filling spectral projections | 12 | Core algebra | Non-trivial example $(t-2)^2(t-5)$, right & left eigenvectors |
| §4 Diagonalization: stack the pieces | 10 | Formalization | $PDP^{-1}$, cancellation algebra, connection to value tables |
| §5 Eigenspace geometry | 4 | Visual deepening | What $A$ does, dominant eigenvalue |
| §6 Our restriction & minimal polynomial | 8 | Boundary & future | Minimal poly is the real condition |
| Summary + preview | 2 | Wrap-up | |
| **Total** | **~56** | | |

---

## Design Decisions to Discuss

1. **§3 example choice:** Using $B = \begin{pmatrix}2&0&3\\0&2&3\\0&0&5\end{pmatrix}$ with eigenvalues $2, 2, 5$. The rank-2 projection $P_2$ requires genuine cross-filling (two steps). All numbers stay integer. The repeated eigenvalue also naturally sets up §6 (minimal polynomial). Alternative: a 4×4 with two rank-2 projections — richer but heavier.

2. **Left eigenvector depth:** Currently kept simple — just "$\mathbf{v}^T A = \lambda \mathbf{v}^T$, verify it." The deeper interpretation (left eigenvector as a linear functional / "detector" that extracts the eigenspace component) could be added if time permits, but current plan keeps it light per your guidance.

3. **§4c cancellation algebra:** This is the new section from your comment. It explicitly shows $P^{-1}P$ canceling in $B^2 = PD^2P^{-1}$ and generalizes to $g(B) = Pg(D)P^{-1}$. Ends by connecting back to value tables — the two viewpoints are the same machine.

4. **Frame count:** 56 frames is slightly higher than L15. If too dense, §5 (geometry, 4 frames) could be folded into §2 as TikZ examples, or §6 could be trimmed by combining the two "fine" examples (§3's $B$ and the $3I$ matrix).

5. **§1 → §2 flow:** §1 ends with eigenspace definition, §2 opens with value table verification of compatible projections. This creates a natural "pause and verify" moment before the heavier cross-filling in §3.

---

## TikZ Diagrams Needed

1. **§1 Frame 4:** 3D vector decomposition — $\mathbf{v}$ as sum of 3 colored arrows in 3 eigenspace directions
2. **§1 Frame 8:** Before/after — eigenspace components scaled by eigenvalues (3D)
3. **§2 Frame 8:** 2D eigenspace decomposition — multiple vectors decomposed along two eigenspace lines
4. **§5 Frame 1:** 2D eigenspace lines with vector decomposition and parallelogram construction
5. **§5 Frame 2:** Before/after action showing scaling along eigenspace directions
6. **§5 Frame 3:** Iterated $C^n$ — vectors converging to dominant eigenspace
7. **§6 Frame 7:** Shear matrix — eigenspace is only a line, off-line vectors shear

---

*This plan fulfills L15's "Next Lecture" promise. No change-of-basis language is used. Value tables are the primary verification tool. Diagonalization emerges from cross-filling the spectral projections. Sets up the exponential lecture as the next step.*
