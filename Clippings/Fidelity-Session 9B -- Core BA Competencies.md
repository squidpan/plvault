---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 9B -- Core BA Competencies
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-23
description:
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---
---

# Fidelity — Session 9B: Core BA Competencies

Now we're mapping the **broader core skills across Fidelity's BA population**, not just the seven trading-focused bullets.

The actual JD lists these core areas: strong data analysis/data fluency, data lineage/mapping, systems of record/system changes, translating findings into requirements, data flows/APIs/business logic, engineering partnership, strong SQL, current-state/gap analysis, and communication/requirements documentation.

Several overlap with Session 9A, so I'm going to concentrate on what adds something new.

## 9B-1 — Strong SQL capability

This one needs careful positioning.

Your submitted resume lists **Oracle** and describes Oracle-based data-distribution models, relational-schema mapping, log/data analysis, and validation work, but it does **not explicitly claim SQL** in the skills section or Fed bullets.

So I would say:

> I use SQL primarily as a Business Analyst and systems-analysis tool rather than as a database developer. I'm comfortable querying relational data, filtering and joining datasets, using aggregations, and using the results to validate mappings or investigate data discrepancies. My database experience at the Fed was primarily with Oracle, where I worked with relational pricing data and downstream data-distribution models.

If they probe technically, you now have the refresher fresh in your head:

`SELECT / WHERE / ORDER BY`  
`INNER JOIN / LEFT JOIN`  
`GROUP BY / HAVING`  
`COUNT / SUM / AVG`  
`NULL`  
`CASE`  
CTEs  
subqueries

### Rating: **3.5–4/5**

I would **not say "strong SQL developer."**

I'd say:

> **Practical SQL for BA analysis, validation and troubleshooting.**

---

# 9B-2 — Experience with data flows, APIs and business logic

This is **5/5 territory**.

Your resume specifically says you mapped the legacy relational pricing schema to REST API JSON payloads and helped validate the transition from legacy Oracle-based processing to API/JSON during cloud migration.

### Interview answer

> A good example is the MRPrice modernization at the Fed. The legacy application used Oracle-based data structures and distribution mechanisms, while the modernized architecture exposed pricing data through REST APIs in AWS. I worked on mapping the existing relational pricing fields to the JSON payload and validating that the data delivered through the API maintained the same business meaning expected by downstream consumers.
> 
> When I analyze an API, I'm interested not only in the endpoint itself but in where the data originates, what business rules or transformations are applied, what the payload contains, and what the downstream system does with it.

### Rep Code bridge

That's directly transferable:

**Rep Code source**

→ business rules / validation

→ API/interface

→ possible translation

→ downstream application

→ trading/clearing/operations

Fidelity explicitly describes Rep Code Expansion as spanning data models and integrations across trading, clearing and operational platforms.

### Rating: **5/5**

---

# 9B-3 — Understanding systems of record and system changes

We've discussed SOR conceptually, but let's turn it into an interview answer.

> I think of the system of record as the authoritative source for a particular piece of business data. When analyzing a change, I first want to establish where the value originates and which system owns it, rather than assuming that a downstream copy is authoritative.
> 
> From there, I trace how the value moves through downstream systems, where it may be transformed, and which systems depend on it. That becomes especially important when you're changing something like an identifier because simply changing the source doesn't mean every downstream system can consume the new representation.

### Fidelity example

Suppose:

**Authoritative Rep Code**

`ABC1`

↓

System B stores `ABC1`

↓

Interface C translates

`ABC1 → XYZ`

↓

Legacy trading system stores `XYZ`

`XYZ` isn't necessarily the authoritative Rep Code.

It's a **downstream representation of the authoritative identifier**.

That's exactly why lineage matters.

### Rating: **5/5 conceptually / strong transferable experience**

---

# 9B-4 — Analyze current state and identify gaps

This is another excellent MRPrice modernization parallel.

Your resume describes modernization from Oracle-based data distribution toward REST APIs/AWS.

### Interview answer

> In a modernization project, I start by understanding the current state—applications, data, interfaces, workflows and dependencies—and then compare that with the target-state capability.
> 
> At the Fed, the MRPrice modernization involved moving from legacy Oracle-based processing and distribution toward an AWS and REST API architecture. Part of my role was understanding how the existing data was represented and consumed and then helping validate how those requirements were satisfied in the new architecture.
> 
> The gap analysis is essentially identifying what works in the current state, what the target state requires, and what needs to change in between.

### Apply that to Fidelity

**AS-IS**

3-character Rep Code

↓

Inventory systems/interfaces

↓

**TO-BE**

4-character Rep Code + legacy compatibility

↓

**GAP**

For every system ask:

- Can it store 4?
    
- Validate 4?
    
- Display 4?
    
