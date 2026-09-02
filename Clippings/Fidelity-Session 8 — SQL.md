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

| Perspective               | Direction                            |
| ------------------------- | ------------------------------------ |
| **Business/process flow** | Account → Order → Execution          |
| **Foreign-key reference** | Execution FK → Order PK → Account PK |

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

```pqsl
fidelity_rep_code_ba_prep=> select symbol, SUM(quantity) AS order_quantity from orders GROUP BY symbol HAVING SUM(quantity) >= 200 ORDER BY symbol;
 symbol | order_quantity 
--------+----------------
 IBM    |            225
 MSFT   |            200
(2 rows)

```
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


```
fidelity_rep_code_ba_prep=> select o.order_id, o.account_id, a.client_name, a.rep_code AS account_rep_code, o.rep_code AS order_rep_code, o.symbol, o.order_status  from orders o JOIN client_account a ON o.account_id = a.account_id where a.rep_code <> o.rep_code ORDER BY o.account_id;
 order_id | account_id | client_name | account_rep_code | order_rep_code | symbol | order_status 
----------+------------+-------------+------------------+----------------+--------+--------------
    50006 |      10001 | Paul Client | ABC1             | DEF1           | TSLA   | FILLED
(1 row)

fidelity_rep_code_ba_prep=> 
```


---

Perfect. **That is the exact mismatch we planted.**

`account 10001` is assigned:

`ABC1`

but `order 50006` carries:

`DEF1`

So your JOIN + filter is doing a real BA-style data-quality check:

> **Find orders whose Rep Code does not agree with the Rep Code assigned to the account.**

That is directly relevant to the Fidelity role because it combines:

**data mapping + reconciliation + lineage + business-rule validation**

## What you just learned

Your query structure was:

`FROM orders o`

→ start with orders

`JOIN client_account a`

→ bring in the account

`ON o.account_id = a.account_id`

→ match child FK to parent PK

`WHERE a.rep_code <> o.rep_code`

→ keep only mismatches

That is the core JOIN pattern you need to get comfortable with.

## Next JOIN exercise

Now let's use the Rep Code reference data too.

Business question:

> **For every order, show the order Rep Code and what business relationship/name that Rep Code represents.**

You'll need:

**orders**

and:

**rep_code_master**

Relationship:

`orders.rep_code`

references logically/matches:

`rep_code_master.rep_code`

Return:

`order_id`

`account_id`

`o.rep_code`

`r.rep_name`

`r.rep_type`

`symbol`

`order_status`

Use aliases:

`orders o`

`rep_code_master r`

Your JOIN condition should be:

`o.rep_code = r.rep_code`

Build that query yourself.

After that, we'll do the more interesting one:

> **Which active/new Rep Codes do not have a usable legacy translation?**

That will introduce a **LEFT JOIN**, which is especially useful for finding missing mappings.


---

```
fidelity_rep_code_ba_prep=> select o.order_id, o.account_id, o.rep_code, r.rep_name, r.rep_type, o.symbol, o.order_status from orders o JOIN rep_code_master r ON o.rep_code=r.rep_code;
 order_id | account_id | rep_code |        rep_name         |  rep_type  | symbol |   order_status   
----------+------------+----------+-------------------------+------------+--------+------------------
    50001 |      10001 | ABC1     | Smith Advisory Team     | TEAM       | IBM    | FILLED
    50002 |      10002 | DEF1     | Mary Jones              | INDIVIDUAL | AAPL   | FILLED
    50003 |      10003 | GHI1     | North Region Advisory   | TEAM       | MSFT   | PARTIALLY_FILLED
    50004 |      10004 | ABC1     | Smith Advisory Team     | TEAM       | IBM    | NEW
    50005 |      10005 | JKL1     | Legacy Transition Group | TEAM       | NVDA   | FILLED
    50006 |      10001 | DEF1     | Mary Jones              | INDIVIDUAL | TSLA   | FILLED
(6 rows)

fidelity_rep_code_ba_prep=> 
```


---

Perfect. **That JOIN is correct.**

You just enriched each order with the business meaning of its Rep Code:

`orders.rep_code`

→ matches →

`rep_code_master.rep_code`

and returned the descriptive attributes:

`rep_name` and `rep_type`.

This is a good example of a common BA/data-analysis pattern:

**transactional table**

`orders`

↓

**reference/master table**

`rep_code_master`

↓

**human-readable business context**

The result also makes the intentional mismatch easier to interpret: order `50006` carries `DEF1`, which resolves to **Mary Jones**, even though account `10001` is assigned `ABC1` / **Smith Advisory Team**.

## Next: `LEFT JOIN` for missing mappings

Now we want to answer a very Fidelity-relevant question:

> **Which Rep Codes do not have a usable legacy translation?**

This is where `LEFT JOIN` is better than a normal `JOIN`.

Why? Because a normal inner `JOIN` only returns rows that match on both sides. If a Rep Code has **no translation**, it can disappear from the result—which is exactly the row we want to find.

Conceptually:

**rep_code_master r**

LEFT JOIN

**rep_code_translation t**

ON

`r.rep_code = t.new_rep_code`

The `LEFT JOIN` says:

> Keep **all** Rep Codes from the left table, even if no matching translation row exists.

Then a missing translation can show up with:

`t.legacy_rep_code = NULL`

For this exercise, return:

`r.rep_code`  
`r.rep_name`  
`r.active_flag`  
`t.legacy_rep_code`  
`t.active_flag AS translation_active`

First write the **LEFT JOIN without filtering** so you can see all six Rep Codes and their translation state.

Then we'll filter for the problematic cases.


---

```
fidelity_rep_code_ba_prep=> select r.rep_code, r.rep_name, r.active_flag, t.legacy_rep_code, r.active_flag AS translation_active from rep_code_master r LEFT JOIN rep_code_translation t ON r.rep_code = t.new_rep_code;
 rep_code |        rep_name         | active_flag | legacy_rep_code | translation_active 
----------+-------------------------+-------------+-----------------+--------------------
 ABC1     | Smith Advisory Team     | t           | XYZ             | t
 DEF1     | Mary Jones              | t           | DEF             | t
 GHI1     | North Region Advisory   | t           | GHI             | t
 JKL1     | Legacy Transition Group | t           |                 | t
 MNO1     | Inactive Advisor Group  | f           | MNO             | f
 PQR1     | Trading Support Desk    | t           | PQR             | t
(6 rows)
```


---


Almost perfect. The JOIN itself is correct, and the result is exactly the kind of thing we wanted to see.

There is one aliasing mistake in your `SELECT` list:

You wrote:

`r.active_flag AS translation_active`

but `translation_active` should come from the translation table, so it should be:

`t.active_flag AS translation_active`

Right now your output makes `translation_active` simply repeat the master record's `active_flag`, which happens to look plausible for most rows but isn't actually answering the translation-status question.

The corrected query is:

```
SELECT
    r.rep_code,
    r.rep_name,
    r.active_flag,
    t.legacy_rep_code,
    t.active_flag AS translation_active
FROM rep_code_master r
LEFT JOIN rep_code_translation t
    ON r.rep_code = t.new_rep_code;
```

What should stand out conceptually is `JKL1`:

- Rep Code is active.
    
- `legacy_rep_code` is `NULL`.
    
- Translation row itself exists and is active in our seed data, but there is no actual legacy code value.
    

That is a useful distinction: **a translation record can exist while the mapping value itself is missing**.

So the next BA-style question is:

> Which active Rep Codes are missing a usable legacy Rep Code?

We want rows where:

`r.active_flag = TRUE`

and

`t.legacy_rep_code IS NULL`

Notice that `NULL` uses:

`IS NULL`

not:

`= NULL`

Build that query yourself from the corrected LEFT JOIN.


---

```
fidelity_rep_code_ba_prep=> select r.rep_code, r.rep_name, r.active_flag, t.legacy_rep_code, t.active_flag AS translation_active from rep_code_master r LEFT JOIN rep_code_translation t ON r.rep_code = t.new_rep_code;
 rep_code |        rep_name         | active_flag | legacy_rep_code | translation_active 
----------+-------------------------+-------------+-----------------+--------------------
 ABC1     | Smith Advisory Team     | t           | XYZ             | t
 DEF1     | Mary Jones              | t           | DEF             | t
 GHI1     | North Region Advisory   | t           | GHI             | t
 JKL1     | Legacy Transition Group | t           |                 | t
 MNO1     | Inactive Advisor Group  | f           | MNO             | f
 PQR1     | Trading Support Desk    | t           | PQR             | t
(6 rows)

fidelity_rep_code_ba_prep=> 
```


---

Perfect. Now the output is semantically correct: `translation_active` is coming from the translation table.

The interesting row is still:

`JKL1 | Legacy Transition Group | active=t | legacy_rep_code=NULL | translation_active=t`

So the master Rep Code is active and its translation record is active, but the actual legacy code is missing.

Now filter for exactly that problem.

Use:

`r.active_flag = TRUE`

and

`t.legacy_rep_code IS NULL`

So your query should keep the same `LEFT JOIN`, then add a `WHERE` clause with those two conditions.

That should isolate the active Rep Codes that **do not have a usable legacy mapping**.

Run it and paste the result.


---

```
fidelity_rep_code_ba_prep=> select r.rep_code, r.rep_name, r.active_flag, t.active_flag AS translation_active,t.legacy_rep_code from rep_code_master r LEFT JOIN rep_code_translation t ON r.rep_code = t.new_rep_code WHERE r.active_flag = TRUE AND t.legacy_rep_code is NULL;
 rep_code |        rep_name         | active_flag | translation_active | legacy_rep_code 
----------+-------------------------+-------------+--------------------+-----------------
 JKL1     | Legacy Transition Group | t           | t                  | 
(1 row)

fidelity_rep_code_ba_prep=> 
```

---

Perfect. **That LEFT JOIN + `IS NULL` check is exactly the kind of query I wanted you to get comfortable with.**

You just answered:

> Which active Rep Codes do not have a usable legacy mapping?

and correctly isolated:

`JKL1 — Legacy Transition Group`

That is a very realistic BA/data-quality query for this project.

A few key takeaways from what you just did:

- `JOIN` answers: **which rows relate across tables?**
    
- `LEFT JOIN` is useful when you want to keep the full population on the left even when the related data is missing.
    
- `IS NULL` is how you test for missing values.
    
- SQL can validate **business readiness**, not just retrieve data.
    

