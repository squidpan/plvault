# SQL Analysis Guide

Use SQL to test assumptions and quantify requirement gaps—not merely to retrieve rows.

## Core BA investigation patterns

1. **Trace propagation:** Compare the account's authoritative rep code with the value captured on each order.
2. **Find missing coverage:** Cross-join active codes and active consumers, then left-join the currently effective approved mapping.
3. **Reconcile outputs:** Compare the rep code, legacy alias, and mapping version written to a trade with the mapping effective at processing time.
4. **Detect ambiguity:** Group approved mappings by code and consumer and identify overlapping active candidates.
5. **Test negative paths:** Include missing, inactive, expired, malformed, and duplicate mapping scenarios.

## Questions before writing a query

- Which table or service is authoritative for this field?
- At what business event should the value be captured?
- Does the query need current state or state as of an event timestamp?
- Which consumer or interface policy applies?
- What population and time window define completeness?
- What result would prove the requirement false?

## Evidence practice

- Record the question, query purpose, filters, execution date, result summary, and limitations.
- Use approved work systems for real queries and evidence.
- Keep this repository limited to fictional schemas and values.

The executable worked examples are in `sql/synthetic-rep-code-ba-lab.sql`. The earlier v1 lesson is retained in `archive/docs/` to show how the analysis evolved.
