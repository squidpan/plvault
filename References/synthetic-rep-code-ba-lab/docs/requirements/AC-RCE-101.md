---
id: AC-RCE-101
project: Synthetic Rep Code Expansion
type: acceptance-criteria
status: approved
title: Acceptance criteria — legacy identifier translation
description: Observable success, exception, and audit behavior for US-RCE-101.
classification: synthetic-training
categories: [requirements, testing]
tags: [artifact-acceptance-criteria, project-rce, status-approved]
created: 2026-09-16
updated: 2026-09-16
owner_role: Product Owner
source: "[[US-RCE-101]]"
story: "[[US-RCE-101]]"
tests: ["[[TC-RCE-101-01]]", "[[TC-RCE-101-02]]"]
baseline: BL-RCE-2026-01
related: ["[[BR-RCE-001]]", "[[INT-RCE-001]]"]
---

# Acceptance Criteria — Legacy Identifier Translation

## AC-RCE-101-01 — Active unique mapping

**Given** expanded identifier `A7Q4`, legacy consumer `LEGACY-ROUTER-1`, and one active mapping to `K42`
**When** the transaction is prepared for that consumer
**Then** the outbound legacy field contains `K42`
**And** the authoritative transaction retains `A7Q4`.

## AC-RCE-101-02 — No active mapping

**Given** a valid expanded identifier with no active mapping for the processing time
**When** translation is requested
**Then** no legacy message is sent
**And** the transaction enters a controlled exception state with reason `NO_ACTIVE_MAPPING`.

## AC-RCE-101-03 — Multiple active mappings

**Given** more than one active candidate mapping for the same expanded identifier and consumer
**When** translation is requested
**Then** no alias is selected
**And** the transaction enters exception state `AMBIGUOUS_MAPPING`.

## AC-RCE-101-04 — Expired mapping

**Given** a mapping whose effective end precedes the transaction's processing time
**When** translation is requested
**Then** the expired mapping is not used.

## AC-RCE-101-05 — Audit evidence

**Given** any translation attempt
**When** processing completes or stops
**Then** audit evidence records the input, selected output if any, mapping version, consumer, timestamp, outcome/reason, and correlation ID without exposing prohibited sensitive data.

## AC-RCE-101-06 — Retry consistency

**Given** a retry with the same correlation ID and unchanged effective mapping version
**When** translation is repeated
**Then** the same outcome is returned without creating a duplicate downstream delivery.
