---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 11a - wrap up
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-29
description:
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---
---

Good. Let's consolidate it now. I want you to understand this as **one business story**, not as 20 disconnected concepts.

I'll distinguish what the **JD actually tells us** from the implementation details we've been using as **hypothetical examples**.

# Fidelity Rep Code Expansion — the whole story

## 1. Start with the business, not technology

Fidelity has something called a **Rep Code**.

The important thing is that Rep Code isn't merely a database identifier. According to the JD, clients use Rep Codes for multiple purposes, including identifying:

- individual advisors
- teams
- compensation structures
- order-handling roles

So our mental model is:

**Rep Code = an identifier carrying some form of representative/business attribution.**

It may answer questions such as:

> Which advisor/team/role is associated with this account or transaction?

That's why getting the Rep Code wrong can be a **business-data problem**, not merely a malformed-field problem.

---

# 2. Why Fidelity has a problem

The existing Rep Code structure is **three characters**.

Think:

`ABC`, `DEF`  ,  `XYZ`

That worked historically.

But Fidelity says the three-character construct is becoming inadequate because of:

**client growth + evolving advisor structures + M&A + more complex distribution models + codes rarely being retired.**

They've even tried special characters as a short-term mitigation, but the JD says that produced poor UX, limited adoption and incompatibility with downstream vendors.

So eventually you hit:

> **We need a larger identifier space.**

Hence:

**3 characters → support 4 characters**

For example:

`ABC` versus `ABC1`

But that's only the visible part of the project.

---

# 3. Why changing `CHAR(3)` to `CHAR(4)` doesn't solve it

Rep Code doesn't live in one database table. It moves through an ecosystem.

Conceptually:

**Rep Code authoritative data**
↓
**Account**
↓
**Order Management**
↓
**Order**
↓
**Execution / Trade**
↓
**Trade processing**
↓
**Clearing**
↓
**Reporting / supervisory / operational consumers**

The JD explicitly says the initiative spans **core data models, supervisory workflows, trading, clearing and operational integrations**.

Therefore, changing the source system doesn't automatically make the enterprise four-character capable.

Somewhere there might be:

`VARCHAR(3)` or: `rep_code.length = 3`

or an API schema:

`maxLength: 3` or a fixed-width file: 

`REP_CODE PIC X(3)`

or a vendor application that simply cannot accept:

`ABC1`

That's the real modernization problem.

---

# 4. First thing the BA establishes: AS-IS

This is what you were doing in Session 7.

Before asking what needs changing, understand what Rep Code does **today**.

Our hypothetical OMS example gave us:

**Account**

`Rep Code = ABC`
↓
OMS creates order
↓
**Order defaults to `ABC`**
↓
authorized user may override
↓
**Order Rep Code = DEF**
↓

trade processing uses effective order Rep Code

And we discovered that a mismatch:

`Account = ABC`

`Order = DEF`

isn't necessarily an error.

It could be a legitimate business rule.

That means the BA needs to understand:

**source → defaulting → validation → override → precedence → downstream usage → reporting/audit**

before writing requirements.

---

# 5. Find the authoritative source

Next comes the **System of Record / authoritative source** question.

You asked this yourself:

> Is there a Rep Code Master that acts as the authoritative source?

Excellent BA question.

We don't know Fidelity's actual implementation from the JD.

But conceptually there must be some authoritative mechanism for determining what Rep Codes mean and whether they're valid.

Because otherwise OMS can't reliably answer:

> Is `ABC1` a legitimate Rep Code?

And importantly:

**Exists ≠ Valid.**

There may be other rules:

`exists?`

↓

`active?`

↓

`effective today?`

↓

`allowed for this business context?`

↓

**VALID**

Those rules have to survive the expansion.

---

# 6. Then comes migration strategy

This was your question this morning:

> What happens to existing three-character Rep Codes?

That's fundamental.

The JD **does not tell us the migration strategy**.

So we cannot claim:

> “Every existing advisor gets a new four-character Rep Code.”

Possible, but unknown.

For our exercise we used another plausible model:

Existing:

`ABC`

remains valid.

New codes can be:

`XYZ1`

That creates a **mixed environment**:

`ABC` — valid 3-character

`DEF` — valid 3-character

`ABC1` — valid 4-character

`XYZ1` — valid 4-character

Now the requirement isn't necessarily:

> Rep Code is four characters.

It may instead be:

> **The platform must support valid three- and four-character Rep Codes.**

That distinction is huge.

---

# 7. Now inventory the systems and interfaces

This is where the BA starts building the impact map.

For every system/interface ask:

