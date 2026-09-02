---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 8 — SQL PostgresSQL
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-30
description:
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---
---

# How I normaly connect

Yes — and I’ve already created the seed file for the lab.

[Download the PostgreSQL seed data](sandbox:/mnt/data/fidelity-rep-code-sql-lab.sql)

> [!PostgresSQL seed data]-
> -- Fidelity Rep Code SQL Lab (PostgreSQL)
> -- Conceptual training data only; not Fidelity production schema/data.
> 
> DROP SCHEMA IF EXISTS fidelity_lab CASCADE;
> CREATE SCHEMA fidelity_lab;
> SET search_path TO fidelity_lab;
> 
> CREATE TABLE rep_code_master (
>     rep_code        VARCHAR(4) PRIMARY KEY,
>     rep_name        VARCHAR(100) NOT NULL,
>     rep_type        VARCHAR(30) NOT NULL,
>     active_flag     BOOLEAN NOT NULL DEFAULT TRUE
> );
> 
> CREATE TABLE rep_code_translation (
>     new_rep_code    VARCHAR(4) PRIMARY KEY,
>     legacy_rep_code VARCHAR(3),
>     active_flag     BOOLEAN NOT NULL DEFAULT TRUE,
>     CONSTRAINT fk_translation_rep
>         FOREIGN KEY (new_rep_code) REFERENCES rep_code_master(rep_code)
> );
> 
> CREATE TABLE client_account (
>     account_id      BIGINT PRIMARY KEY,
>     client_name     VARCHAR(100) NOT NULL,
>     rep_code        VARCHAR(4),
>     account_status  VARCHAR(20) NOT NULL,
>     CONSTRAINT fk_account_rep
>         FOREIGN KEY (rep_code) REFERENCES rep_code_master(rep_code)
> );
> 
> CREATE TABLE orders (
>     order_id        BIGINT PRIMARY KEY,
>     account_id      BIGINT NOT NULL,
>     rep_code        VARCHAR(4),
>     symbol          VARCHAR(12) NOT NULL,
>     side            VARCHAR(4) NOT NULL,
>     quantity        INTEGER NOT NULL,
>     order_status    VARCHAR(30) NOT NULL,
>     created_at      TIMESTAMP NOT NULL,
>     CONSTRAINT fk_order_account
>         FOREIGN KEY (account_id) REFERENCES client_account(account_id)
> );
> 
> CREATE TABLE executions (
>     execution_id    BIGINT PRIMARY KEY,
>     order_id        BIGINT NOT NULL,
>     executed_qty    INTEGER NOT NULL,
>     executed_price  NUMERIC(12,2) NOT NULL,
>     executed_at     TIMESTAMP NOT NULL,
>     CONSTRAINT fk_execution_order
>         FOREIGN KEY (order_id) REFERENCES orders(order_id)
> );
> 
> CREATE TABLE trades (
>     trade_id        BIGINT PRIMARY KEY,
>     order_id        BIGINT NOT NULL,
>     account_id      BIGINT NOT NULL,
>     rep_code        VARCHAR(4),
>     legacy_rep_code VARCHAR(3),
>     symbol          VARCHAR(12) NOT NULL,
>     quantity        INTEGER NOT NULL,
>     trade_status    VARCHAR(30) NOT NULL,
>     CONSTRAINT fk_trade_order
>         FOREIGN KEY (order_id) REFERENCES orders(order_id),
>     CONSTRAINT fk_trade_account
>         FOREIGN KEY (account_id) REFERENCES client_account(account_id)
> );
> 
> INSERT INTO rep_code_master (rep_code, rep_name, rep_type, active_flag) VALUES
> ('ABC1', 'Smith Advisory Team', 'TEAM', TRUE),
> ('DEF1', 'Mary Jones', 'INDIVIDUAL', TRUE),
> ('GHI1', 'North Region Advisory', 'TEAM', TRUE),
> ('JKL1', 'Legacy Transition Group', 'TEAM', TRUE),
> ('MNO1', 'Inactive Advisor Group', 'TEAM', FALSE),
> ('PQR1', 'Trading Support Desk', 'ORDER_ROLE', TRUE);
> 
> INSERT INTO rep_code_translation (new_rep_code, legacy_rep_code, active_flag) VALUES
> ('ABC1', 'XYZ', TRUE),
> ('DEF1', 'DEF', TRUE),
> ('GHI1', 'GHI', TRUE),
> ('JKL1', NULL, TRUE),
> ('MNO1', 'MNO', FALSE),
> ('PQR1', 'PQR', TRUE);
> 
> INSERT INTO client_account (account_id, client_name, rep_code, account_status) VALUES
> (10001, 'Paul Client', 'ABC1', 'ACTIVE'),
> (10002, 'Jane Investor', 'DEF1', 'ACTIVE'),
> (10003, 'Robert Client', 'GHI1', 'ACTIVE'),
> (10004, 'Acme Family Trust', 'ABC1', 'ACTIVE'),
> (10005, 'Northshore LLC', 'JKL1', 'ACTIVE'),
> (10006, 'Old Account', 'MNO1', 'CLOSED');
> 
> INSERT INTO orders (order_id, account_id, rep_code, symbol, side, quantity, order_status, created_at) VALUES
> (50001, 10001, 'ABC1', 'IBM',  'BUY',  100, 'FILLED',           '2026-08-20 09:35:00'),
> (50002, 10002, 'DEF1', 'AAPL', 'BUY',   50, 'FILLED',           '2026-08-20 10:15:00'),
> (50003, 10003, 'GHI1', 'MSFT', 'SELL', 200, 'PARTIALLY_FILLED', '2026-08-20 11:10:00'),
> (50004, 10004, 'ABC1', 'IBM',  'BUY',  125, 'NEW',              '2026-08-21 09:05:00'),
> (50005, 10005, 'JKL1', 'NVDA', 'BUY',   75, 'FILLED',           '2026-08-21 13:25:00'),
> (50006, 10001, 'DEF1', 'TSLA', 'BUY',   25, 'FILLED',           '2026-08-21 14:10:00');
> 
> INSERT INTO executions (execution_id, order_id, executed_qty, executed_price, executed_at) VALUES
> (70001, 50001,  40, 250.00, '2026-08-20 09:36:10'),
> (70002, 50001,  60, 250.05, '2026-08-20 09:36:25'),
> (70003, 50002,  50, 225.50, '2026-08-20 10:16:12'),
> (70004, 50003, 100, 410.25, '2026-08-20 11:12:30'),
> (70005, 50005,  75, 135.75, '2026-08-21 13:27:05'),
> (70006, 50006,  25, 340.10, '2026-08-21 14:11:15');
> 
> INSERT INTO trades (trade_id, order_id, account_id, rep_code, legacy_rep_code, symbol, quantity, trade_status) VALUES
> (90001, 50001, 10001, 'ABC1', 'XYZ', 'IBM',  100, 'SETTLED'),
> (90002, 50002, 10002, 'DEF1', 'DEF', 'AAPL',  50, 'SETTLED'),
> (90003, 50003, 10003, 'GHI1', 'GHI', 'MSFT', 100, 'PENDING'),
> (90004, 50005, 10005, 'JKL1', NULL,  'NVDA',  75, 'EXCEPTION'),
> (90005, 50006, 10001, 'DEF1', 'DEF', 'TSLA',  25, 'SETTLED');
> 
> -- Intentional data-quality scenarios:
> -- 50006 uses DEF1 even though account 10001 is assigned ABC1.
> -- JKL1 has no legacy mapping, creating an exception scenario.
> 


