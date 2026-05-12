# Slide Plan: Exponential Functions (Lecture 18)

**Lecture:** 18  
**Placement:** After Lecture 17 (Complex Numbers)  
**Prerequisites students already have:** complex numbers $\mathbb{C}$, polar form $|z|e^{i\theta}$, conjugate pairs for real polynomials, eigenvalues (possibly complex), spectral decomposition $A = \sum \lambda_i P_i$, value tables, spectral formula $g(A) = \sum g(\lambda_i) P_i$

---

## The Philosophical Thread

The exponential function is **one idea appearing in four disguises**:

1. **Compound interest** — repeated tiny multiplicative nudges converge: $(1+x/n)^n \to e^x$
2. **Differential equations** — the function whose rate of change equals itself: $y' = y \implies y = e^t$
3. **Rotation on the circle** — tiny imaginary nudges produce rotation: $e^{i\theta} = \cos\theta + i\sin\theta$
4. **Taylor expansion is the binomial theorem** — the exponential of $d/dx$ is a shift, and its power series IS Taylor's formula

All four are the **same limit** $(1 + \text{something}/n)^n$, just with different "somethings": a real number, a matrix, a complex number, a differential operator.

---

## §1 — Definition: What Is $e$? (Compound Interest)

**Tension:** "If a bank gives 100% interest, compounded more and more often — do you get infinite money?"

| Frame | Content |
|-------|---------|
| 1 | Setup: deposit \$1, bank pays 100% annual interest |
| 2 | Compound once: $1 \times (1+1) = 2$ |
| 3 | Compound twice: $1 \times (1+\frac{1}{2})^2 = 2.25$ |
| 4 | Table: $n = 1, 2, 4, 10, 100, 1000$ — values converge to $2.718\ldots$ |
| 5 | **Reveal:** It converges to a number we call $e$. No infinite money. |
| 6 | General rate $x$: $(1+x/n)^n \to e^x$ — this IS the definition of the exponential function |

**Key insight frame:** "Compounding infinitely often doesn't blow up — it converges. This limit IS the exponential."

---

## §2 — The Binomial Expansion: From Limit to Power Series

**Tension:** "Can we compute $e^x$ without taking a limit every time?"

| Frame | Content |
|-------|---------|
| 1 | Recall binomial expansion: $(1+x)^n = 1 + \frac{n}{1!}x + \frac{n(n-1)}{2!}x^2 + \frac{n(n-1)(n-2)}{3!}x^3 + \cdots$ |
| 2 | Think of $e^x = (1+\frac{x}{\infty})^\infty$. Apply binomial expansion with $x \mapsto x/n$, $n \to \infty$ |
| 3 | Each coefficient: $\frac{n(n-1)\cdots(n-k+1)}{n^k} \to 1$ as $n \to \infty$ |
| 4 | **Result (boxed):** $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$ — the exponential power series |
| 5 | This is not magic — it is literally the binomial theorem applied to the limit definition |

**Key insight frame:** "The power series for $e^x$ is just the binomial expansion of $(1+x/n)^n$ when $n = \infty$."

---

## §3 — Exponential Solves $y' = ky$ (Differential Equations)

**Tension:** "If your speed equals your position — where do you end up?"

| Frame | Content |
|-------|---------|
| 1 | Setup: $y' = 2y$. Speed is twice your current value. At time $0$: $y(0) = 1$ |
| 2 | Tiny time step $\Delta t = 1/n$: $y(1/n) \approx y(0) + \frac{1}{n} \cdot 2y(0) = y(0)(1 + 2/n)$ |
| 3 | Next step: $y(2/n) \approx y(1/n)(1+2/n) = y(0)(1+2/n)^2$ |
| 4 | After $n$ steps (at time $t=1$): $y(1) = y(0)(1+2/n)^n$ |
| 5 | **Reveal:** As $n \to \infty$: $y(1) = y(0) \cdot e^2$ |
| 6 | General time $s$: need $ns$ steps $\to$ $y(s) = y(0)(1+2/n)^{ns} \to y(0)e^{2s}$ |

**Key insight frame:** "The exponential IS the solution to $y' = ky$. Rate proportional to value $\implies$ exponential growth."

---

## §4 — Complex Exponential & Euler's Formula

**Tension:** "What does $e^{i\theta}$ even mean? We defined $e^x$ as a limit — does it work for complex numbers?"

### 4a: The Limit Definition Still Works (3 frames)

