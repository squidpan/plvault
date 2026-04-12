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

## Interview questions

[[Pico]]
[[SRE Interview - Pico]]

### AWS

I’d say I have solid working familiarity with AWS, especially in the context of production systems that rely on it. 

In my most recent role at the Federal Reserve Bank of New York, I supported a streaming market data application where price quotes were processed on-prem and then distributed to internal consumers through AWS-based infrastructure. 

While I wasn’t directly provisioning AWS resources, I worked closely with the system’s data flow across environments and collaborated with teams responsible for the cloud components. 

I have experience working with AWS in my environment using Spring boot microserives application that interacts with AWS.

This gave me practical exposure to how AWS is used in a hybrid architecture—particularly around data distribution, system reliability, and troubleshooting across on-prem and cloud boundaries. I was involved in analyzing data flow issues, understanding how latency and delivery could be impacted, and helping ensure the system met reliability expectations. 

I’m comfortable with core AWS concepts like cloud networking, distributed systems, and monitoring, and I’ve been actively building my hands-on knowledge to deepen my technical skills further. I’m confident I can ramp up quickly in an SRE-focused AWS environment.





2. Market data (real time or historical reference)  
		Yes. talk about NPQS
		
3. Trading platforms and Trading APIs  
		
4. Do you know c/c++, Java, python?  
		Yes, c/c++ and Java. 
5. UNIX(df, ps -ef, top, htop, free, ftp, sftp, free)
		
6. Monitoring tools

7. TCP UDP differences
8. Jira, Confluence
9. Pressure Difficult customer
10. Challenges daily 

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




