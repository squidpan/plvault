---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 1--Brokerage and Wealth Management 101
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-21
description: The goal is to understand who the participants are, what the major business objects are, and what happens when somebody buys a security. The Fidelity JD tells us that Rep Code Expansion ultimately touches advisor structures, supervisory workflows, trading, clearing, operations, and integrations, so this foundation matters.
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---
The goal is to understand who the participants are, what the major business objects are, and what happens when somebody buys a security. The Fidelity JD tells us that Rep Code Expansion ultimately touches advisor structures, supervisory workflows, trading, clearing, operations, and integrations, so this foundation matters.




---

# Session 1 — Brokerage & Wealth Management 101

We'll build this from **zero**, and I'll keep bringing it back to the Fidelity Rep Code project so the terminology doesn't become abstract.

For this session, don't worry about SQL, APIs, Oracle, or implementation details. The goal is to understand **who the participants are, what the major business objects are, and what happens when somebody buys a security.**

The Fidelity JD tells us that Rep Code Expansion ultimately touches **advisor structures, supervisory workflows, trading, clearing, operations, and integrations**, so this foundation matters.

---

## 1. Start with you and $10,000

Suppose you have $10,000 and want to buy 20 shares of Apple. You can't normally walk directly onto a stock exchange and say:

> "Hi, I'd like 20 shares of Apple."

You need access to the securities marketplace.

So you open an account with a financial-services company such as Fidelity.

At the simplest level:

**You**

↓

**Your brokerage account**

↓

**Brokerage firm / broker-dealer**

↓

**Market**

↓

**AAPL**

But that's only the visible part.

Behind that transaction is a collection of people, accounts, identifiers, systems, business rules and organizations.

That's the world we're going to unpack.

---

# 2. First concept: Client / Investor

That's the easiest one.

**You are the client/investor.** You own assets and want financial services.

You might be:

- an individual investor
- a wealthy individual  
- a trust
- a corporation
- a pension fund
- another institution

For our example: **Paul → investor/client** You have $10,000 that you want to invest.

But Fidelity doesn't just throw your money into one giant bucket labeled "Paul."

It establishes an **account**.

---

# 3. Client ≠ Account

This distinction is extremely important.

One **client** can have **multiple accounts**.

For example:

**Paul**

→ Individual Brokerage Account  
→ Traditional IRA  
→ Roth IRA  
→ Joint Brokerage Account

Therefore:

**Client ID**

is not necessarily the same thing as:

**Account ID**

Imagine:

| Client | Account | Type      |
| ------ | ------- | --------- |
| Paul   | 12345   | Brokerage |
| Paul   | 67890   | IRA       |
| Paul   | 24680   | Joint     |

One person. Three accounts.

And each account can potentially have different:

- owners
- tax treatment
- investment permissions
- restrictions
- advisors
- trading permissions
- assets
- reporting requirements

Already you can see why identifiers matter.

---

# 4. What is a brokerage account?

A brokerage account is essentially the business/legal container through which you hold and trade investments.

Your account might contain:

**Cash**

$10,000

and later:

**Securities**

20 AAPL  
10 MSFT  
50 XYZ bond

The brokerage firm's systems maintain records describing things such as:

> Account 12345 belongs to Paul.

> Account 12345 owns 20 shares of AAPL.

> Account 12345 has $3,500 available cash.

> Account 12345 is permitted to perform certain types of trades.

Now we need an organization capable of operating that brokerage business.

---

# 5. Broker-dealer

A **broker-dealer** is a regulated financial firm involved in securities transactions.

The name contains two concepts:

### Broker

A broker facilitates transactions **for customers**.

Think:

> "My customer wants to buy this security. I facilitate that transaction."

### Dealer

A dealer can transact **for its own account**.

Think:

> "The firm itself is buying or selling securities."

Hence:

**broker + dealer = broker-dealer**

Large financial-services organizations can have multiple legal entities performing different functions, so don't assume that the consumer-facing brand name and the particular regulated broker-dealer legal entity are always identical.

For interview purposes, the important idea is:

**Broker-dealer = regulated securities intermediary.**

---

# 6. Where does the Financial Advisor enter?

Now let's change the example. Instead of deciding yourself:

