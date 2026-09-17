---
id: LINEAGE-RCE-001
project: Synthetic Rep Code Expansion
type: lineage
status: approved
title: Expanded Representative Identifier End-to-End Lineage
description: Fictional lineage from advisor setup through transaction confirmation.
classification: synthetic-training
categories: [data, lineage]
tags: [artifact-lineage, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Data Domain Owner
source: Synthetic lineage workshop
data_elements: ["[[DATA-RCE-001]]"]
interfaces: ["[[INT-RCE-001]]"]
related: ["[[MAP-RCE-001]]"]
---

# Expanded Representative Identifier Lineage

| Seq | Source/producer | Element | Transform/rule | Interface | Consumer/store | Use/control |
|---:|---|---|---|---|---|---|
| 1 | Advisor Registry | [[DATA-RCE-001]] | Validate domain and entitlement | Registry API | Order Entry | Capture authoritative value |
| 2 | Order Entry | Expanded code | Preserve unchanged | [[INT-RCE-001]] | Translation Service | Determine consumer capability |
| 3 | Translation Service | Expanded code + alias | [[BR-RCE-001]] / [[MAP-RCE-001]] | [[INT-RCE-001]] | Legacy Routing | Emit alias or stop |
| 4 | Legacy Routing | Alias + correlation ID | No identifier transform | Route message | Confirmation/Audit | Reconcile acknowledgement |

The original expanded code remains on the authoritative transaction and audit record at every stage.
