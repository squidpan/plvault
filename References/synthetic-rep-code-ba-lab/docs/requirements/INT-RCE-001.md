---
id: INT-RCE-001
project: Synthetic Rep Code Expansion
type: interface
status: approved
title: Order Entry to Legacy Routing via Translation Service
description: Fictional synchronous translation and routing exchange for a registered legacy consumer.
classification: synthetic-training
categories: [integration, data]
tags: [artifact-interface, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Integration Product Owner
source: Synthetic interface contract v1
requirements: [FR-RCE-010-02, FR-RCE-010-03, NFR-RCE-010-01]
data_elements: ["[[DATA-RCE-001]]"]
tests: ["[[TC-RCE-101-01]]", "[[TC-RCE-101-02]]"]
related: ["[[MAP-RCE-001]]", "[[RISK-RCE-001]]"]
---

# Order Entry → Translation Service → Legacy Routing

| Attribute | Synthetic definition |
|---|---|
| Trigger | Order ready for routing |
| Request | Expanded code, consumer ID, processing timestamp, correlation ID |
| Response | Outcome, legacy alias if resolved, mapping version, reason code |
| Timeout | 500 ms training assumption; no downstream send on timeout |
| Retry | Same correlation ID; idempotent result/delivery guard |
| Error path | Controlled exception queue owned by Operations Support |
| Reconciliation | Request outcomes vs. downstream acknowledgements by correlation ID |
| Monitoring | Error rate, latency, unmapped/ambiguous counts, queue age |

Compatibility: modern consumers receive the expanded code directly and do not invoke translation.
