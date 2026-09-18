---
categories:
  - "[[Clippings]]"
title: SPG Interview prep 6 Session 1 - Configuration Workshop
source: https://chatgpt.com/g/g-p-6a5517dc2a148191b5c289c2f4d2ce72/c/6a6b4867-a174-83ea-8e69-f7608b9878cc
author:
published:
created: 2026-08-05
description: SPG Interview prep 6 Session 1 - Configuration Workshop
tags:
  - chatgpt/conversation
---
This is where I think your interview preparation will really separate you from other candidates.

Up to now we've learned **what** the insurance business does.

Now we're going to learn **what you would actually configure**.

One important point before we start:

> We **do not know SPG's proprietary implementation** of Surefyre. Everything below is an implementation model based on the job description, publicly available information about configurable insurance platforms, and standard insurance implementation practices. During the interview, present it as **"this is how I would expect a configurable insurance platform to work,"** not **"this is exactly how Surefyre works."**

---

# Configuration Workshop — Session 1

# Configuring a New Insurance Program

## Scenario

The Product Manager tells us:

> "We're launching a new Cyber Liability insurance product."

Your job is **not** to write software.

Your job is to configure Surefyre so that the product can be sold.

---

# Step 1 — Discovery

Before opening Surefyre, meet with the business.

Questions:

- Who will sell this?
    
- Who will underwrite it?
    
- Which carrier is backing it?
    
- Which states are supported?
    
- Who approves exceptions?
    
- What documents are required?
    
- What integrations are needed?
    
- What makes someone ineligible?
    

**Deliverables**

- Requirements
    
- Business rules
    
- Workflow
    
- User roles
    

This should sound very familiar to you from your BA work.

---

# Step 2 — Configure the Application Form

The business wants these sections.

## Applicant Information

Fields

- Business Name
    
- FEIN
    
- Address
    
- Website
    
- Years in Business
    

---

## Business Information

Fields

- Annual Revenue
    
- Number of Employees
    
- Industry
    
- NAICS Code
    

---

## Cyber Security

Fields

- MFA Enabled?
    
- Endpoint Protection?
    
- Encryption?
    
- Cloud Provider?
    
- Prior Breach?
    

---

## Documents

Uploads

- Security Questionnaire
    
- Financial Statements
    
- Existing Policy
    
- Loss Runs
    

Notice:

This is mostly **configuration**.

---

# Step 3 — Required Fields

Now the business says:

Business Name

Required

Revenue

Required

MFA Question

Required only if

Cyber Coverage selected

You configure rules like:

```text
Coverage = Cyber

↓

Show Cyber Questions

Otherwise

Hide Cyber Questions
```

This is one of the most common configuration tasks.

---

# Step 4 — Conditional Logic

Example

Question

Have you experienced a cyber breach?

If

No

↓

Continue

If

Yes

↓

Display

- Number of incidents
    
- Date
    
- Cost
    
- Root cause
    

The form changes dynamically.

That is exactly why JavaScript knowledge appears in the job description.

Not to build React applications.

To support behavior like this.

---

# Step 5 — Validation Rules

Business says

Revenue

must be

greater than zero

State

must be supported

Effective Date

cannot be in the past

Email

must be valid

Files

must be PDF

Maximum upload

20 MB

These become validation rules.

---

# Step 6 — Routing Rules

Now the submission is complete.

Business says

Revenue

Under

$5M

↓

Small Business Team

Revenue

$5M–50M

↓

Commercial Team

Revenue

Over

$50M

↓

Senior Underwriter

That's workflow configuration.

No code.

---

# Step 7 — Referral Rules

Business says

If

Prior Breach

=

Yes

↓

Senior Underwriter

If

Revenue

$100M

↓

Manager Approval

If

High Risk Industry

↓

Cyber Specialist

Those are configurable routing rules.

---

# Step 8 — User Roles

Different users see different screens.

Retail Agent

- submit
    
- upload
    
- view status
    

Underwriter

- review
    
- request documents
    
- quote
    

Manager

- approve
    
- override
    

Administrator

- configure
    

Typical implementation work includes:

- permissions
    
- menus
    