> "I want 20 shares of Apple."

suppose you're working with a financial advisor.

You might say:

> "I have $500,000. I'm retiring soon. How should this money be invested?"

Now we have another actor:

**Client**

↓

**Financial Advisor**

↓

**Brokerage relationship/accounts**

The advisor may help the client with things such as:

- investment strategy
    
- asset allocation
    
- portfolio decisions
    
- financial planning
    
- securities transactions
    
- account servicing
    

This brings us much closer to the Fidelity project.

---

# 7. Financial Advisor vs Registered Representative

These terms can overlap in real organizations, but they aren't automatically interchangeable.

For our foundation, think about them this way.

### Financial Advisor

A relatively broad business/client-facing description.

> Person who helps clients manage investments and financial decisions.

### Registered Representative

A more specific securities-industry concept.

A registered representative is an individual registered to conduct particular securities business through a broker-dealer, subject to the appropriate registration and supervision.

You will also hear:

**Registered Rep**

or simply:

**Rep**

And now you should recognize an important word:

> **Rep Code**

We're getting close.

---

# 8. Why does the firm need to identify the rep?

Suppose Fidelity has thousands of representatives.

A transaction happens.

The firm may need to know:

> Which client?

> Which account?

> Which representative/advisor?

> Which office/team?

> Who handled the order?

> Who has supervisory responsibility?

> What compensation arrangement applies?

> Which business organization owns the relationship?

You can't reliably represent all of that by someone's name.

Imagine three people named:

**John Smith**

Names aren't good database identifiers.

So financial systems use **identifiers**.

A simplified example:

|Rep|Rep Code|
|---|---|
|John Smith|ABC|
|Mary Jones|DEF|
|Robert Lee|XYZ|

Now:

**ABC**

can travel through systems much more reliably than:

**John Smith**

This is our first conceptual introduction to the **Rep Code**.

We're deliberately keeping it simple because Session 2 is entirely about rep codes.

---

# 9. Client → Advisor → Account

We can now build a richer model.

Imagine:

**Paul**

is serviced by:

**Mary Jones**

whose rep code is:

**DEF**

and Paul owns:

**Brokerage Account 12345**

Conceptually:

**Client: Paul**

↓

**Advisor: Mary Jones**

↓

**Rep Code: DEF**

↓

**Account: 12345**

Now suppose Paul wants to buy Apple.

---

# 10. What is an Order?

Paul tells Mary:

> "Buy 20 shares of Apple."

That instruction becomes an **order**.

An order is **not yet a trade**.

That's an important distinction.

### Order

An instruction/request to buy or sell something.

For example:

**BUY 20 AAPL**

An order could contain information such as:

|Field|Example|
|---|---|
|Account|12345|
|Side|BUY|
|Security|AAPL|
|Quantity|20|
|Order Type|Market|
|Rep Code|DEF|

Don't treat this as Fidelity's actual schema. We're constructing a conceptual model.

But notice something.

**DEF has now potentially moved from advisor/account context into trading context.**

That's why your Rep Code project isn't simply an HR directory project.

---

# 11. Order ≠ Execution ≠ Trade

These three concepts are important.

### Order

> "Buy 20 shares of AAPL."

That's the instruction.

### Execution

The market actually matches some or all of your order with somebody willing to sell.

For example:

> 20 AAPL executed at $225.

### Trade

The resulting transaction created by that execution.

So conceptually:

**Order**

↓

**Execution**

↓

**Trade**

This can become considerably more complicated because an order can potentially have multiple executions.

For example:

> Buy 1,000 shares.

Perhaps:

400 execute at $225.00  
300 execute at $225.02  
300 execute at $225.05

One order.

Multiple executions.

But don't worry about that complexity yet.

---

# 12. What happens after the trade?

Suppose your order executes.

Your screen may quickly show that you bought Apple.

But the financial system isn't finished.

The transaction must go through post-trade processing.

At a high level:

**Order**

↓

**Execution**

↓

**Trade**

↓

**Clearing**

↓

**Settlement**

These last two words matter.

---

# 13. Clearing

Clearing is essentially the process of determining and preparing the obligations created by trades so they can be completed correctly.

Among other things, the ecosystem has to establish:

> Who owes securities?

