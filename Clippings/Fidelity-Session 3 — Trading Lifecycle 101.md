---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 2 — Rep Codes 101
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-21
description: "one advisor-assisted stock order end-to-end and keep asking one question: Where might the Rep Code matter at this point?"
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---

---

# Session 3 — Trading Lifecycle 101

Now we'll follow **one advisor-assisted stock order end-to-end** and keep asking one question:

> **Where might the Rep Code matter at this point?**

We're going beyond what the Fidelity JD explicitly documents here. The JD tells us Rep Code Expansion spans **trading, clearing, supervisory workflows, operational platforms, data models and integrations**; the detailed trading lifecycle below is the general brokerage-domain model we'll use to understand why.

---

# 1. Our scenario

Let's keep the same example.

**Client:** Paul  
**Advisor:** Mary Jones  
**Rep Code:** `ABC`  
**Account:** `12345`  
**Available cash:** $50,000

You tell Mary:

> "Buy 100 shares of IBM."

Eventually we want:

**Paul → Mary → Account 12345 → Order → Market → Execution → Trade → Clearing → Settlement**

But there is a lot happening between those boxes.

---

# 2. Step 1 — Client and advisor relationship

Before the trade even exists, Fidelity needs to know things about the relationship.

Conceptually:

**CLIENT**

Paul

↓

**ACCOUNT**

12345

↓

**ADVISOR/REP BUSINESS RELATIONSHIP**

Mary / `ABC`

At this point, the Rep Code could already exist as reference/account-related data.

Remember:

`ABC` isn't Paul's identifier.

And it isn't necessarily just Mary's employee identifier.

It's the **business identifier associated with the relevant rep/advisor relationship or structure**.

---

# 3. Step 2 — Paul wants to buy IBM

Paul tells Mary:

> Buy 100 IBM.

That is still a **client instruction**, not necessarily yet the final electronic order.

Information needs to be captured.

Conceptually:

|Attribute|Value|
|---|---|
|Account|12345|
|Security|IBM|
|Side|BUY|
|Quantity|100|
|Order Type|Market|
|Rep Code|ABC|

There could be many additional fields and controls in a real brokerage environment.

But these are enough for our model.

---

# 4. Before trading: can Paul actually do this?

The firm doesn't necessarily send the order straight to the market.

Various validations may occur.

For example:

**Does account 12345 exist?**

**Is the account active?**

**Does Paul have authority over it?**

**Is IBM a valid security?**

**Is the account allowed to trade this security?**

**Does the order meet applicable account/business controls?**

And relevant to our project:

> **Is `ABC` a valid Rep Code for this business context?**

This introduces an important concept:

# Pre-trade validation

These are checks performed before an order proceeds into execution.

---

# 5. What is an OMS?

Now introduce an acronym you're likely to encounter:

## OMS — Order Management System

An OMS manages orders through their lifecycle.

Conceptually:

**Order entered**

↓

**OMS**

↓

validate

↓

track status

↓

route

↓

receive execution information

↓

update order

An OMS might know:

**Order ID:** `ORD9001`

**Account:** `12345`

**Security:** `IBM`

**Quantity:** `100`

**Side:** `BUY`

**Rep Code:** `ABC`

Again, that's illustrative—not Fidelity's actual schema.

---

# 6. Why is an Order ID different from Account ID?

This is the same identifier discipline we've been developing.

**Client ID**

identifies Paul.

**Account ID**

identifies Paul's brokerage account.

**Rep Code**

identifies the relevant rep/business relationship.

**Security identifier**

identifies IBM.

**Order ID**

identifies this particular order.

Later:

**Execution ID**

identifies an execution.

**Trade ID**

identifies a trade record/transaction.

Different business objects need different identifiers.

This is basic, but it's extremely important for systems analysis.

---

# 7. Step 3 — Order routing

The OMS now has an order:

> BUY 100 IBM

It needs to reach somewhere capable of executing it.

Conceptually:

**Advisor / Order Entry**

↓

**OMS**

↓

**Routing**

↓

**Execution Venue**

An execution venue might be an exchange or another market venue/mechanism capable of executing the order.

We don't need market-microstructure details yet.

For now:

