---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 11b - interview prep with Jenna
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-09-02
description:
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---
---

Absolutely. Below is the **Jenna/Fidelity interview Q&A review table** from the mock we just completed. I’m keeping the answers close to **your actual examples and wording**, rather than turning them into generic interview answers. The goal is to remember the **story and sequence**, not memorize sentences.

## Fidelity Interview — Jenna Q&A Review

| #      | Likely Question                                                                         | Your Answer / Key Points                                                                                                                                                                                                                                                                                                                                                       | Mental Trigger                                                         |
| ------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **0**  | **Tell me about yourself.**                                                             | I'm a Senior Business Analyst with a financial-services background. Most recently at the New York Fed, I supported a streaming fixed-income market-data application and its modernization from an Oracle-based environment to AWS and APIs.                                                                                                                                    | **Senior BA → financial services → Fed → market data → modernization** |
| **1**  | **Tell me about the application you supported at the Fed.**                             | Streaming fixed-income market-data application. Consolidated pricing from multiple sources and distributed it in real time to downstream consumers such as FedTrade and analytics applications.                                                                                                                                                                                | **Sources → consolidate → downstream**                                 |
| **2**  | **What specifically were your BA responsibilities?**                                    | Requirements analysis; relational pricing schema → JSON payload mapping; Pre-QA testing; UAT coordination; QA/Production release deployments; worked closely with Development, Infrastructure and Operations.                                                                                                                                                                  | **Requirements → data → test → release**                               |
| **3**  | **Walk me through relational-schema-to-JSON mapping.**                                  | Legacy consumers received pricing through Oracle; cloud consumers received it through REST APIs. For each consolidated pricing field, understand lineage back to vendor source and transformations, then determine corresponding JSON field. Worked with developers and consumers to agree on required reference/pricing fields.                                               | **Vendor → transformation → Oracle → JSON → consumer**                 |
| **4**  | **How did you validate the API against the legacy database?**                           | Took consolidated pricing snapshots at four specific times daily. Exported Oracle results to CSV and compared them with API JSON responses. QA tool automated field comparison; manual investigation handled discrepancies and possible timing/network effects.                                                                                                                | **Same time → CSV vs JSON → reconcile**                                |
| **5**  | **What if Oracle and API values don't match?**                                          | First determine whether it's a true pricing mismatch or timing issue. Compare values/timestamps, inspect logs/data, then involve Dev/Ops as needed. Example: database insertion timing could differ from API response timing.                                                                                                                                                  | **Real mismatch or timing?**                                           |
| **6**  | **How would you use lineage to locate a genuine discrepancy?**                          | Trace backward from consolidated field → normalized value → authoritative raw vendor source such as Bloomberg/Reuters/Tradeweb. Use data-load logs and SQL to find the first point where values diverge. Some maturity-date-dependent calculations/behaviors turned out to require code fixes.                                                                                 | **Consolidated → normalized → raw**                                    |
| **7**  | **Once you identify the problem, what do you do?**                                      | Update existing Jira ticket or create one. Document expected vs actual behavior, data/log/SQL findings and Dev discussions. Make acceptance criteria clear, put it into development workflow, and track through Kanban/standup → Dev → QA → release.                                                                                                                           | **Evidence → Jira → AC → Dev → QA**                                    |
| **8**  | **How do you determine acceptance criteria?**                                           | Derive them from required business/system behavior. Example: vendor retires/replaces price fields; criteria verify new MID is ingested/consolidated/distributed, correct BID is used, and EOD reporting is correct. Start high-level and refine with Dev, QA and consumers.                                                                                                    | **Expected behavior → AC → testing**                                   |
| **9**  | **When is a story ready for development?**                                              | Collaborative decision with PO and squad. Doesn't need to be perfect, but team needs enough understanding of business behavior, acceptance criteria, important data, dependencies and major unanswered questions. Refine collaboratively rather than waiting for a perfect specification.                                                                                      | **Enough to start, not perfect**                                       |
| **10** | **What if Dev discovers a dependency after starting?**                                  | Understand dependency and impact on requirement/AC. Work with Dev/SMEs; determine whether existing story changes, another story is needed, or sequencing changes. Update Jira and make dependency visible.                                                                                                                                                                     | **Impact → dependency → story/sequencing**                             |
| **11** | **Why is hands-on system access important for a BA?**                                   | Don't rely only on Jira/meetings. For UI: know/use application. Backend: database access, SQL, logs, reports, APIs and realistic test/UAT data. Allows BA to investigate and validate requirements independently and uncover dependencies earlier.                                                                                                                             | **UI → use it; DB → query it; logs → inspect**                         |
| **12** | **Give me a specific example of unclear requirements.**                                 | Consumers wanted Bloomberg's MID instead of internally derived MID. Assumption: Bloomberg MID would always be populated. Validation showed it sometimes wasn't, causing entire pricing record to fail. Requirement changed: use Bloomberg MID when available; otherwise derive MID from BID/ASK and identify source as `BB/CBBT` or `Derived`.                                 | **Request → assumption → gap → fallback → attribution**                |
| **13** | **How did you discover the missing MID problem?**                                       | Business reported entire price for a CUSIP missing from final distributed copy. Traced security backward through normalization to raw vendor feed. Logs/raw pricing tables showed Bloomberg MID was empty despite subscription to that field.                                                                                                                                  | **Business symptom → backward lineage → root cause**                   |
| **14** | **How would you begin analyzing a legacy system that still requires 3-char Rep Codes?** | Recognize legacy compatibility requirement, but don't jump immediately to solution. Identify systems/interfaces, where 4-char originates, storage, validation, transmission, transformations and downstream dependencies. Then determine whether centralized 4→3 mapping solves requirement.                                                                                   | **Discover first → solution second**                                   |
| **15** | **How do you analyze each system/interface for Rep Code impact?**                       | Determine whether it: receives 3/4 chars; stores; validates; transmits; transforms; has business logic dependent on Rep Code; merely passes through; who depends on its output; where authoritative source originates; whether historical meaning must be retained.                                                                                                            | **Receive → Store → Validate → Transform → Output**                    |
| **16** | **What do you mean by preserving historical meaning?**                                  | Determine whether the system needs to preserve the Rep Code **and its business meaning as of the transaction date**. Ask whether mappings/relationships can change, whether they're effective-dated, and whether historical reporting/audit/reconciliation must reproduce what code meant when transaction occurred.                                                           | **Meaning at transaction time**                                        |
| **17** | **Mapping says `ABC1→XYZ`, but SME says just truncate to `ABC`. What do you do?**       | Verify actual current behavior with data, logs, configuration/code with Dev and test examples. Test collision risk: `ABC1→ABC`, `ABC2→ABC`. Bring evidence to SME/PO/Dev, reconcile against authoritative mapping, agree intended behavior, document rule and exceptions.                                                                                                      | **Evidence before assumption**                                         |
| **18** | **What's wrong with simply truncating `ABC1` and `ABC2`?**                              | Both become `ABC`, creating a collision/ambiguity and destroying the distinction between two business identities. Don't silently truncate when controlled mapping is required.                                                                                                                                                                                                 | **ABC1 + ABC2 → ABC = identity lost**                                  |
| **19** | **What if `ABC1` has no legacy mapping?**                                               | First determine whether missing mapping is expected/valid or an error. If downstream supports 4 chars, perhaps continue. If legacy requires 3 chars, business must define reject/hold/queue behavior, ownership of resolution, retry/reprocessing and alerting. Never silently substitute/truncate.                                                                            | **Missing mapping ≠ automatically error**                              |
| **20** | **Order has `ABC1`, account has `ABC2`; both are valid. Which is correct?**             | Don't assume either. Trace where each originated and establish SOR/authoritative source for this business use. Determine whether Rep Code relationships/mappings are effective-dated. Both may be valid but applicable at different times. Compare against transaction timestamp and applicable business rule.                                                                 | **SOR + effective date + transaction time**                            |
| **21** | **How do you explain six-system impact to a nontechnical PO?**                          | Don't dump technical checklist. Explain that this isn't simply switching 3→4 chars on one date. Legacy compatibility must remain until dependent workflows can support new codes. Identify affected trading/supervisory/operational workflows and sequence changes in phases.                                                                                                  | **Business impact → dependencies → phases**                            |
| **22** | **How would you help prioritize Release 1?**                                            | Start with systems/interfaces where business logic actually depends on Rep Code. Then assess critical workflow, dependencies, systems unable to accept 4 chars, and downstream impacts. Give PO/squad evidence to determine minimum safe Release-1 scope while maintaining compatibility elsewhere.                                                                            | **Business logic → criticality → dependencies → safe boundary**        |
| **23** | **Business and technical teams understand a requirement differently. Example?**         | Oracle→REST migration. Consumers knew legacy relational/view representation; developers were creating JSON/API representation. You traced fields/lineage, mapped them, worked with consumers and Dev to agree required fields/business meaning, then validated Oracle vs API data.                                                                                             | **Two perspectives → mapping → evidence → agreement**                  |
| **24** | **Dev says API works as designed; consumer says it's not what they need.**              | Example `CALLABLE_DATE`: legacy SQL View performed consumer-specific transformation—NULL → blank string; otherwise `YYYYMMDD`. Consumer initially expected API to reproduce it. Ultimately agreed API supplies native/source value and consumer owns required formatting/transformation. Make responsibility/API contract explicit.                                            | **Where does transformation belong?**                                  |
| **25** | **How do you identify all downstream consumers?**                                       | Put end-to-end flow on paper using sequence/swimlane diagram showing systems, interfaces, actors and dependencies. Use diagram with SMEs/Dev to validate understanding. Follow each system's output to its next consumer. Continuously update diagram during discovery.                                                                                                        | **Diagram = discovery tool**                                           |
| **26** | **What if SMEs don't know every downstream consumer?**                                  | Investigate technical evidence: logs for connections/data transmission, interface/configuration/endpoint information, SQL where tables/views/metadata expose dependencies. Take findings back to SMEs/Dev to validate whether consumers are active and affected.                                                                                                               | **People + logs + config + SQL**                                       |
| **27** | **SME says application is decommissioned, but logs show connections.**                  | Don't assume either is correct. Verify logs are current and identify connection source. Could be remaining interface/batch/component. Work with Dev/Ops to identify it; return evidence to SME. Keep it as potential dependency until discrepancy resolved.                                                                                                                    | **Conflicting evidence → investigate → reconcile**                     |
| **28** | **Critical production issue interrupts planned BA work. What do you do?**               | Understand business impact/severity. Engage Ops/Dev for root cause and short-term mitigation. If permanent code fix needed, create/update Jira from incident findings, define behavior/AC, work with PO/SME to prioritize release. Make impact on planned work visible.                                                                                                        | **Impact → mitigate → fix → prioritize**                               |
| **29** | **Why Fidelity / why Rep Code Expansion?**                                              | Very close to work done at Fed: data analysis, lineage, downstream impact and complex systems. Fed experience traced vendor data through normalization/consolidation to consumers; modernization included relational→REST JSON mapping and validation. Rep Code isn't simply 3→4 chars—it requires lineage, dependencies, validation, business rules and legacy compatibility. | **This resembles work I already enjoy doing**                          |
| **30** | **What questions do you have for Jenna?**                                               | Ask about current-state documentation/discovery; target timeline; phased rollout/legacy compatibility; what trading-focused BA should accomplish in first 90 days.                                                                                                                                                                                                             | **Current state → timeline → 90 days**                                 |

