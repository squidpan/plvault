---
categories:
  - "[[Processes]]"
type:
description:
source: chatgpt-manual
tags:
created: 2026-07-13
last: 2026-07-13
status:
origin:
run_id:
input_prompt:
---

> [!Prompt]
> done. A) what other information do I need to extract as handoff material to the other chat. Remember i am wanting to go to new chats each to make 1) career center functional again and to 2) continue with efk. also can you draw out (sequence diag. or flow chart) the logic and data-flow (puml) from source jd to roles (need diagrams on roles processing, roles db, etc) resumes (differnet types of resumes), operational commands used in each case etc. same thing for subsequent steps in the wokflow. I think this will make it easier to explain in detail what the over flow is.  (A) and (B) are both ways to build a complete enough handoff stuff so I spend less time here. It is too slow. what d'ya think?

Yes — this is exactly right. Before moving to new chats, create a **handoff pack**, not just one README.

You need two handoffs:

```text
1) Career Center Functional Recovery
2) EFK / EOS Continuation
```

And yes, diagrams will help a lot. I’d make **PlantUML flow/sequence diagrams** part of the handoff.

## A) Extra handoff material to extract

For **Career Center functional recovery**, extract:

```text
Current branch:
ops/recover-ats-html-workflow

Known-good regression packages:
LSEG
Broadridge

Final deliverable:
data/application-packages/application-<job>-2026-v1/

Confirmed broken shortcut:
assembled-v2 → teal-export → application package

Missing bridge:
new pipeline → application-summary.md + frbny-section.md

Validated final-mile scripts:
assemble_full_resume.py
assemble_ats_resume.py
export_resume_html.py
export_ats_text.py
build_application_package.py

Key docs already committed:
docs/operations/recovery/
docs/operations/handoffs/
docs/requirements/stories/US-CS-RECOVERY-001...
```

For **EFK / EOS**, extract:

```text
EKF / EOS architecture docs
EKF diagrams
engineering artifact standards
artifact naming standard
Obsidian metadata standard
document structure standard
template library
validation architecture
ADR docs
```

## B) Diagrams to create

I’d create these files:

```text
docs/operations/diagrams/jd-to-application-package-flow.puml
docs/operations/diagrams/jd-to-role-sequence.puml
docs/operations/diagrams/resume-generation-flow.puml
docs/operations/diagrams/final-mile-application-package-flow.puml
docs/operations/diagrams/efk-eos-overview.puml
```

Start with this:

```bash
mkdir -p docs/operations/diagrams
```

### 1) JD to Application Package Flow

```bash
cat > docs/operations/diagrams/jd-to-application-package-flow.puml <<'EOF'
@startuml
title Career System — JD to Application Package Flow

start

:Raw JD;
:Normalize JD;
:Generate Role;
:Generate Resume Version;
:Generate JD Intelligence;
:Generate Candidate Match;
:Generate Candidate Strategy;
:Generate Candidate Explainability;
:Generate Resume Tailoring;
:Generate Resume Bullet Ranking;

partition "Missing Bridge" {
  :Generate Application Summary;
  :Generate Targeted FRBNY Resume Section;
}

:Generate ATS Resume;
:Generate Full Resume;
:Export HTML;
:Export ATS TXT;
:Build Application Package;
:Update Submission Notes;
:Application Tracker / CSV / Postgres;

stop
@enduml
EOF
```

### 2) Final-Mile Package Flow

```bash
cat > docs/operations/diagrams/final-mile-application-package-flow.puml <<'EOF'
@startuml
title Career System — Final-Mile Application Package Flow

start

:application-summary.md;
:frbny-section.md;

:run-full-resume-generator.sh;
note right
scripts/assemble_full_resume.py
end note

:full-resume.md;

:run-ats-resume-generator.sh;
note right
scripts/assemble_ats_resume.py
end note

:ats-resume.md;

:run-resume-html-export.sh;
:full-resume.html;
:ats-resume.html;

:run-ats-text-export.sh;
:ats-resume.txt;

:run-application-package.sh;
note right
scripts/build_application_package.py
end note

:application-packages/application-<job>-2026-v1/;

stop
@enduml
EOF
```

### 3) EFK / EOS Overview

