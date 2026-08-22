---
categories:
  - "[[Clippings]]"
title: Fidelity-Session 1-6 -- Consolidated Q and A
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
author:
published:
created: 2026-08-21
description: The Fidelity JD asks for an “understanding of regulatory environments.” For this role, I want you to understand why a seemingly technical identifier like Rep Code has implications for supervision, books and records, auditability, traceability, testing and controlled change.
tags:
  - clippings
  - fidelity
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a85c8ce-c900-83ea-a3c8-ebc097bd9285
---
# TRD-10 - Pre-Trade Layer 1

---


```puml
@startuml

title TRD-10 — Pre-Trade (Layer 1)

top to bottom direction

skinparam componentStyle rectangle

actor Client

actor "Advisor / Registered Rep" as Advisor

rectangle "Client / Account System" as AccountSys

rectangle "Rep Code System of Record" as RepSOR

rectangle "Order Entry" as OrderEntry

rectangle "Pre-Trade Validation" as Validation

rectangle "Order Management System (OMS)" as OMS

rectangle "Order Routing" as Routing

rectangle "Execution Venue" as Venue

Client -right-> Advisor : Trade instruction\nBuy 100 IBM

RepSOR -right-> AccountSys : Rep Code assignment /\nrelationship data

Advisor -down-> OrderEntry : Account #\nSecurity / Side / Qty\nRep Code

AccountSys -right-> OrderEntry : Account #\nStatus\nRep relationship

OrderEntry -down-> Validation : Order + Account #\nRep Code + Security\nSide + Qty

Validation -left-> RepSOR : Validate Rep Code\n(if required)

Validation -right-> AccountSys : Validate account /\npermissions / status

Validation -down-> OMS : Validated order\nOrder ID + Account #\nRep Code + Security\nSide + Qty

OMS -down-> Routing : Routed order\nOrder ID + Account #\nRep Code? + Security\nSide + Qty

Routing -down-> Venue : Execution request\n(fields depend on interface)

note right of Validation

[[TRD-11-pre-trade-rep-code-lineage.puml Drill down: TRD-11]]

Rep Code Data Lineage

covers Rep SOR + Account +

Order Entry + Validation + OMS

end note

note right of Routing

BA discovery:

Does Rep Code continue,

get transformed,

or get dropped?

end note

@enduml
```


---


# TRD-11 - Pre-Trade Rep Code Data lineage Layer 2

```puml
@startuml

title TRD-11 — Pre-Trade Rep Code Data Lineage (Layer 2)

caption Parent: TRD-10 | Boundary: Rep SOR + Account + Order Entry + Validation + OMS

top to bottom direction

skinparam componentStyle rectangle

rectangle "Rep Code SOR" as SOR

rectangle "Client / Account System" as ACCT

rectangle "Order Entry" as OE

rectangle "Pre-Trade Validation" as VAL

rectangle "OMS" as OMS

rectangle "Next Boundary:\nOrder Routing" as NEXT

SOR -right-> ACCT : authoritative Rep Code\n+ business relationship

ACCT -down-> OE : account_id\nadvisor_rep_code\naccount status

OE -down-> VAL : account_id\nrep_code\nsecurity_id\nside / qty

VAL -left-> SOR : Rep Code lookup / validation\n(if required)

VAL -right-> ACCT : account / Rep relationship\nvalidation

VAL -down-> OMS : order_id\naccount_id\nrep_code\nsecurity_id\nside / qty

OMS -down-> NEXT : flow continues\n(field contract = discovery item)

note right of OE

Example mapping questions:

Account.advisor_rep_code

-> OrderEntry.rep_code

-> OMS.repCd

  

Exact Fidelity field names

are NOT known.

end note

note right of VAL

Impact checks:

field length / UI / validation

business rules / interfaces

transformations

end note

note bottom of NEXT

Forward lineage = downstream impact.

Backward lineage = origin.

  

[[TRD-10-pre-trade.puml Back to parent: TRD-10]]

end note

@enduml
```

---

# TRD-20 - Post-Trade Processing Layer 1

---

