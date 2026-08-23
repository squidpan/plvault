---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 8 — SQL
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

Yes. **Your confusion is justified—the way I drew it mixed two different ideas into the same downward arrow.** Let's fix that now before we do JOINs.

There are **two directions you can talk about**, and they are not the same:

1. **Foreign-key reference direction**
    
2. **Parent → child relationship/navigation direction**
    

## 1. Foreign-key reference direction

The SQL constraint says:

`orders.account_id` **REFERENCES** `client_account.account_id`

Overlay that directly:

**CLIENT_ACCOUNT**  
`account_id` ← **is referenced by** ← `account_id` **ORDERS**

Or reading from Orders toward Client Account:

**ORDERS**  
`account_id` FK → **references** → `client_account.account_id` PK **CLIENT_ACCOUNT**

That is the literal SQL relationship.

### Read this arrow left → right:

**ORDERS.account_id (FK)**  
→ **REFERENCES** →  
**CLIENT_ACCOUNT.account_id (PK)**

So:

> **FK → references → PK**

That's the rule to remember.

---

# 2. Why did I draw Client Account above Orders?

Because I switched to describing the **parent/child business relationship**, not the direction of the `REFERENCES` statement.

Look at it this way:

**CLIENT_ACCOUNT** ← parent  
`account_id` PK  
↓  
↓ **has orders / is referenced by**  
↓  
**ORDERS** ← child  
`account_id` FK  
`order_id` PK

Read **top → bottom**:

> A **Client Account has Orders**.

Or more technically:

> `CLIENT_ACCOUNT.account_id` **is referenced by** `ORDERS.account_id`.

Read **bottom → top**:

> An **Order references its Client Account**.

Both describe the **same relationship from opposite directions**.

---

# Overlay the language directly onto the diagram

Here's the version I should have given you:

**CLIENT_ACCOUNT**  
`account_id` **PK**  
    ↑  
    │ **REFERENCED BY**  
    │  
    │ **REFERENCES**  
    │  
**ORDERS**  
`account_id` **FK**  
`order_id` **PK**

Now read it both ways.

### Bottom → top

**ORDERS.account_id FK**

↑ **REFERENCES**

**CLIENT_ACCOUNT.account_id PK**

Therefore:

> `orders.account_id` references `client_account.account_id`.

### Top → bottom

**CLIENT_ACCOUNT.account_id PK**

↓ **IS REFERENCED BY**

**ORDERS.account_id FK**

Therefore:

> `client_account.account_id` is referenced by `orders.account_id`.

Same fact.

---

# 3. Your `\d client_account` actually showed both perspectives

Remember PostgreSQL gave you:

**Foreign-key constraints:**

`fk_account_rep FOREIGN KEY (rep_code) REFERENCES rep_code_master(rep_code)`

That means:

**CLIENT_ACCOUNT.rep_code FK**

→ references →

**REP_CODE_MASTER.rep_code PK**

But then PostgreSQL separately showed:

**Referenced by:**

`TABLE "orders" ... FOREIGN KEY (account_id) REFERENCES client_account(account_id)`

That's PostgreSQL changing perspective.

It's telling you:

> "You're currently looking at CLIENT_ACCOUNT. Here are the other tables whose foreign keys point **at me**."

So from the perspective of `client_account`:

**REP_CODE_MASTER**

↑ `client_account` references it

**CLIENT_ACCOUNT**

↓ `orders` references it

**ORDERS**

---

# 4. Now add Orders → Executions

From your `\d orders`:

`executions.order_id` **REFERENCES** `orders.order_id`

So the most precise diagram is:

**CLIENT_ACCOUNT**  
`account_id` **PK**  
↑  
│ `orders.account_id` **REFERENCES** this  
│  
**ORDERS**  
`account_id` **FK**  
`order_id` **PK**  
↑  
│ `executions.order_id` **REFERENCES** this  
│  
**EXECUTIONS**  
`order_id` **FK**

Notice that the **FK reference arrows point UP** in this layout.

Now read bottom → top:

> Execution references an Order.

> Order references a Client Account.

That's the database FK direction.

---

# 5. But business flow goes the other direction

