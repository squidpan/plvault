---
categories:
  - "[[Processes]]"
type:
description:
source: chatgpt-manual
tags:
created: 2026-05-27
last: 2026-05-27
status:
origin:
run_id:
input_prompt:
---


## Target system:

- Pop!_OS
- Docker already cleaned/reinstalled
- Rancher Desktop removed
- Existing shared project:
    
    ```
    /opt/projects/motorweb
    ```
    
- Existing workflows:
    - MotorWeb dev
    - mw_notes_job app enhancements
    - Obsidian
    - obsidian-skills-ng
    - Python learning
    - Spring Boot learning
    - VS Code
    - PyCharm via JetBrains Toolbox

Goal:  
Build a clean, modular, reproducible Linux developer environment from scratch using a new user:

```
bas
```

---

# Recommended Final Architecture

```
/opt/projects/
    motorweb/

~/pjs/
    repos/
    vaults/
    scripts/
    tmp/

~/.config/shell/
    env.sh
    paths.sh
    aliases.sh
    functions.sh
    prompt.sh
```

---

# PHASE 0 — Create Tracking Repo

From `pl`:

```
mkdir -p ~/pjs/repos/linux-dev-env
cd ~/pjs/repos/linux-dev-env
git init
```

Suggested structure:

```
linux-dev-env/
    README.md
    setup/
    shell/
    docs/
```

---

# PHASE 1 — Create User `bas`

From `pl`:

```
sudo adduser bas
```

Add sudo:

```
sudo usermod -aG sudo bas
```

---

# PHASE 2 — Shared Project Group Setup

Create shared group:

```
sudo groupadd projects
```

Add users:

```
sudo usermod -aG projects pl
sudo usermod -aG projects bas
```

Assign ownership:

```
sudo chgrp -R projects /opt/projects
```

Permissions:

```
sudo chmod -R g+rwX /opt/projects
```

Preserve group ownership:

```
sudo find /opt/projects -type d -exec chmod g+s {} \;
```

---

# PHASE 3 — Login As `bas`

Either:

```
su - bas
```

or graphical login.

---

# PHASE 4 — Create Directory Structure

As `bas`:

```
mkdir -p ~/pjs/{repos,vaults,scripts,tmp}
mkdir -p ~/.config/shell
mkdir -p ~/bin
mkdir -p ~/dotfiles/originals
```

---

# PHASE 5 — Backup Default Dotfiles

```
cp ~/.profile ~/dotfiles/originals/profile.original
cp ~/.bashrc ~/dotfiles/originals/bashrc.original
```

Optional:

```
cp ~/.bash_logout ~/dotfiles/originals/bash_logout.original
```

---

# PHASE 6 — Create Minimal `.profile`

Edit:

```
nano ~/.profile
```

Content:

```
# ~/.profile

[ -f "$HOME/.config/shell/env.sh" ] && \
    source "$HOME/.config/shell/env.sh"

[ -f "$HOME/.config/shell/paths.sh" ] && \
    source "$HOME/.config/shell/paths.sh"
```

---

# PHASE 7 — Create Minimal `.bashrc`

Edit:

```
nano ~/.bashrc
```

Content:

```
# ~/.bashrc[ -f "$HOME/.config/shell/aliases.sh" ] && \    source "$HOME/.config/shell/aliases.sh"[ -f "$HOME/.config/shell/functions.sh" ] && \    source "$HOME/.config/shell/functions.sh"[ -f "$HOME/.config/shell/prompt.sh" ] && \    source "$HOME/.config/shell/prompt.sh"
```

---

# PHASE 8 — Create Shell Modules

## env.sh

```
nano ~/.config/shell/env.sh
```

Content:

```
export PJS_ROOT="$HOME/pjs"

export REPOS_ROOT="$PJS_ROOT/repos"
export VAULTS_ROOT="$PJS_ROOT/vaults"
export SCRIPTS_ROOT="$PJS_ROOT/scripts"

export EDITOR=vim
export BROWSER=google-chrome
```

---

## paths.sh

```
nano ~/.config/shell/paths.sh
```

Content:

```
export PATH="$HOME/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
```

---

## aliases.sh

```
nano ~/.config/shell/aliases.sh
```

Content:

```
alias ll='ls -lah'

alias cdp='cd $PJS_ROOT'
alias cdr='cd $REPOS_ROOT'
alias cdv='cd $VAULTS_ROOT'
alias cds='cd $SCRIPTS_ROOT'
```

---

## functions.sh

```
nano ~/.config/shell/functions.sh
```

Content:

```
mkcd() {
    mkdir -p "$1"
    cd "$1"
}
```

---

## prompt.sh

```
nano ~/.config/shell/prompt.sh
```

Content:

```
PS1='\u@\h:\w\$ '
```

---

# PHASE 9 — Reload Shell

```
source ~/.profile
source ~/.bashrc
```

Verify:

```
echo $PJS_ROOTalias
```

---

# PHASE 10 — Install Core Linux Tools

```
sudo apt update
```

Install:

```
sudo apt install -y \
    git \
    curl \
    wget \
    build-essential \
    tmux \
    ripgrep \
    fd-find \
    jq \
    tree \
    htop \
    vim \
    python3-pip \
    python3-venv
```

---

# PHASE 11 — Verify Existing GUI Apps

Test:

```
code
```

```
google-chrome
```

```
obsidian
```

These should already work because they are system-installed.

---

# PHASE 12 — VS Code Setup

Install recommended extensions ONLY:

- Python
- Pylance
- Docker
- GitLens
- Markdown All in One
- YAML

Avoid extension overload.

---

# PHASE 13 — Python Workflow (Simple First)

DO NOT install pyenv yet.

Use:

```
python3 -m venv .venvsource .venv/bin/activate
```

Inside projects.

Example:

```
cd ~/pjs/repos
mkdir python-test
cd python-test

python3 -m venv .venv
source .venv/bin/activate
```

Then:

```
pip install requests
```

This teaches clean Python fundamentals first.

---

# PHASE 14 — Docker Verification

Verify Docker:

```
docker ps
```

If permission denied:

logout/login again.

Test container:

```
docker run hello-world
```

---

# PHASE 15 — Git + GitHub SSH

Generate SSH key:

```
ssh-keygen -t ed25519 -C "bas@pop-os"
```

Start agent:

```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Add public key to GitHub:

```
cat ~/.ssh/id_ed25519.pub
```

Test:

```
ssh -T git@github.com
```

---

# PHASE 16 — Create First Real Dev Repos

As `bas`:

```
cd ~/pjs/repos
```

Clone or create:

```
linux-dev-env
obsidian-skills-ng
mw_notes_job
python-learning
springboot-learning
```

DO NOT copy old configs wholesale.

Rebuild intentionally.

---

# Recommended Future Phases (Later)

NOT NOW.

Later add:

- pyenv
- nvm
- tmux customization
- starship prompt
- shell completion
- Docker Compose workflows
- dev containers
- Kubernetes
- CI/CD helpers

Only after the base environment feels stable.

---

# README.md Template For Repo

You can place this in:

```
~/pjs/repos/linux-dev-env/README.md
```

[[README - Linux Developer Env Buiold - bas User]]