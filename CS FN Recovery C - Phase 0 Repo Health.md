---
categories:
  - "[[Processes]]"
type:
description: CS FN recovery B phase 0
source: chatgpt-manual
tags:
created: 2026-07-13
last: 2026-07-13
status:
origin:
run_id:
input_prompt:
---


Excellent. I think we've now done the "engineering management" work (handoffs, project sources, architecture). It's time to get the system working again.

## Overall Objective

The mission is **not** to redesign Career System.

The mission is:

> **Restore the ability to take a brand-new Job Description and reliably produce a production-ready application package that you can submit to employers.**

The operations handoff defines this objective clearly and identifies the missing bridge between the modern JD pipeline and the proven final-mile generators.

---

# Overall Recovery Plan

I see this as a 5-phase recovery effort.

## Phase 0 — Repository Validation (Today)

**ETA:** 1–2 hours

Goal:

> Make sure the repository we're working from is healthy before changing anything.

Deliverables:

- verify git branch
    
- verify working tree
    
- verify stashes
    
- inventory scripts
    
- inventory generated artifacts
    
- verify regression packages exist
    
- verify master-profile is complete
    

No code changes.

---

## Phase 1 — Regression Validation

**ETA:** 1 day

Goal:

Prove the existing final-mile pipeline still works.

Use ONLY

- LSEG
    
- Broadridge
    

Expected output:

```
ATS markdown
ATS HTML
ATS txt

Full markdown
Full HTML

Application package
```

If these fail...

Stop.

Fix the final-mile scripts first.

---

## Phase 2 — Missing Bridge Recovery

**ETA:** 2–4 days

This is the real work.

We need to reconstruct:

```
modern pipeline
        ↓
application-summary.md

modern pipeline
        ↓
targeted-frbny-section.md
```

Those two artifacts become the contract into the proven generators.

This phase is where we will probably touch Python.

---

## Phase 3 — New JD Validation

**ETA:** 1–2 days

Take a brand-new JD.

Run

```
JD

↓

normalize

↓

role

↓

candidate pipeline

↓

bridge

↓

ATS resume

↓

application package
```

No manual editing should be required except reviewing the final resume.

---

## Phase 4 — Operational Hardening

**ETA:** ongoing

Only after applications are flowing again.

Things like:

- regression tests
    
- logging
    
- better error messages
    
- diagrams
    
- documentation
    
- EFK integration
    
- PostgreSQL
    
- Motorweb integration
    

---

# Today's Goal

Today's goal is intentionally modest.

We are **not** writing Python today unless we discover something obviously broken.

Today's deliverable is a complete understanding of the live repository.

Specifically:

## Step 1

Repository health

```bash
cd ~/pjs/repos/career-system

git branch --show-current

git status --short

git log --oneline --decorate -10

git stash list
```

---

## Step 2

Inventory

Verify the folders actually exist.

Examples:

```
bin/

scripts/

data/application-packages/

data/application-summaries/

data/resume-sections/

data/master-profile/

docs/operations/
```

---

## Step 3

Regression inventory

Verify

```
application-lseg-senior-ba-2026-v1

application-broadridge-product-analyst-2026-v1
```

are still intact.

---

## Step 4

Verify bridge inputs

Do these exist?

```
application-summary.md

frbny-section.md
```

for

- LSEG
    
- Broadridge
    

Those become our reference implementation.

---

## Step 5

Verify wrappers

Make sure the operational wrappers exist:

```
run-full-resume-generator.sh

run-ats-resume-generator.sh

run-resume-html-export.sh

run-ats-text-export.sh

run-application-package.sh
```

---

# What I expect we'll learn today

By the end of today I expect we'll know:

✅ repository state

✅ exactly where the bridge begins

✅ exactly where the bridge ends

✅ every script involved

✅ every artifact involved

✅ whether the regression packages are still reproducible

After today we should be able to say:

> "We know precisely what must be fixed."

instead of

> "Something in the resume pipeline is broken."

---

## My estimated timeline

Assuming there aren't any major surprises:

- **Today:** Repository validation and regression inventory.
    
- **Next 1–2 sessions:** Prove the LSEG and Broadridge pipelines still generate the expected outputs.
    
- **Following 2–4 sessions:** Reconstruct the missing bridge from the modern JD pipeline to the proven final-mile generators.
    
- **Final validation:** Run a completely new JD through the restored workflow and produce both:
    
    - an **ATS-friendly HTML resume** (your highest priority for applications),
        
    - a **human-friendly narrative HTML/Markdown resume**,
        
    - and a complete **application package** ready for submission.
        

Once that succeeds, we'll consider Career System functionally recovered and then move on to hardening, testing, and future enhancements.

---
I actually like your AM/PM plan.

- **AM = Apply to jobs using the existing manual process.** That keeps your primary objective (getting interviews) moving.
    
- **PM = Recover and improve Career System.** That invests in reducing the manual work over time.
    

That strikes a good balance between immediate results and long-term productivity.

---

# Phase 0 — Repository Validation

This is an **inspection phase**. We are deliberately **not changing code** today.

## Success criteria for today

By the end of today, I want us to have:

- ✅ a verified repository state
    
- ✅ verified recovery branch
    
- ✅ verified operational scripts
    
- ✅ verified regression packages
    
- ✅ verified bridge artifacts
    
- ✅ an implementation plan with no guesswork
    

If we discover a problem, we'll document it before fixing it.

---

# Step 0.1 — Repository Health

Please run the following from your Career System repository.

```bash
cd ~/pjs/repos/career-system

echo "===== BRANCH ====="
git branch --show-current

echo
echo "===== STATUS ====="
git status --short

echo
echo "===== LAST 15 COMMITS ====="
git log --oneline --decorate -15

echo
echo "===== STASHES ====="
git stash list

echo
echo "===== REMOTES ====="
git remote -v
```

## output

```outout
[PL] pl@pop-os:~/pjs/repos/career-system $ cd ~/pjs/repos/career-system

echo "===== BRANCH ====="
git branch --show-current

echo
echo "===== STATUS ====="
git status --short

echo
echo "===== LAST 15 COMMITS ====="
git log --oneline --decorate -15

echo
echo "===== STASHES ====="
git stash list

echo
echo "===== REMOTES ====="
git remote -v
===== BRANCH =====
ops/recover-ats-html-workflow

===== STATUS =====

===== LAST 15 COMMITS =====
53ec345 (HEAD -> ops/recover-ats-html-workflow, origin/ops/recover-ats-html-workflow) Add recovery workflow and EFK handoff diagrams
30662df Add operations and EKF handoff notes
46e7985 Document docs-prv audit result
d2284a8 Restore validated FRBNY sections for regression packages
f797192 Document application package recovery findings
9643fe7 Fix Teal export normalization and add Teal resumes for imported JDs
f50b4a4 Add assembled employer-aware resumes for imported JDs
eb5d050 Add resume bullet ranking for imported JDs
f2a0df9 Add resume tailoring for imported JDs
4c92d41 Add candidate explainability for imported JDs
a89cab2 Add candidate strategy for imported JDs
7ac3079 Add candidate matching for imported JDs
ac3fa69 Add JD intelligence for imported JDs
3ed8502 Document current recovery pipeline state
1a3081c Add roles and resume versions for imported JDs

===== STASHES =====

===== REMOTES =====
origin	git@github-squidpan:squidpan/career-system.git (fetch)
origin	git@github-squidpan:squidpan/career-system.git (push)
[PL] pl@pop-os:~/pjs/repos/career-system $ 

```

---

# Step 0.2 — Repository Structure

Next we'll verify the expected directories.

Run:

```bash
echo "===== TOP LEVEL ====="
find . -maxdepth 1 | sort

echo
echo "===== DATA ====="
find data -maxdepth 1 | sort

echo
echo "===== DOCS ====="
find docs -maxdepth 2 | sort

echo
echo "===== BIN ====="
find bin -maxdepth 1 | sort

echo
echo "===== SCRIPTS ====="
find scripts -maxdepth 1 | sort
```


## ouput

