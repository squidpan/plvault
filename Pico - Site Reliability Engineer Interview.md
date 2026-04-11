---
categories:
  - "[[Meetings]]"
type:
  - "[[Job Interviews]]"
org:
people: []
date: 2026-04-10
role:
rating:
created: 2026-04-10
---
## Questions and topics

### Monitoring tools

# ✅ Strong, interview-ready answer

Writing

Yes, I have experience working with monitoring tools, particularly Prometheus and Grafana in a production environment.

In my role at the Federal Reserve Bank of New York, I worked closely with DevOps and operations teams who used Prometheus and Grafana to monitor performance and latency across a hybrid architecture. Specifically, we tracked the end-to-end flow of market data—from when consolidated price ticks left the on-prem application to when they were delivered through AWS to downstream consumers.

While I wasn’t directly configuring dashboards, I regularly used Grafana to analyze metrics and identify latency issues, and collaborated with engineering teams to interpret the data and troubleshoot performance problems.

This gave me a strong understanding of how monitoring and observability tools are used in real-time systems to detect issues, analyze latency, and ensure reliability.

---

# 🎯 Why this answer is powerful

### ✅ 1. You confidently say “YES”

You **did work with monitoring tools**—don’t qualify it too weakly.

---

### ✅ 2. You name-drop the right tools

- Prometheus
- Grafana

👉 These are industry-standard and **highly relevant to SRE roles**

---

### ✅ 3. You emphasize WHAT matters most

- Latency tracking
- End-to-end visibility
- Real-time systems

👉 This is exactly what Pico does with market data

---

# 🔥 If they push deeper (very likely)

## 💬 “What kind of metrics were you looking at?”

Strong answer:

> We were primarily focused on latency metrics, such as the time it took for price ticks to move from the on-prem system into AWS and reach downstream consumers.
> 
> We also looked at throughput and system health indicators to identify bottlenecks or delays in the pipeline.

---

## 💬 “How did Grafana help you troubleshoot issues?”

> Grafana provided visualization of real-time metrics, which made it easier to identify anomalies such as latency spikes or drops in throughput.
> 
> By correlating metrics across different parts of the system, we could narrow down where the issue was occurring.

---

## 💬 “What is Prometheus used for?”

> Prometheus is used to collect and store time-series metrics, which can then be queried and visualized using tools like Grafana.

---

# 💡 Optional power upgrade (this is 🔥)

Add this sentence if you want to stand out:

> “That experience helped me understand the importance of observability in distributed systems, especially for diagnosing latency across system boundaries.”

---

# 🚀 How Pico will interpret your answer

They won’t think:  
❌ “He didn’t configure dashboards”

They WILL think:  
✅ “He understands how monitoring is used in real-time trading systems”

---

# 💥 Key insight (very important)

For Pico SRE:

👉 Using monitoring tools > configuring monitoring tools

They care more about:

- Can you **read metrics**
- Can you **interpret latency**
- Can you **debug systems using observability**

---

# 🚀 If you want to go even deeper

I can:

- Give you a **quick crash course on Prometheus + Grafana (so you sound like a pro)**
- Or simulate a **full interview combining AWS + Linux + market data + monitoring**

Just say 👍



###  Did you ever worked supported any trading platforms? Trading APIs?

>[!answer]
>While I haven’t directly worked on a trading platform or implemented trading APIs myself, I have supported systems that are closely tied to trading workflows.
>
In my role at the Federal Reserve Bank of New York, I worked on a real-time market data platform that distributed price ticks to downstream systems, including trading-related applications like Auctions and FedTrade. These systems relied on the data we provided to make trading and pricing decisions. Because of that, I developed a strong understanding of how critical accurate and low-latency market data is to trading systems. I was involved in analyzing data flow, identifying delays or inconsistencies, and ensuring reliable delivery to those downstream consumers.
So while my experience is more on the market data and infrastructure side rather than direct order execution or API integration, I’ve worked very closely with systems that support trading, and I understand the impact that upstream data has on trading platforms.


### Do you understand how trading systems work?

At a high level, I understand that trading systems rely on real-time market data to make decisions and execute orders.

Market data feeds provide price updates, which are processed into order books, and trading systems use that information to determine when and how to place orders.

My experience has been on the data side of that pipeline, ensuring that the information reaching those systems is accurate and timely.





###  Are you familiar with market data (real time or historical reference) ?

>[!Answer]
>Yes, I do have experience working with market data, particularly in a real-time streaming context.
>In my most recent role at the Federal Reserve Bank of New York, I supported a market data application that processed and distributed real-time price quotes. The system ingested market data, performed cleansing and consolidation, and then distributed price ticks to internal consumers through a hybrid on-prem and AWS-based architecture.
>
>Through that work, I became familiar with how real-time market data flows through a system—from ingestion to distribution—and how latency, data quality, and reliability impact downstream consumers.
I also have an understanding of historical or reference data in contrast to real-time data. Real-time data is focused on low-latency delivery of live price updates, while historical data is typically used for analysis, backtesting, or replaying market conditions.
Overall, my experience has given me a strong foundation in how market data systems operate and the importance of accuracy, consistency, and low latency.



---

### Are you familiar with AWS?

