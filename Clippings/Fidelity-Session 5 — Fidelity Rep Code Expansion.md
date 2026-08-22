---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 5 — Fidelity Rep Code Expansion
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-21
description: Now we're going to take Sessions 1–4 and apply them specifically to the project described in the JD.
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---
---

# Session 5 — Fidelity Rep Code Expansion

Now we're going to take Sessions 1–4 and apply them specifically to the project described in the JD.

One discipline throughout this session: I'll distinguish **what the Fidelity JD actually tells us** from the **conceptual architecture we're using to understand it**. We should not walk into an interview presenting our training model as Fidelity's actual implementation.

---

# 1. What do we actually know about the project?

From the JD, we know Fidelity's current Rep Code construct is **three characters** and is no longer sufficient because of:

- client/advisor growth,
    
- M&A activity,
    
- increasingly complex distribution/advisor structures,
    
- multiple uses for Rep Codes,
    
- and the fact that codes are rarely retired.
    

The JD specifically says Rep Codes are being used for **individual advisors, teams, compensation structures, and order-handling roles**.

Fidelity tried a short-term mitigation involving **special characters**, but according to the JD that produced poor UX, limited adoption, and incompatibility with downstream vendor systems.

The strategic direction is:

> **Enable four-character Rep Codes while maintaining compatibility with legacy systems through a centralized translation approach.**

And the initiative spans **core data models, supervisory workflows, trading, clearing, operational platforms, and integrations**.

That's our factual foundation.

---

# 2. The business problem comes before the technology problem

It's tempting to summarize the project as:

> Change Rep Code from 3 characters to 4.

That's technically true but misses the actual problem.

The business problem is closer to:

> **The existing Rep Code namespace can no longer adequately support Fidelity's growing and increasingly complex business structures.**

The **four-character code is the solution direction**.

That's an important BA distinction:

**Business problem**

Insufficient identifier capacity/flexibility

↓

**Business capability needed**

Support continued growth and more complex Rep Code structures

↓

**Solution direction**

Four-character Rep Codes

↓

**Constraint**

Existing legacy systems still depend on the old construct

↓

**Migration/compatibility strategy**

Centralized translation

That is much stronger than thinking:

> "Project = database field expansion."

---

# 3. Why not just add the fourth character everywhere?

Session 4 should make the answer obvious now.

Imagine our conceptual As-Is:

**Rep SOR**

`ABC`

↓

**Account**

`ABC`

↓

**Order Entry**

`ABC`

↓

**OMS**

`ABC`

↓

**Trading**

`ABC`

↓

**Clearing**

`ABC`

↓

**Supervision / Reporting / Operations**

`ABC`

After years of use, assumptions about three characters may exist in:

**database schemas**

`CHAR(3)`

**UI fields**

maximum length 3

**validation**

`length(repCode) = 3`

**APIs**

`maxLength: 3`

**batch files**

positions 51–53

**business rules**

three-character pattern

**reports**

field widths/groupings

**vendor interfaces**

three-character requirement

That's why:

> **3 → 4 is not a field-size project. It's an enterprise dependency project.**

---

# 4. As-Is versus To-Be

Let's use familiar BA terminology.

## AS-IS

Conceptually:

**Authoritative Rep Code**

`ABC`

↓

**Enterprise systems**

designed around 3-character representation

↓

**Downstream / vendor consumers**

expect 3-character representation

The JD tells us that this legacy construct is constrained and special-character mitigation hasn't solved the underlying problem.

## TO-BE

At the highest level:

**Authoritative Rep Code capability**

`ABCD`

↓

**Modern-capable systems**

support four-character codes

while:

**Legacy systems**

continue functioning through some form of:

**centralized translation**

The exact technical architecture is **not provided in the JD**.

---

# 5. The coexistence problem

This is probably the most important architectural concept in Session 5.

Fidelity cannot necessarily say:

> Friday night everything uses three characters. Saturday morning every system uses four.

