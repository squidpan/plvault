---
categories:
  - "[[Skills]]"
type:
description:
source:
tags:
created: 2026-05-15
last: 2026-05-15
status:
prompts:
origin:
run_id:
input_prompt:
---
## Practice Questions + Answers

### 1. Tell me about yourself.
>[!Mine] 
>I'm a senior **business analyst** and **Application support professional** with experience in supporting **enterprise applications across insurance, financial systems environments**. 
>
>Throughout my career, I’ve worked at the intersection of business operations, QA/UAT, application support, and production release coordination.
>
>Most recently, at the Federal Reserve Bank of New York, I supported **a large-scale streaming market data application** responsible for **ingesting, processing, and distributing real-time pricing data to downstream** trading and financial systems. 
>
>My responsibilities included **requirements gathering and coordination**, PreQA/UAT deployment and testing,  production readiness, troubleshooting support, and **cross-functional coordination** between business, infrastructure, database, and operations teams.
>
  At AIG, I worked on **rolling out travel insurance products and policies** for the APAC region. 

---
****### 2. Why are you interested in AEGIS and this Senior Business Analyst role?****
> [!m]
> 
> The role is very **close to the work I've done** throughout my career. I see this as an opportunity to **bring together my insurance background and my more recent hands-on application support and release coordination experience**. 

---
### 3. Describe your experience with application support.
  >[!m] 
  >At FRBNY, the application operates across on-prem (Linux, Oracle) and AWS cloud infrastructure. 
  >
  >A **typical release cycle** ranged from about **two to six months** depending on the **complexity of the business, infrastructure, and architectural requirements**. 
  >
  >Enhancements and new functionality were **managed in Jira as user stories** with acceptance **criteria** and **categorized as functional or non-functional** requirements.
  >
  >I worked closely with **business users, development teams, DevOps, infrastructure, and operations teams to coordinate release planning** and **ensure enough time was allocated for QA/UAT** testing before production deployment. One of our goals was to provide the business with ==at least three weeks== of testing time in QA/UAT environments before production releases.
  >
  >My responsibilities included **maintaining deployment runbooks, documenting step-by-step implementation procedures, executing and troubleshooting deployments, validating key functional workflows, performing post-release health checks**, and coordinating with DevOps teams to ensure successful deployments across UAT and production environments.

---
### 4. Tell me about your experience with QA and UAT.
>[!m]
>QA and UAT have been a significant part of my work throughout my career, especially in highly regulated financial and insurance environments.
>
>Two areas were especially critical during testing. The **first was data quality** validation. We needed to ensure that **all incoming market price data was successfully processed and distributed downstream with no missing or corrupted data**. For example, if tens of thousands of pricing records entered the system, **the counts and values had to reconcile correctly across downstream systems within expected latency thresholds.** We also ran regression testing throughout the day across development and QA/UAT environments to identify anomalies.
>
>The second area involved **price cleansing workflows**. This was a GUI-based application that allowed business users to identify and manually correct suspect pricing data before redistribution downstream. I developed detailed **step-by-step test scenarios to validate the workflow functionality** and ensure **the release behaved correctly from both technical and user perspectives**.
>
>Earlier in my insurance experience at AIG Travel Guard, QA/UAT activities also included **validating travel policy premium pricing tables** using Excel-based test scenarios and business rules involving variables such as destination, product type, age, and coverage options.
>
>Overall, my approach to QA/UAT focuses on ensuring that functionality, data quality, workflows, and operational readiness are fully validated before production deployment.

