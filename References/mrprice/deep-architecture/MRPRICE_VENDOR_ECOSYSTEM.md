---
type: deep-architecture
status: draft
source: mrprice-docs
categories:
   - "[[MRPrice]]"
   - "[[Market Data]]"
   - "[[Vendor Feeds]]"
tags:
   - mrprice
   - market-data
   - bloomberg
   - trep
   - vendor-feeds
   - normalization
created: 2026-06-10
last: 2026-06-10
origin: chatgpt
---

# MRPrice Vendor Ecosystem

## Purpose

MRPrice consumed fixed-income pricing data from multiple market-data vendors and internal sources. The purpose of the vendor ecosystem was to provide market coverage, pricing comparison, resilience, and validation confidence.

## Vendor Sources

### Bloomberg BPIPE / CBBT

Bloomberg provided enterprise market-data feeds and composite bond pricing data used as part of the pricing input set.

### Reuters / Refinitiv TREP

TREP/RMDS acted as the real-time distribution layer for streaming market-data ticks and instrument subscriptions.

### TMKR

TMKR provided an additional contributor source for pricing comparison and consolidation.

### TWEB

TWEB provided another contributor source used in pricing validation and consolidation.

## Canonical Flow

```text
Bloomberg BPIPE/CBBT
Reuters TREP
TMKR
TWEB
        ↓
Raw Feed Acquisition
        ↓
Vendor Normalization
        ↓
Tick Consolidation
        ↓
Validation Framework
        ↓
Oracle Distribution
        ↓
Consumer Applications