> Who owes money?

> How much?

> To whom?

Think of clearing as:

**"Figure out and prepare what everyone owes."**

That's simplified, but useful for now.

---

# 14. Settlement

Settlement is when the obligations are actually fulfilled.

Conceptually:

**Buyer receives securities**

and

**Seller receives money**

So:

### Clearing

Determine/prepare the obligations.

### Settlement

Complete the exchange.

That's enough distinction for Session 1.

---

# 15. Put the whole lifecycle together

We now have:

**CLIENT**

Paul

↓

**FINANCIAL ADVISOR / REGISTERED REP**

Mary Jones

↓

**REP CODE**

DEF

↓

**ACCOUNT**

12345

↓

**ORDER**

Buy 20 AAPL

↓

**EXECUTION**

20 AAPL @ market price

↓

**TRADE**

Transaction created

↓

**CLEARING**

Obligations processed

↓

**SETTLEMENT**

Cash/securities exchanged

This is the first mental model I want you to retain.

---

# 16. Where Fidelity's Rep Code problem starts becoming interesting

Now imagine **DEF** appears throughout that ecosystem.

Perhaps it exists in:

**Advisor system**

↓

**Account system**

↓

**Order system**

↓

**Trading system**

↓

**Clearing**

↓

**Supervisory system**

↓

**Reporting**

↓

**External transmission**

Again, that's a conceptual illustration—not a claim about Fidelity's actual architecture.

Now Fidelity says:

> We're expanding three-character Rep Codes to four characters.

Old:

**DEF**

New:

**DEF1**

Immediately, the BA should ask:

> Which systems know about DEF?

> Which systems store DEF?

> Which systems transmit DEF?

> Which databases define the field as three characters?

> Which applications validate exactly three characters?

> Which reports display it?

> Which external vendors receive it?

> Which business rules depend upon it?

> Which historical trades contain DEF?

> Which systems can accept DEF1?

> Which systems cannot?

That is why the actual JD says the initiative spans **core data models, supervisory workflows, trading, clearing and operational platforms**, while maintaining legacy compatibility through centralized translation.

And that's why **data lineage** is such an important requirement for your position.

But we're not going there yet.

---

# 17. One more distinction: Brokerage vs Wealth Management

You'll hear both.

### Brokerage

More transaction/account oriented.

> Hold securities.

> Buy/sell securities.

> Process orders and trades.

You might make your own investment decisions.

### Wealth Management

Broader relationship/advisory model.

It may encompass:

- financial planning
    
- investment advice
    
- portfolio management
    
- retirement planning
    
- tax-aware strategies
    
- estate considerations
    
- advisor relationships
    

There's overlap.

For our Fidelity project, the important connection is that **advisor relationships eventually interact with brokerage/trading infrastructure**.

That's one reason something called a "Rep Code" can wind up affecting trading systems.

---

# 18. Connect this to what you already know

There is actually a useful bridge to your previous experience.

At FRBNY, you dealt with financial data flowing through systems to downstream consumers. Your resume describes Oracle-based master/consumer-specific views and mapping legacy relational pricing data into REST/JSON structures.

At Fidelity, you previously worked with reference data, security-master data, golden-copy management, normalization and downstream distribution to trading and other platforms.

Don't equate **security master** with **rep master**—they're different business domains.

But the architectural idea should already feel familiar:

**Authoritative data**

↓

**identifier**

↓

**business attributes**

↓

**distribution**

↓

**multiple downstream consumers**

↓

**each consumer depends upon the data being correct**

That's going to become an important bridge later.

---

# Session 1 — What I want you to know

Don't memorize paragraphs. Make sure these ideas make sense:

1. **Client and account are different things.**
    
2. One client can have multiple accounts.
    
3. A **broker-dealer** facilitates securities transactions and operates in a regulated environment.
    
4. A **financial advisor** helps clients with financial/investment decisions.
    
5. A **registered representative/rep** is a registered securities professional associated with a broker-dealer.
    
6. A **Rep Code** is an identifier associated with the rep/advisor/business relationship and can matter to downstream business processes.
    
7. **Order ≠ execution ≠ trade.**
    
8. After execution come **clearing and settlement**.
    
