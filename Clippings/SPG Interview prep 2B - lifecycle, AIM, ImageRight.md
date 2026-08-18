---
categories:
  - "[[Clippings]]"
title: "SPG Interview prep 2b - Surefyre Session 2B: lifecycle, AIM, ImageRight"
source: https://chatgpt.com/g/g-p-6a5517dc2a148191b5c289c2f4d2ce72/c/6a6b4867-a174-83ea-8e69-f7608b9878cc
author:
published:
created: 2026-08-05
description: Surefyre Functional Consultant Boot Camp 2B
tags:
  - chatgpt/conversation
---
# Plan

|Approximate time|Deliverable|
|---|---|
|1:30–2:10|Boot Camp Session 2A|
|2:10–2:50|Session 2B: lifecycle, AIM, ImageRight|
|2:50–3:30|PlantUML diagram set|
|3:30–4:10|Insurance Domain 101|
|4:10–5:10|Configuration Workshop summary|
|5:10–5:50|MRPrice mappings and interview answers|
|5:50–6:30|Final cheat sheets and study plan|

Yes. This is exactly the right next topic.

One thing I want to do slightly differently than Session 2A.

Session 2A taught the **insurance industry**.

Session 2B should teach the **software architecture** and where **you** fit.

By the end of Session 2B, you should be able to walk into the interview and draw this on a whiteboard in under two minutes.

```
              Retail Agent
                    │
                    ▼
          Surefyre Agent Portal
                    │
          (validation/workflow)
                    │
                    ▼
      Surefyre Underwriting Workbench
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
   AIM Core System          ImageRight
      │                           │
      ▼                           ▼
 Carrier / Policy           Documents /
 Administration             Workflow
```

If you can explain that diagram confidently, you're already ahead of many candidates.

---

# Session 2B — Surefyre System Architecture & Lifecycle

## Learning objectives

By the end of this session you should understand:

✓ Why SPG bought Surefyre
✓ What Agent Portal does
✓ What Underwriting Workbench does
✓ What AIM does
✓ What ImageRight does
✓ Where integrations occur
✓ Where YOU fit

---

# 1. Why SPG bought Surefyre

Let's first think about the business problem.

Imagine SPG before Surefyre.

Retail agent
↓
emails PDF
↓
underwriter opens Outlook
↓
saves attachment
↓
copies information
↓
opens policy system
↓
types information again
↓
emails customer
↓
asks for missing info
↓
receives another email
↓
copies information again
↓
creates quote
↓
emails PDF

Lots of:

- manual work
- duplicate entry
- delays
- mistakes
- lost emails
- poor audit trail
    

---

Surefyre digitizes that entire process.

Instead of

PDF
↓
Email
↓
Manual typing
↓
More email

it becomes

Portal
↓
Workflow
↓
Validation
↓
Integrations
↓
Quote
↓
Bind

---

# 2. Agent Portal

Think of the Agent Portal as

> **the front door into SPG.**

External users log in here.

Who?

- Retail agents
- Agency staff
- Possibly wholesalers
    

NOT usually the insured customer.

---

## What happens here?

Agent selects

"New Restaurant Submission"

1. Portal asks
2. Business Name
3. Address
4. Revenue
5. Payroll
6. Years in business
7. Liquor sales
8. Prior claims
9. Upload loss runs
10. Upload financials
11. Upload application

Everything is validated immediately.

Example

1. Revenue: cannot be blank
2. State: must be valid
3. PDF: must be uploaded
4. Liquor %: cannot exceed 100

No underwriter involved yet.

---

### Agent Portal Inputs

Business information

1. Applicant
2. Locations
3. Employees
4. Revenue
5. Coverage requested
6. Uploaded documents

---

### Agent Portal Outputs

1. Validated submission
2. Missing data messages
3. Submission ID
4. Status
5. Messages
6. Quote
7. Documents

---

# 3. Underwriting Workbench

Once submitted...

the work moves here.

This is where SPG employees work.

Typical users

- Underwriter
- Assistant Underwriter
- Operations
- Manager
    

---

What do they see?

1. New submissions
2. Tasks
3. Queues
4. Documents
5. Prior communication
6. Rating
7. History
8. Referral reasons
9. Think of it as
10. Outlook
11. Work Queue
12. Task List
13. CRM
14. Workflow
15. Business Rules

combined into one screen.

---

## Underwriter decides

1. Accept
2. Decline
3. Need More Info
4. Refer
5. Quote
6. Bind

---

# Example

Agent enters

1. Restaurant
2. Revenue: $4M
3. Liquor sales: 60%

