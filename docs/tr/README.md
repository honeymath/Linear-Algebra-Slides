# tr/ — Test Rationale

**Purpose:** Document the "why" behind test design and test scenarios.

## What Goes Here

Test Rationale (TR) documents explain:
- Why specific test scenarios were chosen
- Edge cases and boundary conditions being tested
- Test coverage strategy
- Risk assessment and mitigation through testing

## Format

Each TR should include:
- **Context:** Which DR is being tested?
- **Test Strategy:** What approach is being taken?
- **Test Scenarios:** What specific cases are covered?
- **Rationale:** Why these tests are sufficient?

## Naming Convention

Use `TR-XXXX-YYYY-ZZZZ.md` where:
- XXXX = ADR number
- YYYY = DR number being tested
- ZZZZ = sequential test rationale (zero-padded, e.g., `TR-0001-0001-0001.md`)

## Relationship to Other Documents

- Parent: `DR-` (Design Rationale)
- Children: None (leaf nodes in decision chain)

## Example Structure

```
TR-0001-0001-0001: LaTeX compilation test scenarios
TR-0001-0001-0002: Slide rendering consistency tests
```

## Note

Test rationale is separate from test code. This documents the reasoning behind test design, not the test implementation itself.
