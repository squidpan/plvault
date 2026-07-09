---
categories:
  - "[[Processes]]"
type:
description: "chatgpt summary F: CA Operations experience source"
source: chatgpt-manual
tags:
created: 2026-07-07
last: 2026-07-07
status:
origin:
run_id:
input_prompt:
---
---
Yes. Start with **v0.5.0 Career System Experience Source Domain Model**.

Core idea:

```text
JD
 ↓
required skills / role signals
 ↓
Experience Source
 ↓
Experience Assets
 ↓
Resume Evidence / STAR Stories / Interview Prep
```

Create this next:

```bash
cd ~/pjs/repos/career-system

mkdir -p docs/architecture
vi docs/architecture/experience-source-domain-model.md
```

Recommended domain objects:

```text
ExperienceSource
- source_id
- name
- repo
- version
- status
- domains
- asset_index

ExperienceAsset
- asset_id
- source_id
- asset_type
- title
- path
- tags
- role_families
- skill_ids

ExperienceSkill
- skill_id
- name
- source_id
- evidence_paths
- jd_keywords

ResumeEvidence
- evidence_id
- source_id
- skill_ids
- resume_family
- bullet_text
- claims_to_avoid

InterviewStory
- story_id
- source_id
- story_type
- linked_skills
- linked_roles
- star_summary
```

Initial schema folders:

```text
data/experience-sources/
  mrprice-experience-source.json

data/experience-assets/
  mrprice-assets-index.json

data/experience-skills/
  mrprice-skills.json

data/resume-evidence/
  mrprice-resume-evidence.json

data/interview-stories/
  mrprice-interview-stories.json
```

First design rule:

```text
Career System should not copy the whole MRPrice repo.

It should reference MRPrice as an external source and maintain structured indexes/summaries inside Career System.
```

This keeps responsibilities clean:

```text
mrprice-experience-intelligence = source knowledge
career-system = matching / scoring / resume generation
```

Next step: write `docs/architecture/experience-source-domain-model.md`, then commit it as the v0.5.0 design foundation.

---

>[!Prompt]
>let's write docs/architecture/experience-source-domain-model.md, then commit it as the v0.5.0 design foundation.


---

ChatGPT

This will be the design anchor for how Career System consumes MRPrice and future experience repos without copying their full contents. After this, we can add JSON schemas/index files against the model.

ChatGPT

Create/open the file:

```bash
cd ~/pjs/repos/career-system

mkdir -p docs/architecture

vi docs/architecture/experience-source-domain-model.md
```

Paste this:

:::writing{variant="document" id="68440"}
# Experience Source Domain Model

## Purpose

This document defines the Career System domain model for external experience repositories.

Experience Sources allow Career System to use structured professional experience as evidence for:

- JD analysis
- candidate matching
- resume tailoring
- resume generation
- interview preparation
- skill extraction

The first implemented Experience Source is:

```text
mrprice-experience-intelligence
```

---

# Design Principle

Career System should not copy the full contents of external experience repositories.

Instead, Career System should maintain structured references, indexes, summaries, and mappings that point to the source repository.

```text
Experience Repository
        ↓
Career System Index
        ↓
JD Matching
        ↓
Resume Evidence
        ↓
Resume / Interview Output
```

This keeps responsibilities clean:

```text
mrprice-experience-intelligence
    = source knowledge

career-system
    = matching, scoring, tailoring, generation
```

---

# Core Domain Objects

## 1. ExperienceSource

Represents an external repository or knowledge source containing structured professional experience.

### Fields

```text
source_id
name
source_type
repository_name
repository_path
repository_url
branch
release
status
domains
primary_assets
notes
```

### Example

```json
{
  "source_id": "mrprice",
  "name": "MRPrice Experience Intelligence",
  "source_type": "experience_repository",
  "repository_name": "mrprice-experience-intelligence",
  "branch": "main",
  "release": "v0.4.1",
  "status": "active"
}
```

---

## 2. ExperienceAsset

Represents a specific reusable asset inside an Experience Source.

Examples:

- Resume evidence file
- STAR story file
- Interview bank
- Skills mapping
- Architecture note
- Diagram
- Deep architecture note