- Transmit 4?
    
- Receive 4?
    
- Does it truncate?
    
- Does it require translation?
    
- What happens to historical data?
    
- What happens when mapping fails?
    

That is exactly how I'd approach this project.

### Rating: **5/5**

---

# 9B-5 — Partner closely with engineering and technical teams

Your resume strongly supports this through the Fed modernization, testing, operational support, release coordination and technical environment.

### Interview answer

> I've always worked closely with engineering and technical teams. At the Fed that included developers, infrastructure, architecture and operations teams across Linux, Oracle, OpenShift and AWS.
> 
> My role was often to bridge the groups: understand the business requirement, work through the technical implementation and dependencies with engineering, help clarify requirements or acceptance criteria, and then coordinate validation through QA/UAT and production readiness.

### Rating: **5/5**

---

# 9B-6 — Translate findings into business and functional requirements

This is central to your resume. It explicitly says you developed actionable JIRA user stories with acceptance criteria from high-level Epics and prioritized functional/non-functional requirements from business, infrastructure and architecture into releases.

### Interview answer

> Once I've completed discovery and understand the current-state behavior and technical constraints, I translate that into requirements the team can implement and test. In Agile environments I've done that through JIRA user stories with acceptance criteria, along with supporting process flows, data mappings and technical dependencies.
> 
> I try to make the acceptance criteria measurable enough that development understands what needs to be built and QA and the business can determine whether the requirement has actually been satisfied.

This is where your Farm Credit exercise also gives you additional **practice**, but I would keep professional experience and interview-prep exercises separate.

### Rating: **5/5**

---

# 9B-7 — Strong communication and requirements documentation

Again, very strong.

Your resume documents JIRA stories/acceptance criteria, operational runbooks, troubleshooting procedures, deployment documentation, support knowledge bases, testing and cross-functional stakeholder work.

### Interview answer

> Documentation has been a major part of my BA work. Depending on the audience and purpose, I've produced requirements, JIRA user stories and acceptance criteria, process and data-flow diagrams, test plans, operational runbooks, troubleshooting procedures and release documentation.
> 
> I try to make documentation useful to the person consuming it rather than documenting for its own sake. A developer needs enough precision to implement the requirement, a tester needs measurable acceptance criteria, and a business stakeholder needs to understand the process and business impact.

### Rating: **5/5**

---

# 9B-8 — Strong data analysis and data fluency

This ties several pieces together.

Your Fed resume describes Oracle data-distribution models, relational pricing schemas, JSON payload mapping, log analysis using shell scripting and Excel Power Query/Pivot, and validation of legacy Oracle data against API JSON payloads. Your earlier Fidelity work included reference data, pricing, time-series, security-master and golden-copy data management.

### Interview answer

> Data has been central to much of my work. At the Fed I worked with fixed-income pricing data in Oracle, analyzed logs and data anomalies, mapped relational fields to API payloads and validated data between legacy and modernized implementations. Earlier at Fidelity I worked with reference, pricing, time-series and security-master data.
> 
> As a BA, I want to understand not just the field name but what the data represents, where it comes from, how it changes, what business rules apply to it and which downstream processes depend on it.

### Rating: **5/5**

---

## Session 9B summary

|Fidelity core competency|Fit|Primary evidence|
|---|--:|---|
|**Strong SQL**|**3.5–4/5**|Practical relational-data analysis; Oracle experience + refreshed hands-on SQL|
|**Data flows / APIs / business logic**|**5/5**|Oracle → REST/JSON → AWS modernization|
|**Systems of record / system changes**|**5/5 transferable**|Data ownership, downstream distribution, lineage/mapping|
|**Current-state / gap analysis**|**5/5**|Legacy Oracle AS-IS → AWS/API TO-BE|
|**Engineering partnership**|**5/5**|Dev, infrastructure, architecture, operations, QA/UAT|
|**Translate findings → requirements**|**5/5**|Epics → JIRA stories + AC; functional/non-functional requirements|
|**Communication / documentation**|**5/5**|Requirements, AC, diagrams, testing, runbooks, troubleshooting/release docs|
|**Data analysis / fluency**|**5/5**|Pricing/reference/security-master data, Oracle, JSON, logs, Power Query/Pivot|

The pattern across both **9A and 9B** is becoming pretty clear: **the main domain gap is direct brokerage order/trade workflow experience. The systems/data/technical BA requirements are overwhelmingly aligned with your background.** The JD itself makes that less concerning because financial-services/trading experience is preferred rather than mandatory.

### Next: Session 9C

Now we should consolidate 9A + 9B into the **one-page Fidelity JD → Your Evidence → Interview Answer cheat sheet**. That's the artifact you'll actually review before the screener rather than rereading all of Session 9.

---

