---
type: workflow
status: draft
source: mrprice-docs
categories:

- "[[MRPrice]]"
- "[[Benchmark Processing]]"
- "[[Data Quality]]"
- tags:
	- benchmark
	- validation
	- workflow
	- pricing
	- governance
created: 2026-06-10
last: 2026-06-10
origin: chatgpt
---

# MRPrice Benchmark Validation Workflow

## Purpose

The Benchmark Validation Workflow ensured that pricing data met quality standards before becoming available to downstream consumers.

The workflow was designed to identify suspect pricing and route exceptions for review.

## Common Exceptions

### Missing Tick

Example:

```text
Bloomberg = Present
Reuters = Missing
```

### Bid / Ask Spread Failure

Example:

```text
Spread exceeds expected threshold
```

### Stale Pricing

Example:

```text
Price has not updated within expected interval
```

### Outlier Movement

Example:

```text
Unexpected price movement
```

## Workflow

```text
Market Data Tick
         ↓
Validation Rules
         ↓
Exception?
      /      \
    No        Yes
    |          |
 Publish   Workflow Queue
                ↓
          Inspector Review
                ↓
          Guardian Approval
                ↓
             Publish
```

## Benchmark Processing

Several times throughout the trading day, benchmark workflows reviewed:

* suspect pricing
* validation exceptions
* missing vendor contributions
* pricing anomalies

## Operational Importance

The workflow helped maintain:

* pricing integrity
* auditability
* operational controls
* consumer confidence

## Related Notes

* [[MRPRICE_FOUR_EYES_CONTROL_MODEL]]
* [[MRPRICE_TICK_CONSOLIDATION_ENGINE]]
* [[MRPRICE_PRODUCTION_SUPPORT]]

