---
categories:
  - "[[Clippings]]"
title: SPG Interview prep 5 Session 3 - Insurance Domain 101 underwriting deep dive
source: https://chatgpt.com/g/g-p-6a5517dc2a148191b5c289c2f4d2ce72/c/6a6b4867-a174-83ea-8e69-f7608b9878cc
author:
published:
created: 2026-08-05
description: SPG Interview prep 5 Session 3 - Insurance Domain 101 underwriting deep dive
tags:
  - chatgpt/conversation
---
Perfect. This session is probably the **most valuable** for your interview because it explains what the business users inside Surefyre are actually trying to accomplish.

---

# Insurance Domain 101 — Session 3

# Underwriting Deep Dive

## Purpose

Understand how underwriters think.

You're **not interviewing to become an underwriter**, but if you understand their decision-making process, you'll understand why Surefyre has:

- workflows
    
- approvals
    
- referrals
    
- queues
    
- validations
    
- integrations
    
- notifications
    

Everything exists to support underwriting.

---

# What Is Underwriting?

At its simplest:

> **Underwriting is the process of deciding whether an insurance company should accept a risk, and if so, under what terms and at what price.**

Notice there are **three** decisions:

1. Should we insure them?
    
2. Under what conditions?
    
3. How much should we charge?
    

---

# What Does an Underwriter Actually Do?

Think of an underwriter as a **risk evaluator**, not a salesperson.

Typical day:

Receive submission

↓

Review application

↓

Review documents

↓

Evaluate risk

↓

Request more information

↓

Check guidelines

↓

Determine eligibility

↓

Obtain rating

↓

Quote / Refer / Decline

---

# The Five Questions Every Underwriter Asks

## 1. What is the applicant asking us to insure?

Examples:

- restaurant
    
- trucking company
    
- software company
    
- hospital
    
- contractor
    
- apartment building
    

Different businesses have different risks.

---

## 2. What could go wrong?

Insurance calls this

**Exposure**

Examples

Restaurant

↓

Kitchen fire

↓

Customer injury

↓

Liquor liability

↓

Food poisoning

Software company

↓

Cyber attack

↓

Privacy breach

↓

Business interruption

Construction company

↓

Worker injury

↓

Property damage

↓

Equipment theft

Exposure means

"What losses are possible?"

---

# Risk vs Exposure

People often use these interchangeably.

They're related but different.

## Exposure

The possibility that something bad could happen.

Example

A trucking company has

exposure

to vehicle accidents.

---

## Risk

The likelihood and financial impact.

Example

Ten trucks

↓

Very experienced drivers

↓

Good safety history

↓

Modern fleet

Lower Risk

versus

Ten trucks

↓

Many accidents

↓

Poor maintenance

↓

Inexperienced drivers

Higher Risk

Exposure may be the same.

Risk is different.

---

# 3. Does this fit our appetite?

This is a huge insurance term.

## Carrier Appetite

Every insurance company wants certain business.

And doesn't want other business.

Example

Carrier A loves

Restaurants

Retail

Small offices

Carrier B specializes in

Hospitals

Medical groups

Carrier C specializes in

Cyber insurance

Technology companies

Energy companies

Carrier D specializes in

Construction

Heavy equipment

Manufacturing

Same business.

Different appetites.

---

# Appetite Example

Restaurant

One location

Good safety history

No claims

Small revenue

Carrier says

Great.

Restaurant

Five locations

Many liquor claims

Poor inspections

Recent fire

Carrier says

Outside appetite.

---

# 4. Is it Eligible?

Eligibility is more objective.

Typical questions

State?

Revenue?

Payroll?

Industry?

Years in business?

Claims history?

Construction type?

Building age?

Occupancy?

Sometimes

one answer

automatically makes the risk ineligible.

That's where Surefyre validation rules come in.

---

# Example Eligibility Rule

If

Business Type

=

Nuclear Power Plant

↓

Automatically ineligible.

Or

Revenue

Maximum Program Limit

↓

Route elsewhere.

Those are configurable business rules.

---

# 5. Do I Have Authority?

Very important.

Even if the underwriter likes the risk...

they may not have authority.

---

# Underwriting Authority

Example

Junior Underwriter

May approve

Premium

Up to

$10,000

Senior Underwriter

Up to

$100,000

Chief Underwriter

Unlimited

Same risk.

Different authority.

---

# Referral

If authority is exceeded

↓

Referral

to

Senior Underwriter

