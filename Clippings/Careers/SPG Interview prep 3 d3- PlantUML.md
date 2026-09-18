---
categories:
  - "[[Clippings]]"
title: SPG Interview prep 3 d3- PlantUML
source: https://chatgpt.com/g/g-p-6a5517dc2a148191b5c289c2f4d2ce72/c/6a6b4867-a174-83ea-8e69-f7608b9878cc
author:
published:
created: 2026-08-05
description: SPG Interview prep 3 d3- PlantUML
tags:
  - chatgpt/conversation
---
I think D3 is where we should slow down and get it exactly right.

This is **the business diagram**.

If D2 answers:

> **"What is Surefyre?"**

then D3 answers:

> **"What actually happens when someone wants insurance?"**

This is also the first diagram where I think we should use **swimlanes**, just like we did in Farm Credit.

---

# Why swimlanes?

We are no longer showing software architecture.

We're showing **ownership**.

Who owns each activity?

That is much easier to understand.

---

# Proposed D3

Instead of this

```
Submission

↓

Validation

↓

Quote

↓

Bind

↓

Policy
```

I'd rather show

```
Retail Agent | Agent Portal | Underwriter | Enterprise Systems
```

because immediately you know

who is doing what.

---

# Proposed D3 Layout

```
================================================================================

                    D3 — Agent Submission Lifecycle

================================================================================

Retail Agent        Agent Portal       Underwriter         Enterprise Systems

      │                  │                   │                    │
      │ Start New App    │                   │                    │
      ├─────────────────▶│                   │                    │
      │                  │                   │                    │
      │ Enter Applicant  │                   │                    │
      ├─────────────────▶│                   │                    │
      │                  │                   │                    │
      │ Upload Docs      │                   │                    │
      ├─────────────────▶│                   │                    │
      │                  │                   │                    │
      │                  │ Validate Fields   │                    │
      │                  ├──────────────────▶│                    │
      │                  │                   │                    │
      │                  │ Rules             │                    │
      │                  │ Queue Assignment  │                    │
      │                  │                   │                    │
      │                  │──────────────────▶│                    │
      │                  │                   │                    │
      │                  │                   │ Review Risk        │
      │                  │                   │                    │
      │                  │                   │ Get Rating ───────▶│
      │                  │                   │                    │
      │                  │                   │◀───────────────────│
      │                  │                   │                    │
      │                  │                   │ Quote              │
      │                  │◀──────────────────│                    │
      │                  │                   │                    │
      │◀─────────────────│                   │                    │
      │                  │                   │                    │
      │ Accept Quote     │                   │                    │
      ├─────────────────▶│                   │                    │
      │                  │                   │                    │
      │                  │──────────────────▶│                    │
      │                  │                   │ Bind Coverage      │
      │                  │                   │───────────────▶    │
      │                  │                   │                    │
      │◀─────────────────│ Policy Issued     │                    │

================================================================================
```

---

## Why I like this

Notice we haven't mentioned

AIM

ImageRight

REST

SOAP

JSON

JavaScript

Nothing.

This is a **business diagram.**

That is exactly what D3 should be.

---

# D3 should answer ONE question

> **"What happens from the moment a retail agent starts a submission until a policy is issued?"**

Nothing more.

---

# Even better...

I would remove

"Validation"

"Rules"

"Workflow"

as boxes.

Those belong in D2.

Instead

they become activities.

Example

```
Agent Portal

Validate Required Fields

Validate Documents

Determine Program

Assign Queue

Notify Underwriter
```

That's much more natural.

---

# I also want to simplify underwriting

Instead of

Approve

Decline

Refer

Quote

Bind

I'd make the primary path

```
Review

↓

Need More Information?

↓

Rate

↓

Quote

↓

Customer Accepts?

↓

Bind

↓

Issue
```

Later,

D4 becomes

```
Underwriter Decision Tree
```

where all the

Referral

Senior Approval

Decline

Authority

exceptions

are shown.

That separation mirrors how we approached Farm Credit:

- **D3 = Happy path (business flow)**
    
- **D4 = Decision logic (branches and exceptions)**
    

---

# I would actually redesign the remaining diagrams slightly

Now that we've gone through D1 and D2, I think the complete set should tell a coherent story.

|Diagram|Primary Question|
|---|---|
|D1|Who are the participants?|
|D2|What is Surefyre?|
|D3|What happens to a submission?|
|D4|How does underwriting make decisions?|
|D5|What does the Technical Consultant implement?|
|D6|How do systems integrate?|
|D7|How is a new customer/program implemented?|
|D8|What technologies does the Technical Consultant configure?|

That sequence builds naturally from business context to implementation, just like we did with the Farm Credit diagrams.

---

## One suggestion before I generate D3

Based on what we've learned from D1 and D2, I propose a new rule for all remaining diagrams:

> **Every diagram should answer exactly one interview question.**

That will keep them focused, readable, and memorable.

For D3, the interview question is:

> **"Walk me through a typical insurance submission from start to finish."**

If we keep that single purpose in mind, I think D3 will become one of the strongest diagrams in your interview prep package.