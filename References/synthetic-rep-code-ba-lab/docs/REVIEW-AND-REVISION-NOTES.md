# Review and Revision Notes

Review date: 2026-09-16

## Retained

- The domain-foundation notes: they explain the synthetic business problem clearly.
- The pre-trade, post-trade, lineage, translation, and ERD diagrams: they make system boundaries and data movement visible.
- The SQL lab: it provides hands-on investigation patterns instead of documentation alone.
- The layered diagram convention: it supports executive overview, analyst detail, and implementation detail without crowding one diagram.

## Revised

- Reframed the repository from interview preparation to a reusable synthetic BA case study.
- Added an explicit boundary prohibiting real employer, customer, account, production, and confidential data.
- Instantiated the requirements lifecycle: discovery, epic, feature, story, acceptance criteria, rules, data, interface, decision, risk, lineage, mapping, tests, and RTM.
- Replaced the single-key translation model with consumer-specific, effective-dated, versioned mappings.
- Corrected the legacy translation flow so translated values reach the legacy consumer.
- Added fail-closed exception handling rather than an ambiguous bypass.
- Added a validator for metadata, identifiers, links, and RTM references.

## Archived or Removed

- Archived the original translation diagram and v1 SQL model for learning comparison.
- Removed dated recruiting/status notes because they do not contribute to the reusable case study.
- Removed empty interview scaffolding.

## Deliberate Gaps

- The SQL model demonstrates the requirement but does not implement a PostgreSQL exclusion constraint for overlapping effective-date ranges. A production design should select a constraint, trigger, or controlled service policy and test it explicitly.
- The PlantUML diagrams should be rendered in the user's local toolchain as a final visual QA step.
- The synthetic requirements are a coherent worked example, not a claim about any employer's actual systems or practices.