> **Routing = determining where/how the order gets sent for potential execution.**

---

# 8. Does Rep Code go to the market?

Here's where I want you to develop an important BA habit.

You might ask me:

> Does `ABC` actually get transmitted to the exchange?

My answer is:

**Don't assume it does.**

The Fidelity JD doesn't tell us.

And that's exactly what a BA would investigate.

Maybe:

**Order Entry → ABC**

but:

**OMS → Exchange message → no ABC**

while another downstream system receives it.

Or perhaps some relevant field derived from it travels elsewhere.

We don't know.

So your BA question becomes:

> **At what points in the order lifecycle is Rep Code present, required, transformed, derived, or removed?**

That's **data lineage**.

---

# 9. Step 4 — Execution

Suppose the market finds sellers.

Your 100-share order might execute:

**40 IBM @ $250.00**

and:

**60 IBM @ $250.05**

Now remember Session 1:

### One order

`ORD9001`

### Two executions

`EXEC01 = 40 IBM @ $250.00`

`EXEC02 = 60 IBM @ $250.05`

The order is now completely filled:

40 + 60 = 100.

---

# 10. Order status

The OMS needs to track what's happening.

For example:

**NEW**

↓

**ROUTED**

↓

**PARTIALLY FILLED**

↓

**FILLED**

Or perhaps:

**CANCELED**

**REJECTED**

etc.

Exact status terminology varies by platform.

The conceptual point is that an order is a **stateful business object**.

It changes state as it progresses.

That's relevant to BA work because requirements frequently contain rules such as:

> If X happens while order status is Y, system shall do Z.

---

# 11. Execution becomes trade information

Once execution occurs, the firm has actual transaction information.

Before execution:

> Paul **wants** 100 IBM.

After execution:

> Paul **bought** 40 IBM at X and 60 IBM at Y.

Now post-trade systems need that information.

Conceptually:

**OMS / Execution**

↓

**Trade processing**

↓

**Clearing**

↓

**Settlement**

And other consumers could potentially include:

**Operations**

**Supervision**

**Positions**

**Reporting**

**Books and records**

etc.

Now we're getting into the area described by the Fidelity JD.

---

# 12. Pre-trade vs. post-trade

This distinction is useful.

### Pre-trade

Everything leading toward execution.

For our simplified model:

**Client instruction**

↓

**Order entry**

↓

**validation**

↓

**OMS**

↓

**routing**

### Trade / execution

The transaction occurs.

### Post-trade

Everything necessary after execution:

**trade processing**

↓

**clearing**

↓

**settlement**

↓

**positions / records / reporting / other downstream processing**

This is simplified, but it's a useful interview mental model.

---

# 13. Step 5 — Clearing

We covered the basic definition already.

After trades occur, the financial ecosystem needs to establish obligations.

Conceptually:

**Paul's side**

owes cash.

**Seller's side**

owes IBM shares.

Clearing helps determine and prepare those obligations for settlement.

You gave a good definition last session:

> **What does everyone owe?**

Keep that.

---

# 14. Step 6 — Settlement

Now the obligations are completed.

Conceptually:

**Buyer's side**

receives IBM.

**Seller's side**

receives cash.

The transaction is settled.

For most U.S. securities transactions today there are specific settlement conventions, but we don't need to memorize settlement timing yet.

The business concept is enough:

> **Settlement completes the exchange resulting from the trade.**

---

# 15. Step 7 — Position

Now introduce another important financial-data concept.

Before the trade:

Paul's account may contain:

`IBM position = 0`

After settlement/process updates:

`IBM position = 100`

A **position** represents the quantity/exposure held in a security.

So:

**Trade**

changes:

**Position**

Conceptually:

|Account|Security|Position|
|---|---|--:|
|12345|IBM|100|

This should already resonate with your financial-data background.

---

# 16. Books and records

The firm also has to maintain records of what happened.

Conceptually:

**Who?**

Paul/account 12345

**What?**

Bought IBM

**How much?**

100 shares

**When?**

transaction timestamp/date

**At what prices?**

execution prices

**Which business relationship?**

potentially relevant advisor/rep information

**What happened afterward?**

clearing/settlement status

This is one reason identifier integrity becomes important.

