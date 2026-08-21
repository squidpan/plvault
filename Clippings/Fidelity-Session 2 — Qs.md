---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 2 — Qs
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

---

# Session 2 — Rep Codes 101



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