```puml
@startuml

title TRD-20 — Post-Trade Processing (Layer 1)

top to bottom direction

skinparam componentStyle rectangle

actor "Trading / Operations User" as OpsUser

actor "Business / Supervisory User" as BizUser

rectangle "Execution Venue" as Venue

rectangle "Order Management System (OMS)" as OMS

rectangle "Trade Processing" as TradeProc

rectangle "Rep Code Translation" as Translation

rectangle "Rep Code System of Record" as RepSOR

rectangle "Clearing" as Clearing

rectangle "Settlement" as Settlement

rectangle "Positions / Books & Records" as Books

rectangle "Supervisory Workflow" as Supervision

rectangle "Reporting" as Reporting

Venue -down-> OMS : Execution(s)\nExecution ID + Order ID\nSecurity / Qty / Price

OMS -down-> TradeProc : Trade details\nOrder ID + Execution ID\nAccount # + Rep Code\nSecurity / Qty / Price

TradeProc -down-> Clearing : Trade obligation data\nAccount #\nRep Code / translated code\nSecurity / Qty / Price

Clearing -down-> Settlement : Cleared obligations\nCash owed\nSecurities owed

Settlement -down-> Books : Settled trade\nAccount # + Security / Qty\nTrade status

TradeProc -left-> Translation : Rep Code\n(e.g. ABC1)

Translation -left-> RepSOR : Resolve / validate\nmapping context

Translation -right-> TradeProc : Legacy / target mapping\n(e.g. ABC1 -> XYZ)

TradeProc -right-> Supervision : Trade + advisor context\nAccount # + Rep Code\nOrder / Trade IDs

TradeProc -right-> Reporting : Trade / activity data\nAccount # + Rep Code\nSecurity / Qty / Price

RepSOR --> Supervision : Authoritative Rep Code meaning

RepSOR --> Reporting : Authoritative Rep Code meaning

OpsUser --> TradeProc : Investigate exceptions /\nreconcile trade

Books -[hidden]left-> BizUser

BizUser -[hidden]up-> RepSOR

BizUser -up-> Supervision : Review / supervise activity

BizUser -up-> Reporting : Consume reports / insights

note left of Translation

Conceptual only:

centralized translation approach;

actual implementation unknown.

  

[[TRD-21-rep-code-translation-legacy-compatibility.puml Drill down: TRD-21]]

end note

note right of Supervision

Candidate only:

TRD-31 Supervision &

Traceability — build only

if visual review says useful.

end note

@enduml
```


---


## TRD-21 - Rep code translation & Legacy Compatibility Layer 2

```puml
@startuml

title TRD-21 — Rep Code Translation & Legacy Compatibility (Layer 2)

caption Parent: TRD-20 | Boundary: OMS + Trade Processing + Translation + Clearing

top to bottom direction

skinparam componentStyle rectangle

rectangle "OMS" as OMS

rectangle "Trade Processing" as TP

rectangle "Centralized Translation\nCapability (conceptual)" as XLATE

database "Rep Code / Mapping\nAuthoritative Data" as MAP

rectangle "Clearing / Legacy-Compatible\nConsumer Boundary" as CLR

rectangle "Exception Behavior\nTBD by Fidelity" as EXC

OMS -down-> TP : order_id / execution_id\naccount_id / rep_code\nsecurity / qty / price

TP -left-> XLATE : new-world Rep Code\nwhen translation is required

XLATE -left-> MAP : resolve mapping /\nauthoritative meaning

MAP -right-> XLATE : mapping result

XLATE -right-> TP : legacy-compatible\nrepresentation

TP -down-> CLR : trade + account\nRep representation\nsecurity / qty / price

XLATE -down-> EXC : no/invalid mapping or\ntranslation unavailable

note right of XLATE

Conceptual example only:

ABC1 <-> XYZ

  

Business-identity mapping,

NOT truncation.

  

Exact implementation and

translation location unknown.

end note

note right of TP

BA checks:

3 vs 4 consumers?

translation direction?

cardinality?

effective dating/history?

ownership/approval?

reconciliation?

end note

note bottom of EXC

Do not invent behavior.

Discover reject / hold / queue /

retry / other requirement.

  

[[TRD-20-post-trade.puml Back to parent: TRD-20]]

end note

@enduml
```

---