## The Rep Code checklist to remember

You came up with this yourself during the mock, and I think it's one of the most useful things to review before the interview:

|For every system/interface, ask…|Why|
|---|---|
|**1. Receive?**|Does it receive 3-char, 4-char, or both?|
|**2. Store?**|Can its data model actually hold 4 characters?|
|**3. Validate?**|Does existing validation assume 3 characters?|
|**4. Transmit?**|What does it send downstream?|
|**5. Transform?**|Does it translate/change Rep Code?|
|**6. Business logic?**|Does system behavior depend on Rep Code?|
|**7. Pass-through?**|Is it merely carrying the value?|
|**8. Who depends on its output?**|Continue forward lineage; don't stop at the first consumer.|
|**9. Authoritative source?**|Where does the Rep Code originate / what is the SOR?|
|**10. Historical meaning?**|**Does the system need to preserve the Rep Code and its business meaning as of the transaction date?**|

That last question is the exact one you asked me to preserve.

## Your strongest real Fed stories

You don't need 30 separate stories. Most of the interview can be handled with about **five real examples**:

|Story|What it proves|
|---|---|
|**Oracle relational → REST/JSON migration**|Mapping, lineage, modernization, API, stakeholder alignment|
|**Oracle CSV vs API JSON snapshot reconciliation**|Data analysis, testing, validation, troubleshooting|
|**Missing Bloomberg MID / fallback to derived MID**|Ambiguous requirements, discovery, business rules, exceptions, acceptance criteria|
|**CALLABLE_DATE SQL View transformation**|Business vs technical perspective, API contract, transformation ownership|
|**Maturity-dependent pricing defect**|Backward lineage, logs, SQL, root-cause analysis, working with Dev|