System rule says

> Liquor sales > 40%

↓

1. Senior approval required
2. Automatically moves work to Senior Underwriter Queue - Nobody manually routes it.

That's configuration.

---

# 4. AIM

Now we leave Surefyre.

1. AIM is another Vertafore product.
2. Think of AIM as the operational insurance system.
3. If Surefyre is the front office
4. AIM is the back office.

---

AIM stores things like

1. Programs
2. Policies
3. Accounts
4. Agents
5. Premium
6. Transactions
7. Commissions
8. Billing references
9. Business relationships

etc.

---

Analogy

Amazon website
↓
Order Management System



Surefyre
↓
AIM

---

When a submission becomes real business...

AIM probably becomes the system of record.

---

### What flows into AIM?

1. Applicant 2. Coverage 2. Premium 2. Policy
2. Producer 3. Dates 3. Carrier 3. Transaction
3. Status

---

# 5. ImageRight

ImageRight is easier.

Think

1. SharePoint 2. Document Management
2. Workflow 3. Scanning 3. built specifically for insurance.

Everything gets stored.

1. Applications 2. Loss Runs 2. Emails 2. Photos 2. Signed documents
2. Certificates 3. Correspondence 3. Audit records 3. Generated PDFs

---

Suppose

restaurant uploads

1. loss runs
2. health inspection
3. financial statements

Those don't belong in JSON. **They belong in ImageRight.**

---

# 6. Overall architecture

Think about your FRBNY experience.

MRPrice

↓

REST APIs

↓

AWS

↓

Consumers

Surefyre is similar.

```
Agent
↓
Surefyre Portal
↓
Business Rules
↓
Underwriting Workbench
↓
REST APIs
↓
AIM
↓
ImageRight
↓
Carrier Systems
↓
Rating Services

```

Different industry.

Same architectural thinking.

---

# 7. Where integrations occur

You'll probably work around here.

```
Portal
↓
REST
↓
AIM

```

or

```
Portal
↓
REST
↓
Carrier API

```

or

```
Portal
↓
REST
↓
Document Service

```

or

```
Portal
↓
Python Import
↓
AIM
```

Notice

you're not writing AIM. You're integrating with AIM.

Huge difference.

---

# 8. Where YOU fit

This is the interview gold.

You are NOT the underwriter. NOT the developer. NOT operations. NOT IT.

You sit between all of them.

```
Business
↓
Requirements
↓
YOU
↓
Configuration
↓
Testing
↓
Deployment
↓
Support
```

---

Business says

> We need another question.

You configure it.

Business says

> This should route differently.

You configure it.

Business says

> We need another document.

You configure it.

Business says

> This integration changed.

You coordinate.

Business says

> Customer reports a problem.

You reproduce it.

Business says

> Need new API field.

You work with Engineering.

---

Sound familiar?

That's your entire FRBNY career.

---

# 9. Mapping MRPrice to Surefyre

This is one of the strongest analogies you can make during the interview.

|MRPrice (FRBNY)|Surefyre|
|---|---|
|Business users|Underwriters|
|Trading applications|Agent Portal|
|Market data workflow|Insurance submission workflow|
|JSON payload mapping|JSON form configuration|
|REST APIs|REST integrations|
|Release coordination|Configuration deployments|
|Health checks|Go-live validation|
|Production support|Customer configuration support|
|Runbooks|Configuration documentation|
|Dev/Ops coordination|Product/Engineering/Professional Services coordination|


---

# 10. One question I think they'll ask

I would almost bet on this one:

> "What do you think a Technical Consultant does?"

Here's how I'd answer it:

> "My understanding is that the Technical Consultant bridges the business and the technology. The business defines how a particular insurance program should operate—what information to collect, how risks should be evaluated, where work should be routed, and how systems should integrate. The Technical Consultant translates those requirements into Surefyre configuration by building forms, workflows, business rules, integrations, and supporting documentation. They then test the solution, coordinate with Product and Engineering when deeper technical work is required, support deployments, and help resolve customer issues after go-live. That's very similar to the implementation and release work I've done throughout my career, just in a different business domain."

---

## Next session

I think we've now established the complete business picture.

The next session should move into **Insurance Domain 101**, where we'll learn just enough insurance terminology to be comfortable talking with underwriters and implementation teams without trying to become insurance experts.

After that, we'll switch into the **Configuration Workshop**, where everything becomes very hands-on—JSON, JavaScript, Python, REST, OpenAPI, and Postman. That's where you'll likely feel most at home because it maps directly to your technical background.