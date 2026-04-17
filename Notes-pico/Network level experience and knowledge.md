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
# Background

They will ask me about network level experience and knowledge to see if I can handle network related troubleshooting as an SRE when connecting to quantitative trading platforms and clients. help me out here.

---

# Need to know

Networking (VERY critical)

- TCP vs UDP (most feeds are UDP multicast)    
- Multicast basics
- Packet loss debugging (`netstat`, `ethtool`)
- Latency vs throughput tradeoffs
---


Perfect—this is one of the **most important parts of your interview**. Pico SREs are expected to think at the **network + packet + application** level.

I’ll give you:

- What they expect
- What YOU should say
- Real troubleshooting answers

---

# 🧠 1. What Pico means by “network knowledge”

From their materials, you are dealing with:

- **Multicast market data feeds**
- **Ultra-low latency networks (PicoNet)**
- **Packet-level visibility (Corvil)**
- **Colocation environments**  
    

---

## 🎯 Key expectation

> Can you troubleshoot issues between exchange → network → client?

---

# 🔗 2. The network path you must understand

Exchange → Multicast Feed → Network (PicoNet) → NIC → InRush → App

👉 Problems can occur at ANY layer

---

# 🔥 3. Core networking concepts YOU MUST speak to

---

## 🌐 A. Packets

> Small units of data sent over the network

---

## 📡 B. Multicast (VERY IMPORTANT)

> One-to-many data distribution used for market data feeds

---

## 🔥 Why it matters:

- Efficient delivery
- But:
    - No guarantee of delivery
    - Packet loss possible

---

## 🌐 C. Latency

> Time for data to travel from exchange to client

---

## 📉 D. Packet Loss

> Missing packets → missing ticks → broken order book

---

## 🧠 E. NIC (Network Interface Card)

- Where packets enter the server
- Check stats for:
    - drops
    - errors

---

# 🔧 4. Commands you should reference

## 🧩 Network checks

```
ping <host>  
netstat -i  
ethtool -S eth0

```
---

## 🧩 Packet capture

```
tcpdump -i eth0
```

---

## 🧩 Connectivity

```
traceroute <host>
```

---

# 🎯 5. How to answer: “Tell me your network experience”

## 💬 Use THIS:

> I have experience supporting real-time market data systems where data flows from on-prem systems through network infrastructure into cloud environments.
> 
> I understand key networking concepts such as packet flow, multicast delivery, latency, and packet loss, and how they impact real-time data systems.
> 
> In troubleshooting, I typically isolate issues by checking network connectivity, NIC statistics, and packet flow using tools like netstat, ethtool, and tcpdump, and then correlate that with application behavior to determine where the issue originates.

---

# 🔥 6. REAL troubleshooting scenario (YOU WILL GET THIS)

## ❓ “Client reports delayed market data”

---

## 💬 Your answer:

> I would first determine whether the issue is isolated or widespread.
> 
> Then I would check network latency and connectivity using ping or traceroute, and inspect NIC statistics for packet drops using netstat or ethtool.
> 
> Since market data uses multicast, I would verify that packets are being received correctly and check for packet loss, as missing packets can cause delays or inconsistencies.
> 
> I would also correlate this with monitoring tools to determine if the issue is at the network layer or within the application.

---

# 💥 7. Advanced answer (this will impress them)

> In multicast environments, packet loss is particularly important because there’s no retransmission, so I would check whether gap recovery mechanisms are triggered at the application level.

🔥 This is **EXACTLY Pico-level thinking**

---

# 🧠 8. Tie to Pico (VERY IMPORTANT)

Say this:

> I understand that in Pico’s environment, network performance directly impacts market data quality and trading decisions, so troubleshooting requires visibility at both the packet and application level.

---

# 🔥 9. What NOT to do

Don’t:

- Go too deep into theory
- Say “I don’t know networking”

---

Instead:

> Show structured thinking + awareness

---

# 🎯 10. One-line memory

> Network issues = latency, packet loss, or connectivity problems

---

# 🚀 FINAL BOOST (read this before interview)

