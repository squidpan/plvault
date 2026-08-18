---
categories:
  - "[[Art Catalog]]"
  - "[[Jinie Choi Art]]"
tags:
  - python
  - artwork
  - image-processing
  - runbook
  - environment
type: runbook
description: Setup and operating guide for the Python artwork image collection and image selection tools used by the Jinie Choi Art repository.
created: 2026-08-12
last_modified: 2026-08-12
status: active
---

# Python Artwork Tools — Setup and Runbook

## Purpose

This runbook explains how to set up and use the Python artwork-processing tools in the `jinie-choi-art` repository.

The tools support an iterative workflow for recovering artwork images from legacy folders and reducing groups of website-generated image variants to one preferred candidate per artwork/image family.

The scripts are designed to be safe:

- report to stdout by default
- do not modify source images
- require `-u` / `--update` before copying
- use new target folders for iterative processing
- keep staging images outside Git

## Repository Location

Expected local repository:

    /home/pl/pjs/repos/jinie-choi-art

Using the configured environment variable:

    $REPOS_ROOT/jinie-choi-art

## Python Version

Current tested Python version:

    Python 3.13.14

Check it with:

    python3.13 --version

## Why This Repo Uses a Virtual Environment

The project uses a local Python virtual environment:

    .venv/

This isolates project dependencies from the Pop!_OS system Python installation.

This became necessary because the system `pip` under `/usr/lib/python3/dist-packages` was not compatible with Python 3.13 and failed with:

    ModuleNotFoundError: No module named 'distutils'

The `.venv` avoids modifying the operating-system Python installation.

## One-Time Environment Setup

Run these commands once after creating or cloning the repository:

    cd $REPOS_ROOT/jinie-choi-art

    python3.13 -m venv .venv

    source .venv/bin/activate

    python -m ensurepip --upgrade

    python -m pip install --upgrade pip

    python -m pip install Pillow

Verify:

    which python

Expected path:

    /home/pl/pjs/repos/jinie-choi-art/.venv/bin/python

Verify the Python version:

    python --version

Verify Pillow:

    python -c "from PIL import Image; print('Pillow OK')"

## Normal Startup on Later Days

Do not recreate `.venv`.

Start work with:

    cd $REPOS_ROOT/jinie-choi-art

    source .venv/bin/activate

Confirm:

    which python
    python --version

The prompt normally begins with:

    (.venv)

## Leaving the Virtual Environment

Run:

    deactivate

The `.venv` directory remains in the repository and can be activated again later.

It is excluded from Git by `.gitignore`.

# Artwork Processing Workflow

The current working flow is:

    legacy source folders
        ↓
    collect candidate images
        ↓
    data/staging/all-images/
        ↓
    group similar filenames and select best image
        ↓
    data/staging/pass-1-selected/
        ↓
    review
        ↓
    later refinement passes
        ↓
    catalog candidates

Source files are never deleted by these scripts.

# Script 1 — collect_images.py

Location:

    scripts/artwork/collect_images.py

Purpose:

- recursively scan a source folder
- find supported image files in subfolders
- print planned operations to stdout
- copy nothing unless update mode is explicitly requested

Example source used during recovery:

    ~/Downloads/galleryjs_wp_ipage_backup_1013_2017

Typical dry run:

    cd $REPOS_ROOT/jinie-choi-art

    source .venv/bin/activate

    python scripts/artwork/collect_images.py       ~/Downloads/galleryjs_wp_ipage_backup_1013_2017       data/staging/all-images

Review stdout before copying.

Use the script's `-u` / `--update` option when the reported operations are correct.

Always check the script's current options with:

    python scripts/artwork/collect_images.py --help

# Script 2 — select_best_images_v3.py

Location:

    scripts/artwork/select_best_images_v3.py

Purpose:

- inspect candidate image dimensions and file sizes
- normalize common legacy WordPress derivative filenames
- use similar filenames as the primary grouping rule
- group files into image families
- select one preferred candidate per filename family
- report all groups and selections to stdout
- copy nothing unless `-u` / `--update` is supplied

## Filename Family Examples

Files such as:

    000001.jpg
    000001@2x.jpg
    000001-677x402.jpg
    000001-677x402@2x.jpg
    000001-300x208.jpg

are treated as variants of family:

    000001

