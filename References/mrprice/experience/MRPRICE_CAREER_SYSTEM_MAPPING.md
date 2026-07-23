---

type: experience
status: draft
source: mrprice-repository
categories:
- "[[MRPrice]]"
- "[[Career System]]"

tags:
- career-system
- skills
- resume-generation
- interview-prep
- jd-analysis

created: 2026-06-10

last: 2026-06-10

origin: chatgpt

---

# MRPrice Career System Mapping

## Purpose

This document maps MRPrice knowledge assets into Career System concepts.

The goal is to make MRPrice usable as structured source material for:

* JD analysis
* resume tailoring
* resume generation
* interview preparation
* skill extraction
* role matching

---

# Source Repository

MRPrice Experience Intelligence Repository:

```text
mrprice-experience-intelligence
```

Primary source folders:

```text
References/mrprice/architecture
References/mrprice/deep-architecture
References/mrprice/experience
References/mrprice/diagrams
```

---

# Mapping Model

```text
MRPrice Note
      ↓
Career Skill
      ↓
Resume Evidence
      ↓
JD Match
      ↓
Tailored Resume / Interview Prep
```

---

# Core Skill Mapping

| MRPrice Source                        | Career System Skill    | Resume / Interview Use                             |
| ------------------------------------- | ---------------------- | -------------------------------------------------- |
| MRPRICE_VENDOR_ECOSYSTEM              | Market Data            | Market-data platform experience                    |
| MRPRICE_VENDOR_NORMALIZATION          | Data Integration       | Data mapping, transformation, vendor normalization |
| MRPRICE_TICK_CONSOLIDATION_ENGINE     | Data Quality           | Consolidated pricing, CUSIP alignment              |
| MRPRICE_BENCHMARK_VALIDATION_WORKFLOW | Data Validation        | Benchmark checks, exception handling               |
| MRPRICE_FOUR_EYES_CONTROL_MODEL       | Governance / Controls  | Auditability, workflow controls                    |
| MRPRICE_ORACLE_DISTRIBUTION           | Oracle / SQL           | Consumer views, pricing distribution               |
| MRPRICE_STP_AND_BATCH_PROCESSING      | Production Support     | Cron, shell, operations support                    |
| MRPRICE_TECHNICAL_REFRESH             | Modernization          | Technical refresh, OOB adoption                    |
| MRPRICE_CLOUD_MIGRATION               | Cloud Migration        | Oracle-to-REST, API modernization                  |
| MRPRICE_MODERNIZATION_JOURNEY         | Architecture Evolution | Legacy-to-cloud narrative                          |

---

# Resume Family Mapping

## Business Analyst / BSA

Use these MRPrice sources:

* MRPRICE_TECHNICAL_REFRESH
* MRPRICE_CLOUD_MIGRATION
* MRPRICE_MODERNIZATION_JOURNEY
* MRPRICE_ORACLE_DISTRIBUTION
* MRPRICE_RESUME_EVIDENCE

Career System emphasis:

* requirements
* UAT
* stakeholder management
* data mapping
* consumer requirements
* migration validation

---

## Application Support

Use these MRPrice sources:

* MRPRICE_PRODUCTION_SUPPORT
* MRPRICE_STP_AND_BATCH_PROCESSING
* MRPRICE_BENCHMARK_VALIDATION_WORKFLOW
* MRPRICE_TICK_CONSOLIDATION_ENGINE
* MRPRICE_INTERVIEW_BANK

Career System emphasis:

* production support
* troubleshooting
* incident coordination
* validation
* Oracle/Linux environment

---

## Production Support

Use these MRPrice sources:

* MRPRICE_STP_AND_BATCH_PROCESSING
* MRPRICE_VENDOR_ECOSYSTEM
* MRPRICE_TICK_CONSOLIDATION_ENGINE
* MRPRICE_BENCHMARK_VALIDATION_WORKFLOW
* MRPRICE_STAR_STORIES

Career System emphasis:

* operational monitoring
* market-data feeds
* missing tick investigation
* support runbooks
* escalation

---

## Market Data Support

Use these MRPrice sources:

* MRPRICE_VENDOR_ECOSYSTEM
* MRPRICE_VENDOR_NORMALIZATION
* MRPRICE_TREP_INTEGRATION
* MRPRICE_TICK_CONSOLIDATION_ENGINE

Career System emphasis:

* Bloomberg
* Reuters/TREP
* fixed-income pricing
* CUSIP alignment
* vendor normalization

---

## Cloud Migration / Technical BA

Use these MRPrice sources:

* MRPRICE_CLOUD_MIGRATION
* MRPRICE_CLOUD_TARGET_ARCHITECTURE
* MRPRICE_MODERNIZATION_JOURNEY
* MRPRICE_TECHNICAL_REFRESH

Career System emphasis:

* Oracle-to-REST migration
* API payload validation
* service-oriented architecture
* modernization roadmap

---

# JD Keyword Mapping

## If JD Mentions "Production Support"

Use:

* MRPRICE_STP_AND_BATCH_PROCESSING
* MRPRICE_PRODUCTION_SUPPORT
* MRPRICE_BENCHMARK_VALIDATION_WORKFLOW

Resume evidence:

* feed monitoring
* incident investigation
* operational checks
* exception workflows

---

## If JD Mentions "Application Support"

Use:

* MRPRICE_PRODUCTION_SUPPORT
* MRPRICE_ORACLE_DISTRIBUTION
* MRPRICE_STP_AND_BATCH_PROCESSING

Resume evidence:

* Linux / Oracle platform support
* cross-team escalation
* data validation
* troubleshooting

---

## If JD Mentions "Business Analyst"

Use:

* MRPRICE_TECHNICAL_REFRESH
* MRPRICE_CLOUD_MIGRATION
* MRPRICE_MODERNIZATION_JOURNEY

Resume evidence:

* requirements analysis
* migration validation
* stakeholder coordination
* UAT

---

## If JD Mentions "Market Data"

Use:

* MRPRICE_VENDOR_ECOSYSTEM
* MRPRICE_TREP_INTEGRATION
* MRPRICE_TICK_CONSOLIDATION_ENGINE

Resume evidence:

* Bloomberg
* Reuters/TREP
* vendor feeds
* pricing consolidation
* fixed income

---

## If JD Mentions "Data Quality"

Use:

* MRPRICE_BENCHMARK_VALIDATION_WORKFLOW
* MRPRICE_TICK_CONSOLIDATION_ENGINE
* MRPRICE_FOUR_EYES_CONTROL_MODEL

Resume evidence:

* missing tick checks
* validation rules
* exception handling
* governance workflows

---

## If JD Mentions "Cloud Migration" or "REST APIs"

Use:

* MRPRICE_CLOUD_MIGRATION
* MRPRICE_CLOUD_TARGET_ARCHITECTURE
* MRPRICE_MODERNIZATION_JOURNEY
* MRPRICE_ORACLE_DISTRIBUTION

Resume evidence:

* Oracle view to REST payload mapping
* API validation
* service-oriented access model
* consumer migration

---

# Career System Integration Notes

Future Career System should be able to consume this repository as:

```text
experience_source: mrprice
source_repo: mrprice-experience-intelligence
source_type: architecture_and_experience
```

Potential future tables or JSON objects:

```text
experience_stories
experience_skills
resume_evidence
interview_answers
architecture_patterns
```

---

# Suggested Career System Usage

For each JD:

1. Extract JD keywords.
2. Match JD keywords to MRPrice source notes.
3. Pull matching resume evidence.
4. Pull matching STAR stories.
5. Generate tailored resume.
6. Generate interview prep package.

---

# Highest-Value MRPrice Evidence

Top reusable evidence areas:

1. Technical Refresh
2. Cloud Migration
3. Market Data Platform Support
4. Oracle Distribution
5. Tick Consolidation
6. Benchmark Validation
7. Four-Eyes Governance
8. Production Support
9. Vendor Normalization
10. Oracle-to-REST API Modernization

---

# Related Notes

* [[MRPRICE_SKILLS_MAPPING]]
* [[MRPRICE_RESUME_EVIDENCE]]
* [[MRPRICE_STAR_STORIES]]
* [[MRPRICE_INTERVIEW_BANK]]

