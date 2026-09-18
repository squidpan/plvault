---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 4 — Systems, Data & Data Lineage
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-22
description: This is a major session for your Fidelity role because the JD specifically calls for data lineage/mapping experience, understanding systems of record/system changes, data flows/APIs/business logic, and the ability to work through complex systems and dependencies.
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---

---

# Session 4 — Systems, Data & Data Lineage

This is a major session for your Fidelity role because the JD specifically calls for **data lineage/mapping experience, understanding systems of record/system changes, data flows/APIs/business logic, and the ability to work through complex systems and dependencies.**

We're going to build those concepts around the Pre/Post Trade maps we already created.

The central question today is:

> **If I see `REP_CODE = ABC1` on a trade, how do I determine where it came from, what happened to it, where else it went, and what will be affected if its structure changes?**

---

# 1. Start with the simplest possible system flow

Suppose discovery gives us this conceptual flow:

**Rep Code SOR**

↓

**Account System**

↓

**Order Entry**

↓

**OMS**

↓

**Trade Processing**

↓

**Clearing**

↓

**Reporting**

Now add data:

**Rep Code SOR**

`ABC1`

↓

**Account System**

`Account=12345`  
`RepCode=ABC1`

↓

**Order Entry**

`Account=12345`  
`RepCode=ABC1`  
`Security=IBM`  
`Qty=100`

↓

**OMS**

`Order=ORD9001`  
`Account=12345`  
`RepCode=ABC1`

↓

**Trade Processing**

`Trade=TRD7001`  
`Order=ORD9001`  
`RepCode=ABC1`

↓

**Clearing**

`Trade=TRD7001`  
`RepCode=?`

↓

**Reporting**

`Trade=TRD7001`  
`RepCode=?`

Those question marks are intentional.

As BA, **we don't fill them in because we think we know the answer.**

We investigate.

That principle is going to run through this entire session.

---

# 2. System of Record — SOR

We've already introduced this.

The **System of Record** is the authoritative source for a particular piece of business information.

Suppose five systems contain:

`ABC1`

But the Advisor/Rep platform owns the authoritative definition of `ABC1`.

Conceptually:

**REP SOR**

`ABC1 = Smith Advisory Team`

↓

copies/distributions

↓

Account

↓

Trading

↓

Reporting

If Reporting says:

`ABC1 = Jones Team`

while the SOR says:

`ABC1 = Smith Team`

we have a problem.

The important point is:

> **Containing data does not make a system the System of Record.**

---

# 3. Source system is not always the SOR

This distinction is useful.

Suppose Trading receives Rep Code from the OMS.

From Trading's perspective:

**OMS = source system**

because that's where Trading received the value.

But OMS might have received it from Account Services.

And Account Services received it from the authoritative Rep system.

So:

**Rep SOR**

↓

**Account**

↓

**OMS**

↓

**Trading**

For Trading:

**Immediate source = OMS**

but:

**Authoritative source = Rep SOR**

Don't confuse them.

That's a very useful systems-analysis distinction.

---

# 4. Upstream and downstream

These terms are relative.

Consider:

**Account → OMS → Trading → Clearing**

From the perspective of **Trading**:

### Upstream

OMS  
Account  
Rep SOR

because information comes from that direction.

### Downstream

Clearing  
Reporting  
other consumers

because information travels toward them.

But from the perspective of **OMS**:

Account is upstream.

Trading is downstream.

So:

> **Upstream/downstream always depends on the system/process you're standing in.**

---

# 5. Interface

Now we need to distinguish:

**system**

from:

**connection between systems**.

Suppose:

**OMS**

↓

**Trading**

How does data actually get from one to the other?

Perhaps:

REST API

message queue

file

database interface

event stream

FIX message

batch process

etc.

That's the **interface/integration mechanism**.

For our Fidelity exercise we don't know the actual interfaces, so our parent diagram simply says:

**OMS → Trading**

During discovery you'd ask:

> How is Rep Code transmitted between these systems?

That could reveal an important dependency.

---

# 6. Why interfaces matter to Rep Code Expansion

Imagine:

OMS database supports:

`VARCHAR(4)`

Trading database supports:

`VARCHAR(4)`

You might conclude:

> Great. Both systems support ABC1.

Not necessarily.

Suppose the interface between them says:

`REP_CODE maxLength = 3`

Then:

**OMS**

supports 4

↓

**INTERFACE**

supports only 3

↓

**Trading**

supports 4

You still have an impact.

That's why the BA can't investigate only applications.

You investigate:

