---
id: DISC-RCE-001
project: Synthetic Rep Code Expansion
type: discovery-note
status: complete
title: Legacy Consumer Translation Discovery
description: Fictional discovery findings that produced the translation feature.
classification: synthetic-training
categories: [discovery]
tags: [artifact-discovery-note, project-rce, status-complete]
created: 2026-09-16
updated: 2026-09-16
owner_role: Business Analyst
source: Synthetic cross-functional workshop
related: ["[[FEATURE-RCE-010]]", "[[DEC-RCE-001]]", "[[RISK-RCE-001]]"]
---

# Legacy Consumer Translation Discovery

## Objective

Determine how expanded identifiers can flow through modern systems while supporting one fictional legacy router.

## Findings

| Type | Statement | Confidence | Derived artifact |
|---|---|---|---|
| Fact | The legacy router accepts only three characters. | High | [[INT-RCE-001]] |
| Fact | Truncation can collide with an existing code. | High | [[RISK-RCE-001]] |
| Decision | Translation will be centralized and governed. | Approved | [[DEC-RCE-001]] |
| Requirement signal | Mapping must be unique and effective-dated. | High | [[BR-RCE-001]] |
| Open question | Which additional consumers need temporary aliases? | Open | Consumer inventory action |

## Follow-up

Create consumer inventory, validate lineage per consumer, assign mapping owner/support role, prototype exception and reconciliation behavior, and review AC with Product, Engineering, QA, Operations, and Control roles.
