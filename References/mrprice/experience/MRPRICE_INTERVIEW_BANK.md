---

type: experience
status: draft
source: mrprice-repository
categories:
 - "[[MRPrice]]"
 - "[[Interview Preparation]]"
tags:
 - interview
 - application-support
 - production-support
 - business-analysis
 - market-data

created: 2026-06-10

last: 2026-06-10

origin: chatgpt

---

# MRPrice Interview Bank

## Purpose

This document provides interview-ready talking points based on MRPrice experience.

Use these questions and answers as preparation material for:

* Business Analyst
* Business Systems Analyst
* Application Support
* Production Support
* Market Data Support
* Technical BA
* Cloud Migration

---

# Business Analyst Questions

## Tell me about a large modernization project you supported.

Key Points:

* Technical Refresh initiative
* AC Server to ACPlus evolution
* Reduction of custom code
* Improved maintainability
* Improved supportability
* Cross-team coordination

Primary Story:

* Technical Refresh

---

## Tell me about a project involving changing business requirements.

Key Points:

* Consumer-specific Oracle views
* Different consumer requirements
* Oracle-to-REST evolution
* Data-access modernization

Primary Story:

* Cloud Migration

---

## Describe your experience gathering requirements.

Key Points:

* Consumer data requirements
* Oracle view consumers
* Validation workflows
* Cloud migration planning

---

# Application Support Questions

## Describe an application issue you investigated.

Key Points:

* Missing ticks
* Feed issues
* Pricing anomalies
* Validation failures
* Cross-team troubleshooting

Primary Story:

* Production Support

---

## How do you troubleshoot production problems?

Key Points:

* Review monitoring information
* Verify feed status
* Analyze impacted data
* Determine scope
* Escalate when required
* Coordinate resolution

Primary Story:

* Production Support

---

## Describe your experience supporting business-critical applications.

Key Points:

* Central Bank pricing platform
* Market-data operations
* Daily pricing distribution
* Data-quality validation

Primary Story:

* Production Support

---

# Production Support Questions

## Describe a production incident.

Key Points:

* Missing market-data feed
* Pricing anomaly
* Validation exception
* Operational investigation

Primary Story:

* Production Support

---

## How do you prioritize issues?

Key Points:

* Business impact
* Data impact
* Consumer impact
* Operational risk

---

## What monitoring experience do you have?

Key Points:

* Feed monitoring
* Batch monitoring
* Validation monitoring
* Operational checks

---

# Market Data Questions

## Explain how market data flowed through the platform.

Key Points:

```text
Bloomberg
Reuters TREP
TMKR
TWEB
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

Primary Story:

* Pricing Validation

---

## What is data normalization?

Key Points:

* Vendor field alignment
* CUSIP mapping
* Common data model
* Source independence

Primary Story:

* Tick Consolidation

---

## What is pricing consolidation?

Key Points:

* Multiple vendor inputs
* Single trusted pricing record
* Validation before publication
* Consistent downstream consumption

Primary Story:

* Tick Consolidation

---

# Cloud Migration Questions

## Describe your cloud migration experience.

Key Points:

* Oracle consumer views
* REST API transition
* Service-oriented architecture
* Consumer readiness testing

Primary Story:

* Cloud Migration

---

## Explain the Oracle-to-REST transition.

Key Points:

Legacy:

```text
Oracle Views
      ↓
Applications
```

Modern:

```text
Business Services
      ↓
REST APIs
      ↓
Applications
```

Primary Story:

* Cloud Migration

---

# Governance Questions

## Describe a controlled workflow you supported.

Key Points:

* Inspector
* Guardian
* Four-eyes principle
* Auditability

Primary Story:

* Pricing Validation

---

## What is the four-eyes principle?

Key Points:

* Reviewer ≠ Approver
* Separation of duties
* Risk reduction
* Audit support

Primary Story:

* Pricing Validation

---

# Behavioral Questions

## Tell me about a time you worked across multiple teams.

Primary Story:

* Technical Refresh

---

## Tell me about a time you solved a difficult problem.

Primary Story:

* Production Support

---

## Tell me about a time you improved a process.

Primary Story:

* Technical Refresh

---

## Tell me about a time you worked through ambiguity.

Primary Story:

* Cloud Migration

---

# Best Stories By Role

## Business Analyst

* Technical Refresh
* Cloud Migration

## Application Support

* Production Support
* Pricing Validation

## Production Support

* Production Support
* Pricing Validation

## Market Data Support

* Tick Consolidation
* Pricing Validation

## Technical BA

* Technical Refresh
* Cloud Migration

## Cloud Migration

* Cloud Migration
* Technical Refresh

