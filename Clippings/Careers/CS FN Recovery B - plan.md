---
categories:
  - "[[Processes]]"
type:
description: CS recovery B phase 0
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

Please paste the complete output.

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















