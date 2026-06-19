---

type: deep-architecture
status: draft
source: mrprice-docs
categories:

* "[[MRPrice]]"
* "[[Modernization]]"
* "[[Architecture]]"
  tags:
* modernization
* technical-refresh
* cloud-migration
* acplus
* alveo
* architecture
  created: 2026-06-10
  last: 2026-06-10
  origin: chatgpt

---

# MRPrice Modernization Journey

## Overview

MRPrice evolved through multiple architectural generations.

The platform transitioned from a heavily customized on-premise market-data platform toward a modern service-oriented cloud architecture.

## Phase 1 — Legacy Platform

### Characteristics

```text
AC Server
Custom Code
Oracle Distribution
Shell Scripts
Consumer-Specific Views
```

The platform relied heavily on custom operational processes and custom integrations.

### Distribution Model

```text
MRPRICE_TICKER
        ↓
MRPRICE_TICKER_FTR
MRPRICE_TICKER_COPS
MRPRICE_TICKER_SPLINE
        ↓
Consumer Applications
```

Consumer applications accessed pricing through Oracle views designed specifically for their requirements.

---

## Phase 2 — Technical Refresh

### Objective

Modernize the platform while remaining on-premise.

### Key Goals

* reduce custom code
* leverage ACPlus OOB functionality
* improve maintainability
* simplify support
* standardize workflows

### Major Changes

```text
AC Server
      ↓
ACPlus
```

### Data Load Redesign

A significant portion of the Technical Refresh initiative focused on redesigning legacy shell-based processing and data-load architecture.

Benefits included:

* reduced operational complexity
* improved maintainability
* improved supportability

### Personal Contribution

Technical Refresh represented approximately two-thirds of the user's MRPrice project work.

---

## Phase 3 — Cloud Migration

### Objective

Transition toward cloud-native and service-oriented architecture.

### Architectural Shift

Legacy:

```text
Oracle Views
       ↓
Applications
```

Target:

```text
REST APIs
       ↓
Applications
```

### Consumer Access Evolution

Legacy Consumer View:

```text
MRPRICE_TICKER_COPS
```

Modern Equivalent:

```text
REST Endpoint
```

Both provide consumer-specific access to pricing data.

The primary difference is the delivery mechanism.

### Roadmap Components

* Alveo
* Kafka
* PostgreSQL
* Cassandra
* REST APIs
* Service Layer

---

## Transformation Summary

```text
Legacy Platform
        ↓
Technical Refresh
        ↓
ACPlus
        ↓
Cloud Migration
        ↓
Modern Services
```

## Interview Talking Points

This journey demonstrates experience with:

* legacy modernization
* technical refresh initiatives
* cloud migration
* architecture evolution
* operational transformation
* API-based modernization

## Related Notes

* [[MRPRICE_TECHNICAL_REFRESH]]
* [[MRPRICE_CLOUD_MIGRATION]]
* [[MRPRICE_ORACLE_DISTRIBUTION]]
* [[MRPRICE_STP_AND_BATCH_PROCESSING]]