And this is the source of the confusion.

Our business lifecycle is naturally:

**CLIENT ACCOUNT**

↓

**ORDER**

↓

**EXECUTION**

↓

**TRADE**

But FK references may look like:

**CLIENT ACCOUNT**

↑ referenced by

**ORDER**

↑ referenced by

**EXECUTION**

So there are two different things:

|Perspective|Direction|
|---|---|
|**Business/process flow**|Account → Order → Execution|
|**Foreign-key reference**|Execution FK → Order PK → Account PK|

They don't have to point in the same direction.

---

# 6. A concrete example makes it much easier

Suppose:

### CLIENT_ACCOUNT

|account_id|client_name|
|--:|---|
|**10001**|Paul Client|

### ORDERS

|order_id|account_id|symbol|
|--:|--:|---|
|50001|**10001**|IBM|
|50006|**10001**|TSLA|

The value `10001` in `ORDERS` points back to:

`CLIENT_ACCOUNT.account_id = 10001`

So:

**Order 50001**

`account_id = 10001`

↑ references

**Client Account 10001**

And:

**Order 50006**

`account_id = 10001`

↑ references

**Client Account 10001**

Therefore the parent/child relationship is:

**ONE CLIENT ACCOUNT**

↓

can have

↓

**MANY ORDERS**

But each of those orders contains the FK pointing **back to its parent account**.

That's the fundamental relational-database idea.

---

# 7. This will make JOINs much easier

Later we'll write something conceptually like:

`CLIENT_ACCOUNT.account_id = ORDERS.account_id`

You're telling SQL:

> Match the **parent's primary key** with the **child's foreign key**.

Conceptually:

**CLIENT_ACCOUNT**

`account_id = 10001` **PK**

↕ MATCH

**ORDERS**

`account_id = 10001` **FK**

And that's how SQL can give us:

|Account|Client|Order|Symbol|
|---|---|---|---|
|10001|Paul Client|50001|IBM|
|10001|Paul Client|50006|TSLA|

The account row gets associated with **multiple matching order rows**.

---

## The one rule I want you to remember

When somebody asks:

> **"Which table references which?"**

Look for the **foreign key**.

### FK → REFERENCES → PK

So here:

**`orders.account_id` FK**

→ **REFERENCES** →

**`client_account.account_id` PK**

When we're drawing **business flow**, however, we may draw:

**Client Account → Orders → Executions**

That's a different perspective.

From now on, when I draw database relationships for this SQL session, I'll explicitly label arrows **`FK REFERENCES`** or **`IS REFERENCED BY`** rather than using an ambiguous downward arrow. That should prevent this exact confusion when we get into JOINs.

---


Good. Back to **Session 8A-5**.

We now know from inspecting the schema that:

`client_account.account_id` = **PK**

and later we'll use:

`orders.account_id` **FK → REFERENCES → `client_account.account_id` PK**

But we don't need a JOIN yet.

## 8A-5 — Active client accounts

Business question:

> **Show all ACTIVE client accounts, including account number, client name, and assigned Rep Code, sorted by account number.**

You inspected `client_account`, so you know the relevant columns:

`account_id`  
`client_name`  
`rep_code`  
`account_status`

Build it yourself using the pattern you've learned:

**SELECT** → the three columns we want  
**FROM** → `client_account`  
**WHERE** → only ACTIVE accounts  
**ORDER BY** → `account_id`

Remember:

- `'ACTIVE'` is text, so it needs quotes.
    
- Finish with `;`.
    

Run it and paste the query + output. Then we'll move into **Orders**, where we'll do a couple of useful filters before starting aggregation and JOINs.


---

Correct. **8A-5 passed.**

You returned the five active accounts and their assigned Rep Codes. You included `account_status` even though the original request didn't require displaying it—that's perfectly valid and actually useful while you're verifying the filter.

One thing omitted from the original requirement was:

> **sort by account number**

Your seed data happened to come back in account order, but SQL does **not guarantee row order unless you explicitly request it**.

So the production-quality version would add:

`ORDER BY account_id;`

That's an important habit.

# 8B — Start working with Orders

Now let's inspect actual business activity.

