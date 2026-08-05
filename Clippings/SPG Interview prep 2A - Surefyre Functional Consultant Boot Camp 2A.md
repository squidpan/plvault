---
categories:
  - "[[Clippings]]"
title: SPG Interview prep 2 - Surefyre Functional Consultant Boot Camp 2A
source: https://chatgpt.com/g/g-p-6a5517dc2a148191b5c289c2f4d2ce72/c/6a6b4867-a174-83ea-8e69-f7608b9878cc
author:
published:
created: 2026-08-05
description: Surefyre Functional Consultant Boot Camp 2A
tags:
  - chatgpt/conversation
---
Yes. The ETA is reasonable **provided we keep today focused on producing the complete study package rather than trying to master every topic while we write it**.

From roughly 1:30 p.m., four to five concentrated hours puts us around **5:30–6:30 p.m. today**. In that time, we can realistically complete:

1. Boot Camp Session 2A and 2B
2. Insurance Domain 101
3. The core PlantUML diagrams
4. Configuration Workshop summaries for JSON, JavaScript, Python, REST, OpenAPI, and Postman
5. MRPrice-to-SPG experience mappings
6. Interview questions and draft answers
7. A final condensed cheat sheet for tomorrow’s study
    

We should keep the main notes detailed enough to understand but create a second, much shorter set of interview cheat sheets. Tomorrow should be for repetition, speaking answers aloud, and mock questions—not creating more foundational material.

# Surefyre Functional Consultant Boot Camp

## Session 2A — Insurance Ecosystem, Specialty Insurance, MGAs, Agents, Carriers, and “The Business”

## 1. The basic insurance ecosystem

At the highest level, insurance involves four core participants:

**Person or business needing insurance  
→ Agent or broker who helps obtain coverage  
→ MGA, wholesaler, or insurance company that evaluates the submission  
→ Insurance carrier that accepts the financial risk**

In a simple consumer transaction, an insurance agent may submit directly to a carrier.

In specialty insurance, the chain is often longer:

**Business customer  
→ Retail insurance agent  
→ Wholesale broker or MGA  
→ Insurance carrier**

