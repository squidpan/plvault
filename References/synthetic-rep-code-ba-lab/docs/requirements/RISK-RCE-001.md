---
id: RISK-RCE-001
project: Synthetic Rep Code Expansion
type: risk
status: approved
title: Silent Identifier Truncation Misroutes a Transaction
description: If a four-character code is truncated, a syntactically valid but incorrect three-character code may cause misrouting and weak detectability.
classification: synthetic-training
categories: [risk, data]
tags: [artifact-risk, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Product Risk Owner
source: Synthetic failure-mode analysis
probability: medium
impact: high
affected: ["[[EPIC-RCE-001]]", "[[US-RCE-101]]", "[[INT-RCE-001]]"]
related: ["[[DEC-RCE-001]]", "[[BR-RCE-001]]"]
---

# Silent Identifier Truncation Misroutes a Transaction

Mitigations: prohibit truncation, use one controlled mapping source, validate uniqueness/effective dates, fail closed, reconcile translations to downstream acknowledgements, alert on mapping exceptions, and retain reconstructable audit evidence.

Contingency: stop affected legacy delivery, isolate impacted correlation IDs, notify the support/control roles, reconcile outcomes, correct the mapping under change control, and replay only after authorization.
