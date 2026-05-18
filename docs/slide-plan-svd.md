# Slide Plan: Singular Value Decomposition — Revised

**Placement:** After normal matrices and the specialization back to real symmetric matrices.  
**Correct emphasis:** This is a real applied/statistics lecture. The main route should be real matrices, real inner products, real symmetric matrices, and orthogonal diagonalization. Complex/Hermitian language is only background, not the visible story.

The lecture should begin from statistics:

> A random vector has a round normal distribution. After a linear transformation, what shape does the distribution become?

Equivalent geometric question:

> A matrix maps the unit ball to some stretched shape. What are the axes and axis lengths of that shape?

That question is singular value decomposition.

---

## 0. Corrected Thesis

SVD is not primarily “a rectangular version of unitary diagonalization” for these slides. That language is mathematically true over $\mathbb C$, but it is the wrong entrance.

For this applied linear algebra course, the correct story is:

$$
\boxed{
\text{normal distribution / round ball}
\xrightarrow{\ A\ }
\text{ellipse / ellipsoid}
}
$$

The axes of this ellipsoid are found by ordinary real symmetric matrices:

$$
A^TA.
$$

Since $A^TA$ is real symmetric and positive semidefinite, the previous lecture’s real specialization applies:

$$
A^TA=V\Sigma^2V^T
$$

with $V$ orthogonal and $\Sigma^2$ diagonal with nonnegative entries.

Then:

$$
\boxed{A=U\Sigma V^T}
$$

where:

- $V$ gives orthonormal input axes;
- $\Sigma$ gives the lengths of the ellipsoid axes;
- $U$ gives orthonormal output axes;
- $\sigma_i$ are the singular values;
- small $\sigma_i$ means weak/noisy/statistically unstable direction;
- zero $\sigma_i$ means an invisible direction, i.e. null space.

**Main slogan:** SVD is the coordinate system of a linear transformation seen through balls, ellipses, and Gaussian clouds.

---

## 1. What Was Wrong in the Previous Plan

The previous draft overused Hermitian/unitary language. That loses the point of the previous normal-matrix lecture.

Lecture 19 ended by specializing complex theory back to real matrices:

- Hermitian geometry is the general machine.
- Real symmetric matrices are the real-world specialization.
- Real symmetric matrices can be orthogonally diagonalized over $\mathbb R$.
- For real applied problems, we should use $A^T$, orthogonal matrices, and real axes.

So the SVD lecture should visibly use:

$$
A^T,\qquad A^TA,\qquad V^TV=I,\qquad A=U\Sigma V^T.
$$

Only after the real story is clear should we mention:

> Over $\mathbb C$, replace transpose by Hermitian transpose: $A^H$, $V^H$.

That should be a short remark, not the main notation.

---

## 2. Statistical Origin

### Guiding Question

Suppose:

$$
x\sim N(0,I).
$$

That means the distribution is round: every direction has the same variance.

Now apply a real matrix:

$$
y=Ax.
$$

Question:

$$
\boxed{\text{What is the shape of }y?}
$$

The covariance transforms as:

$$
\operatorname{Cov}(y)
=\operatorname{Cov}(Ax)
=A\operatorname{Cov}(x)A^T
=AA^T.
$$

So a standard normal cloud becomes a Gaussian cloud whose principal axes are controlled by $AA^T$.

Equivalent ball picture:

$$
\|x\|\le 1
\quad\Longrightarrow\quad
Ax\text{ fills an ellipse/ellipsoid.}
$$

The axis directions are the left singular vectors $u_i$, and the axis lengths are the singular values $\sigma_i$.

This is the right motivation because students can see statistics, geometry, and linear algebra in the same picture.

---

## 3. Core Visual Pictures

### Picture A — Gaussian Cloud

```text
input space                         output space

 round Gaussian cloud       A        tilted ellipse Gaussian cloud
        ○○○○○             ---->              ◐◐◐◐◐
      ○○○○○○○                             ◐◐◐◐◐◐◐
        ○○○○○                               ◐◐◐◐◐

 all directions equal                long axis + short axis
```

Slide purpose: SVD answers “what are the axes of the transformed normal distribution?”

### Picture B — Unit Circle to Ellipse