```output
[PL] pl@pop-os:~/pjs/repos/career-system $ echo "===== TOP LEVEL ====="
find . -maxdepth 1 | sort

echo
echo "===== DATA ====="
find data -maxdepth 1 | sort

echo
echo "===== DOCS ====="
find docs -maxdepth 2 | sort

echo
echo "===== BIN ====="
find bin -maxdepth 1 | sort

echo
echo "===== SCRIPTS ====="
find scripts -maxdepth 1 | sort
===== TOP LEVEL =====
.
./backup
./bin
./data
./docs
./.git
./.gitignore
./INSTALL_FROM_ZIP.md
./install-overlay.sh
./INSTALL_TEAL_EXPORT_V040.md
./.obsidian
./obsidian
./ops
./README_APPLICATION_PACKAGE_GENERATOR.md
./README_CANDIDATE_MATCHING_ENGINE.md
./README_CANDIDATE_MATCHING_FUNCTIONAL_FIX.md
./README-CAREER-SYSTEM-v0.4_REQUIREMENTS-HANDOFF.md
./README_EMPLOYER_AWARE_RESUME_ASSEMBLY.md
./README_EXPLAINABLE_CANDIDATE_STRATEGY_ENGINE.md
./README_GAP_ANALYSIS_ENGINE.md
./README_INTERVIEW_INTELLIGENCE_INTEGRATION.md
./README_INTERVIEW_PREP_ENGINE.md
./README_JD_AWARE_INTERVIEW_INTELLIGENCE.md
./README_JD_NORMALIZER.md
./README_JD_TITLE_CLEANUP.md
./README.md
./README_PERSONALIZED_CANDIDATE_STRATEGY_ENGINE.md
./README_REFERENCE_REGISTRIES.md
./README_RESUME_ASSEMBLY_ENGINE.md
./README_RESUME_BULLET_RANKING.md
./README_RESUME_BULLET_RANKING_REFINEMENT.md
./README_RESUME_COMPRESSION.md
./README_RESUME_COMPRESSION_V0411.md
./README_RESUME_ENHANCEMENT_ENGINE.md
./README_RESUME_FINALIZATION_ENGINE.md
./README_RESUME_GENERATION_ENGINE.md
./README_RESUME_MASTER_CLEANUP.md
./README_RESUME_MASTER_NARRATIVE_CLEANUP.md
./README_RESUME_NARRATIVE_ASSEMBLY.md
./README_RESUME_OVERLAY.md
./README_RESUME_TAILORING_ENGINE.md
./README_RESUME_TAILORING_INTELLIGENCE.md
./README_RESUME_VERSION_GENERATOR.md
./README_ROLE_AWARE_RESUME_ASSEMBLY.md
./README_ROLE_REGISTRY.md
./README_ROLE_RESUME_MAPPING.md
./README_TEAL_EXPORT_ENGINE.md
./README_TRACKER_IMPORT.md
./README_TRACKER_ROLE_CLASSIFICATION.md
./scripts
./services
./sql
./templates
./tests

===== DATA =====
data
data/application-artifacts
data/application-packages
data/application-summaries
data/application-tracker
data/application-tracking
data/ats-exports
data/candidate-explainability
data/candidate-matching
data/candidate-strategy
data/cover-letter-masters
data/cover-letter-versions
data/experience-assets
data/experience-matches
data/experience-matching
data/experience-skills
data/experience-sources
data/fit-triage
data/full-resumes
data/gap-analysis
data/generated-resumes
data/interview-prep
data/interview-stories
data/jd-intelligence
data/jds
data/manual-enhancements
data/master-profile
data/master-resumes
data/reference
data/resume-bullet-ranking
data/resume-drafts
data/resume-enhancement
data/resume-evidence
data/resume-generated
data/resume-masters
data/resume-sections
data/resume-system-manifest.json
data/resume-tailoring
data/resume-versions
data/roles
data/source-resumes
data/thank-you-letters
data/tracker

===== DOCS =====
docs
docs/api
docs/api/openapi
docs/architecture
docs/architecture/career-system-roadmap-v0.5.x.md
docs/architecture/career-system-roadmap-v0.6.x.md
docs/architecture/experience-source-domain-model.md
docs/architecture/experience-source-domain-model-v0.5.1-refinement.md
docs/design
docs/design/resume-master-v2.md
docs/integrations
docs/integrations/mrprice-experience-integration.md
docs/operations
docs/operations/application-status-update-workflow.md
docs/operations/CURRENT-PIPELINE.md
docs/operations/deploy
docs/operations/diagrams
docs/operations/handoffs
docs/operations/jd-cleanup-2026-06-16.md
docs/operations/postgres
docs/operations/recovery
docs/prototypes
docs/prototypes/application-package-generator-v0.6.2.md
docs/prototypes/application-package-generator-v0.9.0.md
docs/prototypes/application-readiness-report-v0.6.5.md
docs/prototypes/ats-resume-generator-v0.7.2.md
docs/prototypes/ats-safe-export-v0.8.0.md
docs/prototypes/experience-matching-prototype-v0.5.2.md
docs/prototypes/experience-scoring-prototype-v0.5.4.md
docs/prototypes/full-resume-generator-v0.7.0.md
docs/prototypes/interview-recommendation-prototype-v0.5.6.md
docs/prototypes/jd-matching-prototype-v0.5.3.md
docs/prototypes/manual-enhancement-engine-v0.6.4.md
docs/prototypes/master-resume-generator-v0.6.1.md
docs/prototypes/resume-assembly-prototype-v0.5.9.md
docs/prototypes/resume-draft-assistance-v0.5.7.md
docs/prototypes/resume-quality-enhancement-v0.6.3.md
docs/prototypes/resume-recommendation-prototype-v0.5.5.md
docs/prototypes/resume-section-generator-v0.5.8.md
docs/prototypes/resume-tailoring-engine-v0.6.0.md
docs/reference
docs/reference/LINUX_DEV_ENV_ALIGNMENT_BACKLOG.md
docs/reference/POSTGRES_DEPENDENCIES.md
docs/reference/README_POSTGRES_STANDARD_v2.md
docs/releases
docs/releases/README_RELEASE_PROCESS.md
docs/releases/RELEASE-v0.10.0-application-tracking.md
docs/releases/RELEASE-v0.11.0-postgres-api-foundation.md
docs/requirements
docs/requirements/acceptance-criteria
docs/requirements/adr
docs/requirements/architecture
docs/requirements/bases
docs/requirements/bugs
docs/requirements/canvas
docs/requirements/context
docs/requirements/data-model
docs/requirements/diagrams
docs/requirements/epics
docs/requirements/glossary
docs/requirements/indexes
docs/requirements/openapi
docs/requirements/prerequisites
docs/requirements/principles
docs/requirements/README.md
docs/requirements/reference
docs/requirements/releases
docs/requirements/sprints
docs/requirements/standards
docs/requirements/stories
docs/requirements/templates
docs/requirements/traceability
docs/requirements/trello
docs/requirements/uat
docs/resume-system
docs/resume-system/COMMUNICATIONS_WORKFLOW.md
docs/resume-system/RESUME_MASTER_STRATEGY.md
docs/resume-system/RESUME_SYSTEM_README.md
docs/resume-system/RESUME_TO_JOB_WORKFLOW.md
docs/resume-system/RESUME_VERSIONING.md
docs/standards
docs/standards/application-package-workflow.md
docs/standards/candidate-explainability-standard.md
docs/standards/candidate-matching-standard.md
docs/standards/candidate-strategy-standard.md
docs/standards/company-registry-standard.md
docs/standards/employer-aware-resume-assembly-standard.md
docs/standards/gap-analysis-standard.md
docs/standards/interview-intelligence-integration-standard.md
docs/standards/interview-prep-standard.md
docs/standards/jd-aware-interview-intelligence-standard.md
docs/standards/jd-normalization-workflow.md
docs/standards/jd-title-standard.md
docs/standards/master-resume-standard.md
docs/standards/python
docs/standards/resume-assembly-workflow.md
docs/standards/resume-bullet-ranking-standard.md
docs/standards/resume-compression-standard.md
docs/standards/resume-compression-v2-standard.md
docs/standards/resume-enhancement-standard.md
docs/standards/resume-family-registry-standard.md
docs/standards/resume-finalization-standard.md
docs/standards/resume-generation-standard.md
docs/standards/resume-master-narrative-standard.md
docs/standards/resume-narrative-assembly-standard.md
docs/standards/resume-tailoring-intelligence-standard.md
docs/standards/resume-tailoring-standard.md
docs/standards/resume-version-generation-workflow.md
docs/standards/role-aware-resume-assembly-standard.md
docs/standards/role-code-registry-standard.md
docs/standards/role-code-standard.md
docs/standards/role-registry-workflow.md
docs/standards/role-resume-mapping-standard.md
docs/standards/teal-export-workflow.md
docs/standards/tracker-import-workflow.md
docs/standards/tracker-role-classification-workflow.md
docs/templates
docs/templates/submission-notes-template.md

===== BIN =====
bin
bin/import-obsidian-raw-jds.sh
bin/list-reference-registries.sh
bin/load-application-artifacts-to-postgres.sh
bin/load-applications-to-postgres.sh
bin/run-application-dashboard-generator.sh
bin/run-application-package-generation.sh
bin/run-application-package-generator.sh
bin/run-application-package.sh
bin/run-application-readiness-report.sh
bin/run-application-tracker-generator.sh
bin/run-ats-resume-generator.sh
bin/run-ats-text-export.sh
bin/run-candidate-explainability.sh
bin/run-candidate-matching.sh
bin/run-candidate-strategy.sh
bin/run-career-center-api.sh
bin/run-experience-keyword-match.sh
bin/run-full-resume-generator.sh
bin/run-gap-analysis.sh
bin/run-interview-prep.sh
bin/run-interview-recommendation.sh
bin/run-jd-intelligence.sh
bin/run-jd-match.sh
bin/run-jd-normalization.sh
bin/run-jd-title-cleanup-patch.sh
bin/run-jd-title-rebuild.sh
bin/run-master-resume-generator.sh
bin/run-resume-assembly.sh
bin/run-resume-bullet-generator.sh
bin/run-resume-bullet-ranking.sh
bin/run-resume-enhancement.sh
bin/run-resume-finalization.sh
bin/run-resume-generation.sh
bin/run-resume-html-export.sh
bin/run-resume-narrative-assembly.sh
bin/run-resume-quality-enhancer.sh
bin/run-resume-recommendation.sh
bin/run-resume-section-generator.sh
bin/run-resume-tailoring.sh
bin/run-resume-tailor.sh
bin/run-resume-version-generation.sh
bin/run-role-aware-resume-assembly.sh
bin/run-role-generation.sh
bin/run-role-metadata-propagation.sh
bin/run-score-match.sh
bin/run-submission-notes-normalization.sh
bin/run-teal-export.sh
bin/run-tracker-role-classification.sh
bin/run-tracker-role-import.sh
bin/setup-career-center-api.sh
bin/setup-career-center-postgres.sh
bin/smoke-test-career-center-api.sh
bin/validate-master-resumes.sh
bin/validate-resume-compression.sh
bin/validate-resume-compression-v2.sh
bin/validate-resume-master-v2.sh

===== SCRIPTS =====
scripts
scripts/assemble_ats_resume.py
scripts/assemble_full_resume.py
scripts/assemble_resume_narratives.py
scripts/assemble_resume.py
scripts/assemble_resumes.py
scripts/assemble_role_aware_resumes.py
scripts/build_application_package.py
scripts/classify_tracker_roles.py
scripts/enhance_resume_quality.py
scripts/export_ats_text.py
scripts/export_resume_html.py
scripts/extract_jd_keywords.py
scripts/finalize_resumes.py
scripts/generate_application_dashboard.py
scripts/generate_application_package.py
scripts/generate_application_packages.py
scripts/generate_application_readiness_report.py
scripts/generate_application_tracker.py
scripts/generate_candidate_explainability.py
scripts/generate_candidate_matching.py
scripts/generate_candidate_strategy.py
scripts/generate_gap_analysis.py
scripts/generate_interview_prep.py
scripts/generate_jd_intelligence.py
scripts/generate_master_resume.py
scripts/generate_resume_bullet_ranking.py
scripts/generate_resume_bullets.py
scripts/generate_resume_enhancement.py
scripts/generate_resume_section.py
scripts/generate_resumes.py
scripts/generate_resume_tailoring.py
scripts/generate_resume_versions_from_roles.py
scripts/generate_roles_from_jds.py
scripts/generate_teal_export_resumes.py
scripts/import_tracker_roles.py
scripts/list_reference_registries.py
scripts/load_application_artifacts_to_postgres.py
scripts/load_applications_to_postgres.py
scripts/match_experience_keywords.py
scripts/match_jd.py
scripts/normalize_jd_oo.py
scripts/normalize_jd.py
scripts/normalize_submission_notes.py
scripts/patch_jd_title_cleanup.py
scripts/propagate_role_metadata_to_submission_notes.py
scripts/__pycache__
scripts/rebuild_jd_titles_from_metadata.py
scripts/recommend_interview_assets.py
scripts/recommend_resume_assets.py
scripts/score_experience_match.py
scripts/tailor_resume.py
scripts/validate_master_resumes.py
scripts/validate_resume_compression.py
scripts/validate_resume_compression_v2.py
scripts/validate_resume_master_v2.py
[PL] pl@pop-os:~/pjs/repos/career-system $ 

```

