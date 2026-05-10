# Slide Plan: The Exponential Function & Matrix Exponential

**Lecture placement:** Week 14 (§5.5–5.6), after spectral decomposition  
**Prerequisites students already have:** eigenvalues, Lagrange interpolation, spectral decomposition $A = \sum \lambda_i P_i$, spectral formula $g(A) = \sum g(\lambda_i)P_i$

---

## The Core Idea

The exponential $e^x = \lim_{n\to\infty}\left(1+\frac{x}{n}\right)^n$ is fundamentally about **repeated tiny nudges**.

- Each factor $(1 + x/n)$ is a tiny multiplicative step
- Repeat $n$ times → compound effect
- This idea works **identically** for matrices: replace $x$ with $A$, replace $1$ with $I$

The slide should make students **feel** why the limit definition is natural before touching any formula.

---

## §1 — What Is $e$? (Compound Interest)

**Tension:** "If a bank gives you 100% interest, compounded more and more often — do you get infinite money?"

| Frame | Content |
|-------|---------|
| 1 | Setup: you deposit \$1, bank pays 100% annual interest |
| 2 | Compound once: $1 \times (1+1) = 2$ |
| 3 | Compound twice: $1 \times (1+\tfrac{1}{2})^2 = 2.25$ |
| 4 | Table: $n = 1,2,4,10,100,1000$ — values converge to $2.718\ldots$ |
| 5 | **Reveal:** No infinite money. It converges to a number we call $e$ |
| 6 | General rate $x$: $(1+x/n)^n \to e^x$ |

**Key insight frame:** "Compounding infinitely often doesn't blow up — it converges. This limit IS the exponential function."

### Binomial Expansion Detour (2–3 frames)

$$\left(1+\frac{x}{n}\right)^n = 1 + n\cdot\frac{x}{n} + \frac{n(n-1)}{2!}\cdot\frac{x^2}{n^2} + \cdots$$

As $n\to\infty$, each coefficient $\frac{n(n-1)\cdots}{n^k} \to 1$, giving the power series:

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

---

## §2 — Exponential Solves $y'=ky$ (Differential Equations)

**Tension:** "If your speed equals your position — where do you end up?"

| Frame | Content |
|-------|---------|
| 1 | Setup: $y' = 2y$. Speed is twice your distance. At time 0, $y(0) = 1$ |
| 2 | Tiny time step $\Delta t = 1/n$: speed $\approx 2y(0)$, so $y(1/n) \approx y(0) + \frac{1}{n}\cdot 2y(0) = y(0)(1+2/n)$ |
| 3 | Next step: $y(2/n) \approx y(1/n)(1+2/n) = y(0)(1+2/n)^2$ |
| 4 | After $n$ steps: $y(1) = y(0)(1+2/n)^n$ |
| 5 | **Reveal:** As $n\to\infty$: $y(1) = y(0)\cdot e^2$ |
| 6 | General time $s$: need $ns$ steps → $y(s) = y(0)(1+2/n)^{ns} \to y(0)e^{2s}$ |

**Key insight frame:** "The exponential function is what you get when the rate of change is proportional to the current value."

---

## §3 — Matrix Exponential: Systems of Equations

**Tension:** "What if speed depends on TWO quantities at once?"

### 3a: The Problem (2 frames)

Vector differential equation: $\mathbf{y}' = A\mathbf{y}$

$$\begin{pmatrix} y_1' \\ y_2' \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 2 & 3 \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix}$$

"Each component's speed depends on BOTH components. We can't solve them separately."

### 3b: Same Discrete Trick (3 frames)

| Frame | Content |
|-------|---------|
| 1 | Tiny step: $\mathbf{y}(1/n) \approx \mathbf{y}(0) + \frac{1}{n}A\mathbf{y}(0) = \left(I + \frac{A}{n}\right)\mathbf{y}(0)$ |
| 2 | After $n$ steps: $\mathbf{y}(1) \approx \left(I + \frac{A}{n}\right)^n \mathbf{y}(0)$ |
| 3 | **Definition:** $e^{A} := \lim_{n\to\infty}\left(I + \frac{A}{n}\right)^n$ — same idea, matrix version |

### 3c: Computing $e^{As}$ via Spectral Formula (4–5 frames)

This is **the payoff of all Week 12–13 work**.

Students already know: if $A$ has eigenvalues $\lambda_1, \lambda_2$ with projections $P_1, P_2$, then $g(A) = g(\lambda_1)P_1 + g(\lambda_2)P_2$ for any polynomial $g$.

**Key move:** The limit $(I + A/n)^{ns}$ is a polynomial in $A$ at each finite $n$. So:

$$\left(I + \frac{A}{n}\right)^{ns} = \left(1+\frac{\lambda_1}{n}\right)^{ns} P_1 + \left(1+\frac{\lambda_2}{n}\right)^{ns} P_2$$

As $n\to\infty$:

$$\boxed{e^{As} = e^{\lambda_1 s}\, P_1 + e^{\lambda_2 s}\, P_2}$$

### 3d: Concrete Calculation (3–4 frames)

Use $A = \begin{pmatrix} 0 & -1 \\ 2 & 3 \end{pmatrix}$, eigenvalues $\lambda_1=1, \lambda_2=2$.