```text
unit circle                          ellipse

        v2                                   u2
        ↑                                    ↗ short axis
    ○○○○○○○              A              ◐◐◐◐◐
  ○○○     ○○○          ---->         ◐◐       ◐◐
    ○○○○○○○                         ◐◐◐◐◐◐◐◐◐
        → v1                                  → u1 long axis
```

Slide purpose: $Av_i=\sigma_i u_i$ should be visible before it is algebra.

### Picture C — Weak Direction in Regression

```text
parameter direction                  data movement

 strong direction  ---------------------------> visible
 weak direction    --->                         nearly invisible
 zero direction    ·                            no movement
```

Slide purpose: small singular values explain unstable regression coefficients.

---

## 4. Prerequisites Already Built

Students already know the required tools:

1. **Linear regression:** solve $Ax\approx b$ by projecting $b$ onto $\operatorname{Col}(A)$.
2. **Orthogonal projections:** closest point = perpendicular projection.
3. **Four subspaces:** column space, null space, row space, left null space.
4. **Positive semidefinite matrices:** $x^TA^TAx=\|Ax\|^2\ge0$.
5. **Real symmetric spectral theorem:** real symmetric matrices have orthogonal diagonalization.
6. **Diagonal cross-filling:** orthogonal projections can be turned into orthonormal vectors.

The new move:

$$
\boxed{
\text{Even if }A\text{ is rectangular, }A^TA\text{ is square symmetric.}
}
$$

So we do not diagonalize $A$. We diagonalize the stretch-measuring matrix $A^TA$.

---

## 5. Main Narrative

### §1 — Statistics First: What Happens to a Normal Cloud?

**Tension:** “A standard normal distribution is round. What does a matrix do to it?”

| Frame | Content |
|---|---|
| 1 | Draw a round Gaussian cloud in $\mathbb R^2$. |
| 2 | Apply a matrix $A$; draw an ellipse-shaped Gaussian cloud. |
| 3 | Ask: what are the long and short axes? |
| 4 | State covariance rule: if $y=Ax$, then $\operatorname{Cov}(y)=A\operatorname{Cov}(x)A^T$. |
| 5 | For $x\sim N(0,I)$, get $\operatorname{Cov}(y)=AA^T$. |
| 6 | Key: axes of the transformed Gaussian come from a symmetric matrix. |

This section should avoid all complex/unitary notation.

---

### §2 — Same Question Without Probability: Ball to Ellipsoid

**Tension:** “If probability is too much, just look at the unit ball.”

| Frame | Content |
|---|---|
| 1 | Draw the unit circle/ball: all input directions have length $1$. |
| 2 | Apply $A$; the image becomes an ellipse/ellipsoid. |
| 3 | Mark the long axis and short axis. |
| 4 | Define singular values visually: half-axis lengths of $A(B_1)$. |
| 5 | Mark input directions $v_i$ that map to axes. |
| 6 | Mark output directions $u_i$ along axes. |
| 7 | Reveal the geometric equation: $Av_i=\sigma_i u_i$. |

The first definition should be geometric:

$$
\boxed{\sigma_i=\text{axis length of the ellipsoid }A(B_1).}
$$

Only after this do we say these numbers can be computed from $A^TA$.

---

### §3 — Why $A^TA$ Finds the Input Axes

**Tension:** “How can a rectangular matrix have axes?”

For any input vector $x$:

$$
\|Ax\|^2=x^TA^TAx.
$$

So $A^TA$ measures output length from the input side.

| Frame | Content |
|---|---|
| 1 | Start with the question: which unit vector $x$ makes $\|Ax\|$ large? |
| 2 | Compute $\|Ax\|^2=x^TA^TAx$. |
| 3 | Define $G=A^TA$ as the stretch-measuring matrix. |
| 4 | Show $G^T=G$: it is real symmetric. |
| 5 | Show $x^TGx=\|Ax\|^2\ge0$: it is positive semidefinite. |
| 6 | Apply real symmetric orthogonal diagonalization: $G=V\Sigma^2V^T$. |
| 7 | Interpret $v_i$: orthonormal input axes. |

This is the critical correction:

$$
\boxed{
A^TA\text{ is real symmetric, so real orthogonal diagonalization applies.}
}
$$

No unitary language is needed here.

---

### §4 — Singular Values from Eigenvalues

**Tension:** “Why are singular values square roots?”

Let:

$$
A^TA v_i=\lambda_i v_i,\qquad \|v_i\|=1.
$$

Then:

$$
\|Av_i\|^2
=v_i^TA^TAv_i
=\lambda_i v_i^Tv_i
=\lambda_i.
$$

Since a squared length is nonnegative:

$$
\lambda_i\ge0.
$$

Define:

$$
\boxed{\sigma_i=\sqrt{\lambda_i}.}
$$

Frame sequence:

| Frame | Content |
|---|---|
| 1 | Eigen-equation for $A^TA$: $A^TA v_i=\lambda_i v_i$. |
| 2 | Compute output length: $\|Av_i\|^2=\lambda_i$. |
| 3 | Since length squared cannot be negative, $\lambda_i\ge0$. |
| 4 | Define $\sigma_i=\sqrt{\lambda_i}$. |
| 5 | Therefore $Av_i$ has length $\sigma_i$. |
| 6 | Visual callback: these are exactly the ellipse axis lengths. |

---

### §5 — Output Axes

**Tension:** “The input axis $v_i$ is known. Where does it land?”

For $\sigma_i>0$, define:

$$
\boxed{u_i=\frac{Av_i}{\sigma_i}.}
$$

Then:

$$
Av_i=\sigma_i u_i.
$$

Prove the $u_i$ are orthonormal using real inner products:

$$
u_i^Tu_j
=\frac{(Av_i)^T(Av_j)}{\sigma_i\sigma_j}
=\frac{v_i^TA^TAv_j}{\sigma_i\sigma_j}
=\frac{\sigma_j^2}{\sigma_i\sigma_j}v_i^Tv_j.
$$

So:

- if $i=j$, $u_i^Tu_i=1$;
- if $i\ne j$, $u_i^Tu_j=0$.

Slide requirement: show this as an inner-product table, matching the diagonal cross-filling style from previous lectures.

---

### §6 — Stack the Axis Equations

**Tension:** “If we know all axis equations, can we rebuild the matrix?”

Start with:

$$
Av_1=\sigma_1u_1,\quad
Av_2=\sigma_2u_2,\quad\cdots
$$

Stack columns:

$$
A
\underbrace{
\begin{pmatrix}
|&|&&|\\
v_1&v_2&\cdots&v_n\\
|&|&&|
\end{pmatrix}
}_{V}
=
\underbrace{
\begin{pmatrix}
|&|&&|\\
u_1&u_2&\cdots&u_m\\
|&|&&|
\end{pmatrix}
}_{U}
\underbrace{\Sigma}_{\text{axis lengths}}.
$$

Since $V$ is orthogonal:

$$
V^T=V^{-1}.
$$

Therefore:

$$
\boxed{A=U\Sigma V^T.}
$$

Every slide should use the real notation $V^T$, not $V^H$, unless explicitly making the complex remark.

---

### §7 — Zero Singular Values and Invisible Directions

**Tension:** “What if an axis length is zero?”

If $\sigma_i=0$, then $\lambda_i=0$ and:

$$
\|Av_i\|^2=v_i^TA^TAv_i=0.
$$

Thus:

$$
Av_i=0.
$$

So $v_i\in\operatorname{Null}(A)$.

Frame sequence:

| Frame | Content |
|---|---|
| 1 | Show a flattened ellipse: one axis has length $0$. |
| 2 | Algebra: $\sigma_i=0\Rightarrow \|Av_i\|=0$. |
| 3 | Therefore $Av_i=0$. |
| 4 | Null-space interpretation: $v_i$ is invisible to the data. |
| 5 | Four-subspace picture: input splits into visible row-space directions and invisible null-space directions. |
| 6 | Output space splits into column space and left null space. |

Real orthogonal decompositions:

$$
\mathbb R^n=\operatorname{Row}(A)\overset{\perp}{\oplus}\operatorname{Null}(A),
$$

$$
\mathbb R^m=\operatorname{Col}(A)\overset{\perp}{\oplus}\operatorname{Null}(A^T).
$$

---

### §8 — The SVD Theorem

**Reveal:** Every real matrix maps balls to ellipsoids with orthogonal axes.

Theorem:

> For every real $m\times n$ matrix $A$, there exist real orthogonal matrices $U,V$ and a rectangular diagonal matrix $\Sigma$ with nonnegative entries such that
>
> $$
> A=U\Sigma V^T.
> $$