### Fields

```text
asset_id
source_id
asset_type
title
path
tags
domains
role_families
skill_ids
priority
status
```

### Asset Types

```text
architecture_note
deep_architecture_note
resume_evidence
star_story
interview_bank
skills_mapping
career_system_mapping
diagram
```

---

## 3. ExperienceSkill

Represents a skill derived from an Experience Source.

Examples:

- Market Data
- Vendor Normalization
- Tick Consolidation
- Oracle Distribution
- REST API Validation
- Production Support
- Four-Eyes Governance

### Fields

```text
skill_id
source_id
name
category
description
evidence_assets
jd_keywords
resume_families
confidence
status
```

---

## 4. ResumeEvidence

Represents reusable resume material derived from an Experience Source.

### Fields

```text
evidence_id
source_id
title
summary
resume_family
role_families
skill_ids
bullet_text
supporting_assets
claims_to_avoid
status
```

### Resume Families

```text
business_analyst
business_systems_analyst
application_support
production_support
market_data_support
technical_ba
cloud_migration
operations
```

---

## 5. InterviewStory

Represents an interview-ready STAR or story asset.

### Fields

```text
story_id
source_id
title
story_type
situation
task
actions
result
themes
linked_skills
linked_roles
supporting_assets
status
```

### Story Types

```text
technical_refresh
cloud_migration
production_support
data_quality
governance
market_data_operations
```

---

## 6. InterviewPromptMapping

Maps likely interview questions to stories and evidence.

### Fields

```text
prompt_id
question
role_family
source_id
recommended_story_ids
recommended_evidence_ids
talking_points
status
```

---

## 7. JDExperienceMatch

Represents the relationship between a JD and relevant Experience Source evidence.

### Fields

```text
match_id
jd_id
source_id
matched_skills
matched_assets
matched_resume_evidence
matched_interview_stories
fit_notes
risk_notes
status
```

---

# Folder Strategy

## Existing

```text
data/experience-sources/
  mrprice-experience-source.json
```

## Proposed

```text
data/experience-assets/
  mrprice-assets-index.json

data/experience-skills/
  mrprice-skills.json

data/resume-evidence/
  mrprice-resume-evidence.json

data/interview-stories/
  mrprice-interview-stories.json

data/interview-prompts/
  mrprice-interview-prompts.json

data/jd-experience-matches/
```

---

# MRPrice Initial Source Mapping

## Experience Source

```text
source_id: mrprice
repo: mrprice-experience-intelligence
release: v0.4.1
status: active
```

## Primary Assets

```text
MRPRICE_SKILLS_MAPPING
MRPRICE_RESUME_EVIDENCE
MRPRICE_STAR_STORIES
MRPRICE_INTERVIEW_BANK
MRPRICE_CAREER_SYSTEM_MAPPING
```

## Primary Domains

```text
market-data
production-support
application-support
business-analysis
technical-refresh
cloud-migration
data-quality
oracle
linux
rest-api
governance
```

---

# JD Keyword Mapping Concept

Career System should map JD language to Experience Source assets.

## Example

JD mentions:

```text
production support
incident investigation
Oracle
Linux
```

Career System should match:

```text
source_id: mrprice

assets:
- MRPRICE_STP_AND_BATCH_PROCESSING
- MRPRICE_PRODUCTION_SUPPORT
- MRPRICE_RESUME_EVIDENCE
- MRPRICE_INTERVIEW_BANK

resume evidence:
- production support for Linux/Oracle market-data platform
- feed monitoring
- incident investigation
- operational checks

interview stories:
- Production Support and Market Data Operations
```

---

# Resume Generation Concept

Current path:

```text
JD
  ↓
Resume Tailoring
  ↓
Resume Generation
```

Target path:

```text
JD
  ↓
Skill Extraction
  ↓
Experience Source Matching
  ↓
Resume Evidence Selection
  ↓
Resume Tailoring
  ↓
Resume Generation
```

---

# Interview Preparation Concept

Target path:

```text
JD
  ↓
Role Family Detection
  ↓
Experience Source Matching
  ↓
STAR Story Selection
  ↓
Interview Bank Selection
  ↓
Interview Prep Package
```

---

# Design Boundary

Career System owns:

- indexes
- matching logic
- scoring
- resume tailoring
- resume generation
- interview package generation

Experience Source repositories own:

- raw experience knowledge
- architecture notes
- stories
- evidence
- diagrams
- source context

---

# Initial Implementation Plan

## v0.5.0

Design Experience Source domain model.

Deliverables:

```text
docs/architecture/experience-source-domain-model.md
```

## v0.5.1

Create MRPrice structured indexes.

Deliverables:

```text
data/experience-assets/mrprice-assets-index.json
data/experience-skills/mrprice-skills.json
data/resume-evidence/mrprice-resume-evidence.json
data/interview-stories/mrprice-interview-stories.json
```

## v0.5.2

Create matching rules.

Deliverables:

```text
data/experience-matching/mrprice-keyword-map.json
docs/architecture/experience-matching-strategy.md
```

## v0.5.3

Integrate with resume tailoring.

Deliverables:

```text
updated resume-tailoring workflow
MRPrice evidence-aware tailoring output
```

---

# Open Questions

## Path References

Should Career System store absolute local paths, repo-relative paths, or logical Obsidian links?

Recommendation:

Use repo-relative paths plus source repository metadata.

## Source Sync

Should Career System copy source summaries or read directly from the MRPrice repository?

Recommendation:

Use structured summaries and indexes in Career System. Do not copy full source notes.

## Skills Repository Integration

Should skills be generated inside Career System or Obsidian Skills NG?

Recommendation:

Generate structured skill objects in Career System first. Later export or sync selected skills into Obsidian Skills NG.

---

# Summary

Experience Sources make Career System more powerful by connecting job descriptions to actual professional evidence.

MRPrice is the first Experience Source.

The model can later support additional experience repositories such as:

- AIG
- Thomson Reuters
- EmblemHealth
- Central Bank projects
- Motorweb proof-of-concept work
:::

Then commit:

```bash
git add docs/architecture/experience-source-domain-model.md

git commit -m "Add experience source domain model v0.5.0"

git push
```

Optionally tag:

```bash
git tag v0.5.0-experience-source-domain-model

git push origin v0.5.0-experience-source-domain-model
```

---

ChatGPT

Excellent. Career System now has a tagged v0.5.0 design foundation.

```text
5099ed0  Add experience source domain model v0.5.0
tag      v0.5.0-experience-source-domain-model
```

Next logical step:

```text
v0.5.1
MRPrice structured indexes
```

Create:

```text
data/experience-assets/mrprice-assets-index.json
data/experience-skills/mrprice-skills.json
data/resume-evidence/mrprice-resume-evidence.json
data/interview-stories/mrprice-interview-stories.json
```

This turns the domain model into actual Career System data.

I’d do `mrprice-assets-index.json` first, because every later file points back to assets.

user

ok do mrprice-assets-index.json

ChatGPT

Good. This is the first file that turns the domain model into actual structured data.

Create:

```bash
mkdir -p data/experience-assets

vi data/experience-assets/mrprice-assets-index.json
```

Paste:

