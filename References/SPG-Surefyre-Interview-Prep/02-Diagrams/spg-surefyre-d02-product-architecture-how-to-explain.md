
# D2 — Surefyre Product Architecture

## Purpose

This diagram explains **how Surefyre fits into the insurance ecosystem** and how information moves from the external retail agent to internal underwriting and then into enterprise insurance systems.

Unlike D1, which explained *who* participates in the insurance process, D2 explains **how the software supports that process**.

---

# Core Message

Surefyre is the digital platform that connects:

* external retail agents
* internal underwriting teams
* enterprise insurance systems
* document repositories
* carrier and rating services

The Technical Consultant configures and supports this platform.


---
![[spg-surefyre-d02-product-architecture-v2_PNG.png]]

---

# Walkthrough

## Step 1 — Retail Agent

The process begins with the retail agent.

The agent:

* gathers customer information
* completes the application
* uploads supporting documents
* submits the insurance request

The retail agent never works directly in AIM or ImageRight.

Their primary interface is the **Surefyre Agent Portal**.

---

## Step 2 — Agent Portal

The Agent Portal is the front door into Surefyre.

It provides:

* online applications
* document upload
* validation
* communication
* submission tracking
* quote retrieval
* status updates

Think of it as the customer-facing application.

---

## Step 3 — Rules and Workflow Engine

Once submitted, Surefyre evaluates the submission.

Typical activities include:

* required-field validation
* conditional questions
* eligibility checks
* workflow routing
* referral rules
* queue assignment
* notification generation

This layer contains much of the configurable business logic.

---

## Step 4 — Underwriting Workbench

Internal users work here.

Typical users include:

* underwriters
* underwriting assistants
* operations analysts
* managers

The workbench allows them to:

* review submissions
* request additional information
* evaluate risk
* calculate or obtain rates
* generate quotes
* approve
* refer
* decline
* bind

---

## Step 5 — Enterprise Systems

The workbench exchanges information with enterprise systems.

### AIM

AIM is the operational insurance platform.

It manages information such as:

* accounts
* policies
* transactions
* premiums
* producers
* operational data

Think of AIM as the operational "system of record."

---

### ImageRight

ImageRight manages:

* applications
* correspondence
* uploaded documents
* generated PDFs
* workflow documents
* audit records

Rather than storing documents directly inside Surefyre, references and metadata are exchanged with ImageRight.

---

### Carrier / Rating / Third-Party Services

Surefyre also communicates with external systems.

Examples include:

* rating engines
* carrier APIs
* risk-scoring services
* address validation
* business-information providers
* fraud detection

These integrations enrich the submission and support underwriting decisions.

---

# Where the Technical Consultant fits

The Technical Consultant does not replace the underwriter.

Instead, they configure and support the platform.

Typical responsibilities include:

* requirements gathering
* workflow design
* JSON configuration
* JavaScript configuration
* REST integrations
* document mapping
* testing
* troubleshooting
* deployment support
* documentation

---

# MRPrice Bridge

The implementation pattern is similar to the work I performed supporting MRPrice.

At the Federal Reserve Bank of New York I worked with:

* business stakeholders
* developers
* QA
* operations
* infrastructure

to support a mission-critical platform.

Although the business domain was market data instead of insurance, the implementation lifecycle was very similar:

* understand requirements
* configure or coordinate changes
* validate data
* test integrations
* support releases
* monitor production
* resolve issues

---

# Interview Questions This Diagram Supports

## "Tell me what you understand about Surefyre."

Use the diagram.

---

## "Where does AIM fit?"

Use the diagram.

---

## "Where does ImageRight fit?"

Use the diagram.

---

## "Who uses the Agent Portal?"

Use the diagram.

---

## "Who uses the Workbench?"

Use the diagram.

---

## "Where would you work?"

Point to:

* Rules
* Workflow
* Workbench
* Integrations

Explain that your role is configuring and supporting those components.

---

# 30-Second Version

> "Retail agents submit business through the Surefyre Agent Portal. Surefyre validates the submission, applies workflow rules, and routes it to the Underwriting Workbench where internal users review the risk, request additional information, generate quotes, or make underwriting decisions. The workbench exchanges information with systems like AIM for operational insurance data, ImageRight for document management, and carrier or rating services through integrations. My role as a Technical Consultant would be to configure those workflows, forms, integrations, and business rules and support them through testing, deployment, and production."

---

# Transition to D3

D2 explained **where the software fits**.

D3 answers the next question:

> **"What actually happens to a submission from beginning to end?"**

Instead of focusing on the platform architecture, D3 follows a **single insurance submission** as it moves through validation, underwriting, quoting, binding, and policy issuance.

---

# Next: D3 — Agent Submission Lifecycle

I actually think **D3 is where everything starts to click**. It's analogous to the Farm Credit business activity diagrams we created. Rather than showing software boxes, D3 tells a business story. We'll design it so that you can explain the entire insurance lifecycle in about **90 seconds**, and from that point on, terms like **submission**, **quote**, **bind**, **issue**, and **renewal** will have a concrete place in the flow instead of being vocabulary to memorize.