$$P_1 = \frac{A-2I}{1-2} = \begin{pmatrix} 2 & 1 \\ -2 & -1 \end{pmatrix}, \quad P_2 = \frac{A-I}{2-1} = \begin{pmatrix} -1 & -1 \\ 2 & 2 \end{pmatrix}$$

$$e^{As} = e^s \begin{pmatrix} 2 & 1 \\ -2 & -1 \end{pmatrix} + e^{2s}\begin{pmatrix} -1 & -1 \\ 2 & 2 \end{pmatrix}$$

Solution: $\mathbf{y}(s) = e^{As}\,\mathbf{y}(0)$. Write out the full answer.

---

## §4 — Complex Eigenvalues & Euler's Formula

**Tension:** "What if the eigenvalues are complex numbers? Does $e^{i\theta}$ even make sense?"

### 4a: The Limit Definition Still Works (3 frames)

$$e^{i\theta} = \lim_{n\to\infty}\left(1 + \frac{i\theta}{n}\right)^n$$

Each factor $(1 + i\theta/n)$ is a complex number with:
- Real part $\approx 1$ (almost no stretching)
- Imaginary part $\theta/n$ (tiny rotation by angle $\approx \theta/n$)

**TikZ diagram:** Unit circle in complex plane. Show $n$ tiny rotation steps from $1$ to $e^{i\theta}$.

- $n = 4$: four visible rotation steps (polygon inscribed in circle)
- $n = 16$: smooth arc

### 4b: Euler's Formula (2 frames)

$$e^{i\theta} = \cos\theta + i\sin\theta$$

This is just the power series:
$$e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \cdots = \underbrace{\left(1 - \frac{\theta^2}{2!} + \cdots\right)}_{\cos\theta} + i\underbrace{\left(\theta - \frac{\theta^3}{3!} + \cdots\right)}_{\sin\theta}$$

### 4c: Rotation Matrix Example (3–4 frames)

The matrix $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has eigenvalues $\lambda = \pm i$.

$$e^{R\theta} = e^{i\theta}P_1 + e^{-i\theta}P_2$$

After computing projections and simplifying:

$$e^{R\theta} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

**Key insight frame:** "The matrix exponential of a 90° rotation generator gives rotation by any angle $\theta$. Complex eigenvalues = rotation."

---

## §5 — Exponential of $d/dx$ IS Taylor's Theorem (Bonus / If Time Permits)

**Tension:** "What if the 'matrix' is a derivative operator?"

| Frame | Content |
|-------|---------|
| 1 | Define: $\exp\!\left(\frac{d}{dx}\right) = \lim_{n\to\infty}\left(I + \frac{1}{n}\frac{d}{dx}\right)^n$ |
| 2 | What does $\left(I + \frac{1}{n}\frac{d}{dx}\right)$ do? Maps $f(x) \mapsto f(x) + \frac{1}{n}f'(x)$ |
| 3 | For a line $f(x)=kx+b$: shifting up by $k/n$ = shifting left by $1/n$. **TikZ diagram** |
| 4 | Any smooth function looks like a line on a tiny interval → $f(x)+\frac{1}{n}f'(x) \approx f(x+1/n)$ |
| 5 | Apply $n$ times: $f(x) \to f(x+1/n) \to f(x+2/n) \to \cdots \to f(x+1)$ |
| 6 | **Reveal:** $\exp\!\left(\frac{d}{dx}\right)f(x) = f(x+1)$ |
| 7 | Power series version: $f(x) + f'(x) + \frac{f''(x)}{2!} + \cdots = f(x+1)$ — this IS Taylor expansion! |

**Key insight frame:** "Taylor's theorem is nothing more than the binomial expansion applied to the derivative operator."

---

## Summary of Sections

| Section | Frames (est.) | Phase | Role |
|---------|--------------|-------|------|
| §1 Compound Interest → $e^x$ | 8–9 | Concretization | Ground the limit in money/growth |
| §2 $y'=ky$ | 6–7 | Bridge | From static formula to dynamic process |
| §3 Matrix Exponential | 12–14 | Formalization | Main content — spectral formula payoff |
| §4 Complex / Euler | 8–10 | Extension | Complex eigenvalues = rotation |
| §5 Shift Operator | 7–8 | Bonus | Taylor = exponential of $d/dx$ |
| **Total** | **~42–48** | | |

---

## Design Decisions to Discuss

1. **§1 Compound interest** — is this too elementary for POSTECH students? Or is the concretization needed because the limit definition feels abstract?

2. **§4 Complex eigenvalues** — how much complex number background do students need here? The syllabus says complex numbers are introduced in Week 13. Should this section assume fluency or re-ground the basics?

3. **§5 Differential operator** — the legacy `linearODE.tex` includes this. It's beautiful but might be too much for one lecture. Should we keep it as a bonus section or cut it?

4. **Emoji mapping** — the exponential story is more about "growth/rotation" than "ingredients." Possible emoji anchors:
   - 💰→💰💰 for compound interest (money doubling)
   - 🔄 for rotation (complex exponential)
   - Or skip emoji entirely — the concretization here is already visual (graphs, unit circle) rather than tabular

5. **Frame count** — 42–48 frames is substantial. Should we split into two lectures (exponential + complex/rotation)?

---

*Questions? Call me back:* {{SHELL_PREFIX}}ell
