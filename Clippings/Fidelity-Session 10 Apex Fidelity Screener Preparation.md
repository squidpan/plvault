---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 10 Apex Fidelity Screener Preparation
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

# Fidelity — Session 10: Apex/Fidelity Screener Preparation

Now we switch from **learning** to **performing**.

The objective is not to sound like you've memorized Fidelity's architecture. The screener needs to conclude:

> **This is an experienced, technically strong financial-services BA who can understand a complex trading/data problem quickly, work independently across systems and teams, and communicate clearly.**

The JD supports that emphasis: trading experience is preferred rather than required, while technical aptitude, regulatory awareness, lineage/mapping, complex dependencies, and technical-to-business translation are central to the trading-focused BA allocation.

## Session 10 plan

We'll prepare these in the order you're likely to encounter them:

|Part|Screener topic|Goal|
|---|---|---|
|**10.1**|Tell me about yourself|60–90 sec opening|
|**10.2**|Why this role / why Fidelity?|Connect your background to Rep Code|
|**10.3**|What do you understand about Rep Code Expansion?|Demonstrate preparation without pretending insider knowledge|
|**10.4**|Technical / systems questions|Lineage, APIs, SQL, dependencies, SOR|
|**10.5**|Trading-domain questions|Demonstrate sufficient working vocabulary|
|**10.6**|Behavioral / discovery|How you actually operate as a BA|
|**10.7**|Weakness/gap questions|Trading, SQL, regulatory without self-disqualifying|
|**10.8**|Recruiter logistics|Contract, rate, hybrid, availability|
|**10.9**|Questions you ask them|Strong closing|
|**10.10**|Mock screener|Rapid spoken practice|

We should be able to build the core material in about **30–45 minutes**.

---

# 10.1 — “Tell me about yourself”

This is probably the most important answer.

I would **not** start by walking chronologically through your entire career.

Use:

**Who you are now → most relevant Fed work → earlier Fidelity connection → why that leads naturally to this role.**

### Version I recommend

> I'm a Senior Business Analyst with a financial-services background, and most of my career has been at the intersection of business, data and technology.
> 
> Most recently, I worked at the Federal Reserve Bank of New York supporting a streaming fixed-income market-data application and its modernization from an Oracle-based environment toward AWS and REST APIs. My work included requirements analysis, data mapping from relational schemas to JSON payloads, JIRA user stories and acceptance criteria, QA and UAT, release coordination, and working closely with developers and infrastructure teams across Linux, Oracle, OpenShift and AWS.
> 
> Earlier in my career, I also worked at Fidelity through Capgemini, supporting fixed-income feeds and reference, pricing and security-master data used by downstream trading and other financial platforms.
> 
> What interested me about this opportunity is that Rep Code Expansion appears to require exactly that combination of business analysis, data lineage, systems analysis and working through dependencies across multiple platforms.

That answer is well supported by your resume.

### What I like about this opening

Within about a minute, you've already planted:

**Senior BA**

**financial services**

**fixed income**

**market data**

**Fidelity**

**Oracle**

**AWS**

**REST**

**data mapping**

**requirements**

**UAT**

**complex systems**

And you haven't claimed direct brokerage trading experience.

---

# 10.2 — “Why are you interested in this role?”

Don't answer:

> “Because I need a job.”

Even though compensation and getting back to work obviously matter, that's not useful to the screener.

Instead:

> I'm interested because the problem is very close to the kind of work I've done successfully. It isn't just a requirements-writing role. It requires understanding data, systems and interfaces, tracing dependencies and working with engineering and business stakeholders.
> 
> The Rep Code Expansion problem is particularly interesting because changing an identifier from three to four characters sounds simple initially, but once that identifier flows through trading, clearing, supervisory and operational systems, it becomes an end-to-end data and systems problem. That's the kind of analysis I enjoy doing.

The description itself says Rep Code Expansion affects core data models, supervisory workflows, trading, clearing and operational integrations while requiring legacy compatibility through centralized translation.

And then you have an optional final sentence:

> I also worked at Fidelity earlier in my career, so returning there in a different capacity is appealing to me.

Good. Short. Don't overplay it.

---

# 10.3 — “What do you understand about Rep Code Expansion?”

This is where all those domain sessions start paying off.

I'd use approximately **45 seconds**:

> My understanding from the project description is that the existing three-character Rep Code namespace has become constrained as Fidelity's business and advisor structures have grown more complex. The target state expands that identifier to four characters.
> 
> The real challenge isn't simply increasing the field length. You have multiple systems and interfaces with different capabilities and release cycles, so the new four-character representation has to coexist with legacy three-character processing. That creates questions around the authoritative source, data lineage, validation, translation, downstream compatibility and exception handling.
> 
> I'd approach it by mapping the current end-to-end Rep Code flow, identifying every system and interface that consumes or transforms it, and then performing the gap analysis against the four-character target state.

The first paragraph is directly grounded in the JD; the second and third are **our BA analysis of the implications**, not confirmed Fidelity implementation detail.

That distinction is important.

---

# 10.4 — Likely technical questions

These should now feel much easier.

### “What is data lineage?”

> Data lineage is the traceable journey of a data element from its authoritative source through downstream systems, including any transformations along the way. I think about it in both directions: backward lineage tells me where the value came from, while forward lineage tells me where it goes and what depends on it.

### “What is a system of record?”

> The system of record is the authoritative source for a particular business record or data element. A downstream system may contain a copy or transformed representation of that value without being its authoritative source.

