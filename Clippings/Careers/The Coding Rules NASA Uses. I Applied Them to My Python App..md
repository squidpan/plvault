---
categories:
  - "[[Clippings]]"
title: "The Coding Rules NASA Uses. I Applied Them to My Python App."
source: "https://blog.venturemagazine.net/the-coding-rules-nasa-uses-i-applied-them-to-my-python-app-8b8dd5254736"
author:
  - "[[inprogrammer]]"
published: 2026-04-01
created: 2026-06-23
description: "NASA's Jet Propulsion Laboratory has ten coding rules designed for software running on Mars rovers and space probes where a bug cannot be patched and a failure can mean losing a mission worth hundreds of millions of dollars."
tags:
  - "clippings"
url: "https://blog.venturemagazine.net/the-coding-rules-nasa-uses-i-applied-them-to-my-python-app-8b8dd5254736"
---
## Rules designed for Mars rovers revealed two bugs that had been hiding in production for months.

![The Coding Rules NASA Uses. I Applied Them to My Python App.](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*edmFtg_mvsCENBW2jqZYcA.png)

Gemini (nano banana)

NASA’s Jet Propulsion Laboratory follows a strict set of coding rules called the Power of Ten, written by Gerard Holzmann.

These rules were made for C programs used in Mars rovers and space missions, where even a small bug cannot be fixed later and can cause a huge failure.

This made me curious. What would happen if I used these same rules in a simple Python FastAPI app on Earth? Not because the risk is the same, but because rules that remove common bugs might reveal problems I normally miss.

Here is what I found.

