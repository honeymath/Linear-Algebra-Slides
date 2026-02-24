# docs/

Formal project artifacts. All documents here belong to the team, not to any individual.

## Contents

### Decision Traceability Chain

| Directory | Purpose | Traceability |
|-----------|---------|--------------|
| `adr/` | Architecture Decision Records — system-level "why" | Root |
| `dr/` | Design Rationale — implementation-level "why this way" | Child of ADR |
| `eir/` | Engineering Investigation Records — exploration and dead ends | Child of DR |
| `tr/` | Test Rationale — test design "why this scenario" | Child of DR |
| `ret/` | After Action Records — execution experience "what happened and what we learned" | Child of DR |

### Analysis Traceability Chain

| Directory | Purpose | Traceability |
|-----------|---------|--------------|
| `aa/` | Architecture Analysis — external system "what and why" | Root |
| `da/` | Design Analysis — external component "how and why" | Child of AA |
| `ta/` | Test Analysis — external testing "how tested and why" | Child of DA |

### Other

| Directory | Purpose |
|-----------|---------|
| `knowledge/` | Distilled team knowledge entries |
| `issues/` | Structured issue documents |

## Decision Traceability Chain

```
ADR-XXXX                          (Architecture Decision)
  └── DR-XXXX-YYYY                (Design Rationale for that ADR)
        ├── EIR-XXXX-YYYY-ZZZZ   (Investigation Record for that DR)
        ├── TR-XXXX-YYYY-ZZZZ    (Test Rationale for that DR)
        └── RET-XXXX-YYYY-ZZZZ   (After Action Record for that DR)
```

## Analysis Traceability Chain

```
AA-XXXX                           (Architecture Analysis)
  └── DA-XXXX-YYYY                (Design Analysis for that AA)
        └── TA-XXXX-YYYY-ZZZZ    (Test Analysis for that DA)
```

## Cross-referencing

The Decision chain and Analysis chain are independent but may cross-reference:

- An AA may **inspire** an ADR (analyzing a library leads to a decision about adoption)
- An ADR may **motivate** an AA (deciding to adopt a framework triggers analysis of it)
- Cross-references use the format: `See AA-0001` or `Motivated by ADR-0012`

Use `0000` as a placeholder when a record has no parent at a given level.

## Summary Layer

Every document type directory has a `summary/` sub-directory containing
human-readable summaries. See any `summary/README.md` for details.