This query is basically checking a rule like:

> Every active Rep Code that requires legacy compatibility should have a valid legacy mapping.

That is very close to how requirements, data analysis, and testing come together.

### Next useful SQL step

I'd do one more JOIN exercise before moving to CTE/CASE:

> **Find trades whose legacy Rep Code does not match the expected mapping from the authoritative translation table.**

That will let us compare:

**trade.legacy_rep_code**

against

**rep_code_translation.legacy_rep_code**

for the same four-character Rep Code.

After that, I think you've covered the most important JOIN patterns for interview prep, and we can move into lighter-weight CTE/CASE work rather than spending forever on SQL.

---

```
Explain the LEFT part again. which table is on the left? rep_code_translation?
```



---

No — **`rep_code_master` is the LEFT table.**

The easiest rule is:

> In `A LEFT JOIN B`, **A is the left table** and **B is the right table**.

Your query says:

`FROM rep_code_master r LEFT JOIN rep_code_translation t`

So:

**LEFT table** = `rep_code_master r`  
**RIGHT table** = `rep_code_translation t`

## Overlay it on your query

```
FROM rep_code_master r
     LEFT JOIN rep_code_translation t
       ON r.rep_code = t.new_rep_code
```

Think of it visually:

**LEFT — rep_code_master (`r`)**

`ABC1`  
`DEF1`  
`GHI1`  
`JKL1`  
`MNO1`  
`PQR1`

↓ try to find a matching row using Rep Code

**RIGHT — rep_code_translation (`t`)**

`ABC1 → XYZ`  
`DEF1 → DEF`  
`GHI1 → GHI`  
`JKL1 → NULL`  
`MNO1 → MNO`  
`PQR1 → PQR`

The key behavior of `LEFT JOIN` is:

> **Keep every qualifying row from the LEFT table whether or not a matching row exists on the RIGHT.**

## Why that's useful

Imagine `PQR1` didn't exist at all in `rep_code_translation`.

### With an INNER JOIN

`PQR1` disappears.

You might never notice that it lacks a translation record.

### With a LEFT JOIN

PostgreSQL preserves `PQR1`:

|r.rep_code|r.rep_name|t.legacy_rep_code|
|---|---|---|
|ABC1|Smith Advisory Team|XYZ|
|DEF1|Mary Jones|DEF|
|...|...|...|
|**PQR1**|Trading Support Desk|**NULL**|

PostgreSQL is essentially saying:

> "PQR1 exists on the left. I couldn't find matching information on the right, so I'll keep PQR1 and fill the right-side columns with NULL."

That's why `LEFT JOIN` is so useful for **finding missing relationships**.

## One subtlety in our JKL1 example

Our `JKL1` is slightly different.

There **is** a matching translation row:

`JKL1 → NULL`

So the LEFT JOIN finds the row, but its `legacy_rep_code` value itself is NULL.

There are actually two possible problems:

**Problem A — no translation row exists**

`JKL1` in master

→ no `JKL1` row at all in translation

**Problem B — translation row exists but value is missing**

`JKL1` in master

→ translation row exists

→ `legacy_rep_code = NULL`

Our canned `JKL1` demonstrates **Problem B**.

Later we can deliberately create a row demonstrating **Problem A**, because distinguishing those two conditions is useful.

### The memory trick

Whenever you see:

`A LEFT JOIN B`

read it as:

> **"Keep A. Bring me B when you can."**

So ours is:

> **"Keep all the Rep Code master records. Bring me their translation information when available."**

That's the **LEFT** in `LEFT JOIN`.



---

Not quite. There are **two separate concepts getting mixed together: JOIN type and WHERE filtering.**

### What we've done

|Exercise|JOIN type|Purpose|
|---|---|---|
|Account ↔ Order mismatch|**INNER JOIN**|Match orders to accounts|
|Order ↔ Rep Code Master|**INNER JOIN**|Match orders to Rep Code definitions|
|Rep Master ↔ Translation|**LEFT OUTER JOIN**|Keep all master Rep Codes even if translation is missing|

So the **first two were INNER JOINs**. The third was a **LEFT OUTER JOIN**.

### Why the first one looked different

We wrote:

`JOIN client_account a ON o.account_id = a.account_id`

In SQL, plain:

`JOIN`

normally means:

`INNER JOIN`

So these are equivalent:

`JOIN client_account a`

and:

`INNER JOIN client_account a`

Then we added:

`WHERE a.rep_code <> o.rep_code`

But **WHERE does not determine the JOIN type**.

It simply filters the result **after the tables have been joined**.

Think:

**INNER JOIN**

> Give me rows where A and B have a match.

**LEFT OUTER JOIN**

> Give me **all A rows**, plus matching B data when available.

**WHERE**

> Now filter whatever result you produced.

---

### And LEFT JOIN is actually an OUTER JOIN

This is another terminology point:

**OUTER JOIN** is the family.

It contains:

`LEFT OUTER JOIN`

`RIGHT OUTER JOIN`

`FULL OUTER JOIN`

And SQL lets us shorten:

`LEFT OUTER JOIN`

to simply:

`LEFT JOIN`

So our third query:

`rep_code_master LEFT JOIN rep_code_translation`

was specifically a **LEFT OUTER JOIN**.

### Easy mental model

**INNER JOIN:**