```bash
cat > docs/operations/diagrams/efk-eos-overview.puml <<'EOF'
@startuml
title EFK / EOS — Engineering Operating System Overview

actor User

rectangle "Career System" {
  component "JD Pipeline"
  component "Resume Pipeline"
  component "Application Package Pipeline"
}

rectangle "Motorweb Career Center" {
  component "FastAPI"
  database "PostgreSQL"
  component "Dashboard"
}

rectangle "Engineering Knowledge Framework" {
  component "Standards"
  component "ADRs"
  component "Templates"
  component "Validation"
  component "Obsidian Publish"
}

rectangle "Observability / EFK" {
  component "Structured Logs"
  component "Collector"
  database "Elastic/OpenSearch"
  component "Dashboards"
}

User --> "Career System"
"Career System" --> "PostgreSQL"
"FastAPI" --> "PostgreSQL"
"Dashboard" --> "FastAPI"

"Career System" --> "Structured Logs"
"FastAPI" --> "Structured Logs"
"Structured Logs" --> "Collector"
"Collector" --> "Elastic/OpenSearch"
"Elastic/OpenSearch" --> "Dashboards"

"Career System" --> "Standards"
"Motorweb Career Center" --> "Standards"
"Standards" --> "Validation"
"Templates" --> "Obsidian Publish"

@enduml
EOF
```

Then commit:

```bash
git add docs/operations/diagrams
git commit -m "Add recovery workflow and EFK handoff diagrams"
git push
git status --short
```

## My recommendation

Yes: make the diagrams and handoff docs here, then move to fresh chats.

New chat 1:

```text
Career Center Functional Recovery v2
Goal: reconnect new JD pipeline to proven application-package workflow.
Use LSEG/Broadridge as regression tests.
```

New chat 2:

```text
EFK / EOS Continuation
Goal: continue engineering knowledge framework, standards, diagrams, validation, observability.
```

This chat has done its job: recovery investigation, validation, and architecture clarification. Now we should hand off into cleaner, faster chats.

---


Yes. Below is the **working operational script inventory** as I understand it right now. I’m separating **verified/currently used**, **active but bridge/incomplete**, and **legacy/avoid for final resumes**.

This is exactly the kind of inventory the recovery handoff asked for: each stage should identify purpose, inputs, outputs, wrapper scripts, Python scripts, intermediate artifacts, final artifacts, and whether artifacts belong under `data/` or `ops/runs/` .

---

# Career System Operational Workflow — Script Inventory

## Golden rule

The final operational deliverable is:

```text
data/application-packages/application-<job-slug>-2026-v1/
```

Not `assembled-v2`.  
Not `teal-export`.  
Not just `full-resume.md`.

The historical recovery work showed that the real objective is to make Career System generate application packages so you can apply for jobs .

---

# Phase 0 — Capture JD

## Step 0.1 — Clip JD using Obsidian Web Clipper

**Manual step**

Input:

```text
Job posting page
```

Output:

```text
Obsidian clipped markdown JD
```

Example target file name:

```text
jd-raw-<company>-<role>.md
```

No `bin/` script yet.

---

## Step 0.2 — Copy raw JD into Career System

**Manual command**

```bash
cd ~/pjs/repos/career-system

cp -p <obsidian-clipped-jd>.md \
  data/jds/raw/jd-raw-<company>-<role>.md
```

Output:

```text
data/jds/raw/jd-raw-<company>-<role>.md
```

Status:

```text
Active manual operational step
```

---

# Phase 1 — JD normalization

## Step 1 — Normalize raw JD

Wrapper:

```text
bin/run-jd-normalization.sh
```

Python:

```text
scripts/normalize_jd.py
scripts/normalize_jd_oo.py
```

Typical command pattern:

```bash
./bin/run-jd-normalization.sh \
  run-$(date +%Y-%m-%d)-jd-normalization-v1 \
  data/jds/raw
```

For a subset/regression run:

```bash
./bin/run-jd-normalization.sh \
  run-$(date +%Y-%m-%d)-jd-normalization-new-jds-v1 \
  /tmp/career-raw-new-jds
```

Input:

```text
data/jds/raw/*.md
```

Output:

```text
data/jds/normalized/jd-<job-slug>-2026-v1.md
ops/runs/<run-id>/output/
```

Status:

```text
Active / required
```

Notes:

The normalized JD becomes the job metadata source. This aligns with the later application-tracking design where normalized JD metadata feeds generated rollups, PostgreSQL, dashboards, and REST APIs .