|Session|Question / concept|Your resulting answer to retain|
|---|---|---|
|**1 — Brokerage 101**|Client vs. account|**Client** is the customer; one client can have multiple **accounts** at the financial-services firm.|
||Order vs. trade|**Order** expresses intent to buy/sell. Execution of the order creates trade activity.|
||Why Rep Code?|Connects activity to the relevant **registered-rep/advisor/business relationship**, rather than identifying the client.|
||Legacy compatibility|Systems designed around the old Rep Code construct can break when presented with a representation they don't support.|
||Clearing vs. settlement|**Clearing determines obligations — who owes what. Settlement fulfills them — securities and cash actually move.**|
|**2 — Rep Codes**|Employee ID vs. Rep Code|Employee ID identifies someone internally. Rep Code serves a **brokerage business/operational relationship** and can travel through financial workflows.|
||Does Rep Code identify client?|**No.** It relates to the representative/business relationship associated with the client/account/activity.|
||Why does wrong Rep Code matter?|It can break **lineage, attribution and reconciliation** across downstream processes.|
||System of Record|The **authoritative source of truth** for the data.|
||Data lineage|Trace the data from its origin through systems, transformations and consumers.|
|**3 — Trading Lifecycle**|Order → execution|Order represents intent; **execution occurs when some/all of it is filled**.|
||OMS|Receives/manages orders and participates in routing them toward execution.|
||Technical → business impact|Don't stop at “field supports only 3.” Explain what business capability can fail or become incorrect.|
||Starting impact discovery|Understand the **end-to-end As-Is Rep Code lifecycle** with a few connected systems and their inputs/outputs.|
||Important BA discipline|**Finding → business impact → solution/options.** Don't jump directly to an assumed solution.|
|**4 — Data & Lineage**|Source vs. SOR|Trading's immediate source may be OMS while the **Rep SOR remains the authoritative source**.|
||Lineage vs. mapping|**Lineage = path/journey. Mapping = correspondence between source and target fields/values.**|
||DBs both support 4 chars — enough?|**No.** Interfaces, validation, UI, rules, transformations and downstream consumers must also support the required representation.|
||`XYZ` in legacy system → authoritative code|Trace **backward lineage** toward the source/mapping.|
||Finding downstream impact|Trace **forward lineage** from the changed source.|
||`VARCHAR(10)` means system supports 4?|**No. Storage capability alone doesn't establish application/end-to-end capability.**|
|**5 — Rep Code Expansion**|Business problem|Existing Rep Code namespace/construct no longer adequately scales with Fidelity's growth and increasingly complex business structures.|
||Why phased change?|Systems have different owners/releases/dependencies; rollout must be **sequenced** without creating incompatible intermediate states.|
||Why not `ABC1 → ABC`?|Could create a technically valid but **incorrect existing code**, destroying business meaning.|
||Migration vs. coexistence|**Migration = movement toward target state. Coexistence = old/new capabilities operating together during transition.**|
||Missing translation|**Don't invent behavior.** Identify the exception and obtain required behavior from appropriate SMEs/Product/Operations.|
||OMS validation still requires 3|OMS is **not ready**, even if its DB/UI/interfaces support 4.|
||Field test vs. capability test|Accepting `ABC1` proves field support. **End-to-end testing proves the business process remains correct through validation, processing, translation, downstream use and reconciliation.**|
||Gap analysis|Compare **As-Is against To-Be**, then identify storage/UI/rule/interface/mapping/exception/testing/dependency gaps.|
|**6 — Regulatory Environment**|Trade succeeds with wrong Rep Code|Technical success doesn't equal business correctness. Wrong attribution can affect **supervision, reporting, records and traceability**.|
||Lineage and auditability|Lineage helps reconstruct **where data originated, where it traveled and how it transformed**.|
||Historical mappings|Need to understand what the Rep Code/business relationship **meant at transaction time**.|
||Preventive control|**Stops** an error—for example, reject an invalid Rep Code before processing.|
||Detective control|**Detects** an error—for example, reconciliation discovers incorrect translation.|
||BA vs. regulatory SME|SME interprets regulatory/business obligation; **BA translates it into process, data, system behavior, requirements, AC and testing.**|
||Your regulatory positioning|Experienced in **controlled financial environments**, data integrity, traceability, regression/UAT and controlled releases; work with regulatory SMEs rather than claiming regulatory expertise.|

---

### Six-session mental chain

You can now connect everything:

**Client / Account / Advisor**

→ **Rep Code**

→ **Order**

→ **OMS**

→ **Execution**

→ **Trade**

→ **Clearing**

→ **Settlement**

while simultaneously tracing:

**SOR → source → interface → mapping → transformation → downstream consumer**

and analyzing:

**As-Is → To-Be → gaps → requirements → AC → testing → release**

That's the framework we're building.


---





