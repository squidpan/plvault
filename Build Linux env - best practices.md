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



Creating a fresh Linux user specifically for building a clean developer environment is one of the best ways to:

- learn Linux properly
- avoid breaking your existing setup
- evolve toward reproducible environments
- discover what tooling you truly need
- document your workflow cleanly

Given your goals (Python + full stack + automation + Linux/SRE mindset + MotorWeb workflow), this is exactly the kind of thing professional Linux developers and DevOps engineers do.

I would call the user:

```
bas
```

Simple and clean.

Avoid:

- `basic`
- `bass`

because shorter usernames are easier in shell work.

---

# High-Level Goal

You are going to build:

```
User: basPurpose: Clean developer workstationApproach: Minimal + modular + reproducible
```

The idea is:

```
OS  -> clean user      -> shell framework          -> dev tooling              -> projects                  -> containers/venvs
```

---

# Phase 1 — Create Clean User

From your current account:

```
sudo adduser bas
```

Then:

```
sudo usermod -aG sudo bas
```

Optional useful groups:

```
sudo usermod -aG docker bas
```

Later maybe:

```
sudo usermod -aG dialout bas
```

---

# Phase 2 — Login as bas

Either:

```
su - bas
```

or logout/login graphically.

---

# Phase 3 — Create Clean Directory Structure

Inside `/home/bas`:

```
mkdir -p ~/pjsmkdir -p ~/binmkdir -p ~/.config/shellmkdir -p ~/pjs/reposmkdir -p ~/pjs/vaultsmkdir -p ~/pjs/labsmkdir -p ~/pjs/pythonmkdir -p ~/pjs/webmkdir -p ~/pjs/scripts
```

This is your foundation.

---

# Phase 4 — Build Modular Shell Architecture

THIS is the important part.

Instead of giant `.profile` and `.bashrc` files:

## Use:

```
~/.config/shell/
```

---

# Recommended Structure

```
~/.config/shell/    env.sh    paths.sh    aliases.sh    functions.sh    java.sh    python.sh    node.sh    git.sh    prompt.sh
```

This is clean and scalable.

---

# Phase 5 — Minimal `.profile`

Create:

```
nano ~/.profile
```

Use:

```
# load shell environment[ -f "$HOME/.config/shell/env.sh" ] && \    source "$HOME/.config/shell/env.sh"[ -f "$HOME/.config/shell/paths.sh" ] && \    source "$HOME/.config/shell/paths.sh"
```

That’s it.

Minimal.  
Professional.

---

# Phase 6 — Minimal `.bashrc`

Create:

```
nano ~/.bashrc
```

Use:

```
# interactive shell config[ -f "$HOME/.config/shell/aliases.sh" ] && \    source "$HOME/.config/shell/aliases.sh"[ -f "$HOME/.config/shell/functions.sh" ] && \    source "$HOME/.config/shell/functions.sh"[ -f "$HOME/.config/shell/prompt.sh" ] && \    source "$HOME/.config/shell/prompt.sh"
```

Again:  
small and modular.

---

# Phase 7 — Build `env.sh`

Example:

```
export PJS_ROOT="$HOME/pjs"export REPOS_ROOT="$PJS_ROOT/repos"export VAULTS_ROOT="$PJS_ROOT/vaults"export WEB_ROOT="$PJS_ROOT/web"export PYTHON_ROOT="$PJS_ROOT/python"export EDITOR=nvimexport BROWSER=google-chrome
```

---

# Phase 8 — Build `paths.sh`

Example:

```
export PATH="$HOME/bin:$PATH"export PATH="$HOME/.local/bin:$PATH"
```

Later:

```
export PATH="$PYENV_ROOT/bin:$PATH"
```

---

# Phase 9 — Build `aliases.sh`

Example:

```
alias ll='ls -lah'alias gs='git status'alias cdp='cd $PJS_ROOT'alias cdr='cd $REPOS_ROOT'alias cdv='cd $VAULTS_ROOT'
```

---

# Phase 10 — Build `functions.sh`

THIS is where your environment becomes powerful.

Example:

```
mkcd() {    mkdir -p "$1"    cd "$1"}
```

Example:

```
venv-on() {    source .venv/bin/activate}
```

Example:

```
motorweb-dev() {    cd "$REPOS_ROOT/motorweb"}
```

