# Slide Plan: Lecture 21 — Positive Definite and Positive Semidefinite Matrices

**Placement:** Last lecture, after SVD.  
**Main goal:** classify real symmetric matrices by the geometry of the quadratic form

$$
q_A(x)=x^TAx.
$$

The motivating question should not be an abstract definition. It should be:

$$
\boxed{\text{When can a real symmetric matrix be written as }A=M^TM?}
$$

Equivalently:

$$
\boxed{x^TAx=\|Mx\|^2.}
$$

If this is possible, then $x^TAx$ can never be negative. This forces us to study which symmetric matrices always give nonnegative quadratic forms.

---

## 0. Thesis

A real symmetric matrix $A$ should be read as a machine that assigns a squared length:

$$
\|x\|_A^2=x^TAx.
$$

But not every symmetric matrix gives a real length. The set

$$
\{x:x^TAx=1\}
$$

may be:

- an ellipse/circle — good length geometry;
- parallel lines/cylinder-like degenerate geometry — semidefinite boundary case;
- a hyperbola — not length geometry.

The lecture’s endpoint is a set of practical tests:

$$
\boxed{A\succeq 0\quad\Longleftrightarrow\quad x^TAx\ge0\text{ for all }x}
$$

and ways to verify it:

1. **Eigenvalue criterion:** real symmetric $A$ is PSD iff all eigenvalues are nonnegative; PD iff all are positive.
2. **Diagonal cross-filling criterion:** diagonal pivots reveal the sign structure; positive pivots give positive definite, nonnegative pivots with zero-row/column handling give semidefinite, negative pivots give negative directions.
3. **Factorization criterion:** $A=M^TM$ iff $A$ is positive semidefinite; full-column-rank $M$ gives positive definite.

---

## 1. Legacy Evidence and Ingredients

From `positiveDefiniteMatrix.tex`, keep and reorganize these ideas:

### 1.1 Bilinear forms and matrices

Every symmetric bilinear form on $\mathbb R^n$ can be written as

$$
\langle v,w\rangle_A=v^TAw.
$$

The matrix $A$ is the value table of the form on the standard basis:

$$
a_{ij}=e_i^TAe_j.
$$

### 1.2 Natural construction from $M^TM$

For any matrix $M$,

$$
x^TM^TMx=\|Mx\|^2\ge0.
$$

If $M$ has linearly independent columns, then $Mx\ne0$ for $x\ne0$, hence

$$
x^TM^TMx>0\qquad(x\ne0).
$$

So:

- $M^TM$ is always positive semidefinite;
- $M^TM$ is positive definite iff columns of $M$ are linearly independent.

This is the right motivation for the question “when is $A=M^TM$?”

### 1.3 Unit ball pictures

Legacy gives the correct visual examples:

| Matrix | Equation $x^TAx=1$ | Shape |
|---|---|---|
| $\begin{pmatrix}1/4&0\\0&1\end{pmatrix}$ | $x^2/4+y^2=1$ | ellipse |
| $\begin{pmatrix}0&0\\0&1\end{pmatrix}$ | $y^2=1$ | two parallel lines |
| $\begin{pmatrix}-1&0\\0&1\end{pmatrix}$ | $-x^2+y^2=1$ | hyperbola |

These should be early slides, before formal definitions.

### 1.4 Eigenvalue criterion

Use real symmetric orthogonal diagonalization:

$$
A=\Omega\Lambda\Omega^T.
$$

Then

$$
x^TAx=(\Omega^Tx)^T\Lambda(\Omega^Tx).
$$

So sign of $x^TAx$ is controlled by diagonal entries/eigenvalues of $\Lambda$.

Conclusion:

$$
A\succeq0\Longleftrightarrow \lambda_i\ge0\text{ for all }i,
$$

$$
A\succ0\Longleftrightarrow \lambda_i>0\text{ for all }i.
$$

### 1.5 Cauchy inequality is needed for cross-filling proof

Legacy proves Cauchy inequality for PSD forms:

$$
\langle x,y\rangle_A^2\le \langle x,x\rangle_A\langle y,y\rangle_A.
$$

This is used crucially for:

1. If a PSD matrix has a zero diagonal entry, then the whole row and column are zero.
2. In diagonal cross-filling, if pivot $a=e_i^TAe_i>0$, then the remainder
   $$
   A-P
   $$
   is PSD because
   $$
   v^TAv\ge v^TPv
   $$
   follows from Cauchy:
   $$
   \langle v,v\rangle_A\ge \frac{\langle v,e_i\rangle_A^2}{\langle e_i,e_i\rangle_A}.
   $$