| Question      | What you're looking for                     |
| ------------- | ------------------------------------------- |
| Receive?      | Can it receive 3 and 4?                     |
| Store?        | Does its data model support 4?              |
| Validate?     | Any hard-coded 3-char rules?                |
| Transmit?     | Can outbound interfaces send 4?             |
| Transform?    | Does it modify Rep Code?                    |
| Business use? | Does logic depend on Rep Code?              |
| Pass-through? | Does it merely transport it?                |
| SOR?          | Where does authoritative meaning originate? |
| History?      | Does it retain historical meaning?          |
| Consumer?     | Who depends on its output?                  |

This is **data lineage + dependency analysis**.

And that's directly aligned with the JD's emphasis on data lineage/mapping, systems of record, data flows/APIs, current-state analysis, gaps and complex dependencies.

---

# 8. Categorize the ecosystem

This is a useful mental simplification.

### A. Systems capable of both 3 and 4

Example:

OMS receives: `ABC` or `ABC1`

Both work. No translation required.

### B. New-world systems

Perhaps they operate using the authoritative four-character representation.

Again, translation may not be required.

### C. Legacy 3-character consumers

Here's our problem.

OMS:

`ABC1`

↓

Trade Processing:

`ABC1`

↓

Legacy Clearing:

**“I only accept three characters.”**

Now what?

---

# 9. Centralized translation

This part **is in the JD**.

Fidelity intends to maintain compatibility with legacy systems through a **centralized translation approach**.

Conceptually:

`ABC1`

↓

**Translation capability**

↓

lookup authoritative mapping

↓

`XYZ`

↓

Legacy Consumer

And remember our important lesson:

### Translation ≠ truncation

Bad:

`ABC1 → ABC`

just because we're chopping off the fourth character.

Why?

Imagine:

`ABC1`

and

`ABC2`

Truncate both:

`ABC1 → ABC`

`ABC2 → ABC`

We've destroyed business identity.

Instead, translation should be based on an approved **business mapping**.

Conceptually:

`ABC1 → XYZ`

That preserves the intended legacy-compatible representation.

---

# 10. Cardinality complicates translation

We covered this yesterday.

Easy case:

`ABC1 ↔ ABC`

**1:1**

But potentially:

`ABC1 → ABC`

`ABC2 → ABC`

That's **many-to-one**.

Now translating backward:

`ABC → ???`

can't tell you whether the original value was `ABC1` or `ABC2`.

Therefore translation may be **lossy**.

Which leads directly to:

# 11. Lineage matters

Suppose:

Original:

`ABC1`

Legacy representation:

`ABC`

If all we retain is:

`ABC`

we may lose the original business identity.

So the BA asks:

> What information must be preserved so that we can reconstruct the original Rep Code associated with the transaction?

That's lineage.

Conceptually:

**Order**

`original_rep = ABC1`

↓

**Translation**

`legacy_rep = ABC`

↓

**Clearing**

`ABC`

But somewhere the organization retains enough lineage to establish:

`Trade 12345`

`ABC`

← translated from →

`ABC1`

That's especially important if Rep Code participates in reporting, supervision or other attribution-sensitive processes.

---

# 12. Effective dating

Now add time.

Suppose:

January–June:

`ABC1 → ABC`

July onward:

`ABC1 → XYZ`

Both mappings may be legitimate.

So asking:

> What's the mapping for ABC1?

is incomplete.

The real question is:

> **What mapping was effective for ABC1 when this transaction occurred?**

Conceptually:

|New|Legacy|From|To|
|---|---|---|---|
|ABC1|ABC|Jan 1|Jun 30|
|ABC1|XYZ|Jul 1|—|

Now a May transaction resolves differently from an August transaction.

That's **historical traceability**.

---

# 13. Missing mappings are business exceptions

Suppose:

New Rep Code:

`QRS1`

Trade reaches a legacy boundary.

Translation asks:

`QRS1 → ???`

No mapping exists.

What happens?

**Do not invent the answer.**

Possibilities might include:

reject

hold

exception queue

manual remediation

retry

something else entirely

But that's Fidelity's business requirement to define.

This was one of the most important lessons from our diagram work:

> **Missing mapping behavior = TBD until discovered.**

---

# 14. Overrides make everything more interesting

Return to our Session 7 example.

Account:

`ABC1`

OMS defaults:

`ABC1`

Authorized user overrides:

`DEF1`

Now which Rep Code matters to the transaction?

If existing business rules say the **order-level Rep Code takes precedence**, then downstream processing potentially needs:

`DEF1`

—not the account's `ABC1`.

And if legacy clearing accepts only three:

`DEF1`

↓

Translation

↓

`DEF`

The account remains:

`ABC1`

So now lineage potentially needs to explain:

**Account default:** `ABC1`

**Order effective Rep:** `DEF1`

**Legacy representation:** `DEF`

That's why understanding the existing business process **before** modifying the system matters so much.

---

# 15. Think about the human/business consequence

This is what we explored yesterday.

Rep Code can represent advisor/team/compensation/order-handling relationships according to the JD.

Therefore a wrong Rep Code potentially means more than:

> “Bad value in column REP_CODE.”

It can mean:

**wrong business attribution**

↓

potentially incorrect reporting / supervision / operational processing

↓

potentially incorrect production or compensation-related attribution depending upon the firm's processes

So:

**data integrity = business integrity.**

That's the connection I want you to remember.

---

# 16. What does the Fidelity BA actually do?

Now everything collapses into your job.

You're not hired merely to write:

> “As a user, I want four-character Rep Codes…”

You're hired to **discover what changing this identifier does to the enterprise**.

Your workflow looks something like:

**Understand AS-IS**
↓
identify SOR and business meaning
↓
trace Rep Code lineage
↓
inventory systems/interfaces
↓
identify owners/SMEs
↓
determine 3/4-character capabilities
↓
discover validation/business rules
↓
identify legacy boundaries
↓
understand translation/mapping
↓
identify exceptions
↓
understand historical/effective-date requirements
↓
identify supervisory/regulatory/reporting impacts
↓

**Gap Analysis**

AS-IS vs required TO-BE

↓

translate discoveries into:

**business requirements**

**functional requirements**

**user stories**

**acceptance criteria**

**data mappings**

**process/data-flow diagrams**

↓

work with engineering

↓

QA/UAT

↓

validate end-to-end behavior

↓

production readiness

That is the role.

And the JD specifically wants someone who can go deep technically and then translate findings for business stakeholders, while independently reaching across the organization to discover answers rather than waiting for requirements to arrive.

---

# 17. Now connect it to you

This is why your FRBNY experience is relevant.

You don't have to claim:

> “I've done Rep Code Expansion before.”

You haven't.

Your bridge is:

**Fidelity problem**

Data moves across systems and interfaces and changes representation.

**Your FRBNY experience**

You worked with streaming market data across Linux, Oracle and AWS, including Oracle data-distribution models, troubleshooting pricing/data-load anomalies, mapping a legacy relational pricing schema into REST API JSON payloads, and validating legacy Oracle data against REST API payloads during modernization.

That's a very credible bridge:

> “The domain is different, but the analysis pattern is familiar to me. At the Fed I worked on modernization where data originating in a legacy Oracle model had to be represented correctly through REST/JSON interfaces and consumed downstream. My role involved understanding the source data, mappings, dependencies and validation. That's why the Rep Code problem makes sense to me as a lineage and system-impact problem rather than simply expanding a field from three to four characters.”

And then you have another advantage:

**You've actually worked at Fidelity before.**

Your v3 documents your work with fixed-income and ratings feeds, reference/pricing/time-series data, security master/golden-copy data and distribution to trading, portfolio-management, regulatory and risk platforms.

So you're not walking into the concept of enterprise financial data completely cold.

---

## The entire project in one picture

Keep **this** in your head:

**Business growth / M&A / advisor complexity**

↓

### 3-character Rep Code capacity is inadequate

↓

**Introduce 4-character capability**

↓

### Existing enterprise has dependencies everywhere

**SOR → Accounts → OMS → Trading → Clearing → Reporting / Supervision / Operations**

↓

### Some systems support 4 chars

**Pass through normally**

### Some legacy systems don't

**Use centralized translation**

`ABC1 → mapped legacy representation`

↓

### Preserve

**business identity + lineage + effective dating + validation + auditability**

↓

### BA's job

**Discover → Map → Analyze gaps → Define requirements → Validate end-to-end**

---

And here's the sentence I'd like you to be able to say naturally by Monday:

> **“I see Rep Code Expansion as much more than increasing a field from three to four characters. The Rep Code carries business meaning across accounts, orders, trading, clearing and other downstream processes. My first step would be to understand the current state and authoritative source, trace the data lineage and business rules, identify every system and interface that stores, validates, transforms or consumes the code, and then determine where four-character support is possible versus where centralized legacy translation is required. From there I can identify gaps and translate them into requirements and acceptance criteria.”**

Don't memorize it word-for-word. **Understand the story well enough that you can recreate it.**

### Where we are now

**Session 7: complete.**

**Rep Code end-to-end refresher: complete.**

Next on our plan is **JD → Paul experience mapping**. That's where we stop talking hypothetically about Fidelity and go bullet-by-bullet through what they're asking for and make sure you have a **real example from your own experience** ready for each important requirement.



---