First, look at the rows:

```
SELECT *
FROM orders
ORDER BY order_id;
```

Run that and look at the data.

Then answer this **without SQL first**:

> Looking at the results, which columns would you use if a Trading SME asked:
> 
> **“Show me all BUY orders that have already been completely filled.”**

Tell me the **columns and values you'd filter on**. Then we'll turn your answer into the SQL query.

---


Exactly. Now **8A-5 is fully complete**, including the explicit ordering.

Let's move into **8B — Orders**.

First inspect the actual order data:

```
SELECT *
FROM orders
ORDER BY order_id;
```

Then don't write another SQL statement yet.

Look at the result and answer this business question:

> **“Show me all BUY orders that have already been completely filled.”**

Tell me:

1. Which column identifies **BUY vs. SELL**?
    
2. What value should it contain?
    
3. Which column tells us the **order's status**?
    
4. What value means completely filled?
    

Then we'll translate your business logic into a SQL `WHERE ... AND ...` query.

---

Exactly. **All four correct.**

Business requirement:

> Show BUY orders that have been completely filled.

translates directly into two predicates:

`side = 'BUY'`

**AND**

`order_status = 'FILLED'`

## 8B-1 — You write the query

Let's return these columns:

`order_id`  
`account_id`  
`rep_code`  
`symbol`  
`side`  
`quantity`  
`order_status`

Filter using the two conditions you just identified and sort by `order_id`.

Build the entire query yourself:

**SELECT → FROM → WHERE condition 1 AND condition 2 → ORDER BY → ;**

Before running it, predict how many rows you expect from the six orders if you have the table output in front of you.

Run it and paste the result.

After this, we'll do one more filtering exercise involving **dates/inequality**, then move to **8C — aggregates (`COUNT`, `SUM`, `GROUP BY`)**. After that comes the big one: **8D — JOINs**.

---


Perfect. **8B-1 passed.** The result is exactly what the business rule asked for: BUY orders whose `order_status` is `FILLED`.

You also just exposed an interesting row we’ll come back to:

`order_id 50006`  
`account_id 10001`  
`rep_code DEF1`

Earlier, account `10001` was assigned `ABC1`.

That mismatch is intentional. We’ll find it properly with a JOIN rather than eyeballing it.

## 8B-2 — Date filtering

Now one more practical filter before aggregates.

Business question:

> **Show me all orders created on or after August 21, 2026.**

You’ll use:

`created_at`

and a comparison such as:

`created_at >= '2026-08-21'`

Return:

`order_id`  
`account_id`  
`rep_code`  
`symbol`  
`order_status`  
`created_at`

Sort by `created_at`.

Build and run that yourself.

After this, we go to **8C — aggregates** with questions like:

> How many orders are there by status?

> How many shares were ordered by symbol?

Then we start **JOINs**, which is the most important SQL section for this Fidelity prep.

---

Perfect. **8B-2 passed.**

You filtered correctly on the timestamp and returned the three orders created on or after August 21.

A subtle point: PostgreSQL interpreted:

`'2026-08-21'`

as midnight at the start of that date, so the condition effectively means:

`created_at >= 2026-08-21 00:00:00`

That is exactly what we wanted here.

# 8C — Aggregates

Now we move from retrieving individual rows to answering summary questions.

## 8C-1 — Count orders by status

Business question:

> **How many orders are in each order status?**

We need:

`COUNT(*)`

and:

`GROUP BY order_status`

Think conceptually:

**SELECT** → status + count  
**FROM** → orders  
**GROUP BY** → status  
**ORDER BY** → status

Build the query yourself.

The output should look conceptually like:

`FILLED | ?`

`NEW | ?`

`PARTIALLY_FILLED | ?`

Run it and paste the result.

After that we'll do:

> **How many shares were ordered by symbol?**

which introduces `SUM(quantity)`.

Then we'll start **JOINs**.

---

Exactly. **8C-1 passed.**

You just answered a business question with aggregation rather than returning transaction-level rows:

|Status|Count|
|---|--:|
|FILLED|4|
|NEW|1|
|PARTIALLY_FILLED|1|

