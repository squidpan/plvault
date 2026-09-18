---
categories:
  - "[[Clippings]]"
title: "The Modern Python Project Layout That Saved My Production Code"
source: "https://dailypythonpro.medium.com/the-modern-python-project-layout-that-saved-my-production-code-1966ec0237f9?sk=ae89261e1300020e304a54ad04dd1f0b"
author:
  - "[[Daily Python]]"
published: 2026-08-14
created: 2026-08-27
description: "A clean, production-tested blueprint using uv, pyproject.toml, and the src/ layout."
tags:
  - "clippings"
url: "https://dailypythonpro.medium.com/the-modern-python-project-layout-that-saved-my-production-code-1966ec0237f9?sk=ae89261e1300020e304a54ad04dd1f0b"
---
Starting a new Python project usually feels delightful. You fire up a terminal, make a directory, toss in a `main.py`, create a quick script, and hit run. Within ten minutes, your prototype is live and delivering results.

Then three months pass.

> Not a Medium member? You can read it [here for free](https://dailypythonpro.medium.com/the-modern-python-project-layout-that-saved-my-production-code-1966ec0237f9?sk=ae89261e1300020e304a54ad04dd1f0b).

Your quick script has evolved into a full-fledged backend service. What started as a single file is now an unruly collection of modules: `utils.py`, `helpers.py`, `common.py`, and `tools.py`—four separate files that all do mysteriously similar things, yet nobody on your team dares to delete any of them. You have a `[requirements.txt](https://medium.com/@dailypythonpro/stop-using-requirements-txt-the-pylock-toml-migration-guide-cdb963275422)` from six months ago, a `setup.py` that someone copied from an old StackOverflow thread, and a `tox.ini` that hasn't worked since Python 3.10.

If opening your codebase gives you the same feeling as opening a closet where everything was crammed inside right before guests arrived, you are not alone.

For years, Python project structure felt less like an engineering discipline and more like an individual art form. Every team had its own custom setup, every open-source repository invented its own layout, and onboarding a new engineer meant explaining three layers of legacy build tooling before they could run a single unit test.

The good news? **Python project architecture has reached a level of maturity, speed, and elegance we could only dream of a few years ago.**

After spending considerable time analyzing modern packaging standards, testing various tooling combinations across production environments, and refining repository layouts, I’ve settled on a unified project architecture that eliminates guesswork.

In this guide, I will share the exact blueprint I use to structure production-ready Python applications — one that stays clean, scales effortlessly, and remains a joy to maintain months after the initial release.

## `pyproject.toml` as the Single Source of Truth

If there is one fundamental rule for modern Python development, it is this: **your project configuration must live in a single, standardized file.**

Historically, Python repositories suffered from fragmented configuration. A typical production repository used to look like an artifact museum of Python build systems:

- `setup.py` for build rules and package metadata
- `requirements.txt` for runtime dependencies
- `requirements-dev.txt` for development dependencies
- `setup.cfg` or `flake8` for linting rules
- `.black` or `pyproject.toml` for code formatting
- `pytest.ini` for testing flags

This fragmentation created friction everywhere. [CI/CD pipelines](https://medium.com/@cloudwithazeem/kubernetes-vs-openshift-choosing-devops-and-ci-cd-workflows-853b360f0ac5) had to parse three different files, new developers spent hours getting their local environment aligned, and stale settings accumulated across ignored config files.

Thanks to [PEP 621](https://peps.python.org/pep-0621/) and universal ecosystem adoption, `**pyproject.toml**` **now acts as the single source of truth for your entire codebase.**

![pyproject.toml as the Single Source of Truth](https://miro.medium.com/v2/resize:fit:700/1*_NqaV8LtETfREOfsxw1PYg.png)

**Image 01:** A sample pyproject.toml file showing how a Python project can define its project metadata, dependencies, and configuration in a single standardized file.

Notice how clean this consolidation is. Your metadata, **runtime dependencies**, **developer tooling**, **linter configurations**, and **test runner rules** exist in one place. When you want to update lint rules or adjust target Python versions, you open one file.

## `uv`: Modern Workflow

Having a unified configuration file is incredible, but you also need a package manager that respects your time.

For years, the Python ecosystem forced us to stitch together multiple tools: `pyenv` to install Python versions, `virtualenv` or `venv` to isolate environments, `pip-tools` or `poetry` to compile lockfiles, and `pip` to install packages. Each tool was competent, but the combined workflow felt sluggish and fragile.

Enter [uv](https://github.com/astral-sh/uv), the extremely fast Python package and project manager written in Rust by Astral. 🛠️

In my testing and daily usage, `**uv**` **has completely transformed how I interact with Python environments.** It isn't just a faster `pip`; it is an all-in-one execution engine that seamlessly manages Python releases, virtual environments, dependency resolution, and script execution. I wrote this article to explain how **uv** works. You can read it for a more detailed, in-depth explanation.

[

## uv Is Quietly Fixing Python’s Biggest Pain Point

### I ignored UV for months, I Was Wrong. After switching from pip, I realized the real benefit had nothing to do with…

dailypythonpro.medium.com



](https://dailypythonpro.medium.com/uv-is-quietly-fixing-pythons-biggest-pain-point-368e1fb77d92?source=post_page-----1966ec0237f9---------------------------------------)

## Why Speed Changes Developer Habits

When environment creation and dependency locking take 45 seconds, developers take shortcuts. They avoid updating packages, they reuse dirty global environments, and they delay running fresh installs locally.

When `uv` performs full dependency resolution and installation in **under 200 milliseconds**, developer behavior changes immediately:

- **Clean sub-shell executions:** Running commands inside isolated environments becomes instant using `uv run`.
- **Deterministic lockfiles:** Generating and updating lockfiles becomes a zero-friction habit rather than a chore.
- **Seamless version switching:** You can run tests across Python 3.11, 3.12, and 3.13 without manually configuring local interpreters via `uv run --python 3.13 pytest`.

Starting a fresh modern project with `uv` takes seconds:

uv init --package my_service  
cd my_service  
uv add httpx pydantic pydantic-settings  
uv add --dev pytest ruff mypy pre-commit

This single sequence initializes your directory, sets up your virtual environment, generates a deterministic lockfile, and configures your `pyproject.toml`. No manual virtual environment activation scripts required!

Python 3.15 introduces some very interesting features. If you’re curious about how Python is evolving and becoming more modern, you can read this article. I explain how some of the new features in Python 3.15 could make Python more challenging for beginners.

[

## Python 3.15: The End of Simple Python?

### The hidden engineering reasons behind CPython’s most divisive update yet.

dailypythonpro.medium.com



](https://dailypythonpro.medium.com/python-3-15-the-end-of-simple-python-4be2b2e20898?source=post_page-----1966ec0237f9---------------------------------------)

## The `src/` Layout

When deciding on directory architecture, developers often choose between a “flat layout” (where the package folder lives directly in the root) and the `**src/**` **layout** (where application source code lives inside a dedicated `src/` directory).

After diagnosing subtle packaging bugs in production builds, I strongly advocate for the `**src/**` **layout** for every serious Python application.

Here is what a clean repository layout looks like:

![](https://miro.medium.com/v2/resize:fit:700/1*AR5X9b54EMyX6cmRKL2UtQ.png)

**Image 02:** A typical `src/` layout used in many well-structured Python applications. In my experience, a large number of production-grade Python projects follow this structure because it helps keep application code separate from configuration, tests, documentation, and other project files.

### The Subtle Danger of Flat Layouts

In a flat layout, your directory structure puts your package folder side-by-side with your test directory at the root level:

![The Subtle Danger of Flat Layouts for python project](https://miro.medium.com/v2/resize:fit:700/1*Lot-z8NUcsnC0SfoLaidRg.png)

**Image 03:** The Subtle Danger of Flat Layouts for python project

When you execute tests locally in a flat layout, Python automatically adds the current working directory to `sys.path`. As a result, `import my_service` imports your raw source directory directly from disk, **not the installed version of your package.**

This creates a dangerous false sense of security. Your test suite might pass locally, but fail in production because:

- An uncommitted file or asset was present locally but omitted from the package build.
- A compiled extension or dynamic entry point wasn’t generated correctly during package installation.
- Relative imports behaved differently inside the raw folder versus an installed package.

The `src/` layout prevents this entire category of bugs. Because `src/` is not automatically on Python’s path when running tools from the root directory, your test runners are forced to install your package in **editable mode** (`uv pip install -e .`) before executing. You test what you actually package and ship! 📦

## Internal Package Architecture

Inside the `src/my_service/` module, the goal is to establish predictable boundaries so engineers never have to guess where new code belongs.

### 1. `models/`: Pure Data Contracts

Your data models define the state and structure of your application. These should be lightweight, typed, and declarative. I prefer using [Pydantic](https://www.google.com/search?q=https%3A%2F%2Fdocs.pydantic.dev%2F) v2 or native dataclasses.

Crucial architectural rule: **business logic and side effects do not belong in models.**

![Python Pydantic code example demonstrating a structured data model and validation.](https://miro.medium.com/v2/resize:fit:700/1*g5HdnCmBrTSJ9DVOUehY7g.png)

**Image 04:** A Python code example using **Pydantic** to define and validate structured data with type-safe models.

### 2. `services/`: Business Logic & Orchestration

This is where your application actually does work. Service modules execute business rules, interact with databases, call external APIs, and coordinate operations.

![Python project services directory containing business logic and orchestration code.](https://miro.medium.com/v2/resize:fit:700/1*tN--TWUzT06mgqVLKkgiXw.png)

**Image 05:** The `services/` directory in a Python project, which contains the **business logic and orchestration layer** responsible for coordinating application workflows and connecting different components.

By explicitly isolating **data definitions** inside `models/` and **action logic** inside `services/`, you prevent circular dependencies and keep your unit tests focused.

### 3. `config.py`: Centralized & Validated Settings

Never scatter `os.getenv()` or `os.environ.get()` calls across your codebase. Scattered environment variables turn debugging into a scavenger hunt and result in silent failures when required variables are missing.

Use `pydantic-settings` to create a single, strongly-typed configuration object that validates environment variables at application startup:

![Python Pydantic Settings model used to define and validate application configuration.](https://miro.medium.com/v2/resize:fit:700/1*KWiGXj0ZuuW4BThl-q52kQ.png)

**Image 06:** A Python example demonstrating how **Pydantic Settings** can be used to manage application configuration through a typed settings model, making environment variables and configuration values easier to validate and maintain

If a required environment variable is missing or malformed, your app fails immediately with a clear error message during launch — long before taking traffic in production.

### 4. The Discipline of `utils/`

Every codebase eventually creates a `utils/` or `helpers/` module. Left unchecked, `utils/` becomes a garbage dump for orphaned code. 🗑️

I enforce a simple mental rule: **If a helper function knows about your specific business domain, it does not belong in** `**utils/**`**.**

- Allowed in `utils/`: Generic date parsers, cryptographic hash wrappers, exponential backoff decorators, or custom string formatting.
- Not allowed in `utils/`: `calculate_user_discount()`, `format_invoice_payload()`, or `parse_stripe_webhook()`. Those belong strictly inside their respective domain services.

## Static Quality & Ergonomics

A great structure relies on automated enforcement so code reviews can focus on architecture rather than formatting debates.

### Replacing Legacy Linters with Ruff

In older projects, maintaining static analysis meant orchestrating `flake8`, `isort`, `black`, and `pyupgrade` simultaneously.

[Ruff](https://github.com/astral-sh/ruff) unifies all of these tools into a single, lightning-fast Rust executable. It handles linting, auto-formatting, import sorting, and code modernization in milliseconds.

Integrating Ruff into your `pyproject.toml` ensures that every developer on your team automatically enforces identical code formatting rules:

[tool.ruff]  
line-length = 88  
[tool.ruff.lint]  
select = ["E", "F", "I", "UP", "B", "SIM"]

### Strict Type Safety with Mypy

In 2026, dynamic typing without type hints in production code is a unnecessary risk. Type annotations are self-documenting code that your IDE uses to catch bugs before you even commit.

Configure **Mypy** in strict mode right from project inception:

[tool.mypy]  
strict = true  
python_version = "3.12"

Retrofitting strict type safety into a legacy codebase is challenging; starting with `strict = true` on day one takes almost zero extra effort and prevents entire classes of `AttributeError` and `TypeError` runtime crashes.

## Cross-Platform Ergonomics

While `Makefile` has traditionally been used to alias common commands, it causes friction for team members developing on Windows.

A modern alternative gaining rapid adoption is [just](https://github.com/casey/just), a handy command runner that works identically across Linux, macOS, and Windows.

Creating a concise `justfile` in your repository root gives every engineer a simple set of commands:

# List available commands  
default:  
    @just --list  
# Format all code automatically  
fmt:  
    uv run ruff format .  
    uv run ruff check . --fix  
# Run static analysis and type checks  
check:  
    uv run ruff check .  
    uv run mypy src/  
# Run unit tests  
test:  
    uv run pytest  
# Execute full validation pipeline  
all: fmt check test

Now, onboarding a team member requires a single instruction: _“Clone the repository and run_ `_just all_`_."_ 🚀

## Lockfile Portability & Multi-Package Architecture

As your engineering organization expands, two advanced operational requirements usually arise: **reproducible deployment lockfiles** and **monorepo workspaces**.

### Standardized Lockfiles

While `uv.lock` provides exceptional performance for local development, the ecosystem is actively shifting toward interoperable, tool-agnostic standards like [PEP 751](https://peps.python.org/pep-0751/) (`pylock.toml`).

Using standardized lockfiles ensures that your security scanners, deployment containers, and CI/CD audit tools can parse your exact locked dependency tree without requiring proprietary CLI plugins.

### Multi-Package Workspaces

When your application grows beyond a single package into multiple microservices or shared internal libraries, avoid creating scattered independent repositories. Instead, leverage `uv` workspaces inside a clean monorepo structure:

# pyproject.toml in root directory  
[tool.uv.workspace]  
members = ["packages/*", "services/*"]

This structure allows you to share common domain models or utility libraries across multiple services while keeping dependency management centralized.

## Structural Pitfalls to Avoid

To keep your repository aging gracefully, steer clear of these five common anti-patterns:

- **Avoid Barrel Re-Exports:** Resist the urge to import and re-export everything inside high-level `__init__.py` files. It creates circular import traps, increases memory footprint, and obscures where functions are defined.
- **Avoid Deep Hierarchy Nesting:** If a file path looks like `src/my_app/services/providers/aws/s3/v2/uploader.py`, your abstractions are too deep. Keep your package layout flat within reason—usually two to three nesting levels deep at most.
- **Avoid Hardcoded File Paths:** Always resolve relative file paths using `importlib.resources` or `pathlib.Path(__file__).parent` rather than assuming working directory context.
- **Avoid Unversioned Environments:** Always check your lockfile (`uv.lock` or `pylock.toml`) into version control for applications to ensure 100% reproducible builds across staging and production environments.
- **Avoid Optional Quality Gates:** Never treat linting and type checking as optional manual steps. Automate them via `pre-commit` hooks and GitHub Actions pipelines so unvetted code never hits your primary branch.

## Summary

Building clean Python projects is not about creating complex abstractions or showing off clever design patterns. **It is about removing friction so you can focus on writing domain logic.**

By establishing a modern foundation, you unlock immediate benefits:

- `**pyproject.toml**` provides a single, unified home for all metadata and tool configurations.
- `**uv**` replaces slow legacy workflows with near-instant package installation and environment setup.
- **The** `**src/**` **layout** guarantees that test runs accurately mirror installed package builds.
- `**models/**` **and** `**services/**` **separation** keeps data structures decoupled from business operations.
- **Ruff & Mypy** automate style enforcement and catch type errors before deployment.
- `**justfile**` gives contributors a cross-platform command interface.

When you eliminate structural ambiguity, you no longer waste time debating directory layouts or fighting package managers. You build software that is easy to onboard into, straightforward to test, and effortless to ship.

Pick a clean layout, lock in modern defaults, and spend your energy building software worth shipping. 💡