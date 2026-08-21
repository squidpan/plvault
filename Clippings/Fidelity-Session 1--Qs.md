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

---

# Session 1 — Brokerage & Wealth Management 101



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
