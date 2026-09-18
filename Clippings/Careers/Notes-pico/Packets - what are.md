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
what are packets

Great—this is a **fundamental concept**, and explaining it clearly (without overcomplicating) will make you sound **solid and confident**.

---

# 🧠 What are packets?

## ✅ Simple definition (use this in interview)

> A packet is a small unit of data that is sent over a network from one system to another.

---

# 📦 Think of it like this (easy analogy)

👉 Sending data over a network is like mailing a book:

- The book = full data
- Each page = a **packet**
- The network = postal system

Instead of sending one huge block, data is:  
👉 **broken into smaller packets**  
👉 sent individually  
👉 reassembled at the destination

---

# 🔍 What’s inside a packet?

Each packet contains:

### 1. **Payload**

- The actual data (e.g., part of a price tick)

### 2. **Header**

- Source IP address
- Destination IP address
- Protocol (TCP/UDP)
- Sequence info

---

# ⚡ Why packets exist

Networks use packets because:

- Easier to route efficiently
- More reliable (for TCP)
- Allows parallel transmission
- Reduces congestion impact

---

# 🌐 Packets in YOUR context (very important)

In your FRBNY experience:

👉 Market data (price ticks) was transmitted as:

- **streams of packets over the network**

---

# 🔥 Why packets matter for Pico / SRE

## 💥 Key idea:

> Market data systems depend on packets arriving correctly and quickly.

---

## 🚨 If packets are lost:

- Missing price updates
- Incomplete order book
- Trading decisions become inaccurate

---

# 🔗 Packets + UDP (important connection)

👉 Most market data uses **UDP**

- Fast
- Low overhead
- BUT:  
    ❌ No guarantee packets arrive

👉 That’s why:

- NIC stats matter
- Packet loss matters

---

# 💬 Interview-ready answer

> Packets are small units of data transmitted over a network.
> 
> In distributed systems, data is broken into packets, sent across the network, and then reassembled at the destination.
> 
> In real-time market data systems, price updates are transmitted as packets, so ensuring that packets are delivered quickly and without loss is critical for maintaining accurate data.

---

# 🔥 Strong follow-up (if you want to impress)

> In low-latency systems, even small packet delays or losses can impact downstream processing and lead to inconsistencies in the data.

---

# 🧠 One-line memory trick

> Packets = “small pieces of data moving across the network”

---

# 🚀 If you want next level understanding

I can:

- Explain **how packets flow from exchange → feed handler (InRush)**
- Or show **how packet loss creates order book gaps (very useful for interview)**

Just say 👍