# LaTeX Installation — Minimal Approaches

**Purpose:** Quick reference for team members to install minimal LaTeX distributions suitable for command-line Beamer slide compilation.

## Context

This project uses Beamer presentation framework with LaTeX. For CI/CD, local development, and reproducible builds, teams need reliable LaTeX installations without bloat.

## Installation Options

### Option 1: TeX Live (Recommended)

**Ubuntu/Debian — Minimal Beamer Setup (~150-200MB)**
```bash
sudo apt install texlive-latex-base texlive-beamer texlive-fonts-recommended texlive-latex-extra
```

**Full Minimal TeX Live (~300-400MB)**
```bash
# Download from https://tug.org/texlive/
./install-tl -scheme=minimal
```

### Option 2: MiKTeX (Alternative)

**Ubuntu/Debian**
```bash
sudo apt install miktex
```

**Advantage:** On-demand package installation (~50MB base, grows as needed)

### Option 3: Alpine Linux / Docker (Absolute Minimal)

**Dockerfile**
```dockerfile
FROM alpine:latest
RUN apk add --no-cache texlive texlive-latex texlive-beamer texlive-fonts
```

**Result:** ~250MB container, perfect for CI/CD pipelines

### Option 4: macOS (Homebrew)

**Minimal BasicTeX**
```bash
brew install basictex  # ~100MB
tlmgr install beamer   # Install Beamer on-demand
```

## Verification

```bash
# Check LaTeX installation
pdflatex --version

# Test Beamer availability
pdflatex -interaction=batchmode '\documentclass{beamer}\begin{document}\end{document}'
```

## Team Recommendation

For this project, use **Option 1** (TeX Live on Linux) or **Option 4** (BasicTeX on macOS):
- Stable and well-supported
- Includes all Beamer dependencies
- Suitable for CI/CD environments
- ~150-200MB footprint

## Related Documents

- CI/CD pipeline configuration: See `process-governance` skill documentation
- Beamer customization: Check `DA-0001-0001: Beamer Metropolis theme customization` (when created)
- Docker setup: Consider `TA-` (Test Analysis) for containerized build validation
