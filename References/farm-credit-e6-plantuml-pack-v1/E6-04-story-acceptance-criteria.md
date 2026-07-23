# E6 — Issue and Settle Security

## Epic objective

Exchange an approved Farm Credit debt security for cash accurately through the applicable book-entry and settlement process, while providing operational control, reconciliation, exception handling, and auditability.

## Primary user story

**As a Settlement Operations Analyst,**  
I want the platform to generate, validate, submit, and monitor an issuance instruction for an approved security  
**so that** the security can be issued and settled accurately on the agreed settlement date.

## Primary actor

- Settlement Operations Analyst

## Supporting actors

- Issuance Officer
- Issuance Approver / Treasury Manager
- Finance / Accounting Analyst
- Operations Support
- Dealer or investor-side settlement participant
- CUSIP / security-identifier service
- Federal Reserve book-entry / Fedwire Securities interface
- General ledger / cash system

## Inputs and outputs

| Direction | Data / information |
|---|---|
| Into platform | approved security terms, principal, trade date, settlement date, maturity date, rate terms, CUSIP, submitter identity, correction reason |
| Out to settlement interface | issuance instruction, security identifier, principal, settlement date, product terms, correlation/message identifiers |
| Back into platform | accepted, pending, rejected, settled status; reason codes; timestamps; final security movement |
| To finance/reconciliation | final security quantity, cash proceeds, ledger postings, break details |
| To users | validation results, approval status, settlement status, actionable exceptions, audit history |

## Acceptance criteria and diagram traceability

| ID | Acceptance criterion | Use case | Happy path | Exception path |
|---|---|---|---|---|
| AC-E6-01 | Given a transaction has final approval, when an instruction is generated, then it contains the approved CUSIP, principal, settlement date, maturity date, and product-specific terms. | UC-E6-01 to UC-E6-04 | E6-01 through E6-12 | — |
| AC-E6-02 | Given a mandatory field is missing or invalid, when submission is attempted, then transmission is blocked and the field-level error is identified. | UC-E6-04 | E6-11 to E6-13 | EX correction flow applies after external rejection |
| AC-E6-03 | Given a valid instruction is submitted, when an external response is received, then the platform records accepted, pending, rejected, or settled status with message ID and timestamp. | UC-E6-05 and UC-E6-06 | E6-14 through E6-21 | EX-01 through EX-04 |
| AC-E6-04 | Given an instruction is rejected, when Operations opens the exception, then the rejection reason, affected data, prior versions, and corrective actions are visible. | UC-E6-07 | — | EX-05 through EX-08 |
| AC-E6-05 | Given a correction changes a material approved term, when the instruction is resubmitted, then reapproval is required and recorded first. | UC-E6-07 and UC-E6-08 | — | EX-09 through EX-17 |
| AC-E6-06 | Given settlement completes, when reconciliation runs, then final security quantity, cash proceeds, and approved amount reconcile or an actionable break is created. | UC-E6-09 | E6-22 through E6-35 | Follow-on exception if break remains |
| AC-E6-07 | Given any instruction, approval, response, correction, or retry occurs, then user, timestamp, old value, new value, message ID, and reason are retained in audit history. | UC-E6-10 | Throughout | Throughout |
| AC-E6-08 | Given an exception cannot be resolved within the permitted process or time, when Operations escalates it, then an owner, severity, blocked status, and notification are recorded. | UC-E6-11 | — | Final unresolved path |

## Interview explanation

Use this order when pointing to the diagrams:

1. The context diagram identifies the people, systems, and information exchanged.
2. The use-case diagram defines the functional scope and actor responsibilities.
3. The happy-path sequence demonstrates normal issuance, external acknowledgment, settlement, and reconciliation.
4. The exception sequence demonstrates controls, auditability, material-change approval, retry, and escalation.

## Discovery questions

- Which security terms are mandatory for each debt product?
- Which source owns the CUSIP and when is it assigned?
- What defines a material versus non-material correction?
- Which approvals are required before initial submission and resubmission?
- What settlement statuses and reason codes are received?
- What are the cut-off times and escalation thresholds?
- Can settlement be partial, or must it be all-or-nothing?
- How are duplicates and idempotent retries prevented?
- What systems provide cash and security positions for reconciliation?
- What records must be retained, and for how long?
