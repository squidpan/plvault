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



These are great commands for making Git tell the story of your project.

Run from:

```
cd /opt/projects/motorweb
```

## At-a-glance commit history

```
git log --oneline --decorate --graph --all
```

Better version:

```
git log --graph --decorate --oneline --all --date=short
```

## Show commits with dates

```
git log --pretty=format:"%h %ad %d %s" --date=short
```

Example style:

```
a1b2c3d 2026-05-22 (HEAD -> main, tag: v0.5.3) Add ted local deploy wrapper scripts
```

## Show only tags/releases

```
git tag
```

Sorted newest first:

```
git tag --sort=-creatordate
```

With tag messages:

```
git tag -n99 --sort=-creatordate
```

## Show release timeline

```
git log --oneline --decorate --simplify-by-decoration --all
```

This is very useful because it highlights branches/tags.

## See what changed between releases

```
git log --oneline v0.5.2..v0.5.3
```

Diff summary:

```
git diff --stat v0.5.2..v0.5.3
```

Full changed files:

```
git diff --name-status v0.5.2..v0.5.3
```

## Show one release tag

```
git show v0.5.3
```

Shorter:

```
git show --stat v0.5.3
```

## Friendly release report

Use this:

```
git for-each-ref refs/tags \  --sort=-creatordate \  --format='%(creatordate:short)  %(refname:short)  %(subject)'
```

## Best command for your goal

This one paints the best picture:

```
git log --graph --decorate --oneline --all --date=short \  --pretty=format:"%C(yellow)%h%Creset %C(cyan)%ad%Creset %C(auto)%d%Creset %s"
```

## Commit message style going forward

Use messages that tell the release story:

```
Add dataload foundationAdd schema evolution docsAdd logging foundation documentationAdd Uvicorn port troubleshooting docsAdd ted local deploy wrapper scriptsDocument simplified laptop user modelConsolidate root README with setup and run instructions
```

Good pattern:

```
Verb + thing changed + purpose/context
```

Examples:

```
Add job dataload CSV-to-JSON pipelineDocument file-backed database designAdd release deployment scripts for tedAdd local validation runbook for tagged releasesFix JSON backend query filtering
```

Your Git history should read like a project timeline.