This is important: **don't search your memory for a brand-new example every time Jenna changes the wording of a question.**

One good experience can answer several questions from different angles.

For example, the **missing MID story** can answer:

- Tell me about ambiguous requirements.
    
- Tell me about something the business didn't realize it needed.
    
- How do you perform root-cause analysis?
    
- How do you use data lineage?
    
- How do you derive acceptance criteria?
    
- Tell me about working with SMEs/developers.
    
- How do you handle exceptions?
    

## Four concepts I especially want you to retain

**1. Acceptance criteria aren't merely a test list.**

> Define the expected business/system behavior as acceptance criteria; those criteria then become the basis for testing.

**2. Ready and Done are different.**

> **Ready:** Do we understand enough to start?  
> **Done:** Have we satisfied what we agreed to deliver?

**3. Don't trust assumptions when evidence is available.**

> SME knowledge + actual data + logs + SQL + system behavior → reconcile → document decision.

**4. Don't approach Rep Code Expansion as `CHAR(3) → CHAR(4)`.**

Think:

> **Business identity → SOR → lineage → storage → validation → business logic → interfaces → downstream consumers → legacy translation → exceptions → historical meaning.**

That's the conceptual center of your Fidelity preparation.

## Questions for Jenna

I'd have these available, but probably ask only **2–3 depending on time**:

> **1. How well documented is the current-state Rep Code process today? Are there existing end-to-end architecture, data-flow or lineage diagrams, or will part of the BA's role be discovering and documenting that current state?**
> 
> **2. What's the current target timeline for enabling four-character Rep Codes across the enterprise?**
> 
> **3. Is the implementation expected to be phased across different systems or business areas, with legacy three-character compatibility maintained during the transition?**
> 
> **4. What would you expect the trading-focused BA to accomplish in the first 90 days?**

I'd prioritize **#1 and #4**. If her answer to #2 already explains the phased rollout, don't ask #3 just because it's on the list.

At this point, I would **not add much more material**. The next useful exercise is to turn this big table into a **one-page Thursday interview cheat sheet**—something you can scan in 5–10 minutes rather than rereading 30 Q&As.