### 5. How do you gather and manage requirements?
>[!m]
>One of the largest requirements initiatives I worked on was a **multi-year effort to migrate** a streaming market data application **from a legacy on-premises environment to AWS cloud infrastructure**. The application distributed real-time pricing data to multiple downstream **consumer** systems, so **one of the key business requirements** was ensuring that consumers could **cut over to the cloud platform without losing data integrity or changing the pricing data they received**.
>
>I usually begin requirements gathering by understanding **the business problem, the current workflow, the impacted users, operational pain points, and any downstream dependencies.** From there, I work with business users and technical teams to **translate those needs into user stories, acceptance criteria, test scenarios,** and implementation requirements.
>
>In this particular project, a significant portion of the requirements effort focused on **mapping legacy Oracle pricing table schema into API-friendly JSON payloads for REST-based distribution** through the cloud platform. We needed to **ensure that the cleansed pricing data distributed through the new REST APIs matched the data previously delivered through the legacy on-premises Oracle environment**. 
>
>**The acceptance criteria** included validating **pricing counts, values, and downstream distribution behavior between both environments to ensure consistency and operational readiness before migration**. I worked closely with business users, developers, DevOps, database teams, and downstream consumers throughout the process to coordinate requirements, testing, and deployment readiness. 
>
>

### 6. How have you worked with technical teams?

>[!m]
>I’m comfortable working closely with developers, database teams, infrastructure, DevOps, operations, and business users. **My role is often to make sure the business need is clearly understood**, the technical teams have enough detail to implement, and the business users can validate the result.
>
>For example, in my most recent role, I coordinated deployment activities between business users, infrastructure, database, and operations teams to support successful production releases.

---
### 7. What is your ServiceNow experience?
>[!m]
>My ServiceNow experience has been from the **operational and workflow side rather than as a platform administrator**. I used ServiceNow to coordinate software access, tooling, infrastructure requests, and support/change workflows. In that sense, I understand ServiceNow as more than just a ticketing tool — it supports enterprise workflows, approvals, task assignment, audit trail, and operational coordination.

---
### 8. Tell me about your insurance industry experience.
>[!m]
>I have direct insurance experience through EmblemHealth and AIG. 
>
>At EmblemHealth and at **AIG Property Casualty PMO**, I worked on **HP PPM and Business Objects enhancement requests**, requirements clarification, UAT planning, and stakeholder communication. 
>
>At **AIG Travel Guard**, I supported **global travel insurance system enhancements, e-business operations, distribution channels,** and project closure activities.

---
### 9. Tell me about a time you had to manage changing priorities.

>[!m]
>In release and application support work, **priorities can change quickly because production readiness, QA defects, business needs**, and **infrastructure constraints all compete for attention**. I handled that by keeping a clear view of release scope, risk, dependencies, and stakeholder impact. 
>
>At Gresham/Federal Reserve, I **prioritized functional and non-functional requirements from business, infrastructure, and architecture teams into release**s. When issues came up, I make sure to confer the issue with the team and stay focused **on impact, urgency, dependencies,** and whether the change affected production readiness or user acceptance.

---
### 10. How do you ensure quality in application changes?
>[!m]
>I focus on quality throughout the lifecycle, not just at the end. That means **clear requirements, acceptance criteria, testable user stories,** QA test plans, UAT coordination, deployment validation, and post-release checks. 
>
>In my recent role, I created Pre-QA test plans, tested deployment steps and scripts, validated post-release health checks, and maintained runbooks and troubleshooting procedures. That helped reduce ambiguity and made releases more repeatable.

---
### 11. What is your experience creating documentation, job aids, or training materials?

>[!m]
>
>I’ve created several types of documentation, including operational **runbooks**, deployment documentation, **troubleshooting procedures,** support knowledge bases, rollout materials, **quick reference guides,** and **user training materials** as needed. 
>
>At AIG, I published a **Business Objects Quick Reference Guide for self-service training**. At EmblemHealth, I prepared rollout materials and training for the PPM Resource Management module. More recently, I maintained runbooks and support documentation using Confluence and Visio.

---
### 12. What would you say is your biggest strength for this role?

>[!m]
>
>
My biggest strength is that I can **operate comfortably between business users and technical teams**. I understand requirements, workflows, testing, production support, and release coordination. **I also have prior insurance experience, so I’m familiar with regulated enterprise environments where documentation, approvals, quality, and stakeholder communication matte**r.

---
