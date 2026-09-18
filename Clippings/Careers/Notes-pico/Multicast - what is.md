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
what is multicast

Excellent—**multicast is a must-know concept** for Pico and market data systems. If you explain this well, it signals you understand **how real-time feeds are actually delivered**.

---

# 🧠 What is multicast?

## ✅ Simple interview definition

> Multicast is a network communication method where one sender transmits data to multiple receivers at the same time efficiently.

---

# 📦 Easy analogy

👉 Think of multicast like a **live TV broadcast**:

- One broadcaster sends the signal
- Many viewers receive it simultaneously
- The broadcaster sends **only one stream**, not one per viewer

---

# 🔁 Compare with other methods (important)

## 🔹 Unicast (1 → 1)

- One sender → one receiver
- Example: downloading a file

## 🔹 Broadcast (1 → all)

- One sender → everyone on network
- Inefficient

## 🔹 Multicast (1 → many specific receivers) ✅

- One sender → multiple subscribed receivers
- Efficient and targeted

---

# 🌐 How multicast works (simple)

- Sender sends data to a **multicast group address** (e.g., `239.x.x.x`)
- Receivers “join” that group
- Network delivers packets only to those subscribers

---

# ⚡ Why multicast is used in market data

👉 This is the **most important part for Pico**

## 💥 Key reason:

> Efficiency + low latency

Instead of sending the same market data to each client individually:

❌ Unicast:

- 100 clients → 100 streams (slow, expensive)

✅ Multicast:

- 100 clients → 1 stream (fast, efficient)

---

# 📊 Real-world (your context)

In systems like:

- Refinitiv TREP
- InRush Ticker Plant

👉 Market data feeds are often distributed via multicast

---

# 🚨 Important downside (VERY important)

> Multicast usually uses UDP → no guaranteed delivery

So:

- Packets can be lost
- Systems must handle:
    - Gap detection
    - Retransmission
    - Redundant feeds

---

# 🔧 SRE perspective (this is what they want)

## 💬 Example answer

> Multicast is commonly used in market data systems to efficiently distribute real-time data to multiple consumers.
> 
> As an SRE, I’d be concerned with ensuring reliable delivery, monitoring for packet loss, and verifying that systems handle gaps or failover correctly.

---

# 🔥 Interview-ready answer (clean version)

> Multicast is a network communication method where a single sender transmits data to multiple receivers simultaneously using a multicast group.
> 
> It’s commonly used in market data systems because it allows efficient, low-latency distribution of data to many clients.
> 
> Since multicast typically uses UDP, it doesn’t guarantee delivery, so systems need mechanisms to handle packet loss and ensure data consistency.

---

# 💥 Bonus (impress them)

If you want to go one level deeper:

> “In market data systems, multicast is often combined with gap recovery or redundant feeds to maintain data integrity.”

🔥 That’s **exactly how systems like InRush work**

---

# 🧠 One-line memory trick

> Multicast = “one sender, many receivers, one stream”

---

# 🚀 If you want next level

I can:

- Show you **how multicast + UDP + packet loss affects order books (step-by-step)**
- Or give you **networking questions Pico loves to ask**

Just say 👍