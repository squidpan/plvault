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

# Linux Developer Environment — bas User

## Purpose

This repository tracks the setup and evolution of a clean Linux developer workstation environment on Pop!_OS.

Goals:

- modular shell architecture
- reproducible environment
- Docker-based workflows
- Python development
- MotorWeb development support
- Obsidian knowledge workflows

---

# Directory Structure

```text
~/pjs/
    repos/
    vaults/
    scripts/
    tmp/

~/.config/shell/
```

---

# Shell Architecture

## ~/.profile

Loads:

- env.sh
- paths.sh

## ~/.bashrc

Loads:

- aliases.sh
    
- functions.sh
    
- prompt.sh
    

---

# Shared Projects

```text
/opt/projects/
```

Used for:

- shared application repos
- MotorWeb
- deployment-oriented projects

---

# Python Workflow

Currently using:

- system python
- venv
- pip

pyenv intentionally deferred until needed.

---

# Docker Workflow

Docker installed cleanly.  
Rancher Desktop removed.

Verification:

```bash
docker ps
docker run hello-world
```

---

# Philosophy

- minimal
- modular
- reproducible
- intentionally built
- version controlled