or

Manager

or

Carrier

This explains why Surefyre needs:

approval workflows

queues

notifications

status tracking

---

# Underwriting Outcomes

After evaluating everything, there are several possible outcomes.

## Quote

"We'll insure you."

---

## Quote with Conditions

"We'll insure you if..."

Examples

Higher deductible

Lower limits

Install sprinkler system

Improve security

---

## Refer

Needs additional approval.

---

## Request More Information

Need

financial statements

photos

claims explanation

inspection report

etc.

---

## Decline

No coverage offered.

---

# Why Decline?

Examples

Outside appetite

Too many claims

Fraud concerns

Too hazardous

Incomplete information

No underwriting authority

---

# Loss History

One of the biggest factors.

Example

Restaurant

Five years

No claims

↓

Good

Restaurant

Five years

Four fires

↓

Concern

The underwriter asks

"Is this likely to happen again?"

---

# Premium Isn't Arbitrary

Premium reflects expected risk.

Example

Restaurant A

No claims

↓

Lower premium

Restaurant B

Five claims

↓

Higher premium

Same business.

Different premium.

---

# Deductible Tradeoff

Higher deductible

↓

Customer pays more

↓

Insurance pays less

↓

Lower premium

Lower deductible

↓

Insurance pays more

↓

Higher premium

---

# Limits Tradeoff

Higher limits

↓

Insurance pays more

↓

Higher premium

Lower limits

↓

Lower premium

---

# How Surefyre Supports Underwriting

Notice how every underwriting decision maps to a Surefyre feature.

|Underwriter Activity|Surefyre Feature|
|---|---|
|Review submission|Underwriting Workbench|
|Check completeness|Validation rules|
|Request documents|Workflow + notifications|
|Assign reviewer|Routing rules and queues|
|Refer to senior|Approval workflow|
|Obtain rating|Rating integrations|
|Record rationale|Notes and audit history|
|Issue quote|Quote workflow|
|Bind|Status transition|
|Issue policy|Integration with policy and document systems|

This table is worth remembering because it connects the business process to the product.

---

# Where the Technical Consultant Fits

The Technical Consultant is **not deciding whether to insure the customer**.

Instead, they enable the underwriters by configuring the platform.

Examples include:

- application forms
    
- required fields
    
- conditional questions
    
- eligibility rules
    
- routing logic
    
- referral workflows
    
- authority thresholds
    
- notifications
    
- document templates
    
- integration mappings
    
- API connections
    
- testing
    
- troubleshooting
    
- production support
    

That's why the role is so cross-functional.

---

# Mapping to Your Experience

A strong bridge to your FRBNY background is:

> "Although the business domain is different, I recognize the same pattern of rule-driven decision making. At the Federal Reserve, we evaluated incoming market data, applied business rules, identified exceptions, coordinated with operations, validated downstream data, and supported production workflows. In Surefyre, the rules evaluate insurance submissions rather than market data, but the implementation, testing, and operational support disciplines are very similar."

Notice what you're doing here:

- You're **not claiming underwriting experience**.
    
- You're demonstrating that you understand **rule-driven enterprise systems**, which is exactly what SPG needs.
    

---

# Underwriting Vocabulary Cheat Sheet

|Term|Interview-Friendly Meaning|
|---|---|
|**Exposure**|The possibility that a loss could occur.|
|**Risk**|The likelihood and potential severity of that loss.|
|**Carrier Appetite**|The types of business an insurer wants to write.|
|**Eligibility**|Whether a submission meets the program's rules.|
|**Authority**|The level of decision-making delegated to an underwriter.|
|**Referral**|Routing a submission to someone with greater expertise or authority.|
|**Loss History**|Previous insurance claims used to evaluate future risk.|
|**Premium**|The price paid for insurance coverage.|
|**Deductible**|The amount the insured pays before insurance coverage begins.|
|**Coverage Limit**|The maximum amount the insurer will pay for a covered loss.|

---

# Session 4 Preview — Specialty Insurance Deep Dive

Now that you understand **how underwriters think**, the next logical topic is:

- What makes **specialty insurance** different from standard insurance?
    
- Why MGAs exist
    
- Examples of specialty insurance programs
    
- Why Surefyre is especially valuable in the specialty insurance market
    
- What SPG's enterprise customers are likely implementing
    

This session will tie together the business concepts you've learned with the types of organizations and implementations you'll likely encounter as an SPG Technical Consultant.