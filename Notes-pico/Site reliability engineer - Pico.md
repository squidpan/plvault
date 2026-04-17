---
categories:
  - "[[Jobs]]"
type: []
org:
  - "[[Pico]]"
start:
year:
url: https://job-boards.greenhouse.io/picoquantitativetrading/jobs/4664671006
status:
role: (SRE) Site Reliability Engineer
created: 2026-04-11
tags:
  - pico
---
## Job Description
- Assist clients in solving problems and maximizing the value of Redline products and services within their enterprise.
- Respond promptly to production issues, provide workarounds whenever possible.
- Replicate customer issues and verify fixes for customer patches and releases.
- Manage production environment:

	- Software upgrade
	- Routine changes
	- Proactive monitoring
	- Performance tuning of applications
	- Assess impact of exchange-driven initiatives and participate in relevant weekend testing
---
- Work closely with development engineers to promptly resolve customer requests.
- Work closely with Pico server and network teams for issue troubleshooting and change management.
- Elevate Redline managed practice and ensure customer success by:

- Putting in place the necessary automation and scripting.
- Continuous improvement of tools (monitoring, inventory, runbooks.)
---
- Bachelor’s degree or higher in an Engineering discipline ie. Computer Science, Electrical Engineering, Math or Management Information Systems.
- Experience with financial services front office systems, market data tickerplants, order execution technology and the global exchange technology landscape.
- Strong understanding of Linux and linux performance tuning.
- Solid experience with Intel based computer architecture and IT systems networking.
- Experience with programming and scripting, knowledge of Python, C/C++ or Java is a plus.
- Excellent customer service attitude and interpersonal skills.
- Strong communication skills both written and verbal.
- Experience working in a team-oriented, collaborative environment.
- Task and result oriented with strong work ethics and values.
- Ability to be flexible and adapt to any given situation.
---
## Interview questions

[[Pico]]
[[SRE Interview - Pico]]

### AWS
I’d say I have **a solid working familiarity with AWS,** especially in the context of production systems that rely on it. 

In my most recent role at the Federal Reserve Bank of New York, I supported **a streaming market data application where price quotes were processed on-prem and then distributed to internal consumers through AWS-based infrastructure.**  EKS, MSK, ECS, etc.

While I wasn’t directly provisioning AWS resources, I **worked closely with the system’s data flow across environments** and collaborated with teams responsible for the cloud components. 

Also, I worked with AWS in my environment where I deployed a locally developed Rest API Java Spring boot web app (jar file) to AWS using **AWS Elastic Beanstalk** (run and manage web apps), Elastic Container Services (**ECS**) and Relational Database Service (**RDS**-managed database service). 

This gave me **practical exposure to how AWS is used in a hybrid architecture—particularly around data distribution, system reliability, and troubleshooting across on-prem and cloud boundaries.** I was involved in analyzing data flow issues, understanding how latency and delivery could be impacted, and helping ensure the system met reliability expectations. 

I’m comfortable with core AWS concepts like cloud networking, distributed systems, and monitoring, and I’ve been actively building my hands-on knowledge to deepen my technical skills further. I’m confident I can ramp up quickly in an SRE-focused AWS environment.
### Market data
Yes, I do have experience working with market data, particularly in a real-time streaming context. 

In my most recent role at the Federal Reserve Bank of New York, I supported a market data application that processed and distributed real-time price quotes. The system ingested market data, performed cleansing and consolidation, and then distributed price ticks to internal consumers through a hybrid on-prem and AWS-based architecture.

Through that work, I became **familiar with how real-time market data flows through a system—from ingestion to distribution—and how latency, data quality, and reliability impact downstream consumers.** 

I also have an understanding of historical or Overall, my experience has given me a strong foundation in how market data systems operate and the importance of accuracy, consistency, and low latency.reference data in contrast to real-time data. 

