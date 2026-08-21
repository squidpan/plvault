---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 2 — Rep Codes 101
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-21
description: We'll start with what a Rep Code actually represents, why it's different from a simple employee ID, how it can relate to accounts/orders/trades, why Fidelity is running out of codes, and why M&A and advisor-team structures make the problem worse.
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---

The goal is to understand who the participants are, what the major business objects are, and what happens when somebody buys a security. The Fidelity JD tells us that Rep Code Expansion ultimately touches advisor structures, supervisory workflows, trading, clearing, operations, and integrations, so this foundation matters.


---

# Session 2 — Rep Codes 101

Exactly. The question for today is:

> **If Mary Jones already has a unique employee/person identifier, why does Fidelity need `ABC`, `DEF`, etc.? What exactly is a Rep Code identifying?**

The Fidelity JD gives us an unusually useful clue. It says Rep Codes are being used for multiple purposes, including **identifying individual advisors, teams, compensation structures, and order-handling roles**. It also says codes are rarely retired, contributing to exhaustion of the available three-character space.

We need to distinguish what the JD actually tells us from the simplified model we'll use to understand it.

---

## 1. Start with Mary Jones

Suppose Mary works for a financial-services organization.

Internally, HR might have:

**Employee ID: 847392**

That answers:

> **Who is Mary Jones as an employee?**

It can be associated with:

name  
employment status  
department  
manager  
payroll  
email  
etc.

But that's not necessarily the identifier the brokerage business wants flowing through accounts, orders, trades, compensation processes, supervision, and downstream systems.

Why?

Because those systems may need to identify **Mary's business role or relationship**, rather than merely Mary the human being.

That's the key distinction.

---

# 2. Person identity vs. business identity

Think about:

**Employee ID 847392**

= **Mary the person/employee**

versus a conceptual:

**Rep Code ABC**

= **a particular brokerage/advisor business assignment or relationship involving Mary**

That gives us a much better mental model.

Don't memorize:

> Rep Code = Advisor ID

Instead think:

> **Rep Code = a business identifier used to represent a rep/advisor-related assignment, relationship, role, or structure within brokerage operations.**

The actual Fidelity model could be more specific than that. The JD doesn't provide their complete data model.

---

# 3. Why does this distinction matter?

Imagine Mary works with two different advisor teams.

Perhaps conceptually:

**Mary Jones**

Employee ID: `847392`

but she participates in:

**Team Alpha → Rep Code ABC**

and

**Team Beta → Rep Code XYZ**

Now one human being is associated with multiple business contexts.

Conversely, imagine:

**Team Alpha**

contains:

Mary  
John  
Susan

The business may need to associate certain activity with the **team**, not merely one employee.

The Fidelity JD explicitly tells us that Rep Codes can be used for **teams**, so this isn't just an abstract possibility.

Already:

> **one person = one Rep Code**

doesn't work as our mental model.

---

# 4. Account relationship

Let's bring Paul back.

Suppose:

**Client: Paul**

↓

**Account: 12345**

↓

**Serviced by advisor relationship represented by Rep Code ABC**

Now Fidelity can potentially associate:

**Account 12345 → ABC**

without every downstream system needing Mary's name.

And some reference/master data somewhere can establish what:

**ABC**

means.

Conceptually:

|Rep Code|Business meaning|
|---|---|
|ABC|Mary / Advisor relationship A|
|DEF|Advisor Team B|
|XYZ|Some other valid business assignment|

Again, illustrative—not Fidelity's actual table.

---

# 5. This is reference data

This concept should be familiar from your old Fidelity Asset Control work.

Imagine thousands/millions of business transactions containing:

`ABC`

You don't want every transaction carrying all possible descriptive information about ABC.

Instead:

**Transaction**

contains:

`rep_code = ABC`

and some authoritative/reference data establishes:

`ABC → whatever business definition ABC represents`

This is conceptually similar to other identifier/reference-data patterns.

For example:

**Security identifier**

`IBM`

↓

reference/security master

↓

International Business Machines + attributes

Or:

**Account ID**

`12345`

↓

account master

↓

Paul's brokerage account + attributes

Likewise conceptually:

**Rep Code**

`ABC`

↓

rep/advisor reference information

↓

business meaning of ABC

This does **not** mean Fidelity actually calls the authoritative source a "Rep Master." We don't know that from the JD.

---

# 6. Now put ABC onto an account

Suppose:

**Paul**

↓

**Account 12345**

↓

