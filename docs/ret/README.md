# ret/ — After Action Records

**Purpose:** Document execution experience, what happened, and lessons learned.

## What Goes Here

After Action Records (RET) capture:
- How a design actually worked in practice
- Deviations from planned implementation
- Performance observations and bottlenecks
- Lessons learned and process improvements
- Team reflections on what went well and what didn't

## Format

Each RET should include:
- **Objective:** What was the work to execute?
- **Plan:** What was expected to happen?
- **Execution:** What actually happened?
- **Outcome:** Results and metrics
- **Lessons:** What did we learn?
- **Improvements:** What should change next time?

## Naming Convention

Use `RET-XXXX-YYYY-ZZZZ.md` where:
- XXXX = ADR number
- YYYY = DR number this action implements
- ZZZZ = sequential record number (zero-padded, e.g., `RET-0001-0001-0001.md`)

## Relationship to Other Documents

- Parent: `DR-` (Design Rationale)
- Children: None (leaf nodes in decision chain)

## Example Structure

```
RET-0001-0001-0001: Slide migration to new Beamer version
RET-0001-0001-0002: LaTeX module reorganization execution
```

## Note

After Action Records are critical for continuous improvement. They turn execution into institutional knowledge that improves future implementations.
