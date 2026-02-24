# issues/ — Structured Issue Documents

**Purpose:** Document issues, bugs, and feature requests in a structured format.

## What Goes Here

Issue documents capture:
- Bug reports with reproduction steps
- Feature requests with rationale
- Technical debt items
- Known limitations and workarounds
- Enhancement proposals

## Format

Each issue should include:
- **Title:** Clear, descriptive summary
- **Description:** What is the issue?
- **Impact:** Who does this affect? How critical?
- **Steps to Reproduce:** (for bugs)
- **Expected vs. Actual:** (for bugs)
- **Proposed Solution:** (for features/enhancements)
- **Related Documents:** Links to ADR/DR/RET if applicable

## Naming Convention

Use descriptive names: `ISSUE-NUMBER-title.md` (e.g., `ISSUE-001-slide-rendering-bug.md`)

## Example Structure

```
ISSUE-001-beamer-theme-fonts-not-rendering.md
ISSUE-002-request-add-speaker-notes-support.md
ISSUE-003-latex-compilation-timeout-on-large-files.md
```

## Workflow

- Create issue document when problem/request is identified
- Link to related ADR/DR/RET for traceability
- Update issue when resolution is found
- Reference issue in RET when fixed

## Integration

These issues inform:
- ADR creation (if architectural change needed)
- DR (if design change needed)
- RET (when issue is resolved)