```json
{
  "source_id": "mrprice",
  "source_name": "MRPrice Experience Intelligence",
  "source_release": "v0.4.1",
  "source_status": "active",

  "asset_count": 18,

  "assets": [

    {
      "asset_id": "mrprice_vendor_ecosystem",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_VENDOR_ECOSYSTEM",
      "path": "References/mrprice/deep-architecture/MRPRICE_VENDOR_ECOSYSTEM.md",
      "domains": ["market-data"],
      "role_families": ["market_data_support", "application_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_vendor_normalization",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_VENDOR_NORMALIZATION",
      "path": "References/mrprice/deep-architecture/MRPRICE_VENDOR_NORMALIZATION.md",
      "domains": ["data-quality", "data-integration"],
      "role_families": ["business_analyst", "market_data_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_tick_consolidation",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_TICK_CONSOLIDATION_ENGINE",
      "path": "References/mrprice/deep-architecture/MRPRICE_TICK_CONSOLIDATION_ENGINE.md",
      "domains": ["market-data", "data-quality"],
      "role_families": ["market_data_support", "production_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_validation_workflow",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_BENCHMARK_VALIDATION_WORKFLOW",
      "path": "References/mrprice/deep-architecture/MRPRICE_BENCHMARK_VALIDATION_WORKFLOW.md",
      "domains": ["data-quality", "governance"],
      "role_families": ["application_support", "production_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_four_eyes",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_FOUR_EYES_CONTROL_MODEL",
      "path": "References/mrprice/deep-architecture/MRPRICE_FOUR_EYES_CONTROL_MODEL.md",
      "domains": ["governance"],
      "role_families": ["business_analyst", "application_support"],
      "priority": "medium"
    },

    {
      "asset_id": "mrprice_stp_batch",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_STP_AND_BATCH_PROCESSING",
      "path": "References/mrprice/deep-architecture/MRPRICE_STP_AND_BATCH_PROCESSING.md",
      "domains": ["production-support", "operations"],
      "role_families": ["production_support", "application_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_modernization_journey",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_MODERNIZATION_JOURNEY",
      "path": "References/mrprice/deep-architecture/MRPRICE_MODERNIZATION_JOURNEY.md",
      "domains": ["modernization", "cloud-migration"],
      "role_families": ["business_analyst", "technical_ba"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_resume_evidence",
      "asset_type": "resume_evidence",
      "title": "MRPRICE_RESUME_EVIDENCE",
      "path": "References/mrprice/experience/MRPRICE_RESUME_EVIDENCE.md",
      "domains": ["resume"],
      "role_families": [
        "business_analyst",
        "application_support",
        "production_support",
        "market_data_support"
      ],
      "priority": "critical"
    },

    {
      "asset_id": "mrprice_star_stories",
      "asset_type": "star_story",
      "title": "MRPRICE_STAR_STORIES",
      "path": "References/mrprice/experience/MRPRICE_STAR_STORIES.md",
      "domains": ["interview"],
      "role_families": [
        "business_analyst",
        "application_support",
        "production_support"
      ],
      "priority": "critical"
    },

    {
      "asset_id": "mrprice_interview_bank",
      "asset_type": "interview_bank",
      "title": "MRPRICE_INTERVIEW_BANK",
      "path": "References/mrprice/experience/MRPRICE_INTERVIEW_BANK.md",
      "domains": ["interview"],
      "role_families": [
        "business_analyst",
        "application_support",
        "production_support",
        "market_data_support"
      ],
      "priority": "critical"
    },

    {
      "asset_id": "mrprice_skills_mapping",
      "asset_type": "skills_mapping",
      "title": "MRPRICE_SKILLS_MAPPING",
      "path": "References/mrprice/experience/MRPRICE_SKILLS_MAPPING.md",
      "domains": ["skills"],
      "role_families": ["all"],
      "priority": "critical"
    },

    {
      "asset_id": "mrprice_career_system_mapping",
      "asset_type": "career_system_mapping",
      "title": "MRPRICE_CAREER_SYSTEM_MAPPING",
      "path": "References/mrprice/experience/MRPRICE_CAREER_SYSTEM_MAPPING.md",
      "domains": ["career-system"],
      "role_families": ["all"],
      "priority": "critical"
    }
  ]
}
```

Then:

```bash
git add data/experience-assets/mrprice-assets-index.json

git commit -m "Add MRPrice asset index"

git push
```

### Why this file matters

This becomes the central registry:

```text
Experience Source
        ↓
Asset Index
        ↓
Skills
Resume Evidence
Interview Stories
JD Matching
```

Once this is committed, the next file (`mrprice-skills.json`) becomes much easier because every skill can point back to one or more asset IDs instead of raw note names.

...

```
* [new tag] v0.5.0-experience-source-domain-model -> v0.5.0-experience-source-domain-model

```


---

ChatGPT

Excellent. Career System now has a tagged v0.5.0 design foundation.

```text
5099ed0  Add experience source domain model v0.5.0
tag      v0.5.0-experience-source-domain-model
```