If you say:

> “I check packet flow, NIC stats, and multicast behavior, then correlate with application performance”

🔥 You will sound like a **real SRE**

---


---

# 🧠 1. Examples of gap recovery mechanisms: What is a “gap”:

Examples of gap recovery mechanisms

## ✅ Simple definition

> A gap occurs when one or more market data messages (packets) are missing, usually detected via sequence numbers.

---

## Example:

1001, 1002, 1003, 1007

👉 Missing:

- 1004, 1005, 1006  
    👉 That’s a **gap**

---

# 🔥 2. Why gaps matter

> Order books must be built from a complete, ordered stream of updates.

👉 Missing messages =  
❌ Incorrect order book  
❌ Wrong trading decisions

---

# 🛠️ 3. Gap recovery mechanisms (THIS is the core)

---

# 🔵 1. Retransmission (Request missing packets)

## ✅ How it works

- System detects missing sequence
- Sends request to exchange or feed handler
- Receives missing packets

---

## Example:

Detected gap: 1004–1006    
→ Request retransmission    
→ Receive missing packets    
→ Apply updates

---

## 💬 Interview line

> One common mechanism is retransmission, where missing packets are requested and replayed to restore the correct sequence.

---

# 🟡 2. Snapshot + Replay (VERY IMPORTANT)

## ✅ How it works

- Instead of recovering each packet:
    - Get a **snapshot of full order book**
    - Apply updates from latest sequence onward

---

## Example:

Gap detected → Request snapshot    
→ Rebuild order book    
→ Resume live feed

---

## 💬 Interview line

> Another approach is snapshot recovery, where the system rebuilds the order book from a known good state and resumes processing from the latest sequence.

---

---

# 🔴 3. Primary / Secondary Feed Failover

## ✅ How it works

- Two feeds:
    - Primary
    - Secondary

If gap in primary:  
👉 Switch to secondary

---

## 💬 Interview line

> Systems often use redundant feeds, and if a gap is detected in the primary feed, the system can switch to the secondary feed to maintain continuity.

---

---

# 🟣 4. Gap Detection + Auto Resync

## ✅ How it works

- System continuously monitors sequence numbers
- Automatically:
    - pauses processing
    - resyncs feed

---

## 💬 Interview line

> Feed handlers like InRush include gap detection logic that can automatically trigger recovery or resynchronization.

---

---

# ⚫ 5. PCAP Replay (VERY ADVANCED)

From Pico docs:

- Raw data stored as PCAP
- Replay exact packet sequence  
    

---

## ✅ How it’s used

- Debugging
- Reproducing issue
- Not real-time recovery

---

## 💬 Interview line

> PCAP replay can be used offline to reproduce gaps and analyze their impact for debugging and testing purposes.

---

---

# 🎯 4. What Pico specifically does (IMPORTANT)

From your docs:

- Gap detection on multicast feeds
- Compare primary vs secondary
- Book snapshot recovery  
    

---

👉 This means:

> Pico uses **multiple recovery strategies together**

---

# 💥 5. Interview-ready answer (BEST VERSION)

> Gap recovery mechanisms are used to handle missing market data messages detected through sequence numbers.
> 
> Common approaches include retransmission requests to recover missing packets, snapshot-based recovery where the order book is rebuilt from a known state, and failover to a secondary feed if the primary feed experiences packet loss.
> 
> Systems like InRush also include built-in gap detection and recovery logic, and in some cases, PCAP replay can be used for post-incident analysis.
> 
> These mechanisms are critical to ensure order book consistency in real-time trading systems.

---

# 🔥 6. Strong follow-up (VERY impressive)

> In multicast environments, gap recovery is especially important because packets are not retransmitted automatically, so the application layer must handle recovery.

---

# 🧠 One-line memory

> Gap recovery = “detect missing data → restore correct sequence”

---

# 🚀 If you want final prep

I can:

- Give you **top 5 hardest Pico technical questions**
- Or do a **live mock interview before you go to sleep**

Just say:  
👉 “mock interview”