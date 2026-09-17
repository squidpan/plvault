# Synthetic Rep Code BA Lab

An applied, fictional Business Analyst case study for identifier expansion across a trading lifecycle. It combines domain learning, requirements analysis, data lineage, mappings, interfaces, controls, SQL investigation, acceptance criteria, testing, and Development handoff.

> **Synthetic-only boundary:** Nothing in this repository describes an employer's actual systems, policies, schemas, data, decisions, or requirements. Never add proprietary names, screenshots, issue exports, meeting notes, source code, queries, production data, credentials, or customer information. Actual work belongs only in employer-approved systems.

## Relationship to the BA Starter Pack

- The BA Starter Pack is the reusable methodology and template library.
- This repository is the applied synthetic case study.

Do not copy the Starter Pack templates here. Instantiate them as case-study artifacts under `docs/requirements/`.

## Repository map

| Path | Purpose |
|---|---|
| `docs/domain/` | Trading, rep-code, lineage, control, and SQL learning |
| `docs/requirements/` | Connected Epic → Feature → Story → AC → rule/data/interface/decision/risk/test artifacts and RTM |
| `diagrams/` | Layered process, lineage, compatibility, and ERD diagrams |
| `sql/` | PostgreSQL synthetic schema, seed data, and BA investigation queries |
| `exercises/` | Discovery and analysis simulations |
| `sources/` | Source register and confidentiality boundary—not proprietary source files |
| `archive/` | Superseded synthetic artifacts retained for comparison |

## Requirements narrative

Start at `docs/requirements/00-RCE-WALKTHROUGH.md`. It tells the requirements story and links every detailed artifact.

## Working lifecycle

1. Establish the outcome, scope, stakeholders, and authoritative source.
2. Walk the current trading process and trace the identifier end to end.
3. Identify gaps at every receive/store/validate/transform/transmit/use point.
4. Record rules, data definitions, interfaces, decisions, risks, and open questions.
5. Derive requirements, stories, acceptance criteria, and tests.
6. Use the RTM to expose missing coverage.
7. Validate with SQL, diagrams, negative paths, reconciliation, and UAT evidence.
8. Baseline the approved set and conduct a Development/QA walkthrough.

## Validation

From the repository root:

    python3 scripts/validate_artifacts.py

Optional diagram rendering requires PlantUML:

    plantuml -checkonly diagrams/*.puml

## What was intentionally removed

Old recruiter/opportunity status logs were not carried into this revised learning repository. They were time-bound administrative records rather than reusable BA assets and included unnecessary real-world recruiting context.
