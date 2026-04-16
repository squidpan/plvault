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
Explain with examples what order books (level 1/2/3)

Great—this is a **core concept for Pico**, and if you explain it clearly with examples, you’ll sound very strong.

---

# 🧠 What is an Order Book?

## ✅ Simple definition

> An order book is a real-time list of buy and sell orders for a financial instrument, organized by price.

---

## 📊 Structure

BUY (Bids)        SELL (Asks)  
Price   Size      Price   Size  
99.99   200       100.01  150  
99.98   300       100.02  400

- **Bids** = buyers (what people are willing to pay)
- **Asks** = sellers (what people want to sell for)

---

# 🔍 Levels of Order Book Data

---

# 🟢 Level 1 (Top of Book)

## ✅ What it shows

> Only the **best bid and best ask**

---

## Example:

Best Bid:  99.99 (200 shares)  
Best Ask: 100.01 (150 shares)

👉 This is what most basic systems use

---

## 💡 Key idea:

- Very lightweight
- Minimal data
- Fast

---

## 💬 Interview line

> Level 1 provides the top of book, showing the best bid and ask prices.

---

# 🟡 Level 2 (Depth of Book)

## ✅ What it shows

> Multiple price levels on both sides

---

## Example:

BUY (Bids)        SELL (Asks)  
99.99   200       100.01  150  
99.98   300       100.02  400  
99.97   500       100.03  600

---

## 💡 Key idea:

- Shows **market depth**
- More data → more insight

---

## 💬 Interview line

> Level 2 provides multiple levels of bids and asks, giving visibility into market depth.

---

# 🔴 Level 3 (Full Order Book)

## ✅ What it shows

> Individual orders (not just aggregated levels)

---

## Example:

Price 99.99:  
  Order1: 100 shares  
  Order2: 100 shares  
  
Price 100.01:  
  Order3: 50 shares  
  Order4: 100 shares

---

## 💡 Key idea:

- Full detail of every order
- Includes:
    - Order IDs
    - Individual participants

---

## 💬 Interview line

> Level 3 provides full order-level detail, including individual orders rather than aggregated price levels.

---

# ⚖️ Quick Comparison

|Level|What you see|Detail|Use case|
|---|---|---|---|
|Level 1|Best bid/ask|Low|Basic trading|
|Level 2|Multiple levels|Medium|Most trading systems|
|Level 3|Individual orders|High|HFT / advanced systems|

---

# 🔥 Why this matters for Pico

👉 Systems like:

- InRush Ticker Plant

👉 Must:

- Process **Level 2 / Level 3 data**
- Build order books in real time
- Handle massive message rates

---

# 💥 SRE perspective

Higher levels = more data:

- Level 1 → low load
- Level 2 → medium
- Level 3 → 🔥 extremely high throughput

👉 This affects:

- CPU usage
- Network load
- Latency

---

# 🎯 Interview-ready answer (clean version)

> An order book is a real-time list of buy and sell orders organized by price.
> 
> Level 1 shows the best bid and ask, Level 2 shows multiple price levels providing market depth, and Level 3 shows individual orders with full detail.
> 
> Systems like InRush process Level 2 and Level 3 data to build order books in real time, which requires handling very high message rates and low latency.

---

# 🧠 One-line memory trick

> L1 = top  
> L2 = depth  
> L3 = full detail

---

# 🚀 If you want next level

I can:

- Show you **how order books are built from raw packets (very useful for Pico)**
- Or give you **tricky follow-up questions they may ask**

Just say 👍