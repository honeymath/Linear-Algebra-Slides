# eir/ — Engineering Investigation Records

**Purpose:** Document exploration, experiments, and dead ends encountered during implementation.

## What Goes Here

Engineering Investigation Records (EIR) capture:
- Approaches that were tried and didn't work
- Exploratory spikes and prototyping
- Technical investigations and findings
- Lessons learned from failed approaches

## Format

Each EIR should include:
- **Investigation:** What was being explored?
- **Approach:** How was it investigated?
- **Findings:** What was discovered?
- **Outcome:** Why did this not work? What was learned?

## Naming Convention

Use `EIR-XXXX-YYYY-ZZZZ.md` where:
- XXXX = ADR number
- YYYY = DR number this investigation supports
- ZZZZ = sequential record number (zero-padded, e.g., `EIR-0001-0001-0001.md`)

## Relationship to Other Documents

- Parent: `DR-` (Design Rationale)
- Children: None (leaf nodes in decision chain)

## Example Structure

```
EIR-0001-0001-0001: Investigation of alternative Beamer themes
EIR-0001-0001-0002: Attempted dynamic slide generation approach
```

## Note

These records are valuable for the team to understand what was tried and why certain approaches were rejected. They prevent re-investigation of known dead ends.