`REP_CODE = ABC`

That could tell systems:

> This account/activity is associated with business relationship ABC.

Now Paul says:

> Buy 100 IBM.

An order could conceptually contain:

|Field|Value|
|---|---|
|Account|12345|
|Security|IBM|
|Side|BUY|
|Quantity|100|
|Rep Code|ABC|

Why carry `ABC`?

Because downstream processes may need the business context associated with the transaction.

And now we're getting directly into **your trading BA role**.

---

# 7. Follow ABC through the trading flow

Our Session 1 model was:

**Client**

↓

**Account**

↓

**Order**

↓

**Execution**

↓

**Trade**

↓

**Clearing**

↓

**Settlement**

Now overlay the advisor relationship:

**Advisor / Rep relationship**

↓

**REP CODE = ABC**

↓

**Account 12345**

↓

**Order**

`account=12345`  
`rep=ABC`  
`security=IBM`

↓

**Trading systems**

↓

**Downstream systems**

Potentially including supervision, clearing, reporting, operations, external transmissions, etc.

The Fidelity JD explicitly says the Rep Code Expansion effort spans **core data models, supervisory workflows, trading, clearing, and operational platforms**.

Now you can start seeing why.

---

# 8. Rep Code may have business meaning beyond "who sold it?"

This is where Fidelity's problem gets particularly interesting.

The JD tells us clients use Rep Codes for multiple purposes:

**individual advisors**

**teams**

**compensation structures**

**order-handling roles**

Let's unpack those conceptually.

### Individual advisor

Perhaps:

`ABC → Mary Jones-related assignment`

Straightforward.

### Team

Perhaps:

`DEF → Smith Wealth Management Team`

Several people could participate in that team.

### Compensation structure

A code may participate in determining or representing how business is attributed for compensation purposes.

Conceptually:

> Which rep/team gets credit for this business?

We don't yet know Fidelity's exact compensation mechanics, so don't go beyond that.

### Order-handling role

The individual or business relationship associated with servicing the client may not necessarily be identical to whoever performs some action related to an order.

That creates another possible business distinction.

And now you can see why treating Rep Code as simply:

> "Mary's employee number"

would be inadequate.

---

# 9. Why don't they just keep reusing old codes?

Suppose Fidelity has:

`AAA`  
`AAB`  
`AAC`  
...  
`ZZZ`

Three characters provide a finite namespace.

And the JD specifically tells us:

> codes are **rarely retired**.

Why might a financial institution want to preserve an old identifier?

Think about historical data.

Suppose `ABC` represented some relationship in 2015.

Historical records might say:

**2015 Trade 765432 → Rep Code ABC**

If Fidelity later reassigned `ABC` to an entirely different relationship, somebody investigating that historical trade years later could encounter ambiguity:

> Does ABC mean the old relationship or the new one?

That's bad for traceability.

I'm making the historical example as a **systems-analysis inference**; the JD tells us codes are rarely retired but doesn't specify all reasons.

The important concept is:

**identifiers can acquire long-lived historical meaning.**

---

# 10. Why M&A makes the problem worse

The JD specifically mentions **M&A activity** as one factor putting pressure on the current Rep Code structure.

Suppose Fidelity's platform supports an organization with:

2,000 advisor relationships.

Then that business acquires another organization with:

800 more.

Suddenly you need to incorporate:

new advisors  
new teams  
new relationships  
new business structures  
possibly overlapping legacy conventions

You can't simply assume:

> "We'll delete some old codes."

Especially when historical records and downstream systems may still contain them.

So growth + M&A + increasingly complicated advisor structures = more identifier pressure.

---

# 11. Why three characters eventually become a problem

The JD says the existing three-character structure was designed for **legacy needs** and has become constrained by modern growth and complexity.

Someone apparently tried to stretch the namespace using **special characters**.

Conceptually, perhaps something like:

`AB#`

instead of:

`ABC`

The JD says this short-term mitigation caused:

**poor user experience**

**limited client adoption**

**incompatibility with downstream vendor systems**.

That last one should immediately trigger your systems-analyst brain.

Imagine Vendor X says:

> Rep Code must match `[A-Z0-9]{3}`.

Fidelity sends:

`AB#`

Vendor:

> INVALID.

That's exactly the kind of downstream dependency a BA has to discover.

---

# 12. So Fidelity wants four characters

Conceptually:

Old world:

`ABC`

New world:

`ABC1`

The obvious reaction is:

