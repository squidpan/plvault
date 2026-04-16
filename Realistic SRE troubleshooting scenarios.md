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
Give you real troubleshooting scenarios (like: feed delay, packet loss, CPU spike)


Perfect—this is exactly what Pico will test. These scenarios are **very close to what you’ll actually do on the job**.

I’ll give you **realistic SRE troubleshooting scenarios**, and for each:

- What’s happening
    
- How to think
    
- Commands to use
    
- A **strong interview-style answer**
    

---

# 🔥 SCENARIO 1 — Market Data Feed Delay

## 🧠 Situation

Client says:

> “We are receiving delayed market data.”

---

## 🎯 How to think (structured approach)

Break it into layers:

1. **Upstream (exchange/feed)**
    
2. **Network**
    
3. **Server (CPU/memory)**
    
4. **Application (queue/backlog)**
    

---

## 🔧 Commands to use

top

👉 Check CPU usage

free -h

👉 Memory pressure

ping <feed_source>

👉 Network latency

netstat -i

👉 Packet drops

tail -f app.log

👉 Processing delays / errors

---

## 💬 Interview answer

> I would start by identifying where the delay is introduced in the pipeline.
> 
> First, I’d check system resources using tools like top and free to ensure the server isn’t CPU or memory constrained.
> 
> Then I’d verify network health using ping or netstat to check for latency or packet loss.
> 
> I’d also review application logs using tail to see if there are processing delays or queue backlogs.
> 
> The goal is to isolate whether the delay is upstream, network-related, or within the application itself.

---

# 🔥 SCENARIO 2 — Packet Loss in Market Data

## 🧠 Situation

Client reports:

> “We are missing ticks / data gaps.”

---

## 🎯 Key concept

👉 Market data often uses **UDP**  
👉 Packet loss = missing data = broken order book

---

## 🔧 Commands

netstat -i

ethtool -S eth0

👉 Look for:

- RX dropped packets
    
- Errors
    

---

## 💬 Interview answer

> Packet loss is critical in market data systems because it can lead to gaps in the order book.
> 
> I’d start by checking NIC statistics using tools like netstat or ethtool to identify dropped packets or errors.
> 
> Then I’d investigate network congestion or hardware issues.
> 
> I’d also verify whether the application is handling gap detection and recovery properly, such as requesting retransmission or failing over to a redundant feed.

---





# 🔥 SCENARIO 3 — High CPU Usage (Latency Spike)

## 🧠 Situation

System latency increases suddenly.

---

## 🔧 Commands

```code
top or htop
```
Identify:

- Which process is consuming CPU

```code
ps -ef | grep <process>
```



## 💬 Interview answer

> I’d use top or htop to identify processes consuming high CPU.
> 
> If a specific process is causing the issue, I’d investigate whether it’s due to increased load, inefficient processing, or a potential bug.
> 
> High CPU usage can directly impact latency in real-time systems, so isolating and resolving the root cause quickly is critical.



# 🔥 SCENARIO 4 — Application Not Running

## 🧠 Situation

Client:

> “We are not receiving any data.”

---

## 🔧 Commands

ps -ef | grep app_name

👉 Check if process is running

netstat -tulnp

👉 Check if port is listening

tail -f app.log

---

## 💬 Interview answer

> I’d first verify whether the application is running using ps.
> 
> If it’s not running, I’d check logs to understand why it stopped.
> 
> If it is running, I’d verify that it’s listening on the correct ports and accepting connections using netstat.
> 
> Then I’d continue troubleshooting downstream or upstream dependencies.

---
# 🔥 SCENARIO 5 — Disk Full (Silent Failure)

## 🧠 Situation

System behaves strangely, logs stop updating.

---

## 🔧 Commands

df -h

df -i

---

## 💬 Interview answer

> I’d check disk usage using df -h to ensure the system isn’t out of space.
> 
> If the disk is full, logs may stop writing and applications may fail silently.
> 
> I’d also check inode usage with df -i, since running out of inodes can cause similar issues.


# 🔥 SCENARIO 6 — Memory Pressure / Swapping

## 🧠 Situation

System is slow, inconsistent latency.

---

## 🔧 Commands

free -h

top

👉 Look for:

- High memory usage
- Swap usage

---

## 💬 Interview answer

> I’d check memory usage using free and top.
> 
> If the system is swapping, it can significantly impact performance and latency.
> 
> In a real-time system, avoiding swapping is critical, so I’d investigate memory leaks or high memory usage processes.

---

# 🔥 SCENARIO 7 — Network Connectivity Issue

## 🧠 Situation

Client cannot connect to service.

---

## 🔧 Commands

ping server

traceroute server

netstat -tulnp

---

## 💬 Interview answer

> I’d first verify basic connectivity using ping.
> 
> If that fails, I’d use traceroute to identify where the connection is breaking.
> 
> I’d also confirm that the service is running and listening on the expected port using netstat.

---

> .

---

# 💥 MASTER ANSWER STRATEGY (THIS IS HUGE)

No matter the question, follow this structure:

### 🧠 1. Identify scope

> “I’d determine where in the pipeline the issue occurs…”

### 🔍 2. Check layers

- System (CPU, memory, disk)
- Network
- Application

### 🔧 3. Use tools

Mention commands naturally

### 🎯 4. Isolate root cause

---

# 🚀 If you want FINAL LEVEL prep

I can:

- Run a **live mock where I act like interviewer and you answer**
- Or give you a **“cheat sheet” you can memorize before interview (1 page, high impact)**

Just tell me 👍