Imagine the trade record says:

`REP_CODE = ABC`

but nobody can determine what `ABC` meant at the time of the transaction.

That's a problem.

---

# 17. Supervisory workflow

Now another phrase directly from the Fidelity JD:

> **supervisory workflows**

Brokerage activity occurs within a regulated/supervised environment.

Certain activities may need to be:

monitored,

reviewed,

approved,

flagged,

or investigated.

We aren't learning the specific rules yet—that's Session 6.

For now, understand the architectural consequence:

**Trading activity**

↓

may feed

↓

**Supervisory systems/workflows**

And those systems may need to know:

> Which representative/business relationship was associated with this activity?

Therefore:

**Rep Code**

may matter to supervision as well as trading.

---

# 18. Reporting

Another downstream consumer:

**Reporting**

Imagine management wants:

> Show trading activity by advisor team.

or:

> Show activity associated with Rep Code ABC.

or:

> Show exceptions by representative.

Reporting may depend upon Rep Code.

Therefore:

**Rep Code isn't merely transactional data.**

It can become an important **reporting dimension**.

That's why one or two of Fidelity's other BA resources may focus specifically on reporting; the JD lists reporting-focused BAs separately from your trading-focused allocation.

---

# 19. Now introduce systems of record

Let's say the trading system receives:

`REP_CODE = ABC`

Should the trading system decide what ABC means?

Probably not if some other authoritative system owns Rep Code reference data.

Conceptually:

**REP SOR**

`ABC = Mary/Team/Relationship X`

↓

**Account system**

↓

**OMS**

↓

**Trading**

↓

**Post-trade**

↓

**Reporting / supervision / operations**

The Rep Code can travel.

But the authoritative definition originates elsewhere.

That's the difference between:

**system containing data**

and:

**system owning authoritative data**.

---

# 20. Now make it a four-character code

Everything is working.

Then Fidelity introduces:

`ABC1`

Remember what the JD tells us: Fidelity wants to support four-character codes while maintaining compatibility with legacy systems through centralized translation.

Now walk the lifecycle again.

**Rep SOR**

`ABC1`

↓

**Account**

Can it store 4?

↓

**Order Entry**

Can UI accept 4?

↓

**OMS**

Can database store 4?

↓

**Business rules**

Do they assume length = 3?

↓

**Trading interfaces**

Can they transmit 4?

↓

**Legacy trading system**

Can it consume 4?

↓

**Clearing**

What representation does it expect?

↓

**Supervision**

Can it identify `ABC1`?

↓

**Reporting**

Can it report `ABC1` correctly?

Suddenly:

> **"Change Rep Code from 3 to 4 characters."**

is an enterprise impact-analysis problem.

---

# 21. Let's introduce a failure

Suppose:

**SOR**

`ABC1`

↓

**Account**

`ABC1`

↓

**OMS**

`ABC1`

↓

**Legacy Trading System**

only allows `CHAR(3)`.

What could happen?

### Failure A — rejection

> Invalid Rep Code.

Order processing fails.

### Failure B — truncation

`ABC1 → ABC`

Much more dangerous because the transaction might continue with **incorrect data**.

### Failure C — missing value

System drops the field.

### Failure D — incorrect translation

`ABC1 → XYZ`

when correct mapping should have been:

`ABC1 → DEF`

The trade may execute, but now downstream business attribution is wrong.

That distinction matters enormously:

> **A technical failure is not always the worst outcome. A successful transaction carrying incorrect business data can be worse.**

That's very relevant to BA testing.

---

# 22. Central translation enters the flow

Fidelity's stated approach becomes easier to understand now.

Suppose:

**Modern Rep Code**

`ABC1`

↓

**Central Translation**

`ABC1 → XYZ`

↓

**Legacy Trading**

`XYZ`

↓

later perhaps some downstream process needs to understand:

`XYZ → ABC1`

Conceptually, this allows:

**new-world systems**

and

**old-world systems**

to coexist during modernization.

Again, the JD says **centralized translation approach**; it does not tell us the implementation architecture.

---

# 23. Your Trading BA job begins to emerge

Imagine your manager says:

> Paul, you're responsible for Trading impact analysis for Rep Code Expansion.