> "Give me the intersection — only matching records."

**LEFT JOIN:**

> "Keep everything from my left table; attach the right-side data when you find it."

And remember:

> **WHERE is a filter, not a JOIN type.**

You're asking these questions at exactly the right point, because getting **INNER vs LEFT + ON vs WHERE** straight before we add more complicated JOINs will make the rest much easier.



---


Good. Next we'll do the **trade-to-translation reconciliation JOIN**.

Business question:

> **Find trades where the legacy Rep Code stored on the trade does not match the expected legacy mapping for that trade's four-character Rep Code.**

Conceptually:

**TRADES**

`rep_code = ABC1`  
`legacy_rep_code = XYZ`

JOIN

**REP_CODE_TRANSLATION**

`new_rep_code = ABC1`  
`legacy_rep_code = XYZ`

Then compare:

`trades.legacy_rep_code`

vs.

`rep_code_translation.legacy_rep_code`

### Step 1 — Show all trade/mapping pairs

Use aliases:

`trades tr`

`rep_code_translation t`

Join on:

`tr.rep_code = t.new_rep_code`

Return:

`tr.trade_id`  
`tr.rep_code`  
`tr.legacy_rep_code AS trade_legacy_code`  
`t.legacy_rep_code AS expected_legacy_code`  
`tr.trade_status`

Sort by `trade_id`.

Write that JOIN yourself first and paste the result.

Then we'll add the mismatch filter.



---

```
fidelity_rep_code_ba_prep=> select tr.trade_id, tr.rep_code, tr.legacy_rep_code AS trade_legacy_code, t.legacy_rep_code AS expected_legacy_code, tr.trade_status from trades tr JOIN rep_code_translation t ON tr.rep_code = t.new_rep_code order by trade_id;
 trade_id | rep_code | trade_legacy_code | expected_legacy_code | trade_status 
----------+----------+-------------------+----------------------+--------------
    90001 | ABC1     | XYZ               | XYZ                  | SETTLED
    90002 | DEF1     | DEF               | DEF                  | SETTLED
    90003 | GHI1     | GHI               | GHI                  | PENDING
    90004 | JKL1     |                   |                      | EXCEPTION
    90005 | DEF1     | DEF               | DEF                  | SETTLED
(5 rows)

fidelity_rep_code_ba_prep=> 
```



---

Perfect. The JOIN is correct, and this is a good reconciliation view.

For the first three settled/pending trades, the values line up exactly:

- `ABC1 → XYZ`
    
- `DEF1 → DEF`
    
- `GHI1 → GHI`
    

For `90004`, both the trade and expected mapping are `NULL`, which is why it is already marked `EXCEPTION` in our canned data.

## Next — find actual mismatches

Now add a filter for cases where:

`tr.legacy_rep_code <> t.legacy_rep_code`

But there's a wrinkle: **`NULL` doesn't behave like an ordinary value in SQL**.

A comparison like:

`NULL <> NULL`

doesn't evaluate to TRUE; it evaluates to **UNKNOWN**.

So if we want a robust PostgreSQL comparison that treats NULLs properly, use:

`IS DISTINCT FROM`

This is very handy.

So your condition becomes:

`tr.legacy_rep_code IS DISTINCT FROM t.legacy_rep_code`

That means:

> Keep rows where the two values are different, including cases where one is NULL and the other is not.

Build the same JOIN and add that `WHERE` condition.

With the current canned data, I expect **zero rows**, because the stored legacy values currently match the expected mappings—including the JKL1 case where both are NULL.

Run it and show me the result. Then I'll deliberately give you one small update statement to create a bad trade mapping so you can rerun the reconciliation query and catch it.


---

```
fidelity_rep_code_ba_prep=> select tr.trade_id, tr.rep_code, tr.legacy_rep_code AS trade_legacy_code, t.legacy_rep_code AS expected_legacy_code, tr.trade_status from trades tr JOIN rep_code_translation t ON tr.rep_code = t.new_rep_code WHERE tr.legacy_rep_code IS DISTINCT FROM t.legacy_rep_code order by trade_id;
 trade_id | rep_code | trade_legacy_code | expected_legacy_code | trade_status 
----------+----------+-------------------+----------------------+--------------
(0 rows)

fidelity_rep_code_ba_prep=> 
```


---

Perfect. That result is exactly what we expected: **no trade currently contains a legacy Rep Code that disagrees with the translation table.**

This is a useful reconciliation query because it tests:

**Trade representation**

against

**Expected translation mapping**

for the same new Rep Code.

Now let's intentionally create one bad row so you can see the query catch it.

Run this:

```
UPDATE trades
SET legacy_rep_code = 'BAD'
WHERE trade_id = 90005;
```

Then rerun your reconciliation query:

```
SELECT
    tr.trade_id,
    tr.rep_code,
    tr.legacy_rep_code AS trade_legacy_code,
    t.legacy_rep_code AS expected_legacy_code,
    tr.trade_status
FROM trades tr
JOIN rep_code_translation t
    ON tr.rep_code = t.new_rep_code
WHERE tr.legacy_rep_code IS DISTINCT FROM t.legacy_rep_code
ORDER BY trade_id;
```

You should now get **trade 90005** as a mismatch.

This demonstrates a very real BA/data-quality pattern:

> **Expected mapping vs. actual transaction value → identify reconciliation breaks**

After that, we'll restore the data and move into one last compact SQL section:

**CASE → simple CTE → one subquery example → Oracle differences**

Then I think your SQL refresher is sufficient for this interview prep.

---

```
fidelity_rep_code_ba_prep=> UPDATE trades
SET legacy_rep_code = 'BAD'
WHERE trade_id = 90005;
UPDATE 1
fidelity_rep_code_ba_prep=> SELECT
    tr.trade_id,
    tr.rep_code,
    tr.legacy_rep_code AS trade_legacy_code,
    t.legacy_rep_code AS expected_legacy_code,
    tr.trade_status
FROM trades tr
JOIN rep_code_translation t
    ON tr.rep_code = t.new_rep_code
WHERE tr.legacy_rep_code IS DISTINCT FROM t.legacy_rep_code
ORDER BY trade_id;
 trade_id | rep_code | trade_legacy_code | expected_legacy_code | trade_status 
----------+----------+-------------------+----------------------+--------------
    90005 | DEF1     | BAD               | DEF                  | SETTLED
(1 row)

fidelity_rep_code_ba_prep=> 

```



---

Perfect. That is exactly what a reconciliation query should do.

You deliberately corrupted:

`trade 90005`

from expected:

`DEF`

to actual:

`BAD`

and the query isolated the mismatch:

`trade_id 90005 | DEF1 | BAD | DEF`

That is a very good example of **expected mapping vs. actual transaction value**.

First restore the row:

```
UPDATE trades
SET legacy_rep_code = 'DEF'
WHERE trade_id = 90005;
```

Then rerun the reconciliation query once more to confirm you are back to:

`0 rows`

After that, I’d do only **three compact SQL topics** before calling the refresher sufficient for this interview:

### 8E — `CASE`

Business question:

> Classify each Rep Code translation as `READY`, `MISSING_MAPPING`, or `INACTIVE`.

This teaches conditional logic inside a query.

### 8F — CTE

We'll take a useful query and wrap it as:

`WITH something AS (...)`

Then query the result.

The goal is to learn:

> **CTE = give an intermediate query a readable name so a larger investigation is easier to understand.**

### 8G — One subquery + Oracle differences

One practical subquery, then a short PostgreSQL → Oracle comparison covering only what matters for you:

`LIMIT` vs Oracle row limiting  
boolean handling  
string/date functions  
`COALESCE` / Oracle `NVL` awareness  
`VARCHAR`/`VARCHAR2` terminology  
CTEs/JOINs essentially familiar  
standard `SELECT`, `WHERE`, `GROUP BY`, joins remain transferable

So you're now roughly **45–60 minutes from finishing the planned SQL refresher**, not another 2–3 hours.

And the most important material is already done:

**SELECT / WHERE / ORDER BY**

**GROUP BY / SUM / COUNT / HAVING**

**INNER JOIN**

**LEFT OUTER JOIN**

**NULL handling**

**PK/FK relationships**

**data-quality mismatch detection**

**translation reconciliation**

Those are the areas I'd most want you to be comfortable discussing for this Fidelity BA role.


---


Good. First restore our deliberate corruption and verify the lab is clean:

```
UPDATE trades
SET legacy_rep_code = 'DEF'
WHERE trade_id = 90005;
```

Then rerun your reconciliation query. You should get `(0 rows)`.

After that:

## 8E — `CASE`: turn data into a business classification

So far we've retrieved and compared data. A BA often wants something more useful:

> **Classify every Rep Code's legacy-translation readiness.**

Let's define our training rules:

- Master Rep Code inactive → `INACTIVE`
    
- Active Rep Code but legacy mapping is NULL → `MISSING_MAPPING`
    
- Active Rep Code with legacy mapping → `READY`
    

This introduces:

`CASE`

Think of it like an Excel `IF`/`IFS` expressed in SQL:

`CASE`

→ if condition A, return result A

→ else if condition B, return result B

→ otherwise return result C

→ `END`

### Business question

> Show every Rep Code, its legacy mapping, and a calculated `mapping_status`.

We still need our:

**LEFT:** `rep_code_master r`

**RIGHT:** `rep_code_translation t`

because we don't want Rep Codes disappearing merely because translation information is unavailable.

I'll give you the new `CASE` syntax because you haven't used it yet:

```
CASE
    WHEN r.active_flag = FALSE THEN 'INACTIVE'
    WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
    ELSE 'READY'
END AS mapping_status
```

Now **you build the complete query around that**.

Return:

`r.rep_code`  
`r.rep_name`  
`t.legacy_rep_code`  
the `CASE ... END AS mapping_status`

and sort by `r.rep_code`.

Before running it, predict:

- `ABC1` → ?
    
- `JKL1` → ?
    
- `MNO1` → ?
    

Then run it and paste the result.


---

```
fidelity_rep_code_ba_prep=> select r.rep_code, r.rep_name, t.legacy_rep_code from rep_code_master r, rep_code_translation t CASE
    WHEN r.active_flag = FALSE THEN 'INACTIVE'
    WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
    ELSE 'READY'
END AS mapping_status ORDER BY r.repo_code;
ERROR:  syntax error at or near "CASE"
LINE 1: ...rep_code from rep_code_master r, rep_code_translation t CASE
                                                                   ^
fidelity_rep_code_ba_prep=> 
```


