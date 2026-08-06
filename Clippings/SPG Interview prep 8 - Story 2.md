---
categories:
  - "[[Clippings]]"
title: SPG Interview prep 8 - Story 2
source: https://chatgpt.com/g/g-p-6a5517dc2a148191b5c289c2f4d2ce72/c/6a6b4867-a174-83ea-8e69-f7608b9878cc
author:
published:
created: 2026-08-05
description: SPG Interview prep 8 - Story 2
tags:
  - chatgpt/conversation
---
Great. Now let's move to **Story 2**.

After reviewing the SPG role, I actually think **Story 2 may be even more important than Story 1.**

Why?

Because SPG is an **implementation consulting** company.

They're not looking for someone that can just build software.

They want someone that can **prevent problems before the customer finds them.**

That is exactly what your Pre-QA story demonstrates.

---

# Story 2 — Improving Quality Through Pre-QA Testing

## Why this story?

This story demonstrates:

- proactive thinking
    
- business analysis
    
- testing
    
- quality
    
- implementation consulting
    
- customer mindset
    
- risk reduction
    

Those are all things a Technical Consultant should be doing.

---

# Situation

On the MRPrice project, we recognized that many issues were not being discovered until the formal QA cycle.

By the time QA found them:

- developers had already moved on
    
- schedules slipped
    
- fixes became more expensive
    
- releases became more stressful
    

We wanted to improve the process.

---

# Challenge

The challenge wasn't simply "test more."

We wanted to catch problems earlier.

That meant validating:

- business rules
    
- workflow behavior
    
- data
    
- deployments
    
- environment readiness
    

before formal QA.

---

# My Role

I helped establish what became our Pre-QA process.

Working with Product Owners, developers, and QA, I:

- reviewed new requirements
    
- challenged ambiguous requirements
    
- identified edge cases
    
- developed structured test scenarios
    
- verified business behavior
    
- validated deployment readiness
    
- confirmed data quality
    
- coordinated with developers before formal QA began
    

The goal wasn't to replace QA.

It was to improve what entered QA.

---

# Example

Suppose a story changed the pricing workflow.

Instead of waiting for QA,

we asked questions like:

- What happens if data is missing?
    
- What happens if the value is zero?
    
- What happens if the workflow skips a step?
    
- What happens if an upstream dependency fails?
    
- What happens in DR?
    
- What happens after deployment?
    

That thinking significantly improved quality.

---

# Result

By finding issues earlier:

- developers received faster feedback
    
- QA became more productive
    
- fewer avoidable defects reached later stages
    
- releases became smoother
    

Most importantly,

the business gained more confidence in the releases.

---

# Why This Matters to SPG

This is exactly how I would approach a Surefyre implementation.

When configuring a customer solution,

I wouldn't simply ask,

"Does the happy path work?"

I'd ask:

- What happens if required information is missing?
    
- What if the user has the wrong role?
    
- What if the API is unavailable?
    
- What if the document upload fails?
    
- What if a referral should occur?
    
- What if a workflow loops?
    
- What if the business changes its rules?
    

That's how implementation consultants think.

---

# Where This Maps to Surefyre

Imagine we're implementing:

Cyber Insurance.

Business says:

"If revenue exceeds $100 million,

route to Senior Underwriter."

I wouldn't only test

Revenue = $200M

I'd also test:

Revenue = exactly $100M

Revenue = $99,999,999

Revenue missing

Revenue negative

Revenue not numeric

Wrong user role

Workflow restarted

Integration unavailable

Those are implementation consultant test cases.

---

# 30-Second Version

> One improvement I helped introduce on the Federal Reserve project was a Pre-QA process. Instead of waiting for formal QA to discover issues, we validated business rules, workflows, deployment readiness, and data quality earlier in the lifecycle. That improved release quality and reduced rework. I would bring that same preventive mindset to customer implementations at SPG.

---

# 90-Second Version

Use the complete story.

---

# Interview Question

**"Tell me about a time you improved a process."**

Excellent answer.

---

# Interview Question

**"How do you approach testing?"**

Excellent answer.

---

# Interview Question

**"How do you reduce implementation risk?"**

Excellent answer.

---

# Hidden Skill You're Demonstrating

Most candidates say

"I write test cases."

This story demonstrates something much bigger.

It shows:

**systems thinking.**

You're thinking about:

- business
    
- workflow
    
- data
    
- deployment
    
- operations
    
- support
    

instead of just individual screens.

---

# Strong Closing

I like ending with this sentence:

> "One lesson I've learned over the years is that it's much less expensive to ask the right questions before deployment than to answer difficult questions after production."

That sounds exactly like someone a Professional Services organization wants on customer implementations.

---

## One improvement to our overall interview strategy

After writing the first two stories, I see a pattern that I think we should use throughout the interview.

Rather than positioning yourself primarily as a **Business Analyst**, position yourself as an **Enterprise Implementation Consultant**.

That phrase naturally includes:

- business analysis
    
- requirements
    
- configuration
    
- testing
    
- integrations
    
- release readiness
    
- troubleshooting
    
- customer communication
    
- production support
    

It also aligns closely with how SPG describes the Technical Consultant role.

I think that's a stronger and more natural positioning than simply saying, "I'm a Business Analyst," because it better reflects both your experience and the work SPG is asking you to do.