You don't necessarily write code.

You start investigating.

### Business

Which trading workflows use Rep Code?

### Data

Where does Rep Code originate?

### Systems

Which trading applications contain it?

### Database

Which tables/columns contain it?

### Interfaces

Which APIs/messages/files transmit it?

### Business rules

Which rules depend upon it?

### Downstream

Who consumes the trading output?

### Legacy

Which applications can't handle four characters?

### Translation

Where must translation occur?

### Error handling

What happens if mapping doesn't exist?

### Historical data

How do we interpret old trades?

### Testing

How do we prove both old and new Rep Codes work?

That's why the JD wants someone who can:

> **work through complex systems and dependencies**

and:

> **go deep technically and then translate findings for business stakeholders.**

---

# 24. Example of “go deep technically → translate to business”

Suppose engineering tells you:

> `TRD_ORDER.REP_CD` is `CHAR(3)`, outbound FIX mapping populates field X from that column, and the downstream consumer rejects payloads when field length exceeds three.

You investigate.

Then you explain to a business stakeholder:

> The current trading platform can only carry the existing three-character Rep Code. Without either modifying that system or translating the new code before it reaches the interface, orders associated with four-character Rep Codes could fail or carry incorrect advisor attribution.

That's what the JD means.

You're capable of understanding:

**database → mapping → interface → validation**

but communicate:

**business consequence**.

That is the business/technology intersection you're targeting.

---

# 25. Your FRBNY parallel

This is where your experience becomes relevant without pretending MRPrice and Rep Codes are the same domain.

Your resume says you supported an Oracle-based data-distribution model, mapped legacy relational pricing schemas to REST/JSON payloads, validated legacy Oracle data against API JSON payloads, and supported downstream consumers.

Conceptually:

### FRBNY

**Legacy source/data model**

↓

**mapping/transformation**

↓

**new REST representation**

↓

**downstream consumer**

↓

**validate equivalence**

### Fidelity Rep Code

**new Rep Code representation**

↓

**mapping/translation**

↓

**legacy/modern interfaces**

↓

**downstream consumers**

↓

**validate correct business meaning**

Not the same systems.

Not the same data.

But very transferable **systems-analysis thinking**.

---

# Session 3 mental model

Keep this:

**CLIENT**

↓

**ADVISOR / REP RELATIONSHIP**

↓

**ACCOUNT**

↓

**ORDER ENTRY**

↓

**PRE-TRADE VALIDATION**

↓

**OMS**

↓

**ROUTING**

↓

**EXECUTION**

↓

**TRADE**

↓

**CLEARING**

↓

**SETTLEMENT**

↓

**POSITIONS / BOOKS & RECORDS / REPORTING**

And potentially throughout that ecosystem:

**REP CODE**

↓

**business attribution / identification**

while:

**REP CODE SOR**

maintains the authoritative meaning.

---

# Knowledge check

Same approach: answer these **in your own words**. Don't look anything up.

**Q1.** What is the difference between an **order**, an **execution**, and a **trade**?

**Q2.** What does an **OMS** do?

**Q3.** If the Rep Code exists on an order inside Fidelity, should we automatically assume that Fidelity sends the Rep Code to the stock exchange? Why or why not?

**Q4.** What's the difference between **pre-trade** and **post-trade** processing?

**Q5.** Suppose `ABC1` reaches a legacy trading system whose database field is `CHAR(3)`. Why could silently turning it into `ABC` potentially be worse than rejecting it?

**Q6.** Engineering tells you: _"Our trading database column only supports three characters."_ As the BA, translate that technical finding into a **business impact statement** that a Product Owner could understand.

**Q7 — most important.** Fidelity tells you:

> "Paul, determine the trading impact of four-character Rep Codes."

What's the **first thing you would do**? Don't give me 20 steps. Tell me how you would begin the discovery.

Once we tighten these up, we'll move to **Session 4 — Systems, Data & Data Lineage**, where we're going to start drawing the kind of end-to-end system/data picture you could actually use on this Fidelity project.


---


This is exactly why we're doing the domain training **before** trying to manufacture interview answers. Q3, Q4, Q6 and Q7 exposed concepts that aren't solid yet. That's useful. We should fix them rather than move on prematurely.