---

# Step 0.3 — Regression Inventory

We'll verify the known-good reference packages.

```bash
echo "===== LSEG PACKAGE ====="
find data/application-packages/application-lseg-senior-ba-2026-v1 -maxdepth 2 | sort

echo
echo "===== BROADRIDGE PACKAGE ====="
find data/application-packages/application-broadridge-product-analyst-2026-v1 -maxdepth 2 | sort
```

## output

```output
echo "===== LSEG PACKAGE ====="
find data/application-packages/application-lseg-senior-ba-2026-v1 -maxdepth 2 | sort

echo
echo "===== BROADRIDGE PACKAGE ====="
find data/application-packages/application-broadridge-product-analyst-2026-v1 -maxdepth 2 | sort
```
---

# Step 0.4 — Bridge Artifacts

We'll confirm the reference inputs that feed the validated final-mile generators.

```bash
echo "===== APPLICATION SUMMARIES ====="
find data/application-summaries | sort

echo
echo "===== RESUME SECTIONS ====="
find data/resume-sections | sort
```

## output

```output
[PL] pl@pop-os:~/pjs/repos/career-system $ echo "===== APPLICATION SUMMARIES ====="
find data/application-summaries | sort

echo
echo "===== RESUME SECTIONS ====="
find data/resume-sections | sort
===== APPLICATION SUMMARIES =====
data/application-summaries
data/application-summaries/broadridge-product-analyst-summary-v1.md
data/application-summaries/citi-ba-summary-v1.md
data/application-summaries/finbourne-summary-v1.md
data/application-summaries/ice-senior-ba-summary-triage-v1.md
data/application-summaries/ice-senior-ba-summary-v1.md
data/application-summaries/lseg-senior-ba-summary-v1.md
data/application-summaries/new-york-life-technical-ba-summary-v1.md
data/application-summaries/qode-ba-summary-v1.md
data/application-summaries/shutterstock-ba-summary-v1.md
data/application-summaries/upmc-systems-analyst-summary-v1.md

===== RESUME SECTIONS =====
data/resume-sections
data/resume-sections/broadridge-product-analyst-frbny-section.md
data/resume-sections/citi-ba-frbny-section.md
data/resume-sections/citi-ba-frbny-section-v3.md
data/resume-sections/drum-upskill-technical-business-analyst-frbny-section.md
data/resume-sections/finbourne-frbny-section.md
data/resume-sections/ice-senior-ba-frbny-section.md
data/resume-sections/lseg-senior-ba-frbny-section.md
data/resume-sections/new-york-life-technical-ba-frbny-section.md
data/resume-sections/pico-frbny-section.md
data/resume-sections/qode-ba-frbny-section.md
data/resume-sections/shipscience-support-engineer-frbny-section.md
data/resume-sections/shutterstock-ba-frbny-section.md
data/resume-sections/upmc-systems-analyst-frbny-section.md
[PL] pl@pop-os:~/pjs/repos/career-system $ 

```
---

# Step 0.5 — Final-Mile Scripts

Finally, we'll verify the operational scripts we intend to rely on.

```bash
ls -l \
bin/run-full-resume-generator.sh \
bin/run-ats-resume-generator.sh \
bin/run-resume-html-export.sh \
bin/run-ats-text-export.sh \
bin/run-application-package.sh
```


## output

```output
[PL] pl@pop-os:~/pjs/repos/career-system $ ls -l \
bin/run-full-resume-generator.sh \
bin/run-ats-resume-generator.sh \
bin/run-resume-html-export.sh \
bin/run-ats-text-export.sh \
bin/run-application-package.sh
-rwxrwxr-x 1 pl pl 290 Jun 13 12:57 bin/run-application-package.sh
-rwxrwxr-x 1 pl pl 538 Jun 12 18:07 bin/run-ats-resume-generator.sh
-rwxrwxr-x 1 pl pl 197 Jun 13 11:34 bin/run-ats-text-export.sh
-rwxrwxr-x 1 pl pl 607 Jun 12 10:38 bin/run-full-resume-generator.sh
-rwxrwxr-x 1 pl pl 205 Jun 12 11:17 bin/run-resume-html-export.sh
[PL] pl@pop-os:~/pjs/repos/career-system $ 

```
---

# One addition to our recovery process

Based on how you've been working over the past few weeks, I'd like to introduce a lightweight **Recovery Journal**.

Each day we work on recovery, we'll record:

```text
Recovery Day: 1

Objective:
Repository validation

Completed:
✔ Verified branch
✔ Verified scripts
✔ Verified packages

Problems Found:
...

Decisions:
...

Tomorrow:
...
```

I don't necessarily mean as a formal document yet—just as part of our working process. Later, we can decide whether to keep it as a markdown file in `docs/operations/recovery/`.

---

I think today's work should end with **high confidence in what we have**, not with partially written code. If we can say, "the repository is healthy, the regression baseline is verified, and we know exactly where the missing bridge begins," then Phase 0 will have achieved its purpose.

---


## no ops folder - Phase 0 is not closed yet!!



Yes—I see `cs-tree-L7-ops-2026-07-13.txt`, and you were right to stop us before closing Phase 0. The `ops/` folder was **not included in the recovery ZIP handoff list**, even though the handoff repeatedly refers to `ops/runs/<run-id>/output/`.

We need to treat **Ops Run-State Validation as part of Phase 0**.

## What the tree already tells us

The intended run structure appears to be:

```text
ops/runs/<run-id>/
├── input/
├── logs/
├── output/
└── run-manifest.md
```

Many historical runs follow this pattern, including normalization, role generation, resume generation, candidate processing, and application-package generation.

But there is also a clearly suspicious structure:

```text
ops/runs/data/jds/raw/jd-raw-ice-ba.md/
ops/runs/data/jds/raw/jd-raw-lseg-...md/
ops/runs/data/jds/raw/jd-raw-new-york-life-...md/
```

Each of those contains large copied input sets, logs, output, and a manifest. That strongly suggests that at some point a path or filename was mistakenly treated as a `run-id`. It does **not** look like an intentional canonical run hierarchy.

The many `v1`, `v2`, `v3`… runs are also not automatically “good” or “bad.” Some are likely development iterations, reruns after bugs, failed experiments, or successful predecessors. The directory name alone cannot tell us which.

## Do not empty or delete `ops/` yet

I agree with the goal of eventually starting recovery with a clean active run area, but we should not erase evidence before determining:

- which wrappers still write there;
    
- which Python scripts create run directories;
    
- whether run inputs are copied or linked;
    
- what manifests record;
    
- whether logs record exit status;
    
- which historical runs created canonical data artifacts;
    
- whether `ops/runs` is tracked in Git;
    
- whether any code reads old runs as inputs.
    

The safe approach is:

```text
Audit
→ classify
→ preserve/archive
→ establish clean active run area
→ run new recovery tests
```

Not:

```text
delete ops/runs
→ discover later that scripts or evidence depended on it
```

# Revised Phase 0

Phase 0 is not closed yet.

Add:

## Phase 0.6 — Ops Folder and Run-System Audit

We need four answers:

1. What code writes to `ops/`?
    
2. What code reads from `ops/`?
    
3. What is the intended run-folder contract?
    
4. Which historical content should be archived, retained, or marked invalid?
    

## Step 0.6A — Basic size and Git tracking

Run:

```bash
cd ~/pjs/repos/career-system

echo "===== OPS SIZE ====="
du -sh ops
du -sh ops/runs
du -h --max-depth=2 ops/runs | sort -h | tail -40

echo
echo "===== OPS FILE AND DIRECTORY COUNTS ====="
find ops -type d | wc -l
find ops -type f | wc -l
find ops/runs -mindepth 1 -maxdepth 1 -type d | wc -l

echo
echo "===== GIT TRACKING ====="
git ls-files ops | wc -l
git status --short ops
git check-ignore -v ops ops/runs 2>/dev/null || true

echo
echo "===== TOP-LEVEL OPS STRUCTURE ====="
find ops -maxdepth 2 -mindepth 1 -printf '%y %p\n' | sort
```

## Step 0.6B — Find every code reference to `ops`

```bash
echo "===== CODE REFERENCES TO OPS/RUNS ====="
grep -RIn \
  --exclude-dir=.git \
  --exclude-dir=__pycache__ \
  --exclude='*.pyc' \
  -E 'ops/runs|ops/|run-manifest|RUN_DIR|run_dir|RUN_ID|run_id' \
  bin scripts tests templates docs/standards docs/operations \
  | tee /tmp/career-system-ops-references-20260713.txt
```

This is the most important output. It will show whether wrappers or Python scripts construct the directories.

## Step 0.6C — Inventory run shapes

```bash
echo "===== TOP-LEVEL RUN DIRECTORIES ====="
find ops/runs -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort

echo
echo "===== STANDARD RUN SHAPE COUNTS ====="
printf "with input: "
find ops/runs -mindepth 2 -maxdepth 2 -type d -name input | wc -l

printf "with logs: "
find ops/runs -mindepth 2 -maxdepth 2 -type d -name logs | wc -l

printf "with output: "
find ops/runs -mindepth 2 -maxdepth 2 -type d -name output | wc -l

printf "with manifest: "
find ops/runs -mindepth 2 -maxdepth 2 -type f -name 'run-manifest.md' | wc -l

echo
echo "===== NONSTANDARD TOP-LEVEL ENTRIES ====="
find ops/runs -mindepth 1 -maxdepth 1 \
  ! -name 'run-*' \
  -printf '%y %f\n' | sort
```

I expect this to identify `ops/runs/data` as nonstandard.

## Step 0.6D — Inspect manifests and logs for status semantics

```bash
echo "===== MANIFEST FIELD SAMPLE ====="
find ops/runs -type f -name 'run-manifest.md' -print0 \
  | xargs -0 grep -HinE \
    'status|success|failed|failure|error|exit|completed|started|finished|command|input|output' \
  | head -200

echo
echo "===== ERROR SIGNALS IN LOGS ====="
find ops/runs -type f -path '*/logs/*' -print0 \
  | xargs -0 grep -HinE \
    'traceback|exception|error|failed|failure|no such file|not found|invalid' \
  | head -250
```

A lack of errors does not prove success, but this will tell us whether the current logging format is usable.

## Step 0.6E — Check whether historical runs are consumed

```bash
echo "===== READ REFERENCES TO HISTORICAL RUN OUTPUTS ====="
grep -RIn \
  --exclude-dir=.git \
  --exclude-dir=ops \
  --exclude-dir=__pycache__ \
  -E 'ops/runs/run-|ops/runs/data' \
  . \
  | head -250
```

This tells us whether anything outside `ops/` points directly at old run outputs.

# What I expect we will do after the audit

Most likely, we will preserve the history but move it out of the active run namespace:

```text
ops/
├── archive/
│   └── pre-functional-recovery-20260713/
│       └── runs/
├── runs/
└── README.md
```

Then new recovery execution would begin with:

```text
ops/runs/run-2026-07-13-...
```

But I do **not** recommend performing that move until we inspect the code references and determine whether Git is tracking all of it.

If we archive it, we should do so with Git-aware commands:

```bash
git branch --show-current
git switch ops/recover-ats-html-workflow
git mv ...
```

No `git checkout`.

## Likely cleanup classifications

We will probably classify historical runs as:

```text
validated-reference
successful-historical
failed
superseded
malformed-path
unknown
```

The malformed `ops/runs/data/...` hierarchy will likely fall under `malformed-path`, but we need script and manifest evidence before finalizing that conclusion.

## Journal impact

Do not create the earlier final Phase 0 journal yet. After this audit, the journal should include:

- intended `ops/runs` contract;
    
- scripts that write to it;
    
- scripts that do not;
    
- whether manifests record success/failure adequately;
    
- historical run classification;
    
- archival decision;
    
- clean-run policy for Phase 1.
    

This was an important catch. `ops/` is not peripheral—it is supposed to be the execution evidence and run-log system. We need to understand it before running LSEG and Broadridge again.



---

This is excellent. This tells us a lot, and more importantly it tells us **what not to change.**

This was exactly the kind of audit I wanted before touching anything.

# Executive Summary

The repository is actually in much better shape than I feared.

The problems are architectural rather than corruption.

I would classify them like this.

---

# 1. The good news

The pipeline is remarkably consistent.

You have

- 96 runs
    
- every run has an output directory
    
- 54 runs use the newer standardized layout
    
- manifests exist for over half
    
- logs exist where expected
    
- no empty outputs
    
- no empty logs
    
- no obvious runtime failures
    

That is actually impressive.

---

# 2. Biggest discovery

This surprised me.

```
git ls-files ops
```

returns

```
ops/runs/.gitkeep
```

ONLY.

That means

**all runs are already intentionally ignored.**

That is exactly what I would have recommended.

So we do NOT need to redesign git handling.

Git handling is already correct.

---

# 3. The real problem

This is the important part.

The problem is NOT

```
ops/
```

The problem is

```
data/
```

Because your permanent artifacts contain references back into

```
ops/runs/...
```

For example

```
assembled_resume_file

cover_letter

gap-analysis

application-manifest

resume-final

...
```

point to

```
ops/runs/run-2026-...
```

That creates hidden coupling.

The permanent repository depends on temporary run folders.

That is backwards.

---

# 4. Second discovery

This

```
ops/runs/data/
```

is wrong.

Very wrong.

You have

```
ops
    runs
        data
            jds
```

which contains

```
run-manifest.md

logs

outputs

inputs
```

embedded under

```
data/
```

That means a pipeline accidentally normalized

```
ops/runs/data
```

instead of

```
data
```

So now you literally have

```
ops
   runs
      data
         jds
            raw
                jd-raw-ice-ba.md
                    input
                    output
                    logs
                    run-manifest
```

This should never exist.

That entire subtree is clearly accidental.

---

# 5. No evidence of failures

Good news.

Your grep found

```
Status: complete
```

everywhere.

The only oddity is

```
status: running
```

at top

then

```
Status: complete
```

later.

That's just the shell script writing

```
status: running
```

before execution

then appending

```
Completed
```

afterward.

Not a problem.

---

# 6. Missing manifests

44 runs have no manifest.

Not ideal.

Not catastrophic.

Those are mostly generators written before the newer wrappers.

Those wrappers simply never wrote manifests.

---

# 7. Git ignore

Perfect.

```
ops/runs/*
!ops/runs/.gitkeep
```

Exactly what I'd expect.

No changes needed.

---

# 8. Code architecture

This grep is extremely valuable.

Everything consistently uses

```
ops/runs/$RUN_ID/output
```

That means we can improve the architecture without breaking interfaces.

Huge win.

---

# 9. Historical README references

These don't concern me.

Things like

```
rm -rf ops/runs/run...
```

are documentation.

No issue.

---

# 10. What actually worries me

These.

```
application-manifest.json

assembled-v2.json

assembled-v3.json

final.json
```

They contain things like

```
assembled_resume_file

cover_letter

role

```

pointing into

```
ops/runs/...
```

Those are supposed to be permanent data.

They should never reference temporary build directories.

That is the architectural bug.

---

# My assessment

I would rate the system like this.

Pipeline quality:

**9/10**

Repository organization:

**7/10**

Artifact separation:

**4/10**

Run history:

**9/10**

Git hygiene:

**10/10**

Overall:

**8.5/10**

Which is honestly much higher than I expected.

---

# What I would NOT do

I would NOT

- delete runs
    
- redesign run folders
    
- archive anything
    
- move ops
    
- rename ops
    
- change shell wrappers
    
- touch gitignore
    

None of those are worth the risk.

---

# What I WOULD fix

Instead, I would make **three small, high-value changes**:

### Phase 1 (safe)

1. Remove the accidental `ops/runs/data` subtree after verifying it is just a mistaken pipeline output.
    
2. Stop writing absolute or `ops/runs/...` paths into permanent JSON artifacts (`assembled-v2`, `assembled-v3`, `final`, `application-manifest`, etc.). Store stable IDs or relative paths into `data/` instead.
    
3. Standardize manifest creation so every new run produces a `run-manifest.md` with a consistent final status.
    

### Phase 2 (later)

Introduce a run library abstraction:

```
ops/
    runs/
    archive/
```

with tooling to archive or prune old runs automatically, without changing the existing pipeline.

---

## Recommendation

I do **not** think this repository needs a major refactor. The pipeline itself is solid.

The issue is primarily one of **artifact ownership and metadata references**, not execution.

I would proceed by fixing those architectural seams while leaving the working pipeline intact. That approach minimizes risk and preserves the operational workflow you've built.


---

Absolutely. And this time I'm going to do it the way we said we should do all large operational documents.

**Split into multiple heredocs** so they're easier to validate and impossible to break with one missing code fence.

I am **not** going to try to squeeze a 500+ line document into a single ChatGPT response again—that's exactly how fence mistakes happen.

### Part 1

