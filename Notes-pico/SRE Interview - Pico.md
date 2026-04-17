---
categories:
  - "[[Meetings]]"
  - "[[Jobs]]"
type:
  - "[[Job Interviews]]"
org:
  - "[[Pico]]"
people: []
date: 2026-04-10
role:
rating:
created: 2026-04-11
tags:
  - pico
---
# Company

[[Pico]]

## Meeting with Skarlet Goetchius

- Skarlet is from HR and is not technical.
- She asked me about
	- my Python experience: I don't have experience but since I am familiar with Java, I told her that if needed, I should be able to understand the coded logic, make basic updates. I need to better undestand specific scenaros that require working with Python. Knowing this, I will be able to target my learning towards effectively supporting the tass
	- c/c++: I have c/c++ experience: I explained that the formulas engine code used in Streaming market data price quote system I supported at the Fed is simiiar to C/C++.
	- this is a new role that formalizes what the team always has been doing.
	- I will be reporting to Olieen in Dublin who is Alex's manager also
	- Skarlet will ping Olieen tomorrow to see if she can interview me and will let me know. I said I am open all week but need to remind her that I will not be available tomorrow Tuesdat from 2-3:30pm
	- She said she will send me info on Redline product and this is the product I will be supporting. I think she means Redline feed product
	- she asked me and I told her I was making $170k at Gresham and that $125k compensation for this role is fine. I told her I need insurance benefits (medical, dental, etc.)
	- She reminded me that it is a big drop in income, and I said yes and am willing to work with that number. 
	- It's because I need this job even though I will be in the hole every month like $3000+ compared to the 170k salary. 
	- also the medical premium for me and jinie is like $800 to $1200/month.
	- 
- 



## Unix

[[SRE Interview Prep]]

[[Linux]]

[[Linux performance tuning]]

[[Prometheus and Graphan]]


## Monitoring tools 

>[!Prometheus and Grafana]-
>I have experience working with monitoring tools, particularly Prometheus and Grafana in a production environment.
>
>In my role at the Federal Reserve Bank of New York, I worked closely with DevOps and operations teams who used Prometheus and Grafana to monitor performance and latency across a hybrid architecture. Specifically, we tracked the end-to-end flow of market data—from when consolidated price ticks left the on-prem application to when they were delivered through AWS to downstream consumers. 
>
>While I wasn’t directly configuring dashboards, I regularly used Grafana to analyze metrics and identify latency issues, and collaborated with engineering teams to interpret the data and troubleshoot performance problems.
This gave me a strong understanding of how monitoring and observability tools are used in real-time systems to detect issues, analyze latency, and ensure reliability.

---
### Metrics were you looking at

>[!latency: onprem -> AWS -> downstream]-
>We were primarily focused on latency metrics, such as the time it took for price ticks to move from the on-prem system into AWS and reach downstream consumers. 
>We also looked at throughput and system health indicators to identify bottlenecks or delays in the pipeline.
 
---

### Grafana troubleshoot issues

>[!Latency spikes/drops]-
>Grafana provided visualization of real-time metrics, which made it easier to identify anomalies such as latency spikes or drops in throughput. 
>
>By correlating metrics across different parts of the system, we could narrow down where the issue was occurring.

---

### Prometheus

Prometheus is used to collect and store time-series metrics, which can then be queried and visualized using tools like Grafana.

---

> “That experience helped me understand the importance of observability in distributed systems, especially for diagnosing latency across system boundaries.”

---
## Trading platforms and APIs

>[!FedTrade Auctions and Trading]-
>While I haven’t directly worked on a trading platform or implemented trading APIs myself, I have supported systems that are closely tied to trading workflows. 
>
>In my role at the Federal Reserve Bank of New York, I worked on a real-time market data platform that distributed price ticks to downstream systems, including trading-related applications like Auctions and FedTrade. These systems relied on the data we provided to make trading and pricing decisions. Because of that, I developed a strong understanding of how critical accurate and low-latency market data is to trading systems. I was involved in analyzing data flow, identifying delays or inconsistencies, and ensuring reliable delivery to those downstream consumers. 
>
>So while my experience is more on the market data and infrastructure side rather than direct order execution or API integration, I’ve worked very closely with systems that support trading, and I understand the impact that upstream data has on trading platforms.
### How trading systems work?

>[!high level]-
>At a high level, I understand that trading systems rely on real-time market data to make decisions and execute orders.
>
>Market data feeds provide price updates, which are processed into order books, and trading systems use that information to determine when and how to place orders. 
>
>My experience has been on the data side of that pipeline, ensuring that the information reaching those systems is accurate and timely.
##  Market data