| Frame | Content |
|-------|---------|
| 1 | Apply the same limit: $e^{i\theta} = \lim_{n\to\infty}(1 + \frac{i\theta}{n})^n$ |
| 2 | Each factor $(1 + i\theta/n)$ is a complex number: modulus $\approx 1$ (no stretching), argument $\approx \theta/n$ (tiny rotation). So each multiplication is a tiny rotation by $\theta/n$ |
| 3 | **TikZ:** Unit circle. Show $n$ tiny rotation steps from $1$ to $e^{i\theta}$. For $n=4$: a polygon inscribed in the circle. For $n=16$: smooth arc. The limit traces the circle. |

### 4b: Euler's Formula from the Power Series (3 frames)

| Frame | Content |
|-------|---------|
| 4 | Substitute $x = i\theta$ into the power series: $e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \cdots$ |
| 5 | Separate real and imaginary parts using $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, $\ldots$: Real part: $1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots = \cos\theta$. Imaginary part: $\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots = \sin\theta$ |
| 6 | **Euler's formula (boxed):** $e^{i\theta} = \cos\theta + i\sin\theta$ — the exponential function encompasses all of trigonometry. Rotation IS exponentiation of imaginary numbers. |

### 4c: Geometric Meaning (2 frames)

| Frame | Content |
|-------|---------|
| 7 | **TikZ:** The unit circle with angle $\theta$, showing $e^{i\theta}$ as the point $(\cos\theta, \sin\theta)$. Special cases: $e^{i\pi} = -1$, $e^{i\pi/2} = i$, $e^{2\pi i} = 1$ |
| 8 | General complex exponential: $e^{a+bi} = e^a \cdot e^{bi} = e^a(\cos b + i\sin b)$. Real part controls growth/decay, imaginary part controls rotation. |

**Key insight frame:** "$e^{i\theta}$ = rotation by $\theta$. The exponential function unifies growth AND rotation."

---

## §5 — Exponential of $d/dx$ IS Taylor's Theorem (The Shift Operator)

**Tension:** "What if we put a derivative operator into the exponential? Does $(1 + \frac{1}{n}\frac{d}{dx})^n$ make sense?"

This is the philosophical core — **the exponential of the derivative is a shift**, and this fact IS Taylor's theorem.

| Frame | Content |
|-------|---------|
| 1 | Define: $\exp(\frac{d}{dx}) = \lim_{n\to\infty}(I + \frac{1}{n}\frac{d}{dx})^n$. Same limit, new object inside. |
| 2 | What does $(I + \frac{1}{n}\frac{d}{dx})$ do to a function? It maps $f(x) \mapsto f(x) + \frac{1}{n}f'(x)$ |
| 3 | **For a linear function** $f(x) = kx + b$: $f(x) + \frac{1}{n}f'(x) = kx + b + \frac{k}{n} = k(x + \frac{1}{n}) + b = f(x + \frac{1}{n})$. Shifting a line UP by $k/n$ is the same as shifting it LEFT by $1/n$. **TikZ:** Line $y = kx+b$ and its shift. |
| 4 | **For any smooth function:** On a tiny interval $(x, x+1/n)$, any smooth function looks approximately linear. So $f(x) + \frac{1}{n}f'(x) \approx f(x + 1/n)$. **TikZ:** Parabola with a tiny linear approximation segment. |
| 5 | Apply $n$ times: $f(x) \to f(x+1/n) \to f(x+2/n) \to \cdots \to f(x+1)$ |
| 6 | **Reveal (boxed):** $\exp(\frac{d}{dx})[f](x) = f(x+1)$ — the exponential of the derivative operator IS the shift-by-one operator! |
| 7 | Now use the binomial/power series: $e^{d/dx} = I + \frac{d}{dx} + \frac{1}{2!}\frac{d^2}{dx^2} + \frac{1}{3!}\frac{d^3}{dx^3} + \cdots$ |
| 8 | Apply to $f$: $f(x+1) = f(x) + f'(x) + \frac{f''(x)}{2!} + \frac{f'''(x)}{3!} + \cdots$ — **This IS Taylor expansion!** |
| 9 | General shift: $\exp(s\frac{d}{dx})[f](x) = f(x+s)$. Taylor's theorem for arbitrary $s$: $f(x+s) = f(x) + sf'(x) + \frac{s^2}{2!}f''(x) + \cdots$ |

**Key insight frame:** "Taylor's theorem is nothing but the binomial expansion applied to the derivative operator. The derivative is an infinitesimal shift; exponentiating it gives a finite shift."