---


Yep — syntax issue, and it's a useful one.

The `CASE` expression belongs in the **SELECT list** because you're asking SQL to create a calculated output column called `mapping_status`.

You currently have roughly:

`SELECT columns FROM tables CASE ...`

But conceptually we need:

**SELECT**

- real column
    
- real column
    
- real column
    
- **calculated CASE column**
    

**FROM**

- tables and JOIN relationship
    

**ORDER BY**

- result
    

There's also a second issue: you wrote:

`FROM rep_code_master r, rep_code_translation t`

That's an old-style way of combining tables and, without a join condition, would produce a **Cartesian product**: every master row paired with every translation row. We don't want that.

Use the `LEFT JOIN` you just learned.

## Build it in this order

Start with your SELECT columns:

```
SELECT
    r.rep_code,
    r.rep_name,
    t.legacy_rep_code,
```

Now the **fourth selected column** is your calculated value:

```
CASE
    WHEN r.active_flag = FALSE THEN 'INACTIVE'
    WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
    ELSE 'READY'
END AS mapping_status
```

Then:

```
FROM rep_code_master r
LEFT JOIN rep_code_translation t
    ON r.rep_code = t.new_rep_code
```

Then:

```
ORDER BY r.rep_code;
```

### Read the whole thing conceptually

`SELECT r.rep_code`

> Give me the Rep Code.

`r.rep_name`

> Give me its business name.

`t.legacy_rep_code`

> Give me its legacy mapping.

`CASE ... END AS mapping_status`

> **Calculate a new output value** based on business rules.

Then:

`FROM rep_code_master r LEFT JOIN ...`

> Get the underlying data.

One more tiny typo in your attempt:

`r.repo_code`

should be:

`r.rep_code`

### Before you run it

Based on our rules, you should predict:

`ABC1 → READY`

`JKL1 → MISSING_MAPPING`

`MNO1 → INACTIVE`

Now construct the complete query and run it.

---

```
fidelity_rep_code_ba_prep=> select r.rep_code, r.rep_name, t.legacy_rep_code, CASE
    WHEN r.active_flag = FALSE THEN 'INACTIVE'
    WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
    ELSE 'READY'
END AS mapping_status from rep_code_master r, rep_code_translation t ORDER BY r.rep_code;
 rep_code |        rep_name         | legacy_rep_code | mapping_status  
----------+-------------------------+-----------------+-----------------
 ABC1     | Smith Advisory Team     | XYZ             | READY
 ABC1     | Smith Advisory Team     | DEF             | READY
 ABC1     | Smith Advisory Team     | GHI             | READY
 ABC1     | Smith Advisory Team     |                 | MISSING_MAPPING
 ABC1     | Smith Advisory Team     | MNO             | READY
 ABC1     | Smith Advisory Team     | PQR             | READY
 DEF1     | Mary Jones              | XYZ             | READY
 DEF1     | Mary Jones              | DEF             | READY
 DEF1     | Mary Jones              | GHI             | READY
 DEF1     | Mary Jones              |                 | MISSING_MAPPING
 DEF1     | Mary Jones              | MNO             | READY
 DEF1     | Mary Jones              | PQR             | READY
 GHI1     | North Region Advisory   | XYZ             | READY
 GHI1     | North Region Advisory   | DEF             | READY
 GHI1     | North Region Advisory   | GHI             | READY
 GHI1     | North Region Advisory   |                 | MISSING_MAPPING
 GHI1     | North Region Advisory   | MNO             | READY
 GHI1     | North Region Advisory   | PQR             | READY
 JKL1     | Legacy Transition Group | XYZ             | READY
 JKL1     | Legacy Transition Group | DEF             | READY
 JKL1     | Legacy Transition Group | GHI             | READY
 JKL1     | Legacy Transition Group |                 | MISSING_MAPPING
 JKL1     | Legacy Transition Group | MNO             | READY
 JKL1     | Legacy Transition Group | PQR             | READY
 MNO1     | Inactive Advisor Group  | XYZ             | INACTIVE
 MNO1     | Inactive Advisor Group  | DEF             | INACTIVE
 MNO1     | Inactive Advisor Group  | GHI             | INACTIVE
 MNO1     | Inactive Advisor Group  |                 | INACTIVE
 MNO1     | Inactive Advisor Group  | MNO             | INACTIVE
 MNO1     | Inactive Advisor Group  | PQR             | INACTIVE
 PQR1     | Trading Support Desk    | XYZ             | READY
 PQR1     | Trading Support Desk    | DEF             | READY
 PQR1     | Trading Support Desk    | GHI             | READY
 PQR1     | Trading Support Desk    |                 | MISSING_MAPPING
 PQR1     | Trading Support Desk    | MNO             | READY
 PQR1     | Trading Support Desk    | PQR             | READY
(36 rows)

fidelity_rep_code_ba_prep=> 
```


---


Exactly — and this output shows **why the JOIN condition matters**.

You got **36 rows** because you used:

`FROM rep_code_master r, rep_code_translation t`

That creates a **Cartesian product**:

**6 Rep Code rows × 6 translation rows = 36 combinations**

So every Rep Code got paired with every translation row.

That’s why you see nonsense combinations like:

