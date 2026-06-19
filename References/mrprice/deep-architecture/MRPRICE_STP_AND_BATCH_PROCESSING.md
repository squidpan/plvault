---

type: deep-architecture
status: draft
source: mrprice-docs
categories:

* "[[MRPrice]]"
* "[[Operations]]"
* "[[Production Support]]"
  tags:
* mrprice
* stp
* batch
* cron
* shell-scripts
* operations
* production-support
  created: 2026-06-10
  last: 2026-06-10
  origin: chatgpt

---

# MRPrice STP and Batch Processing

## Purpose

MRPrice operated as a combination of:

* Straight Through Processing (STP)
* Scheduled Batch Processing

The platform was designed to process market-data ticks in near real-time while supporting a variety of scheduled operational activities throughout the business day.

## STP Model

The primary objective of the STP architecture was to minimize latency between incoming vendor market-data ticks and availability of consolidated pricing for consumers.

### Real-Time Flow

```text
Vendor Tick
        ↓
Normalization
        ↓
Consolidation
        ↓
Validation
        ↓
Oracle
        ↓
Consumers
```

The target was to provide consolidated pricing as quickly as possible after market data entered the platform.

## Operational Day

Typical production operations occurred during:

```text
06:00 AM
to
05:00 PM
```

During this period the platform continuously:

* received streaming market data
* consolidated pricing
* validated benchmark data
* processed workflow exceptions
* distributed pricing updates

## Batch Processing

In addition to real-time processing, MRPrice relied on scheduled jobs supporting:

### Security Universe Maintenance

Updating securities eligible for market-data subscriptions.

### Benchmark Processing

Running validation and benchmark generation activities.

### Data Synchronization

Synchronizing reference and pricing information across components.

### Operational Maintenance

Supporting housekeeping and administrative processes.

## Cron-Based Scheduling

Many operational processes were orchestrated through Linux cron scheduling.

Examples included:

```text
MRPRICE_TICKER
MRPRICE_TICKER_FTR
MRPRICE_TICKER_COPS
MRPRICE_TICKER_SPLINE
```

These processes supported various market-data loading, transformation, and distribution functions.

## Shell-Based Processing

The platform contained significant shell scripting components.

Technologies included:

```text
ksh
bash
cron
```

Scripts handled:

* data loading
* orchestration
* monitoring
* exception handling
* operational automation

## Monitoring and Support

Production support responsibilities included:

### Feed Monitoring

Ensuring vendor feeds remained operational.

### Missing Tick Investigation

Investigating situations where expected market data was not received.

### Benchmark Validation Support

Supporting exception workflows and data-quality reviews.

### Incident Resolution

Coordinating issue investigation across:

* business users
* operations
* development teams
* vendor support teams

## Technical Refresh Impact

The Technical Refresh initiative redesigned many shell-based data-load processes.

Goals included:

* reducing complexity
* improving maintainability
* leveraging ACPlus functionality
* reducing custom code
* simplifying operational support

## Business Value

The hybrid STP and batch-processing model provided:

* low-latency pricing distribution
* operational flexibility
* supportability
* resiliency
* scalable processing

## Interview Talking Points

This architecture demonstrates experience with:

* Production Support
* Application Support
* Linux Operations
* Shell Scripting
* Cron Scheduling
* Incident Management
* Market Data Platforms
* Operational Automation
* Enterprise Batch Processing

## Related Notes

* [[MRPRICE_TECHNICAL_REFRESH]]
* [[MRPRICE_TICK_CONSOLIDATION_ENGINE]]
* [[MRPRICE_BENCHMARK_VALIDATION_WORKFLOW]]
* [[MRPRICE_PRODUCTION_SUPPORT]]

