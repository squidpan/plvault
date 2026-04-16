---
categories:
  - "[[Clippings]]"
  - "[[Jobs]]"
title: Pico.net SRE Interview Prep
source: https://chatgpt.com/c/69d911de-aa54-832b-8ec7-39dfbe3ca7b8
author:
published:
created: 2026-04-10
description: Site Reliability Engineer (SRE) interview prep
tags:
  - chatgpt/conversation
---
# Summary

Interview preparation for the role of Site Reliability Engineer (SRE) at [[Pico]] SRE tier 2/3 support to clients using Pico's Redline trading application products, Inrush Ticker Plant and Redline Feed.
  
---

![[Pico#About]]
---

![[Pico#Customers]]
![[Pico#Products]]

# Unix - critical topics

[[CPU pinning IRQ affinity Hugepages NUMA sysctl]]
[[Unix Linux]]
# Networking - critical topics

- TCP vs UDP (most feeds are UDP multicast)    
- Multicast basics
- Packet loss debugging (`netstat`, `ethtool`)
- Latency vs throughput tradeoffs

[[Intel based computer Architecture and IT systems Networking]]
[[Packets - what are]]
[[Multicast - what is]]
[[Network level experience and knowledge]]
# Low-latency systems

- Why microseconds matter
- Avoiding GC pauses, context switching
- Lock-free / high-performance systems (conceptual)

# Market data basics

- Order book (bid/ask)
- Trades vs quotes
- Level 1 vs Level 2 data

[[Market Data]]

---

# 5. How to sound strong in the interview

## 💬 Strong positioning statement

> “I understand Pico operates ultra-low latency trading infrastructure where reliability and microsecond performance are critical. As an SRE, my focus would be on **ensuring stable feed handling, minimizing latency, and quickly diagnosing issues across network, OS, and application layers.”**

---

## Market data delay issue — what do you check?**

**Q: Market data delay issue — what do you check?**

Answer structure:

1. Network: Packet drops, NIC stats
2. System: CPU usage, context switches
3. Application: Thread backlog, queue buildup
4. Feed: Exchange issues vs internal issue

---

## 💬 Example behavioral angle

> “I treat incidents as both a resolution task and a learning opportunity—documenting root cause and improving monitoring to prevent recurrence.”

---
[[End to end dataflow - pico]]

[[End to end dataflow and SRE troubleshooting spots - Exchanges to Trading apps via pico products]]

# AWS
[[AWS]]
[[SRE Pico Mock Interview 1]]

---

# Trading Systems and APIs
[[Trading Systems and Trading APIs]]
[[Trading firms]]

[[Quantitave Trading]]

[[Quantitative Trading group interview]]


# SFTP
[[Real SFTP usage step-by-step]]

# SRE Troubleshooting scenarios

[[Realistic SRE troubleshooting scenarios]]

# Monitoring tools
[[Prometheus and Graphan]]

# Order books

[[Bloomberg B-PIPE CBBT]]

[[Order Books]]
[[Order Execution]]
[[Equity Order Books - higher frequency]]

[[Trep and Inrush Ticker Plant]]


[[Pico Inrush and Redline feed vs Bloomberg raw market data feed]]


[[SRE Cheat Sheet to Memorize]]

[[Troubleshooting order book inconsistencies in inrush ticker plant]]

[[BBO (best bid offer) and conflation (reduce message rate) ]]

[[PCAP file]]

[[Fix Protocol]]

[[Position - what is]]




[[5 hardest Pico technical questions]]

# Others
[[Deal with Pressure]]

[[Thank you Skarlet]]

[[Pico Redline and Historical Data stored in Cloud]]

[[Runbooks]]

---

[[Colocation sites]]

---






---

If you want, I can also help you:

- Prepare for the **technical interview with Olieen (this is the real test)**
- Or simulate **what she will likely ask (very targeted)**



---

# 🚀 If you want next level

I can:

- Simulate **Olieen’s technical interview (very realistic)**
- Or give you **deep dive on order book construction + failure modes**


---

# 🚀 If you want next level

I can:

- Give you a **diagram you can explain verbally in interview (very powerful)**
- Or simulate a **deep technical grilling on this topic**

Just say 👍




---