Proof architecture:

1. Form $G=A^TA$.
2. $G$ is real symmetric positive semidefinite.
3. Orthogonally diagonalize $G$:
   $$
   A^TA=V\Sigma^2V^T.
   $$
4. For $\sigma_i>0$, define $u_i=Av_i/\sigma_i$.
5. Prove $u_i$ are orthonormal.
6. Complete the $u_i$ to an orthonormal basis of $\mathbb R^m$.
7. Stack $Av_i=\sigma_i u_i$.
8. Get $AV=U\Sigma$ and hence $A=U\Sigma V^T$.

Complex remark, one slide only:

> Over $\mathbb C$, replace $T$ by $H$ and “orthogonal” by “unitary.” The real applied story is the one we use today.

---

### §9 — Worked Example: Circle to Ellipse

Use a $2\times2$ real matrix where the ellipse picture is clear, for example:

$$
A=\begin{pmatrix}2&1\\0&1\end{pmatrix}.
$$

Frame sequence:

| Frame | Content |
|---|---|
| 1 | Draw the unit circle and its image ellipse. |
| 2 | Compute $A^TA$. |
| 3 | Compute $\det(tI-A^TA)$ honestly. |
| 4 | Orthogonally diagonalize $A^TA$: find $v_1,v_2$. |
| 5 | Singular values are square roots of eigenvalues. |
| 6 | Compute $u_i=Av_i/\sigma_i$. |
| 7 | Stack $U,\Sigma,V^T$. |
| 8 | Verify $Av_i=\sigma_i u_i$ by colored columns. |

Need colored visual consistency:

- $v_1,u_1,\sigma_1$: blue long axis.
- $v_2,u_2,\sigma_2$: red short axis.
- use underbraces for $U,\Sigma,V^T$.

---

### §10 — Worked Example: Rectangular Regression Matrix

Use a matrix with nearly dependent columns:

$$
A=\begin{pmatrix}
1&1\\
1&1.1\\
1&0.9
\end{pmatrix}.
$$

This matrix is rectangular because statistics often has:

$$
\text{few parameters} \longrightarrow \text{many measurements}.
$$

Here two parameter directions matter:

$$
v_{\text{strong}}\approx \frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},
\qquad
v_{\text{weak}}\approx \frac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}.
$$

Frame sequence:

| Frame | Content |
|---|---|
| 1 | Explain rows = measurements, columns = model features. |
| 2 | Compute $A(1,1)^T$: large data movement. |
| 3 | Compute $A(1,-1)^T$: small data movement. |
| 4 | Compute $A^TA$. |
| 5 | Diagonalize $A^TA$ and read singular values. |
| 6 | Interpret strong/weak directions statistically. |
| 7 | Connect small singular value to unstable coefficient estimates. |

This is where “rectangle” becomes natural:

> In data fitting, the number of observations and the number of parameters are usually different. That is why rectangular matrices appear.

But the deeper motivation is still the transformed normal cloud / ellipsoid.

---

### §11 — Least Squares Becomes Diagonal

**Tension:** “Why does SVD matter for regression computation?”

Least squares:

$$
\min_x\|Ax-b\|^2.
$$

Insert real SVD:

$$
A=U\Sigma V^T.
$$

Because $U,V$ preserve lengths, set:

$$
y=V^Tx,\qquad c=U^Tb.
$$

Then:

$$
\|Ax-b\|^2
=\|U\Sigma V^Tx-b\|^2
=\|\Sigma y-c\|^2.
$$

Now each coordinate is independent:

$$
\min_y\sum_i(\sigma_i y_i-c_i)^2.
$$

So:

$$
y_i=\frac{c_i}{\sigma_i}
\quad(\sigma_i>0).
$$

This gives the pseudoinverse:

$$
A^+=V\Sigma^+U^T.
$$

Statistical meaning:

- large $\sigma_i$: stable direction;
- small $\sigma_i$: noise amplification;
- zero $\sigma_i$: unidentifiable parameter direction.

---

### §12 — PCA and Covariance

**Tension:** “Where do principal components come from?”

For centered data matrix $X$:

$$
\frac1N X^TX
$$

is the sample covariance matrix of features.

If:

$$
X=U\Sigma V^T,
$$

then:

$$
X^TX=V\Sigma^2V^T.
$$