- visible fields
    
- editable fields
    

---

# Step 9 — Notifications

Examples

Submission received

↓

Email Agent

Referral

↓

Notify Senior Underwriter

Quote Ready

↓

Notify Agent

Bound

↓

Notify Operations

Again:

Configuration.

---

# Step 10 — Documents

Business wants

Quote PDF

Binder

Policy

Welcome Letter

Certificate

Template selection

↓

Field merge

↓

Generate PDF

↓

Store in ImageRight

---

# Step 11 — API Configuration

Business says

After Quote

↓

Call Rating API

Receive

Premium

Display Premium

Technical Consultant activities

- endpoint URL
    
- authentication
    
- request mapping
    
- response mapping
    
- timeout values
    
- error handling
    

Developers may build the API client if custom code is required, but the consultant often configures how the platform uses it.

---

# Step 12 — Testing

Now everything must be tested.

Examples

Positive

Revenue

100000

Valid

Pass

Negative

Revenue

blank

Expected

Validation Error

Boundary

Revenue

5000000

Expected

Correct Queue

Integration

Rating API

Expected

Premium Returned

Regression

Existing Product

Still Works

This is where your QA/UAT background is directly applicable.

---

# Step 13 — Production

Before Go-Live

Verify

- configuration
    
- users
    
- permissions
    
- endpoints
    
- integrations
    
- templates
    
- notifications
    
- migrations
    

Again, this mirrors your release readiness work at FRBNY.

---

# What Technologies Are Actually Being Used?

|Technology|Likely Use in This Scenario|
|---|---|
|HTML|Form layout and presentation|
|CSS|Styling (usually limited customization)|
|JavaScript|Dynamic fields, validation, client-side behavior|
|JSON|Configuration and API payloads|
|REST APIs|Rating, policy, document, and third-party integrations|
|SOAP|Legacy carrier integrations (where applicable)|
|Postman|API testing and troubleshooting|
|Python|Data migration, import/export utilities, validation scripts|
|SQL|Data verification and troubleshooting (if applicable)|

Notice something important.

You're not being asked to become a full-stack developer.

You're being asked to understand enough of each technology to configure, test, validate, and troubleshoot enterprise implementations.

---

# How This Maps to Your Experience

This is one of the strongest connections you can make in the interview.

|SPG Responsibility|Your Experience|
|---|---|
|Gather requirements|✔ Extensive BA experience|
|Design workflows|✔ Business process analysis|
|Configure rules (conceptually)|✔ Requirements, acceptance criteria, release planning|
|Test functionality|✔ QA, UAT, regression testing|
|Validate integrations|✔ REST, JSON, Postman, API testing|
|Support deployments|✔ Release coordination, production readiness|
|Troubleshoot issues|✔ FRBNY production support|
|Work across teams|✔ Business, Development, QA, Operations, Infrastructure|

The one major difference is:

**You'll learn Surefyre's configuration screens and product conventions instead of a custom financial platform.**

---

# Interview Scenario

Suppose they ask:

> "A customer says a Cyber Liability submission isn't reaching the Senior Underwriter even though revenue exceeds $100 million. How would you approach it?"

A strong answer would be:

> "I'd first reproduce the issue in a test environment. Then I'd verify the submission data to confirm the revenue value and any other routing criteria. Next I'd review the workflow or routing configuration to see whether the threshold or conditions are configured correctly. I'd also check whether the user's role, queue assignments, or a recent configuration change affected the routing. If the workflow appears correct, I'd inspect any related integration or application logs and work with Engineering if I suspected a product defect. Once resolved, I'd regression test similar routing scenarios to ensure the fix didn't affect other programs."

That answer demonstrates a structured troubleshooting approach without pretending you've already configured Surefyre.

---

## Configuration Workshop — Session 2 Preview

Next we'll move from **configuration concepts** to the actual technologies in the SPG job description:

- JavaScript for configurable forms
    
- JSON configuration
    
- REST payloads
    
- Swagger/OpenAPI
    
- Postman collections and environments
    
- Python automation for implementation work
    

This is where we'll connect the configuration tasks you've just learned to the technical skills the interviewers are likely to ask about.