**Real-time data is focused on low-latency delivery of live price updates, while historical data is typically used for analysis, backtesting, or replaying market conditions**.
		
### Trading platforms and Trading APIs  
While I haven’t directly worked on a trading platform or implemented trading APIs myself, I have supported systems that are closely tied to trading workflows.

In my role at the Federal Reserve Bank of New York, **I worked on a real-time market data platform that distributed price ticks to downstream systems, including trading-related applications like Auctions and FedTrade.** These systems relied on the data we provided to make trading and pricing decisions. Because of that, I developed a strong understanding of how critical accurate and low-latency market data is to trading systems. I was involved in analyzing data flow, identifying delays or inconsistencies, and ensuring reliable delivery to those downstream consumers.

So while my experience is more on the market data and infrastructure side rather than direct order execution or API integration, I’ve worked very closely with systems that support trading, and I understand the impact that upstream data has on trading platforms.

### Monitoring tools
I have experience working with monitoring tools, particularly Prometheus and Grafana in a production environment.

In my role at the Federal Reserve Bank of New York, I worked closely with DevOps and operations teams who used Prometheus and Grafana to monitor performance and latency across a hybrid architecture. Specifically, we tracked the end-to-end flow of market data—from when consolidated price ticks left the on-prem application to when they were delivered through AWS to downstream consumers.

While I wasn’t directly configuring dashboards, I regularly used Grafana to analyze metrics and identify latency issues, and collaborated with engineering teams to interpret the data and troubleshoot performance problems.  
This gave me a strong understanding of how monitoring and observability tools are used in real-time systems to detect issues, analyze latency, and ensure reliability.
#### Metrics
We were primarily focused on latency metrics, such as the time it took for price ticks to move from the on-prem system into AWS and reach downstream consumers.  
We also looked at throughput and system health indicators to identify bottlenecks or delays in the pipeline.
#### Prometheus
Prometheus is used to collect and store time-series metrics, which can then be queried and visualized using tools like Grafana.
#### Grafana
Grafana provided visualization of real-time metrics, which made it easier to identify anomalies such as latency spikes or drops in throughput.

By correlating metrics across different parts of the system, we could narrow down where the issue was occurring.
### UNIX - system monitoring and troubleshooting

I’m comfortable using core Linux commands for system monitoring and troubleshooting. For example, I use df to check disk usage, ps and top or htop to monitor processes and CPU utilization, and free to analyze memory usage.

For troubleshooting, I also use tools like tail and grep to analyze logs, and network tools like netstat, ss, or ping to check connectivity and service availability.

In an SRE context, I focus on using these tools to quickly **identify issues such as resource bottlenecks, process failures, or network-related problems that could impact system performance and latency**.

I’d use these commands to quickly isolate whether an issue is system, network, or application related.

**`df`**
If a system is running slowly or failing, I’d check disk usage to ensure logs or data aren’t filling up storage.

**`ps`**
I use ps to identify running processes and verify if critical services like feed handlers are up.”

**`top`**
Shows CPU, memory, processes in real time
If there’s latency in market data, I’d check top to see if CPU is saturated or if a process is consuming excessive resources

**`htop`**
Interactive, easier-to-read version of `top`
I prefer htop for quickly identifying resource-heavy processes and thread-level behavior.

**`free`**
Shows RAM usage
If performance degrades, I check memory usage to see if the system is under pressure or swapping

**`ftp`**
Transfers files over network (less secure)

**`sftp`**
Secure file transfer over SSH
```code
sftp user@server
```
Used to securely transfer logs or configuration files between systems during troubleshoot.

**`netstat`**
Useful to verify if services are listening on expected ports.
shows network connections such as 
- open ports
- listening services
**`ping`**
Quickly check network connectivity between systems

**`traceroute`**
Identify where latency occurs in the network path

```code
traceroute hostname
```
**`ethtool`**
I’d use this to check for packet drops or errors—critical in market data systems.
```code
ethtool -S eth0
```