> Great. Increase `VARCHAR(3)` to `VARCHAR(4)`.

**No.**

That's precisely why this is a large program.

Imagine:

### System A

Database:

`REP_CODE VARCHAR(3)`

### System B

API specification:

`repCode maxLength: 3`

### System C

UI validation:

"Exactly 3 characters"

### System D

Batch file:

positions 45–47 = Rep Code

### System E

business rule:

three-character lookup

### Vendor F

only accepts legacy three-character codes.

Now introduce:

`ABC1`

Potential impact everywhere.

---

# 13. And here's Fidelity's clever complication

They apparently can't upgrade everything simultaneously.

The JD says they're introducing a scalable four-character solution while maintaining compatibility with legacy systems through a:

> **centralized translation approach.**

Let's build a conceptual example.

New canonical world:

**ABCD**

But Legacy System X can only understand:

**XYZ**

So perhaps some centralized capability knows:

|New Code|Legacy Representation|
|---|---|
|ABCD|XYZ|

Then:

**Modern system**

`ABCD`

↓

**TRANSLATION**

`ABCD → XYZ`

↓

**Legacy system**

`XYZ`

That's illustrative—we haven't been given Fidelity's actual mapping design.

But now you should see the architecture problem.

---

# 14. This creates data lineage

Suppose you're the trading BA.

You discover:

**Advisor platform**

`ABCD`

↓

**Account system**

`ABCD`

↓

**Order system**

`ABCD`

↓

**Translation service**

`ABCD → XYZ`

↓

**Legacy trading system**

`XYZ`

↓

**Clearing interface**

`XYZ`

Now somebody asks:

> Trade 827364 belongs to which advisor relationship?

You may need to trace:

`XYZ`

back through:

`XYZ → ABCD`

back to the authoritative business relationship.

That's **data lineage**.

Not merely:

> "I know how to draw arrows in Visio."

It's:

> **Where did this value originate, how was it transformed, where did it travel, and what does it mean at every stage?**

That's one of the central requirements in your JD.

---

# 15. This also creates data mapping

Suppose Trading System A contains:

`REP_CD`

and new Advisor System B contains:

`representativeCode`

and API C contains:

`repCode`

and legacy file D has:

`positions 45–47`.

As BA, you may document:

|Source|Source Field|Target|Target Field|Rule|
|---|---|---|---|---|
|Advisor|representativeCode|Order|REP_CD|direct|
|Order|REP_CD|Legacy Trading|REP|translate 4→3|
|Trading|REP|Reporting|rep_code|translate/reference|

That's **data mapping**.

Again, we're illustrating the concept rather than claiming this is Fidelity's actual architecture.

---

# 16. System of Record

Now introduce another JD phrase:

> **Understanding of systems of record and system changes.**

Imagine five systems contain:

`ABCD`

Which one gets to decide what `ABCD` actually means?

There should generally be some authoritative source for that information.

That's the **System of Record (SOR)** concept.

Suppose:

**Advisor Master System = SOR**

It says:

`ABCD = Smith Advisor Team`

Trading has a copy.

Reporting has a copy.

Clearing receives a copy.

But if they disagree:

**SOR says ABCD = Smith Team**

and

**Reporting says ABCD = Jones Team**

you don't take a vote.

You investigate why Reporting differs from the authoritative source.

This concept is going to be extremely important for your Fidelity interview.

---

# 17. This is surprisingly close to something you've done before

At your earlier Fidelity assignment, you worked with **Asset Control**, reference data, security-master creation, golden-copy management, normalization and downstream distribution.

Different domain object:

**Security**

rather than:

**Rep/advisor relationship**

But conceptually:

### Your old Fidelity world

Vendor data

↓

normalization / cleansing

↓

**Golden copy**

↓

downstream trading / portfolio / risk / regulatory consumers

### Rep Code world

Rep/advisor business information

↓

authoritative representation

↓

**Rep Code**

↓

downstream accounts / trading / supervision / clearing / operations

They're not identical architectures.

But the **master/reference-data thinking** transfers extremely well.

That could become one of your strongest interview bridges later.

---

# 18. Your BA brain should now start asking questions

Imagine your Fidelity Product Owner tells you:

> Paul, we're expanding Rep Codes from three to four characters. Figure out the trading impact.

Don't immediately write:

> **User Story:** As a trader, I want four-character rep codes...

Too soon.

You don't understand the ecosystem yet.

You start **discovery**:

> Where is Rep Code created?

> What is the System of Record?

