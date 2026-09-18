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
During the interview they will ask me if I am familiar with AWS. Can you suggest how I should answer the question? Here is my background and indirect experience with AWS. At the Federal Reserve Bank of New York (FRBNY), my most recent job, I worked as a business analyst to support the Bank's streaming market data price quote application that distributes price ticks that are cleansed and consolidated from the on-premises Linux client server application to FRBNY internal market data consumers thru the AWS cloud infrastructure.

  

You’re actually in a **great position**—you _do_ have relevant AWS experience, just not in a “hands-on DevOps engineer” way. The key is to **frame it confidently and translate it into SRE-relevant skills**.

Here’s how to answer it effectively 👇

---

# ✅ Strong interview answer (tailored to you)

Writing

I’d say I have solid working familiarity with AWS, especially in the context of production systems that rely on it.

In my most recent role at the Federal Reserve Bank of New York, I supported a streaming market data application where price quotes were processed on-prem and then distributed to internal consumers through AWS-based infrastructure. While I wasn’t directly provisioning AWS resources, I worked closely with the system’s data flow across environments and collaborated with teams responsible for the cloud components.

This gave me practical exposure to how AWS is used in a hybrid architecture—particularly around data distribution, system reliability, and troubleshooting across on-prem and cloud boundaries. I was involved in analyzing data flow issues, understanding how latency and delivery could be impacted, and helping ensure the system met reliability expectations.

I’m comfortable with core AWS concepts like cloud networking, distributed systems, and monitoring, and I’ve been actively building my hands-on knowledge to deepen my technical skills further. I’m confident I can ramp up quickly in an SRE-focused AWS environment.

---

# 🎯 Why this answer works

It does **3 important things**:

### 1. ✅ You don’t undersell yourself

You _were_ working with AWS systems—even if indirectly.

---

### 2. ✅ You align with SRE responsibilities

You emphasize:

- Reliability
    
- Latency
    
- Troubleshooting
    
- Distributed systems
    

👉 That’s exactly what Pico cares about.

---

### 3. ✅ You show growth mindset

You admit:

> “not hands-on provisioning”

…but follow with:

> “actively building hands-on knowledge”

This is **much better than pretending**.

---

# 🔧 If they push deeper (VERY likely)

## 💬 Follow-up: “What AWS services are you familiar with?”

You can say:

Writing

Given my exposure, I’m most familiar with AWS at an architectural level—particularly how services are used to support distributed applications.

For example, I understand how compute services like EC2 are used to host applications, how networking is handled through VPCs and load balancing, and how data streaming or messaging services can be used to distribute real-time data.

In my role, I interacted more from a system and data flow perspective—understanding how data moved from on-prem systems into AWS and how issues in that pipeline could impact latency or delivery.

---

# 💡 Optional upgrade (if you want to stand out)

Add ONE concrete guess (even if you didn’t configure it):

> “I believe the architecture likely involved EC2-based services and possibly load balancing or streaming services for distributing the data…”

This shows:

- Curiosity
    
- Systems thinking
    
- Cloud awareness
    

---

# 🚫 What NOT to say

Avoid:

- “I don’t have AWS experience” ❌
    
- “I only did business analysis” ❌
    
- Overclaiming hands-on Terraform/Kubernetes ❌
    

---

# 🔥 Pro tip for THIS specific role (very important)

For Pico + Redline:

👉 They care LESS about AWS  
👉 They care MORE about:

- Linux
    
- Networking
    
- Latency
    
- Market data systems
    

So your strategy is:

> “I understand AWS in context, but my strength is in system behavior, reliability, and data flow.”

---

# 🚀 If you want to go one level deeper

I can give you:

- **Top 10 AWS questions they might ask (with answers)**
    
- Or a **mock interview specifically for Pico SRE**
    

Yes I want to go one level deeper. give me the Tops 10 questions with answers and mock interview for pico SRE

  

Great—this is exactly the right move. I’ll give you two things:

1. **Top 10 AWS questions (with strong, realistic answers tailored to YOU)**
    
2. **A realistic Pico SRE mock interview (what they’ll likely ask + how to answer)**
    

---

# 🔥 PART 1 — Top 10 AWS Questions (with answers tailored to your background)

## 1. What AWS services are you familiar with?

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
> 1. **Network:** Check for packet loss, latency between on-prem and AWS
>     
> 2. **Compute:** CPU utilization, resource contention
>     
> 3. **Application:** Queue backlogs, thread delays
>     
> 4. **Data pipeline:** Any bottlenecks in ingestion or distribution
>     
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

**Answer:**

> Autoscaling automatically adjusts the number of compute instances based on demand.
> 
> While less common in ultra-low latency trading systems, it’s important in general distributed systems for handling variable load.

---

## 10. How does AWS fit into a hybrid architecture?

**Answer (THIS ONE IS GOLD FOR YOU):**

> In a hybrid setup, on-prem systems handle critical or latency-sensitive workloads, while AWS provides scalable distribution, processing, or access layers.
> 
> In my role, market data was processed on-prem and then distributed through AWS to internal consumers, so understanding how those environments interacted was key to troubleshooting and ensuring reliability.