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

give you a “cheat sheet” you can memorize before interview (1 page, high impact) for the 10 troubleshooting scenarios

Here’s your **1-page, high-impact SRE troubleshooting cheat sheet**—designed so you can **memorize and recall under pressure** in the interview.

---

# ⚡ 🧠 PICO SRE TROUBLESHOOTING CHEAT SHEET

## 🎯 MASTER FRAMEWORK (ALWAYS START HERE)

👉 Say this first in ANY scenario:

> “I’d approach this by isolating where in the pipeline the issue is occurring—checking system resources, network health, and application behavior to identify the root cause.”

---
# 🔥 1. MARKET DATA DELAY


### Think:

- Where is the delay? (source → network → system → app)

### Commands:
```code
top  
free -h  
ping <host>  
tail -f app.log
```
### Say:

> “I’d check CPU, memory, network latency, and application logs to isolate where the delay is introduced.”



# 2. PACKET LOSS / MISSING TICKS

### Think:

- UDP → packet drops → data gaps

### Commands:

netstat -i  
ethtool -S eth0

### Say:

> “I’d check NIC stats for dropped packets and verify whether the system is handling gap detection or failover.”

---

# 🔥 3. HIGH CPU / LATENCY SPIKE

### Think:

- CPU bottleneck = slower processing

### Commands:


```
top  
htop  
ps -ef | grep <app>

```
### Say:

> “I’d identify high CPU processes and determine whether load, inefficiency, or a bug is causing the spike.”

---

# 🔥 4. NO DATA / APPLICATION DOWN

### Think:

- Is the service running?

### Commands:

```
ps -ef | grep app  
netstat -tulnp  
tail -f app.log

```
### Say:

> “I’d verify the process is running, check logs for errors, and confirm it’s listening on the correct port.”

---

# 🔥 5. DISK FULL / LOG FAILURE

### Think:

- Silent failure risk

### Commands:

```
df -h  
df -i

```
### Say:

> “I’d check disk and inode usage since a full disk can prevent logging and disrupt applications.”

---

# 🔥 6. MEMORY PRESSURE / SWAPPING

### Think:

- Swapping = huge latency impact

### Commands:

```
free -h  
top

```
### Say:

> “I’d check memory usage and swap activity since swapping can severely degrade performance.”

---

# 🔥 7. NETWORK CONNECTIVITY ISSUE

### Think:

- Can systems talk to each other?

### Commands:
```

ping <host>  
traceroute <host>  
netstat -tulnp
```

### Say:

> “I’d verify connectivity, trace the network path, and confirm the service is reachable.”

---

# 🔥 8. LATENCY SPIKE (USING MONITORING)

### Think:

- Use Grafana to pinpoint

### Tools:

- Grafana
- Prometheus

### Say:

> “I’d use Grafana dashboards to identify where latency increases and correlate it with system metrics.”

---

# 🔥 9. DATA INCONSISTENCY / BAD ORDER BOOK

### Think:

- Missing or out-of-order messages

### Check:

- Packet loss
- App logs

### Say:

> “I’d check for dropped packets or processing issues that could lead to inconsistent order book state.”

---

# 🔥 10. CLIENT-REPORTED ISSUE (GENERIC)

### Think:

- Always structure response

### Say:

> “I’d first clarify the issue and impact, then systematically check system, network, and application layers to isolate the root cause.”

---

# 💥 MUST-MENTION KEYWORDS (SPRINKLE THESE)

Use these naturally:

- **Latency**
- **Throughput**
- **Packet loss**
- **Order book**
- **Real-time data**
- **Root cause analysis**
- **Distributed systems**

---

# 🧠 GOLDEN STRUCTURE (MEMORIZE)

For ANY question:

> “First I’d identify where the issue is occurring, then check system resources, network health, and application behavior using tools like top, netstat, and logs to isolate the root cause.”

---

# 🚀 FINAL INTERVIEW HACK

If you forget everything, say this:

> “I’d break the problem down into system, network, and application layers and use monitoring tools and Linux commands to isolate the issue.”

👉 That alone sounds like a solid SRE.

---

# 🔥 You’re now ready for this part of the interview

If you want next:

- I can run a **live rapid-fire mock (you answer, I critique)**
- Or give you a **final 15-minute pre-interview checklist**

Just say 👍