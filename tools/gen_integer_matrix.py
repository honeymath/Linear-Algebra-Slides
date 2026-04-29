#!/usr/bin/env python3
"""Generate integer matrices with prescribed integer eigenvalues via the LU trick.

The trick: L (lower triangular, 1s on diagonal) × U (upper triangular, 1s on diagonal)
gives P with det(P) = 1, so P^{-1} is also integer. Then A = P D P^{-1} has integer
entries and eigenvalues equal to the diagonal of D.

Usage:
    python3 gen_integer_matrix.py                      # interactive defaults
    python3 gen_integer_matrix.py --eigenvalues 1 3    # 2×2 with eigenvalues 1,3
    python3 gen_integer_matrix.py --eigenvalues 2 2 5 --L 0,0,2,0,1,1 --U 0,0,1,0,1,0
"""

import argparse
import sys
from sympy import Matrix, eye, zeros, Rational, simplify, factor, Symbol, Poly, prod


def build_LU(n, L_below=None, U_above=None):
    """Build L and U matrices from below-diagonal and above-diagonal entries.

    L_below: list of entries below diagonal, read left-to-right, top-to-bottom.
             For 3×3: [L21, L31, L32]. For 2×2: [L21].
    U_above: same for above diagonal.
             For 3×3: [U12, U13, U23]. For 2×2: [U12].
    """
    L = eye(n)
    U = eye(n)

    if L_below is None:
        L_below = [1] * (n * (n - 1) // 2)
    if U_above is None:
        U_above = [1] * (n * (n - 1) // 2)

    idx = 0
    for i in range(n):
        for j in range(i):
            L[i, j] = L_below[idx]
            idx += 1

    idx = 0
    for i in range(n):
        for j in range(i + 1, n):
            U[i, j] = U_above[idx]
            idx += 1

    return L, U


def compute_all(eigenvalues, L_below=None, U_above=None):
    """Compute A, P, P^{-1}, spectral projections, eigenspaces, and verify everything."""
    n = len(eigenvalues)
    eigenvalues = [Rational(e) for e in eigenvalues]

    L, U = build_LU(n, L_below, U_above)
    P = L * U
    P_inv = P.inv()
    D = zeros(n)
    for i in range(n):
        D[i, i] = eigenvalues[i]

    A = P * D * P_inv

    print("=" * 70)
    print("INTEGER MATRIX GENERATOR — LU TRICK")
    print("=" * 70)
    print(f"\nDimension: {n}×{n}")
    print(f"Eigenvalues: {[int(e) for e in eigenvalues]}")

    print(f"\nL = {latex_matrix(L)}")
    print(f"U = {latex_matrix(U)}")
    print(f"P = LU = {latex_matrix(P)}")
    print(f"det(P) = {P.det()}")
    print(f"P^{{-1}} = {latex_matrix(P_inv)}")
    print(f"\nD = {latex_matrix(D)}")
    print(f"\nA = PDP^{{-1}} = {latex_matrix(A)}")

    # Characteristic polynomial
    t = Symbol('t')
    char_poly = (t * eye(n) - A).det()
    char_poly = factor(char_poly)
    print(f"\ndet(tI - A) = {char_poly}")

    # Find distinct eigenvalues and their multiplicities
    distinct = []
    seen = set()
    for e in eigenvalues:
        if e not in seen:
            mult = eigenvalues.count(e)
            distinct.append((e, mult))
            seen.add(e)

    print(f"\nDistinct eigenvalues: {[(int(e), m) for e, m in distinct]}")

    # Spectral projections via Lagrange
    print("\n" + "-" * 50)
    print("SPECTRAL PROJECTIONS (Lagrange formula)")
    print("-" * 50)

    projections = {}
    for lam, mult in distinct:
        others = [(e, m) for e, m in distinct if e != lam]
        proj = eye(n)
        for other_lam, other_mult in others:
            proj = proj * (A - other_lam * eye(n)) / (lam - other_lam)
        projections[lam] = proj

        # Value table
        vt = []
        for e2, _ in distinct:
            if e2 == lam:
                vt.append(1)
            else:
                vt.append(0)

        print(f"\nP_{{{int(lam)}}} = {latex_matrix(proj)}")
        print(f"  rank = {proj.rank()}")
        print(f"  value table = ({', '.join(str(v) for v in vt)})")

    # Verify projection properties
    print("\n" + "-" * 50)
    print("VERIFICATION")
    print("-" * 50)

    proj_list = list(projections.values())
    lam_list = [lam for lam, _ in distinct]

    # Sum = I
    total = sum(proj_list[1:], proj_list[0])
    assert total == eye(n), "FAIL: projections don't sum to I"
    print("✓ ΣP_i = I")

    # P_i^2 = P_i
    for lam, proj in projections.items():
        assert proj * proj == proj, f"FAIL: P_{int(lam)}^2 ≠ P_{int(lam)}"
    print("✓ P_i² = P_i for all i")

    # P_i P_j = 0
    for i, (l1, p1) in enumerate(projections.items()):
        for j, (l2, p2) in enumerate(projections.items()):
            if i != j:
                assert p1 * p2 == zeros(n), f"FAIL: P_{int(l1)}·P_{int(l2)} ≠ 0"
    print("✓ P_i·P_j = 0 for i≠j")

    # AP_i = λ_i P_i
    for lam, proj in projections.items():
        assert A * proj == lam * proj, f"FAIL: A·P_{int(lam)} ≠ {int(lam)}·P_{int(lam)}"
    print("✓ A·P_i = λ_i·P_i for all i")

    # Spectral decomposition
    recon = zeros(n)
    for lam, proj in zip(lam_list, proj_list):
        recon = recon + lam * proj
    assert recon == A, "FAIL: Σλ_iP_i ≠ A"
    print("✓ A = Σλ_i·P_i")

    # Eigenspace basis vectors
    print("\n" + "-" * 50)
    print("EIGENSPACES")
    print("-" * 50)

    for lam, proj in projections.items():
        cols = proj.columnspace()
        print(f"\nE_{{{int(lam)}}} = Col(P_{{{int(lam)}}}) = span{{ {', '.join(latex_vec(c) for c in cols)} }}")
        for c in cols:
            Ac = A * c
            expected = lam * c
            assert Ac == expected, f"FAIL: A·{latex_vec(c)} ≠ {int(lam)}·{latex_vec(c)}"
            print(f"  A·{latex_vec(c)} = {latex_vec(Ac)} = {int(lam)}·{latex_vec(c)} ✓")

    # Cross-filling (two-factor decomposition) for each projection
    print("\n" + "-" * 50)
    print("CROSS-FILLING (Two-Factor Decomposition)")
    print("-" * 50)

    all_U_factors = []
    all_V_factors = []

    for lam, proj in projections.items():
        r = proj.rank()
        print(f"\nP_{{{int(lam)}}} (rank {r}):")

        U_cols, V_rows = cross_fill(proj)
        all_U_factors.append((lam, U_cols, V_rows))

        print(f"  U_{{{int(lam)}}} = {latex_matrix(U_cols)}  ({n}×{r})")
        print(f"  V_{{{int(lam)}}} = {latex_matrix(V_rows)}  ({r}×{n})")

        # Verify V·U = I_r
        VU = V_rows * U_cols
        assert VU == eye(r), f"FAIL: V·U ≠ I for λ={int(lam)}"
        print(f"  V·U = I_{r} ✓")

        # Verify U·V = P
        UV = U_cols * V_rows
        assert UV == proj, f"FAIL: U·V ≠ P for λ={int(lam)}"
        print(f"  U·V = P_{{{int(lam)}}} ✓")

        # Right eigenvectors (columns of U)
        print(f"  Right eigenvectors: {', '.join(latex_vec(U_cols.col(j)) for j in range(r))}")
        # Left eigenvectors (rows of V)
        print(f"  Left eigenvectors: {', '.join(latex_vec(V_rows.row(j).T) for j in range(r))}")

    # Stacked diagonalization P_full, D_full, Q_full
    print("\n" + "-" * 50)
    print("DIAGONALIZATION (stacked cross-fillings)")
    print("-" * 50)

    P_full = Matrix.hstack(*[U for _, U, _ in all_U_factors])
    Q_full = Matrix.vstack(*[V for _, _, V in all_U_factors])

    D_blocks = []
    for lam, U_f, _ in all_U_factors:
        r = U_f.cols
        block = lam * eye(r)
        D_blocks.append(block)

    from sympy import diag as sympy_diag
    D_full = Matrix.diag(*D_blocks)

    print(f"\nP_full = {latex_matrix(P_full)}")
    print(f"Q_full = P_full^{{-1}} = {latex_matrix(Q_full)}")
    print(f"D_full = {latex_matrix(D_full)}")

    assert Q_full * P_full == eye(n), "FAIL: Q·P ≠ I"
    print("✓ Q·P = I")

    assert P_full * D_full * Q_full == A, "FAIL: P·D·Q ≠ A"
    print("✓ A = P·D·P^{-1}")

    # LaTeX output for slides
    print("\n" + "=" * 70)
    print("LATEX SNIPPETS")
    print("=" * 70)

    print(f"\n% Matrix A")
    print(f"A = {latex_bmatrix(A)}")

    print(f"\n% Characteristic polynomial")
    print(f"\\det(tI - A) = {char_poly}")

    for lam, proj in projections.items():
        print(f"\n% Projection P_{{{int(lam)}}}")
        print(f"P_{{{int(lam)}}} = {latex_bmatrix(proj)}")

    print(f"\n% Eigenvector matrix P")
    print(f"P = {latex_bmatrix(P_full)}")
    print(f"P^{{-1}} = {latex_bmatrix(Q_full)}")
    print(f"D = {latex_bmatrix(D_full)}")

    # Test vector
    print("\n" + "-" * 50)
    print("SUGGESTED TEST VECTORS")
    print("-" * 50)

    for v_entries in [[1] * n, list(range(1, n + 1)), list(range(2, n + 2))]:
        v = Matrix(v_entries)
        pieces = [(lam, proj * v) for lam, proj in projections.items()]
        total = zeros(n, 1)
        for _, p in pieces:
            total = total + p
        all_int = all(all(x == int(x) for x in p) for _, p in pieces)
        all_nonzero = all(p != zeros(n, 1) for _, p in pieces)

        if all_int and all_nonzero and total == v:
            print(f"\nv = {latex_vec(v)} — all pieces integer and nonzero:")
            for lam, piece in pieces:
                print(f"  P_{{{int(lam)}}}·v = {latex_vec(piece)}")
                Ap = A * piece
                print(f"  A·(P_{{{int(lam)}}}·v) = {latex_vec(Ap)} = {int(lam)}·{latex_vec(piece)}")
            print(f"  Sum = {latex_vec(total)} = v ✓")
            Av = A * v
            print(f"  A·v = {latex_vec(Av)}")
            scaled_sum = zeros(n, 1)
            for lam2, p2 in pieces:
                scaled_sum = scaled_sum + lam2 * p2
            print(f"  Sum of scaled pieces = {latex_vec(scaled_sum)} ✓")


def cross_fill(P):
    """Cross-fill a projection matrix P into U·V where V·U = I.

    Uses the pivot-based greedy algorithm: scan for nonzero diagonal entries
    (or largest entries) and extract rank-1 layers.
    """
    n = P.rows
    r = P.rank()

    if r == 0:
        return Matrix(n, 0, []), Matrix(0, n, [])

    R = P.copy()
    U_cols = []
    V_rows = []

    for step in range(r):
        # Find pivot: largest absolute diagonal entry in remaining matrix
        best_idx = -1
        best_val = 0
        for i in range(n):
            if abs(R[i, i]) > abs(best_val):
                best_val = R[i, i]
                best_idx = i

        if best_val == 0:
            # No diagonal pivot — find any nonzero entry
            for i in range(n):
                for j in range(n):
                    if abs(R[i, j]) > abs(best_val):
                        best_val = R[i, j]
                        best_idx = (i, j)
            if isinstance(best_idx, tuple):
                i, j = best_idx
                col_vec = R.col(j) / best_val
                row_vec = R.row(i)
                U_cols.append(col_vec)
                V_rows.append(row_vec)
                R = R - col_vec * row_vec
                continue

        if best_idx == -1:
            break

        pivot = best_val
        col_vec = R.col(best_idx) / pivot
        row_vec = R.row(best_idx)

        U_cols.append(col_vec)
        V_rows.append(row_vec)

        R = R - col_vec * row_vec

    U = Matrix.hstack(*U_cols)
    V = Matrix.vstack(*V_rows)

    return U, V


def latex_matrix(M):
    """Format a sympy Matrix as a readable string."""
    rows = []
    for i in range(M.rows):
        row = [str(int(M[i, j])) for j in range(M.cols)]
        rows.append(" ".join(row))
    return f"[{'; '.join(rows)}]"


def latex_vec(v):
    """Format a column vector."""
    if v.cols == 1:
        return f"({', '.join(str(int(v[i])) for i in range(v.rows))})"
    else:
        return f"({', '.join(str(int(v[0, j])) for j in range(v.cols))})"


def latex_bmatrix(M):
    """Format as LaTeX \\begin{pmatrix}...\\end{pmatrix}."""
    rows = []
    for i in range(M.rows):
        row = " & ".join(str(int(M[i, j])) for j in range(M.cols))
        rows.append(row)
    return "\\begin{pmatrix}" + " \\\\ ".join(rows) + "\\end{pmatrix}"


def parse_entries(s):
    """Parse a comma-separated string of integers."""
    return [int(x.strip()) for x in s.split(",")]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate integer matrices with prescribed eigenvalues")
    parser.add_argument("--eigenvalues", "-e", type=int, nargs="+", default=[1, 3],
                        help="Eigenvalues (may repeat for multiplicity)")
    parser.add_argument("--L", type=str, default=None,
                        help="Below-diagonal entries of L, comma-separated")
    parser.add_argument("--U", type=str, default=None,
                        help="Above-diagonal entries of U, comma-separated")

    args = parser.parse_args()

    L_below = parse_entries(args.L) if args.L else None
    U_above = parse_entries(args.U) if args.U else None

    compute_all(args.eigenvalues, L_below, U_above)