Large financial platforms contain many systems with different:

owners,

release schedules,

vendors,

technologies,

risks,

regulatory dependencies,

and modernization timelines.

Therefore, we should expect some period where:

**new-world capability**

and

**legacy capability**

must coexist.

Conceptually:

**4-character world**

↕

**compatibility/translation capability**

↕

**3-character world**

That is what makes this more than a simple migration.

---

# 6. What does “centralized translation” mean?

We have to be careful here.

The JD tells us only that there is a:

> **centralized translation approach**.

It does **not** tell us whether that is:

a database,

an API,

a service,

middleware,

a repository,

a library,

or some combination.

So our conceptual example remains:

**Canonical/new Rep Code**

`ABC1`

↓

**Centralized Translation Capability**

`ABC1 ↔ XYZ`

↓

**Legacy Consumer**

`XYZ`

The business purpose is:

> Allow new four-character Rep Codes to coexist with systems that still require a legacy representation.

---

# 7. Translation creates a very important question

Suppose:

`ABC1 → XYZ`

What does `XYZ` mean?

It cannot just be:

> Chop off one character.

We already know why:

`ABC1 → ABC`

could accidentally produce a valid but **incorrect** existing code.

Instead, translation needs to preserve the correct **business identity/relationship**.

Conceptually:

**New representation**

`ABC1`

and

**Legacy representation**

`XYZ`

must correspond to the **same intended business relationship**.

This brings together Session 4:

**mapping**

`ABC1 ↔ XYZ`

**lineage**

Where did ABC1/XYZ travel?

**reconciliation**

Do ABC1 and XYZ represent the same intended business meaning?

---

# 8. Translation isn't merely string conversion

This distinction matters.

Bad mental model:

> Take four characters and convert them to three.

Better mental model:

> **Map a new-world Rep Code representation to the appropriate legacy representation while preserving its business meaning.**

Consider:

`ABC1 = Smith Advisory Team`

Legacy representation:

`XYZ = Smith Advisory Team`

Conceptually:

`ABC1 ↔ XYZ`

Both represent the intended relationship in their respective environments.

Again, this is our conceptual model, not a Fidelity-confirmed implementation.

---

# 9. What happens if there's no mapping?

Now we're doing BA requirements analysis.

Suppose:

**New order**

`RepCode = ABC1`

↓

legacy consumer requires 3-char representation

↓

translation lookup

↓

**NO MAPPING FOUND**

What should happen?

We don't know.

Possible business decisions could include:

**Reject transaction**

**Hold transaction**

**Route to exception processing**

**Alert operations**

**Use some fallback**

But we absolutely should **not invent the answer**.

The BA requirement question is:

> **What is the required business behavior when a valid four-character Rep Code has no legacy mapping?**

That's a requirement waiting to be discovered.

---

# 10. What happens if the mapping is wrong?

Potentially worse.

Expected:

`ABC1 → XYZ`

Actual:

`ABC1 → DEF`

Everything may technically succeed.

Order accepted.

Trade executed.

Clearing completed.

Reporting produced.

But activity could now be associated with the **wrong business relationship**.

Remember our Session 3 principle:

> **Successful processing does not necessarily mean correct processing.**

That's why data validation and reconciliation matter.

---

# 11. What happens if translation is unavailable?

Another requirement question.

Suppose translation is centralized and some dependent system requires it.

Conceptually:

**Trading**

↓

**Translation capability**

💥 unavailable

↓

**Legacy consumer**

What happens?

Again, possibilities might include:

queue,

retry,

fail,

manual exception,

fallback,

etc.

We don't know.

The BA asks:

> What is the required availability/error behavior?

This introduces **non-functional requirements** as well as functional ones.

---

# 12. Functional vs non-functional requirements

Consider:

### Functional

> System shall translate an eligible four-character Rep Code to its corresponding legacy representation before sending data to Legacy System X.

Conceptual example only.

### Functional

