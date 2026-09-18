---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 3 — Qs
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
one advisor-assisted stock order end-to-end and keep asking one question: Where might the Rep Code matter at this point?

---

# Session 3 — Trading Lifecycle 101


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