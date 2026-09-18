---
categories:
  - "[[Processes]]"
type:
description: User Stores Interview Prep for Farm Credit  - Farm Credit east
source: chatgpt-manual
tags:
created: 2026-07-21
last: 2026-07-21
status:
origin:
run_id:
input_prompt:
---

I actually think this is a better approach than trying to memorize Agile theory. If they ask you to write a story over the phone, you want to be writing **stories you've essentially lived**, not textbook examples.

Below is the style we've been using in Career System, but adapted to **MR Price**.

---

# Epic 1 - Modernize Market Data Distribution

## Business Goal

Modernize the MR Price application to distribute streaming market data from the legacy platform to AWS-based REST services for downstream consumers.

---

## User Story 1.1 — Validate Price Data Before Release

**As an** Operations Support Analyst

**I want** to validate market price data before each production release

**So that** downstream trading and business applications receive accurate streaming market data.

### Acceptance Criteria

- Pricing data successfully loaded into Oracle.
    
- SQL validation queries complete successfully.
    
- Sample instruments match expected values.
    
- Missing or stale prices are identified.
    
- Business owner approves data quality before release.
    

---

## User Story 1.2 — Verify Deployment Readiness

**As a** Release Coordinator

**I want** deployment readiness validated before Production

**So that** releases are completed with minimal operational risk.

### Acceptance Criteria

- Deployment package approved.
    
- Linux servers available.
    
- Oracle database available.
    
- Required services running.
    
- Release checklist completed.
    
- Infrastructure sign-off received.
    

---

## User Story 1.3 — Validate REST API Output

**As an** Application Support Analyst

**I want** to compare Oracle pricing with AWS REST API responses

**So that** downstream systems receive correct market data.

### Acceptance Criteria

- REST endpoint available.
    
- JSON payload matches Oracle values.
    
- Required fields populated.
    
- No unexpected data differences.
    
- Validation documented.
    

---

# Epic 2 - Improve Production Support

## Business Goal

Improve operational support and reduce production incidents.

---

## User Story 2.1 — Production Health Checks

**As an** Operations Analyst

**I want** automated health checks after deployment

**So that** production issues are identified immediately.

### Acceptance Criteria

- Linux processes running.
    
- Oracle connectivity verified.
    
- Market data flowing.
    
- Health-check scripts complete successfully.
    
- Results documented.
    

---

## User Story 2.2 — Investigate Pricing Issues

**As an** Application Support Analyst

**I want** to analyze production pricing anomalies

**So that** business users receive timely issue resolution.

### Acceptance Criteria

- Production logs collected.
    
- Shell scripts executed.
    
- SQL validation completed.
    
- Root cause identified.
    
- Resolution communicated.
    

---

# Epic 3 - Improve Requirements Quality

## Business Goal

Improve communication between business users and development teams.

---

## User Story 3.1 — Document Business Requirements

**As a** Business Analyst

**I want** business requirements documented as JIRA user stories

**So that** developers clearly understand requested functionality.

### Acceptance Criteria

- Story linked to Epic.
    
- Business objective documented.
    
- Functional requirements complete.
    
- Acceptance criteria defined.
    
- Product Owner approves.
    

---

## User Story 3.2 — Refine Stories During Grooming

**As a** Development Team

**I want** user stories refined before sprint planning

**So that** work can be estimated accurately.

### Acceptance Criteria

- Story reviewed by Product Owner.
    
- Questions resolved.
    
- Dependencies identified.
    
- Acceptance criteria updated.
    
- Story ready for estimation.
    

---

# Epic 4 - Support QA and UAT

## Business Goal

Improve testing quality before Production.

---

## User Story 4.1 — Create Test Cases

**As a** QA Analyst

**I want** test cases created from approved user stories

**So that** requirements are fully validated.

### Acceptance Criteria

- Test cases trace to requirements.
    
- Positive scenarios documented.
    
- Negative scenarios documented.
    
- Expected results defined.
    
- Test cases reviewed.
    

---

## User Story 4.2 — Execute UAT

**As a** Business User

**I want** to validate the delivered functionality

**So that** the solution meets business needs.

### Acceptance Criteria

- Test execution completed.
    
- Defects documented.
    
- Critical defects resolved.
    
- Business approval received.
    
- UAT sign-off completed.
    

---

# If they ask you to write one on the phone...

You can almost write this from memory:

---

**Epic**

Improve Release Readiness

---

**User Story**

> As an Operations Support Analyst,
> 
> I want to validate production readiness before deployment,
> 
> so that streaming market data is delivered accurately to downstream applications.

---

**Acceptance Criteria**

- Deployment package approved.
    
- Environment available.
    
- Database connectivity verified.
    
- Health checks completed.
    
- Sample prices validated.
    
- Business sign-off received.
    

---

This is exactly the level I'd expect from a senior BA in a phone interview.

### One suggestion for interviews

If they ask, "How did you come up with the acceptance criteria?", don't answer, "I just wrote them."

Instead, tie it back to your actual experience:

> "For MR Price, the acceptance criteria came from conversations with the Product Owner, developers, Operations, Infrastructure, and the business users. We identified what had to be true before we could consider the story complete—for example, validating Oracle data, checking Linux services, confirming REST API responses, and obtaining business sign-off. I documented those conditions so QA, developers, and stakeholders all had the same definition of done."

That answer is consistent with your FRBNY work experience, your resume, and the type of BA they're looking for.