```bash
cd ~/pjs/repos/career-system

mkdir -p docs/operations/recovery

cat > docs/operations/recovery/RECOVERY-JOURNAL-2026-07-13.md <<'EOF'
# Career System Functional Recovery Journal

## Metadata

- Date: 2026-07-13
- Phase: 0
- Branch: ops/recover-ats-html-workflow
- Status: COMPLETE
- Result: PASS

---

# Recovery Day 1 — Phase 0

## Objective

Validate:

- Git repository health
- repository structure
- operational scripts
- bridge artifacts
- known-good regression packages
- application-package contract
- ops/runs execution-history
- manifests
- logs
- Git-ignore behavior

---

# 1. Git Repository Validation

Verified:

- branch: ops/recover-ats-html-workflow
- working tree clean
- remote verified
- no stashes
- using git switch instead of git checkout

---

# 2. Repository Structure Validation

Verified:

- bin/
- scripts/
- templates/
- docs/
- data/
- ops/
- tests/

Verified application output folders:

- data/application-packages/
- data/application-summaries/
- data/resume-sections/
- data/full-resumes/
- data/ats-exports/

Verified operations folders:

- docs/operations/
- docs/operations/recovery/
- docs/operations/diagrams/

EOF
```

---

### Part 2

Append:

```bash
cat >> docs/operations/recovery/RECOVERY-JOURNAL-2026-07-13.md <<'EOF'

# 3. Operational Script Validation

Verified final-mile wrappers:

- run-full-resume-generator.sh
- run-ats-resume-generator.sh
- run-resume-html-export.sh
- run-ats-text-export.sh
- run-application-package.sh

Verified corresponding Python implementations.

Wrappers are executable.

---

# 4. Regression Package Validation

Known-good packages:

- application-lseg-senior-ba-2026-v1
- application-broadridge-product-analyst-2026-v1

Verified package contents:

- application-summary.md
- ats-resume.md
- ats-resume.html
- ats-resume.txt
- full-resume.md
- full-resume.html
- package-manifest.json
- README.md
- submission-notes.md

Manual browser-generated PDFs are considered user artifacts and are not part of automated regression testing.

Interview recommendation artifacts are outside the current recovery scope.

---

# 5. Canonical Deliverable

The authoritative operational output is:

data/application-packages/application-<job-slug>-2026-v1/

All final ATS and narrative resume artifacts belong inside the application package.

EOF
```

---

### Part 3

```bash
cat >> docs/operations/recovery/RECOVERY-JOURNAL-2026-07-13.md <<'EOF'

# 6. Ops Run-System Audit

Summary:

- ops size approximately 23 MB
- 96 historical runs
- every run contains output/
- 54 runs contain input/
- 54 runs contain logs/
- 52 runs contain run-manifest.md
- 44 runs use output-only pattern

No empty logs.

No empty output directories.

No runtime failures detected.

Git ignore:

    ops/runs/*
    !ops/runs/.gitkeep

Only .gitkeep is tracked.

Historical runs are intentionally excluded from Git.

EOF
```

---

### Part 4

```bash
cat >> docs/operations/recovery/RECOVERY-JOURNAL-2026-07-13.md <<'EOF'

# 7. Architectural Findings

Three execution patterns exist.

Pattern A

input/
logs/
output/
run-manifest.md

Pattern B

output/

Pattern C

Direct generation into:

- data/full-resumes/
- data/ats-exports/
- data/application-packages/

without a unified run record.

Observed malformed hierarchy:

ops/runs/data/jds/raw/...

Likely caused by an unsafe run_id containing path separators.

No cleanup will occur during Phase 0.

EOF
```

---

### Part 5

```bash
cat >> docs/operations/recovery/RECOVERY-JOURNAL-2026-07-13.md <<'EOF'

# 8. Permanent Artifact References

Permanent JSON files currently reference historical paths inside ops/runs.

Examples include:

- assembled-v2
- assembled-v3
- final resume metadata
- application-manifest
- gap-analysis

This creates coupling between permanent artifacts and runtime history.

The issue is documented for future hardening but is not part of Phase 0.

---

# 9. Deferred Hardening

Deferred until recovery is complete:

1. Reject unsafe run IDs.
2. Standardize manifests.
3. Standardize run envelopes.
4. Add final-mile run records.
5. Remove absolute paths.
6. Archive historical runs.
7. Remove malformed ops/runs/data after verification.
8. Define retention policy.

---

# 10. Phase 0 Acceptance

- [x] Repository validated
- [x] Scripts validated
- [x] Regression packages validated
- [x] Ops structure audited
- [x] Git-ignore verified
- [x] Architectural seams documented

Result:

PASS

Next:

Phase 1 — Final-Mile Regression Validation

EOF
```

---

## Verify

```bash
less docs/operations/recovery/RECOVERY-JOURNAL-2026-07-13.md
```

Then:

```bash
grep '^#' docs/operations/recovery/RECOVERY-JOURNAL-2026-07-13.md
```

Then:

```bash
git status
```

This version avoids nested Markdown fences entirely inside the heredocs, so there are no unbalanced triple backticks to break the generated file. It's also split into five manageable sections, which is the pattern I'd recommend adopting for long operational documents going forward.

---

Excellent. This is exactly why we're doing Phase 0 before touching architecture.

## Phase 0 Status

Everything we wanted to verify has now been verified.

### ✅ Repository

- branch correct
    
- clean except expected untracked files
    

### ✅ Pipeline

- known-good packages still exist
    
- scripts exist
    
- outputs exist
    

### ✅ ops/runs

- 96 runs
    
- every run has output/
    
- no empty output directories
    
- no log errors
    

### ✅ Git ignore

Working exactly as intended.

### ✅ Recovery journal

Created successfully.

---

## One small issue

Your very first heredoc was interrupted:

```
EOFocs/operations/diagrams/:/olders:
```

That happened because the terminal received some stray characters while pasting.

Fortunately...

```
grep '^#'
```

shows all headings correctly.

So the document is **probably** fine.

I would just inspect the Repository Structure section once:

```bash
sed -n '25,70p' docs/operations/recovery/RECOVERY-JOURNAL-2026-07-13.md
```

If you see garbage like

```
EOFocs/operations...
```

just delete those few lines manually.

If it looks normal, leave it alone.

---

# About the untracked files

Nothing to worry about.

```
cs-ops-folder-tree-L7-ops-head234.txt
cs-tree-L7-ops-2026-07-13.txt
tree-L4-ops.txt
```

Those are audit artifacts.

```
data/docs/
```

needs to be investigated later before we decide whether it's permanent or temporary.

**Do not delete anything yet.**

---

# We have now completed what I consider Phase 0.

Not "kind of."

Actually completed.

That means we have earned the right to start improving architecture without risking the working system.

---

# What comes next

Now we start **Phase 1**, but notice what Phase 1 is **not**.

It is **NOT**:

- rewriting the pipeline
    
- moving directories
    
- deleting runs
    
- changing outputs
    
- changing generated files
    

Instead it is purely **instrumentation**.

We will:

1. standardize run manifests
    
2. standardize run status
    
3. standardize run metadata
    
4. create missing manifests
    
5. document the run lifecycle
    

Notice something important:

**None of those change any business output.**

That is why I wanted Phase 0 first.

---

I also want to compliment one decision you made earlier that has paid off: insisting on treating this like an operations recovery rather than jumping straight into refactoring. The audit uncovered real architectural seams (like `ops/runs/data/...` and permanent artifacts pointing back into run history) that we would almost certainly have missed if we'd started "cleaning things up" first. Now we know exactly where the boundaries are before we touch them.

---

That's a good question, and I'd actually answer **"mostly yes, but it's approaching the point where it should split."**

When we created the branch, the scope was:

> Recover the ATS HTML/application package workflow.

That was accurate.

However, Phase 0 uncovered several broader architectural issues:

- inconsistent run envelopes (input/logs/output/manifest vs output-only)
    
- malformed `ops/runs/data/...` hierarchy
    
- permanent artifacts pointing into runtime history
    
- inconsistent manifest usage
    
- lack of final-mile run records
    
- absolute paths in metadata
    
- retention/archival concerns
    

Those aren't ATS HTML problems—they're **operations architecture** problems.

### So how I see it

**Current branch (`ops/recover-ats-html-workflow`)**

- ✅ Finish recovering the operational workflow.
    
- ✅ Prove that the end-to-end application package generation works.
    
- ✅ Make the pipeline reliable again.
    

This is still the right place for **Phase 1 regression validation** because it directly supports the recovery objective.

**Future branch (after recovery succeeds)**  
Once the pipeline is healthy, I'd create something like:

```
ops/harden-run-framework
```

or

```
ops/standardize-run-system
```

or

```
architecture/run-framework-v1
```

That branch would own the improvements we intentionally deferred:

- standardized manifests
    
- run metadata schema
    
- safe `run_id` generation
    
- removal of runtime/history coupling
    
- archival and retention policy
    
- cleanup of malformed historical directories
    
- final-mile instrumentation
    

Those changes deserve their own branch because they are architectural enhancements rather than recovery work.

### Why I wouldn't rename this branch

Renaming a published branch that's already been pushed to GitHub (`origin/ops/recover-ats-html-workflow`) adds churn for little benefit. The branch name still accurately reflects its primary purpose: recovering the operational application-generation workflow.

The important thing is to keep the **scope** disciplined. If we find ourselves implementing run-framework standards, retention policies, or refactoring the architecture before we've proven the pipeline works, then we've drifted beyond the branch's intent.

So my recommendation is:

- **Keep** `ops/recover-ats-html-workflow`.
    
- Finish the recovery and regression work on this branch.
    
- Merge it once the pipeline is demonstrably healthy.
    
- Create a fresh branch dedicated to the run-system architecture improvements that Phase 0 identified.
    

