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
> 
> anything else I need from you? once I go over to the new chat #1, let me know which folders and files I should package and upload? and give me a zip command to get those files.
> 

Yes. Before new chat #1, package only what the new chat needs to rebuild context fast.

## Upload this pack to new chat #1

Include:

```text
bin/
scripts/
templates/
docs/operations/
docs/standards/
docs/prototypes/
docs/requirements/
data/jds/
data/roles/
data/master-profile/
data/application-summaries/
data/resume-sections/
data/generated-resumes/
data/full-resumes/
data/ats-exports/
data/application-packages/application-lseg-senior-ba-2026-v1/
data/application-packages/application-broadridge-product-analyst-2026-v1/
data/resume-tailoring/
data/resume-bullet-ranking/
data/candidate-matching/
data/candidate-strategy/
data/candidate-explainability/
data/jd-intelligence/
```

Reason: this includes the scripts, standards, recovery docs, known-good regression packages, and the pipeline data around JD → role → resume → application package. Your tree confirms these folders/files exist in the repo, including the LSEG/Broadridge application packages and final-mile scripts.

## Zip command

Run from repo root:

```bash
cd ~/pjs/repos/career-system

zip -r /tmp/career-system-functional-recovery-handoff-$(date +%Y%m%d).zip \
  bin \
  scripts \
  templates \
  docs/operations \
  docs/standards \
  docs/prototypes \
  docs/requirements \
  data/jds \
  data/roles \
  data/master-profile \
  data/application-summaries \
  data/resume-sections \
  data/generated-resumes \
  data/full-resumes \
  data/ats-exports \
  data/application-packages/application-lseg-senior-ba-2026-v1 \
  data/application-packages/application-broadridge-product-analyst-2026-v1 \
  data/resume-tailoring \
  data/resume-bullet-ranking \
  data/candidate-matching \
  data/candidate-strategy \
  data/candidate-explainability \
  data/jd-intelligence
```

Then verify:

```bash
ls -lh /tmp/career-system-functional-recovery-handoff-*.zip
unzip -l /tmp/career-system-functional-recovery-handoff-$(date +%Y%m%d).zip | head -80
```

Upload that zip to the new chat.

