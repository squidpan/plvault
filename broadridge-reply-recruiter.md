---
categories:
  - "[[Letters]]"
author: []
rating:
topics: []
last:
tags:
  - letter
created:
subject: Joshua Stalsworth's reply
recipients:
type:
---
# Hello

Hi Paul,

Thank you for applying to our Product Analyst role. Before we proceed, could you please provide the following details?

1. What is your **current** work authorization in the United States? Please be **specific**.

2. What is your availability (how soon you could start)

3. What are your salary requirements?

4. Are you able to start in our Newark, NJ, or New York location on day one?  If not, where is your preferred location? (We do not offer relocation for this role)

5. Tell me about your hands-on experience with cash management or money movement workflows — specifically wires, ACH, checks, transfers, or related payment flows. What part of the process did you own?

6. Describe a project where you gathered business requirements from users and translated them for development. How did you handle conflicting requirements, testing/UAT, and delivery through the SDLC?
	
	One specific example was the streaming market data application modernization effort at the Federal Reserve Bank of New York. Existing downstream consumers were receiving manually cleansed fixed-income pricing data through Oracle views. As part of the AWS modernization, the business requirement was that those same consumers should be able to retrieve equivalent pricing data through a REST API without losing required fields or business meaning. 
	
	I worked with business users, consuming business application teams, developers to map Oracle view fields to JSON payload fields, document data rules, and define user stories and acceptance criteria around data parity. 
	
	Testing involved comparing Oracle view extracts against REST API payloads to confirm field-level accuracy. Where conflicts arose, they were often around environment availability, UAT sequencing, and different consumer cutover dates. 
	
	With the Operations Support team, I helped coordinate agreement on testing windows, supported defect triage, and worked with teams to obtain UAT signoff before moving consumers toward AWS production.


## Streaming Market data AWS modernization / Oracle view to REST API distribution


### High level Business Requirements

Existing consumers of cleansed fixed-income pricing data needed to receive the same streaming market data distribution data through a REST API instead of directly querying Oracle views.

### User story 1
As a downstream consuming application, I want to retrieve cleansed fixed-income pricing data through a REST API, so that I can migrate away from direct Oracle view dependency without losing required pricing fields.

### User story 2
As a QA/UAT tester, I want to compare Oracle view extracts against REST API JSON payloads,
so that I can verify field-level data parity before production cutover.

### Conflict-handling example

Multiple consumers needed the same data parity outcome, but they had different testing windows, environment availability, and production cutover dates.

I helped separate the shared requirement — data parity from Oracle to REST — from each consumer’s testing and cutover schedule. I coordinated UAT sequencing across AWS UAT and pre-prod environments, supported field-level validation, tracked defects and exceptions, and helped obtain consumer signoff before production migration.

6. This role requires ramping quickly in a financial services environment with client interaction. Can you give an example of a client-facing or stakeholder-heavy initiative in banking/brokerage where your domain knowledge helped you solve a business problem fast

Best,

Josh

Joshua Stalsworth | Talent Acquisition | Broadridge Financial Solutions, Inc.  
Newark, NJ | USA

[Joshua.stalsworth@broadridge.com](mailto:Joshua.stalsworth@broadridge.com)

609-839-3518