> When no valid mapping exists, system shall route the transaction to an exception workflow.

Again, hypothetical until Fidelity defines the behavior.

### Non-functional

Translation capability may have requirements around:

**availability**

**latency**

**throughput**

**auditability**

**security**

**recoverability**

**monitoring**

You already have experience thinking about those kinds of operational requirements from mission-critical financial systems.

---

# 13. Translation direction matters

Another discovery question:

Is translation:

**4 → 3 only?**

Or:

**4 ↔ 3?**

Suppose Legacy Trading returns:

`XYZ`

to another modern system.

Does that modern system need:

`ABC1`?

If yes, perhaps:

`XYZ → ABC1`

is required somewhere.

We cannot assume.

This is exactly why lineage matters.

Trace the complete round trip.

---

# 14. One-to-one mapping?

Another dangerous assumption.

Could:

`ABC1 → XYZ`

be strictly one-to-one?

Maybe.

Could multiple new codes map to one legacy construct?

Possibly.

Could mapping depend on date/business context?

Possibly.

The JD doesn't say.

Therefore your BA discovery questions include:

> Is mapping one-to-one?

> Can a code have multiple legacy representations?

> Can mappings change?

> Are mappings effective-dated?

> Who creates/approves mappings?

> Can mappings be retired?

> How are historical mappings retained?

Those are **excellent discovery questions** because Rep Codes are rarely retired and historical meaning may matter. The JD establishes the first fact; the detailed mapping questions are our analysis.

---

# 15. Historical data is a separate problem

Suppose in 2025:

`ABC = Smith Team`

Then after expansion:

`ABC1 = Smith Team`

What happens to historical trades containing:

`ABC`?

Possible strategies include:

**leave history unchanged**

**translate at query/reporting time**

**migrate historical records**

**maintain historical mapping/reference data**

We don't know Fidelity's choice.

But as BA you need to ask:

> **Does Rep Code Expansion affect historical data, only new transactions, or both?**

Very important.

---

# 16. Now look at Trading specifically

Remember: **your allocation is Trading-focused BA** according to the JD.

You probably don't own the entire enterprise initiative.

Your boundary might be:

**Upstream Order/Account**

↓

**Trading ecosystem**

↓

**Post-trade / Clearing**

Your responsibility becomes something like:

> **Determine how four-character Rep Codes affect Trading and its upstream/downstream dependencies.**

That means investigating the As-Is.

---

# 17. Your Trading impact inventory

You might gradually build something like this:

|Component|Rep Code use|Current constraint|4-char impact|Action|
|---|---|---|---|---|
|Order Entry|Capture/display|TBD|TBD|Discover|
|OMS|Order attribution|TBD|TBD|Discover|
|Trading DB|Store|3 chars?|Potential|Verify|
|Trading API|Transmit|TBD|TBD|Verify|
|Translation|Compatibility|New capability|Major|Understand|
|Clearing Interface|Downstream handoff|3 chars?|Potential|Verify|
|Supervision|Business attribution|TBD|Potential|Verify|

The `?` values matter.

A BA doesn't fill unknowns with guesses.

**TBD becomes a managed discovery item.**

---

# 18. Start with As-Is

Your Session 3 answer was already heading here.

Manager:

> Determine Trading impact.

You:

> **First I need to understand the current Rep Code lifecycle through the Trading environment—where it enters, which systems use it, how it moves between them, whether it's transformed, and which downstream consumers depend on it.**

Then create:

**As-Is flow**

↓

**impact inventory**

↓

**gaps**

↓

**To-Be**

↓

**requirements**

↓

**testing**

That's a very strong BA sequence.

---

# 19. Gap analysis

Once you know As-Is and target capability, compare them.

Example:

|Capability|As-Is|To-Be|Gap|
|---|---|---|---|
|Rep Code length|3|4|Yes|
|OMS storage|10|10|No|
|OMS validation|exactly 3|support 3/4|Yes|
|Trading interface|max 3|support required representation|Yes|
|Legacy clearing|3|remains 3|Translation needed|
|Reporting|unknown|correctly represent new codes|Discovery needed|

