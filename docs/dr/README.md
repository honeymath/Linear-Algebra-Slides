# dr/ — Design Rationale

**Purpose:** Record implementation-level design decisions that realize an ADR.

## What Goes Here

Design Rationale (DR) documents explain:
- How an architectural decision is implemented
- Specific design patterns and approaches used
- Component organization and interactions
- Technical choices at the implementation level

## Format

Each DR should include:
- **Motivation:** Which ADR does this implement?
- **Design:** How is it structured?
- **Trade-offs:** Why this approach over alternatives?
- **Impact:** What components are affected?

## Naming Convention

Use `DR-XXXX-YYYY.md` where:
- XXXX = ADR number this design implements
- YYYY = sequential number for this design (zero-padded, e.g., `DR-0001-0001.md`)

## Relationship to Other Documents

- Parent: `ADR-` (Architecture Decision Records)
- Children:
  - `EIR-` (Engineering Investigation Records) for explorations
  - `TR-` (Test Rationale) for test design
  - `RET-` (After Action Records) for execution experience

## Example Structure

```
DR-0001-0001: LaTeX module structure for slide organization
DR-0002-0001: Beamer template customization approach
```