Surefyre is intended primarily for the middle of that chain: MGAs, MGUs, and wholesalers that need a digital agent portal and an internal underwriting workbench. ([Vertafore](https://www.vertafore.com/products/underwriting-workbench/surefyre?utm_source=chatgpt.com "Surefyre - Underwriting Workbench & Agent Portal"))

---

# 2. Insurance carrier

An **insurance carrier** is the regulated insurance company that ultimately takes on the financial risk.

Examples include:

- Travelers
- Chubb
- Hartford
- AIG
- Liberty Mutual
- Zurich
- CNA
    

The carrier:

- provides the insurance capacity
- defines its risk appetite
- establishes underwriting guidelines
- collects premium
- assumes responsibility for covered losses
- pays valid claims
- maintains financial reserves
- complies with insurance regulation
    

## Simple example

A restaurant pays $12,000 for one year of insurance coverage.

The carrier agrees to pay covered losses, subject to:

- policy limits
- deductibles
- exclusions
- terms and conditions
    

The carrier is therefore taking on the financial risk.

## Why would a carrier use an MGA?

A carrier may want to enter a specialized market but may not have:

- specialized underwriters
- distribution relationships
- local market expertise
- technology
- operational capacity
- sufficient volume to build its own program
    

Instead, the carrier may authorize an MGA to underwrite that business within agreed rules.

---

# 3. Retail insurance agent

A **retail insurance agent or broker** works directly with the person or business seeking insurance.

The NAIC uses the broader term **producer** for someone who sells, solicits, or negotiates insurance; the term includes both agents and brokers. ([NAIC](https://content.naic.org/insurance-topics/producer-licensing?utm_source=chatgpt.com "Insurance Topics | Producer Licensing"))

A retail agent may:

- interview the customer
- gather business and risk information
- identify needed coverage
- complete applications
- request loss-history documentation
- submit the risk to insurers, wholesalers, or MGAs
- present quotes
- help the customer select coverage
- assist with renewals and policy changes
    

## Example

A restaurant owner tells a local insurance agent:

> I need property, general liability, workers’ compensation, and liquor-liability coverage.

The retail agent gathers:

- location
- type of restaurant
- annual revenue
- payroll
- cooking methods
- liquor sales
- prior claims
- requested coverage limits
    

The retail agent may then submit that information through the Surefyre Agent Portal.

Surefyre describes its agent portal as one centralized place where external agents can submit business, communicate with the underwriting organization, run quotes, track policy status, and download files. ([Vertafore](https://www.vertafore.com/products/underwriting-workbench/surefyre?utm_source=chatgpt.com "Surefyre - Underwriting Workbench & Agent Portal"))

## Important distinction

The retail agent is usually:

- an external user of Surefyre
- a distribution partner
- the person submitting business
    

The retail agent is generally **not the MGA**.

---

# 4. Wholesale broker

A **wholesale insurance broker** sits between the retail agent and specialty insurance markets.

Retail agents may contact a wholesale broker when:

- the risk is difficult to place
- the standard market declined it
- the risk is unusual
- specialized coverage is required
- the retail agent lacks access to the appropriate carrier
    

The wholesale broker:

- knows specialty markets
- has relationships with specialty carriers and MGAs
- helps structure the submission
- finds a market willing to consider the risk
- obtains and communicates quotes
    

## Example

A retail agent has a customer operating:

- a nightclub
- a high-value coastal property
- a hazardous manufacturing operation
- a large public event
- a trucking fleet with prior losses
    

The retail agent may not have direct access to an insurer willing to write that risk. A wholesale broker helps find the appropriate specialty market.

---

# 5. MGA — Managing General Agent

An **MGA** is an insurance intermediary with authority delegated by an insurance carrier.

The precise authority varies by contract, but an MGA may be authorized to:

- evaluate submissions
- apply underwriting rules
- quote coverage
- bind coverage
- issue policies
- collect premiums
- manage agents
- administer policies
- sometimes oversee claims-related functions
    

An MGA therefore does more than merely pass a submission to a carrier.

It can perform parts of the carrier’s underwriting and administration work.

## Mental model

A retail agent says:

> Here is a business that needs insurance.

The MGA says:

> Based on the carrier’s delegated authority and underwriting rules, we will determine whether we can accept the risk, what coverage we can offer, and at what price.

The carrier says:

> You may underwrite this category of business on our behalf, provided you stay within our agreed rules and authority.

## MGA versus carrier

| MGA                                   | Carrier                                   |
| ------------------------------------- | ----------------------------------------- |
| Underwrites under delegated authority | Ultimately bears the insurance risk       |
| May quote and bind                    | Provides insurance capacity               |
| May manage agent relationships        | Pays covered claims                       |
| Specializes in a market or program    | Maintains reserves and regulatory capital |
| Earns commissions and fees            | Earns premium and carries loss exposure   |

## MGA versus retail agent

| Retail agent                          | MGA                                      |
| ------------------------------------- | ---------------------------------------- |
| Works directly with insured customer  | Works with agents, brokers, and carriers |
| Gathers customer requirements         | Evaluates and underwrites risk           |
| Seeks coverage from markets           | May quote and bind coverage              |
| External Surefyre portal user         | Internal Surefyre workbench user         |
| Represents customer’s placement needs | Exercises carrier-delegated authority    |

---

# 6. MGU — Managing General Underwriter

You may also hear **MGU**, or Managing General Underwriter.

In practice, MGA and MGU are sometimes used interchangeably, although MGU emphasizes underwriting authority and technical risk selection.

Surefyre is positioned for:

- MGAs
- MGUs
- wholesalers
    

Its workbench centralizes submission, rating, quoting, and risk-selection workflows. ([Vertafore](https://www.vertafore.com/products/underwriting-workbench/surefyre?utm_source=chatgpt.com "Surefyre - Underwriting Workbench & Agent Portal"))

For the interview, you do not need to argue fine legal distinctions.

A safe statement is:

> “An MGA or MGU is an intermediary that has delegated authority from one or more carriers to perform underwriting and potentially quote, bind, or administer specialized insurance business.”

---

# 7. What is specialty insurance?

**Specialty insurance** covers risks that do not fit comfortably into ordinary, standardized insurance products.

The risk may be:

- unusual
    
- complex
    
- high-value
    
- hazardous
    
- new or emerging
    
- difficult to price
    
- outside a standard carrier’s guidelines
    
- in a niche industry requiring specialist expertise
    

## Standard insurance example

A typical small office building in a low-risk area may fit a carrier’s standard underwriting model.

The application, rating, and coverage may be relatively predictable.

## Specialty insurance example

A carrier may consider the following more specialized:

- coastal property exposed to hurricanes
    
- cyber risk for a technology company
    
- professional liability for a medical specialist
    
- insurance for a nightclub
    
- aviation
    
- marine cargo
    
- entertainment events
    
- cannabis businesses
    
- high-risk construction
    
- trucking fleets
    
- directors and officers liability
    
- unusual product liability
    
- excess or surplus coverage
    

Specialty insurance exists because the risks cannot always be handled using one standard application and one standard rating model.

## Why Surefyre matters here

Each specialty program may require different:

- application questions
    
- forms
    
- underwriting rules
    
- referral thresholds
    
- rating logic
    
- carrier integrations
    
- documents
    
- approval workflows
    
- agent experiences
    

That variability is why a configurable platform is valuable.

Surefyre’s low-code/no-code model is designed to allow MGAs and wholesalers to configure agent onboarding, application forms, rating, routing, and underwriting workflows without requiring a full software-development cycle for every product change. ([Vertafore](https://www.vertafore.com/resources/blog/why-mgas-need-underwriting-workbench?utm_source=chatgpt.com "Why MGAs need an underwriting workbench"))

---

# 8. Insurance program

A **program** is a packaged insurance offering designed for a defined type of customer or risk.

A program may specify:

- eligible businesses
    
- coverage provided
    
- supported states
    
- carrier
    
- underwriting guidelines
    
- rates
    
- limits
    
- deductibles
    
- exclusions
    
- required forms
    
- delegated authority
    
- referral conditions
    

## Example: Restaurant program

A restaurant insurance program might define:

- eligible restaurant types
    
- maximum annual sales
    
- allowable liquor-sales percentage
    
- required fire-suppression equipment
    
- acceptable prior-loss history
    
- supported states
    
- maximum building value
    
- coverage limits
    
- pricing formulas
    
- conditions requiring senior-underwriter review
    

## Why programs matter to the Technical Consultant

The Technical Consultant converts that program into Surefyre configuration:

- form fields
    
- conditional questions
    
- validation
    
- rules
    
- calculations
    
- workflows
    
- document requirements
    
- integration mappings
    
- notifications
    
- user permissions
    

This is why the JD emphasizes applying product expertise to unique customer scenarios and then identifying best practices that can be reused elsewhere.

---

# 9. The insured or policyholder

The **insured** is the person or organization protected by the policy.

The **policyholder** is the person or organization named on the insurance contract.

Often they are the same entity.

Examples:

- restaurant owner
    
- trucking company
    
- manufacturer
    
- medical practice
    
- technology company
    
- property owner
    
- event organizer
    

The insured may not directly use Surefyre.

The likely external Surefyre user is the retail agent submitting the insured’s information.

However, some insurance portals can eventually support direct insured interaction. We should not assume SPG’s exact design without asking.

---

# 10. Insurance underwriter

The **underwriter** evaluates whether the insurer or MGA should accept a risk and under what terms.

The underwriter considers:

- nature of the business
    
- location
    
- exposure
    
- prior claims
    
- financial information
    
- safety practices
    
- requested limits
    
- deductibles
    
- risk controls
    
- carrier guidelines
    
- profitability
    
- completeness and reliability of the information
    

The underwriter may decide to:

- accept
    
- request more information
    
- refer for senior approval
    
- modify terms
    
- apply exclusions
    
- increase premium
    
- adjust limits or deductibles
    
- decline the risk
    

Surefyre’s underwriting workbench centralizes these submissions, data, tasks, rules, rating, quoting, and decision workflows. ([Vertafore](https://www.vertafore.com/products/underwriting-workbench/surefyre?utm_source=chatgpt.com "Surefyre - Underwriting Workbench & Agent Portal"))

---

# 11. Underwriting authority

**Underwriting authority** defines what decisions a person or organization is allowed to make.

For example, a junior underwriter may be allowed to:

- quote businesses with revenue below $2 million
    
- accept risks with no more than one prior loss
    
- provide limits up to $1 million
    

A senior underwriter may have greater authority.

An MGA’s agreement with a carrier may define:

- industries it may write
    
- states it may cover
    
- maximum limits
    
- pricing flexibility
    
- prohibited risks
    
- referral thresholds
    
- binding authority
    

## How this becomes system configuration

The business rule:

> Risks with liquor sales above 40% require senior approval.

May become:

- calculate liquor-sales percentage
    
- set referral flag
    
- prevent automatic quote
    
- route task to senior-underwriter queue
    
- display referral reason
    
- create audit record
    
- notify the responsible user
    

That conversion of underwriting policy into system behavior is central to the Technical Consultant role.

---

# 12. SPG’s likely place in the ecosystem

A simplified view is:

**Business needing coverage  
→ Retail agent  
→ SPG specialty business/MGA/wholesaler  
→ Insurance carrier**

SPG operates specialty insurance businesses. Surefyre provides the agent-facing submission portal and internal underwriting workbench used to streamline application, rating, quoting, and collaboration across those parties. SPG selected Surefyre as part of a modernization effort focused on improving submissions and operational efficiency. ([Vertafore](https://www.vertafore.com/resources/press-releases/specialty-program-group-partners-vertafore-streamline-submissions-and-boost-operational-efficiency?utm_source=chatgpt.com "Specialty Program Group partners with Vertafore"))

The exact legal and operating role may vary among SPG business units:

- some may function as MGAs
    
- some may be wholesalers
    
- some may be program administrators
    
- some may operate specialty underwriting programs
    

You do not need to assume every SPG unit works identically.

---

# 13. Who is “the customer”?

The JD uses “customer” in several places, including configuring Surefyre to meet customer needs and making changes to customer Surefyre instances.

That term may refer to several kinds of stakeholders.

## Possible customer types

### An SPG business unit

A specialty business within SPG that needs a new insurance program configured.

### An underwriting team

The internal business group whose forms, rules, queues, and workflows must be implemented.

### A program administrator or MGA

An organization using Surefyre to manage a specialized insurance offering.

### A wholesaler

An organization receiving submissions from retail agents and placing business with specialty markets.

### An enterprise insurance client

A large insurance organization with:

- multiple programs
    
- many agents
    
- complex integrations
    
- security requirements
    
- multiple user roles
    
- high transaction volume
    

### An external retail agency

The agency may be an external platform user rather than the contracting implementation customer.

## Interview-safe answer

> “I understand that ‘customer’ may refer to an SPG business unit, MGA, wholesaler, underwriting program, or other enterprise insurance organization whose Surefyre instance is being configured. The retail agent is also an important external user, but the internal underwriting and operations teams are likely the primary stakeholders defining how the system must work.”

---

# 14. Who is “the business”?

In enterprise implementation work, **the business** usually means the people who own or operate the business process—not everyone who uses the software.

For Surefyre, “the business” may include:

- underwriting managers
    
- underwriters
    
- underwriting assistants
    
- operations
    
- program managers
    
- product management
    
- sales
    
- Professional Services
    
- compliance
    
- finance
    
- agent-distribution management
    

## Retail agents are business users, but not necessarily “the business owners”

The retail agent uses the portal and has important usability needs.

However, the internal underwriting and operations stakeholders generally define:

- eligibility
    
- required data
    
- underwriting rules
    
- routing
    
- referral logic
    
- quote process
    
- carrier requirements
    
- controls
    
- service-level expectations
    

## Helpful distinction

|Stakeholder|Likely role|
|---|---|
|Retail agent|External user and distribution partner|
|Insured business|End customer receiving coverage|
|Underwriter|Internal decision-maker|
|Operations|Processes and administers work|
|Program manager|Owns product/program outcomes|
|Carrier|Provides capacity and underwriting requirements|
|IT and Security|Governs technical integration and access|
|Technical Consultant|Converts requirements into configuration|
|Engineering|Handles product-level or complex technical changes|
|Professional Services|Coordinates implementation and customer delivery|

---

# 15. How Surefyre connects the participants

## Agent Portal

Used primarily by external agents to:

### Inputs

- insured information
    
- business details
    
- locations
    
- exposure data
    
- prior losses
    
- requested coverage
    
- supporting documents
    

### Outputs

- validation messages
    
- requests for missing information
    
- quote information
    
- status updates
    
- messages from underwriting
    
- downloadable documents
    
- policy-related files
    

## Underwriting Workbench

Used primarily by internal underwriters and operations to:

### Inputs

- agent submission
    
- documents
    
- third-party data
    
- carrier guidelines
    
- rating results
    
- workflow tasks
    
- prior communications
    

### Outputs

- eligibility decision
    
- request for information
    
- referral
    
- quote
    
- decline
    
- underwriting notes
    
- task assignment
    
- bind decision
    
- data passed to downstream systems
    

Surefyre’s published materials describe the platform as supporting the complete workflow from submission through rating, quoting, underwriting, and bind while connecting agents and underwriters. ([Vertafore](https://www.vertafore.com/products/underwriting-workbench/surefyre?utm_source=chatgpt.com "Surefyre - Underwriting Workbench & Agent Portal"))

---

# 16. High-level lifecycle

A useful working model is:

## 1. Customer seeks insurance

A business owner contacts a retail agent.

## 2. Agent collects information

The agent identifies coverage needs and gathers risk data.

## 3. Agent submits through Surefyre

The portal validates required information and documents.

## 4. Surefyre routes the submission

Rules determine:

- correct program
    
- underwriting queue
    
- required review
    
- missing information
    
- potential referral
    

## 5. Underwriter evaluates the risk

The underwriter reviews:

- exposure
    
- eligibility
    
- losses
    
- documents
    
- carrier rules
    
- rating information
    

## 6. Additional information may be requested

The underwriter communicates with the agent through the portal or workflow.

## 7. Risk is rated

The system or external rating service calculates a potential premium.

## 8. Quote is issued

The agent receives terms and pricing.

## 9. Customer accepts

The agent requests binding of coverage.

## 10. Coverage is bound

The MGA or authorized party confirms coverage.

## 11. Downstream systems are updated

Policy, transaction, and document information flows into systems such as AIM and ImageRight.

We will cover AIM and ImageRight in Session 2B.

---

# 17. What the Technical Consultant does across this ecosystem

The Technical Consultant does not personally act as the retail agent, underwriter, or carrier.

You enable their work.

## Your likely responsibilities

- interview underwriting and operations stakeholders
    
- understand the specialty program
    
- model the agent-submission process
    
- identify required fields and documents
    
- translate underwriting rules into form and workflow logic
    
- configure the Agent Portal
    
- configure the Underwriting Workbench
    
- create or modify JSON schemas
    
- add JavaScript behavior
    
- configure integrations
    
- prepare Python migration utilities
    
- test APIs in Postman
    
- support UAT
    
- document instance changes
    
- reproduce problems
    
- coordinate with Engineering, Product, IT, and Security
    

That interpretation closely follows the actual SPG JD.

---

# 18. How to explain this in the interview

## “What is an MGA?”

> “An MGA is an insurance intermediary that has delegated authority from a carrier to perform underwriting and, depending on its agreement, potentially quote, bind, issue, or administer policies. It sits between retail agents and carriers and often specializes in a particular market or insurance program.”

## “What is specialty insurance?”

> “Specialty insurance addresses risks that do not fit standard insurance products because they are unusual, complex, high-risk, emerging, or require specialized underwriting expertise. Each specialty program may require different forms, rules, rating logic, documents, and carrier relationships, which is why a configurable platform such as Surefyre is useful.”

## “Who uses Surefyre?”

> “The external retail agent primarily uses the Agent Portal to submit business, provide documents, communicate with underwriting, obtain quotes, and track status. Internal underwriters and operations teams use the workbench to review submissions, apply underwriting rules, request information, rate and quote risks, route work, and make decisions.”

## “Who is the business?”

> “The core business stakeholders are likely the underwriting, operations, program-management, product, and Professional Services teams that define how a particular insurance program should operate. Retail agents are critical external users, but the internal business owners define the eligibility, workflow, rating, referral, and operational requirements.”

---

# 19. What you need to remember—not memorize

For Friday, reduce this session to six ideas:

1. **The insured needs coverage.**
    
2. **The retail agent gathers information and submits the risk.**
    
3. **The MGA or wholesaler evaluates and processes specialty business.**
    
4. **The carrier ultimately accepts the financial risk.**
    
5. **The Agent Portal supports the external agent.**
    
6. **The Underwriting Workbench supports internal underwriting and operations.**
    

Your role sits across all of them:

> **Understand the business process and turn it into forms, rules, workflows, integrations, tests, and supportable configuration.**

# Today’s working schedule

A reasonable production schedule is:

|Approximate time|Deliverable|
|---|---|
|1:30–2:10|Boot Camp Session 2A|
|2:10–2:50|Session 2B: lifecycle, AIM, ImageRight|
|2:50–3:30|PlantUML diagram set|
|3:30–4:10|Insurance Domain 101|
|4:10–5:10|Configuration Workshop summary|
|5:10–5:50|MRPrice mappings and interview answers|
|5:50–6:30|Final cheat sheets and study plan|

That is achievable, but we should avoid spending too long polishing each Obsidian note on the first pass. Capture the complete content first, then trim during the final cheat-sheet phase.