It creates a `fidelity_lab` schema with these tables:

- `rep_code_master`
- `rep_code_translation`
- `client_account`
- `orders`
- `executions`
- `trades`
    

The data includes deliberate scenarios we’ll investigate later, such as a **Rep Code mismatch between account and order** and a **missing legacy translation mapping**.

## Session 8 — SQL Refresher Plan

We’ll do this progressively, not all at once:

| Stage  | Topic                      | What you'll learn                                                |
| ------ | -------------------------- | ---------------------------------------------------------------- |
| **8A** | Basic `SELECT`             | Inspect tables and columns                                       |
| **8B** | `WHERE`, `ORDER BY`        | Filter Rep Codes, accounts, orders, statuses                     |
| **8C** | Aggregates                 | `COUNT`, `SUM`, `AVG`, `GROUP BY`, `HAVING`                      |
| **8D** | **JOINs**                  | Account → Rep → Order → Trade relationships                      |
| **8E** | Data-quality investigation | Find mismatches, missing mappings, orphan-like conditions        |
| **8F** | Lineage/reconciliation     | Trace Rep Code from account → order → trade → legacy translation |
| **8G** | CTEs / subqueries / `CASE` | More realistic BA analysis                                       |
| **8H** | Oracle differences         | Small cheat sheet only after PostgreSQL SQL is comfortable       |

