---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 9C -- One-Page JD-Evidence-Answer Cheat Sheet
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-23
description:
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---
---

# Fidelity — Session 9C: One-Page JD → Evidence → Answer Cheat Sheet

This is the **review version**. The goal isn't to memorize paragraphs. It's to give you a trigger phrase, your strongest evidence, and a concise answer you can expand naturally.

The Fidelity JD describes a trading-focused BA on Rep Code Expansion, with emphasis on technical aptitude, financial/trading context, data lineage/mapping, regulatory awareness, complex dependencies, SQL, APIs/data flows, current-state analysis, discovery, and translating technical findings into business requirements.

Your resume gives us the main evidence base: FRBNY streaming fixed-income market-data modernization across Linux/Oracle/AWS, Oracle→REST/JSON mapping, JIRA stories/acceptance criteria, QA/UAT and release work, plus earlier Fidelity reference/pricing/security-master experience supporting downstream trading and other platforms.

|Fidelity wants|Your strongest evidence|Interview answer / trigger|
|---|---|---|
|**Financial services / trading**|FRBNY fixed-income market data; earlier Fidelity financial/reference/pricing/security-master data supporting downstream trading|“My background is financial data and systems supporting trading rather than direct OMS/trade-execution ownership. Most recently I supported fixed-income market data at the Fed, and earlier I worked at Fidelity with pricing, reference and security-master data distributed downstream to trading and other platforms.”|
|**Technical aptitude / systems analysis**|Linux, Oracle, AWS, OpenShift, REST/JSON, shell scripting, troubleshooting, deployments|“I'm a BA who is comfortable getting into the technology. I work across the application, data, interfaces and infrastructure to understand what is actually happening rather than stopping at the business requirement.”|
|**Regulatory environment**|Fed/Fidelity controlled financial environments; DR, production controls, testing; prior data feeding regulatory/risk platforms|“I'm not a regulatory SME, but I've worked extensively in controlled financial environments. I work with the appropriate SME to understand the regulatory requirement, translate it into system/data impacts and acceptance criteria, and make sure it is validated.”|
|**Data lineage / mapping**|Oracle pricing schema → REST API JSON mapping; downstream data distribution|“I establish where the data originates, what it means, how it is transformed and where it goes. That's directly applicable to tracing a Rep Code from its authoritative source through four-character processing, translation and legacy consumers.”|
|**Complex systems / dependencies**|MRPrice upstream/downstream dependencies; modernization; releases across multiple technology components|“I map the end-to-end flow first, identify affected systems and interfaces, and then work through dependencies with the appropriate SMEs. One component supporting a change doesn't mean the end-to-end workflow supports it.”|
|**Technical → business translation**|Database/API/data analysis + BA stakeholder responsibilities|“I can work with engineering at the database, API, payload or application level and then explain to the business what the finding means, what's affected and what requirement or decision is needed.”|
|**Discovery / independently finding answers**|Cross-functional work with business, technology, infrastructure, architecture and operations|“I don't expect one SME to know the entire workflow. I establish the high-level flow, identify the owners of each component and follow the data and dependencies across teams until I can explain the end-to-end behavior.”|
|**SQL / data analysis**|Oracle relational-data work professionally; hands-on SQL refreshed in PostgreSQL|“I use SQL as a BA analysis and troubleshooting tool—filtering, joining, aggregating and reconciling data. I'm not positioning myself as a database developer.”|
|**APIs / data flows / business logic**|Oracle-based distribution → REST API/JSON modernization|“I worked on mapping relational pricing fields into REST API JSON payloads and validating that the modernized interface preserved the data and business meaning expected downstream.”|
|**Systems of record**|Reference/master data experience; source→consumer data flows|“First I establish which system owns the authoritative value. Then I trace downstream copies and transformations rather than assuming every system containing the value is authoritative.”|
|**Current state / gap analysis**|MRPrice OnPrem/Oracle AS-IS → AWS/REST TO-BE|“I understand the current architecture and workflow, define the target capability and identify the gaps between them. For Rep Code Expansion I'd do that system by system and interface by interface.”|
|**Engineering partnership**|Developers, infrastructure, architecture, QA/UAT, operations|“I've spent years bridging business and engineering—clarifying requirements, working through implementation dependencies, coordinating validation and supporting production readiness.”|
|**Requirements / acceptance criteria**|Epics → JIRA stories with AC; functional/non-functional requirements|“I translate discovery into implementable user stories and measurable acceptance criteria so development knows what to build and QA/business know how to determine whether it's correct.”|
|**Documentation / communication**|JIRA, Confluence, Visio; runbooks, testing, troubleshooting and deployment docs|“The artifact depends on the audience: requirements and AC for delivery, diagrams/data mappings for understanding, test plans for validation and runbooks for operations.”|
|**Data fluency**|Fixed-income pricing, reference data, security master, Oracle, JSON, log analysis|“I want to understand more than a field name: what it represents, its authoritative source, transformations, business rules and downstream dependencies.”|

