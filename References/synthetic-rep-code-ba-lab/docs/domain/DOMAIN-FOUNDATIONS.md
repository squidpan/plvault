# Synthetic Rep Code BA Lab — Domain Foundations

## Session 1 — Brokerage & Wealth Management 101
- Client is the customer; one client can have multiple accounts.
- Order = instruction; execution = fill; trade = resulting transaction.
- Rep Code is not the client identifier.
- Clearing determines obligations; settlement fulfills them.
- Self-directed brokerage does not require a dedicated advisor.

## Session 2 — Rep Codes 101
- Employee ID identifies a person/employee; Rep Code represents a brokerage business relationship, assignment, team, compensation structure, order-handling role, etc.
- System of Record (SOR) is the authoritative source of truth.
- Rep Codes can have historical meaning; reuse can create ambiguity.
- Data lineage traces origin, movement, transformation, and consumption.
- Synthetic case-study direction: 4-character Rep Codes with controlled translation for legacy compatibility.

## Session 3 — Trading Lifecycle 101
- Order → execution(s) → trade.
- OMS manages orders through the lifecycle.
- Pre-trade = before execution; post-trade = after execution.
- Do not assume where Rep Code travels; trace it.
- Technical finding → business impact → solution/options.
- Successful processing does not necessarily mean correct processing.

## Session 4 — Systems, Data & Data Lineage
- Immediate source system is not necessarily the SOR.
- Lineage = path/journey; mapping = source/target correspondence.
- Interfaces and rules can block 4-character support even when databases can store it.
- Backward lineage traces to origin; forward lineage supports impact analysis.
- End-to-end capability requires storage, UI/input, validation, business logic, interfaces, transformations, and downstream compatibility.

## Session 5 — Synthetic Rep Code Expansion
- Business problem: 3-character namespace/construct no longer scales with growth and increasingly complex business structures.
- Solution direction: support 4-character Rep Codes.
- Constraint: legacy 3-character processing must continue to work.
- Compatibility strategy: centralized translation approach.
- Migration = movement toward target state; coexistence = old/new operating together during transition.
- Do not invent missing-mapping behavior; obtain required behavior from SMEs/Product/Operations.
- Gap analysis compares As-Is to To-Be and drives requirements, AC, testing, and release dependencies.

## Session 6 — Regulatory Environment for a Trading BA
- Correct attribution matters even if a trade executes and settles.
- Data lineage supports traceability/auditability.
- Historical mappings may be needed to understand business meaning at transaction time.
- Preventive controls stop errors; detective controls find them.
- Regulatory SME interprets obligations; BA translates them into process, data, system behavior, requirements, acceptance criteria, and tests.
- Positioning: experience in controlled financial environments without claiming regulatory-expert status.