That's **gap analysis**.

And notice:

You cannot do good gap analysis until you understand both:

**As-Is**

and

**To-Be**.

---

# 20. Migration vs coexistence

These aren't necessarily the same thing.

### Migration

Moving from old state to new state.

**3-character model → 4-character-capable model**

### Coexistence

Old and new operate simultaneously.

**3-char + 4-char**

or:

**4-char modern representation + 3-char legacy representation**

The Fidelity JD strongly implies some degree of compatibility/coexistence because it explicitly says the new solution must maintain compatibility with legacy systems through centralized translation.

The detailed migration strategy isn't provided.

---

# 21. Testing becomes much bigger than “does ABC1 fit?”

Suppose you're writing acceptance criteria.

Weak test:

> Enter `ABC1`. Verify field accepts four characters.

Necessary perhaps, but nowhere near sufficient.

You need scenarios such as:

### Existing legacy code

`ABC`

Does existing functionality still work?

### New code

`ABC1`

Does modern processing work?

### New → legacy mapping

`ABC1 → XYZ`

Correct?

### Invalid code

`ZZZZ`

Correct rejection?

### Missing mapping

What required behavior occurs?

### Incorrect/inactive mapping

Detected?

### Historical trade

Does old `ABC` retain correct historical meaning?

### Downstream reconciliation

Does trade/reporting output preserve correct business attribution?

Now you're testing the **business capability**, not merely field length.

---

# 22. Regression testing is crucial

Why?

Because Fidelity isn't merely adding new codes.

It has an enormous existing population of **three-character codes**.

So the requirement isn't:

> Four-character codes work.

It's more like:

> **Four-character capability works without breaking existing valid three-character processing.**

That's regression territory.

This should be very comfortable for you because regression/QA/UAT is already part of your BA experience.

---

# 23. Acceptance criteria should expose the business rules

Conceptual story:

> **As a trading platform, I need to process transactions associated with supported four-character Rep Codes so that new advisor/business structures can transact without disrupting legacy downstream processing.**

Possible AC — illustrative only:

**Given** an active four-character Rep Code with a valid legacy mapping  
**When** an eligible order proceeds to a legacy consumer  
**Then** the appropriate legacy representation is transmitted.

Another:

**Given** an existing valid three-character Rep Code  
**When** an order proceeds through Trading  
**Then** existing processing remains unchanged.

Another:

**Given** a four-character Rep Code requiring legacy translation  
**When** no valid mapping exists  
**Then** the defined exception behavior occurs and the failure is traceable.

The exact behavior must come from Fidelity SMEs/requirements.

But now you understand what good AC is trying to prove.

---

# 24. Traceability

Now connect everything:

**Business need**

More Rep Code capacity/flexibility

↓

**Requirement**

Support 4-character codes

↓

**System impact**

OMS / Trading / interfaces / clearing etc.

↓

**Mapping**

new ↔ legacy representation

↓

**User story**

specific system capability

↓

**Acceptance criteria**

expected behavior

↓

**Test cases**

prove the behavior

↓

**Defect / result**

↓

**Requirement satisfied**

That's requirements traceability.

It should connect nicely to your existing way of working with stories, acceptance criteria, QA/UAT and Jira.

---

# 25. Release strategy

Suppose 20 systems need changes.

Can they all deploy simultaneously?

Maybe not.

That creates sequencing dependencies.

Perhaps:

**Translation capability must exist**

before:

**System X enables four-character codes**

because otherwise downstream Y can't consume them.

Or:

**SOR changes**

must precede:

**Account System changes**

must precede:

**Trading changes**

Those are **release dependencies**.

We don't know Fidelity's actual sequence.

But the BA should identify dependencies so rollout planning doesn't create an incompatible intermediate state.

---

# 26. Your FRBNY modernization parallel