**Exercise:** Deduce the formula for $f(x+s)$ for general $s$ using $\exp(s \cdot d/dx)$.

---

## §6 — Matrix Exponential: Systems of Differential Equations

**Tension:** "What if speed depends on TWO quantities at once? Each component's rate depends on ALL components."

### 6a: The Problem (2 frames)

| Frame | Content |
|-------|---------|
| 1 | Vector differential equation: $\mathbf{y}' = A\mathbf{y}$, where $A = \begin{pmatrix}0 & -1 \\ 2 & 3\end{pmatrix}$. Written out: $y_1' = -y_2$, $y_2' = 2y_1 + 3y_2$. The speeds are coupled — you can't solve them separately. |
| 2 | But the same discrete-step trick works! Tiny step: $\mathbf{y}(1/n) \approx (I + \frac{A}{n})\mathbf{y}(0)$ |

### 6b: Definition of Matrix Exponential (3 frames)

| Frame | Content |
|-------|---------|
| 3 | After $n$ steps: $\mathbf{y}(1) \approx (I + \frac{A}{n})^n \mathbf{y}(0)$ |
| 4 | **Definition (boxed):** $e^A := \lim_{n\to\infty}(I + \frac{A}{n})^n$ — same idea, replace number with matrix, $1$ with $I$ |
| 5 | Solution: $\mathbf{y}(s) = e^{As}\mathbf{y}(0)$. The matrix exponential solves the system. |

### 6c: Computing $e^{As}$ via the Spectral Formula (THE PAYOFF) (5 frames)

This is where ALL of Lectures 14–17 come together.

| Frame | Content |
|-------|---------|
| 6 | **The key move.** $(I + A/n)^{ns}$ is a polynomial in $A$. By the spectral formula: $(I+\frac{A}{n})^{ns} = (1+\frac{\lambda_1}{n})^{ns} P_1 + (1+\frac{\lambda_2}{n})^{ns} P_2$ |
| 7 | As $n \to \infty$: each $(1+\lambda_i/n)^{ns} \to e^{\lambda_i s}$ |
| 8 | **Result (boxed):** $e^{As} = e^{\lambda_1 s} P_1 + e^{\lambda_2 s} P_2$ — the spectral formula extends to the exponential! |
| 9 | **Concrete calculation:** $A = \begin{pmatrix}0&-1\\2&3\end{pmatrix}$, eigenvalues $1, 2$. Projections: $P_1 = \frac{A-2I}{1-2} = \begin{pmatrix}2&1\\-2&-1\end{pmatrix}$, $P_2 = \frac{A-I}{2-1} = \begin{pmatrix}-1&-1\\2&2\end{pmatrix}$ |
| 10 | $e^{As} = e^s\begin{pmatrix}2&1\\-2&-1\end{pmatrix} + e^{2s}\begin{pmatrix}-1&-1\\2&2\end{pmatrix}$. Solution: $\mathbf{y}(s) = e^{As}\mathbf{y}(0)$. Write out the full answer component-wise. |

### 6d: Geometric Understanding via Eigenspaces (3 frames)

| Frame | Content |
|-------|---------|
| 11 | Decompose initial condition: $\mathbf{y}(0) = P_1\mathbf{y}(0) + P_2\mathbf{y}(0) = \mathbf{w}(0) + \mathbf{u}(0)$ |
| 12 | Each piece evolves independently: $\mathbf{w}'= A\mathbf{w} = 1\cdot\mathbf{w} \implies \mathbf{w}(s) = e^s\mathbf{w}(0)$. $\mathbf{u}' = A\mathbf{u} = 2\cdot\mathbf{u} \implies \mathbf{u}(s) = e^{2s}\mathbf{u}(0)$ |
| 13 | **Total:** $\mathbf{y}(s) = e^s\mathbf{w}(0) + e^{2s}\mathbf{u}(0)$. Each eigenspace component grows at its own rate. The faster eigenvalue dominates. |

---

## §7 — Complex Eigenvalues: Rotation in Differential Equations

**Tension:** "What if eigenvalues are complex? From Lecture 17, we know they exist. Does the formula still work?"