**`uptime`**
Shows
- System load
- How long system has been running

#### Realistic SRE troubleshooting scenarios

##### SCENARIO 1 — Market Data Feed Delay

I would start by identifying where the delay is introduced in the pipeline.
First, I’d check system resources using tools like top and free to ensure the server isn’t CPU or memory constrained.
Then I’d verify network health using ping or netstat to check for latency or packet loss.
I’d also review application logs using tail to see if there are processing delays or queue backlogs.
The goal is to isolate whether the delay is upstream, network-related, or within the application itself.
Break it into layers:

1. **Upstream (exchange/feed)**
2. **Network**
3. **Server (CPU/memory)**
4. **Application (queue/backlog)**

top: Check CPU usgae
free -h: Memory pressure
ping feed_source: network latency
netstat -i: Packet drops

##### SCENARIO 2 — Packet Loss in Market Data
>[!Client reports]
>“We are missing ticks / data gaps."

Packet loss is critical in market data systems because it can lead to gaps in the order book.
I’d start by checking NIC statistics using tools like netstat or ethtool to identify dropped packets or errors.
Then I’d investigate network congestion or hardware issues.
I’d also verify whether the application is handling gap detection and recovery properly, such as requesting retransmission or failing over to a redundant feed.

Market data often uses **UDP**
- Packet loss = missing data = broken order book

netstat -i
ethtool -S eth0

##### SCENARIO 3 — High CPU Usage (Latency Spike)

>[!Issue]
>System latency increases suddenly.

I’d use top or htop to identify processes consuming high CPU.
If a specific process is causing the issue, I’d investigate whether it’s due to increased load, inefficient processing, or a potential bug.
High CPU usage can directly impact latency in real-time systems, so isolating and resolving the root cause quickly is critical.
top/htop/ps: identify which process is consuming CPU

##### SCENARIO 4 — Application Not Running

>[!client]
>We are not receiving any data.

I’d first verify whether the application is running using ps.
If it’s not running, I’d check logs to understand why it stopped.
If it is running, I’d verify that it’s listening on the correct ports and accepting connections using netstat.
Then I’d continue troubleshooting downstream or upstream dependencies.

```code
ps -ef | grep app_name
netstat -tulnp
tail -f app.log

```

##### SCENARIO 5 — Disk Full (Silent Failure)

>[!situation]
>System behaves strangely, logs stop updating.

I’d check disk usage using df -h to ensure the system isn’t out of space.
If the disk is full, logs may stop writing and applications may fail silently.
I’d also check inode usage with df -i, since running out of inodes can cause similar issues.

```code
df -h
df -i
```
##### SCENARIO 6 — Memory Pressure / Swapping

>[!Situation]
>System is slow, inconsistent latency.


I’d check memory usage using free and top.
If the system is swapping, it can significantly impact performance and latency.
In a real-time system, avoiding swapping is critical, so I’d investigate memory leaks or high memory usage processes.
```code
free -h
top
```

Look for:
- High memory usage
- Swap usage

##### SCENARIO 7 — Network Connectivity Issue

>[!Situation]
>Client cannot connect to service.

I’d first verify basic connectivity using ping.
If that fails, I’d use traceroute to identify where the connection is breaking.
I’d also confirm that the service is running and listening on the expected port using netstat.

```code
ping server
traceroute server
netstat -tulnp


```




---


### TCP UDP differences
TCP is connection-oriented and guarantees delivery, while UDP is connectionless and prioritizes speed over reliability.

In market data systems, UDP is often used because low latency is critical, and systems are designed to handle packet loss and retransmission.

### Intel-based computer architecture and IT systems networking

Key points:

**Intel architecture (practically)**
- CPU cores / threads
- CPU utilization
- Cache, NUMA (basic awareness)
- How CPU affects latency

**Networking**
- TCP vs UDP
- Packet loss, latency
- Multicast (VERY important for market data)
- NIC behavior

