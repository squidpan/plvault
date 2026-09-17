# Discovery Exercise — Identifier Override and Legacy Translation

## Scenario

The fictional Order Entry application defaults an account's expanded representative code onto a new order. Authorized users may override that code for approved scenarios. One downstream consumer still accepts only a three-character alias.

## Objective

Discover enough current-state evidence and target behavior to make the override and translation stories Ready without inventing policy.

## Interview roles

- Product owner
- Trading operations user
- Identifier data steward
- Order Entry/OMS engineer
- Integration engineer
- Control/compliance partner
- QA/UAT lead
- Production support owner

## Questions to resolve

1. Which actors can override, under what business scenarios, and with which entitlement?
2. Is the account assignment, order value, or another record authoritative at each lifecycle stage?
3. Must an override capture reason, approval, original value, new value, actor, and timestamp?
4. Which consumers support four characters, and which need an alias?
5. Who owns mappings, effective dates, approvals, corrections, and historical interpretation?
6. What happens for missing, duplicate, future, expired, disabled, or unavailable mappings?
7. How are retries, duplicates, partial failures, reconciliation, and replay controlled?
8. Which reports, supervision, books/records, confirmations, and archives consume the value?
9. What evidence proves correct attribution and enables support investigation?
10. Who has acceptance authority for UAT and controls?

## Deliverables

- Updated current/target flow and lineage
- Decision record for override authority and translation location
- Business rules and data definitions
- Interface/mapping updates
- Risks and controls
- Story/AC/test updates
- RTM coverage review

## Stop condition

Do not choose override or exception behavior merely to complete the exercise. Mark unresolved policy as an owned question, assumption, decision, or risk.
