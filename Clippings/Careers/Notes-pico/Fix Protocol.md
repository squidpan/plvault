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

Explain FIX protocol and how it related to SRE role

This is a **very likely interview question**—and a chance to show you understand the **trading side + SRE side**.

---

# 🧠 1. What is FIX Protocol?

## ✅ Simple interview definition

> FIX (Financial Information eXchange) is a standardized messaging protocol used to send trading information such as orders, executions, and market data between financial systems.

---

# 🔗 2. What FIX is used for

FIX is used for **trading communication**, not raw market data feeds.

### Typical use cases:

- Sending orders to exchanges
- Receiving execution confirmations
- Order status updates

---

## 🧩 Example flow

Trading App → FIX → Broker / Exchange → Execution → FIX → Trading App

---

# 📩 3. Example FIX message (simplified)

35=D | Buy Order  
55=AAPL | Symbol  
54=1 | Buy  
38=100 | Quantity  
44=150.00 | Price

👉 This means:

> “Buy 100 shares of AAPL at $150”

---

# ⚙️ 4. Key FIX concepts

---

## 🔵 A. Session-based protocol

- Uses persistent connection
- Has:
    - Logon
    - Heartbeats
    - Logout

---

## 🟡 B. Message types

- New Order (D)
- Execution Report (8)
- Cancel (F)

---

## 🔴 C. Sequence numbers (VERY IMPORTANT)

- Every message has a sequence number
- Used to detect:
    - Missing messages
    - Out-of-order messages

---

# 🔥 5. How FIX relates to Pico

From your materials:

- Pico has:
    - Order Execution Gateway
    - FIX support  
        

---

👉 Meaning:

> Clients use FIX to send orders through Pico infrastructure to exchanges

---

# 🎯 6. How FIX relates to YOUR SRE role

This is the most important part.

---

## 🔧 As an SRE, you support:

### 1. FIX connectivity

Check:

- Is session up?
- Is connection stable?

---

## 🔧 2. Message flow

Check:

- Are orders being sent?
- Are execution reports coming back?

---

## 🔧 3. Sequence gaps

👉 Similar to market data gaps:

- Missing messages
- Requires resend

---

## 🔧 4. Latency

- Time from:
    - Order sent → execution received

---

## 🔧 5. Troubleshooting

---

# 🧠 7. Example SRE troubleshooting scenario

## ❓ “Client says orders are not going through”

---

## 💬 Your answer:

> I would first check whether the FIX session is established and stable. Then I would verify message flow, ensuring that orders are being sent and acknowledgments are being received.
> 
> I would also check for sequence gaps or resend requests, which could indicate missing messages.
> 
> Finally, I would analyze logs and correlate with network and system metrics to determine whether the issue is at the application, network, or exchange level.

---

# 🔥 8. Key connection (VERY IMPORTANT)

## Market Data vs FIX

|Function|System|
|---|---|
|Market data|InRush / Redline|
|Order execution|FIX|

---

👉 Say this:

> Market data drives decisions, and FIX is used to execute those decisions.

🔥 That’s a **perfect connection**

---

# 💬 9. Interview-ready answer

> FIX protocol is a standardized messaging protocol used for electronic trading, primarily for sending orders and receiving execution information.
> 
> It operates as a session-based protocol with sequence numbers to ensure message integrity and supports various message types such as new orders and execution reports.
> 
> From an SRE perspective, supporting FIX involves ensuring session stability, monitoring message flow, handling sequence gaps, and troubleshooting connectivity or latency issues that could impact order execution.

---

# 💥 10. Strong closing line

> Reliable FIX connectivity is critical because any disruption can directly impact trade execution and client outcomes.

---

# 🧠 One-line memory

> FIX = “protocol for sending orders”

---

# 🚀 Final prep

If you can explain:

- FIX basics
- Session + sequence numbers
- How to troubleshoot

👉 You’re **well above average**

---

If you want:

- A **final 5-minute drill before your interview**
- Or quick recap of everything

Just say:  
👉 “final drill”