> What exactly does Rep Code represent?

> Can one person have multiple Rep Codes?

> Can one Rep Code represent multiple people/team relationships?

> Which accounts contain it?

> Which trading applications consume it?

> Is it carried on every order?

> Which APIs contain it?

> Which databases contain it?

> Which batch files contain it?

> Which systems require exactly three characters?

> Which external vendors receive it?

> Where does translation occur?

> What happens to historical records?

> What happens when translation fails?

> How is the code used for supervision?

> What reports depend on it?

That is precisely the investigative behavior this JD calls for when it says candidates must be **curious, comfortable with ambiguity, willing to reach across the organization, and able to discover information rather than wait for requirements to be handed to them.**

Now we're getting into the actual job.

---

# Session 2 mental model

I want you to replace:

**Rep Code = Mary's ID**

with:

**Mary the person**

↓

may participate in one or more

↓

**business/advisor relationships, roles or structures**

↓

represented operationally through

↓

**REP CODE**

↓

associated with accounts/activity

↓

flows into

↓

**orders → trading → clearing → supervision → reporting/operations**

And:

**System of Record**

↓

authoritative Rep Code meaning

↓

**downstream consumers**

That is the core of Session 2.

---

## Knowledge check

Same deal as last time—answer from what you now understand rather than trying to make the wording perfect.

**Q1.** Why isn't an employee ID necessarily sufficient to replace a Rep Code?

**Q2.** Suppose an account contains `REP_CODE = ABC`. Does that mean `ABC` is the client's identifier? What does it tell us instead?

**Q3.** Why could reusing an old Rep Code for a completely different advisor/team relationship create problems?

**Q4.** What does **System of Record** mean? If five systems contain `ABCD`, why do we care which one is the SOR?

**Q5.** In your own words, what's **data lineage**?

**Q6.** Fidelity introduces `ABCD`, but a legacy trading system only accepts three characters. What kind of problem is that, and conceptually what is Fidelity proposing to do about it?

Once we tighten those up, **Session 3 is Trading Lifecycle 101**. That's where we'll take one advisor-assisted order from the client all the way through trading, clearing and settlement and start identifying what the **Trading-focused BA** actually has to investigate.

---

You're doing well. **Q2 and Q4 are essentially there. Q1, Q3, Q5 and Q6 need refinements that matter for the Fidelity interview.** In particular, I want to correct one assumption in Q1 before it gets embedded in your mental model.

## Q1 — Employee ID vs. Rep Code ⚠️

You said:

> employee id is specific to the organization it is issued from and its purpose is not to interface with external systems. Rep Code originates and travels thru the financial system following its own naming convention.

The first part is reasonable as a general distinction, but **don't define Rep Code primarily by whether it travels externally**. A Rep Code could be used internally, externally, or both depending on the system.

The more important distinction is **what the identifier represents**.

**Employee ID**

→ identifies **Mary as an employee/person** within an employment/HR context.

**Rep Code**

→ identifies a **brokerage business assignment, relationship, team, compensation structure, order-handling role, etc.**

The Fidelity JD explicitly tells us their codes are used for several of those purposes.

So think:

> **Employee ID answers "Who is Mary?" Rep Code answers something closer to "What brokerage business relationship/role is this activity associated with?"**

That's why Mary could theoretically participate in more than one Rep Code relationship.

---

## Q2 — Is ABC the client identifier? ✅

You said:

> No it the rep code of the registered rep that has a business relationship with the client but not the client itself

Correct basic idea.

I'd make it slightly broader because of what we just learned:

> **No. The client and account have their own identifiers. ABC represents the relevant rep/advisor business relationship, assignment, team or other Rep Code construct associated with that account/activity.**

So don't lock yourself into:

**Rep Code = registered representative**

because Fidelity specifically says it can represent more than that.

---

## Q3 — Reusing old Rep Codes ⚠️

You said:

> then it breaks the lineage back to the source and can't reconcile the associated relationships

That's good systems thinking, but there's an even more basic problem.

Imagine:

### 2018

`ABC = Mary Smith Team`

Trade #123 contains:

`REP_CODE = ABC`

Mary eventually leaves.

Fidelity retires ABC.

### 2026

Fidelity reassigns:

`ABC = John Jones Team`

Now somebody investigating Trade #123 sees:

`REP_CODE = ABC`

and current reference data says:

> ABC = John Jones Team

But John had **nothing to do with the 2018 transaction**.

That's historical ambiguity/data-integrity trouble.