The important new concept is:

> `GROUP BY` creates groups of rows sharing the same value, and the aggregate function calculates something for each group.

Here:

**6 individual order rows**

↓ `GROUP BY order_status`

**3 groups**

↓ `COUNT(*)`

**4 FILLED / 1 NEW / 1 PARTIALLY_FILLED**

## 8C-2 — `SUM`

Now Trading asks:

> **How many total shares were ordered for each security?**

You need:

- `symbol`
    
- `quantity`
    
- `SUM(quantity)`
    
- `GROUP BY symbol`
    
- `ORDER BY symbol`
    

The conceptual operation is:

IBM orders → add their quantities together  
AAPL orders → add their quantities together  
MSFT orders → add their quantities together  
etc.

One security appears in **more than one order**, so this exercise demonstrates why aggregation matters.

### Your task

Write the query yourself.

Your result should have two columns:

`symbol`

and the total quantity.

You can initially leave PostgreSQL's default column name as `sum`. After you get the right result, I'll show you **aliases with `AS`**, which lets us make query output much more business-readable:

`total_quantity`

Then we'll do one quick `HAVING` exercise and move into **8D — JOINs**.


---

Your SQL syntax is correct, but there's a **business-question mistake** here—and this is actually more important than the syntax.

I asked:

> **How many total shares were ordered for each security?**

You queried:

`FROM trades`

But **ordered quantity** belongs in our `orders` table.

Your result answers a different question:

> **How many shares appear in trades for each security?**

That's why your IBM result is `100`. In `orders`, there are two IBM orders: `100` and `125`, so **ordered IBM quantity should be 225**.

This is a very BA-relevant distinction:

> **Correct SQL against the wrong data source can produce a perfectly valid but incorrect business answer.**

Before writing SQL, always ask:

**What business question am I answering? → What entity/data represents that concept? → Which table is authoritative/appropriate for it?**

### Try 8C-2 again

Same query structure:

`symbol`

`SUM(quantity)`

`GROUP BY symbol`

`ORDER BY symbol`

But choose the table representing **orders**, not trades.

Also, let's introduce an alias. Instead of allowing PostgreSQL to call the result `sum`, write:

`SUM(quantity) AS total_order_quantity`

So your result will read:

|symbol|total_order_quantity|
|---|--:|
|...|...|

Write the complete query yourself.

This little mistake was actually useful preparation for **JOINs and data lineage**, because Fidelity isn't merely going to care whether you know SQL syntax—they'll care whether you understand **what the data means and where it came from**.

---

Exactly. **8C-2 passed.**

Now we can see why choosing the correct business entity mattered:

|Symbol|Total ordered|
|---|--:|
|AAPL|50|
|IBM|**225**|
|MSFT|200|
|NVDA|75|
|TSLA|25|

IBM is `225` because there are two IBM orders: `100 + 125`.

One small improvement: give the calculated column a useful name:

`SUM(quantity) AS total_order_quantity`

So instead of PostgreSQL displaying `sum`, it displays `total_order_quantity`.

# 8C-3 — `HAVING`

This is the last aggregate concept before **JOINs**.

Business asks:

> **Which securities have more than 100 total shares ordered?**

You've already calculated:

`GROUP BY symbol`

with:

`SUM(quantity)`

Now we want to filter the **groups** based on that calculated total.

This introduces:

`HAVING`

The distinction is important:

**WHERE** → filters individual rows **before grouping**

**HAVING** → filters groups **after aggregation**

For example:

`WHERE side = 'BUY'`

means:

> Only use BUY rows.

Whereas:

`HAVING SUM(quantity) > 100`

means:

> After grouping and summing, only return groups whose total exceeds 100.

### Your task

Return:

`symbol`

`SUM(quantity) AS total_order_quantity`

from `orders`.

Group by `symbol`.

Keep only symbols where:

`SUM(quantity) > 100`

Sort by `symbol`.

Construct and run it yourself.

You should be able to predict the result from the table above before executing it.

After this:

# 8D — JOINs

And that's where we'll answer the much more interesting Fidelity-style question:

> **Which orders have a Rep Code that doesn't agree with the Rep Code assigned to the account?**