Another example:

    2-4-Copy.jpg
    2-4-Copy-3264x500.jpg
    2-4-Copy-1170x500@2x.jpg
    2-4-Copy-270x250@2x.jpg

are treated as family:

    2-4-Copy

## Winner Ranking

Within a filename family, v3 prefers:

1. a filename that does not look like a generated derivative
2. more total image pixels
3. a larger minimum image dimension
4. larger file size as a final weak tie-breaker

The script selects a best available candidate. It does not prove that the file is an archival-quality photograph.

Human review remains part of the cataloging process.

# Pass 1 — Dry Run

Start at the repository:

    cd $REPOS_ROOT/jinie-choi-art

Activate Python:

    source .venv/bin/activate

Run without `-u`:

    python scripts/artwork/select_best_images_v3.py       data/staging/all-images       data/staging/pass-1-selected

Nothing should be copied.

The current legacy dataset produced:

    Found  : 473 candidate image file(s)
    Groups : 187

These counts are reference results for the current dataset, not permanent requirements.

# Pass 1 — Copy Selected Images

For a clean pass, the target directory must be empty.

Check it:

    find data/staging/pass-1-selected -maxdepth 1 -type f | wc -l

If this is a disposable generated Pass 1 directory and it needs to be reset:

    rm -rf data/staging/pass-1-selected
    mkdir -p data/staging/pass-1-selected

Verify:

    find data/staging/pass-1-selected -maxdepth 1 -type f | wc -l

Expected:

    0

Run update mode:

    python scripts/artwork/select_best_images_v3.py       data/staging/all-images       data/staging/pass-1-selected       -u | tee data/staging/pass-1-selected.txt

Verify:

    find data/staging/pass-1-selected -maxdepth 1 -type f | wc -l

For the current dataset, a clean run should produce:

    187

Compare storage:

    du -sh data/staging/all-images
    du -sh data/staging/pass-1-selected

# Important Target-Folder Rule

`select_best_images_v3.py` does not overwrite a file already present in the target directory.

If a destination filename already exists, the current implementation creates another target filename such as:

    image__2.jpg

and later:

    image__3.jpg

Therefore, rerunning `-u` into an already populated Pass 1 directory can produce duplicate output.

For clean iterative passes:

    source directory
        ↓
    dry run
        ↓
    review
        ↓
    empty target directory
        ↓
    -u
        ↓
    new pass result

A future script version should refuse update mode when the target folder is non-empty unless explicitly overridden.

# Iterative Passes

Example working directories:

    data/staging/all-images/
    data/staging/pass-1-selected/
    data/staging/pass-2-selected/
    data/staging/final-selected/

Do not delete or modify the original recovery source merely because a later pass has selected a preferred image.

Each pass should be reproducible from its prior source.

# Staging and Git