Next logical step:

```text
v0.5.1
MRPrice structured indexes
```

Create:

```text
data/experience-assets/mrprice-assets-index.json
data/experience-skills/mrprice-skills.json
data/resume-evidence/mrprice-resume-evidence.json
data/interview-stories/mrprice-interview-stories.json
```

This turns the domain model into actual Career System data.

I’d do `mrprice-assets-index.json` first, because every later file points back to assets.

---

hatGPT

Good. This is the first file that turns the domain model into actual structured data.

Create:

```bash
mkdir -p data/experience-assets

vi data/experience-assets/mrprice-assets-index.json
```

Paste:

```json
{
  "source_id": "mrprice",
  "source_name": "MRPrice Experience Intelligence",
  "source_release": "v0.4.1",
  "source_status": "active",

  "asset_count": 18,

  "assets": [

    {
      "asset_id": "mrprice_vendor_ecosystem",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_VENDOR_ECOSYSTEM",
      "path": "References/mrprice/deep-architecture/MRPRICE_VENDOR_ECOSYSTEM.md",
      "domains": ["market-data"],
      "role_families": ["market_data_support", "application_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_vendor_normalization",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_VENDOR_NORMALIZATION",
      "path": "References/mrprice/deep-architecture/MRPRICE_VENDOR_NORMALIZATION.md",
      "domains": ["data-quality", "data-integration"],
      "role_families": ["business_analyst", "market_data_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_tick_consolidation",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_TICK_CONSOLIDATION_ENGINE",
      "path": "References/mrprice/deep-architecture/MRPRICE_TICK_CONSOLIDATION_ENGINE.md",
      "domains": ["market-data", "data-quality"],
      "role_families": ["market_data_support", "production_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_validation_workflow",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_BENCHMARK_VALIDATION_WORKFLOW",
      "path": "References/mrprice/deep-architecture/MRPRICE_BENCHMARK_VALIDATION_WORKFLOW.md",
      "domains": ["data-quality", "governance"],
      "role_families": ["application_support", "production_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_four_eyes",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_FOUR_EYES_CONTROL_MODEL",
      "path": "References/mrprice/deep-architecture/MRPRICE_FOUR_EYES_CONTROL_MODEL.md",
      "domains": ["governance"],
      "role_families": ["business_analyst", "application_support"],
      "priority": "medium"
    },

    {
      "asset_id": "mrprice_stp_batch",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_STP_AND_BATCH_PROCESSING",
      "path": "References/mrprice/deep-architecture/MRPRICE_STP_AND_BATCH_PROCESSING.md",
      "domains": ["production-support", "operations"],
      "role_families": ["production_support", "application_support"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_modernization_journey",
      "asset_type": "deep_architecture_note",
      "title": "MRPRICE_MODERNIZATION_JOURNEY",
      "path": "References/mrprice/deep-architecture/MRPRICE_MODERNIZATION_JOURNEY.md",
      "domains": ["modernization", "cloud-migration"],
      "role_families": ["business_analyst", "technical_ba"],
      "priority": "high"
    },

    {
      "asset_id": "mrprice_resume_evidence",
      "asset_type": "resume_evidence",
      "title": "MRPRICE_RESUME_EVIDENCE",
      "path": "References/mrprice/experience/MRPRICE_RESUME_EVIDENCE.md",
      "domains": ["resume"],
      "role_families": [
        "business_analyst",
        "application_support",
        "production_support",
        "market_data_support"
      ],
      "priority": "critical"
    },

    {
      "asset_id": "mrprice_star_stories",
      "asset_type": "star_story",
      "title": "MRPRICE_STAR_STORIES",
      "path": "References/mrprice/experience/MRPRICE_STAR_STORIES.md",
      "domains": ["interview"],
      "role_families": [
        "business_analyst",
        "application_support",
        "production_support"
      ],
      "priority": "critical"
    },

    {
      "asset_id": "mrprice_interview_bank",
      "asset_type": "interview_bank",
      "title": "MRPRICE_INTERVIEW_BANK",
      "path": "References/mrprice/experience/MRPRICE_INTERVIEW_BANK.md",
      "domains": ["interview"],
      "role_families": [
        "business_analyst",
        "application_support",
        "production_support",
        "market_data_support"
      ],
      "priority": "critical"
    },

    {
      "asset_id": "mrprice_skills_mapping",
      "asset_type": "skills_mapping",
      "title": "MRPRICE_SKILLS_MAPPING",
      "path": "References/mrprice/experience/MRPRICE_SKILLS_MAPPING.md",
      "domains": ["skills"],
      "role_families": ["all"],
      "priority": "critical"
    },

    {
      "asset_id": "mrprice_career_system_mapping",
      "asset_type": "career_system_mapping",
      "title": "MRPRICE_CAREER_SYSTEM_MAPPING",
      "path": "References/mrprice/experience/MRPRICE_CAREER_SYSTEM_MAPPING.md",
      "domains": ["career-system"],
      "role_families": ["all"],
      "priority": "critical"
    }
  ]
}
```

