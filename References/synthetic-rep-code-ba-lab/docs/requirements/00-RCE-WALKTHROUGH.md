## Synthetic Rep Code Expansion Walkthrough

> [!warning] Fictional training example
> All organizations, systems, identifiers, rules, data, and decisions here are invented. This must not be represented as any employer's actual architecture or policy.

## The point

A fictional brokerage platform has nearly exhausted its three-character representative identifier namespace. The initiative enables four-character identifiers while protecting legacy consumers that cannot yet accept them.

## Story of the requirements

1. **Problem:** new identifiers cannot scale safely; special-character workarounds are unreliable.
2. **Constraint:** some consumers remain limited to three characters during migration.
3. **Hinge decision:** use an owned, effective-dated translation mapping; never truncate.
4. **Transformation:** validate the expanded identifier, resolve a unique active legacy code where needed, and propagate an auditable result.
5. **Failure posture:** unmapped, duplicate, or expired mappings stop processing and enter a controlled exception path.
6. **Proof:** linked AC and tests show success, exception control, and auditability.

## Navigation

- Epic: [[EPIC-RCE-001]]
- Feature: [[FEATURE-RCE-010]]
- Story: [[US-RCE-101]]
- Acceptance criteria: [[AC-RCE-101]]
- Rule: [[BR-RCE-001]]
- Data: [[DATA-RCE-001]]
- Interface: [[INT-RCE-001]]
- Decision: [[DEC-RCE-001]]
- Risk: [[RISK-RCE-001]]
- Discovery: [[DISC-RCE-001]]
- Lineage: [[LINEAGE-RCE-001]]
- Mapping: [[MAP-RCE-001]]
- Tests: [[TC-RCE-101-01]], [[TC-RCE-101-02]]
- RTM: `RTM-RCE-001.csv`

## Synthetic system landscape

`Advisor Setup → Order Entry → Translation Service → Legacy Routing → Confirmation/Audit`

The Translation Service is fictional. It illustrates the analysis pattern: identify the system of record, isolate compatibility logic, make exceptions explicit, and preserve evidence.