The emphasis will be **BA/data-analysis SQL**, not database administration or PL/SQL.

# First: load the lab

Assuming PostgreSQL is already running, let's first find out how you normally connect.

Try:

```
psql --version
```

Then:

```
psql -l
```

If `psql -l` works, show me the output. From there I'll give you the exact command to create/use a practice database and load `~/Downloads/fidelity-rep-code-sql-lab.sql`.

If you've downloaded the file from ChatGPT, it should land in `~/Downloads`, so **don't load it yet until we confirm which database you want to use**.

After that, our very first SQL exercise will be intentionally simple:

> **Show me every active Rep Code and what it represents.**

Then we'll progressively build toward questions like:

> **Which orders carry a Rep Code that doesn't match the account's assigned Rep Code?**

That second question will eventually require a `JOIN`, but I'll make you build up to it rather than just giving you the answer.

And yes — I’ll remind you later about:  
**the diagram visual review** and **deferred Session 7 BA Discovery Exercise**.

# Confirm the PostgreSQL server and administrative account

Good — PostgreSQL itself is installed. The error is straightforward:

> `FATAL: role "pl" does not exist`

`psql` is using your Linux username `pl` as the default PostgreSQL username, but PostgreSQL doesn't currently have a database role named `pl`.

We can set this up cleanly for the new **`fidelity-rep-code-ba-prep`** lab.

First, let's confirm the PostgreSQL server and administrative account. Run:

```
sudo -u postgres psql -l
```

That should list the existing databases using PostgreSQL's built-in `postgres` administrative role.

Then also run:

```
sudo -u postgres psql -c "\du"
```

That will show the existing PostgreSQL roles.

Paste both outputs here. **Don't create anything yet.** Once I see what's already there, we'll create a dedicated setup such as:

`PostgreSQL role: pl`

`Database: fidelity_rep_code_ba_prep`

`Schema: fidelity_lab`

Then you'll be able to connect naturally from your normal Linux account, and we'll load the canned dataset into that database before beginning Exercise 8A.


```
[PL] pl@pop-os:~ $ sudo -u postgres psql -l
[sudo] password for pl: 
could not change directory to "/home/pl": Permission denied
                                    List of databases
     Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
---------------+----------+----------+-------------+-------------+-----------------------
 career_center | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/postgres         +
               |          |          |             |             | postgres=CTc/postgres+
               |          |          |             |             | career_app=c/postgres
 demo          | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 mydb          | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 questiondb    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 quizdb        | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 squidpan      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
 template1     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
(9 rows)

[PL] pl@pop-os:~ $ 

```


Good. PostgreSQL is running fine; the only issue is that your normal Linux user `pl` does not yet exist as a PostgreSQL role.

Also, this line is harmless:

> `could not change directory to "/home/pl": Permission denied`

That happens because the `postgres` OS user cannot enter your home directory. It does **not** mean PostgreSQL failed.

Now run the second command we planned:

```
sudo -u postgres psql -c "\du"
```

That will show the existing PostgreSQL roles.

Once I see that, we’ll create a dedicated role/database cleanly for the lab—most likely:

`role: pl`

`database: fidelity_rep_code_ba_prep`

Then you’ll be able to connect with something simple like:

```
psql -d fidelity_rep_code_ba_prep
```

and load the seed data into the `fidelity_lab` schema.

```
[PL] pl@pop-os:~ $ sudo -u postgres psql -c "\du"
could not change directory to "/home/pl": Permission denied
                                    List of roles
 Role name  |                         Attributes                         | Member of 
------------+------------------------------------------------------------+-----------
 career_app |                                                            | {}
 postgres   | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

[PL] pl@pop-os:~ $ 
```


---

Perfect. There is no existing `pl` PostgreSQL role, so we can create one cleanly and give it ownership of a dedicated practice database.

Run these two commands:

```
sudo -u postgres createuser --createdb pl

sudo -u postgres createdb -O pl fidelity_rep_code_ba_prep
```

Then test:

## Show current_user current_database()

```
psql -d fidelity_rep_code_ba_prep -c "SELECT current_user, current_database();"
```

You should see roughly:

`current_user = pl`

`current_database = fidelity_rep_code_ba_prep`

After that, assuming the SQL seed file is in `~/Downloads`, load it with:

```
psql -d fidelity_rep_code_ba_prep -f ~/Downloads/fidelity-rep-code-sql-lab.sql
```

Then verify the schema/tables:

```
psql -d fidelity_rep_code_ba_prep -c "\dt fidelity_lab.*"
```