| Frame | Content |
|-------|---------|
| 1 | The rotation generator: $R = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$. From L17: eigenvalues $\lambda = \pm i$. |
| 2 | Apply the spectral formula: $e^{R\theta} = e^{i\theta}P_1 + e^{-i\theta}P_2$ |
| 3 | Compute projections and simplify (using $e^{i\theta} = \cos\theta + i\sin\theta$ and $e^{-i\theta} = \cos\theta - i\sin\theta$): $e^{R\theta} = \begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$ — the rotation matrix! |
| 4 | **Key insight (boxed):** The matrix exponential of a 90° rotation generator gives rotation by ANY angle $\theta$. Complex eigenvalues in $\mathbf{y}' = A\mathbf{y}$ produce **oscillation/rotation**, not just growth/decay. |
| 5 | General case: eigenvalues $a \pm bi$ give $e^{as}$(oscillation at frequency $b$) — exponential growth/decay modulated by rotation. |

---

## Summary & The Unified Picture

| Frame | Content |
|-------|---------|
| 1 | **The one definition:** $e^X = \lim_{n\to\infty}(1 + X/n)^n$, where $X$ can be a number, a complex number, a matrix, or a differential operator |
| 2 | **Four manifestations:** (a) $X = x \in \mathbb{R}$: growth/decay. (b) $X = i\theta$: rotation (Euler). (c) $X = A$ (matrix): system of ODEs, computed via spectral formula. (d) $X = d/dx$: shift operator (Taylor's theorem) |
| 3 | **The single philosophy:** Repeated tiny nudges compound into a smooth transformation. The binomial expansion of the limit gives the power series. Everything is one idea. |

---

## Section Summary

| Section | Frames (est.) | Phase | Role |
|---------|--------------|-------|------|
| §1 Compound interest → $e$ | 6 | Concretization | Ground the limit in money/growth |
| §2 Binomial → power series | 5 | Bridge | From limit to computable formula |
| §3 $y' = ky$ | 6 | Application | Dynamic process — exponential IS the solution |
| §4 Complex exponential & Euler | 8 | Extension | Imaginary exponent = rotation |
| §5 Shift operator / Taylor | 9 | **Philosophical core** | $\exp(d/dx) = $ shift; Taylor IS binomial expansion |
| §6 Matrix exponential | 13 | **Main content** | Spectral formula payoff — solve $\mathbf{y}' = A\mathbf{y}$ |
| §7 Complex eigenvalues & rotation | 5 | Extension | Oscillation from complex eigenvalues |
| Summary | 3 | Unification | One definition, four faces |
| **Total** | **~55** | | |

---

## Narrative Flow & Connections

```
§1 (limit definition) ──→ §2 (binomial → series) ──→ §3 (solves y'=ky)
                                    │                         │
                                    ▼                         ▼
                          §5 (exp of d/dx = shift)    §6 (matrix exp, spectral formula)
                          Taylor IS binomial                  │
                                    │                         ▼
                                    │              §7 (complex eigenvalues → rotation)
                                    │                         │
                                    ▼                         ▼
                          §4 (Euler's formula) ◄──── (complex exp = rotation)
                                    │
                                    ▼
                              Summary (unification)
```

---

## Design Decisions

1. **Ordering of §4 vs §5:** The Taylor/shift section (§5) is placed BEFORE the matrix section (§6) because the philosophy "exponential of derivative = shift" is the conceptual climax — it reframes Taylor expansion as nothing mysterious. §4 (Euler) comes between §3 and §5 because it uses the power series from §2 and prepares for §7.

2. **§5 is non-negotiable.** This is the "fucking philosophy" of the lecture — the exponential of the derivative is a shifting operator. Taylor expansion loses its mystery once you see it as the binomial expansion of $(I + \frac{1}{n}\frac{d}{dx})^n$.

3. **Frame count (~55):** Substantial but manageable. If trimming is needed, §1 compound interest (6 frames) can be compressed to 3–4 since students likely know $e$ already. The savings go to §5 or §6.

4. **Where complex numbers enter:** §4 uses Euler's formula directly. §7 brings it back for matrices. The bridge from L17 is: "L17 gave us complex eigenvalues; now we know what $e^{\lambda s}$ means when $\lambda \in \mathbb{C}$."

5. **Legacy source:** The `linearODE.tex` file covers §3, §5, and §6. The new plan reorganizes and extends it with §1 (compound interest concretization), §2 (explicit binomial bridge), §4 (Euler from power series), and §7 (complex eigenvalue example).

---

*Legacy files: `linearODE.tex` (main source for §3, §5, §6)*  
*Prerequisites: L17 (complex numbers), L14–L16 (spectral decomposition, value tables)*
