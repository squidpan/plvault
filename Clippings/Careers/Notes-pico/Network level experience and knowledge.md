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



## Layer 2 Concepts - MAC address, tables, and switches

```[!Question-1]

Identify and explain Layer 2 concepts by accurately describing the purpose of MAC addresses. MAC tables, and how switches use them to forward Ethernet frames.
```
MAC addresses are unique hardware identifiers used to identify devices (NIC) on a local area network, and switches use them in their MAC tables to forward Ethernet frames to the correct port.

Practice describing the switch process in order: 
- learn the source MAC and incoming port
- look up the destination MAC in the MAC table
- forward out the matching port if found, 
- or flood unknown destinations out all other ports if not found.

## BUM traffic behavior

- Broadaast
- Unicast
- Multicast

When and how type occurs on an Ethernet network:

Review the three BUM categories separately: 
- broadcast goes to all devices in the broadcast domain
- unknown unicast is sent when the destination MAC is not in the switch table
- multicast is sent to a specific subscribed group of devices.


## ARP request/response map IP to MAC on a LAN


## OSI model

Review the common mappings: 
- switches and MAC addresses belong to Layer 2
- IP addresses belong to Layer 3, TCP ports belong to Layer 4
- Ethernet frames are Layer 2 data units.

## Network devices: hubs, bridges, switch - collision domains and broadcast domains

Study how each device behaves: 
- hubs repeat signals to all ports
- bridges segment collision domains
- switches learn MAC addresses to forward frames efficiently while still keeping one broadcast domain unless VLANs are used.


## Routing Behavior


How do routers break up Layer 2 broadcast domains and prevent Ehternet broadcasts from crossing network segments.

When asked about routers and broadcasts, say that routers connect different networks, stop Layer 2 broadcasts from crossing subnets, and keep broadcast traffic contained within each segment.

## Default gateway logic: how computer sends traffic to a router when dest. IP is on diff subnet

When the destination is outside your subnet, explain that your computer sends the packet to its configured default gateway, usually a router, which then forwards it onward.
## Network commands
I start by identifying the network interface using `ip link`, then check for packet drops using `ip -s link` or `ethtool -S`. I verify connectivity with `ping` and `traceroute`, and confirm multicast subscription using `netstat -g`. If needed, I use `tcpdump` to validate packet flow and determine whether the issue is at the network or application layer.

---
| Category                  | Command                        | What It Does                        | What You Look For            | When You Use It                 |
| ------------------------- | ------------------------------ | ----------------------------------- | ---------------------------- | ------------------------------- |
| **Interfaces**            | `ip link show`                 | Lists all network interfaces (NICs) | Interface names (eth0, ens3) | First step—identify NIC         |
|                           | `ls /sys/class/net`            | Simple list of NICs                 | Interface names              | Quick lookup                    |
|                           | `ifconfig -a`                  | Legacy interface info               | IP + status                  | Older systems                   |
|                           |                                |                                     |                              |                                 |
| **Basic NIC Stats**       | `ip -s link`                   | Shows RX/TX stats per interface     | `dropped`, `errors`          | Check packet loss quickly       |
|                           |                                |                                     |                              |                                 |
| **Detailed NIC Stats**    | `ethtool -S eth0`              | Deep NIC/driver stats               | `rx_dropped`, `rx_errors`    | Diagnose packet loss at NIC     |
|                           |                                |                                     |                              |                                 |
| **Connectivity**          | `ping <host>`                  | Tests reachability + latency        | packet loss, RTT             | Quick connectivity check        |
|                           | `traceroute <host>`            | Shows network path (hops)           | delays between hops          | Find where latency occurs       |
|                           | `mtr <host>`                   | Real-time ping + traceroute         | packet loss + latency trends | Better version of traceroute    |
|                           |                                |                                     |                              |                                 |
| **Interface Stats**       | `netstat -i`                   | Interface-level statistics          | drops/errors per interface   | Quick network health check      |
|                           |                                |                                     |                              |                                 |
| **Sockets / Connections** | `ss -i`                        | Shows active connections + stats    | connection issues            | Debug connectivity              |
|                           | `ss -ulpn`                     | Shows UDP listeners                 | ports/services               | Verify multicast/listeners      |
|                           |                                |                                     |                              |                                 |
| **Multicast**             | `netstat -g`                   | Shows multicast group membership    | joined groups                | Verify feed subscription        |
|                           |                                |                                     |                              |                                 |
| **Packet Capture**        | `tcpdump -i eth0`              | Live packet capture                 | packet flow                  | Check if data is arriving       |
|                           | `tcpdump -i eth0 -w file.pcap` | Capture to file                     | full packet data             | Deep debugging / replay         |
|                           | `tcpdump -r file.pcap`         | Read captured packets               | sequence / flow              | Analyze past traffic            |
|                           |                                |                                     |                              |                                 |
| **Interrupts (NIC/CPU)**  | `cat /proc/interrupts`         | Shows IRQ distribution across CPUs  | imbalance                    | Diagnose CPU/network contention |
|                           |                                |                                     |                              |                                 |
| **System View (related)** | `top`                          | CPU/memory usage                    | high CPU/system load         | Check system bottlenecks        |
|                           | `vmstat 1`                     | System performance stats            | CPU wait, memory pressure    | Deeper system analysis          |

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