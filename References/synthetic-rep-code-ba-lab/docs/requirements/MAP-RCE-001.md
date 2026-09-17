---
id: MAP-RCE-001
project: Synthetic Rep Code Expansion
type: mapping
status: approved
title: Expanded Code to Legacy Alias Mapping
description: Fictional controlled lookup used only for registered legacy consumers.
classification: synthetic-training
categories: [data, mapping]
tags: [artifact-mapping, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Identifier Governance Owner
source: Synthetic mapping register v1
interface: "[[INT-RCE-001]]"
baseline: BL-RCE-2026-01
related: ["[[BR-RCE-001]]", "[[DATA-RCE-001]]"]
---

# Expanded Code → Legacy Alias Mapping

| Source | Target | Transform | Validation | Error disposition | Rule | Test |
|---|---|---|---|---|---|---|
| `expanded_rep_code` CHAR(4) | `legacy_rep_code` CHAR(3) | Effective-dated lookup by expanded code + consumer | Exactly one active approved row | Stop and queue exception | [[BR-RCE-001]] | [[TC-RCE-101-01]], [[TC-RCE-101-02]] |

Synthetic example row: `A7Q4 + LEGACY-ROUTER-1 → K42`, effective `2026-01-01` through open end, version `MAP-V1`.

Controls: unique active composite key, approval before activation, immutable version history, cache invalidation on activation, audit of change and use, and daily exception/reconciliation review.
