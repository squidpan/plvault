---

type: experience
status: draft
source: mrprice-repository
categories:
- "[[MRPrice]]"
- "[[Resume Evidence]]"
tags:
- resume
- evidence
- market-data
- application-support
- production-support
- business-analysis
created: 2026-06-10
last: 2026-06-10
origin: chatgpt

---

# MRPrice Resume Evidence

## Purpose

This document converts MRPrice architecture and operations knowledge into reusable resume evidence.

The goal is to support tailored resumes for Business Analyst, Business Systems Analyst, Application Support, Production Support, Market Data Support, and Technical BA roles.

---

# Core Positioning Statement

Senior Business Analyst and Application Support professional with experience supporting a Central Bank market-data pricing platform across technical refresh, production support, data validation, Oracle distribution, and cloud migration initiatives.

---

# High-Value Evidence Areas

## 1. Market Data Platform Support

Evidence:

* Supported centralized fixed-income pricing platform.
* Platform consumed market-data feeds from Bloomberg, Reuters/TREP, TMKR, and TWEB.
* Pricing data was normalized, consolidated, validated, and distributed to downstream consumers.

Resume Bullet:

* Supported enterprise market-data pricing platform that normalized, validated, consolidated, and distributed fixed-income pricing from Bloomberg, Reuters/TREP, and other vendor feeds to downstream consumers.

Related Notes:

* [[MRPRICE_VENDOR_ECOSYSTEM]]
* [[MRPRICE_VENDOR_NORMALIZATION]]
* [[MRPRICE_TICK_CONSOLIDATION_ENGINE]]

---

## 2. Tick Consolidation and Data Quality

Evidence:

* Vendor feeds were aligned to common security identifiers such as CUSIP.
* Consolidation logic produced a trusted pricing view from multiple vendor contributors.
* Validation identified missing ticks, stale prices, bid/ask spread issues, and outliers.

Resume Bullet:

* Supported pricing-data quality processes including vendor tick validation, CUSIP alignment, exception review, and consolidated price distribution.

Related Notes:

* [[MRPRICE_TICK_CONSOLIDATION_ENGINE]]
* [[MRPRICE_BENCHMARK_VALIDATION_WORKFLOW]]

---

## 3. Oracle Distribution and Consumer Views

Evidence:

* MRPRICE_TICKER served as the master pricing view for Treasury pricing.
* Consumer-specific views such as MRPRICE_TICKER_FTR, MRPRICE_TICKER_COPS, and MRPRICE_TICKER_SPLINE provided tailored data access for downstream applications.
* These Oracle views later informed REST API payload design.

Resume Bullet:

* Supported Oracle-based pricing distribution model using master and consumer-specific views, enabling downstream systems to consume validated Treasury pricing data.

Resume Bullet:

* Helped validate the transition from Oracle consumer views to REST API payloads during cloud migration planning and testing.

Related Notes:

* [[MRPRICE_ORACLE_DISTRIBUTION]]
* [[MRPRICE_MODERNIZATION_JOURNEY]]
* [[MRPRICE_CLOUD_MIGRATION]]

---

## 4. Technical Refresh

Evidence:

* Technical Refresh moved the platform from legacy AC Server patterns toward ACPlus.
* The initiative reduced custom code and leveraged OOB functionality.
* Legacy shell-based processing and data loads were redesigned.

Resume Bullet:

* Supported technical refresh initiative that reduced custom code, leveraged ACPlus out-of-box functionality, and redesigned legacy shell-based data-load processes to improve maintainability and supportability.

Related Notes:

* [[MRPRICE_TECHNICAL_REFRESH]]
* [[MRPRICE_MODERNIZATION_JOURNEY]]
* [[MRPRICE_STP_AND_BATCH_PROCESSING]]

---

## 5. Cloud Migration

Evidence:

* Legacy consumer access depended heavily on Oracle tables and views.
* Cloud migration introduced REST APIs, business services, and service-oriented access patterns.
* Oracle view outputs were mapped to REST API payloads.

Resume Bullet:

* Supported cloud migration initiative by validating REST API payloads against Oracle source views and helping ensure data quality, consumer readiness, and migration confidence.

Resume Bullet:

* Participated in modernization effort moving pricing distribution from direct Oracle view consumption toward service-based REST API access.

Related Notes:

* [[MRPRICE_CLOUD_MIGRATION]]
* [[MRPRICE_CLOUD_TARGET_ARCHITECTURE]]
* [[MRPRICE_MODERNIZATION_JOURNEY]]

---

## 6. Production Support and Operations

Evidence:

* Platform processed streaming market data during the business day.
* Operations included cron scheduling, shell scripting, monitoring, and exception handling.
* Support work included feed checks, missing tick investigation, validation support, and issue coordination.

Resume Bullet:

* Provided production support for Linux/Oracle market-data platform, including feed monitoring, data validation, incident investigation, operational checks, and cross-team escalation.

Related Notes:

* [[MRPRICE_STP_AND_BATCH_PROCESSING]]
* [[MRPRICE_PRODUCTION_SUPPORT]]
* [[MRPRICE_MARKET_DATA_PIPELINE]]

---

## 7. Governance and Four-Eyes Controls

Evidence:

* Pricing exceptions flowed through Inspector / Guardian review.
* Four-eyes controls prevented the same user from both proposing and approving pricing changes.
* Workflow supported auditability and operational governance.

Resume Bullet:

* Supported controlled price-cleansing workflows using four-eyes review, exception queues, and audit-ready approval processes to maintain pricing integrity.

Related Notes:

* [[MRPRICE_FOUR_EYES_CONTROL_MODEL]]
* [[MRPRICE_BENCHMARK_VALIDATION_WORKFLOW]]

---

# Role-Specific Resume Angles

## Business Analyst / BSA

Emphasize:

* requirements
* UAT
* consumer data needs
* Oracle view to REST payload mapping
* stakeholder communication

## Application Support

Emphasize:

* production support
* incident investigation
* validation workflows
* Oracle/Linux environment
* ServiceNow/runbook style operations

## Market Data Support

Emphasize:

* Bloomberg
* Reuters/TREP
* tick processing
* CUSIP mapping
* pricing consolidation

## Cloud Migration / Technical BA

Emphasize:

* Oracle to REST migration
* API payload validation
* service-oriented distribution
* modernization journey

---

# Claims To Avoid

Do not overstate:

* direct AI engineering
* ownership of the full architecture
* direct development of ACPlus internals
* direct ownership of all vendor feed infrastructure
* production ownership of Kafka/PostgreSQL/Cassandra unless supported by specific experience

---

# Best Reusable Summary

Supported a Central Bank fixed-income market-data pricing platform through technical refresh, production support, Oracle distribution, data validation, and cloud migration initiatives, helping normalize and consolidate vendor pricing feeds, support controlled price-cleansing workflows, and validate the transition from Oracle views to REST API payloads.