If those work, paste the output and we’ll start **Exercise 8A — basic SELECT**, using the canned Rep Code data rather than generic sample tables.

---


```
[PL] pl@pop-os:~ $ sudo -u postgres createuser --createdb pl

sudo -u postgres createdb -O pl fidelity_rep_code_ba_prep
could not change directory to "/home/pl": Permission denied
could not change directory to "/home/pl": Permission denied
[PL] pl@pop-os:~ $ psql -d fidelity_rep_code_ba_prep -c "SELECT current_user, current_database();"
 current_user |     current_database      
--------------+---------------------------
 pl           | fidelity_rep_code_ba_prep
(1 row)

[PL] pl@pop-os:~ $ 
```


Great. The database and `pl` PostgreSQL role are set up correctly.

## Now load the seed data:

```
psql -d fidelity_rep_code_ba_prep -f ~/Downloads/fidelity-rep-code-sql-lab.sql
```

## Then verify the tables: list all tables in a schema

```
psql -d fidelity_rep_code_ba_prep -c "\dt fidelity_lab.*"
```

If that works, also run:

```
psql -d fidelity_rep_code_ba_prep -c "SELECT * FROM fidelity_lab.rep_code_master ORDER BY rep_code;"
```

That will be our first sanity check before we start **Exercise 8A — basic SELECT**.

And yes, the “could not change directory” messages from the `sudo -u postgres` commands were harmless, as expected.

```
[PL] pl@pop-os:~ $ sudo -u postgres createuser --createdb pl

sudo -u postgres createdb -O pl fidelity_rep_code_ba_prep
could not change directory to "/home/pl": Permission denied
could not change directory to "/home/pl": Permission denied
[PL] pl@pop-os:~ $ psql -d fidelity_rep_code_ba_prep -c "SELECT current_user, current_database();"
 current_user |     current_database      
--------------+---------------------------
 pl           | fidelity_rep_code_ba_prep
(1 row)

[PL] pl@pop-os:~ $ psql -d fidelity_rep_code_ba_prep -f ~/Downloads/fidelity-rep-code-sql-lab.sql
psql:/home/pl/Downloads/fidelity-rep-code-sql-lab.sql:4: NOTICE:  schema "fidelity_lab" does not exist, skipping
DROP SCHEMA
CREATE SCHEMA
SET
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
INSERT 0 6
INSERT 0 6
INSERT 0 6
INSERT 0 6
INSERT 0 6
INSERT 0 5
[PL] pl@pop-os:~ $ psql -d fidelity_rep_code_ba_prep -c "\dt fidelity_lab.*"
                  List of relations
    Schema    |         Name         | Type  | Owner 
--------------+----------------------+-------+-------
 fidelity_lab | client_account       | table | pl
 fidelity_lab | executions           | table | pl
 fidelity_lab | orders               | table | pl
 fidelity_lab | rep_code_master      | table | pl
 fidelity_lab | rep_code_translation | table | pl
 fidelity_lab | trades               | table | pl
(6 rows)

[PL] pl@pop-os:~ $ psql -d fidelity_rep_code_ba_prep -c "SELECT * FROM fidelity_lab.rep_code_master ORDER BY rep_code;"
 rep_code |        rep_name         |  rep_type  | active_flag 
----------+-------------------------+------------+-------------
 ABC1     | Smith Advisory Team     | TEAM       | t
 DEF1     | Mary Jones              | INDIVIDUAL | t
 GHI1     | North Region Advisory   | TEAM       | t
 JKL1     | Legacy Transition Group | TEAM       | t
 MNO1     | Inactive Advisor Group  | TEAM       | f
 PQR1     | Trading Support Desk    | ORDER_ROLE | t
(6 rows)

[PL] pl@pop-os:~ $ 

```

---

Perfect. The lab is loaded correctly and all six tables are owned by `pl`. We can start **Session 8A — Basic SELECT**.

For the SQL refresher, I want you to **type the queries yourself** rather than copy finished answers whenever possible. I’ll give you the business question, a small syntax reminder when needed, then we’ll review your result.


## Describe all fields in tables of a schema - pqsl




## 8A — Basic `SELECT`

First enter the database interactively:


#### Enter db interactively 
```
psql -d fidelity_rep_code_ba_prep
```

#### Set the working schema so you don't have to keep typing `fidelity_lab.`:

```
SET search_path TO fidelity_lab;
```

You should then see a prompt similar to:

```
fidelity_rep_code_ba_prep=>
```