`ABC1 → DEF`

`ABC1 → GHI`

`DEF1 → XYZ`

Those are not actual mappings in our lab; SQL just paired every left row with every right row.

## The fix

Use the relationship between the two tables:

`r.rep_code = t.new_rep_code`

with a `LEFT JOIN`.

So the correct shape is:

```
SELECT
    r.rep_code,
    r.rep_name,
    t.legacy_rep_code,
    CASE
        WHEN r.active_flag = FALSE THEN 'INACTIVE'
        WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
        ELSE 'READY'
    END AS mapping_status
FROM rep_code_master r
LEFT JOIN rep_code_translation t
    ON r.rep_code = t.new_rep_code
ORDER BY r.rep_code;
```

### What this should return

Now each Rep Code is paired only with **its own** translation row:

- `ABC1 → XYZ → READY`
    
- `DEF1 → DEF → READY`
    
- `GHI1 → GHI → READY`
    
- `JKL1 → NULL → MISSING_MAPPING`
    
- `MNO1 → MNO → INACTIVE`
    
- `PQR1 → PQR → READY`
    

So instead of **36 rows**, you should get **6 rows**.

### Important lesson

This is the danger of writing:

`FROM table_a, table_b`

without a relationship condition.

It means:

> **Pair every row in A with every row in B.**

That’s called a **Cartesian product** or **cross join**.

For BA work, this is especially dangerous because the query may execute successfully and return lots of data that looks plausible but is completely wrong.

Run the corrected `LEFT JOIN` version and paste the result.

```
fidelity_rep_code_ba_prep=> select r.rep_code, r.rep_name, t.legacy_rep_code, CASE
    WHEN r.active_flag = FALSE THEN 'INACTIVE'
    WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
    ELSE 'READY'
END AS mapping_status from rep_code_master r LEFT JOIN rep_code_translation t ON r.rep_code=t.new_rep_code ORDER BY r.rep_code;
 rep_code |        rep_name         | legacy_rep_code | mapping_status  
----------+-------------------------+-----------------+-----------------
 ABC1     | Smith Advisory Team     | XYZ             | READY
 DEF1     | Mary Jones              | DEF             | READY
 GHI1     | North Region Advisory   | GHI             | READY
 JKL1     | Legacy Transition Group |                 | MISSING_MAPPING
 MNO1     | Inactive Advisor Group  | MNO             | INACTIVE
 PQR1     | Trading Support Desk    | PQR             | READY
(6 rows)

fidelity_rep_code_ba_prep=> 

```


---

Perfect. **8E `CASE` passed.**

You now have a query that turns raw data into a business-readable readiness classification:

- `ABC1` → `READY`
    
- `JKL1` → `MISSING_MAPPING`
    
- `MNO1` → `INACTIVE`
    

That is exactly the kind of thing a BA might use to summarize operational readiness.

One more thing to lock in from the failed attempt:

> A query can run successfully and still be logically wrong.

Your 36-row result was syntactically valid, but because you had no join condition, it created a Cartesian product. That’s a very important SQL/data-analysis lesson.

## 8F — CTE

Now we’ll learn a **CTE**, or Common Table Expression.

Think of it as:

> **Give an intermediate query a name, then query that result as if it were a temporary table.**

We’ll reuse the mapping-status logic you just wrote.

The pattern is:

```
WITH mapping_readiness AS (
    <query here>
)
SELECT *
FROM mapping_readiness;
```

For this exercise, put your existing `SELECT ... CASE ... LEFT JOIN ...` inside the CTE and name it:

`mapping_readiness`

Then outside the CTE, return only:

- `rep_code`
    
- `rep_name`
    
- `mapping_status`
    

where:

`mapping_status <> 'READY'`

This should return just the problematic/non-ready records.

So conceptually:

**CTE**

build all mapping statuses

↓

**outer query**

filter to only non-ready rows

Write it yourself and paste the result. After this, we’ll do one simple subquery and then the short Oracle-vs-Postgres comparison.

---

```
fidelity_rep_code_ba_prep=> WITH mapping_readiness AS (select r.rep_code, r.rep_name, t.legacy_rep_code, CASE                                      
    WHEN r.active_flag = FALSE THEN 'INACTIVE'
    WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
    ELSE 'READY'                                                                           END AS mapping_status from rep_code_master r LEFT JOIN rep_code_translation t ON r.rep_code=t.new_rep_code ORDER BY r.rep_code) select rep_code, rep_name, mapping_status WHERE mapping_status <> 'READY';
ERROR:  column "rep_code" does not exist
LINE 5: ...p_code=t.new_rep_code ORDER BY r.rep_code) select rep_code, ...
                                                             ^
fidelity_rep_code_ba_prep=> WITH mapping_readiness AS (select r.rep_code, r.rep_name, t.legacy_rep_code, CASE
    WHEN r.active_flag = FALSE THEN 'INACTIVE'
    WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
    ELSE 'READY'
END AS mapping_status from rep_code_master r LEFT JOIN rep_code_translation t ON r.rep_code=t.new_rep_code ORDER BY r.rep_code) select rep_code, rep_name, mapping_status from mapping_readiness WHERE mapping_status <> 'READY';
 rep_code |        rep_name         | mapping_status  
----------+-------------------------+-----------------
 JKL1     | Legacy Transition Group | MISSING_MAPPING
 MNO1     | Inactive Advisor Group  | INACTIVE
(2 rows)

fidelity_rep_code_ba_prep=> 

```


