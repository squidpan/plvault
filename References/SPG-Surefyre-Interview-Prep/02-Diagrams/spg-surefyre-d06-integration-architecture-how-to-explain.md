# D6 — Surefyre Integration Architecture: How to Explain

## Purpose

D6 explains how Surefyre exchanges information with enterprise systems. The emphasis is on understanding **integration responsibilities**, not implementation details.

## Core message

Surefyre is the orchestration layer. It collects business information, invokes downstream systems, receives responses, and presents normalized results back to users.

## Integration responsibilities

### AIM
- Policy and transaction data
- Operational insurance records
- Business transaction status

### ImageRight
- Document storage
- Correspondence
- Workflow references
- Document identifiers

### Carrier / Rating Services
- Rating requests
- Quote responses
- Bind or policy confirmations

### Third-Party Services
- Address validation
- Risk enrichment
- External reference data

### Identity & Access
- Authentication
- Authorization
- API tokens
- SSO

## Technical Consultant responsibilities

Typical work includes:

- configure endpoints
- configure authentication
- map fields
- validate JSON/XML payloads
- test with Postman
- troubleshoot failures
- coordinate with Engineering
- document customer-specific configuration

## 30-second explanation

> Surefyre sits between users and enterprise systems. It sends requests to policy, document, rating and external data services, receives responses, normalizes them, and presents the results through the configured workflow. The Technical Consultant configures those integrations and validates that they work correctly across environments.

## Interview questions

- How does Surefyre integrate with other systems?
- Where would REST APIs be used?
- What would you test with Postman?
- Where would Python help?
- How would you troubleshoot a failed integration?

## Transition to D7

D6 explains **how systems communicate**.

D7 explains **how a brand-new customer implementation is executed from kickoff through production.**