>[!realtime historical reference]-
>Yes, I do have experience working with market data, particularly in a real-time streaming context. 
>
>In my most recent role at the Federal Reserve Bank of New York, I supported a market data application that processed and distributed real-time price quotes. The system ingested market data, performed cleansing and consolidation, and then distributed price ticks to internal consumers through a hybrid on-prem and AWS-based architecture.
>
>Through that work, I became familiar with how real-time market data flows through a system—from ingestion to distribution—and how latency, data quality, and reliability impact downstream consumers. 
>
>I also have an understanding of historical or Overall, my experience has given me a strong foundation in how market data systems operate and the importance of accuracy, consistency, and low latency.reference data in contrast to real-time data. 
>
>Real-time data is focused on low-latency delivery of live price updates, while historical data is typically used for analysis, backtesting, or replaying market conditions.

---
## AWS

>[!hybrid at Fed]-
>I’d say I have solid working familiarity with AWS, especially in the context of production systems that rely on it. 
>
>In my most recent role at the Federal Reserve Bank of New York, I supported a streaming market data application where price quotes were processed on-prem and then distributed to internal consumers through AWS-based infrastructure. 
>
>While I wasn’t directly provisioning AWS resources, I worked closely with the system’s data flow across environments and collaborated with teams responsible for the cloud components. 
>
>This gave me practical exposure to how AWS is used in a hybrid architecture—particularly around data distribution, system reliability, and troubleshooting across on-prem and cloud boundaries. I was involved in analyzing data flow issues, understanding how latency and delivery could be impacted, and helping ensure the system met reliability expectations. 
>
>I’m comfortable with core AWS concepts like cloud networking, distributed systems, and monitoring, and I’ve been actively building my hands-on knowledge to deepen my technical skills further. I’m confident I can ramp up quickly in an SRE-focused AWS environment.

### AWS services

>[!ec2 etc]-
>I’ve worked with AWS in the context of a hybrid architecture at the Federal Reserve Bank of New York, where market data processed on-prem was distributed through AWS infrastructure. 
>
>I’m familiar with core services conceptually—like EC2 for compute, VPC for networking, and how load balancing and data distribution services fit into a real-time pipeline. 
>
>My experience is more on the system and data flow side, particularly understanding how issues across on-prem and cloud environments impact latency and reliability.

---

### VPC

>[!logically isolated network]-
>A VPC, or Virtual Private Cloud, is a logically isolated network in AWS where you can define IP ranges, subnets, routing, and security controls.
>
>It allows organizations to replicate a traditional data center network in the cloud, which is especially important in hybrid setups like the one I worked with.

---

### EC2

>[!virtual server]-
>EC2 is AWS’s virtual server offering. It allows you to run applications in the cloud with control over OS, networking, and compute resources.
>
>In low-latency systems like market data, EC2 instances are often tuned for performance and may be part of a larger distributed system.

---

### Troubleshoot a latency in AWS systems

>[!layer by layer]-
>1. **Network:** Check for packet loss, latency between on-prem and AWS
>2. **Compute:** CPU utilization, resource contention
>3. **Application:** Queue backlogs, thread delays
>4. **Data pipeline:** Any bottlenecks in ingestion or distribution
>
>Given my experience with streaming market data, I’d especially focus on where delays are introduced between ingestion and delivery.

---
## TCP and UDP

>[!connection-oriented/connectionless]-
>TCP is connection-oriented and guarantees delivery, while UDP is connectionless and prioritizes speed over reliability. 
>
>In market data systems, UDP is often used because low latency is critical, and systems are designed to handle packet loss and retransmission.

---
### 6. High availability in AWS

>[!HA]-
>High availability means designing systems to remain operational even when components fail. 
>
>In AWS, this is typically achieved using multiple Availability Zones, redundancy, and failover mechanisms. 
>
>In my experience, reliability was critical in ensuring uninterrupted market data delivery.

---
### Load balancer

>[!distributes traffic]-
>A load balancer distributes incoming traffic across multiple instances to improve performance and reliability. 
>
>It helps prevent overload on a single node and ensures failover if one instance goes down.

---
### What is CloudWatch

>[!collect metrics]-
>CloudWatch is AWS’s monitoring service. It collects metrics, logs, and allows alerting. 
>
>While I didn’t directly configure it, I understand its role in observability and how it helps detect issues like latency spikes or failures.

---

### Autoscaling

>[!scale load]- 
>Autoscaling automatically adjusts the number of compute instances based on demand. 
>
>While less common in ultra-low latency trading systems, it’s important in general distributed systems for handling variable load.

---

### AWS and hybrid architecture

>[!onprem data thru aws]- 
>In a hybrid setup, on-prem systems handle critical or latency-sensitive workloads, while AWS provides scalable distribution, processing, or access layers.
>
>In my role, market data was processed on-prem and then distributed through AWS to internal consumers, so understanding how those environments interacted was key to troubleshooting and ensuring reliability.

## C/C++ Java Python

## Notes



