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
need in depth information on Pico's Redline Feed and Historical Data Stored in the Cloud since I will be supporting it as SRE.

Here’s a **deep, SRE-focused breakdown** of Pico’s Redline ecosystem—specifically:

- **RedlineFeed (real-time feed you’ll support)**
- **InRush (core engine underneath)**
- **Historical Market Data (cloud + replay)**

I’ll explain it in a way you can **speak confidently in interviews AND understand how to support it in production**.

---

# 🧠 1. Big Picture Architecture (CRITICAL)

This is the **mental model you need**:

Exchange → InRush (feed handler) → RedlineFeed (normalized distribution)  
        → Client apps (trading / analytics)  
        → Historical storage (cloud / PCAP replay)

---

# 🔵 2. InRush Ticker Plant (CORE ENGINE)

## 🔹 What it does

- Connects directly to **exchanges (180+ venues)**
- Ingests raw market data (UDP multicast packets)
- Builds:
    - Order books (Level 1/2/3)
- Delivers **ultra-low latency data (microseconds)**

---

## 🔹 Key features (important for SRE)

- Maintains **full-depth order books**
- Handles:
    - Gap detection
    - Packet retransmission
    - Failover
- Supports:
    - Filtering (only send needed symbols)
    - Replay mode (historical injection)

👉 This is where:

- Packet loss
- CPU issues
- NIC issues  
    → directly impact performance

---

## 🔧 SRE responsibilities here

You’ll troubleshoot:

- Feed gaps
- Multicast issues
- CPU saturation
- Order book inconsistencies

---

# 🟢 3. RedlineFeed (WHAT YOU’LL SUPPORT MOST)

## 🔹 What it is

> A **managed, normalized, distributed market data feed service**

---

## 🔹 What it does

- Aggregates **multiple exchange feeds**
- Normalizes data into **one consistent format**
- Distributes to clients via:
    - Local InRush instances
    - APIs

👉 Think:

> “Market data as a service”

---

## 🔹 Architecture (VERY IMPORTANT)

- Central **publishing hub (hosted by Pico)**
- Data is sent to:
    - Client servers
    - Each running **embedded InRush**

👉 This means:

- Distributed system
- Multiple hops
- Many failure points

---

## 🔹 Key capabilities

### ✅ Normalization

- Converts multiple feed formats → one format

### ✅ Consolidation

- Combines:
    - Multiple venues
    - Multi-asset data

### ✅ Customization

- Synthetic BBO (best bid/offer)
- Depth control
- Conflation (reduce message rate)

### ✅ High availability

- Dual multicast feeds (primary + backup)
- Snapshot recovery for gaps

---

## 🔹 Performance

- Near direct feed latency (microseconds)
- Co-located with exchanges

---

## 🔧 SRE responsibilities (THIS IS YOUR ROLE)

You will support:

### 1. **Latency monitoring**

- Tick arrival → client delivery

### 2. **Feed health**

- Are multicast feeds stable?
- Are there gaps?

### 3. **Client issues**

- “We are missing data”
- “Latency spike”

### 4. **System reliability**

- Failover working?
- Snapshot recovery working?

---

# ☁️ 4. Redline Historical Market Data (CLOUD + REPLAY)

## 🔹 What it is

> Raw market data stored as **packets (PCAP files)**

---

## 🔹 Key concept (VERY IMPORTANT)

👉 This is NOT just “price history”

It is:

> **Exact raw packets as received from exchanges**

---

## 🔹 Why this matters

- Nanosecond timestamp accuracy
- Exact replay of trading day
- Used for:
    - Backtesting
    - Compliance
    - Debugging

---

## 🔹 How it works

### 1. RECORDING

- InRush captures packets
- Stored as `.pcap` files

---

### 2. ARCHIVING (CLOUD)

- Data sent to **Pico cloud storage**
- Available:
    - Download
    - Cloud access
    - Bulk transfer

---

### 3. REPLAY

- Inject data back into system
- Simulates real trading conditions

---

## 🔹 Key SRE insight

> Historical data = debugging tool

---

## 🔧 SRE responsibilities

You may:

- Help clients replay data to reproduce issues
- Validate:
    - Data integrity
    - Timing accuracy
- Troubleshoot:
    - Missing ticks
    - Sequence issues

---

# 🔥 5. REAL-TIME vs HISTORICAL (CRITICAL FOR INTERVIEW)

|Feature|RedlineFeed|Historical Data|
|---|---|---|
|Purpose|Live trading|Analysis / replay|
|Data type|Normalized|Raw packets|
|Latency|Microseconds|Not real-time|
|Format|Structured feed|PCAP files|
|Use case|Trading|Debugging / backtesting|

---

# 💥 6. WHAT YOU SHOULD SAY IN INTERVIEW

## 💬 Perfect answer

> RedlineFeed provides normalized, low-latency market data aggregated from multiple exchanges and distributed to client systems, typically using embedded InRush instances for local processing.
> 
> InRush acts as the core feed handler, building order books and handling low-level feed processing such as gap detection and recovery.
> 
> Historical market data complements this by storing raw packet-level data in the cloud, which can be replayed for analysis, testing, or debugging.
> 
> From an SRE perspective, supporting this system involves monitoring latency, ensuring data integrity, troubleshooting packet loss or feed gaps, and helping clients diagnose issues using both real-time and historical data.

---

# 🚀 7. KEY INTERVIEW INSIGHT (THIS IS GOLD)

Say this if you can:

> “The combination of real-time feeds and historical replay allows you to move seamlessly between production issues and root cause analysis.”

🔥 That shows **deep system understanding**

---

# 🎯 Final takeaway

You are supporting:

### 🔹 Real-time system

- RedlineFeed → normalized, distributed market data

### 🔹 Core engine

- InRush → ultra-low latency feed handler

### 🔹 Debugging layer

- Historical data → packet-level replay