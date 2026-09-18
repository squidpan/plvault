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
Tell me what a runbook is and what it needs to capture in case of the SRE role at pico.

Great question—**runbooks are central to SRE work**, and Pico will absolutely expect you to understand them well.

---

# 🧠 What is a runbook?

## ✅ Simple interview definition

> A runbook is a documented set of procedures and steps that an engineer follows to diagnose and resolve specific operational issues.

---

## 🔧 In plain English

👉 It’s a **step-by-step guide for handling incidents**

Think:

- “If X happens → do A, B, C”

---

# 🎯 Why runbooks matter (especially at Pico)

In a **low-latency trading environment**:

- Incidents happen fast
- Impact is high (trading \$$ )
- You don’t have time to “figure things out from scratch”

👉 Runbooks ensure:

- Fast response
- Consistency
- Reduced downtime

---

# 🔥 What a good runbook contains (SRE at Pico)

This is the **most important part**—memorize this structure.

---

## 🧩 1. Problem description

> What is the issue?

Example:

- “Market data delay”
- “Missing ticks”
- “Feed disconnect”

---

## 🚨 2. Impact

> What is affected?

- Clients not receiving data
- Latency spike
- Order book inconsistency

---

## 🔍 3. Detection

> How do you know it’s happening?

- Alerts (Prometheus/Grafana)
- Client reports
- Monitoring dashboards

---

## 🔧 4. Troubleshooting steps (CORE SECTION)

This is where your Linux/network knowledge comes in.

Example:

```
top  
free -h  
netstat -i  
ethtool -S eth0  
tail -f app.log

```
👉 Step-by-step:

1. Check CPU
2. Check memory
3. Check NIC stats
4. Check logs

---

## 🔁 5. Resolution steps

> What actions fix the issue?

- Restart service
- Switch to backup feed
- Clear backlog
- Engage network team

---

## 🔄 6. Validation

> How do you confirm it’s fixed?

- Latency returns to normal
- No packet loss
- Clients confirm recovery

---

## 📢 7. Communication

> What do you tell clients/stakeholders?

- Status update
- ETA
- Resolution confirmation

---

## 🧠 8. Root cause (post-incident)

> Why did it happen?

- CPU overload
- Packet loss
- Misconfiguration

---

## 🛠️ 9. Prevention

> How to avoid it again?

- Add monitoring
- Tune system
- Improve alerts

---

# 💥 Example (Pico-specific runbook)

## Scenario: Market Data Delay

### Problem

- Clients reporting delayed ticks

### Detection

- Grafana shows latency spike

### Troubleshooting

```
top  
free -h  
ping feed_source  
netstat -i  
tail -f app.log

```
### Resolution

- Identify CPU bottleneck
- Restart service or rebalance load

### Validation

- Latency back to normal

---

# 💬 Interview-ready answer

> A runbook is a structured set of procedures used to diagnose and resolve operational issues.
> 
> In an SRE role, especially in a low-latency system like Pico’s, a runbook typically includes the problem description, impact, detection methods, step-by-step troubleshooting procedures, resolution steps, and validation.
> 
> It may also include communication guidelines and post-incident analysis to prevent recurrence.
> 
> Runbooks are critical for ensuring fast and consistent responses to incidents in production systems.

---

# 🔥 What Pico REALLY wants to hear

👉 Not just “documentation”

They want:

> “Someone who can follow and improve runbooks to reduce incident response time.”

---

# 🚀 Bonus (very strong statement)

> “Runbooks help standardize incident response and reduce mean time to resolution, which is critical in real-time trading systems.”

🔥 That’s **SRE language**

---

# 🧠 One-line memory trick

> Runbook = “playbook for fixing production issues quickly”

---

# 🚀 If you want next level

I can:

- Help you **write a real Pico-style runbook (you can talk through it in interview)**
- Or simulate a **scenario where they ask you to design one live**

Just say 👍

Help you write a real Pico-style runbook (you can talk through it in interview)