---

# Phase 2 — Role generation

## Step 2 — Generate role record from normalized JD

Likely wrapper:

```text
bin/run-role-generation.sh
```

Likely Python:

```text
scripts/generate_roles_from_jds.py
```

I want to verify these exact names in the repo before we treat them as canonical, because they did **not** appear in the grep output you pasted, probably because the grep pattern did not include `role`.

Check with:

```bash
find bin scripts -type f | grep -Ei "role|jd" | sort
```

Expected command pattern:

```bash
./bin/run-role-generation.sh \
  run-$(date +%Y-%m-%d)-role-generation-v1 \
  data/jds/normalized
```

Input:

```text
data/jds/normalized/jd-<job-slug>-2026-v1.md
```

Output:

```text
data/roles/role-<job-slug>-2026.md
```

Status:

```text
Active / required, but exact wrapper needs confirmation
```

Known current role files:

```text
data/roles/role-blackrock-ops-2026.md
data/roles/role-clearwater-analytics-ba-2026.md
data/roles/role-experis-ba-ai-2026.md
data/roles/role-langchain-support-appsupport-2026.md
data/roles/role-marketaxess-product-2026.md
data/roles/role-plexus-resource-solutions-ba-2026.md
data/roles/role-pri-technology-ba-ai-2026.md
data/roles/role-raas-infotek-llc-ba-2026.md
data/roles/role-tiaa-bsa-2026.md
```

---

# Phase 3 — Resume version generation

## Step 3 — Generate resume-version metadata from role

Wrapper:

```text
bin/run-resume-version-generation.sh
```

Python:

```text
scripts/generate_resume_versions_from_roles.py
```

Command you used successfully:

```bash
./bin/run-resume-version-generation.sh \
  run-$(date +%Y-%m-%d)-resume-version-new-jds-v1 \
  /tmp/career-roles-new-jds
```

Input:

```text
data/roles/role-<job-slug>-2026.md
```

Output:

```text
data/resume-versions/generated/resume-<job-slug>-2026-v1.md
ops/runs/<run-id>/output/
```

Status:

```text
Active / required
```

Important:

This does **not** create the final resume. It creates a resume-version record/metadata artifact.

---

# Phase 4 — JD intelligence

## Step 4 — Generate JD intelligence

Wrapper:

```text
bin/run-jd-intelligence.sh
```

Python:

```text
scripts/generate_jd_intelligence.py
```

Command you used successfully:

```bash
./bin/run-jd-intelligence.sh \
  run-$(date +%Y-%m-%d)-jd-intelligence-new-jds-v2 \
  /tmp/career-normalized-new-jds
```

Input:

```text
data/jds/normalized/jd-<job-slug>-2026-v1.md
```

Output:

```text
data/jd-intelligence/jd-intelligence-<job-slug>.md
data/jd-intelligence/jd-intelligence-<job-slug>.json
ops/runs/<run-id>/output/
```

Status:

```text
Active / required for modern pipeline
```

---

# Phase 5 — Candidate matching

## Step 5 — Generate candidate match

Wrapper:

```text
bin/run-candidate-matching.sh
```

Python:

```text
scripts/generate_candidate_matching.py
```

Direct command you used successfully:

```bash
python3 scripts/generate_candidate_matching.py \
  --run-id run-$(date +%Y-%m-%d)-candidate-matching-new-jds-v1 \
  --input-dir /tmp/career-jd-intelligence-new-jds \
  --output-dir /tmp/career-candidate-matching-new-jds
```

Wrapper pattern:

```bash
./bin/run-candidate-matching.sh \
  run-$(date +%Y-%m-%d)-candidate-matching-v1 \
  data/jd-intelligence
```

Input:

```text
data/jd-intelligence/jd-intelligence-<job-slug>.json
```

Output:

```text
data/candidate-matching/candidate-match-<job-slug>.md
data/candidate-matching/candidate-match-<job-slug>.json
```

Status:

```text
Active / modern decision-support pipeline
```

This fits the broader direction that Career System should not only generate resumes, but also decide whether a role is worth pursuing via fit scoring, gaps, and prioritization .

---

# Phase 6 — Candidate strategy

## Step 6 — Generate candidate strategy

Wrapper:

```text
bin/run-candidate-strategy.sh
```