The repository `.gitignore` intentionally excludes generated working data:

    data/staging/*
    !data/staging/.gitkeep

This means the following are local working data and are not pushed to GitHub:

    data/staging/all-images/
    data/staging/pass-1-selected/
    data/staging/pass-1-selected.txt

The repository keeps only:

- scripts
- documentation
- catalog metadata
- schemas and standards
- Git placeholders such as `.gitkeep`
- eventual publication assets where explicitly intended

# Useful Verification Commands

Show script help:

    python scripts/artwork/collect_images.py --help

    python scripts/artwork/select_best_images_v3.py --help

Count images:

    find data/staging/all-images -maxdepth 1 -type f | wc -l

    find data/staging/pass-1-selected -maxdepth 1 -type f | wc -l

Check directory size:

    du -sh data/staging/all-images
    du -sh data/staging/pass-1-selected

Check Git state:

    git status

Show ignored staging data:

    git status --ignored

# Git Workflow

Always work on branches.

Use:

    git branch
    git switch

Do not use `git checkout`.

Create a branch with:

    git switch -c feature/<branch-name>

Before committing:

    git status
    git diff
    git diff --cached

# Dependency Management

The current v3 selector requires Pillow.

A minimal `requirements.txt` can contain:

    Pillow

Install from it with:

    python -m pip install -r requirements.txt

If an older experimental script using `ImageHash` is retained and still intended to run, that script has an additional dependency:

    ImageHash

The active tooling documentation should be updated whenever the supported script set changes.

# Current Known-Good Baseline

Current working selector:

    scripts/artwork/select_best_images_v3.py

Current primary grouping strategy:

    filename-family normalization first

Current test dataset:

    473 candidate image files

Current Pass 1 family count:

    187

This is the baseline to preserve before beginning further Pass 2 refinements.
# GitHub CLI Setup and Repository Authentication

## Purpose

The project uses the GitHub command-line interface, `gh`, to create and manage the GitHub repository directly from the terminal.

This is separate from Git itself:

- `git` manages local version control, branches, commits, and remotes.
- `gh` talks to GitHub.com and can create repositories, authenticate, open pull requests, inspect issues, and perform other GitHub-specific operations.

Git remains the underlying version-control system.

## Install GitHub CLI on Pop!_OS

On this Pop!_OS 22.04 environment, `gh` was installed from the Ubuntu package repositories.

Run:

    sudo apt update

    sudo apt install gh

Verify:

    gh --version

The initial installation used:

    gh version 2.4.0+dfsg1

The exact version may change later as operating-system packages are updated.

## GitHub Authentication Concepts

GitHub does not accept a normal account password for Git operations over HTTPS.

Authentication can be handled in several ways.

The relevant approaches for this project are:

1. GitHub CLI browser authentication
2. Personal Access Token (PAT)
3. SSH keys

For this project, browser authentication through `gh auth login` is the preferred setup because it is simple, interactive, and avoids manually creating and pasting a long-lived token.

## Browser Authentication — Recommended

Start:

    gh auth login

The interactive prompts used were:

    What account do you want to log into?
    GitHub.com

    What is your preferred protocol for Git operations?
    HTTPS

    Authenticate Git with your GitHub credentials?
    Yes

    How would you like to authenticate GitHub CLI?
    Login with a web browser

GitHub CLI then displays a temporary one-time device code.

Example form:

    XXXX-XXXX

The actual code is temporary and should not be recorded in documentation or committed to Git.

The CLI then prompts:

    Press Enter to open github.com in your browser

After pressing Enter:

1. GitHub opens in the browser.
2. Sign into the intended GitHub account if necessary.
3. Confirm the device code.
4. Authorize GitHub CLI.
5. Return to the terminal.
6. Press Enter if prompted.

A successful login looks similar to:

    Authentication complete.

    Configured git protocol

    Logged in as <github-user>

For this repository setup, the authenticated GitHub account was:

    squidpan

## What the One-Time Code Is

The browser login code is not a permanent authentication token.

It is a short-lived device authorization code used only to connect the terminal session with the GitHub browser login.

Conceptually:

    terminal
        ↓
    gh auth login
        ↓
    temporary device code
        ↓
    browser
        ↓
    GitHub account authorization
        ↓
    GitHub CLI receives credentials
        ↓
    future gh/git HTTPS operations can authenticate

The one-time code expires and should not be saved.

## What a Personal Access Token Is

A Personal Access Token, usually called a PAT, is a manually created GitHub credential.

A PAT can be used in place of a password for HTTPS-based API or Git operations.

It generally looks like a long random secret.

PATs can be configured with permissions such as:

- repository access
- workflow access
- package access
- organization access

Because PATs are secrets, they must never be:

- committed to Git
- stored in Markdown documentation
- pasted into source code
- posted in ChatGPT
- placed in shell history unnecessarily

For this project, a PAT was not required because `gh auth login` successfully completed through the browser flow.

## Browser Authentication vs PAT

Browser authentication is preferred here because:

- no token needs to be manually generated
- no secret needs to be copied into the terminal
- GitHub CLI manages the authentication setup
- it is easier to revoke or reauthenticate through `gh`
- it reduces the chance of accidentally exposing a PAT

A PAT may still be useful later for automation, CI/CD, or tools that cannot use GitHub CLI browser authentication.

## HTTPS vs SSH

During login, HTTPS was selected:

    What is your preferred protocol for Git operations?
    HTTPS

With HTTPS:

    git clone https://github.com/...
    git push
    git pull

GitHub CLI can configure Git so these HTTPS operations use the GitHub credentials established through `gh auth login`.

SSH is another valid GitHub authentication method, typically using:

    git@github.com:owner/repository.git

SSH requires generating and registering an SSH key pair.

For this project, HTTPS is simpler and is the current standard.

Do not change to SSH unless there is a specific reason.

## Verify Authentication

After login, run:

    gh auth status

This shows whether GitHub CLI is authenticated and which account is active.

Also verify the Git protocol configuration:

    gh config get git_protocol -h github.com

Expected:

    https

## Log Out

If the machine should no longer be authenticated:

    gh auth logout

Then follow the prompts.

This removes the GitHub CLI authentication for the selected account.

## Reauthenticate Later

If authentication expires or is revoked:

    gh auth login

Repeat the browser flow.

There is no need to reinstall `gh`.

# Creating the GitHub Repository

## Local State Before Creating the Remote

The local repository was initialized first.

The first baseline commit was created on:

    feature/artwork-catalog-foundation

Baseline commit:

    c55e885

Commit message:

    Establish artwork catalog foundation and image selection workflow

A `main` branch was then created from the same baseline commit.

Current branch structure:

    main
    feature/artwork-catalog-foundation

The feature branch remains the working branch.

## Create the GitHub Repository

From the local repository:

    cd $REPOS_ROOT/jinie-choi-art

Verify:

    git status
    git branch

Create the GitHub repository:

    gh repo create jinie-choi-art \
      --private \
      --source=. \
      --remote=origin

Meaning of the options:

`jinie-choi-art`

    The new GitHub repository name.

`--private`

    Create the GitHub repository as private.

`--source=.`

    Use the current local repository as the source repository.

`--remote=origin`

    Add the new GitHub repository to local Git using the conventional remote name `origin`.

## What `origin` Means

A Git remote is a named reference to another Git repository.

The conventional name for the main remote repository is:

    origin

After GitHub repository creation:

    git remote -v

should show fetch and push URLs for `origin`.

Conceptually:

    local jinie-choi-art repository
                │
                │ git push / git pull
                ↓
          origin
                │
                ↓
      GitHub: jinie-choi-art

`origin` is only a local nickname. It is not a special GitHub object.

## Push Main

Switch to `main`:

    git switch main

Push and establish the upstream relationship:

    git push -u origin main

The `-u` option means:

    --set-upstream

It tells Git that local:

    main

tracks remote:

    origin/main

After that, future pushes can normally be shortened to:

    git push

## Push the Feature Branch

Switch back:

    git switch feature/artwork-catalog-foundation

Push:

    git push -u origin feature/artwork-catalog-foundation

Now that branch tracks:

    origin/feature/artwork-catalog-foundation

## Verify Local and Remote Tracking

Run:

    git branch -vv

This displays local branches and their configured upstream branches.

Also:

    git remote -v

And:

    git status

## Normal Daily Git Workflow

Start:

    cd $REPOS_ROOT/jinie-choi-art

Inspect:

    git status
    git branch

Switch to the intended feature branch:

    git switch feature/artwork-catalog-foundation

Work normally.

Before committing:

    git status
    git diff

Stage files intentionally:

    git add <files>

Inspect staged work:

    git diff --cached

Commit:

    git commit -m "Describe the change"

Push:

    git push

Because the upstream was configured with `-u`, the remote and branch do not need to be supplied every time.

## Pulling Changes

To bring remote changes into the current tracking branch:

    git pull

Before pulling:

    git status

Avoid pulling over uncommitted work unless the state and merge behavior are understood.

# GitHub Safety Notes

Never commit:

- `.venv/`
- GitHub authentication tokens
- passwords
- API keys
- full staging image collections
- generated temporary output

The repository `.gitignore` currently excludes:

    .venv/
    data/staging/*
    data/exports/*
    site/output/*

while preserving selected `.gitkeep` placeholders.

Verify a path is ignored with:

    git check-ignore -v <path>

Examples:

    git check-ignore -v .venv

    git check-ignore -v data/staging/all-images

    git check-ignore -v data/staging/pass-1-selected.txt

# Current GitHub Setup Baseline

Operating system:

    Pop!_OS 22.04

GitHub CLI command:

    gh

GitHub account used:

    squidpan

Git transport:

    HTTPS

Authentication method:

    GitHub CLI browser authentication

Local repository:

    /home/pl/pjs/repos/jinie-choi-art

Primary remote name:

    origin

Primary branches:

    main
    feature/artwork-catalog-foundation

This section documents the proven setup used for the repository so that the same environment can be understood, rebuilt, or troubleshot later.
