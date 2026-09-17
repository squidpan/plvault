---
id: DEC-RCE-001
project: Synthetic Rep Code Expansion
type: decision
status: approved
title: Centralize Legacy Translation
description: Use a governed translation service instead of consumer-specific truncation or distributed lookup logic.
classification: synthetic-training
categories: [decision]
tags: [artifact-decision, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Architecture and Product Decision Forum
source: Synthetic option analysis
decision_date: 2026-09-16
affected: ["[[FEATURE-RCE-010]]", "[[BR-RCE-001]]", "[[INT-RCE-001]]"]
related: ["[[RISK-RCE-001]]"]
---

# Centralize Legacy Translation

## Options considered

| Option | Benefit | Cost/risk |
|---|---|---|
| Truncate to three characters | Fast | Can produce a valid but wrong code; unacceptable |
| Each consumer owns lookup | Local autonomy | Duplicated rules, drift, weak auditability |
| Governed translation service | Consistent mapping, control, migration visibility | New dependency and operational ownership |

## Decision

Select the governed translation service. Preserve the expanded code as authoritative; translate only for registered legacy consumers. Fail closed when a unique active mapping is unavailable.

## Consequences

Requires mapping governance, service availability, exception ownership, reconciliation, monitoring, and a consumer migration inventory.