Then:

```bash
git add data/experience-assets/mrprice-assets-index.json

git commit -m "Add MRPrice asset index"

git push
```

### Why this file matters

This becomes the central registry:

```text
Experience Source
        ↓
Asset Index
        ↓
Skills
Resume Evidence
Interview Stories
JD Matching
```

Once this is committed, the next file (`mrprice-skills.json`) becomes much easier because every skill can point back to one or more asset IDs instead of raw note names.


```
* [new tag] v0.5.0-experience-source-domain-model -> v0.5.0-experience-source-domain-model
```


---

ChatGPT

Excellent.

You now have a real progression in Career System:

```text
e4ae977
Add MRPrice experience source integration

5099ed0
Add experience source domain model v0.5.0

92f0dd7
Add MRPrice asset index
```

This is where Career System starts becoming a knowledge system instead of a collection of JDs and tracker files.

---

# What We Just Built

Before:

```text
JD
 ↓
Resume
```

Now:

```text
JD
 ↓
Experience Source
 ↓
Asset Index
 ↓
Resume Evidence
 ↓
Resume
```

That is a major architectural improvement.

---

# Next File

Now we create:

```text
data/experience-skills/mrprice-skills.json
```

This is the most important structured file because skills become the bridge between:

```text
JD Keywords
        ↓
Skills
        ↓
Experience Evidence
```

---

# Proposed Initial Skills

Don't try to extract 100 skills.

Start with 10 high-value skills from MRPrice.

```text
market_data_platforms

vendor_normalization

tick_consolidation

data_quality_validation

oracle_distribution

production_support

technical_refresh

cloud_migration

rest_api_validation

four_eyes_governance
```

These map almost directly to the notes you've already created.

---

# Why Skills Before Resume Evidence JSON

Because the relationship should be:

```text
Experience Asset
        ↓
Skill
        ↓
Resume Evidence
        ↓
Interview Story
```

not the other way around.

---

# Suggested Next Deliverable

Create:

```bash
mkdir -p data/experience-skills

vi data/experience-skills/mrprice-skills.json
```

with something like:

```json
{
  "source_id": "mrprice",
  "skills": [
    {
      "skill_id": "market_data_platforms",
      "name": "Market Data Platforms",
      "category": "domain",
      "asset_ids": [
        "mrprice_vendor_ecosystem",
        "mrprice_tick_consolidation"
      ]
    }
  ]
}
```

expanded to the 10 core skills above.

---

# Roadmap Update

You are now in:

```text
v0.5.1
Structured Experience Assets
```

Progress:

```text
✓ experience-source.json
✓ experience-source-domain-model.md
✓ mrprice-assets-index.json

Next:
mrprice-skills.json

Then:
mrprice-resume-evidence.json

Then:
mrprice-interview-stories.json
```

After those three files, Career System will have enough structured MRPrice metadata to begin experimenting with:

```text
JD
 ↓
Keyword Match
 ↓
Skill Match
 ↓
Resume Evidence Selection
```

which is where the system starts becoming genuinely useful for tailored resume generation.

user

you want me to create data/experience-skills/mrprice-skills.json and paste the content in?