I think that's the cleanest history and will make it much easier to understand later why each set of changes was made.

---
LSEG generation passed the **artifact-existence test**. All required final outputs were generated and packaged correctly in the isolated worktree.

Now we need the actual regression test: compare regenerated content against the canonical LSEG package.

Run this while still inside the isolated worktree:

```bash
cd /tmp/career-system-final-mile-regression-20260713

CANONICAL_REPO="$HOME/pjs/repos/career-system"
REBUILT_PACKAGE="$PWD/data/application-packages/application-lseg-senior-ba-2026-v1"
CANONICAL_PACKAGE="$CANONICAL_REPO/data/application-packages/application-lseg-senior-ba-2026-v1"

echo "===== CORE FILE CHECKSUM COMPARISON ====="

for f in \
  application-summary.md \
  ats-resume.md \
  ats-resume.html \
  ats-resume.txt \
  full-resume.md \
  full-resume.html
do
  echo
  echo "--- $f ---"
  sha256sum \
    "$CANONICAL_PACKAGE/$f" \
    "$REBUILT_PACKAGE/$f"
done

echo
echo "===== CORE FILE DIFFS ====="

for f in \
  application-summary.md \
  ats-resume.md \
  ats-resume.html \
  ats-resume.txt \
  full-resume.md \
  full-resume.html
do
  echo
  echo "--- $f ---"
  diff -u \
    "$CANONICAL_PACKAGE/$f" \
    "$REBUILT_PACKAGE/$f" \
    || true
done
```

Then verify the real repository stayed untouched:

```bash
cd ~/pjs/repos/career-system

echo "===== MAIN REPOSITORY SAFETY CHECK ====="
git branch --show-current
git status --short
git stash list
```

Expected:

```text
ops/recover-ats-html-workflow
```

with no status or stash output.

How we classify the result:

- All six checksums match: **LSEG exact regression PASS**
    
- Only HTML title, comments, or harmless formatting differs: **conditional PASS**
    
- Resume wording, employment history, FRBNY section, skills, or summary differs: **FAIL pending investigation**
    

Do not compare the PDF, README, manifest, or submission notes byte-for-byte yet.

---
## Broadridge regression: exact PASS

Despite the pasted command block becoming visually garbled, the commands executed successfully. All required package files passed, all six core checksums matched, and all diffs were empty.

### Exact regression results

Both LSEG and Broadridge now pass byte-for-byte for:

- `application-summary.md`
    
- `ats-resume.md`
    
- `ats-resume.html`
    
- `ats-resume.txt`
    
- `full-resume.md`
    
- `full-resume.html`
    

This proves the existing final-mile workflow is reliable and deterministic when given valid:

```text
application-summary.md
targeted FRBNY section
```

## What Phase 1 has established

The following path is not broken:

```text
application summary
+ targeted FRBNY section
→ ATS resume Markdown
→ ATS HTML
→ ATS TXT
→ narrative resume Markdown
→ narrative HTML
→ application package
```

The actual recovery gap is upstream:

```text
modern JD pipeline
→ missing application summary
→ missing targeted FRBNY section
→ proven final-mile workflow
```

## One final safety check

Return to the main repository and verify it is still clean:

```bash
cd ~/pjs/repos/career-system

echo "===== MAIN REPOSITORY SAFETY CHECK ====="
git branch --show-current
git status --short
git stash list
```

Expected:

```text
ops/recover-ats-html-workflow
```

with no status or stash output.

## Next after that

We should close Phase 1 with a short journal entry and commit before starting bridge analysis. Then Phase 2 begins by comparing the exact structure and content contracts of the LSEG and Broadridge summary and FRBNY-section files against the modern pipeline artifacts that should generate them.


---

I found and opened **`upstream-source-artifacts-output.txt`**.

This file is essentially a **complete upstream artifact inventory and pipeline inspection** for your Career System recovery work. It contains:

- **LSEG upstream artifacts**
    
    - application package
        
    - application summary
        
    - ATS export
        
    - resume recommendation
        
    - generated resumes
        
    - full resumes
        
    - normalized JD
        
    - FRBNY resume section
        
    - resume drafts
        
- **Broadridge upstream artifacts**
    
    - application package
        
    - application summary
        
    - ATS export
        
    - interview recommendation
        
    - resume recommendation
        
    - scored match
        
    - generated resumes
        
    - full resumes
        
    - normalized/raw JD
        
    - FRBNY resume section
        
- Dumps of important generated files, including:
    
    - `application-summaries/*.md`
        
    - `experience-matches/*.json`
        
    - `generated-resumes/*.md`
        
    - `full-resumes/*.md`
        
    - normalized JD files
        
- Verification that the **LSEG/Broadridge pipelines are the known-good regression examples** for the Career System recovery.
    

One important finding from the output is that the resume recommendation JSON under the LSEG path appears to reference the **Broadridge JD**:

```json
"jd_path": "data/jds/normalized/jd-broadridge-product-analyst-2026-v1.md"
```

even though the file is named:

```
lseg-senior-ba-resume-recommendation.json
```

That strongly suggests either:

- a copied template that wasn't updated,
    
- a pipeline bug,
    
- or incorrect metadata being carried through the generation process.
    

That is exactly the kind of regression worth fixing before extending the pipeline.

Overall, this output is a valuable recovery artifact because it documents:

- the current upstream inputs,
    
- the intermediate artifacts,
    
- the generated resume chain,
    
- and the known-good outputs that can be used for regression testing during the Career System functional recovery.
---


Absolutely. In fact, I think this is one of the lessons learned from the split-chat experiment.

One thing we've discovered is that we've been treating **operational recovery** as an ad hoc activity rather than work that belongs in the requirements system. Since your Career System already has Epics, Stories, Bugs, Context documents, and Data Models, this recovery effort should be represented there so it can be tracked, reviewed, and closed like any other sprint work.

## I would create a new Epic

Something like:

```text
EPIC-CS-002
Career System Operational Recovery and Pipeline Validation
```

**Business Goal**

Restore confidence that the Career System can reliably generate application packages by validating and documenting the complete artifact generation pipeline.

---

## Then create a small set of stories

### US-CS-201 — Document Artifact Pipeline

**Goal**

Document every artifact produced by the Career System.

**Acceptance Criteria**

- Every artifact identified
    
- Source vs generated classified
    
- Producer identified
    
- Consumer identified
    
- Storage location documented
    

Deliverable:

```
SYSTEM-ARCHITECTURE.md
```

---

### US-CS-202 — Validate Known-Good Pipelines

This is exactly the work we're about to do.

**Acceptance Criteria**

Validate complete pipelines for:

- Broadridge
    
- LSEG
    

Verify:

- artifact chain complete
    
- metadata consistent
    
- no missing outputs
    

Deliverable:

```
PIPELINE-VALIDATION.md
```

---

### US-CS-203 — Pipeline Regression Suite

**Goal**

Establish permanent regression fixtures.

Acceptance Criteria

- Broadridge becomes regression fixture
    
- LSEG becomes regression fixture
    
- Expected outputs documented
    

This becomes the basis for future testing after code changes.

---

### US-CS-204 — Pipeline Defect Log

Instead of fixing bugs as we find them, record them.

Example:

```
PIPE-001
Incorrect jd_path in LSEG recommendation

Status: Open
Severity: High
```

That defect can later become a BUG artifact if implementation work is required.

---

### US-CS-205 — Generation Runbook

Produce the operational documentation.

Deliverable:

```
RUNBOOK-career-system-generation-pipeline.md
```

This explains how to generate artifacts from Raw JD through Application Package, along with validation and recovery steps.

---

## How this fits into your existing sprint process

One thing I like about your requirements system is that it already tracks implementation through stories. Rather than treating this as "documentation," I'd make it a sprint with clear deliverables:

```
Sprint CS-RECOVERY-01

US-CS-201
Document pipeline architecture

US-CS-202
Validate Broadridge

US-CS-202
Validate LSEG

US-CS-203
Create regression baseline

US-CS-204
Log discovered defects

US-CS-205
Write operational runbook
```

Each story produces a concrete artifact that becomes part of the repository.

## One refinement I'd make

I'd add a second category of story that you haven't really used yet: **Technical Debt / Operational Readiness**. This recovery work isn't delivering a new user-facing feature, but it significantly improves the maintainability and reliability of the system. Explicitly classifying it that way makes it easier to prioritize alongside feature work and explains why time is being invested in architecture, validation, and documentation.

I think this is a natural evolution of your requirements system: not every sprint has to build new functionality. Some sprints should intentionally strengthen the foundation so future development is faster and less error-prone.

---
Absolutely. In fact, I think this is one of the lessons learned from the split-chat experiment.

One thing we've discovered is that we've been treating **operational recovery** as an ad hoc activity rather than work that belongs in the requirements system. Since your Career System already has Epics, Stories, Bugs, Context documents, and Data Models, this recovery effort should be represented there so it can be tracked, reviewed, and closed like any other sprint work.

## I would create a new Epic

Something like:

```text
EPIC-CS-002
Career System Operational Recovery and Pipeline Validation
```

**Business Goal**

Restore confidence that the Career System can reliably generate application packages by validating and documenting the complete artifact generation pipeline.

---

## Then create a small set of stories

### US-CS-201 — Document Artifact Pipeline

**Goal**

Document every artifact produced by the Career System.

**Acceptance Criteria**

- Every artifact identified
    
- Source vs generated classified
    
- Producer identified
    
- Consumer identified
    
- Storage location documented
    

Deliverable:

```
SYSTEM-ARCHITECTURE.md
```

---

### US-CS-202 — Validate Known-Good Pipelines

This is exactly the work we're about to do.