> **systems + interfaces + data + business rules.**

---

# 7. Data flow

A **data flow** describes movement of information between components/processes.

For example:

**Account System**

↓

`Account # + Rep Code`

↓

**Order Entry**

↓

`Account # + Rep Code + Security + Qty + Side`

↓

**OMS**

That's what we've already begun drawing.

At the overview level, you're asking:

> **What information moves from A to B?**

That's why your instinct yesterday to draw boxes with information going in/out was good.

---

# 8. Data lineage goes further

This is where people sometimes confuse **data flow** with **data lineage**.

### Data flow

> Data moves from A → B → C.

### Data lineage

asks:

> Where did this particular data element originate?

> Which systems touched it?

> What was its representation in each system?

> Was it transformed?

> Where was it ultimately consumed?

For example:

**Rep SOR**

`rep_code = ABC1`

↓

**Account**

`advisor_rep_code = ABC1`

↓

**OMS**

`repCd = ABC1`

↓

**Translation**

`ABC1 → XYZ`

↓

**Legacy Trading**

`rep = XYZ`

↓

**Reporting**

perhaps ultimately represented as `ABC1` again.

That's lineage.

---

# 9. Forward lineage vs backward lineage

This distinction is especially useful for BA impact analysis.

### Backward lineage

You find:

`XYZ`

in a trade.

You ask:

> **Where did XYZ come from?**

Trace backward:

**Legacy Trade `XYZ`**

↑

Translation

`ABC1 → XYZ`

↑

OMS `ABC1`

↑

Account `ABC1`

↑

Rep SOR `ABC1`

You have traced the data toward its origin.

### Forward lineage

Now Fidelity tells you:

> We're changing the Rep Code structure.

Start at:

**Rep SOR**

and ask:

> **Who consumes this data?**

Trace forward:

SOR

↓

Account

↓

OMS

↓

Trading

↓

Clearing

↓

Reporting

That's **impact analysis**.

So remember:

> **Backward lineage helps answer “Where did this come from?”**

> **Forward lineage helps answer “What could this change affect?”**

---

# 10. Transformation

Now we add another important concept.

Data doesn't always travel unchanged.

Example:

**Source**

`ABC1`

↓

**Transformation**

`ABC1 → XYZ`

↓

**Target**

`XYZ`

Translation is one type of transformation.

But transformations can also include:

formatting,

normalization,

enrichment,

derivation,

aggregation,

filtering,

conversion,

etc.

For Rep Code Expansion, transformation is particularly important because the JD explicitly describes centralized translation to maintain compatibility with legacy systems.

---

# 11. Data mapping

Now let's distinguish **mapping** from **lineage**.

Suppose:

### Account System

field:

`advisor_rep_code`

### OMS

field:

`repCd`

### Trading

field:

`REP_CODE`

You document:

|Source|Source field|Target|Target field|Rule|
|---|---|---|---|---|
|Account|`advisor_rep_code`|OMS|`repCd`|Direct|
|OMS|`repCd`|Trading|`REP_CODE`|Direct|
|Trading|`REP_CODE`|Legacy Consumer|`REP`|Translation required|

That's a **data mapping**.

It answers:

> **How does field X in the source correspond to field Y in the target?**

---

# 12. Lineage vs mapping

This is worth memorizing conceptually.

### LINEAGE

**The journey**

> Where did the data originate, where did it travel, how did it change, and where was it consumed?

### MAPPING

**The correspondence**

> Which source field/value corresponds to which target field/value, and according to what transformation rule?

Think:

**Lineage = path**

**Mapping = correspondence**

That's a good interview shorthand.

---

# 13. Add business rules

Now suppose OMS has:

> Rep Code must contain exactly 3 alphanumeric characters.

That's a **business/system rule**.

Perhaps another rule says:

> Rep Code must be active on trade date.

Another:

> Account must have a valid relationship with the supplied Rep Code.

Now Fidelity introduces four characters.

Even if the database field is:

`VARCHAR(20)`

the application might still reject `ABC1` because:

**validation rule = length 3**

Therefore impact analysis must include:

**Data storage**

AND

**business/application rules**

---

# 14. Dependency

Now we're ready for another JD word.

A **dependency** exists when one component/process relies on another component, data element, interface, rule or capability.

Example:

**Trading System X depends on OMS for Rep Code.**

OMS depends on:

**Account System**

Account System depends on:

**Rep reference data**

Trading also depends on:

**interface specification**

accepting the value.

Therefore:

**Rep Code change**

can ripple through a dependency chain.