Your lineage point follows from that:

> **An identifier needs to retain its historical meaning so transactions can be traced and reconciled correctly.**

The JD only tells us that Rep Codes are rarely retired; this example is our systems-analysis reasoning about why reuse can be problematic.

---

## Q4 — System of Record ✅

You said:

> because SOR represents the truth and should be used by all downstream systems

Yes.

Small refinement:

The downstream systems don't necessarily have to query the SOR directly every time.

Think:

**SOR**

= authoritative source of truth

↓

data may be distributed/transformed

↓

**System A**

**System B**

**System C**

If:

SOR: `ABCD = Smith Team`

Trading: `ABCD = Smith Team`

Reporting: `ABCD = Jones Team`

something is wrong.

The SOR tells us which representation is authoritative.

This should feel familiar from your Fidelity Asset Control experience because your resume explicitly refers to **golden-copy data management**.

---

# Q5 — Data lineage ⚠️

You said:

> Data lineage is traceback of the current data back to it's source

Correct, but **expand it in both directions**.

Data lineage isn't only:

**current value ← where did it come from?**

It's the lifecycle/path of the data:

**Where did it originate?**

↓

**Where did it travel?**

↓

**Was it transformed?**

↓

**Which systems consumed it?**

↓

**Where did it ultimately go?**

For example:

**Rep SOR**

`ABCD`

↓

**Account**

`ABCD`

↓

**Order**

`ABCD`

↓

**Translation**

`ABCD → XYZ`

↓

**Legacy Trading**

`XYZ`

↓

**Clearing**

`XYZ`

If someone gives you `XYZ` from a trade, you can trace **backward** toward its origin.

If somebody asks:

> What will be impacted if `ABCD` changes?

you trace **forward** toward its consumers.

So remember:

> **Data lineage tells me where data originated, where it moved, how it was transformed, and where it was consumed.**

That's an interview-quality definition.

---

# Q6 — Centralized translation ⚠️ but very close

You said:

> They want to use a centralized Repository of REP Code that contains the mapping between legacy 3 char and new 4 char rep code. Systems will use the mapping to translate between the legacy and new.

Conceptually, yes.

But there's one important interview discipline here:

**Don't call it a repository unless Fidelity tells us it's a repository.**

The JD says:

> **"centralized translation approach."**

We don't yet know whether Fidelity implements that as:

a database,

a service,

an API,

a mapping table,

middleware,

a translation engine,

or some combination.

So say:

> **Fidelity plans a centralized translation approach that maps the new four-character Rep Code construct to representations required by legacy systems.**

That's safe and accurate.

Conceptually, though, you've got it:

**Modern**

`ABCD`

↓

**CENTRAL TRANSLATION**

`ABCD ↔ XYZ`

↓

**Legacy**

`XYZ`

The interesting BA questions become:

> Who owns that mapping?

> Is it one-to-one?

> Can mappings change?

> What happens when no mapping exists?

> When does translation occur?

> Which systems receive 4-char versus translated 3-char?

> Can translation happen in both directions?

> How are historical transactions reconciled?

> What happens if the translation capability is unavailable?

Those are exactly the sorts of questions a **technical/data-oriented BA** should start asking.

---

# You're now connecting the concepts

Notice what happened across Sessions 1 and 2.

We started with:

**Paul wants to buy IBM.**

Now we have:

**CLIENT**

Paul

↓

**ACCOUNT**

12345

↓

**ADVISOR BUSINESS RELATIONSHIP**

↓

**REP CODE**

ABCD

↓

**ORDER**

Buy 100 IBM

↓

**TRADING**

↓

**CLEARING**

↓

**SETTLEMENT**

while separately:

**REP CODE SOR**

↓

`ABCD`

↓

**data lineage**

↓

**translation if necessary**

↓

`XYZ`

↓

**legacy consumers**

That's enough foundation to move into the part most directly connected to your highlighted role.

# Next — Session 3: Trading Lifecycle 101

We're going to slow the transaction down and follow **one advisor-assisted stock order** from beginning to end:

**Client → Advisor → Account → Order Entry → Order Management → Routing → Execution → Trade → Clearing → Settlement → Books & Records**

We'll introduce the systems you may encounter—especially **OMS, execution venues, clearing, positions and downstream reporting**—and continuously ask:

> **Where is Rep Code at this point?**

That will start showing you what a **Trading-focused BA on Rep Code Expansion** could actually spend the day investigating.


---


