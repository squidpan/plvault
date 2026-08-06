# D3 — Agent Submission Lifecycle: How to Explain

## Purpose

D3 explains the business lifecycle of a typical insurance submission from the moment a retail agent starts an application through underwriting, quoting, binding, and policy issuance.

D1 explained the participants.

D2 explained where Surefyre fits technically.

D3 explains what happens to one submission from beginning to end.

## Core message

A retail agent gathers information and documents, Surefyre validates and routes the submission, an underwriter evaluates the risk and determines the outcome, and enterprise systems record the resulting policy transaction and documents.

The Technical Consultant enables this process by configuring the forms, validation, workflow, routing, integrations, testing, and production support behind it.

## Walkthrough

### 1. Start the submission

The retail agent selects the appropriate insurance product or program and begins a new application.

Typical information includes:

- applicant identity
- business locations
- operations and exposures
- requested coverage
- prior losses
- limits and deductibles
- supporting documents

### 2. Portal validation

The Surefyre Agent Portal validates the application before it reaches underwriting.

Validation may include:

- required fields
- valid formats
- conditional questions
- supported states
- document completeness
- basic eligibility rules

If information is missing or invalid, the agent corrects and resubmits it.

### 3. Create and route the submission

Once complete, Surefyre:

- creates a submission identifier
- identifies the correct insurance program
- applies routing rules
- assigns the underwriting queue
- notifies the underwriting team

This is a key configuration area for the Technical Consultant.

### 4. Underwriting review

The underwriter reviews:

- applicant and exposure information
- uploaded documents
- prior losses
- carrier and program guidelines
- eligibility and authority
- rating inputs

The underwriter may request more information from the agent.

The portal provides the communication path and tracks the updated status.

### 5. Rating and outcome

The underwriter obtains or calculates the rating and determines the outcome.

Possible outcomes include:

- quote
- referral
- request for additional action
- decline

D3 emphasizes the normal quote path. D4 will focus on underwriting decisions, referrals, authority, and exceptions.

### 6. Quote presentation

When a quote is available:

- Surefyre publishes the quote and status
- the retail agent reviews the terms
- the agent presents the quote to the insured
- the insured accepts, declines, or requests changes

### 7. Bind and issue

When the insured accepts:

- the agent requests binding
- underwriting confirms requirements
- coverage is bound
- enterprise systems create or update the policy transaction
- policy documents are stored
- the portal displays bound or issued status
- the agent receives confirmation and documents

## Key insurance terms

### Submission

The application, risk information, and documents presented for underwriting consideration.

### Quote

An offer of insurance containing proposed coverage, terms, limits, deductibles, and premium.

### Bind

The act of confirming that coverage is in force, subject to the agreed terms and effective date.

### Issue

The creation and delivery of the formal policy and related documents.

### Referral

Routing a risk to another underwriter or authority level because it falls outside normal guidelines or authority.

## 30-second explanation

> A retail agent starts an application in the Surefyre Agent Portal, enters the applicant and risk information, and uploads the required documents. Surefyre validates the submission and routes it to the appropriate underwriting queue. The underwriter reviews the risk, requests additional information when needed, obtains rating, and determines whether to quote, refer, or decline. When a quote is accepted, underwriting binds coverage, the downstream systems record the policy transaction and documents, and Surefyre returns the final status and documents to the agent.

## 60-second explanation

> D3 follows one insurance submission from beginning to end. The retail agent enters the applicant, exposure, coverage, and document information through the Surefyre Agent Portal. The portal validates required fields, formats, conditional questions, and document completeness. Once the submission is complete, Surefyre creates the submission, applies program rules, and assigns it to the correct underwriting queue.
>
> The underwriter then reviews the risk and supporting documents. If information is missing, the request is sent back through the portal and the agent responds. The underwriter obtains or calculates rating and decides whether to quote, refer, decline, or take another action. If the customer accepts a quote, the agent requests binding, underwriting confirms the requirements, and coverage is bound. Enterprise systems then record the policy transaction and store the documents, while Surefyre presents the bound or issued status back to the agent.

## Where the Technical Consultant fits

The Technical Consultant may configure or support:

- application fields and sections
- required-field rules
- conditional questions
- document requirements
- eligibility checks
- queue assignment
- referral routing
- notifications
- rating integrations
- policy transaction mappings
- status updates
- troubleshooting and regression testing
- release and production-readiness documentation

## MRPrice bridge

The insurance content is new, but the implementation pattern is familiar.

At FRBNY, I worked across:

- business requirements
- data validation
- JSON payload mapping
- REST integration
- environment testing
- release coordination
- deployment validation
- production troubleshooting
- runbooks and support documentation

The transferable skill is taking a business process and ensuring that the data, rules, integrations, testing, deployment, and support procedures work together end to end.

## Interview questions this diagram supports

- Walk me through a typical insurance submission.
- What happens before underwriting receives a submission?
- What does the Agent Portal do?
- What does the underwriter do?
- What is the difference between quote, bind, and issue?
- Where would a Technical Consultant contribute?
- How would you test this workflow?
- How would you handle missing information or failed integrations?

## Important caveat

This is a simplified interview model. Exact workflows, system-of-record ownership, underwriting authority, and integration behavior may vary by SPG business unit, insurance program, carrier, and customer configuration.

## Transition to D4

D3 shows the overall lifecycle and the primary quote-to-bind path.

D4 answers the next question:

> How does underwriting decide whether to quote, refer, decline, or request more information?

# Diagram backlog to revisit after the interview

- D2 PlantUML: improve horizontal layout and make it closer to the canonical PNG.
- D3 PlantUML: reduce excessive vertical growth while preserving readable decision paths.
- Review D1–D8 PlantUML as a set for consistent spacing, colors, fonts, legends, and print layout.
- Consider C4-PlantUML, Graphviz layout controls, or draw.io for diagrams where PlantUML auto-layout remains limiting.
