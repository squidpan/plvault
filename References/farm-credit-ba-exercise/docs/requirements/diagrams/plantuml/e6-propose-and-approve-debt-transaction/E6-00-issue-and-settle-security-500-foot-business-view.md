---
id: E6-00
project: farm-credit-ba-exercise
type: diagram-guide
status: approved
epic: E6
feature: E6-01
diagram: E6-00-issue-and-settle-security-500-foot-business-view.puml
layer: "L0 Executive Overview"

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

description: How does a debt transaction move from proposal through issuance, settlement, reconciliation, and closure?
created: 2026-07-21
updated: 2026-07-22
---

```plantuml
@startuml
title E6 — Issue and Settle Security\n500-Foot Business View

skinparam shadowing false
skinparam activity {
  BackgroundColor White
  BorderColor Black
  DiamondBackgroundColor White
  DiamondBorderColor Black
  FontSize 14
}
skinparam defaultTextAlignment center
skinparam ArrowThickness 1.2

|Issuance Team|
start
:Propose debt\ntransaction;

|Treasury Approver|
:Review terms\nand approve;

|Debt Issuance Platform|
:Prepare security\nand identifier;

|Settlement Operations|
:Submit issuance and\nsettlement instruction;

|Federal Reserve\nBook-Entry Infrastructure|
:Issue security and\nsettle DVP;

|Dealer / Investor|
:Receive security\nand provide cash;

|Debt Issuance Platform|
:Receive settlement\nstatus and proceeds;

|Finance / Accounting|
:Reconcile cash,\nsecurity and accounting;

|Debt Issuance Platform|
:Close transaction\nand retain audit trail;

stop

legend bottom
|= Stage |= Primary information |
| Propose | Amount, product, rate, dates |
| Approve | Authorization and controls |
| Prepare | CUSIP and security terms |
| Settle | Security exchanged for cash |
| Reconcile | Cash, quantity and accounting |
| Close | Final status and audit history |

DVP = Delivery versus Payment
The Federal Reserve provides book-entry and settlement infrastructure.
The investor or settlement participant provides the purchase cash.
endlegend

@enduml
```

# E6-00-issue-and-settle-security-500-foot-business-view

## Business Question

How does a debt transaction move from proposal through issuance, settlement, reconciliation, and closure?

## Purpose

Provide a single executive-level view of the end-to-end business capability without implementation detail.

## How to Explain It

This is the 500-foot view of the debt issuance lifecycle. It starts with the issuance team proposing a transaction, moves through Treasury approval, security preparation, settlement through Federal Reserve book-entry infrastructure, receipt of cash from the dealer or investor, reconciliation, and final closure. I would use this diagram first with executives or new team members because it establishes the complete business context before drilling into E6-01.

## Key Talking Points

- The process crosses business, platform, settlement, market participant, and accounting boundaries.
- Approval is only one stage in a larger issue-and-settle lifecycle.
- Delivery versus payment links the movement of the security to receipt of cash.
- The final outcome includes reconciliation and a retained audit trail.

## What This Diagram Does Not Show

Detailed approval rules, field-level requirements, exception handling, or system interactions.

## Position in the Visual Decomposition

`L0 Executive Overview`

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[E6-00-issue-and-settle-security-500-foot-business-view]]