Python:

```text
scripts/generate_candidate_strategy.py
```

Direct command you used successfully:

```bash
python3 scripts/generate_candidate_strategy.py \
  --run-id run-$(date +%Y-%m-%d)-candidate-strategy-new-jds-v1 \
  --input-dir /tmp/career-candidate-strategy-new-jds \
  --output-dir /tmp/career-candidate-strategy-new-jds-output
```

Wrapper pattern:

```bash
./bin/run-candidate-strategy.sh \
  run-$(date +%Y-%m-%d)-candidate-strategy-v1 \
  data/candidate-matching
```

Input:

```text
data/candidate-matching/candidate-match-<job-slug>.json
```

Output:

```text
data/candidate-strategy/candidate-strategy-<job-slug>.md
data/candidate-strategy/candidate-strategy-<job-slug>.json
```

Status:

```text
Active / modern decision-support pipeline
```

---

# Phase 7 — Candidate explainability

## Step 7 — Generate candidate explainability

Wrapper:

```text
bin/run-candidate-explainability.sh
```

Python:

```text
scripts/generate_candidate_explainability.py
```

Direct command you used successfully:

```bash
python3 scripts/generate_candidate_explainability.py \
  --run-id run-$(date +%Y-%m-%d)-candidate-explainability-new-jds-v1 \
  --input-dir /tmp/career-candidate-explainability-new-jds \
  --output-dir /tmp/career-candidate-explainability-new-jds-output
```

Wrapper pattern:

```bash
./bin/run-candidate-explainability.sh \
  run-$(date +%Y-%m-%d)-candidate-explainability-v1 \
  data/candidate-strategy
```

Input:

```text
data/candidate-strategy/candidate-strategy-<job-slug>.json
```

Output:

```text
data/candidate-explainability/candidate-explainability-<job-slug>.md
data/candidate-explainability/candidate-explainability-<job-slug>.json
```

Status:

```text
Active / modern decision-support pipeline
```

---

# Phase 8 — Resume tailoring guidance

## Step 8 — Generate resume tailoring

Wrapper:

```text
bin/run-resume-tailoring.sh
```

Python:

```text
scripts/generate_resume_tailoring.py
```

Direct command you used successfully:

```bash
python3 scripts/generate_resume_tailoring.py \
  --run-id run-$(date +%Y-%m-%d)-resume-tailoring-new-jds-v1 \
  --input-dir /tmp/career-resume-tailoring-new-jds \
  --output-dir /tmp/career-resume-tailoring-new-jds-output
```

Wrapper pattern:

```bash
./bin/run-resume-tailoring.sh \
  run-$(date +%Y-%m-%d)-resume-tailoring-v1 \
  data/candidate-explainability
```

Input:

```text
data/candidate-explainability/candidate-explainability-<job-slug>.json
```

Output:

```text
data/resume-tailoring/resume-tailor-<job-slug>.md
data/resume-tailoring/resume-tailor-<job-slug>.json
```

Status:

```text
Active / required before bullet ranking
```

---

# Phase 9 — Resume bullet ranking

## Step 9 — Generate resume bullet ranking

Wrapper:

```text
bin/run-resume-bullet-ranking.sh
```

Python:

```text
scripts/generate_resume_bullet_ranking.py
```

Important filename issue discovered:

The script looks for files named:

```text
resume-tailoring-*.md
```

But current data files are named:

```text
resume-tailor-*.md
```

So during recovery, you copied/renamed into `/tmp` like this:

```bash
cp data/resume-tailoring/resume-tailor-${f}.md \
   /tmp/career-resume-bullet-ranking-new-jds/resume-tailoring-${f}.md

cp data/resume-tailoring/resume-tailor-${f}.json \
   /tmp/career-resume-bullet-ranking-new-jds/resume-tailoring-${f}.json
```

Working command:

```bash
python3 scripts/generate_resume_bullet_ranking.py \
  run-$(date +%Y-%m-%d)-resume-bullet-ranking-new-jds-v2 \
  /tmp/career-resume-bullet-ranking-new-jds \
  data/resume-versions/generated
```

Wrapper pattern:

```bash
./bin/run-resume-bullet-ranking.sh \
  run-$(date +%Y-%m-%d)-resume-bullet-ranking-v1 \
  data/resume-tailoring \
  data/resume-versions/generated
```