9. Advisor/rep information can therefore travel into systems far beyond the advisor-facing application.
    
10. Changing an identifier from **3 → 4 characters** can consequently affect an enormous system ecosystem.
    

### The mental picture

Keep this one:

**Client → Advisor/Rep → Rep Code → Account → Order → Execution → Trade → Clearing → Settlement**

That's our foundation.

---

## Quick knowledge check

Before Session 2, answer these in your own words. Don't research them and don't worry about getting them perfect.

### **Q1.** What's the difference between a client and an account?

a client **doesn't necessarily need a financial advisor**. A self-directed Fidelity customer could have multiple brokerage/retirement accounts without working through an advisor.

> **Client = person/entity having the relationship with the firm. Account = a particular financial/legal container belonging to that client. One client can have multiple accounts.**

### **Q2.** What's the difference between an order and a trade?

> "Buy me 100 shares of IBM."

That's the **order**.

Suppose it gets filled:

> 20 IBM @ $250  
> 30 IBM @ $250.05  
> 50 IBM @ $250.10

Those are **executions/fills** of the order.

Those executions result in trade transactions.

**Order = instruction**
**Execution = fulfillment/matching of that instruction**
**Trade = resulting transaction**

And importantly, one order doesn't necessarily mean one execution.

**Q3.** Why might a financial firm use a Rep Code instead of simply storing the advisor's name?

**don't think of the Rep Code as an identifier for all of those things.**

At the basic level:

**Client ID → identifies client**
**Account ID → identifies account**
**Rep Code → identifies/represents the relevant representative/advisor relationship or business assignment**

The systems can then **relate** those things. For example:

**Account 12345 → assigned Rep Code DEF**

and:

**Rep Code DEF → Mary Jones / particular rep relationship**

So a system could determine:

> Account 12345 is associated with DEF.

and use reference data to determine what **DEF means**.

This distinction is going to become extremely important when we learn **systems of record and reference data**.

Also, Fidelity's JD tells us its rep codes have evolved beyond simply identifying individual advisors: clients use them for **individual advisors, teams, compensation structures and order-handling roles**. That's part of what has made the problem more complicated.

### **Q4.** Why could changing a Rep Code from three characters to four affect a trading system even though the code identifies an advisor rather than a security?

Suppose a legacy trading system was designed in 1995 to accept:

**REP_CODE = 3 characters**

Then Fidelity sends:

**ABC1**

The legacy system might:

reject it, truncate it to `ABC`, fail validation, corrupt/misinterpret it, 
or fail to process the message.

Meanwhile another modern system may happily accept `ABC1`. 

So the fundamental problem is:

**New 4-character world**

↓

`ABC1`

↓

**Legacy system only understands 3 characters**

💥

And that's why this phrase from the JD is so important:

> **"maintaining compatibility with legacy systems through a centralized translation approach."**

Eventually we're going to understand exactly what that could mean architecturally.


### **Q5.** What's the basic difference between clearing and settlement?

 but be careful with **who gets paid**. Suppose:

**Paul 
buys 100 IBM from Jane.**

Conceptually, at settlement:

**Paul/buyer's side → receives the securities**
**Jane/seller's side → receives the cash**

The broker isn't necessarily the seller receiving the purchase proceeds.

So retain:

> **Clearing = determine/prepare who owes what.**

> **Settlement = fulfill those obligations by completing delivery of securities and payment.**

That's enough for now.



---

You're getting the model. **Q1, Q2, and Q5 are essentially right. Q3 needs one important correction, and Q4 needs a slightly different emphasis.** Those corrections are useful because they lead directly into Rep Codes.


---

### Q1 — Client vs. account ✅

Your answer:

> client is the customer. a client can have multiple accounts thru a financial advisor at a financial services firm

Correct.

One refinement: a client **doesn't necessarily need a financial advisor**. A self-directed Fidelity customer could have multiple brokerage/retirement accounts without working through an advisor.

So I'd retain:

> **Client = person/entity having the relationship with the firm. Account = a particular financial/legal container belonging to that client. One client can have multiple accounts.**

---

### Q2 — Order vs. trade ✅

You have it.

> "Buy me 100 shares of IBM."

That's the **order**.

Suppose it gets filled:

