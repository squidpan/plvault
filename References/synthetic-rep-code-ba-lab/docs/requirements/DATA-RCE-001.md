---
id: DATA-RCE-001
project: Synthetic Rep Code Expansion
type: data-element
status: approved
title: Expanded Representative Identifier
description: Fictional four-character identifier for the representative context attached to a transaction.
classification: synthetic-training
categories: [data]
tags: [artifact-data-element, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Identifier Data Steward
source: Synthetic Advisor Registry
requirements: [FR-RCE-010-01, FR-RCE-010-02]
interfaces: ["[[INT-RCE-001]]"]
related: ["[[BR-RCE-001]]", "[[MAP-RCE-001]]"]
---

# Expanded Representative Identifier

| Attribute | Synthetic definition |
|---|---|
| System of record | Advisor Registry |
| Physical name | `expanded_rep_code` |
| Type / format | `CHAR(4)`, uppercase A–Z and digits 0–9 |
| Nullable | No for in-scope transactions |
| Example | `A7Q4` |
| Uniqueness | Unique within the fictional firm and effective period |
| Historical meaning | The transaction stores the original expanded code; later mapping changes do not rewrite it |
| Quality rules | Valid domain, active/entitled, no whitespace, no silent truncation |

Legacy alias is a separate derived interface value, not a replacement for this element.