Input:

```text
resume-tailoring-<job-slug>.md
resume-tailoring-<job-slug>.json
data/resume-versions/generated/resume-<job-slug>-2026-v1.md
```

Output:

```text
data/resume-bullet-ranking/bullet-ranking-<job-slug>.md
data/resume-bullet-ranking/bullet-ranking-<job-slug>.json
```

Status:

```text
Active, but has naming mismatch issue
```

---

# Phase 10 — Employer-aware assembled resume

## Step 10 — Generate employer-aware assembled resume

Wrapper:

```text
bin/run-role-aware-resume-assembly.sh
```

Python:

```text
scripts/assemble_role_aware_resumes.py
```

Working command:

```bash
./bin/run-role-aware-resume-assembly.sh \
  run-$(date +%Y-%m-%d)-employer-aware-resume-assembly-new-jds-v1 \
  /tmp/career-bullet-ranking-new-jds \
  data/resume-tailoring \
  data/resume-versions/generated
```

Input:

```text
data/resume-bullet-ranking/bullet-ranking-<job-slug>.json
data/resume-tailoring/
data/resume-versions/generated/
```

Output:

```text
data/resume-versions/assembled-v2/resume-<job-slug>-assembled-v2.md
data/resume-versions/assembled-v2/resume-<job-slug>-assembled-v2.json
```

Status:

```text
Intermediate only
Do not use as final application resume
```

Important:

This is where MarketAxess went wrong. The assembled-v2/teal-export artifact was too thin, duplicated FRBNY experience, and was not equivalent to LSEG/Broadridge final packages. The MarketAxess export itself shows the duplicate FRBNY blocks and incomplete content, confirming it is not the final path .

---

# Phase 11 — Teal export

## Step 11 — Teal export / markdown cleanup

Wrapper:

```text
bin/run-teal-export.sh
```

Python:

```text
scripts/generate_teal_export_resumes.py
```

Working command:

```bash
./bin/run-teal-export.sh \
  run-$(date +%Y-%m-%d)-teal-export-new-jds-v4 \
  /tmp/career-assembled-new-jds
```

Input:

```text
data/resume-versions/assembled-v2/resume-<job-slug>-assembled-v2.md
```

Output:

```text
data/resume-versions/teal-export/resume-<job-slug>-assembled-v2-teal-v1.md
```

Status:

```text
Legacy/intermediate
Do not use as final application resume
```

Important:

The filename still says `teal` because it originally existed for Teal-friendly exports. Operationally, we should probably rename or deprecate this stage later because Teal is no longer the final resume manager.

---

# Phase 12 — Missing bridge to final-mile workflow

This is the key gap.

The modern pipeline must produce these two files:

```text
data/application-summaries/<job-slug>-summary-v1.md
data/resume-sections/<job-slug>-frbny-section.md
```

Current known-good examples:

```text
data/application-summaries/lseg-senior-ba-summary-v1.md
data/resume-sections/lseg-senior-ba-frbny-section.md

data/application-summaries/broadridge-product-analyst-summary-v1.md
data/resume-sections/broadridge-product-analyst-frbny-section.md
```

Scripts likely involved historically:

```text
bin/run-resume-section-generator.sh
scripts/generate_resume_section.py

bin/run-resume-recommendation.sh
scripts/recommend_resume_assets.py

bin/run-resume-bullet-generator.sh
scripts/generate_resume_bullets.py

bin/run-resume-generation.sh
scripts/generate_resumes.py

bin/run-resume-enhancement.sh
scripts/generate_resume_enhancement.py
```

Status:

```text
Missing / needs reconstruction
```

This is the next functional recovery work.

---

# Phase 13 — Full resume generation

## Step 13 — Generate full resume

Wrapper:

```text
bin/run-full-resume-generator.sh
```

Python:

```text
scripts/assemble_full_resume.py
```

Working command from LSEG/Broadridge rebuild:

```bash
./bin/run-full-resume-generator.sh \
  data/application-summaries/<job-slug>-summary-v1.md \
  data/resume-sections/<job-slug>-frbny-section.md \
  data/full-resumes/<job-slug>-full-resume-v1.md \
  <job-slug>
```

Example:

```bash
./bin/run-full-resume-generator.sh \
  data/application-summaries/lseg-senior-ba-summary-v1.md \
  data/resume-sections/lseg-senior-ba-frbny-section.md \
  data/full-resumes/lseg-senior-ba-full-resume-v1.md \
  lseg-senior-ba
```