---

Perfect. **8F CTE passed.**

Your first attempt failed for one simple reason: the outer query had no `FROM mapping_readiness`, so PostgreSQL had no source for `rep_code`, `rep_name`, or `mapping_status`. You fixed it correctly on the second try.

The pattern to remember is:

`WITH name AS ( ... )`

→ define an intermediate result

then:

`SELECT ... FROM name WHERE ...`

Your result is exactly right:

- `JKL1` → `MISSING_MAPPING`
    
- `MNO1` → `INACTIVE`
    

That is a nice example of using a CTE to make a more complex query easier to read and reason about.

## 8G — One subquery

Business question:

> **Show all orders whose quantity is greater than the average order quantity.**

This is a good use of a subquery because we first need to calculate:

`AVG(quantity)`

from `orders`

and then compare each order's `quantity` against that average.

The shape is:

`SELECT ... FROM orders WHERE quantity > (SELECT AVG(quantity) FROM orders);`

Return:

- `order_id`
    
- `symbol`
    
- `quantity`
    
- `order_status`
    

Sort by `quantity DESC`.

Write it yourself and run it.

After that, I’ll give you a short **PostgreSQL vs Oracle cheat sheet** and we can consider the SQL refresher complete enough for this interview.

---


```
fidelity_rep_code_ba_prep=> select order_id, symbol, quantity, order_status FROM orders where quantity > (SELECT AVG(quantity) from orders) ORDER BY quantity DESC;
 order_id | symbol | quantity |   order_status   
----------+--------+----------+------------------
    50003 | MSFT   |      200 | PARTIALLY_FILLED
    50004 | IBM    |      125 | NEW
    50001 | IBM    |      100 | FILLED
(3 rows)

fidelity_rep_code_ba_prep=> 
```


---

Exactly right. **8G subquery passed.**

Your inner query:

`SELECT AVG(quantity) FROM orders`

calculates the average quantity first. The outer query then asks:

> Which individual orders have `quantity` greater than that calculated value?

You correctly got MSFT 200, IBM 125, and IBM 100.

## PostgreSQL → Oracle quick bridge

For what you'd likely need as a BA, most of what you just practiced transfers directly.

|Concept|PostgreSQL|Oracle|
|---|---|---|
|`SELECT / FROM / WHERE`|Same|Same|
|`INNER JOIN / LEFT JOIN`|Same|Same|
|`GROUP BY / HAVING`|Same|Same|
|`COUNT / SUM / AVG`|Same|Same|
|`CASE`|Same basic syntax|Same basic syntax|
|CTE `WITH`|Supported|Supported|
|Subqueries|Supported|Supported|
|NULL|`IS NULL`|`IS NULL`|
|First N rows|`LIMIT 10`|commonly `FETCH FIRST 10 ROWS ONLY`|
|Boolean columns|Native `BOOLEAN` in PG|differs by Oracle version/context; legacy schemas commonly use flags such as `Y/N` or `1/0`|
|Null replacement|`COALESCE()`|`COALESCE()` and commonly `NVL()`|
|String type|commonly `VARCHAR`|commonly `VARCHAR2`|
|Current timestamp|`CURRENT_TIMESTAMP`|`CURRENT_TIMESTAMP` also available|
|NULL-safe comparison|`IS DISTINCT FROM` available in modern PG|don't assume identical support/behavior across Oracle environments|

You do **not** need to install Oracle just to prepare for this role. The SQL skills we've practiced are overwhelmingly transferable.

## Session 8 — where you are now

I'd call the planned SQL refresher **complete enough for interview preparation**.

You've actually covered quite a bit:

**Retrieval**  
`SELECT`, aliases, `WHERE`, `AND`, comparisons, dates, `ORDER BY`

**Aggregation**  
`COUNT`, `SUM`, `AVG`, `GROUP BY`, `HAVING`

**Relational model**  
PK, FK, parent/child relationships, schema/table discovery with `psql`

**JOINs**  
`INNER JOIN`, `LEFT OUTER JOIN`, `ON`, table aliases

**Data analysis**  
account/order Rep Code mismatch detection, missing translation mappings, trade/mapping reconciliation

**More advanced basics**  
NULL handling, `CASE`, CTEs, subqueries, Cartesian-product mistake detection

And more importantly, you weren't just typing canned SQL. You made several mistakes, diagnosed them, and corrected them. That's considerably more useful preparation than memorizing syntax.

### The interview-level takeaway

If somebody asks about your SQL ability, I would **not** position you as a SQL developer.

Something along these lines is accurate:

> “I use SQL from a Business Analyst and systems-analysis perspective—to query and validate data, join related datasets, investigate mapping and reconciliation issues, trace values across tables, and support testing and production analysis. I'm comfortable with joins, filtering, aggregation, CTEs and basic subqueries.”

That aligns well with what you just demonstrated.

Next on our agenda is **Session 9 — JD bullet-by-bullet mapping**, which is one of today's three must-finish items. Before starting it, we should also persist today's SQL exercises/progress into `fidelity-rep-code-ba-prep` so none of this stays only in the chat.


---




---

