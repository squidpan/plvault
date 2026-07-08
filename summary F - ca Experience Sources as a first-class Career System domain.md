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