---
id: BR-RCE-001
project: Synthetic Rep Code Expansion
type: business-rule
status: approved
title: Unique Active Translation Required
description: A legacy alias may be emitted only when exactly one approved mapping is active for the expanded code, consumer, and processing time.
classification: synthetic-training
categories: [requirements, rules]
tags: [artifact-business-rule, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Identifier Governance Owner
source: "[[DEC-RCE-001]]"
effective_from: 2026-01-01
requirements: [FR-RCE-010-02, FR-RCE-010-03]
tests: ["[[TC-RCE-101-01]]", "[[TC-RCE-101-02]]"]
baseline: BL-RCE-2026-01
related: ["[[DATA-RCE-001]]", "[[MAP-RCE-001]]"]
---

# Unique Active Translation Required

An expanded identifier **must never be truncated**. A legacy alias may be used only when exactly one approved mapping matches the expanded identifier, registered consumer, and processing timestamp. Zero, multiple, future, expired, or disabled mappings must stop legacy delivery and produce an auditable exception.

The governance owner approves mappings; operations may remediate an exception but may not invent an alias.
