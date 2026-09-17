---
id: FEATURE-RCE-010
project: Synthetic Rep Code Expansion
type: feature
status: approved
title: Controlled Legacy Identifier Translation
description: Translate an expanded identifier only when a legacy consumer requires a shorter compatible value.
classification: synthetic-training
categories: [requirements, integration, data]
tags: [artifact-feature, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Product Owner
source: "[[EPIC-RCE-001]]"
epic: "[[EPIC-RCE-001]]"
baseline: BL-RCE-2026-01
related: ["[[US-RCE-101]]", "[[DEC-RCE-001]]", "[[LINEAGE-RCE-001]]"]
---

# Controlled Legacy Identifier Translation

## Capability outcome

Modern workflows use the four-character code end to end; a controlled service supplies a three-character alias only to explicitly registered legacy consumers.

## Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-RCE-010-01 | The solution shall preserve the four-character identifier as the authoritative transaction value. | Must |
| FR-RCE-010-02 | The solution shall resolve exactly one active, effective-dated legacy alias when a registered legacy consumer requires one. | Must |
| FR-RCE-010-03 | The solution shall stop legacy delivery when no unique active mapping exists. | Must |
| NFR-RCE-010-01 | The solution shall record input, output, mapping version, consumer, timestamp, outcome, and correlation ID for every translation attempt. | Must |

## Supporting artifacts

- Story/AC: [[US-RCE-101]], [[AC-RCE-101]]
- Rule/data/interface: [[BR-RCE-001]], [[DATA-RCE-001]], [[INT-RCE-001]]
- Decision/risk: [[DEC-RCE-001]], [[RISK-RCE-001]]
- Lineage/mapping: [[LINEAGE-RCE-001]], [[MAP-RCE-001]]