I have a solid working understanding of Intel-based systems from a performance and troubleshooting perspective.

In my experience supporting real-time market data systems, I’ve worked with Linux-based environments running on Intel architectures, where CPU utilization, memory usage, and system performance directly impact latency.

I’m familiar with monitoring CPU usage, understanding how processes are scheduled across cores, and how system resource constraints can affect real-time data processing.

On the networking side, I have experience working with distributed systems where low latency and reliable data delivery are critical. I understand key concepts like TCP versus UDP, packet loss, and network latency, and how these factors impact real-time market data pipelines.

Overall, my focus has been on using this knowledge to diagnose performance issues and ensure system reliability in a production environment.

#### 💬 “What do you know about Intel architecture?”

You say:

> At a high level, I understand that Intel-based systems rely on multi-core CPUs where performance depends on efficient use of CPU resources, memory, and caching.
> 
> In low-latency systems, CPU contention, context switching, and cache efficiency can all impact performance, so monitoring and tuning these factors is important.

👉 That’s enough. Don’t overcomplicate.

---
#### 💬 “What is NUMA?” (bonus question)

> NUMA stands for Non-Uniform Memory Access, where memory access time depends on which CPU node is accessing it.
> 
> In performance-sensitive systems, keeping processes and memory on the same NUMA node helps reduce latency.

🔥 This answer is **very impressive if you can deliver it simply**

---

#### 💬 “Why is CPU important in market data systems?”

> Because market data systems process extremely high message rates, CPU performance directly impacts latency.
> 
> If CPU resources are constrained or inefficiently used, it can delay processing and impact downstream systems.

---

#### 🌐 Networking answer (important)

##### 💬 “What networking concepts are you familiar with?”

> I’m familiar with core networking concepts such as TCP vs UDP, latency, packet loss, and connectivity troubleshooting.
> 
> In market data systems, I understand that UDP is often used for low-latency data distribution, and that packet loss needs to be handled through recovery mechanisms.

---

##### 💥 Key positioning (THIS is what wins interviews)

You are NOT:  
❌ “a hardware expert”

You ARE:  
✅ “someone who understands how hardware + networking impact system performance and latency”

---

##### 🔥 Power sentence (memorize this)

> “I focus on how CPU, memory, and network behavior impact latency and reliability in real-time systems.”

---
## Core responsibilities (Tier 2/3)

#### 1. Production troubleshooting
- Investigate:
    - Feed drops
    - Latency spikes
    - Packet loss
    - Data inconsistencies (bad book states)
- Root cause analysis (RCA)
    
👉 Example answer:

> “If market data latency spikes, I’d check NIC stats, packet drops, CPU pinning, and thread contention.”

---
#### 2. System reliability & uptime
- Ensure:    
    - High availability (HA)
    - Failover works correctly
    - Redundant feeds behave as expected

- InRush supports:

	- Gap detection
	- Retransmission
	- Failover between feeds 

---

#### 3. Performance tuning (VERY important)
- CPU affinity / NUMA tuning    
- Kernel tuning (low latency Linux) 
- Network optimization:
    - Multicast
    - UDP tuning
    - Kernel bypass (DPDK/Solarflare/OpenOnload likely)

---

#### 4. Monitoring & observability
- Metrics + alerting (often via Corvil or similar tools)
- Analyze:
    - Tick-to-trade latency
    - Message rates
    - Queue depth

👉 Pico integrates with analytics tools to monitor **nanosecond-level performance** 

---
#### 5. Client-facing support
- Tier 2/3 = **you talk to clients**
- You’ll:
    - Debug client environments
    - Guide configuration
    - Explain issues clearly

- Key skill:
	- Translate deep technical issues into business impact
---

7. Do you know c/c++, Java, python?  
		Yes, c/c++ and Java. 
8. Jira, Confluence
9. Pressure Difficult customer
10. Challenges daily 



