# Linear Algebra Slides Repository

## Project Overview

This repository contains comprehensive lecture slides for Linear Algebra, including LaTeX-based slide presentations covering topics such as:
- Cayley-Hamilton Theorem
- Diagonalization
- LU Decomposition
- Lagrange Interpolation Polynomial
- Spectral Decomposition
- Linear Transformations
- Matrix Operations

The slides are designed as educational materials using Beamer presentation framework with Metropolis theme.

## Documentation Structure

This project follows a formal documentation hierarchy for tracking decisions and analysis:

### Decision Traceability Chain
- **ADR/** — Architecture Decision Records (system-level decisions)
- **DR/** — Design Rationale (implementation-level decisions)
- **EIR/** — Engineering Investigation Records (explorations and dead ends)
- **TR/** — Test Rationale (test design decisions)
- **RET/** — After Action Records (execution experience and lessons learned)

### Analysis Traceability Chain
- **AA/** — Architecture Analysis (external system analysis)
- **DA/** — Design Analysis (external component analysis)
- **TA/** — Test Analysis (external testing analysis)

### Other Documentation
- **knowledge/** — Distilled team knowledge entries
- **issues/** — Structured issue documents

All formal documentation goes in the `docs/` directory and belongs to the team.

## Commit Workflow

**IMPORTANT: All commits must use the `git-commit` skill to ensure proper signing and metadata.**

### Commit Process
1. Make your changes to the codebase
2. Stage your changes with `git add`
3. Use the **`/git-commit`** skill to create your commit (this signs it appropriately)
   - Example: `/git-commit -m "Your commit message"`
4. You will be prompted to push after the commit is created
5. Push to the remote repository when prompted

### Why Use git-commit Skill?
The `git-commit` skill ensures:
- Proper signing of commits with role identity
- Consistent commit metadata
- Team accountability and traceability

## Branch Guidelines

This is a **feature/reconstruction branch** (`2026-reconstruction`), not the main branch.
- Main branch: `main`
- All work on this branch should be properly documented in commits
- Push changes after each commit to keep remote synchronized

## Development Notes

- Slides are primarily written in LaTeX (`.tex` files)
- Beamer theme configuration: Metropolis
- Image assets located in `Pictures/` directory
- Python scripts may be used for auxiliary processing

---

**Last Updated:** 2026-02-24