There's a useful conceptual bridge in the resume you're submitting.

At FRBNY, you worked with legacy Oracle-based distribution and mapped relational pricing data into REST/JSON representations while validating legacy data against the new API representation.

That's not Rep Code Expansion.

But the transferable systems-analysis pattern is:

### MRPrice

**Legacy representation**

↓

**mapping**

↓

**new representation**

↓

**downstream consumers**

↓

**validation/reconciliation**

### Fidelity

**new Rep Code representation**

↓

**mapping/translation**

↓

**legacy-compatible representation**

↓

**downstream consumers**

↓

**validation/reconciliation**

Different business data.

Very similar analytical muscles.

---

# 27. Your previous Fidelity experience is another bridge

Your resume says that during your earlier Fidelity engagement you supported **Asset Control financial-data/reference-data workflows, security master creation, golden-copy management, normalization, consolidation, cleansing and downstream distribution to trading, portfolio management, regulatory and risk platforms.**

Again:

**Security master ≠ Rep Code master.**

Don't claim they're the same.

But the conceptual experience transfers:

**authoritative/reference data**

↓

**normalization/management**

↓

**distribution**

↓

**multiple downstream consumers**

↓

**data integrity matters**

That's very useful for this role.

---

# 28. What you should NOT claim in an interview

This is important.

Don't say:

> Fidelity has a central Rep Code database.

We don't know that.

Don't say:

> Translation happens before Trading.

We don't know that.

Don't say:

> Rep Code gets transmitted to the exchange.

We don't know that.

Don't say:

> ABC1 maps one-to-one to XYZ.

We don't know that.

Instead:

> **“My understanding from the project description is that Fidelity is introducing four-character Rep Codes with a centralized translation approach for legacy compatibility. One of my first discovery tasks on the Trading side would be to determine where translation occurs and which systems require the legacy versus new representation.”**

That's both knowledgeable and disciplined.

---

# 29. Session 5 mental model

Here's the entire initiative in one conceptual chain:

**BUSINESS GROWTH / COMPLEXITY**

↓

**3-character namespace inadequate**

↓

**4-character capability required**

↓

**BUT**

↓

**legacy ecosystem still exists**

↓

**CENTRALIZED TRANSLATION APPROACH**

↓

**NEW + LEGACY COEXISTENCE**

↓

requires:

**Data lineage**

**Data mapping**

**System impact analysis**

**Business rules**

**Exception handling**

**Regression**

**Reconciliation**

**Release dependencies**

**UAT**

That's why Fidelity needs multiple BAs across Trading, reporting, UI, backend, API/external transmissions and related areas—not someone whose job is simply to change a field from 3 to 4.

---

# Knowledge check — Session 5

Don't try to make these interview-perfect. Explain them like you've been doing.

**Q1.** What is the **business problem** Fidelity is solving, as opposed to the technical solution of introducing four-character Rep Codes?

**Q2.** Why can't Fidelity necessarily change every system from three to four characters at once?

**Q3.** Why is:

> `ABC1 → ABC`

not a safe translation strategy?

**Q4.** Explain the difference between **migration** and **coexistence** in this project.

**Q5.** Suppose a four-character Rep Code reaches the translation capability but **no valid legacy mapping exists**. As the BA, what should you do? Don't invent Fidelity's required behavior.

**Q6.** Suppose the OMS database supports four characters, its UI supports four characters, and its inbound interface supports four characters—but its validation rule requires exactly three characters. Is OMS ready? Explain.

**Q7.** What's the difference between testing:

> “The Rep Code field accepts four characters”

and testing the **actual Rep Code Expansion business capability**?

**Q8 — most important.** You're the Trading BA. After documenting the As-Is Rep Code flow, what would you compare it against to perform **gap analysis**, and what kinds of gaps are you looking for?

After we tighten these, **Session 6 is the Regulatory Environment for a Trading BA**. We should also be able to move faster through that one.



---


