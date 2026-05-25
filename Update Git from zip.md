---
categories:
  - "[[Processes]]"
type:
description:
source:
tags:
created: 2026-05-24
last: 2026-05-24
status:
origin:
run_id:
input_prompt:
---



I'll rebuild the deploy-script overlay in smaller chunks so the package creation completes cleanly.
```
motorweb-deploy-scripts-v0.5.3.zip
```

It adds wrapper scripts for:

```
pl cutting a release tag
ted cloning a tagged release
ted setting up JobApp
ted running JobApp
ted validating endpoints
ted killing stale Uvicorn
```

Apply on a branch:

>[! package to git]
>cd /opt/projects/motorweb
 git switch main
 git pull
 git switch -c feature/ted-deploy-scripts
 unzip ~/Downloads/motorweb-deploy-scripts-v0.5.3.zip -d .
 git status
 git add .
 git commit -m "Add ted local deploy wrapper scripts"
 git push -u origin feature/ted-deploy-scripts


then merge:

```
git switch main
git pull
git merge feature/ted-deploy-scripts
git push origin main
```
