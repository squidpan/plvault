---
categories:
  - "[[Topics]]"
  - "[[Jobs]]"
url:
created: 2026-04-15
last: 2026-04-15
type:
tags:
  - nutshell
---
What are Synthetic BBO (best bid/offer) and conflation (reduce message rate) and how does redline feed support it. Are these customizations that customers of Redline feed code into the application?

Great question—this is exactly the kind of **product + systems understanding** Pico is looking for.

Let’s break it down clearly and then answer your key question about **who implements it**.

---

# 🧠 1. What is BBO (Best Bid/Offer)?

## ✅ Simple definition

> BBO is the best (highest) bid and the best (lowest) ask available in the market at a given time.

---

## Example (single exchange)

Bids (buyers)       Asks (sellers)  
99.99 (200)         100.01 (150)  
99.98 (300)         100.02 (400)

👉 BBO:

- Best bid = 99.99
- Best ask = 100.01

---

# 🔥 2. What is **Synthetic BBO**?

## ✅ Definition

> Synthetic BBO combines the best bid and ask across multiple venues or sources to produce a consolidated “best price”.

---

## Example (multi-exchange)

### Exchange A:

- Bid: 99.99
- Ask: 100.02

### Exchange B:

- Bid: 100.00
- Ask: 100.01

---

## Synthetic BBO:

- Best bid = **100.00** (from B)
- Best ask = **100.01** (from B)

---

## 💡 Key idea

> Synthetic BBO = “best price across markets”

---

## 🎯 Why it matters

- Traders want **best execution price**
- Useful for:
    - Smart order routing
    - Arbitrage

---

# ⚡ 3. What is Conflation?

## ✅ Definition

> Conflation reduces the number of market data messages by combining multiple updates into fewer updates over a short time window.

---

## Example (no conflation)

Tick 1 → price = 100.00  
Tick 2 → price = 100.01  
Tick 3 → price = 100.02  
Tick 4 → price = 100.03

👉 4 messages sent

---

## With conflation (e.g., 100ms window)

Send only latest → price = 100.03

👉 1 message sent

---

## 💡 Key idea

> Conflation trades **accuracy/granularity for lower message rate**

---

# ⚖️ 4. Why conflation is used

## Benefits:

- Lower CPU usage
- Lower network load
- Easier for downstream systems

---

## Trade-off:

- Slightly stale data
- Not suitable for HFT

---

# 🔵 5. How RedlineFeed supports these

## 🔹 Synthetic BBO

RedlineFeed can:

- Aggregate multiple exchange feeds
- Compute best bid/ask across them
- Publish a **consolidated feed**

👉 This is done **inside the platform**

---

## 🔹 Conflation

RedlineFeed can:

- Apply configurable time windows
- Reduce update frequency
- Deliver:
    - Full tick stream OR
    - Conflated stream

👉 Also done **inside the platform**

---

# 🎯 6. YOUR KEY QUESTION

## Are these coded by the client?

👉 **Answer: NO (mostly)**

---

## ✅ Correct understanding

> These are typically **built-in features of RedlineFeed**, configurable by the client—not something the client has to implement from scratch.

---

## 🔧 How it works in practice

Clients can:

- Configure:
    - “Give me synthetic BBO across these venues”
    - “Apply 50ms conflation”

But they **don’t write the core logic themselves**

---

## 💬 Interview-ready answer

> Synthetic BBO and conflation are typically supported as built-in features within RedlineFeed.
> 
> Synthetic BBO allows aggregation of best prices across multiple venues, while conflation reduces message rates by combining updates over a time window.
> 
> These are usually configurable by clients based on their needs, rather than being implemented directly in client applications.

---

# 🔥 7. When WOULD clients implement their own?

## They might:

- Further process data
- Build custom strategies

But:

- Core feed processing → Redline
- Trading logic → client

---

# 💥 8. SRE perspective (THIS is important)

These features affect:

## Synthetic BBO:

- More computation
- Aggregation logic

---

## Conflation:

- Lower throughput
- But potential latency trade-offs

---

## 💬 Strong SRE line

> I understand that these features impact both latency and throughput, so monitoring their behavior is important in production environments.

---

# 🧠 One-line memory

- Synthetic BBO = “best price across markets”
- Conflation = “fewer updates, less load”

---

# 🚀 If you want next level

I can:

- Give you **real interview follow-ups on this (they LOVE this topic)**
- Or simulate a **technical deep dive like Olieen might do**

Just say 👍