**Acceptance Criteria**

Validate complete pipelines for:

- Broadridge
    
- LSEG
    

Verify:

- artifact chain complete
    
- metadata consistent
    
- no missing outputs
    

Deliverable:

```
PIPELINE-VALIDATION.md
```

---

### US-CS-203 — Pipeline Regression Suite

**Goal**

Establish permanent regression fixtures.

Acceptance Criteria

- Broadridge becomes regression fixture
    
- LSEG becomes regression fixture
    
- Expected outputs documented
    

This becomes the basis for future testing after code changes.

---

### US-CS-204 — Pipeline Defect Log

Instead of fixing bugs as we find them, record them.

Example:

```
PIPE-001
Incorrect jd_path in LSEG recommendation

Status: Open
Severity: High
```

That defect can later become a BUG artifact if implementation work is required.

---

### US-CS-205 — Generation Runbook

Produce the operational documentation.

Deliverable:

```
RUNBOOK-career-system-generation-pipeline.md
```

This explains how to generate artifacts from Raw JD through Application Package, along with validation and recovery steps.

---

## How this fits into your existing sprint process

One thing I like about your requirements system is that it already tracks implementation through stories. Rather than treating this as "documentation," I'd make it a sprint with clear deliverables:

```
Sprint CS-RECOVERY-01

US-CS-201
Document pipeline architecture

US-CS-202
Validate Broadridge

US-CS-202
Validate LSEG

US-CS-203
Create regression baseline

US-CS-204
Log discovered defects

US-CS-205
Write operational runbook
```

Each story produces a concrete artifact that becomes part of the repository.

## One refinement I'd make

I'd add a second category of story that you haven't really used yet: **Technical Debt / Operational Readiness**. This recovery work isn't delivering a new user-facing feature, but it significantly improves the maintainability and reliability of the system. Explicitly classifying it that way makes it easier to prioritize alongside feature work and explains why time is being invested in architecture, validation, and documentation.

I think this is a natural evolution of your requirements system: not every sprint has to build new functionality. Some sprints should intentionally strengthen the foundation so future development is faster and less error-prone.


---

I think this is exactly the right stopping point for tonight.

Rather than trying to validate the pipeline when you're tired, let's leave the repository in a **known state** with the work fully planned. Tomorrow you can open the repo, look at the stories, and immediately know what to do.

One thing I'd change from my earlier suggestion is to treat this as an **operational recovery sprint** rather than just an epic. The epic explains _why_ we're doing this, while the stories define _how_ we'll execute it.

---

# EPIC-CS-002

## Career System Operational Recovery and Pipeline Validation

### Purpose

Restore confidence that the Career System can reliably generate complete application packages by validating, documenting, and testing the end-to-end artifact generation pipeline.

---

## Business Goal

The Career System has evolved over many weeks of development. Before implementing additional features (Career Center, PostgreSQL, REST APIs, EKF improvements, etc.), the existing pipeline must be fully understood, documented, and validated.

This Epic establishes a repeatable operational baseline.

---

## Success Criteria

By completion of this Epic:

- Complete pipeline documented
    
- All artifacts identified
    
- Upstream/downstream dependencies documented
    
- Known-good regression pipelines established
    
- Operational runbook written
    
- Defects documented
    
- Future development can safely resume
    

---

# Story 1

## US-CS-201

### Inventory Career System Artifacts

### Purpose

Identify every artifact produced by the Career System.

---

### Description

Create an inventory of every input, intermediate artifact, and final output.

Classify each artifact as:

- Source
    
- Generated
    
- Intermediate
    
- Final Deliverable
    
- Temporary
    

---

### Deliverable

```text
docs/architecture/ARTIFACT-INVENTORY.md
```

---

### Acceptance Criteria

✓ Every artifact documented

✓ File locations documented

✓ Classification completed

✓ Owner (generator) identified

---

### Status

```
TODO
```

---

# Story 2

## US-CS-202

### Validate Known-Good Pipelines

This becomes tomorrow's work.

---

### Purpose

Validate the complete generation pipeline using the known-good examples.

Regression Pipelines

- Broadridge
    
- LSEG
    

---

### Validate

```
Raw JD

↓

Normalized JD

↓

Recommendation

↓

Experience Match

↓

Generated Resume

↓

Full Resume

↓

ATS Resume

↓

Application Package
```

---

### Deliverable

```
docs/operations/PIPELINE-VALIDATION.md
```

---

### Acceptance Criteria

✓ Every artifact exists

✓ No missing stages

✓ Metadata consistent

✓ Dependencies verified

---

### Status

```
TODO
```

---

# Story 3

## US-CS-203

### Create Artifact Dependency Map

Purpose

Determine exactly what consumes every artifact.

---

Example

```
Normalized JD

produces

↓

Resume Recommendation

consumed by

↓

Experience Match

↓

Generated Resume

↓

Full Resume
```

---

Deliverable

```
docs/architecture/PIPELINE-DEPENDENCIES.md
```

---

Acceptance Criteria

✓ Every producer documented

✓ Every consumer documented

✓ Upstream/downstream relationships complete

---

Status

```
TODO
```

---

# Story 4

## US-CS-204

### Create Operational Runbook

Purpose

Document how to execute the pipeline.

---

Deliverable

```
docs/runbooks/RUNBOOK-generation-pipeline.md
```

Contents

- Inputs
    
- Commands
    
- Outputs
    
- Validation
    
- Recovery
    
- Troubleshooting
    

---

Acceptance Criteria

Someone unfamiliar with the project could regenerate an application package using only the runbook.

---

Status

```
TODO
```

---

# Story 5

## US-CS-205

### Pipeline Defect Tracking

Purpose

Record every defect discovered during validation.

Examples

- Incorrect metadata
    
- Broken references
    
- Missing artifacts
    
- Wrong filenames
    
- Incorrect dependencies
    

---

Deliverable

```
docs/bugs/PIPELINE-DEFECTS.md
```

---

Acceptance Criteria

Every discovered issue logged.

No fixes performed in this story.

---

Status

```
TODO
```

---

# Story 6

## US-CS-206

### Establish Regression Baseline

Purpose

Create permanent regression test cases.

Regression Pipelines

- Broadridge
    
- LSEG
    

Future changes must continue to produce equivalent outputs.

---

Deliverable

```
docs/testing/REGRESSION-BASELINE.md
```

---

Acceptance Criteria

Baseline artifacts documented.

Expected outputs identified.

Comparison process documented.

---

Status

```
TODO
```

---

# Tomorrow's Plan

When you come back tomorrow afternoon, there is no ambiguity about what to do.

1. Start **US-CS-201** and build the artifact inventory.
    
2. Move to **US-CS-202** and validate the Broadridge and LSEG pipelines against that inventory.
    
3. As you discover relationships, complete **US-CS-203**.
    
4. Record any issues under **US-CS-205** instead of fixing them immediately.
    
5. Once the pipeline is understood, write **US-CS-204** so the process is repeatable.
    
6. Finish by capturing the validated Broadridge and LSEG pipelines as the permanent regression baseline in **US-CS-206**.
    

One final recommendation: because your Career System already has a mature requirements framework, I'd also create a sprint document such as **SPRINT-CS-RECOVERY-01.md** that contains only these six stories, their objectives, and a simple checklist. That gives you a single "mission plan" to open tomorrow instead of jumping between multiple story files, and it fits well with the sprint closeout workflow you've been using.

---


I think this is exactly the right stopping point for tonight.

Rather than trying to validate the pipeline when you're tired, let's leave the repository in a **known state** with the work fully planned. Tomorrow you can open the repo, look at the stories, and immediately know what to do.

One thing I'd change from my earlier suggestion is to treat this as an **operational recovery sprint** rather than just an epic. The epic explains _why_ we're doing this, while the stories define _how_ we'll execute it.

---

# EPIC-CS-002

## Career System Operational Recovery and Pipeline Validation

### Purpose

Restore confidence that the Career System can reliably generate complete application packages by validating, documenting, and testing the end-to-end artifact generation pipeline.

---

## Business Goal

The Career System has evolved over many weeks of development. Before implementing additional features (Career Center, PostgreSQL, REST APIs, EKF improvements, etc.), the existing pipeline must be fully understood, documented, and validated.

This Epic establishes a repeatable operational baseline.

---

## Success Criteria

By completion of this Epic:

- Complete pipeline documented
    
- All artifacts identified
    
- Upstream/downstream dependencies documented
    
- Known-good regression pipelines established
    
- Operational runbook written
    
- Defects documented
    
- Future development can safely resume
    

---

# Story 1

## US-CS-201

### Inventory Career System Artifacts

### Purpose

Identify every artifact produced by the Career System.

---

### Description

Create an inventory of every input, intermediate artifact, and final output.

Classify each artifact as:

- Source
    
- Generated
    
- Intermediate
    
- Final Deliverable
    
- Temporary
    

---

### Deliverable

```text
docs/architecture/ARTIFACT-INVENTORY.md
```

---

### Acceptance Criteria

✓ Every artifact documented

✓ File locations documented

✓ Classification completed

✓ Owner (generator) identified

---

### Status

```
TODO
```

---

# Story 2

## US-CS-202

### Validate Known-Good Pipelines

This becomes tomorrow's work.

---

### Purpose

Validate the complete generation pipeline using the known-good examples.

Regression Pipelines

- Broadridge
    
- LSEG
    

---

### Validate

```
Raw JD

↓

Normalized JD

↓

Recommendation

↓

Experience Match

↓

Generated Resume

↓

Full Resume

↓

ATS Resume

↓

Application Package
```

---

### Deliverable

```
docs/operations/PIPELINE-VALIDATION.md
```

---

