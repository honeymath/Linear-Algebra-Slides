# aa/ — Architecture Analysis

**Purpose:** Analyze external systems, libraries, and frameworks to understand "what and why" for potential adoption.

## What Goes Here

Architecture Analysis (AA) documents examine:
- External libraries and their capabilities
- Framework evaluation and comparison
- Third-party tool assessment
- Technology landscape analysis
- Vendor and dependency evaluation

## Format

Each AA should include:
- **System:** What external system/library is being analyzed?
- **Purpose:** Why are we analyzing this?
- **Capabilities:** What does it do?
- **Pros and Cons:** Strengths and weaknesses
- **Recommendation:** Should we adopt/use this?

## Naming Convention

Use `AA-XXXX.md` where XXXX is a zero-padded number (e.g., `AA-0001.md`)

## Relationship to Other Documents

- Parent: None (root of analysis chain)
- Children: `DA-` (Design Analysis) for deeper component-level analysis

## Example Structure

```
AA-0001: Analysis of Beamer presentation framework
AA-0002: Analysis of LaTeX distribution options
AA-0003: Analysis of slide preview tools
```

## Cross-References

An AA may inspire an ADR:
- Example: "Analysis of Beamer (AA-0001) led to decision to adopt Beamer (ADR-0001)"

Format: "Inspired ADR-0001"