This is why Fidelity wants someone comfortable working through **complex systems and dependencies.**

---

# 15. Let's do a realistic impact-analysis example

Discovery reveals:

**Rep SOR**

supports 4 characters.

↓

**Account System**

supports 4.

↓

**OMS database**

supports 10.

↓

**OMS validation**

requires exactly 3.

↓

**OMS → Trading API**

supports 4.

↓

**Trading database**

supports 3.

↓

**Trading → Clearing file**

allocates exactly 3 positions.

Now someone asks:

> Which components are impacted?

Not simply:

**Trading database.**

You found:

### OMS

Database: **OK**

Validation rule: **IMPACTED**

### OMS → Trading interface

**OK**

### Trading

Database: **IMPACTED**

### Trading → Clearing interface

Fixed-width field: **IMPACTED**

That is systems analysis.

---

# 16. This is why SQL eventually matters

Suppose nobody knows everywhere Rep Code is stored.

You might use SQL to investigate:

> Which tables contain `REP_CODE`?

Then inspect actual data:

> How many distinct codes?

> What's maximum length?

> Are special characters present?

> Are there nulls?

> Which account records don't match reference data?

> Which trade records contain unknown Rep Codes?

That's why our later SQL refresher isn't generic programming training.

It's another **BA discovery/data-analysis tool**.

But SQL stays later today.

---

# 17. Reconciliation

Another concept you're likely to encounter.

Suppose:

### SOR

`ABC1 = Smith Team`

### OMS

`ABC1`

### Trading

`XYZ`

because:

`ABC1 → XYZ`

How do we establish that the values across systems represent the same business relationship?

We **reconcile** them.

Conceptually:

**SOR `ABC1`**

↓

mapping

`ABC1 ↔ XYZ`

↓

**Trading `XYZ`**

↓

confirm expected relationship

That's reconciliation.

If Trading contains:

`QRS`

instead:

🚨 exception.

This is closely related to work you've done validating legacy Oracle data against REST/JSON representations during modernization. Your resume specifically describes that kind of validation.

---

# 18. Let's put the major terms together

Suppose we discover:

**Rep SOR**

`ABC1`

↓

API

↓

**Account System**

`advisor_rep_code = ABC1`

↓

message

↓

**OMS**

`repCd = ABC1`

↓

translation

`ABC1 → XYZ`

↓

fixed-width file

↓

**Legacy Trading**

`REP = XYZ`

Now:

### System of Record

**Rep SOR**

### Source for OMS

**Account System**

### Upstream of OMS

Account / Rep SOR

### Downstream of OMS

Trading

### Interface

API/message/file connecting systems

### Data flow

Movement of Rep Code and related information

### Data lineage

Entire `ABC1 → ... → XYZ` journey

### Data mapping

`advisor_rep_code → repCd → REP`

plus transformation rules

### Transformation

`ABC1 → XYZ`

### Dependency

Legacy Trading depends upon receiving an acceptable Rep representation

### Reconciliation

Prove `XYZ` correctly corresponds to authoritative `ABC1`

That's the vocabulary I want you comfortable with.

---

# 19. Now relate this to our Pre-Trade parent

Our parent diagram contains approximately:

**Rep Code SOR + Account System**

↓

**Order Entry**

↓

**Validation**

↓

**OMS**

↓

**Routing**

↓

**Execution Venue**

For today's topic, we **don't need a completely different diagram**.

We can focus on a meaningful Layer-2 boundary:

### Candidate Layer 2 — Pre-Trade Rep Code Data Lineage

**Rep Code SOR + Account System**

↓

**Order Entry**

↓

**Validation**

↓

**OMS**

That group makes sense because we're asking:

> **How does authoritative Rep Code information get associated with an account/order, validated, and delivered into order management?**

That's a good example of what you were saying yesterday: Layer 2 may drill into **several connected parent components**, not just one box.

We don't need to build it this second. We'll identify these candidates during the lesson and visually review them later.

---

# 20. Post-Trade candidate

Our Post-Trade parent has:

**OMS**

↓

**Trade Processing**

↓

**Clearing**

↓

**Settlement**

with:

**Translation**

off to the side.

A logical Layer-2 boundary might be:

### Post-Trade Rep Code Translation & Handoff

**OMS → Trade Processing ↔ Translation → Clearing**

because those components together answer:

> **How does Rep Code move from executed trade processing toward a legacy/downstream consumer, and where might translation occur?**

Again: a meaningful boundary, not necessarily one parent box.

---

# 21. The BA artifact you're gradually producing

After discovery, you may end up with something like:

|System|Owner|Rep field|Source|Length|Transform?|Downstream|
|---|---|---|---|--:|---|---|
|Account|Team A|`advisor_rep_code`|Rep SOR|4|No|OMS|
|OMS|Team B|`repCd`|Account|4|No|Trading|
|Trading|Team C|`REP_CODE`|OMS|3|TBD|Clearing|
|Clearing Interface|Team D|`REP`|Trading|3|TBD|External/Legacy|

That's an **impact inventory**.

And notice how naturally it follows from your original idea:

> **boxes with information going in and coming out**

We're simply adding rigor.

---

# 22. The really important BA distinction

Suppose someone asks:

> "Does Trading support four-character Rep Codes?"

A weak answer:

> Yes, the database field is VARCHAR(10).

A systems analyst asks:

**Database?**

Yes.

**UI?**

Maybe.

**Validation rules?**

Unknown.

**Inbound interface?**

Yes.

**Outbound interface?**

No.

**Downstream consumer?**

No.

Therefore:

> **The trading application is not end-to-end ready for four-character Rep Codes even though its database can store them.**

That's what **working through complex systems and dependencies** really means.

---

# Session 4 — Core mental model

Keep this chain:

**SOR**

Where is authoritative truth?

↓

**SOURCE**

Where did this system receive it?

↓

**INTERFACE**

How did it arrive?

↓

**MAPPING**

Which field corresponds to which?

↓

**TRANSFORMATION**

Did the value change?

↓

**TARGET**

Where did it land?

↓

**DOWNSTREAM**

Who consumes it next?

And across the entire chain:

# DATA LINEAGE

**Origin → movement → transformation → consumption**

---

## Session 4 knowledge check

Take these one at a time in your own words.

**Q1.** Trading receives `ABC1` from OMS. OMS received it from Account Services, and Account Services received it from the Rep SOR. What's the difference between **Trading's source system** and the **System of Record**?

**Q2.** What's the difference between **data lineage** and **data mapping**?

**Q3.** Both OMS and Trading databases support four-character Rep Codes. Can we conclude that the OMS → Trading flow supports four characters? Why or why not?

**Q4.** You discover:

`Rep SOR ABC1 → Account ABC1 → OMS ABC1 → Translation XYZ → Legacy Trading XYZ`

Someone gives you `XYZ` from a trade and asks what authoritative Rep Code it represents. Are you tracing lineage **forward or backward**, and what are you trying to establish?

**Q5.** Fidelity changes Rep Code at the SOR from a 3-character construct to supporting 4-character codes. You're trying to identify everything potentially impacted downstream. Are you primarily tracing lineage **forward or backward**?

**Q6.** What's wrong with saying:

> "Trading supports four-character Rep Codes because its database column is VARCHAR(10)"?

After these, we'll decide whether Session 4 needs a **Layer-2 lineage PUML**. I think it probably does, but I want you to answer first because your understanding should determine what information belongs on that drill-down diagram—not the other way around.

---

Good. You have the **Session 4 systems-analysis model**. Q2 needs one missing piece; the others are essentially correct.

## Q1 — Source System vs. SOR ✅

You said:

> Trading source system is OMS. Account Services is the source system for OMS. System of Record is the authoritative source of the record.

Exactly.

The distinction to retain is:

**Immediate source** = where _this system_ received the data.

**SOR** = authoritative owner/source of truth for the data.

So:

**Rep SOR → Account Services → OMS → Trading**

From Trading's perspective:

`Source = OMS`

`Authoritative source = Rep SOR`

Very good.

---

## Q2 — Data Lineage vs. Data Mapping ⚠️

You correctly described **lineage**, including forward/backward lineage, but didn't answer the **mapping** half.

You said:

> Data lineage is the journey of the value...

Yes.

Now add:

### Data lineage = the journey/path

`Rep SOR → Account → OMS → Translation → Trading`

It tells us:

> Where did it originate, where did it travel, how did it change, and where was it consumed?

### Data mapping = correspondence

For example:

|Source field|Target field|Rule|
|---|---|---|
|`advisor_rep_code`|`repCd`|Direct|
|`repCd`|`REP_CODE`|Direct|
|`REP_CODE = ABC1`|`REP = XYZ`|Translate|

It tells us:

> **How does this source data element/value correspond to the target data element/value?**

The shorthand I want you to retain:

> **Lineage = path. Mapping = correspondence.**

---

# Q3 — Database support doesn't prove interface support ✅

You said:

> Not yet. it depends on whether the interface supports 4 character REP code. So need to understand if the interfaces passes it thru, blocks it or transforms it

