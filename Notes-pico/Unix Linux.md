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
they will ask my Unix/Linux experience and knowledge of commands including these: df, ps -ef, top, htop, free, ftp, sftp. Can you give me a refresher on what these commands do, how to use them with examples in the context of role of SRE at Pico. also any additional Unix commands that this SRE role might require to use

# Need to know
- CPU pinning / taskset
- IRQ affinity
- HugePages
- NUMA
- Kernel tuning (`sysctl`)
-

Perfect—this is **core SRE territory**, especially for a Pico / low-latency environment. You don’t need to be a Linux admin, but you _must sound comfortable diagnosing systems quickly_.

I’ll give you:

1. **Each command explained simply**
    
2. **How to use it (with examples)**
    
3. **How to frame it in an SRE / trading system context**
    
4. **Extra commands they LOVE to see**
    

---

# 🧠 1. `df` — Disk Space

## 🔹 What it does

Shows disk usage (how full your filesystem is)

## 🔹 Command

df -h

## 🔹 Example output

Filesystem      Size  Used Avail Use% Mounted on  
/dev/sda1        50G   45G   5G   90% /

## 🔹 SRE context (VERY important)

> “If a system is running slowly or failing, I’d check disk usage to ensure logs or data aren’t filling up storage.”

👉 In trading systems:

- Full disk = logs stop writing
    
- Can break market data ingestion
    

---

# 🧠 2. `ps -ef` — Process List

## 🔹 What it does

Shows all running processes

## 🔹 Command

ps -ef | grep java

## 🔹 Example

user  1234  1  0 10:00 ?  00:00:05 java -jar marketdata.jar

## 🔹 SRE context

> “I use ps to identify running processes and verify if critical services like feed handlers are up.”

---

# 🧠 3. `top` — Real-time system monitoring

## 🔹 What it does

Shows CPU, memory, processes in real time

## 🔹 Command

top

## 🔹 Key things to look at:

- CPU usage
    
- Memory usage
    
- High CPU processes
    

## 🔹 SRE context

> “If there’s latency in market data, I’d check top to see if CPU is saturated or if a process is consuming excessive resources.”

---

# 🧠 4. `htop` — Better version of top

## 🔹 What it does

Interactive, easier-to-read version of `top`

## 🔹 Command

htop

## 🔹 Why better

- Visual CPU usage
    
- Easier process management
    

## 🔹 SRE context

> “I prefer htop for quickly identifying resource-heavy processes and thread-level behavior.”

---

# 🧠 5. `free` — Memory usage

## 🔹 What it does

Shows RAM usage

## 🔹 Command

free -h

## 🔹 Example

              total   used   free  
Mem:           16G    12G    4G

## 🔹 SRE context

> “If performance degrades, I check memory usage to see if the system is under pressure or swapping.”

---

# 🧠 6. `ftp` — File transfer (older)

## 🔹 What it does

Transfers files over network (less secure)

## 🔹 Command

ftp server_ip

## 🔹 SRE context

> Rarely used in modern systems  
> Mention awareness only

---

# 🧠 7. `sftp` — Secure file transfer

## 🔹 What it does

Secure file transfer over SSH

## 🔹 Command

sftp user@server

## 🔹 Example

put log.txt  
get data.csv

## 🔹 SRE context

> “Used to securely transfer logs or configuration files between systems during troubleshooting.”

---

# 🔥 2. HIGH-VALUE COMMANDS (these impress interviewers)

These are **more important than ftp** for Pico.

---

## 🔹 `netstat` / `ss` — Network connections

netstat -tulnp

or

ss -tulnp

👉 Shows:

- Open ports
    
- Listening services
    

💬 Say:

> “Useful to verify if services are listening on expected ports.”

---

## 🔹 `ping` — Connectivity

ping hostname

💬 SRE use:

> “Quickly check network connectivity between systems.”

---

## 🔹 `traceroute` — Network path

traceroute hostname

💬 Use:

> “Identify where latency occurs in the network path.”

---

## 🔹 `netstat -i` or `ethtool` — NIC stats (VERY IMPORTANT)

ethtool -S eth0

💬 Say:

> “I’d use this to check for packet drops or errors—critical in market data systems.”

🔥 This is **VERY impressive for Pico**

---

## 🔹 `tail` — Log monitoring

tail -f application.log

💬 SRE use:

> “Monitor logs in real time during incidents.”

---

## 🔹 `grep` — Search logs

grep ERROR application.log

💬 Use:

> “Quickly identify errors or patterns in logs.”

---

## 🔹 `df -i` — Inodes (advanced)

👉 Disk can be “full” even if space exists

💬 Bonus:

> “I’d also check inode usage if files aren’t being created.”

---

## 🔹 `uptime`

uptime

Shows:

- System load
    
- How long system has been running
    

---

# 🎯 How to answer in interview

## 💬 “What Linux commands are you familiar with?”

Say something like:

Writing

I’m comfortable using core Linux commands for system monitoring and troubleshooting. For example, I use df to check disk usage, ps and top or htop to monitor processes and CPU utilization, and free to analyze memory usage.

For troubleshooting, I also use tools like tail and grep to analyze logs, and network tools like netstat, ss, or ping to check connectivity and service availability.

In an SRE context, I focus on using these tools to quickly identify issues such as resource bottlenecks, process failures, or network-related problems that could impact system performance and latency.

---

# 💥 Final tip (THIS is what they want to hear)

Don’t just list commands.

Always tie to:

- **Latency**
    
- **Reliability**
    
- **Troubleshooting**
    

👉 Example:

> “I’d use these commands to quickly isolate whether an issue is system, network, or application related.”

---

# 🚀 If you want next level prep

I can:

- Give you **real troubleshooting scenarios (like: feed delay, packet loss, CPU spike)**
    
- Or do a **rapid-fire Linux quiz like a real interviewer**
    

Just say 👍