**Friend link for nonmember-** [**https://medium.com/@inprogrammer/the-coding-rules-nasa-uses-i-applied-them-to-my-python-app-8b8dd5254736?sk=1221993a4ec59951946f81f6b7a36eb3**](https://medium.com/@inprogrammer/the-coding-rules-nasa-uses-i-applied-them-to-my-python-app-8b8dd5254736?sk=1221993a4ec59951946f81f6b7a36eb3)

## The Rules and What They Mean

## Rule 1: Restrict to Simple Control Flow

No `goto` statements. No `setjmp` or `longjmp`. No recursion.

The idea is simple. When control flow becomes complex, it gets very hard to understand what the program will actually do. If you cannot clearly follow the path your code takes, you cannot be confident that it is correct.

**Applied to Python:**

Python does not have `goto`, but it still has its own traps. Deeply nested `if` statements, recursive functions without clear base cases, and using exceptions to control normal flow all create the same kind of confusion.

They make the code harder to follow. And once you cannot easily trace what is happening, it becomes much harder to trust that the code is correct.

```c
# Violates the rule - exception as control flow
def get_user(user_id):
    try:
        return db.query(User).filter(User.id == user_id).first()
    except:
        return None
```
```c
# Follows the rule - explicit control flow
def get_user(user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        logger.warning("User not found", extra={"user_id": user_id})
    return user
```

==The second version makes the None case explicit and visible==. The first version hides it inside a broad exception catch that swallows any error silently.

**What changed in my app:** I found six functions using bare except clauses that were hiding real errors. Fixing them revealed two bugs that had been silently failing in production.

## Rule 2: Give All Loops a Fixed Upper Bound

Every loop must have a clear upper limit. You should be able to prove how many times it can run. ==If a loop can run forever, it should not exist.==

The reason is simple. Infinite loops are one of the most common causes of systems getting stuck. In safety critical software, even one such loop can freeze the entire system.

**Applied to Python:**

While loops without a clear termination condition are the main offender here.

```c
# Violates the rule - no upper bound
while not task_complete:
    process_next_item()
    time.sleep(1)
```
```c
# Follows the rule - explicit upper bound
MAX_ATTEMPTS = 300
for attempt in range(MAX_ATTEMPTS):
    if task_complete:
        break
    process_next_item()
    time.sleep(1)
else:
    logger.error("Task did not complete within timeout")
    raise TaskTimeoutError("Exceeded maximum attempts")
```

The second version will always terminate. The first version will run forever if `task_complete` never becomes True due to a bug elsewhere.

**What changed in my app:** Three while loops in background tasks had no upper bound. Under specific failure conditions they would have run indefinitely, consuming resources until the server ran out of memory.

## Rule 3: Do Not Use Dynamic Memory Allocation After Initialization

In C this means no malloc after startup. In Python this translates to being careful about unbounded data structures that grow during runtime.

**Applied to Python:**

Lists that grow without limit inside long running processes are the Python equivalent of this problem.

```c
# Violates the rule - unbounded growth
class EventProcessor:
    def __init__(self):
        self.processed_events = []
```
```c
def process(self, event):
        result = handle_event(event)
        self.processed_events.append(result)
        return result# Follows the rule - bounded storage
from collections import dequeclass EventProcessor:
    def __init__(self, max_history=1000):
        self.processed_events = deque(maxlen=max_history)    def process(self, event):
        result = handle_event(event)
        self.processed_events.append(result)
        return result
```

The deque with maxlen automatically discards old entries when the limit is reached. The list grows forever and eventually causes a memory problem.

**What changed in my app:** This rule directly connected to the memory leak I had fixed previously. An unbounded list in a long running background process was the root cause.

## Rule 4: Keep Functions Small and Single Purpose

No function should be longer than what fits on a single printed page. In practice this means under 60 lines with a single clear responsibility.

**Applied to Python:**

Long functions that do multiple things are harder to test, harder to understand, and harder to change safely.

```c
# Violates the rule - one function doing everything
@app.post("/orders")
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    user = await db.execute(select(User).where(User.id == order.user_id))
    user = user.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.balance < order.total:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    new_order = Order(**order.dict())
    db.add(new_order)
    user.balance -= order.total
    await db.commit()
    await send_confirmation_email(user.email, new_order.id)
    await update_inventory(order.items)
    return new_order
```
```c
# Follows the rule - separated responsibilities
@app.post("/orders")
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    user = await get_verified_user(db, order.user_id)
    await verify_sufficient_balance(user, order.total)
    new_order = await save_order(db, order, user)
    await post_order_tasks(user, new_order, order.items)
    return new_order
```

The second version is easier to test because each function has one job. It is easier to read because each function name describes exactly what it does.

**What changed in my app:** I found four route handlers that were doing six to eight things each. Splitting them revealed two places where error handling was missing for specific steps.

## Rule 5: Use Assertions Liberally

Assert that conditions you believe to be true actually are true. If an assertion fails, something has gone wrong that you did not anticipate.

**Applied to Python:**

Python’s assert statement is disabled when running in optimized mode. For production use, explicit checks with proper error handling are more reliable.

```c
# Using assert - disabled in production with -O flag
def calculate_discount(amount, rate):
    assert amount > 0, "Amount must be positive"
    assert 0 <= rate <= 1, "Rate must be between 0 and 1"
    return amount * rate
```
```c
# Production equivalent - always runs
def calculate_discount(amount: float, rate: float) -> float:
    if amount <= 0:
        raise ValueError(f"Amount must be positive, got {amount}")
    if not 0 <= rate <= 1:
        raise ValueError(f"Rate must be between 0 and 1, got {rate}")
    return amount * rate
```

Pydantic validators serve the same purpose at the API boundary. Internal functions benefit from explicit checks that remain active in production.

**What changed in my app:** Adding explicit checks to internal utility functions caught three cases where incorrect data was being passed between functions silently.

## What Actually Improved

After applying these five rules to my FastAPI app for two weeks, I noticed three clear changes.

First, I started finding more bugs during development. Clear control flow and limited loops made problems show up during testing instead of later in production.

Second, I discovered two real production bugs just by removing `bare except` blocks. Those errors were being hidden for months without anyone noticing.

Third, code reviews became faster. When each function does only one thing, it is much easier to understand and review.

## What Did Not Translate Directly

Not every NASA rule makes sense for a web application.

The rule about avoiding dynamic memory is critical for embedded systems with fixed resources. But in a web app that handles changing traffic, dynamic memory is normal and necessary.

The rule about avoiding recursion matters in systems without protection against stack overflow. Python already has limits in place, and most web apps do not use recursion in risky ways.

The real value is not in following every rule exactly. It is in understanding why the rule exists and applying that thinking to the real risks in your own system.

## The Broader Lesson

NASA’s Jet Propulsion Laboratory rules exist because failure can be catastrophic. Most web applications do not have that level of risk.

But the idea behind them still matters. Rules that remove whole categories of bugs are more powerful than rules that catch just one. A `bare except` does not create a single bug. It hides every bug inside that block.

Simple control flow does not prevent only one type of mistake. It makes all mistakes easier to see and fix.

The rules are strict because extreme reliability is needed. The thinking behind them is useful in any kind of software.

## CTA

If this changed how you think about reliability, follow me on Medium. I share real Python and FastAPI production fixes with actual results.

Tried these rules in your code? Drop your findings in the comments.

**Also, check my other article-** [**https://medium.com/stackademic/i-rewrote-200-lines-of-pandas-code-into-20-here-is-how-193dda3335dd**](https://medium.com/stackademic/i-rewrote-200-lines-of-pandas-code-into-20-here-is-how-193dda3335dd)