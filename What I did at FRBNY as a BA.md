---
categories:
  - "[[Skills]]"
type:
loc:
tags:
  - skills
created: 2026-03-18
last: 2026-03-29
---

## What is NPQS again?
- ticker pricing application that distributes streaming market data pricing (bid/ask) to internal Fed Systems both in real-time and snapshot formats.
- architecturally, it is a client server system operating on 2 nodes failover configuration where redundancy is at the database and the application levels.
- asset classes such as Bills, Bonds, Notes, Coupons,etc.
- 


## So what kind of system did you work on over there?

I worked on a system called NPQS that distributes consolidated pricing data (BID, ASK) for 8 fixed income (i.e debt) asset securities to internal business units at the BANK. 
Market data pricing services migrated from on-premises infrastructure that is linux based to in-cloud infrastructure running across Redhat Openshift4 and AWS EKS environment.




Pricing REST API services deliver consolidated, cleansed streaming market price data feeds to BANK's internal consumer applications operating on both on-premises and in-cloud.

## Describe the technology stack of NPQS

The on-premise stack:
- Servers PRIME 7.4.x: update, query, replication servers running on Linux
- DBs: Oracle - Consumer database views (legacy: linked between multiple BUs)
- Resilience: 2 nodes failover: Primary and Dr - East West
- 
Cloud stack:

Private Cloud: Use Openshift4 with AWS environments for NPQS was being built out.


## And what was your role?

Worked with Product Owner (PO), Scrum master, architecture, development and operations support team in an Agile delivery environment to manage release requirements as JIRA stories for the development team, testing, deploying code to the QA environment:
  
• Manage releases of pricing services: planning, deployment, testing, documentation, coordination across teams.  
• Perform release activities, test Linux command line deployments, and environment readiness.  
• Move code through environments, smoke test and troubleshoot deployment issues.  
• Create and manage project requirements and tracking issues in Jira/Confluence.  
• Prioritize functional, non-functional requirements from Business, infrastructure, architecture into releases.  
• Document deployment steps, key technical implementation of releases to stakeholders.  
• Map legacy relational database pricing schemas to Rest API payload data format in Json