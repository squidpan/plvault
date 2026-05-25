---
categories:
  - "[[Processes]]"
type:
description:
source: chatgpt-manual
tags:
created: 2026-05-25
last: 2026-05-25
status:
origin:
run_id:
input_prompt:
---
It is NOT overkill to think about this now. You're actually hitting a real DevOps/CI/CD design issue:

```
interactive humansvsnon-interactive automation
```

# Why passphrases become a problem

A passphrase protects the SSH private key.

Good for humans:

```
if laptop stolenprivate key still encrypted
```

But automation cannot type:

```
interactive password prompts
```

So CI/CD systems need another approach.

---

# What professionals actually do

There are several patterns.

# OPTION 1 — Human developer key WITH passphrase

This is what you have now.

Example:

```
pl SSH keywith passphrase
```

Excellent for:

```
daily developmentlaptop safetymanual git work
```

Keep this.

This is NOT the problem.

---

# OPTION 2 — Automation/deploy key WITHOUT passphrase

Very common.

Example:

```
ted deploy keyread-onlyno passphrase
```

Why acceptable?

Because:

```
limited scoperead-onlyused only for deployment
```

If compromised:

```
attacker can only clone repocannot pushcannot destroy history
```

This is probably your best next step.

---

# Your future-proof clean architecture

Use TWO TYPES OF KEYS.

## 1. Human developer key

Used by:

```
pl
```

Properties:

```
passphrase protectedfull repo accessGitHub user SSH key
```

Example:

```
~/.ssh/id_ed25519_squidpan_dev
```

Purpose:

```
developmentpushcommittaggingadmin
```

---

## 2. Automation/deploy key

Used by:

```
tedfuture CI/CDfuture GitHub Actionsfuture cloud deploy
```

Properties:

```
no passphraseread-onlyrepo-scopeddeploy key
```

Example:

```
~/.ssh/id_ed25519_motorweb_ted_deploy
```

Purpose:

```
clone repopull tagsdeploy releases
```

That is VERY standard and clean.

---

# Why this is NOT overkill

Because later:

```
GitHub ActionsCloud RunDocker deploysKubernetesCI/CD
```

all need non-interactive authentication.

You are simply separating:

```
human identityvsautomation identity
```

which is correct engineering.

---

# The important design principle

DO NOT use your personal developer key for automation.

Bad:

```
pl full-access SSH keyused by ted automation
```

Because if compromised:

```
full repo access exposed
```

Instead:

```
limited deploy key
```

Much safer.

---

# Is no-passphrase safe enough?

For deploy keys:

```
usually yes
```

IF:

```
read-onlylimited scopestored on trusted machinefile permissions correct
```

Linux permissions matter:

```
chmod 700 ~/.sshchmod 600 ~/.ssh/id_ed25519_motorweb_ted_deploy
```

---

# What GitHub Actions does later

Interesting point:

GitHub Actions typically does NOT use SSH keys directly for most repo operations.

Instead it uses:

```
temporary GitHub tokens
```

inside the pipeline.

So your future architecture becomes:

## Local human access

```
SSH keys
```

## CI/CD automation

```
GitHub Actions tokens/secrets
```

## Cloud deployment

```
cloud service accounts
```

---



# Recommended path for YOU

## RIGHT NOW

Keep:

```
pl passphrase-protected SSH key
```

Add later:

```
ted read-only deploy key WITHOUT passphrase
```

That gives you:

```
safe developmentsafe deploymentfuture CI/CD compatibility
```

without complexity.

---

# Your future repo access architecture

## pl

```
GitHub user keypassphrasefull access
```

## ted

```
deploy keyno passphraseread-only
```

## GitHub Actions

```
GitHub tokens/secrets
```

## Cloud

```
service accounts
```

That is actually a very professional architecture direction.

---

# Final recommendation

Do NOT remove passphrases from your personal developer key.

Instead:

```
separate developer identity from deployment identity
```

That is the future-proof solution.