We'll build that JOIN slowly from the PK/FK relationship we just worked through.

---

Exactly. **8C-3 passed.**

You now have the aggregate sequence:

`GROUP BY` → create groups  
`SUM()` / `COUNT()` → calculate per group  
`HAVING` → filter the grouped result

And you correctly returned only:

**IBM = 225**  
**MSFT = 200**

because those are the only symbols whose total ordered quantity exceeds 100.

# 8D — JOINs

Now we get to the most important SQL section for this Fidelity prep.

The business question:

> **Which orders have a Rep Code that does not match the Rep Code assigned to the account?**

We already know the relationship:

**`orders.account_id` FK → REFERENCES → `client_account.account_id` PK**

That means we can connect the two tables using:

`orders.account_id = client_account.account_id`

But first, don't write the mismatch query yet.

## 8D-1 — Basic INNER JOIN

Business asks:

> **Show every order together with the client name and the Rep Code assigned to the account.**

We need data from:

**orders**

and:

**client_account**

Let's give them aliases to keep the SQL readable:

`orders o`

`client_account a`

Then conceptually:

**orders o**

JOIN

**client_account a**

ON

`o.account_id = a.account_id`

Return:

`o.order_id`  
`o.account_id`  
`a.client_name`  
`a.rep_code AS account_rep_code`  
`o.rep_code AS order_rep_code`  
`o.symbol`  
`o.order_status`

Sort by `o.order_id`.

This is your first real JOIN, so I'll give you the skeleton:

`SELECT ...`

`FROM orders o`

`JOIN client_account a`

`ON o.account_id = a.account_id`

`ORDER BY ... ;`

You fill in the SELECT columns.

Run that and paste the result.

Once that works, the very next exercise is the good one:

> **Show only the rows where `account_rep_code <> order_rep_code`.**

That will reveal the intentional mismatch we planted.


---


You're very close. The **JOIN itself was correct** in your second attempt. The problem is where the mismatch condition belongs.

There are three different jobs here:

`JOIN ... ON` = **how the two tables are related**

`WHERE` = **which joined rows you want**

`ORDER BY` = **how to sort the final result**

So the order is:

```
SELECT ...
FROM ...
JOIN ...
    ON ...
WHERE ...
ORDER BY ...;
```

### First, run only the JOIN

Your second query was essentially correct. Run this and **make sure it ends with `;`**:

```
SELECT
    o.order_id,
    o.account_id,
    a.client_name,
    a.rep_code AS account_rep_code,
    o.rep_code AS order_rep_code,
    o.symbol,
    o.order_status
FROM orders o
JOIN client_account a
    ON o.account_id = a.account_id
ORDER BY o.account_id;
```

This should return **all six orders**.

## Then we'll find the mismatch

You were trying to add:

`account_rep_code <> order_rep_code`

Your instinct is right: `<>` means **not equal**.

But don't use the aliases in the `WHERE` clause yet. Refer directly to the source columns:

`a.rep_code <> o.rep_code`

And it belongs **after the JOIN and before ORDER BY**:

```
FROM orders o
JOIN client_account a
    ON o.account_id = a.account_id
WHERE a.rep_code <> o.rep_code
ORDER BY o.account_id;
```

### Read that in English

**FROM orders o**

> Start with Orders.

**JOIN client_account a**

> Bring in Client Account.

**ON o.account_id = a.account_id**

> Match each Order to its Account using the FK/PK relationship.

**WHERE a.rep_code <> o.rep_code**

> Of those matched rows, keep only cases where the Account Rep Code and Order Rep Code disagree.

**ORDER BY o.account_id**

> Sort the remaining result by account.

That's the distinction I want you to internalize:

**JOIN/ON = establish the relationship**

↓

**WHERE = filter the resulting rows**

Your first attempt put the filter immediately after `ON` without `WHERE`; your third put `WHERE` **before the JOIN**; your fourth tried to make the comparison itself another `JOIN`. Those errors are actually useful because you're discovering what each clause does.

First run the **all-six-orders JOIN** above and paste the output. Then **you** add the `WHERE` condition to find the mismatch.

---


