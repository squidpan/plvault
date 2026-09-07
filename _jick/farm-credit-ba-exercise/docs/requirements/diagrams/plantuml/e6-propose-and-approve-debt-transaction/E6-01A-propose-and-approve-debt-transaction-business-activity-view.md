---
id: E6-01A
project: farm-credit-ba-exercise
type: diagram-guide
status: approved
epic: E6
feature: E6-01
diagram: E6-01A-propose-and-approve-debt-transaction-business-activity-view.puml
layer: "L1 Business Workflow"

categories:
  - "[[Diagrams]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - farm-credit
  - debt-issuance
  - business-analysis
  - plantuml
  - interview-study

description: What business activities and status changes occur when a debt transaction is proposed and approved?
created: 2026-07-21
updated: 2026-07-22
---
---
```puml
@startuml
title E6-01 — Propose and Approve Debt Transaction\nBusiness Activity View

skinparam shadowing false
skinparam defaultTextAlignment center
skinparam ArrowThickness 1.2
skinparam activity {
  BackgroundColor White
  BorderColor Black
  DiamondBackgroundColor White
  DiamondBorderColor Black
  FontSize 14
}

|Issuance Officer|
start

:Create draft debt\ntransaction;

note right
Core terms:
- product type
- principal amount
- trade date
- settlement date
- maturity date
- rate or spread
end note

:Save draft;

|Debt Issuance Platform|
:Assign transaction ID\nand Draft status;

:Validate required fields\nand business rules;

if (Valid?) then (Yes)

  |Issuance Officer|
  :Review validation\nresults;

  :Submit transaction\nfor approval;

  |Debt Issuance Platform|
  :Lock submitted version;

  :Create approval request;

  |Treasury Approver|
  :Review terms,\nrisks and exceptions;

  if (Approve?) then (Approve)

    :Approve transaction;

    |Debt Issuance Platform|
    :Set status to\nApproved;

    :Record approval,\nuser and timestamp;

    stop

  else (Return)

    :Return for correction\nwith reason;

    |Debt Issuance Platform|
    :Set status to\nChanges Required;

    |Issuance Officer|
    :Revise transaction;

    --> Save draft;

  endif

else (No)

  |Debt Issuance Platform|
  :Display validation\nerrors;

  |Issuance Officer|
  :Correct invalid or\nmissing terms;

  --> Save draft;

endif

legend bottom
|= Status |= Meaning |
| Draft | Transaction can be edited |
| Submitted | Awaiting approval |
| Changes Required | Returned for correction |
| Approved | Ready for security preparation |

Key control:
The user who creates or changes a transaction
should not approve the same transaction.
endlegend

@enduml
```

---



# E6-01A-propose-and-approve-debt-transaction-business-activity-view

## Business Question

What business activities and status changes occur when a debt transaction is proposed and approved?

## Purpose

Show the main workflow, actors, validation loops, approval decision, and return-for-correction path.

## How to Explain It

This diagram shows the full business workflow for E6-01. The Issuance Officer creates and saves a draft, the platform assigns an ID and validates it, and a valid proposal is submitted as a locked version for Treasury review. The approver can approve it or return it with a reason. Invalid or returned transactions loop back for correction. The key point is that the workflow is controlled by both business validation and independent approval.

## Key Talking Points

- Draft transactions remain editable.
- Submission creates a controlled version for review.
- Returned transactions enter Changes Required status.
- Approval records the approver and timestamp.
- The proposer should not approve the same transaction.

## What This Diagram Does Not Show

Detailed message exchanges, individual business rules, or field-by-field data evolution.

## Position in the Visual Decomposition

`L1 Business Workflow`

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]]
