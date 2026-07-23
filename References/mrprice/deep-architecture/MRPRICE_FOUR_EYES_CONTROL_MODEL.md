---

type: governance
status: draft
source: mrprice-docs
categories:

 - "[[MRPrice]]"
 - "[[Governance]]"
 - "[[Controls]]"
tags:
 - governance
 - controls
 - inspector
 - guardian
 - workflow
 - audit
  
created: 2026-06-10
last: 2026-06-10
origin: chatgpt

---

# MRPrice Four-Eyes Control Model

## Purpose

The Four-Eyes Control Model was designed to ensure that no single individual could introduce and approve a pricing change.

The model enforced separation of duties and supported auditability.

## Core Principle

```text
Inspector ≠ Guardian
```

The person performing the review could not be the same person approving the result.

## Roles

### Inspector

Responsibilities:

* investigate exception
* review pricing issue
* perform analysis
* propose correction

### Guardian

Responsibilities:

* independently review findings
* approve or reject proposed action
* ensure compliance with controls

## Workflow

```text
Exception
     ↓
Inspector
     ↓
Recommendation
     ↓
Guardian
     ↓
Approval / Rejection
```

## Benefits

### Data Quality

Reduces risk of incorrect pricing changes.

### Operational Control

Provides separation of duties.

### Auditability

Creates a clear record of:

* who reviewed
* who approved
* what changed
* when it changed

### Regulatory Alignment

Supports strong governance practices expected in regulated financial environments.

## Interview Relevance

This workflow demonstrates experience with:

* operational controls
* governance
* approval workflows
* risk management
* audit readiness

## Related Notes

* [[MRPRICE_BENCHMARK_VALIDATION_WORKFLOW]]
* [[MRPRICE_PRODUCTION_SUPPORT]]
* [[MRPRICE_OPERATIONS_MODEL]]