This must appear in the plan and proof, not be skipped.

### 1.6 Standard-basis notation must be visually introduced

Before writing expressions like

$$
e_i^TAe_i,
$$

the slides must explicitly explain:

- $e_i$ is the $i$-th standard basis vector;
- multiplying by $e_i$ selects the $i$-th column/row;
- $e_i^TAe_i$ extracts the $i$-th diagonal entry $a_{ii}$.

This should be shown by a colored matrix picture, not only symbols.

Suggested visual frame:

$$
e_2=
\begin{pmatrix}0\\ \color{red}{1}\\0\end{pmatrix},
\qquad
A=
\begin{pmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&\color{red}{a_{22}}&a_{23}\\
a_{31}&a_{32}&a_{33}
\end{pmatrix}.
$$

Then show step-by-step:

$$
Ae_2=
\begin{pmatrix}
a_{12}\\ \color{red}{a_{22}}\\ a_{32}
\end{pmatrix}
\quad\text{selects column 2,}
$$

and

$$
e_2^TAe_2=\color{red}{a_{22}}.
$$

For cross-filling, this visual also explains why $e_i^TAe_i$ is the diagonal pivot.

---

## 2. Main Narrative

### §1 — Can Every Symmetric Matrix Be $M^TM$?

**Tension:** “We know $M^TM$ always gives squared length. Which symmetric matrices come from this construction?”

Frame plan:

| Frame | Content |
|---|---|
| 1 | Start with $x^TM^TMx=\|Mx\|^2\ge0$. This is always safe. |
| 2 | Ask: given a symmetric $A$, can we write $A=M^TM$? |
| 3 | Necessary condition: $x^TAx$ must never be negative. |
| 4 | Define the shape $\{x:x^TAx=1\}$. If $A=M^TM$, this is a pulled-back sphere/ellipse-type object. |
| 5 | Guiding question: how do we test whether $x^TAx$ is always positive/nonnegative? |

Key line:

$$
A=M^TM\quad\Rightarrow\quad x^TAx=\|Mx\|^2\ge0.
$$

---

### §2 — Three Pictures: Ellipse, Lines, Hyperbola

**Tension:** “What can $x^TAx=1$ look like?”

Use concrete $2\times2$ diagonal matrices.

| Frame | Content |
|---|---|
| 1 | Positive definite example: $A=\begin{pmatrix}1/4&0\\0&1\end{pmatrix}$ gives an ellipse. |
| 2 | Positive semidefinite example: $A=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ gives $y=\pm1$, a degenerate ellipse/strip boundary. |
| 3 | Indefinite example: $A=\begin{pmatrix}-1&0\\0&1\end{pmatrix}$ gives a hyperbola. |
| 4 | Show the sign table: positive coefficients produce ellipses; mixed signs produce hyperbolas; zeros produce degeneracy. |
| 5 | Reveal vocabulary: positive definite, positive semidefinite, indefinite. |

Definitions should come after the pictures:

$$
A\succ0\quad\Longleftrightarrow\quad x^TAx>0\text{ for all }x\ne0.
$$

$$
A\succeq0\quad\Longleftrightarrow\quad x^TAx\ge0\text{ for all }x.
$$

---

### §3 — Bilinear Forms: Matrix as Inner-Product Table

**Tension:** “Why do symmetric matrices appear at all?”

Frame plan:

| Frame | Content |
|---|---|
| 1 | Recall ordinary dot product: $v^Tw$. |
| 2 | General symmetric form: $\langle v,w\rangle_A=v^TAw$. |
| 3 | Matrix entries are values on basis vectors: $a_{ij}=e_i^TAe_j$. |
| 4 | Symmetry of the form means $A=A^T$. |
| 5 | Inner product = symmetric bilinear form + positive definiteness. |

This section can be short. It just explains the vocabulary.

---

### §4 — Eigenvalue Criterion

**Tension:** “Can we test positivity using the real symmetric spectral theorem?”

Use the previous lectures directly.

**Root-first structure:** Do not begin with the proof. First show one example where the criterion immediately decides the geometry.

Example reveal:

$$
A=\begin{pmatrix}3&1\\1&3\end{pmatrix}
\quad\Rightarrow\quad
\lambda_1=4,\ \lambda_2=2.
$$

Therefore $A\succ0$ immediately, so $x^TAx=1$ is an ellipse.

Contrast:

$$
B=\begin{pmatrix}1&2\\2&1\end{pmatrix}
\quad\Rightarrow\quad
\lambda_1=3,\ \lambda_2=-1.
$$

Therefore $B$ is indefinite immediately, so $x^TBx=1$ is hyperbola-type.

Frame plan:

| Frame | Content |
|---|---|
| 1 | Powerful example: compute eigenvalues of $A=\begin{pmatrix}3&1\\1&3\end{pmatrix}$; all positive, so ellipse/PD. |
| 2 | Powerful counterexample: $B=\begin{pmatrix}1&2\\2&1\end{pmatrix}$ has one negative eigenvalue, so hyperbola/indefinite. |
| 3 | State the eigenvalue criterion as a theorem. |
| 4 | Now justify: real symmetric matrix has orthogonal diagonalization $A=\Omega\Lambda\Omega^T$. |
| 5 | Change coordinates: set $y=\Omega^Tx$. |
| 6 | Compute $x^TAx=y^T\Lambda y=\lambda_1y_1^2+\cdots+\lambda_ny_n^2$. |
| 7 | Diagonal signs explain ellipse/hyperbola/degenerate shape. |

This is the easy and conceptually transparent criterion.

---

### §5 — Factorization Criterion $A=M^TM$

**Tension:** “Does nonnegative quadratic form actually imply $A=M^TM$?”

Use eigenvalue criterion to prove factorization.

Again, start from a concrete success before proof:

$$
A=\begin{pmatrix}3&1\\1&3\end{pmatrix}
=\Omega
\begin{pmatrix}4&0\\0&2\end{pmatrix}
\Omega^T.
$$

Then

$$
A=(\sqrt\Lambda\Omega^T)^T(\sqrt\Lambda\Omega^T),
\qquad
\sqrt\Lambda=\begin{pmatrix}2&0\\0&\sqrt2\end{pmatrix}.
$$

This shows the criterion’s power before deriving the general formula.

If

$$
A=\Omega\Lambda\Omega^T,
\qquad \Lambda=\operatorname{diag}(\lambda_i),\quad \lambda_i\ge0,
$$

then define

$$
\sqrt\Lambda=\operatorname{diag}(\sqrt{\lambda_i}).
$$

Then

$$
A=\Omega\sqrt\Lambda\sqrt\Lambda\Omega^T
=(\sqrt\Lambda\Omega^T)^T(\sqrt\Lambda\Omega^T).
$$

So take

$$
M=\sqrt\Lambda\Omega^T.
$$

Frame plan:

| Frame | Content |
|---|---|
| 1 | Powerful example: positive eigenvalues let us take square roots and write $A=M^TM$. |
| 2 | State the factorization criterion: $A=M^TM$ iff $A\succeq0$. |
| 3 | Easy direction: if $A=M^TM$, then $x^TAx=\|Mx\|^2\ge0$. |
| 4 | Converse: if $A$ is PSD, eigenvalues are nonnegative. |
| 5 | Take square roots of eigenvalues. |
| 6 | Build $M=\sqrt\Lambda\Omega^T$. |
| 7 | PD iff $M$ has independent columns / no zero singular lengths. |

This answers the opening question.

---

### §6 — Why Cross-Filling Needs Cauchy Inequality

**Tension:** “Eigenvalues are clean, but can our course’s cross-filling machinery test positivity?”

**Root-first structure:** Before proving Cauchy, show why cross-filling is powerful.

Use a concrete matrix:

$$
A=\begin{pmatrix}
1&3&2\\
3&10&7\\
2&7&9
\end{pmatrix}.
$$

Diagonal cross-filling peels off positive rank-one pieces:

$$
A=
\begin{pmatrix}1\\3\\2\end{pmatrix}
\begin{pmatrix}1&3&2\end{pmatrix}
+
\begin{pmatrix}0\\1\\1\end{pmatrix}
\begin{pmatrix}0&1&1\end{pmatrix}
+
\begin{pmatrix}0\\0\\2\end{pmatrix}
\begin{pmatrix}0&0&2\end{pmatrix}.
$$

Therefore the matrix is a sum of squared-length pieces and is positive definite. This is the power of the criterion.

Only after this reveal do we explain the proof mechanism: Cauchy inequality.

Before proving the cross-filling criterion, prove two PSD facts.

#### Lemma 1: zero diagonal forces zero row/column

If $A\succeq0$ and $a_{ii}=0$, then for every $j$,

$$
a_{ij}=0.
$$

Proof uses Cauchy:

$$
a_{ij}^2=\langle e_i,e_j\rangle_A^2
\le \langle e_i,e_i\rangle_A\langle e_j,e_j\rangle_A
=0\cdot a_{jj}=0.
$$

#### Lemma 2: PSD Cauchy inequality

Need to prove or at least state with proof:

$$
\langle x,y\rangle_A^2\le \langle x,x\rangle_A\langle y,y\rangle_A.
$$

Legacy proof uses

$$
w=\langle x,x\rangle_Ay-\langle x,y\rangle_Ax
$$

when $\langle x,x\rangle_A>0$, plus the zero-length case.

Frame plan:

| Frame | Content |
|---|---|
| 1 | Need a tool: PSD forms satisfy Cauchy. |
| 2 | Geometric intuition: dot product of unit vectors is at most 1. |
| 3 | Proof setup with $w=\langle x,x\rangle_Ay-\langle x,y\rangle_Ax$. |
| 4 | Expand $0\le\langle w,w\rangle_A$. |
| 5 | Divide and get Cauchy. |
| 6 | Use Cauchy to prove zero diagonal row/column lemma. |

This section is important because the cross-filling proof depends on it.

---

### §7 — Diagonal Cross-Filling Criterion

**Tension:** “Can diagonal cross-filling certify positivity without computing eigenvalues?”

Open this section with the criterion statement and a fast example before the proof.

Criterion preview:

> If diagonal cross-filling keeps producing positive pivots until the remainder is $0$, then the matrix is positive definite.
>
> If the process only produces positive pivots plus zero rows/columns in the remainder, then the matrix is positive semidefinite.
>
> A negative pivot/remainder obstruction proves the matrix is not positive semidefinite.

Fast examples:

- Positive: $A=\begin{pmatrix}1&3&2\\3&10&7\\2&7&9\end{pmatrix}$ gives pivots $1,1,4$.
- Not PSD: $B=\begin{pmatrix}1&3&2\\3&5&4\\2&4&9\end{pmatrix}$ gives a negative diagonal entry in the remainder after the first cross-fill.

Then dive into the proof.

Let $A$ be symmetric and choose a diagonal pivot

$$
a=e_i^TAe_i=a_{ii}\ne0.
$$

The diagonal cross-filling rank-one piece is

$$
P=Ae_i(e_i^TAe_i)^{-1}e_i^TA.
$$

Then

$$
v^TPv=\frac{\langle v,e_i\rangle_A^2}{\langle e_i,e_i\rangle_A}
=\frac{\langle v,e_i\rangle_A^2}{a}.
$$

So:

- if $a>0$, then $P\succeq0$;
- if $a<0$, then $-P\succeq0$.

For PSD $A$ and $a>0$, the remainder is PSD because Cauchy gives

$$
v^T(A-P)v
=\langle v,v\rangle_A-rac{\langle v,e_i\rangle_A^2}{\langle e_i,e_i\rangle_A}
\ge0.
$$

Frame plan:

| Frame | Content |
|---|---|
| 1 | Recall diagonal cross-filling at pivot $a_{ii}$. |
| 2 | Write rank-one piece $P=Ae_i a^{-1}e_i^TA$. |
| 3 | Compute $v^TPv=\langle v,e_i\rangle_A^2/a$. |
| 4 | Positive pivot gives PSD rank-one piece. Negative pivot gives negative rank-one piece. |
| 5 | If $A$ is PSD, Cauchy proves $A-P$ is PSD. |
| 6 | Conversely, if $a>0$ and $A-P$ is PSD, then $A=P+(A-P)$ is PSD. |
| 7 | Therefore diagonal cross-filling gives a recursive PSD test. |

Important correction to phrase carefully:

- For **positive definite**, diagonal cross-filling should produce strictly positive pivots all the way until zero remainder.
- For **positive semidefinite**, pivots are positive for nonzero active directions, but zero diagonal pivots require the zero-row/column rule. It is safer to say: all extracted nonzero pivots are positive, and any zero diagonal in the remainder must have zero row/column; equivalently no negative pivot/negative remainder appears.
- For negative definite, apply the same criterion to $-A$.
- For indefinite, cross-filling eventually exposes both positive and negative behavior, or a negative pivot/remainder obstruction.

---

### §8 — Worked Cross-Filling Examples

Use legacy examples, but organize visually.

#### Example A: not PSD because zero diagonal row is not zero

Legacy example:

$$
\begin{pmatrix}
1&2&-3\\
2&0&2\\
-3&2&5
\end{pmatrix}
$$

The middle diagonal is $0$, but the middle row/column is not zero. By zero diagonal lemma, not PSD.

#### Example B: cross-filling reveals negative pivot/remainder

Legacy example:

$$
\begin{pmatrix}
1&3&2\\
3&5&4\\
2&4&9
\end{pmatrix}
$$

After first diagonal cross-fill, the remainder has a negative diagonal entry:

$$
\begin{pmatrix}
0&0&0\\
0&-4&-2\\
0&-2&5
\end{pmatrix}.
$$

Not PSD.

#### Example C: positive definite and factorization

Legacy example:

$$
A=\begin{pmatrix}
1&3&2\\
3&10&7\\
2&7&9
\end{pmatrix}.
$$

Cross-filling gives

$$
A=
\begin{pmatrix}1\\3\\2\end{pmatrix}
\begin{pmatrix}1&3&2\end{pmatrix}
+
\begin{pmatrix}0\\1\\1\end{pmatrix}
\begin{pmatrix}0&1&1\end{pmatrix}
+
\begin{pmatrix}0\\0\\2\end{pmatrix}
\begin{pmatrix}0&0&2\end{pmatrix}.
$$

Therefore

$$
A=M^TM
$$

for an appropriate triangular $M$ built from the cross-filling vectors. This gives the computational factorization payoff.

Frame plan:

| Frame | Content |
|---|---|
| 1 | Example A: zero diagonal but nonzero row — immediately not PSD. |
| 2 | Example B: first cross-fill, show negative remainder diagonal. |
| 3 | Example C: first positive pivot and remainder. |
| 4 | Example C continued: second positive pivot. |
| 5 | Example C continued: third positive pivot. |
| 6 | Write sum of rank-one PSD pieces. |
| 7 | Convert sum of rank-one pieces into $M^TM$. |

Use colors for pivots and remainders, matching prior cross-filling style.

---

## 3. Proposed Lecture Structure

| Section | Frames | Purpose |
|---|---:|---|
| §1 Opening question $A=M^TM$ | 5 | Motivation |
| §2 Ellipse/lines/hyperbola pictures | 5 | Geometry before definition |
| §3 Bilinear form vocabulary | 5 | Formal definition |
| §4 Eigenvalue criterion | 6 | Easy spectral test |
| §5 Factorization criterion | 6 | Answer opening question |
| §6 Cauchy inequality and zero diagonal lemma | 6 | Tool for cross-filling proof |
| §7 Cross-filling criterion | 7 | Course-native computational test |
| §8 Worked examples and $M^TM$ construction | 7 | Concrete computation |
| §9 Final summary | 2 | Compare criteria |

Estimated total: **49 frames**.

---

## 4. Final Summary Slide

The final slide should compare the three tests:

| Test | Criterion | Meaning |
|---|---|---|
| Quadratic form | $x^TAx\ge0$ for all $x$ | definition |
| Eigenvalues | all $\lambda_i\ge0$ | spectral/geometry test |
| Cross-filling | positive pivots + PSD remainders | computational course method |
| Factorization | $A=M^TM$ | squared-length construction |

For positive definite, replace $\ge0$ by $>0$ for $x\ne0$, eigenvalues by $>0$, and cross-filling by strictly positive pivots without degeneracy.

---

## 5. Design Notes

1. **Do not start with definitions.** Start with $A=M^TM$ and geometry of $x^TAx=1$.
2. **Use real symmetric matrices only.** This is a real-number application of the previous normal/symmetric theorem.
3. **Draw the shapes.** Ellipse, degenerate lines, and hyperbola must appear before the vocabulary.
4. **Be precise about semidefinite cross-filling.** Zero pivots are subtle: a PSD matrix with zero diagonal must have the whole row/column zero. Do not say “all pivots nonnegative” naively without explaining the zero-row rule.
5. **Cauchy inequality is not optional.** It is the proof engine for zero diagonal rows and for PSD preservation under diagonal cross-filling remainders.
6. **End at criteria and method.** Avoid turning the lecture into advanced optimization/statistics; this is the final linear-algebra classification lecture.
