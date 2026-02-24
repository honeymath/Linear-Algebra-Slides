# adr/ — Architecture Decision Records

**Purpose:** Record system-level architectural decisions and the rationale behind them.

## What Goes Here

Architecture Decision Records (ADRs) document major decisions about:
- Project structure and organization
- Technology selection and integration
- System-level design patterns
- Long-term architectural direction

## Format

Each ADR should include:
- **Decision:** Clear statement of what was decided
- **Context:** Why this decision was needed
- **Consequences:** What changes as a result
- **Alternatives considered:** Other options evaluated

## Naming Convention

Use `ADR-XXXX.md` where XXXX is a zero-padded number (e.g., `ADR-0001.md`)

## Relationship to Other Documents

- Parent: None (root of decision chain)
- Children: `DR-` (Design Rationale) documents that implement this ADR

## Example Structure

```
ADR-0001: Use Beamer with Metropolis theme for all slides
ADR-0002: Organize slides by mathematical topic with LaTeX modules
```