Therefore:

- columns of $V$ are principal feature directions;
- $\sigma_i^2$ measure variance strengths;
- keeping large $\sigma_i$ gives dimensional reduction.

This should be a short application preview, not a full PCA lecture.

---

## 6. Frame Budget

| Section | Frames | Purpose |
|---|---:|---|
| §1 Normal cloud | 6 | Statistical motivation |
| §2 Ball to ellipsoid | 7 | Geometric intuition |
| §3 Why $A^TA$ | 7 | Real symmetric bridge |
| §4 Singular values | 6 | Square-root eigenvalue meaning |
| §5 Output axes | 6 | Construct $u_i$ |
| §6 Stack equations | 5 | Derive $A=U\Sigma V^T$ |
| §7 Zero singular values | 6 | Null-space meaning |
| §8 SVD theorem | 8 | Complete proof |
| §9 Circle example | 8 | Visual computation |
| §10 Regression example | 7 | Rectangular/statistics meaning |
| §11 Least squares | 7 | Diagonal regression |
| §12 PCA preview | 5 | Broader statistics background |

Total: about **78 frames**. This is two modules if done carefully:

- **Module A:** geometry and theorem (§1–§9).
- **Module B:** statistics applications (§10–§12).

If one lecture only, keep §12 as a final preview and compress §9/§10 to one example.

---

## 7. Claims That Must Be Proved

The slides should prove:

1. If $x\sim N(0,I)$ and $y=Ax$, then $\operatorname{Cov}(y)=AA^T$.
2. $A^TA$ is real symmetric.
3. $A^TA$ is positive semidefinite.
4. Real symmetric spectral theorem applies to $A^TA$.
5. Eigenvalues of $A^TA$ are nonnegative.
6. If $A^TA v_i=\sigma_i^2v_i$, then $\|Av_i\|=\sigma_i$.
7. If $\sigma_i>0$, $u_i=Av_i/\sigma_i$ has norm $1$.
8. The $u_i$ are mutually orthogonal.
9. If $\sigma_i=0$, then $Av_i=0$.
10. Stacking $Av_i=\sigma_i u_i$ gives $AV=U\Sigma$.
11. Since $V$ is orthogonal, $A=U\Sigma V^T$.
12. Least squares reduces to $\min_y\|\Sigma y-c\|^2$.
13. Small singular values amplify noise by division.

---

## 8. Visual and Notation Requirements

- Use real notation in the main lecture: $A^T$, $U^T$, $V^T$.
- Use $A=U\Sigma V^T$ as the main formula.
- Mention $A=U\Sigma V^H$ only in a short complex-version remark.
- Do not foreground unitary matrices.
- Draw Gaussian cloud and unit circle before formal theorem.
- Draw ellipse axes and label $u_i,\sigma_i,v_i$.
- Use color-persistent axes:
  - blue = long/strong direction;
  - red = short/weak direction;
  - gray = zero/invisible direction;
  - orange = noise.
- Use an inner-product table to show $u_i^Tu_j=\delta_{ij}$.
- Use underbraces:
  $$
  A=
  \underbrace{U}_{\text{output axes}}
  \underbrace{\Sigma}_{\text{axis lengths}}
  \underbrace{V^T}_{\text{input coordinates}}.
  $$
- Use rectangular $\Sigma$ when $A$ is rectangular.
- Write characteristic polynomials as $\det(tI-A)$, not $\chi_A(t)$.
- Use diagonal cross-filling style when stacking columns and verifying orthogonality.

---

## 9. Final Takeaway Slide

The final slide should say:

$$
\boxed{
\text{SVD is the axis system of }A\text{ acting on balls/Gaussians.}
}
$$

Then:

$$
A=U\Sigma V^T
$$

means:

```text
input vector
   ↓ measure in orthonormal input axes V
coordinates
   ↓ stretch by axis lengths Σ
ellipsoid coordinates
   ↓ rebuild in orthonormal output axes U
output vector
```

Statistics interpretation:

$$
\boxed{
\text{large }\sigma_i=\text{stable visible direction},
\qquad
\text{small }\sigma_i=\text{unstable noisy direction},
\qquad
\sigma_i=0=\text{invisible direction}.
}
$$

This connects normal distributions, ellipses, regression, pseudoinverse, PCA, and numerical stability.
