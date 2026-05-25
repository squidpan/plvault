---
categories:
  - "[[Processes]]"
type:
description:
source: chatgpt-manual
tags:
created: 2026-05-24
last: 2026-05-24
status:
origin:
run_id:
input_prompt:
---


Yes — exactly. That iterative release/test/fix cycle is how real deployment pipelines work.

You are essentially moving toward:



```
developer workflow→ release workflow→ deployment workflow→ operations workflow
```

This is the right time to establish tagging discipline.

# 
Recommended Release Flow

Use semantic-ish versions:

```
v0.5.2v0.5.3v0.5.4
```

When a bug is found:

```
fix on branch→ retest locally→ merge to main→ cut new tag→ ted deploys new tag
```

---

# Your Workflow (`pl`)

## 1. Finish changes

```
cd /opt/projects/motorweb
git switch main
git pullgit status
```

---

## 2. Commit final changes

```
git add .git commit -m "Finalize v0.5.2 dataload foundation"
```

---

## 3. Push main

```
git push origin main
```

---

## 4. Create annotated tag

Annotated tags are better for releases.

```
git tag -a v0.5.2 -m "motorweb v0.5.2 dataload foundation"
```

---

## 5. Push tag

```
git push origin v0.5.2
```

Verify:

```
git tag
```

You should see:

```
v0.5.2
```

---

# Ted Deployment Workflow

Assume `ted` deploys into:

```
/opt/releases/motorweb
```

---

# First-time ted setup

## 1. Create releases area

As `pl`:

```
sudo mkdir -p /opt/releases/motorwebsudo chown -R ted:deployers /opt/releasessudo chmod -R 2775 /opt/releases
```

---

# Ted deploy steps

## 1. Switch to ted

```
su - ted
```

or:

```
sudo su - ted
```

---

## 2. Go to releases area

```
cd /opt/releases/motorweb
```

---

## 3. Clone specific tag

IMPORTANT:  
Deploy tags, not random branches.

```
git clone --branch v0.5.2 git@github-squidpan:squidpan/motorweb.git motorweb-v0.5.2
```

---

## 4. Enter app

```
cd motorweb-v0.5.2/apps/job-application-platform
```

---

## 5. Create venv

```
python3.13 -m venv .venv
```

---

## 6. Activate

```
source .venv/bin/activate
```

---

## 7. Install requirements

```
python -m pip install -r requirements.txt
```

---

## 8. Run initial dataload

```
scripts/dataload/run-initial-dataload.sh
```

Expected:

```
jobs.json generatedjobs.csv copieddatabase-files populated
```

---

## 9. Start API

```
scripts/run-json.sh
```

Expected:

```
Uvicorn running on 127.0.0.1:8000
```

---

# Ted validation tests

Open another terminal as `ted`.

---

## Health endpoint

```
curl http://127.0.0.1:8000/health
```

Expected:

```
{"status":"ok"}
```

---

## Query jobs

```
curl http://127.0.0.1:8000/jobs
```

Expected:

```
JSON list of jobs
```

---

## Filter by status

```
curl 'http://127.0.0.1:8000/jobs?status=Applied'
```

---

## Keyword query

```
curl 'http://127.0.0.1:8000/jobs?keyword=Analyst'
```

---

## Validate storage backend

```
curl http://127.0.0.1:8000/storage
```

Expected:

```
{"backend":"json"}
```

---

# If Ted finds problems

Example:

```
GET /jobs brokendataload failedJSON malformedendpoint missing
```

Then your cycle becomes:

```
pl fixes issue→ commit→ merge main→ tag v0.5.3→ push tag→ ted deploys v0.5.3
```

This iterative release loop is normal and healthy.

---

# VERY important future rule

Eventually:

```
developers do NOT deploy from branches
```

Deploy only:

```
tagsrelease branchescontainer images
```

That discipline becomes critical later with CI/CD and cloud deployments.

---

# Recommended next docs later

You should eventually add:

```
docs/releases/docs/deployment/docs/runbooks/
```

Specifically:

```
docs/runbooks/ted-local-release-deploy.mddocs/releases/release-tagging-strategy.mddocs/deployment/local-release-flow.md
```

You are now thinking like:

```
developerrelease engineerdeployment engineeroperations engineer
```

all together — which is exactly the right direction for `motorweb`.