### Exercise 8A-1 — Look at the whole Rep Code master

Business question:

> **What Rep Codes exist, what do they represent, and which are active?**

You already effectively ran this once, but now do it from inside `psql`:

```
SELECT *
FROM rep_code_master
ORDER BY rep_code;
```

Notice the columns:

`rep_code` — identifier  
`rep_name` — business meaning/name  
`rep_type` — team, individual, order role, etc.  
`active_flag` — active/inactive

This table is our conceptual **authoritative Rep Code reference data** for the lab.

---

## Exercise 8A-2 — Select only the columns you actually need

Instead of `SELECT *`, suppose the BA question is:

> **Show me every Rep Code and the business name it represents.**

Write a query selecting only:

`rep_code`  
`rep_name`

from:

`rep_code_master`

Don't use `SELECT *`.

Run it and paste your query + output.

---

## Exercise 8A-3 — Filter active Rep Codes

Next business question:

> **Which Rep Codes are currently active?**

For this one you'll need:

```
WHERE active_flag = TRUE
```

But **you construct the complete query**.

Return:

`rep_code`  
`rep_name`  
`rep_type`

and sort by:

`rep_code`

---

## Exercise 8A-4 — Filter by business type

Then we'll ask:

> **Which active Rep Codes represent TEAMS?**

You'll combine two conditions:

`rep_type = 'TEAM'`

and

`active_flag = TRUE`

using:

`AND`

This is already moving toward real BA investigation:

> "Show me the active advisor-team constructs affected by Rep Code Expansion."

---

### One important SQL habit

Start thinking of every query as:

**Business question**

↓

**Which table contains the data?**

↓

**Which columns do I need?**

↓

**Which rows do I need?**

↓

**How should the result be ordered/grouped?**

That becomes:

`SELECT`
↓
`FROM`
↓
`WHERE`
↓
`ORDER BY`

Later we'll add:

`JOIN`
`GROUP BY`
`HAVING`
and CTEs.

For now, do **8A-2 first** and paste your query and result. We'll go one exercise at a time rather than racing through them.

---


Perfect. I can see **pgAdmin is connected to `fidelity_rep_code_ba_prep`**, the `fidelity_lab` schema and six tables are visible, and your query against `client_account` returned the six seeded accounts correctly. Your terminal is also sitting inside the database with:

`search_path = fidelity_lab`

So we have **two useful ways to work**:

- **psql** — I want you comfortable here because it reinforces SQL itself.
    
- **pgAdmin** — excellent for visually inspecting tables, columns, constraints, results, and later joins.
    

We'll use both.

## Session 8A — Exercise 2

You're currently at:

```
fidelity_rep_code_ba_prep=>
```

Business asks:

> **Show me every Rep Code and the business name it represents.**

You know the table:

`rep_code_master`

And you only need:

`rep_code`  
`rep_name`

### Your task

Write the SQL yourself.

Think:

**SELECT** → which columns?

**FROM** → which table?

**ORDER BY** → let's sort by `rep_code`.

Don't use `SELECT *`.

Run it in `psql` and paste your **query and result** here.

### One thing I noticed in pgAdmin

You've already done something useful without us formally covering it:

`ORDER BY account_id ASC`

`ASC` means **ascending**. It's also the default, so these are equivalent:

`ORDER BY account_id`

and

`ORDER BY account_id ASC`

We'll get to `DESC` shortly.

Go ahead with **8A-2**.

---

You're in **psql's multiline mode** because the first statement wasn't terminated with a semicolon.

Notice the prompt changed:

`fidelity_rep_code_ba_prep=>` = ready for a **new command**

`fidelity_rep_code_ba_prep->` = PostgreSQL thinks you're **still typing the previous command**

You currently have something equivalent to two `SELECT`s mashed into one unfinished statement.

Cancel the unfinished command with:

```
\r
```

You should see:

`Query buffer reset (cleared).`

and return to:

```
fidelity_rep_code_ba_prep=>
```

Then let's do **8A-2** again.

The business question is:

> Show every Rep Code **and its business name**, sorted by Rep Code.

You started correctly with:

`SELECT rep_code ...`

But we need **two columns**.

### Small syntax reminder

Multiple selected columns are separated by commas:

`SELECT column1, column2`

So construct:

**SELECT:** `rep_code` + `rep_name`  
**FROM:** `rep_code_master`  
**ORDER BY:** `rep_code`

And this time end the complete statement with:

`;`

