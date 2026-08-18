# D1 — SPG / Surefyre Insurance Ecosystem

## Purpose

Use this diagram to explain the high-level insurance distribution chain and where SPG fits.

The diagram is intentionally simplified. It is not meant to show every legal relationship, system, or insurance transaction. Its purpose is to establish the four principal participants before discussing Surefyre, underwriting workflow, AIM, ImageRight, or technical configuration.

## Core message

A business needs insurance coverage. A retail insurance agent gathers the business and risk information and submits it to a specialty insurance organization such as an SPG business. That SPG business may operate as an MGA, wholesaler, or program administrator. It evaluates or administers the submission within carrier guidelines and authority. The insurance carrier provides capacity and ultimately bears the covered insurance risk.

![[References/SPG-Surefyre-Interview-Prep/02-Diagrams/spg-surefyre-d01-insurance-ecosystem-v2_PNG.png]]



## Participants

### Business Owner or Organization

The insured or prospective policyholder.

Provides:

- business information
- risk and exposure information
- requested coverage
- supporting documents

Receives:

- coverage options
- pricing and terms
- policy documents
- ongoing service

### Retail Insurance Agent or Broker

Works directly with the business seeking coverage.

Responsibilities include:

- understanding the client’s insurance needs
- gathering risk information
- preparing the submission
- presenting quotes and terms
- supporting ongoing policy service

The retail agent is normally an external user of the Surefyre Agent Portal.

### SPG Specialty Business

May operate as an MGA, wholesaler, or program administrator, depending on the program.

Responsibilities may include:

- receiving and evaluating submissions
- applying underwriting guidelines and business rules
- requesting missing information
- quoting or binding within delegated authority
- administering programs and insurance transactions
- coordinating with carriers and agents

Internal underwriters and operations users would typically work through the Surefyre Underwriting Workbench.

### Insurance Carrier

The regulated insurance company that provides insurance capacity and ultimately bears the covered risk.

Responsibilities include:

- defining risk appetite
- setting underwriting guidelines
- granting delegated authority
- providing insurance capacity
- paying valid covered claims
- meeting regulatory and financial obligations

## What the arrows mean

### Primary business and information flow

The forward flow is:

Business owner → Retail agent → SPG specialty business → Insurance carrier

This represents:

- coverage needs and risk information
- application and supporting documents
- approved or administered specialty business

### Response flow

The return flow is:

Insurance carrier → SPG specialty business → Retail agent → Business owner

This represents:

- carrier capacity, guidelines, and authority
- quote, terms, status, and documents
- coverage options, pricing, and service

## 30-second explanation

A business owner works with a retail insurance agent to obtain coverage. The agent gathers the risk information and submits it to an SPG specialty business. Depending on the program, that SPG business may act as an MGA, wholesaler, or program administrator. It evaluates and processes the submission within carrier guidelines and delegated authority. The insurance carrier provides the capacity and ultimately bears the covered insurance risk. Quotes, terms, status, and documents then flow back through SPG and the retail agent to the insured.

## 60-second interview explanation

This diagram shows the simplified insurance ecosystem around Surefyre. The business owner or organization is the insured that needs coverage. A retail insurance agent works directly with that client, gathers the business and risk information, and prepares the submission. The submission is then sent to an SPG specialty business, which may operate as an MGA, wholesaler, or program administrator depending on the program.

The SPG business applies underwriting guidelines and business rules, may request more information, and may quote or bind coverage within delegated authority. The insurance carrier provides capacity, defines risk appetite and guidelines, and ultimately bears the covered insurance risk. The response then comes back through SPG to the agent and insured as a quote, terms, status, and policy-related documents.

Surefyre supports the digital interaction between the external agent and the internal SPG underwriting and operations teams.

## How this leads into D2

Use this transition:

Now that the business participants are clear, the next diagram shows how Surefyre supports their work. The retail agent interacts through the Agent Portal, while SPG underwriters and operations users work through the Underwriting Workbench. Surefyre then connects with downstream systems such as AIM, ImageRight, rating services, and carrier integrations.

## Likely interview questions

### Is the retail agent the MGA?

Usually not. The retail agent works directly with the insured and submits the risk. The MGA operates between agents and carriers and may have delegated underwriting, quoting, or binding authority.

### Does SPG always act as an MGA?

Not necessarily. SPG contains specialty businesses that may perform MGA, wholesale, or program-administration functions. The exact operating model can vary by business unit and insurance program.

### Who is the customer?

The word customer can have several meanings. It may refer to an SPG business unit, underwriting program, MGA, wholesaler, or enterprise insurance organization whose Surefyre instance is being configured. The retail agent is also an important external user of the platform.

### Who is “the business” in an implementation?

The primary business stakeholders are usually underwriting, operations, program management, product, Professional Services, sales, and compliance. Retail agents are critical external users, but the internal stakeholders usually define eligibility, workflow, referral, rating, and operational requirements.

### Who bears the insurance risk?

The insurance carrier ultimately bears the covered insurance risk. An MGA may evaluate, quote, bind, or administer business under delegated authority, but the carrier provides the insurance capacity.

## Terms to remember

- Insured: person or organization protected by the policy
- Retail agent: works directly with the insured and seeks coverage
- MGA: intermediary with delegated authority from a carrier
- Wholesaler: accesses specialty markets for retail agents
- Program administrator: manages a defined insurance program
- Carrier: regulated insurer that provides capacity and bears the risk
- Capacity: financial ability and authority to write insurance
- Delegated authority: authority granted by a carrier to an MGA or other intermediary
- Risk appetite: types and levels of risk a carrier is willing to accept

## Your connection to the role

Your role as Technical Consultant would sit across this ecosystem rather than belonging to only one participant.

You would help translate the needs of underwriting, operations, Professional Services, product, IT, security, and agent users into:

- forms
- JSON schemas
- validation rules
- JavaScript behavior
- workflow and routing
- calculations
- REST or SOAP integrations
- Python migration utilities
- testing and deployment documentation

## MRPrice bridge

A useful comparison is:

In MRPrice, business and operational users depended on a technical platform that received data, applied rules, validated information, distributed results, and supported downstream consumers. In Surefyre, the business domain is insurance rather than streaming market data, but the implementation pattern is similar: understand the users and rules, configure and test the workflow, integrate with other systems, validate production readiness, and support issues after deployment.

## Important caveat

This is a simplified interview model. The exact contractual relationships, systems of record, underwriting authority, and transaction flow can vary by SPG business, carrier, insurance program, and jurisdiction.