> 20 IBM @ $250  
> 30 IBM @ $250.05  
> 50 IBM @ $250.10

Those are **executions/fills** of the order.

Those executions result in trade transactions.

The important thing you already understood is:

**Order = instruction**

**Execution = fulfillment/matching of that instruction**

**Trade = resulting transaction**

And importantly, one order doesn't necessarily mean one execution.

---

### Q3 — Why Rep Code instead of advisor name? ⚠️

Here's the important correction.

You said:

> with rep code, a firm can find out who is the client, financial advisor/Registered Representative business owning the services?

You're heading toward the right concept, but **don't think of the Rep Code as an identifier for all of those things.**

At the basic level:

**Client ID → identifies client**

**Account ID → identifies account**

**Rep Code → identifies/represents the relevant representative/advisor relationship or business assignment**

The systems can then **relate** those things.

For example:

**Account 12345 → assigned Rep Code DEF**

and:

**Rep Code DEF → Mary Jones / particular rep relationship**

So a system could determine:

> Account 12345 is associated with DEF.

and use reference data to determine what **DEF means**.

This distinction is going to become extremely important when we learn **systems of record and reference data**.

Also, Fidelity's JD tells us its rep codes have evolved beyond simply identifying individual advisors: clients use them for **individual advisors, teams, compensation structures and order-handling roles**. That's part of what has made the problem more complicated.

We'll unpack that in Session 2.

---

### Q4 — Why can 3 → 4 affect trading? ⚠️

You wrote:

> legacy systems using the old code can't flow into the systems capable of processing new 4 char codes and if they do, things will break.

The **"things will break"** idea is right, but reverse the mental model slightly.

Suppose a legacy trading system was designed in 1995 to accept:

**REP_CODE = 3 characters**

Then Fidelity sends:

**ABC1**

The legacy system might:

reject it,

truncate it to `ABC`,

fail validation,

corrupt/misinterpret it,

or fail to process the message.

Meanwhile another modern system may happily accept `ABC1`.

So the fundamental problem is:

**New 4-character world**

↓

`ABC1`

↓

**Legacy system only understands 3 characters**

💥

And that's why this phrase from the JD is so important:

> **"maintaining compatibility with legacy systems through a centralized translation approach."**

Eventually we're going to understand exactly what that could mean architecturally.

---

### Q5 — Clearing vs. settlement ✅, with one correction

You said:

> clearing is figuring out the obligations that need to be fulfilled for the order to complete (what does everyone owe?)

Excellent mental definition.

And:

> settlement is when the client get securities and financial firm (or broker?) gets paid

Very close, but be careful with **who gets paid**.

Suppose:

**Paul buys 100 IBM from Jane.**

Conceptually, at settlement:

**Paul/buyer's side → receives the securities**

**Jane/seller's side → receives the cash**

The broker isn't necessarily the seller receiving the purchase proceeds.

So retain:

> **Clearing = determine/prepare who owes what.**

> **Settlement = fulfill those obligations by completing delivery of securities and payment.**

That's enough for now.

---

# Your Session 1 mental model is good

You're now basically here:

**CLIENT**

Paul

↓

**ACCOUNT**

Brokerage Account 12345

↓

**ADVISOR / REGISTERED REP**

Mary

↓

**REP CODE**

DEF

↓

**ORDER**

Buy 100 IBM

↓

**EXECUTION(S)**

20 @ X, 30 @ Y, 50 @ Z

↓

**TRADE(S)**

↓

**CLEARING**

Who owes what?

↓

**SETTLEMENT**

Deliver securities / deliver cash

And here's the question that's going to open **Session 2**:

If Mary is already a person with an employee/person identifier, **why does Fidelity need something called a Rep Code at all?**

And why does Fidelity's JD say clients are using Rep Codes not merely for individual advisors, but for **teams, compensation structures, and order-handling roles**—to the point that they're exhausting the available three-character combinations?

That's where this gets much more interesting.

## Next: Session 2 — Rep Codes 101

We'll start with **what a Rep Code actually represents**, why it's different from a simple employee ID, how it can relate to accounts/orders/trades, why Fidelity is running out of codes, and why M&A and advisor-team structures make the problem worse.

You're ready for that one.