Input:

```text
data/application-summaries/<job-slug>-summary-v1.md
data/resume-sections/<job-slug>-frbny-section.md
data/master-profile/contact-info.md
data/master-profile/older-experience.md
data/master-profile/education.md
data/master-profile/publications.md
data/master-profile/skills.md
```

Output:

```text
data/full-resumes/<job-slug>-full-resume-v1.md
```

Status:

```text
Verified working / final-mile
```

---

# Phase 14 — ATS resume generation

## Step 14 — Generate ATS resume

Wrapper:

```text
bin/run-ats-resume-generator.sh
```

Python:

```text
scripts/assemble_ats_resume.py
```

Working command from LSEG/Broadridge rebuild:

```bash
./bin/run-ats-resume-generator.sh \
  data/application-summaries/<job-slug>-summary-v1.md \
  data/resume-sections/<job-slug>-frbny-section.md \
  data/full-resumes/<job-slug>-ats-resume-v1.md \
  <job-slug>
```

Example:

```bash
./bin/run-ats-resume-generator.sh \
  data/application-summaries/lseg-senior-ba-summary-v1.md \
  data/resume-sections/lseg-senior-ba-frbny-section.md \
  data/full-resumes/lseg-senior-ba-ats-resume-v1.md \
  lseg-senior-ba
```

Input:

```text
data/application-summaries/<job-slug>-summary-v1.md
data/resume-sections/<job-slug>-frbny-section.md
data/master-profile/contact-info.md
data/master-profile/ats-employment-history.md
data/master-profile/education.md
data/master-profile/publications.md
data/master-profile/skills.md
```

Output:

```text
data/full-resumes/<job-slug>-ats-resume-v1.md
```

Status:

```text
Verified working / final-mile
```

Known-good ATS output includes the clean LSEG format with Paul’s contact block, professional summary, Gresham/FRBNY on-site experience, prior employers, education, publications, and skills .

---

# Phase 15 — HTML export

## Step 15 — Export resume markdown to HTML

Wrapper:

```text
bin/run-resume-html-export.sh
```

Python:

```text
scripts/export_resume_html.py
```

Command:

```bash
./bin/run-resume-html-export.sh \
  data/full-resumes/<job-slug>-full-resume-v1.md \
  data/full-resumes/<job-slug>-full-resume-v1.html

./bin/run-resume-html-export.sh \
  data/full-resumes/<job-slug>-ats-resume-v1.md \
  data/full-resumes/<job-slug>-ats-resume-v1.html
```

Input:

```text
data/full-resumes/<job-slug>-full-resume-v1.md
data/full-resumes/<job-slug>-ats-resume-v1.md
```

Output:

```text
data/full-resumes/<job-slug>-full-resume-v1.html
data/full-resumes/<job-slug>-ats-resume-v1.html
```

Status:

```text
Verified working / final-mile
```

---

# Phase 16 — ATS text export

## Step 16 — Export ATS resume to TXT

Wrapper:

```text
bin/run-ats-text-export.sh
```

Python:

```text
scripts/export_ats_text.py
```

Command:

```bash
./bin/run-ats-text-export.sh \
  data/full-resumes/<job-slug>-ats-resume-v1.md \
  data/ats-exports/<job-slug>-ats-resume-v1.txt
```

Input:

```text
data/full-resumes/<job-slug>-ats-resume-v1.md
```

Output:

```text
data/ats-exports/<job-slug>-ats-resume-v1.txt
```

Status:

```text
Verified working / final-mile
```

---

# Phase 17 — Application package generation

## Step 17 — Build application package

Wrapper:

```text
bin/run-application-package.sh
```

Python:

```text
scripts/build_application_package.py
```

Command:

```bash
./bin/run-application-package.sh \
  <job-slug> \
  application-<job-slug>-2026-v1
```

Example:

```bash
./bin/run-application-package.sh \
  lseg-senior-ba \
  application-lseg-senior-ba-2026-v1
```

Input sources checked by script:

```text
data/experience-matches/<job-slug>-resume-recommendation.json
data/experience-matches/<job-slug>-interview-recommendation.json
data/generated-resumes/<job-slug>-resume-v1.md
data/generated-resumes/<job-slug>-resume-tailored-v1.md
data/generated-resumes/<job-slug>-resume-enhanced-v1.md
data/application-summaries/<job-slug>-summary-v1.md
data/full-resumes/<job-slug>-full-resume-v1.md
data/full-resumes/<job-slug>-full-resume-v1.html
data/full-resumes/<job-slug>-ats-resume-v1.md
data/full-resumes/<job-slug>-ats-resume-v1.html
data/ats-exports/<job-slug>-ats-resume-v1.txt
```

Output:

```text
data/application-packages/application-<job-slug>-2026-v1/
```

Expected package contents:

```text
application-summary.md
ats-resume.html
ats-resume.md
ats-resume.txt
full-resume.html
full-resume.md
package-manifest.json
README.md
resume-enhanced.md
resume-generated.md
resume-recommendation.json
resume-tailored.md
submission-notes.md
```

Optional:

```text
interview-recommendation.json
PDF
```

Status:

```text
Verified working / true final deliverable
```

---

# Phase 18 — Manual PDF generation

## Step 18 — Browser PDF from HTML

Manual step:

```text
Open ats-resume.html or full-resume.html in browser
Print → Save to PDF
```

Output example:

```text
data/application-packages/application-<job-slug>-2026-v1/paul-lyu-<job-slug>-resume-v1.pdf
```

Status:

```text
Manual but operational
```

---

# Phase 19 — Submission notes / application event

## Step 19 — Update submission notes

File:

```text
data/application-packages/application-<job-slug>-2026-v1/submission-notes.md
```

Purpose:

```text
Application event record
Source for application tracker / CSV / Postgres / Motorweb
```

This aligns with your earlier approved architecture direction: `submission-notes.md` is the Application Event Record, and generated rollups feed applications.csv, PostgreSQL, dashboards, and REST APIs .

Status:

```text
Operationally important / should not be casual note
```

---

# Scripts currently in use by workflow stage

## Core active scripts

```text
bin/run-jd-normalization.sh
scripts/normalize_jd.py
scripts/normalize_jd_oo.py

bin/run-resume-version-generation.sh
scripts/generate_resume_versions_from_roles.py

bin/run-jd-intelligence.sh
scripts/generate_jd_intelligence.py

bin/run-candidate-matching.sh
scripts/generate_candidate_matching.py

bin/run-candidate-strategy.sh
scripts/generate_candidate_strategy.py

bin/run-candidate-explainability.sh
scripts/generate_candidate_explainability.py

bin/run-resume-tailoring.sh
scripts/generate_resume_tailoring.py

bin/run-resume-bullet-ranking.sh
scripts/generate_resume_bullet_ranking.py

bin/run-role-aware-resume-assembly.sh
scripts/assemble_role_aware_resumes.py

bin/run-full-resume-generator.sh
scripts/assemble_full_resume.py

bin/run-ats-resume-generator.sh
scripts/assemble_ats_resume.py

bin/run-resume-html-export.sh
scripts/export_resume_html.py

bin/run-ats-text-export.sh
scripts/export_ats_text.py

bin/run-application-package.sh
scripts/build_application_package.py
```

## Active but bridge/recovery scripts to inspect next

```text
bin/run-resume-section-generator.sh
scripts/generate_resume_section.py

bin/run-resume-recommendation.sh
scripts/recommend_resume_assets.py

bin/run-resume-bullet-generator.sh
scripts/generate_resume_bullets.py

bin/run-resume-generation.sh
scripts/generate_resumes.py

bin/run-resume-enhancement.sh
scripts/generate_resume_enhancement.py

bin/run-resume-finalization.sh
scripts/finalize_resumes.py

bin/run-application-package-generation.sh
scripts/generate_application_packages.py

bin/run-application-package-generator.sh
scripts/generate_application_package.py
```

## Legacy / avoid as final path

```text
bin/run-teal-export.sh
scripts/generate_teal_export_resumes.py

data/resume-versions/assembled-v2/
data/resume-versions/teal-export/
```

Use them only as intermediate/recovery evidence until renamed, retired, or reconnected properly.

---

# Biggest unresolved operational gap

The gap is not ATS export.

The gap is:

```text
modern pipeline
→ application-summary.md
→ targeted FRBNY resume section
→ proven final-mile generators
```

That is the next functional recovery target.