ChatGPT

Yes.

At this stage, I'm still recommending a **design-first/manual-first approach**, exactly like we did with `mrprice-assets-index.json`.

Create:

```bash
mkdir -p data/experience-skills

vi data/experience-skills/mrprice-skills.json
```

Then paste the initial structured skill inventory.

I would start with **10 skills only** so we validate the model before creating dozens.

:::writing{variant="document" id="68441"}
{
  "source_id": "mrprice",
  "source_release": "v0.4.1",

  "skill_count": 10,

  "skills": [

    {
      "skill_id": "market_data_platforms",
      "name": "Market Data Platforms",
      "category": "domain",
      "asset_ids": [
        "mrprice_vendor_ecosystem",
        "mrprice_tick_consolidation"
      ],
      "jd_keywords": [
        "market data",
        "pricing",
        "fixed income",
        "vendor feeds"
      ]
    },

    {
      "skill_id": "vendor_normalization",
      "name": "Vendor Normalization",
      "category": "data_integration",
      "asset_ids": [
        "mrprice_vendor_normalization"
      ],
      "jd_keywords": [
        "data mapping",
        "normalization",
        "transformation",
        "integration"
      ]
    },

    {
      "skill_id": "tick_consolidation",
      "name": "Tick Consolidation",
      "category": "data_quality",
      "asset_ids": [
        "mrprice_tick_consolidation"
      ],
      "jd_keywords": [
        "consolidation",
        "pricing",
        "market data",
        "data quality"
      ]
    },

    {
      "skill_id": "data_quality_validation",
      "name": "Data Quality Validation",
      "category": "quality",
      "asset_ids": [
        "mrprice_validation_workflow"
      ],
      "jd_keywords": [
        "data quality",
        "validation",
        "exception handling",
        "root cause analysis"
      ]
    },

    {
      "skill_id": "oracle_distribution",
      "name": "Oracle Distribution",
      "category": "database",
      "asset_ids": [
        "mrprice_modernization_journey"
      ],
      "jd_keywords": [
        "oracle",
        "sql",
        "database",
        "data access"
      ]
    },

    {
      "skill_id": "production_support",
      "name": "Production Support",
      "category": "operations",
      "asset_ids": [
        "mrprice_stp_batch",
        "mrprice_validation_workflow"
      ],
      "jd_keywords": [
        "production support",
        "incident management",
        "monitoring",
        "troubleshooting"
      ]
    },

    {
      "skill_id": "technical_refresh",
      "name": "Technical Refresh",
      "category": "modernization",
      "asset_ids": [
        "mrprice_modernization_journey"
      ],
      "jd_keywords": [
        "modernization",
        "technical refresh",
        "platform migration"
      ]
    },

    {
      "skill_id": "cloud_migration",
      "name": "Cloud Migration",
      "category": "cloud",
      "asset_ids": [
        "mrprice_modernization_journey"
      ],
      "jd_keywords": [
        "cloud migration",
        "aws",
        "modernization",
        "migration"
      ]
    },

    {
      "skill_id": "rest_api_validation",
      "name": "REST API Validation",
      "category": "integration",
      "asset_ids": [
        "mrprice_modernization_journey"
      ],
      "jd_keywords": [
        "rest api",
        "api testing",
        "api validation",
        "service integration"
      ]
    },

    {
      "skill_id": "four_eyes_governance",
      "name": "Four Eyes Governance",
      "category": "governance",
      "asset_ids": [
        "mrprice_four_eyes",
        "mrprice_validation_workflow"
      ],
      "jd_keywords": [
        "governance",
        "controls",
        "audit",
        "approval workflow"
      ]
    }

  ]
}
:::

Then:

```bash
git add data/experience-skills/mrprice-skills.json

git commit -m "Add MRPrice skills index"

git push
```

One thing I'd change from the earlier design: after this commit, let's pause and review the structure before creating `mrprice-resume-evidence.json`.

We're now defining the core Career System data model, so it's worth validating that:

```text
Experience Source
      ↓
Asset Index
      ↓
Skills
```

feels right before we build the next layers.


---