Perfect—this is exactly the kind of thing that can **differentiate you from other candidates**.

I’ll give you a **realistic Pico-style runbook** you can:

- Talk through in the interview
- Reference naturally
- Show you think like an SRE

---

# 📘 🧠 PICO SRE RUNBOOK

## Scenario: Market Data Delay / Latency Spike

---

## 🔹 1. Problem Description

> Clients are experiencing delayed market data (price ticks arriving slower than expected).

---

## 🔹 2. Impact

- Increased latency in market data delivery
- Potential stale order books
- Trading decisions impacted

---

## 🔹 3. Detection

### Alerts / Monitoring:

- Latency spike observed in Grafana dashboards
- Metrics from Prometheus exceed threshold

### Client Symptoms:

- “Data is delayed”
- “Ticks arriving late”

---

## 🔹 4. Initial Triage (FIRST 2–3 minutes)

### Questions:

- Is this affecting **one client or multiple clients**?
- Is it **one feed or all feeds**?

👉 Helps isolate:

- Local issue vs system-wide issue

---

## 🔹 5. Troubleshooting Steps (CORE)

## 🧩 A. System Resource Check

top  
free -h

Check:

- CPU saturation
- Memory pressure

---

## 🧩 B. Network Health

```
ping <feed_source>  
netstat -i  
ethtool -S eth0

```
Check:

- Packet loss (RX-DRP)
- Latency spikes
- NIC errors

---

## 🧩 C. Application / Feed Handler

ps -ef | grep inrush  
tail -f app.log

Check:

- Process running
- Backlogs / delays
- Error messages

---

## 🧩 D. Feed Integrity

Check:

- Missing sequence numbers
- Gap detection logs
- Failover status (primary vs backup feed)

---

## 🧩 E. Monitoring Correlation

Use Grafana:

- Identify when latency spike started
- Correlate with:
    - CPU
    - Network
    - Throughput

---

## 🔹 6. Root Cause Identification

Possible causes:

- CPU overload
- Packet loss (network/NIC)
- Feed congestion
- Application backlog
- Upstream exchange issue

---

## 🔹 7. Resolution Actions

Depending on root cause:

### If CPU issue:

- Restart or rebalance process
- Adjust resource allocation

### If packet loss:

- Switch to backup feed
- Escalate to network team

### If application backlog:

- Restart service
- Clear queue

### If upstream issue:

- Confirm with provider
- Notify clients

---

## 🔹 8. Validation

Confirm:

- Latency returns to normal (Grafana)
- No packet drops
- Clients confirm recovery

---

## 🔹 9. Communication

### During incident:

- “We are investigating elevated latency in market data delivery.”

### After resolution:

- “Latency has returned to normal; root cause identified as [X].”

---

## 🔹 10. Post-Incident (RCA)

Document:

- Root cause
- Timeline
- Impact

---

## 🔹 11. Prevention

- Add alert thresholds
- Improve monitoring
- Tune system (CPU/network)

---

# 🎯 How to talk through this in interview (VERY IMPORTANT)

## 💬 Say something like:

> For example, if there’s a market data latency issue, I’d follow a structured runbook approach—starting with identifying scope and impact, then checking system resources, network health, and application behavior using tools like top, netstat, and logs.
> 
> I’d correlate findings with monitoring dashboards like Grafana to pinpoint where latency is introduced, then take appropriate action such as resolving resource bottlenecks or switching feeds.
> 
> Finally, I’d validate recovery and document the root cause to prevent recurrence.

---

# 💥 Why this is powerful

You’re demonstrating:

- Structured thinking
- Real SRE workflow
- Knowledge of Pico systems
- Command-line + monitoring usage

---

# 🧠 One-line memory version

> “Identify → Check system/network/app → Correlate metrics → Fix → Validate → Document”

---

# 🚀 If you want next level

I can:

- Give you **2–3 more runbooks (packet loss, feed down, bad order book)**
- Or simulate a **live interview where you walk through this under pressure**

Just say 👍