## Q1 — Order → Execution → Trade

You said:

> order gets executed resulting in a trade

**Correct, but let's make the middle piece explicit.**

**Order** = instruction.

> Buy 100 IBM.

**Execution** = some or all of that order is actually filled.

> 40 IBM @ $250  
> 60 IBM @ $250.05

**Trade** = transaction resulting from execution.

The key thing you were missing is that **one order can have multiple executions**.

Keep:

> **Order = intention/instruction. Execution = fill. Trade = resulting transaction.**

---

# Q2 — OMS

You said:

> Order Management system receives orders and routes them to a place where they can be executed

**Good.**

Add one thing:

An OMS doesn't merely route an order. It **manages/tracks the order through its lifecycle**.

Think:

**Receive**

↓

**Validate**

↓

**Track**

↓

**Route**

↓

**Receive execution information**

↓

**Update order status**

For example:

`NEW → ROUTED → PARTIALLY FILLED → FILLED`

So a good basic definition is:

> **An OMS receives and manages orders through their lifecycle, including validation, routing, status tracking and processing execution information.**

That's plenty for you right now.

---

# Q3 — Does Rep Code get sent to the exchange?

You put:

> ?

Good. Because the correct answer is:

> **We don't know.**

And that's actually an important **BA answer**.

We know Rep Code may exist on an order inside Fidelity.

That does **not** automatically mean:

**Fidelity OMS → Exchange carries Rep Code**

Maybe it does.

Maybe it doesn't.

Maybe some transformed/derived identifier goes out.

Maybe Rep Code stays entirely within Fidelity and downstream internal systems.

The JD doesn't tell us.

Therefore, as the Trading BA:

> **I would trace the Rep Code through the order flow and identify which systems and interfaces actually consume or transmit it rather than assuming that because it exists on the order it goes to every downstream system.**

This is the beginning of **data lineage**.

### Important BA habit

You're going to encounter this constantly:

> "System A has field X, therefore System B must get X."

**No. Verify it.**

That's exactly what this JD's discovery requirement is about.

---

# Q4 — Pre-trade vs post-trade

You said:

> validation and reporting?

You've got **examples** of each, but not the distinction yet.

Think of the **execution** as the dividing line.

### BEFORE EXECUTION = PRE-TRADE

**Client instruction**

↓

**Order entry**

↓

**Validation**

↓

**OMS**

↓

**Routing**

↓

### EXECUTION

💥 Trade happens

↓

### AFTER EXECUTION = POST-TRADE

**Trade processing**

↓

**Clearing**

↓

**Settlement**

↓

**Positions**

↓

**Books & records**

↓

**Reporting / other downstream processing**

So:

> **Pre-trade = processes leading up to execution.**

> **Post-trade = processes necessary after execution to process, clear, settle, record and report the resulting transaction.**

That's the mental model.

---

# Q5 — Silent truncation

You said:

> processing incorrect data without failure introduces inconsistencies that are dangerous

**Exactly.**

This is a strong answer.

Let's see why.

Correct:

`ABC1 = Smith Team`

Legacy system only supports three characters.

Instead of rejecting:

`ABC1`

it silently does:

`ABC`

Now everything looks successful.

**Order accepted.**

**Trade executes.**

**Processing continues.**

But perhaps:

`ABC = completely different business relationship`

Now you've potentially created a successful financial transaction carrying **incorrect business attribution**.

That's potentially much harder to detect than:

> ERROR: INVALID REP CODE.

This is a useful BA/testing principle:

> **Successful processing does not necessarily mean correct processing.**

Remember that phrase.

---

# Q6 — Translate technical finding into business impact

Engineering says:

> "Our trading database column only supports three characters."

You answered `??`, so let's build it.

### Step 1 — Technical fact

`REP_CODE CHAR(3)`

### Step 2 — New business requirement

Fidelity needs:

`ABCD`

### Step 3 — Technical consequence

Existing field can't represent `ABCD`.

### Step 4 — Business consequence

Orders associated with new four-character Rep Codes may:

**fail**

or

**carry incorrect Rep Code information**

### Step 5 — Business-language answer

You tell the Product Owner:

> **The current trading platform cannot represent the new four-character Rep Codes. Unless the system is modified or the code is translated before reaching it, orders associated with the new codes could be rejected or processed with incorrect advisor/business attribution.**

That's what this JD means by:

> **"Comfortable going deep technically and then translating findings for business stakeholders."**

You're not telling the Product Owner:

> CHAR(3) needs VARCHAR(4).

You're telling them:

> **Here's how this technical limitation threatens the business process.**

That's an important distinction.

---

# Q7 — Where do you start discovery?

This is probably the **most important question in the entire exercise so far**.

Fidelity says:

> "Paul, determine the trading impact of four-character Rep Codes."

Your instinct might be:

> I'll gather requirements.

But **from whom?**

Nobody necessarily knows the complete requirement.

That's specifically why Fidelity says they want BAs who independently discover information rather than waiting for requirements to be handed to them.

So start with:

> **First I would understand the current-state Rep Code flow through the trading environment—where the Rep Code originates, which trading systems consume it, how it moves between those systems, and which business processes depend on it.**

That's your starting point.

Notice what you **didn't** do:

❌ Immediately write Jira stories.

❌ Immediately design the four-character solution.

❌ Ask engineering to change every field to four characters.

❌ Assume you know which systems are impacted.

You first understand:

# AS-IS

And this connects directly to BA work you've done before.

---

# How would you actually discover the AS-IS?

Now imagine Monday morning at Fidelity.

Your manager says:

> "Paul, you're covering Trading. Figure out Rep Code impact."

You need people.

Perhaps you start with:

**Product Owner / business SME**

> How does Trading use Rep Code today?

Then:

**Trading application SME**

> Which applications touch it?

Then:

**Data/DB SME**

> Where is it stored?

Then:

**Integration/API SME**

> Where is it transmitted?

Then:

**Operations**

> What happens when it's wrong?

And every answer can reveal another dependency.

For example:

Trading SME:

> "We receive Rep Code from Account Services."

You:

> **"Who owns that interface?"**

Interface SME:

> "We get it through Order Gateway."

You:

> **"Does Order Gateway modify it?"**

Engineer:

> "No, but we translate it before sending trades to Legacy Clearing."

🚨

Now you've discovered another system.

You:

> **"Who owns Legacy Clearing?"**

And off you go.

That is the **networking/discovery** behavior Fidelity explicitly called out.

---

# You're building a map

At first perhaps you know only:

**???**

↓

**Trading**

↓

**???**

After discovery:

**Rep SOR**

↓

**Account System**

↓

**Order Entry**

↓

**OMS**

↓

**Trading**

↓

**Translation**

↓

**Legacy Clearing**

↓

**Operations**

↓

**Reporting**

Now you can ask each system owner:

> Does your system contain Rep Code?

> What format?

> Where does it come from?

> Where does it go?

> Does your system transform it?

> What business rules use it?

> Does anything assume three characters?

That's **impact analysis**.

---

# And here's an important connection to your previous work

You've actually done pieces of this behavior.

At FRBNY, you weren't sitting around waiting for somebody to hand you every technical answer. You worked across business, infrastructure, architecture, development, QA and operations around a financial-data platform and its downstream consumers. Your resume reflects that environment.

Later, when we prepare your interview answer, we can combine the **methodology we're learning now** with specific examples of what you actually did.

But right now I don't want you memorizing the interview answer.

I want the thought process to become natural:

> **I don't know the impact yet. First I need to understand the As-Is and trace the data through the ecosystem.**

That's the BA mindset Fidelity appears to be asking for.

---

# One thing before Session 4

I don't think we should move on quite yet. I want to make sure these two ideas clicked.

No need to answer all seven questions again.

Just answer these **two**:

### A.

Engineering tells you:

> `REP_CODE` in Trading System X is `CHAR(3)`.

Explain to a **business Product Owner** why that's a problem for Rep Code Expansion. Don't talk to them like a database engineer.

### B.

Your manager says:

> "Paul, determine which trading systems will be affected by four-character Rep Codes."

You don't know the systems yet.

**What do you do first?**

Answer those two in your own words. Once those are solid, we'll move into **Session 4 — Systems, Data & Data Lineage**.