The underlying resume evidence for these claims is substantial: your Fed role explicitly includes JIRA stories with acceptance criteria, functional/non-functional requirements, Oracle data distribution, log analysis, relational-to-JSON mapping and cloud/API transition validation. Your prior Fidelity work includes fixed-income feeds, reference/pricing/time-series/security-master data and downstream trading, portfolio-management, regulatory and risk consumption.

## Rep Code Expansion — your 30-second understanding

This one **is not claimed work experience**; it is our interpretation of the project description Fidelity supplied.

> “My understanding is that Fidelity's existing three-character Rep Code namespace has become constrained as the business has grown and advisor structures have become more complex. The target state introduces four-character Rep Codes, but the difficult part isn't simply increasing a field from three to four characters. The change has to work across data models, trading, clearing, supervisory and operational systems while maintaining compatibility with legacy systems through a centralized translation approach.”

That's a strong answer because it identifies the **business problem** and then immediately recognizes the **systems problem**.

## If they ask: “How would you approach this project?”

Use this sequence:

**Understand the business meaning of Rep Code**

→ **Identify authoritative source/system of record**

→ **Map AS-IS end-to-end flow**

→ **Inventory systems + interfaces**

→ **Trace forward/backward lineage**

→ **Assess each system for 4-character support**

→ **Identify translation/legacy dependencies**

→ **Perform gap analysis**

→ **Define requirements + AC**

→ **Coordinate engineering/testing**

→ **Validate end-to-end**

And when assessing each system, remember the questions you've already learned:

**Can it store 4?**

**Can it validate 4?**

**Can it transmit and receive 4?**

**Does it transform or truncate the value?**

**What happens when translation fails?**

**What happens to historical records?**

**Can we trace the downstream representation back to the authoritative Rep Code?**

That thinking aligns closely with the JD's emphasis on data lineage, system changes, current-state gaps, APIs/business logic and complex dependencies.

## Your three strongest stories

Don't try to have 15 unrelated examples ready. Most Fidelity questions can come back to three anchors.

**MRPrice modernization** is the main story: Oracle/OnPrem → AWS/REST, relational→JSON mapping, data flows, dependencies, requirements, engineering collaboration, QA/UAT and technical→business translation.

**MRPrice production/release support** covers complex dependencies, troubleshooting, operational risk, release coordination, runbooks, testing, DR and cross-team communication.

**Earlier Fidelity/Asset Control experience** covers Fidelity familiarity plus fixed-income/reference/pricing/security-master data, normalization/consolidation and downstream trading/risk/regulatory consumers.

## Two boundaries to protect

Don't say:

> “I was a trading BA.”

Say:

> **“I've supported financial and market-data systems used by downstream trading environments.”**

And don't say:

> “I'm a regulatory SME.”

Say:

> **“I've worked in controlled financial environments and know how to partner with regulatory SMEs to translate their requirements into system, data and testing requirements.”**

Those distinctions make the rest of your experience more credible, not less.

### Session 9 status

**9A — Trading-focused bullets: COMPLETE**

**9B — Core BA competencies: COMPLETE**

**9C — Consolidated JD cheat sheet: COMPLETE**

So **Session 9 is complete.**

The next major item is **Session 10 — Apex/Fidelity screener preparation**. That's where we stop thinking bullet-by-bullet and practice how this all comes out in an actual conversation: **Tell me about yourself → why this opportunity → Rep Code understanding → technical/SQL/trading questions → gaps → recruiter logistics.**

---