Functions are MUCH more powerful than aliases.

---

# Phase 11 — Install Tooling Selectively

Now the fun starts.

Only install what your workflow truly needs.

---

# Recommended Core Stack

## Base Tools

```
sudo apt install:
```

- git
- curl
- wget
- build-essential
- tmux
- ripgrep
- fd-find
- jq
- tree
- htop
- vim or neovim

---

# Python Stack

Install:

- pyenv
- pipx
- venv

NOT global pip packages.

---

# Node Stack

Install:

- nvm

NOT apt nodejs.

---

# Java Stack

For MotorWeb/Spring work:

Install:

- OpenJDK 21
- Maven
- Gradle

---

# Docker Stack

Install:

- Docker  
    or:
- Rancher Desktop

---

# Phase 12 — Build Environment Validation Script

Instead of polluting `.profile`.

Create:

```
~/bin/dev-check
```

Example:

```
#!/usr/bin/env bashecho "--- java ---"java --versionecho "--- python ---"python --versionecho "--- node ---"node --version
```

Then:

```
chmod +x ~/bin/dev-check
```

Run manually.

VERY professional approach.

---

# Phase 13 — Create Dotfiles Git Repo

Critical.

Example:

```
mkdir ~/dotfilescd ~/dotfilesgit init
```

Track:

- `.profile`
- `.bashrc`
- `.config/shell/*`
- `.gitconfig`

---

# Phase 14 — Rebuild Your Existing Workflow Slowly

This is where learning happens.

Bring over ONLY:

- env vars you actually use
- aliases you actually need
- tooling you truly use

You’ll likely discover:

- obsolete configs
- duplicated tooling
- unnecessary PATH entries
- old experiments

This cleanup is incredibly valuable.

---

# Phase 15 — MotorWeb Workflow Architecture

Your future setup should look like:

```
~/pjs/repos/    motorweb/    motorweb-ui/    scripts/~/pjs/labs/    docker/    python/    ai/~/pjs/vaults/    obsidian/
```

---

# What You Will Learn From This

This project will teach you:

- Linux shell architecture
- environment isolation
- PATH management
- modular configuration
- reproducibility
- developer workstation engineering
- devops mindset
- configuration hygiene

Honestly, this is VERY aligned with SRE/platform-engineering thinking.

---

# Extremely Important Rule

Do NOT copy your old configs wholesale.

Rebuild intentionally.

That’s where the learning happens.

Your old environment becomes:

- reference material
- not migration material

That distinction is huge.

ok, motorweb is under /opt and im thinking of making all future repos of mine be under /opt rather than ~/pjs/repos. Is opt better for my repos? How should I use my directory ~? I track my Obsidian vault in ~/pjs/vaults. Should this go to /opt?

For **your own repos**, I would keep them under your home directory:

```
~/pjs/repos
```

Use `/opt` for **shared, system-level, or service-style software**, not normal personal development work.

My recommendation:

```
/home/pl/  pjs/    repos/      ← your Git repos    vaults/     ← Obsidian vaults    labs/       ← experiments    scripts/    ← personal scripts/opt/  motorweb/     ← shared/app-style deployment repo if needed  tools/        ← optional manually installed shared tools
```

Do **not** move your Obsidian vault to `/opt`. Keep it here:

```
~/pjs/vaults
```

Why: Obsidian vaults are personal user data. They should live in your home directory, be owned by your user, backed up normally, and synced/versioned easily.

`/opt` is better when something is:

```
installed for the machineshared by multiple usersmanaged like an applicationused for deployment/testingnot primarily personal notes/workspace
```

So for the new `bas` user, I’d do this:

```
/home/bas/pjs/repos       ← bas learning repos/home/bas/pjs/vaults      ← bas test vaults/opt/motorweb             ← shared MotorWeb app repo if both pl and bas need it
```

Important: if both `pl` and `bas` work on `/opt/motorweb`, set permissions carefully with a shared group. Otherwise Git can become annoying.

Best simple rule:

```
~/pjs = personal development workspace/opt = machine-level apps/tools/shared deployments
```

For your daily learning and Python/full-stack projects, use `~/pjs/repos`. For MotorWeb specifically, `/opt/motorweb` is okay because it already seems to be treated like an app/deployment workspace.