>[!AWS - my experience]
>I’d say I have solid working familiarity with AWS, especially in the context of production systems that rely on it.
>
>In my most recent role at the Federal Reserve Bank of New York, I supported a streaming market data application where price quotes were processed on-prem and then distributed to internal consumers through AWS-based infrastructure. 
>
>While I wasn’t directly provisioning AWS resources, I worked closely with the system’s data flow across environments and collaborated with teams responsible for the cloud components.
>
>This gave me practical exposure to how AWS is used in a hybrid architecture—particularly around data distribution, system reliability, and troubleshooting across on-prem and cloud boundaries. I was involved in analyzing data flow issues, understanding how latency and delivery could be impacted, and helping ensure the system met reliability expectations.
>
>I’m comfortable with core AWS concepts like cloud networking, distributed systems, and monitoring, and I’ve been actively building my hands-on knowledge to deepen my technical skills further. I’m confident I can ramp up quickly in an SRE-focused AWS environment.

### What AWS services are you familiar with?

>[!AWS services]
>Given my exposure, I’m most familiar with AWS at an architectural level—particularly how services are used to support distributed applications.
>>For example, I understand how compute services like EC2 are used to host applications, how networking is handled through VPCs and load balancing, and how data streaming or messaging services can be used to distribute real-time data.
>>In my role, I interacted more from a system and data flow perspective—understanding how data moved from on-prem systems into AWS and how issues in that pipeline could impact latency or delivery.


### 1. What AWS services are you familiar with?

**Strong answer:**

> I’ve worked with AWS in the context of a hybrid architecture at the Federal Reserve Bank of New York, where market data processed on-prem was distributed through AWS infrastructure.
> 
> I’m familiar with core services conceptually—like EC2 for compute, VPC for networking, and how load balancing and data distribution services fit into a real-time pipeline.
> 
> My experience is more on the system and data flow side, particularly understanding how issues across on-prem and cloud environments impact latency and reliability.

---

## 2. What is a VPC?

**Answer:**

> A VPC, or Virtual Private Cloud, is a logically isolated network in AWS where you can define IP ranges, subnets, routing, and security controls.
> 
> It allows organizations to replicate a traditional data center network in the cloud, which is especially important in hybrid setups like the one I worked with.

---

## 3. What is EC2?

**Answer:**

> EC2 is AWS’s virtual server offering. It allows you to run applications in the cloud with control over OS, networking, and compute resources.
> 
> In low-latency systems like market data, EC2 instances are often tuned for performance and may be part of a larger distributed system.

---

## 4. How would you troubleshoot a latency issue in an AWS-based system?

**Answer (VERY important):**

> I’d approach it layer by layer:
> 
> 1. **Network:** Check for packet loss, latency between on-prem and AWS
> 2. **Compute:** CPU utilization, resource contention
> 3. **Application:** Queue backlogs, thread delays
> 4. **Data pipeline:** Any bottlenecks in ingestion or distribution
> 
> Given my experience with streaming market data, I’d especially focus on where delays are introduced between ingestion and delivery.

---

## 5. What is the difference between TCP and UDP?

**Answer:**

> TCP is connection-oriented and guarantees delivery, while UDP is connectionless and prioritizes speed over reliability.
> 
> In market data systems, UDP is often used because low latency is critical, and systems are designed to handle packet loss and retransmission.

---

## 6. What is high availability in AWS?

**Answer:**

> High availability means designing systems to remain operational even when components fail.
> 
> In AWS, this is typically achieved using multiple Availability Zones, redundancy, and failover mechanisms.
> 
> In my experience, reliability was critical in ensuring uninterrupted market data delivery.

---

## 7. What is a load balancer?

**Answer:**

> A load balancer distributes incoming traffic across multiple instances to improve performance and reliability.
> 
> It helps prevent overload on a single node and ensures failover if one instance goes down.

---

## 8. What is CloudWatch?

**Answer:**

> CloudWatch is AWS’s monitoring service. It collects metrics, logs, and allows alerting.
> 
> While I didn’t directly configure it, I understand its role in observability and how it helps detect issues like latency spikes or failures.

---

## 9. What is autoscaling?


>[!Answer] 
>Autoscaling automatically adjusts the number of compute instances based on demand.
> 
> While less common in ultra-low latency trading systems, it’s important in general distributed systems for handling variable load.

---

## 10. How does AWS fit into a hybrid architecture?

**:**

> [!Answer (THIS ONE IS GOLD FOR YOU)]
> In a hybrid setup, on-prem systems handle critical or latency-sensitive workloads, while AWS provides scalable distribution, processing, or access layers.
> 
> In my role, market data was processed on-prem and then distributed through AWS to internal consumers, so understanding how those environments interacted was key to troubleshooting and ensuring reliability.


2. Are you familiar with market data, real-time or historical reference?
3. Have you ever supported any trading platforms? How about trading APIs?
4. Do you know c/c++/java, python?
5. Have you worked with Unix commands to check the reliability of the system such as df, ps, top, htop, free?
6. Are you familiar with ftp/sftp protocols?
7. What monitoring applications or tools did you use?
8. What is the difference between TCP and UDP? 

## Notes

- 