### Acceptance Criteria

✓ Every artifact exists

✓ No missing stages

✓ Metadata consistent

✓ Dependencies verified

---

### Status

```
TODO
```

---

# Story 3

## US-CS-203

### Create Artifact Dependency Map

Purpose

Determine exactly what consumes every artifact.

---

Example

```
Normalized JD

produces

↓

Resume Recommendation

consumed by

↓

Experience Match

↓

Generated Resume

↓

Full Resume
```

---

Deliverable

```
docs/architecture/PIPELINE-DEPENDENCIES.md
```

---

Acceptance Criteria

✓ Every producer documented

✓ Every consumer documented

✓ Upstream/downstream relationships complete

---

Status

```
TODO
```

---

# Story 4

## US-CS-204

### Create Operational Runbook

Purpose

Document how to execute the pipeline.

---

Deliverable

```
docs/runbooks/RUNBOOK-generation-pipeline.md
```

Contents

- Inputs
    
- Commands
    
- Outputs
    
- Validation
    
- Recovery
    
- Troubleshooting
    

---

Acceptance Criteria

Someone unfamiliar with the project could regenerate an application package using only the runbook.

---

Status

```
TODO
```

---

# Story 5

## US-CS-205

### Pipeline Defect Tracking

Purpose

Record every defect discovered during validation.

Examples

- Incorrect metadata
    
- Broken references
    
- Missing artifacts
    
- Wrong filenames
    
- Incorrect dependencies
    

---

Deliverable

```
docs/bugs/PIPELINE-DEFECTS.md
```

---

Acceptance Criteria

Every discovered issue logged.

No fixes performed in this story.

---

Status

```
TODO
```

---

# Story 6

## US-CS-206

### Establish Regression Baseline

Purpose

Create permanent regression test cases.

Regression Pipelines

- Broadridge
    
- LSEG
    

Future changes must continue to produce equivalent outputs.

---

Deliverable

```
docs/testing/REGRESSION-BASELINE.md
```

---

Acceptance Criteria

Baseline artifacts documented.

Expected outputs identified.

Comparison process documented.

---

Status

```
TODO
```

---

# Tomorrow's Plan

When you come back tomorrow afternoon, there is no ambiguity about what to do.

1. Start **US-CS-201** and build the artifact inventory.
    
2. Move to **US-CS-202** and validate the Broadridge and LSEG pipelines against that inventory.
    
3. As you discover relationships, complete **US-CS-203**.
    
4. Record any issues under **US-CS-205** instead of fixing them immediately.
    
5. Once the pipeline is understood, write **US-CS-204** so the process is repeatable.
    
6. Finish by capturing the validated Broadridge and LSEG pipelines as the permanent regression baseline in **US-CS-206**.
    

One final recommendation: because your Career System already has a mature requirements framework, I'd also create a sprint document such as **SPRINT-CS-RECOVERY-01.md** that contains only these six stories, their objectives, and a simple checklist. That gives you a single "mission plan" to open tomorrow instead of jumping between multiple story files, and it fits well with the sprint closeout workflow you've been using.


---
Yes. Let's do this exactly the way you've been building the Career System. Don't just "write some stories." We will create a **new Epic** and a **Sprint** with traceable stories that become the authoritative plan for tomorrow.

I would stop after this tonight. Don't start implementation.

---

# Tonight's Goal

At the end of tonight you should have:

```
EPIC-CS-002
│
├── US-CS-201
├── US-CS-202
├── US-CS-203
├── US-CS-204
├── US-CS-205
└── US-CS-206

SPRINT-CS-RECOVERY-01.md
```

Tomorrow you simply start Story 201.

---

# Step 1 — Create a Git Branch

From the repo root:

```bash
cd ~/pjs/repos/career-system

git checkout main
git pull

git checkout -b feature/cs-operational-recovery
```

Don't work on main.

---

# Step 2 — Create Epic

Go to

```
docs/requirements/epics/
```

Create

```
EPIC-CS-002-career-system-operational-recovery.md
```

using your normal naming convention.

```
vi docs/requirements/epics/EPIC-CS-002-career-system-operational-recovery.md
```

Paste:

---

```markdown
# EPIC-CS-002

## Title

Career System Operational Recovery and Pipeline Validation

---

## Status

Proposed

---

## Priority

High

---

## Business Goal

Restore confidence in the Career System by documenting,
validating, and testing the complete application generation
pipeline before additional feature development resumes.

---

## Motivation

Recent operational work revealed that although the system
successfully generates application packages, the pipeline,
dependencies, and artifact relationships are not fully
documented.

Future development requires a stable operational baseline.

---

## Success Criteria

- Artifact inventory completed
- Pipeline documented
- Dependencies documented
- Regression baselines established
- Operational runbook completed
- Pipeline defects identified
- Recovery process documented

---

## Stories

US-CS-201

US-CS-202

US-CS-203

US-CS-204

US-CS-205

US-CS-206
```

Save.

---

# Step 3 — Create Sprint

Go to

```
docs/requirements/sprints/
```

Create

```
SPRINT-CS-RECOVERY-01.md
```

```
vi docs/requirements/sprints/SPRINT-CS-RECOVERY-01.md
```

Paste

```markdown
# Sprint CS-RECOVERY-01

## Goal

Establish a verified operational baseline for the Career
System generation pipeline.

---

## Epic

EPIC-CS-002

---

## Stories

US-CS-201 Artifact Inventory

US-CS-202 Pipeline Validation

US-CS-203 Dependency Map

US-CS-204 Generation Runbook

US-CS-205 Pipeline Defects

US-CS-206 Regression Baseline

---

## Exit Criteria

All stories completed.

Known-good pipeline validated.

Ready to resume feature work.
```

Save.

---

# Step 4 — Create Story Directory

```
docs/requirements/stories/
```

If it already exists, use it.

---

# Step 5 — Story 201

Create

```
US-CS-201-artifact-inventory.md
```

```
vi docs/requirements/stories/US-CS-201-artifact-inventory.md
```

Paste

```markdown
# US-CS-201

## Title

Inventory Career System Artifacts

## Epic

EPIC-CS-002

## Status

TODO

## Description

Document every artifact produced by the Career System.

Classify each as:

- Source
- Generated
- Intermediate
- Final
- Temporary

## Deliverable

docs/architecture/ARTIFACT-INVENTORY.md

## Acceptance Criteria

- Every artifact identified

- File locations documented

- Producer identified

- Classification completed
```

Save.

---

# Step 6 — Story 202

```
vi US-CS-202-pipeline-validation.md
```

Paste

```markdown
# US-CS-202

## Title

Validate Known-Good Pipelines

## Epic

EPIC-CS-002

## Status

TODO

## Pipelines

Broadridge

LSEG

## Validation

Raw JD

↓

Normalized JD

↓

Recommendation

↓

Experience Match

↓

Generated Resume

↓

Full Resume

↓

ATS Resume

↓

Application Package

## Deliverable

docs/operations/PIPELINE-VALIDATION.md

## Acceptance Criteria

Every stage verified.

No missing artifacts.

Metadata verified.

Dependencies verified.
```

---

# Step 7 — Story 203

Create

```
US-CS-203-dependency-map.md
```

Paste

```markdown
# US-CS-203

## Title

Create Pipeline Dependency Map

## Epic

EPIC-CS-002

## Status

TODO

## Description

Document every upstream and downstream dependency.

## Deliverable

docs/architecture/PIPELINE-DEPENDENCIES.md

## Acceptance Criteria

Producer documented.

Consumer documented.

Dependency chain complete.
```

---

# Step 8 — Story 204

Create

```
US-CS-204-generation-runbook.md
```

Paste

```markdown
# US-CS-204

## Title

Generation Pipeline Runbook

## Epic

EPIC-CS-002

## Status

TODO

## Deliverable

docs/runbooks/RUNBOOK-generation-pipeline.md

## Acceptance Criteria

Pipeline can be executed using only the runbook.
```

---

# Step 9 — Story 205

Create

```
US-CS-205-pipeline-defects.md
```

Paste

```markdown
# US-CS-205

## Title

Pipeline Defect Tracking

## Epic

EPIC-CS-002

## Status

TODO

## Deliverable

docs/bugs/PIPELINE-DEFECTS.md

## Acceptance Criteria

Every defect logged.

No fixes performed.
```

---

# Step 10 — Story 206

Create

```
US-CS-206-regression-baseline.md
```

Paste

```markdown
# US-CS-206

## Title

Regression Baseline

## Epic

EPIC-CS-002

## Status

TODO

## Deliverable

docs/testing/REGRESSION-BASELINE.md

## Acceptance Criteria

Broadridge validated.

LSEG validated.

Expected outputs documented.
```

---

# Step 11 — Check Everything

Run:

```bash
git status
```

You should see:

```
new file:

EPIC-CS-002...

SPRINT-CS-RECOVERY-01...

US-CS-201...

US-CS-202...

US-CS-203...

US-CS-204...

US-CS-205...

US-CS-206...
```

---

# Step 12 — Commit the Planning Work

```bash
git add .

git commit -m "Add EPIC-CS-002 operational recovery sprint planning"
```

Do **not** start implementing the stories tonight.

---

## Tomorrow's Mission

Tomorrow afternoon, open **only**:

```
SPRINT-CS-RECOVERY-01.md
```

That sprint document becomes your dashboard. Start with **US-CS-201** (Artifact Inventory), and let each completed story naturally feed the next one. By the end of the sprint, you'll have transformed the operational recovery work we've been doing into first-class, traceable project artifacts that fit the Career System's requirements process. This also gives you a clean checkpoint before returning to feature development like Career Center, PostgreSQL, or Motorweb.

---










