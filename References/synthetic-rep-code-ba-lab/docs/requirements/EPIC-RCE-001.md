---
id: EPIC-RCE-001
project: Synthetic Rep Code Expansion
type: epic
status: approved
title: Expand Representative Identifier Capacity
description: Enable scalable representative identifiers without losing compatibility, control, or auditability.
classification: synthetic-training
categories: [requirements, data]
tags: [artifact-epic, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Product Executive
source: Synthetic capacity assessment
baseline: BL-RCE-2026-01
related: ["[[FEATURE-RCE-010]]", "[[RISK-RCE-001]]"]
---

# Expand Representative Identifier Capacity

## The point

Increase the identifier namespace from three to four characters while keeping transactions accurate across modern and legacy consumers.

## Success measures

- 100% of supported four-character identifiers persist without truncation.
- 100% of legacy-bound transactions use one active approved mapping or stop in a controlled exception state.
- Every translation is reconstructable by input, output, mapping version, timestamp, and correlation ID.

## Scope

Included: identifier creation/validation, translation for legacy consumers, transaction propagation, audit, monitoring, and reconciliation. Excluded: compensation design, advisor hierarchy redesign, and retirement of every legacy consumer.

## Capabilities

- [[FEATURE-RCE-010]]

## Approval/baseline

Baseline `BL-RCE-2026-01` is fictional and includes the linked approved requirements and AC.
