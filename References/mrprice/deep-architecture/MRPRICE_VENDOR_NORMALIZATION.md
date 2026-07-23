---

type: deep-architecture
status: draft
source: mrprice-docs
categories:
 - "[[MRPrice]]"
 - "[[Market Data]]"
 - "[[Normalization]]"
tags:
 - mrprice
 - normalization
 - market-data
 - bloomberg
 - trep
 - cusip

created: 2026-06-10
last: 2026-06-10
origin: chatgpt

---

# MRPrice Vendor Normalization

## Purpose

MRPrice received pricing information from multiple market-data vendors and internal sources.

Each vendor represented securities, prices, timestamps, and metadata differently.

Before pricing could be consolidated and validated, vendor data needed to be transformed into a common internal representation.

This process was known as Vendor Normalization.

## Problem Statement

Different vendors supplied pricing information using different:

* field names
* identifiers
* timestamps
* update frequencies
* pricing conventions
* metadata structures

Without normalization, downstream processing would require vendor-specific logic.

## Vendor Sources

### Bloomberg

Sources included:

* BPIPE
* CBBT

### Refinitiv

Sources included:

* TREP
* RMDS

### Additional Sources

* TMKR
* TWEB

## Normalization Objectives

### Security Alignment

Map vendor-specific identifiers to a common internal security record.

Primary security identifier:

```text
CUSIP
```

### Field Standardization

Example:

Vendor A

```text
BidPrice
AskPrice
SecurityID
```

Vendor B

```text
Bid
Offer
CUSIP
```

Internal Representation

```text
CUSIP
Bid
Ask
Timestamp
Source
```

### Timestamp Alignment

Normalize timestamps to a consistent internal format.

### Source Tracking

Preserve source attribution for:

* auditability
* validation
* troubleshooting
* exception analysis

## Processing Flow

```text
Vendor Feed
        ↓
Raw Tick
        ↓
Normalization
        ↓
CUSIP Mapping
        ↓
Standard Internal Record
        ↓
Consolidation Engine
```

## Relationship to Consolidation

Normalization occurs before consolidation.

The Consolidation Engine expects a common data model regardless of vendor source.

```text
Bloomberg
Reuters
TMKR
TWEB
        ↓
Normalization
        ↓
Consolidation
        ↓
Validation
        ↓
Oracle Distribution
```

## Operational Importance

Normalization helped ensure:

* consistent pricing logic
* reduced complexity
* easier troubleshooting
* improved data quality
* vendor independence

## Interview Talking Points

This architecture demonstrates experience with:

* market-data systems
* data integration
* data transformation
* identifier mapping
* data quality controls
* enterprise integration patterns

## Related Notes

* [[MRPRICE_VENDOR_ECOSYSTEM]]
* [[MRPRICE_TICK_CONSOLIDATION_ENGINE]]
* [[MRPRICE_BENCHMARK_VALIDATION_WORKFLOW]]
* [[MRPRICE_MARKET_DATA_PIPELINE]]

