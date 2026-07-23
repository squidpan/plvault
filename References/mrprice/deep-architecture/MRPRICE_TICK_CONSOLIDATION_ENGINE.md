---

type: deep-architecture
status: draft
source: mrprice-docs
categories:

  - "[[MRPrice]]"
  - "[[Market Data]]"
  - "[[Pricing Engine]]"
tags:
  - mrprice
  - market-data
  - consolidation
  - pricing
  - cusip
  - fixed-income

created: 2026-06-10
last: 2026-06-10
origin: chatgpt

---

# MRPrice Tick Consolidation Engine

## Purpose

The Tick Consolidation Engine was responsible for transforming multiple vendor-specific market-data feeds into a single trusted pricing record for each security.

The objective was not simply to distribute vendor prices but to create a consolidated market view that could be consumed consistently across the Central Bank.

## Input Sources

### Bloomberg

* BPIPE
* CBBT

### Refinitiv

* TREP
* RMDS

### Additional Sources

* TMKR
* TWEB

## Processing Flow

```text
Vendor Tick
        ↓
Normalization
        ↓
Security Mapping
        ↓
Consolidation Rules
        ↓
Validation
        ↓
Consolidated CUSIP Record
```

## Security Identifier

The primary business key was:

```text
CUSIP
```

All vendor data was aligned to a common security identifier before consolidation.

## Consolidated Pricing Record

Typical fields included:

```text
CUSIP
Bid
Ask
Mid
Timestamp
Source Indicators
Validation Status
```

## Latency Goal

MRPrice operated as a near real-time platform.

Once market-data ticks arrived through TREP and related feed handlers, consolidated pricing was expected to become available to consumers with minimal delay.

## Business Value

Benefits included:

* Single source of truth
* Consistent pricing
* Reduced vendor dependency
* Simplified downstream integration
* Improved data quality

## Related Notes

* [[MRPRICE_VENDOR_NORMALIZATION]]
* [[MRPRICE_VENDOR_ECOSYSTEM]]
* [[MRPRICE_ORACLE_DISTRIBUTION]]
* [[MRPRICE_BENCHMARK_VALIDATION_WORKFLOW]]