### “How would you investigate a Rep Code discrepancy?”

This is where today's SQL lab helps your thinking:

> First I'd identify the value we're seeing and where it was observed. Then I'd trace backward toward the authoritative source and compare the value at each interface or transformation point. If translation is involved, I'd compare the actual downstream value with the expected mapping and determine where they diverged. Depending on the systems involved, I'd use SQL, logs, API payloads or other application data to support that analysis.

Excellent answer for this role.

### “How strong is your SQL?”

> I use SQL primarily as a BA analysis and troubleshooting tool. I'm comfortable with filtering, joins, aggregations, CTEs and basic subqueries, and I use those techniques to validate data, reconcile mappings and investigate discrepancies. My professional database experience has primarily been with Oracle. I'm not positioning myself as a database developer.

Keep that boundary.

---

# 10.5 — Trading-domain rapid review

If they probe the domain, you don't need to give lectures.

**Order**

> A client's instruction to buy or sell a security.

**Execution**

> Fulfillment of some or all of that order in the market.

**Trade**

> The resulting transaction created by an execution.

**OMS**

> Receives and manages orders and routes them toward execution.

**Clearing**

> Determines the obligations created by the trade—essentially who owes what.

**Settlement**

> Completion of those obligations through delivery of securities and payment.

**Rep Code**

For our interview model:

> An identifier representing the registered representative, advisory team or other business relationship associated with an account or transaction. I would verify Fidelity's exact business definition during discovery rather than assuming one universal meaning.

That last qualification matters because the supplied JD does **not** define the exact Fidelity Rep Code data model.

---

# 10.6 — “How do you approach discovery when you don't know the system?”

This is likely because the JD explicitly values independent discovery/networking.

> I start by getting the high-level business flow and identifying the major systems, data and actors involved. I usually draw that out because it quickly exposes what I know and what I don't know.
> 
> Then I identify the SMEs or system owners for each part of the flow and drill into the interfaces, data transformations, business rules and dependencies. I document what I learn as I go and use that model to identify gaps and conflicting assumptions.
> 
> I don't expect one person to know the entire end-to-end process, so part of the BA role is connecting information across teams until the complete picture emerges.

That is **very you**, and it matches exactly how we've been building the linked Pre/Post Trade diagrams.

---

# 10.7 — Handling your three potential gaps

### “You haven't been a trading BA?”

Don't get defensive.

> That's correct. My direct background is stronger in financial and market-data systems than in owning brokerage order-management workflows. But I've worked with fixed-income data and systems supporting downstream trading environments, and the systems-analysis aspects of this role—data lineage, mapping, APIs, dependencies and technical discovery—are areas where I have substantial experience. I've also been refreshing the brokerage trading lifecycle so I can apply that experience in the right domain context.

### “Are you a regulatory SME?”

> No, I wouldn't position myself as a regulatory SME. My experience is working as a BA in highly controlled financial environments and partnering with the appropriate regulatory or business SMEs to understand the requirement and translate it into system, data and testing impacts.

### “How strong is your SQL?”

Use the answer from 10.4.

Notice the pattern:

**acknowledge boundary → establish adjacent strength → explain transferability.**

Never:

> “I don't really know trading.”

or:

> “My SQL isn't very strong.”

Those throw away everything surrounding the gap.

---

# 10.8 — Recruiter logistics

For the Apex screener, these may be as important as technical questions.

Based on the opportunity details you've been working from, you're already comfortable with the **$50/hr W2**, **12–18 month contract**, and **Jersey City alternating-week hybrid arrangement**.

If asked about rate:

> Yes, the $50 an hour W2 rate we discussed works for me.

Hybrid:

> Yes, I'm comfortable with the Jersey City hybrid schedule as it was described to me.

Contract:

> Yes. I understand this is a long-term contract opportunity, and I'm comfortable with that arrangement.

Availability:

Give them your actual availability at the time. No need to complicate it.

---

# 10.9 — Questions YOU should ask

Don't unload ten questions. Pick **2–3** depending on what the recruiter already answered.

My preferred ones:

1. **“For the trading-focused BA specifically, which systems or parts of the trading lifecycle would this person be working with most closely?”**
    
2. **“How far along is Rep Code Expansion today—is the trading team primarily in discovery and current-state analysis, or have requirements and implementation already started?”**
    
3. **“What would Fidelity consider the most important thing for this BA to accomplish in the first 60 to 90 days?”**
    

If the screener is purely Apex and Carolyn doesn't know the technical details, that's fine.

Her answer might simply be:

> “That's a good question for the Fidelity manager.”

That's actually useful—you've just identified something to ask Fidelity.

---

## Your five things to remember if everything else disappears

If you're nervous and remember nothing else, remember these:

**1. I'm a technical financial-services BA, not a documentation-only BA.**

**2. MRPrice = fixed-income market data + Oracle → AWS/REST modernization.**

**3. Data lineage = source → transformations → downstream consumers.**

**4. Rep Code Expansion = not merely 3→4 characters; it's an end-to-end systems/dependency/legacy-compatibility problem.**

**5. I don't need to know everything initially; my BA strength is discovering the end-to-end picture across SMEs and systems.**

That's the core of your candidacy.

### Next step

We shouldn't add much more material before testing whether you can **say it naturally**.

So **Session 10.10 should be the mock Apex screener**. I'll play the recruiter, ask one question at a time, and **I won't help you before you answer**. After each response, I'll give you a quick rating, identify anything problematic, tighten it, and immediately ask the next question.

That will tell us much more than writing another cheat sheet.

