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



Your understanding of the SSH plan is right: keep `pl` as the protected human key now, prove the deploy cycle manually, then add a `ted` read-only no-passphrase deploy key when the process is stable. I’ll also sanity-check the GitHub account/repo-transfer angle so the recommendation is clean.

Thought for 7s

Yes — your SSH plan is exactly right:

```
now:pl = passphrase-protected human SSH keylater:ted = read-only deploy key, probably no passphrase
```

You do **not** need to do the no-passphrase deploy key yet. First validate the full manual cycle.

## About creating a clean GitHub account like `tribute`

I like the goal, but I would **not** create a separate personal GitHub account just for this.

A cleaner GitHub-native approach is to create a **GitHub Organization** instead, maybe:

```
tributetribute-labsmotorweb-labs
```

Why an organization is better:

```
clean public profile for projectsseparate from personal account cluttercan invite collaborators laterbetter access control modelrepositories can live under the orgyou still administer it from your normal GitHub account
```

GitHub describes organizations as shared accounts for collaboration across projects with security and administrative features.

## Recommended clean setup

Keep your human GitHub account:

```
squidpan
```

Create organization:

```
tribute
```

Then move repo to:

```
tribute/motorweb
```

or:

```
tribute-labs/motorweb
```

That gives a clean public URL without creating another personal identity.

## Transfer later, not yet

GitHub supports transferring a repository to another user or organization; after transfer, the new owner administers contents, issues, pull requests, releases, projects, and settings.

But I would wait until after:

```
pl cuts tagted deploys tagted validatespl fixes issuepl cuts next tag
```

Then transfer/move when the repo is stable.

## Deploy key plan later

For `ted`, use a repo deploy key:

```
motorweb-popos-ted-readonly-deploy-2026
```

GitHub deploy keys are repository-specific and are read-only by default unless write access is explicitly granted.

So the clean final model is:

```
GitHub org: tributerepo: tribute/motorwebpl/squidpan:admin/write accessted:read-only deploy keyno passphrase laterrepo-scoped
```

I’d avoid a brand-new personal account unless you specifically want to test from a completely separate user identity. For a clean portfolio/project home, a GitHub Organization is better.