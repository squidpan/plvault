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
Give me a example of troubleshooting order book inconsistencies in inrush ticker plant

Perfect—this is a **very realistic Pico SRE scenario**, and if you walk through it clearly, you’ll sound like someone who can actually do the job.

---

# 🧠 SCENARIO: Order Book Inconsistency in InRush Ticker Plant

## 🚨 Problem

Client reports:

> “Our order book doesn’t match the exchange / another feed”

### Example:

- Expected:
    - Best bid: 100.00
- Client sees:
    - Best bid: 99.90

👉 That’s a **data inconsistency**

---

# 🎯 1. How to think (THIS is key)

Order book inconsistencies usually come from:

1. **Missing data (packet loss)**
2. **Out-of-order messages**
3. **Gap not recovered properly**
4. **Application processing issue**
5. **Feed configuration issue**

---

# 🔍 2. Step-by-step troubleshooting (interview gold)

---

## 🧩 Step 1 — Scope the issue

Ask:

- Is it:
    - One symbol or many?
    - One client or multiple clients?
    - One feed or both primary/backup?

👉 This tells you:

- Local vs systemic issue

---

## 🧩 Step 2 — Check for packet loss (MOST COMMON CAUSE)

netstat -i  
ethtool -S eth0

Look for:

- `RX-DRP` (dropped packets)
- NIC errors

---

### 💬 Say:

> Packet loss is a common cause of order book inconsistencies because missing updates can break the book state.

---

## 🧩 Step 3 — Check gap detection / recovery

In InRush logs:

tail -f inrush.log

Look for:

- Sequence gaps
- Retransmission requests
- Recovery failures

---

### 💬 Say:

> I would verify whether gap detection is triggered and whether the system successfully recovered missing messages.

---

## 🧩 Step 4 — Compare primary vs backup feed

👉 InRush usually has:

- Primary feed
- Secondary (backup) feed

Check:

- Are both consistent?

---

### 💬 Say:

> I would compare primary and backup feeds to see if one is experiencing issues.

---

## 🧩 Step 5 — Check system performance

top

Look for:

- High CPU
- Processing delays

---

### 💬 Say:

> If the system is overloaded, it may not process messages fast enough, leading to inconsistencies.

---

## 🧩 Step 6 — Validate order book rebuild

👉 Sometimes:

- Book needs to be rebuilt from snapshot

Check:

- Snapshot recovery working?

---

### 💬 Say:

> I would verify that the order book is correctly rebuilt after any detected gaps.

---

## 🧩 Step 7 — Compare against external reference

- Exchange feed
- Another vendor (e.g., Bloomberg)

---

### 💬 Say:

> I would compare against a trusted external source to confirm whether the issue is internal or upstream.

---

# 🔧 3. Root cause examples

## 🔥 Most common:

### 1. Packet loss

- Missing updates
- Broken book

---

### 2. Gap recovery failure

- System didn’t resync

---

### 3. Feed latency or delay

- Stale book

---

### 4. Misconfiguration

- Wrong symbols
- Incorrect filters

---

# 🛠️ 4. Resolution actions

Depending on cause:

### Packet loss:

- Switch to backup feed
- Fix NIC / network

---

### Gap issue:

- Trigger resync
- Restart feed handler

---

### CPU issue:

- Rebalance load
- Optimize system

---

# ✅ 5. Validation

Confirm:

- Book matches reference
- No packet drops
- No gap alerts

---

# 💬 FULL interview answer (use this)

> If there is an order book inconsistency, I would first scope the issue to determine whether it’s isolated or system-wide.
> 
> Then I would check for packet loss at the NIC level using tools like netstat or ethtool, since missing packets are a common cause of inconsistencies.
> 
> I would also review logs to see if there are sequence gaps and whether gap recovery mechanisms are functioning correctly.
> 
> Next, I would compare primary and backup feeds and validate system performance to ensure there are no processing delays.
> 
> Finally, I would compare the data against an external reference to confirm the issue and take corrective actions such as resynchronizing the feed or switching to a backup source.

---

# 💥 Key insight (THIS impresses them)

> Order book consistency depends on receiving every message in the correct order—any packet loss or gap can break the entire state.

---

# 🧠 One-line memory

> “Missing or out-of-order data = broken order book”

---

# 🚀 If you want next level

I can:

- Give you **a second scenario (multicast failure or latency spike)**
- Or run a **mock where you answer and I critique like an interviewer**

Just say 👍