---
categories:
  - "[[Processes]]"
type:
description:
source: chatgpt-manual
tags:
created:
last:
status:
origin:
run_id:
input_prompt:
---


## 1. Application status dashboard

Read these first:

```
cat data/application-tracker/README.md
cat docs/operations/application-status-update-workflow.md
cat docs/requirements/stories/US-CS-052-application-tracker-dashboard-v1.md
```

Generate dashboard:

```
./bin/run-application-tracker-generator.sh./bin/run-application-dashboard-generator.sh
```

View current status:

```
cat data/application-tracker/applications.mdcolumn -s, -t < data/application-tracker/applications.csv | less -S
```

Also check generated dashboard/output files:

```
find data/application-tracker data/application-summaries data/application-packages \  -type f | grep -Ei "dashboard|summary|applications|readiness|manifest" | sort
```

## 2. JD processing flow

Start with:

```
cat README_JD_NORMALIZER.md
cat README_APPLICATION_PACKAGE_GENERATOR.md
cat README_RESUME_GENERATION_ENGINE.md
```

Run JD normalization:

```
./bin/run-jd-normalization.sh run-$(date +%Y-%m-%d)-jd-normalize-v1 data/jds/raw
```

Verify:

```
find data/jds/normalized -type f | sortfind ops/runs -maxdepth 3 -type f | grep jd-normalize | sort | tail -50
```

## 3. Resume / ATS / HTML pipeline

Likely sequence:

```
./bin/run-role-generation.sh./bin/run-resume-version-generation.sh
./bin/run-full-resume-generator.sh./bin/run-ats-resume-generator.sh
./bin/run-ats-text-export.sh
./bin/run-resume-html-export.sh
./bin/run-application-package-generator.sh
./bin/run-application-dashboard-generator.sh
```

Then inspect:

```
find data/full-resumes data/ats-exports data/application-packages \  -type f | sort | tail -100
```

## 4. New Obsidian clipped JDs

Run this to see what needs copying:

```
ls -lrt ~/pjs/vaults/plvault/Clippings/Careers/JDs/Raw
ls -lrt data/jds/raw
```

Copy only new files:

```
cp -n ~/pjs/vaults/plvault/Clippings/Careers/JDs/Raw/*.md data/jds/raw/git status --short
```

Then rerun normalization and package generation.