Don't worry about capitalization—`select`, `SELECT`, `from`, `FROM` all work. I generally capitalize SQL keywords because it makes queries easier to scan.

Run yours and show me the result.

---

```
fidelity_rep_code_ba_prep=> select * from rep_code_master
fidelity_rep_code_ba_prep-> select rep_code from rep_code_master 
fidelity_rep_code_ba_prep-> \r
Query buffer reset (cleared).
fidelity_rep_code_ba_prep=> select * from rep_code_master
fidelity_rep_code_ba_prep-> \r
Query buffer reset (cleared).
fidelity_rep_code_ba_prep=> select rep_code from rep_code_master
fidelity_rep_code_ba_prep-> \r
Query buffer reset (cleared).
fidelity_rep_code_ba_prep=> select rep_code, rep_name from rep_code_master order by rep_code
fidelity_rep_code_ba_prep-> 
```


---

Exactly — your SQL is now correct. You're just missing the **semicolon** that tells `psql`, “execute this statement.”

You're currently at:

`fidelity_rep_code_ba_prep->`

Type just:

```
;
```

and press Enter.

Your complete statement will then be:

`SELECT rep_code, rep_name FROM rep_code_master ORDER BY rep_code;`

### Key `psql` lesson

The semicolon is what **terminates the SQL statement**.

That's why earlier:

`select * from rep_code_master`

didn't execute. PostgreSQL was waiting for more input.

Remember the prompts:

`=>` = ready for a new statement  
`->` = statement isn't finished yet

And `\r` = throw away/reset whatever unfinished SQL is in the query buffer.

Type `;`, show me the result, and then we'll do **8A-3: `WHERE` filtering**.


---

```
fidelity_rep_code_ba_prep-> \r
Query buffer reset (cleared).
fidelity_rep_code_ba_prep=> select rep_code, rep_name from rep_code_master order by rep_code;
 rep_code |        rep_name         
----------+-------------------------
 ABC1     | Smith Advisory Team
 DEF1     | Mary Jones
 GHI1     | North Region Advisory
 JKL1     | Legacy Transition Group
 MNO1     | Inactive Advisor Group
 PQR1     | Trading Support Desk
(6 rows)

fidelity_rep_code_ba_prep=> 

```



---

Perfect. **8A-2 passed.** And the semicolon lesson is now probably permanently burned in. 🙂

Your query:

`SELECT rep_code, rep_name FROM rep_code_master ORDER BY rep_code;`

did exactly what the business question required: selected only the two needed attributes and sorted the result.

## 8A-3 — `WHERE`

Now the business asks:

> **Show me only the currently active Rep Codes.**

Return these three columns:

`rep_code`  
`rep_name`  
`rep_type`

You already know:

**SELECT** — what columns?  
**FROM** — what table?  
**ORDER BY** — how should results appear?

Now add:

**WHERE** — which rows qualify?

The condition you need is:

`active_flag = TRUE`

So the basic structure is:

`SELECT ... FROM ... WHERE ... ORDER BY ... ;`

### Your turn

Write the complete query yourself and sort by `rep_code`.

One thing to predict **before running it**: we currently have **6 Rep Codes**. How many rows do you expect this query to return?

Run it and paste the query/result.


---

Exactly. **8A-4 passed.**

Your query correctly combined two predicates:

`active_flag = TRUE`

**AND**

`rep_type = 'TEAM'`

and returned the expected three active teams: `ABC1`, `GHI1`, and `JKL1`.

You now have the basic pattern:

`SELECT → FROM → WHERE → ORDER BY`

Let's make it more business-oriented.

## 8A-5 — Move to Accounts

Business question:

> **Show me all ACTIVE client accounts, including the account number, client name, and assigned Rep Code. Sort by account number.**

First inspect the table if you don't remember its structure:

```
\d client_account
```

That `\d` is a **psql command**, not SQL. It shows the table definition.

Then construct the query yourself.

You'll need these columns:

`account_id`  
`client_name`  
`rep_code`

Filter:

`account_status = 'ACTIVE'`

Sort:

`account_id`

### Think about what we're doing conceptually

Now we're moving from:

**Rep reference data**

to:

**Account → Rep relationship**

For example:

`Account 10001 → ABC1`

That's going to become important when we reach JOINs, because eventually we'll ask SQL:

> Account 10001 says its Rep is `ABC1`, but an order for that account says its Rep is `DEF1`. **Find that inconsistency.**

Don't jump there yet. 🙂

Run **8A-5** yourself and paste the query/result.


---