**Exactly.**

And I'd add one more possibility:

**truncates it.**

Suppose:

OMS DB: `VARCHAR(10)` ✅

Trading DB: `VARCHAR(10)` ✅

but interface specification:

`maxLength = 3` ❌

Then the end-to-end flow **doesn't support four characters**.

This is exactly why we investigate:

**System → Interface → System**

rather than looking at databases alone.

---

# Q4 — Backward lineage ✅

You said:

> Tracing backwards. see if there is a authoritative Rep code that maps to the 3 char code

Correct.

You find:

`XYZ`

in Legacy Trading.

Trace:

**Legacy Trading**

`XYZ`

↑

**Translation**

`ABC1 → XYZ`

↑

**OMS**

`ABC1`

↑

**Account**

`ABC1`

↑

**Rep SOR**

`ABC1`

You're establishing:

> **What authoritative business identifier does this legacy representation correspond to?**

This can support traceability and reconciliation.

---

# Q5 — Impact analysis = forward lineage ✅

You said:

> Forward

Exactly.

Something changes at the authoritative source:

**Rep Code SOR**

`ABC → ABC1 capability`

↓

**Who consumes this?**

↓

Account

↓

OMS

↓

Trading

↓

Clearing

↓

Reporting

You trace **forward** to discover potential downstream impact.

That's an important interview concept:

> **Backward lineage helps trace a value to its origin. Forward lineage helps identify downstream impact.**

---

# Q6 — Storage isn't application support ✅

You said:

> need to find out if the application supports 4 chars. ability to store 4 chars rep code alone is not enough

Exactly.

This is one of the most important lessons from Session 4.

You'd investigate:

**Storage**

Can DB store 4?

**UI/input**

Can application accept 4?

**Validation**

Do rules permit 4?

**Business logic**

Does anything assume 3?

**Inbound interface**

Can it receive 4?

**Outbound interface**

Can it transmit 4?

**Transformation**

Does anything truncate/change it?

**Downstream**

Can consumers handle it?

Only then can we say:

> **System/flow supports four-character Rep Codes.**

---

# Session 4 passed

You're now distinguishing concepts that were fairly fuzzy yesterday:

|Concept|Question it answers|
|---|---|
|**SOR**|Where is the authoritative truth?|
|**Source system**|Where did _this system_ receive the data?|
|**Upstream**|What feeds me?|
|**Downstream**|What do I feed?|
|**Interface**|How does data move between systems?|
|**Data flow**|What information moves between components?|
|**Data lineage**|Where did it originate, travel, transform and get consumed?|
|**Data mapping**|How does source data correspond to target data?|
|**Transformation**|How did the representation/value change?|
|**Dependency**|What relies upon what?|
|**Reconciliation**|Do representations across systems correctly correspond?|

And there's an important progression happening:

### Yesterday

> Four-character Rep Code could break Trading.

### Now

You're asking:

> **Where does the value originate? Who receives it? Through what interface? What field is it mapped to? Is it transformed? What rules operate on it? Who consumes it downstream?**

That's the level of thinking this Fidelity BA role calls for.

---

# Diagram decision — Session 4

I think Session 4 **does deserve one Layer-2 diagram**, but not yet a Layer 3.

Our existing **Pre-Trade parent** remains Layer 1.

The useful Layer-2 boundary is probably:

**Rep Code SOR + Account System**

↓

**Order Entry**

↓

**Validation**

↓

**OMS**

and the diagram should expose:

`Rep Code`

`Account #`

`Order ID`

field mappings

source vs. SOR

interfaces

validation

forward/backward lineage

and the handoff boundary into the next portion of Trading.

That would be:

**TRD-11 — Pre-Trade Rep Code Data Lineage**

**Parent:** TRD-10 Pre-Trade

I would **not build Layer 3 yet**. Nothing we've learned requires it.

And per our agreement, we don't need to interrupt the learning flow to build TRD-11 right now. We can build/review the diagram at today's diagram checkpoint and you can visually decide whether the boundary works.

## Next — Session 5: Fidelity Rep Code Expansion

Now we can finally put everything together around the **actual initiative**:

**Why 3 characters became inadequate**

→ **4-character target**

→ **legacy compatibility**

→ **centralized translation**

→ **systems impact**

→ **migration/coexistence**

→ **failure scenarios**

→ **As-Is vs. To-Be**

→ **what the Trading BA actually needs to discover and document**

This should be easier than Session 4 because we now have the vocabulary necessary to understand the problem properly.




