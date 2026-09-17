---
id: US-RCE-101
project: Synthetic Rep Code Expansion
type: story
status: ready
title: Translate Expanded Identifier for a Legacy Consumer
description: Resolve an approved legacy alias without changing the authoritative expanded identifier.
classification: synthetic-training
categories: [requirements, integration]
tags: [artifact-story, project-rce, status-ready]
created: 2026-09-16
updated: 2026-09-16
owner_role: Product Owner
source: FR-RCE-010-01 through FR-RCE-010-03
epic: "[[EPIC-RCE-001]]"
feature: "[[FEATURE-RCE-010]]"
acceptance_criteria: "[[AC-RCE-101]]"
baseline: BL-RCE-2026-01
related: ["[[BR-RCE-001]]", "[[DATA-RCE-001]]", "[[INT-RCE-001]]", "[[RISK-RCE-001]]"]
---

# Translate Expanded Identifier for a Legacy Consumer

> [!tldr] TL;DR
> Preserve the fictional four-character identifier and supply a governed alias only when a registered legacy consumer needs it.

## User story

As an **order-routing operator**, I want **legacy-bound transactions to receive the correct governed alias**, so that **routing remains accurate while consumers migrate**.

## Business value

The story enables incremental modernization without silent data corruption or a synchronized enterprise cutover.

## Scope

Included: consumer capability lookup, active mapping resolution, audit event, controlled exception. Excluded: mapping administration UI and consumer retirement.

## Preconditions

- The expanded code already passed format and entitlement validation.
- Consumer capability registration is available.
- Mapping data is approved and effective-dated.

## Linked detail

- AC: [[AC-RCE-101]]
- Rule: [[BR-RCE-001]]
- Data/mapping: [[DATA-RCE-001]], [[MAP-RCE-001]]
- Interface: [[INT-RCE-001]]
- Decision/risk: [[DEC-RCE-001]], [[RISK-RCE-001]]
