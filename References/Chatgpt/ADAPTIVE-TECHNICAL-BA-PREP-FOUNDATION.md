# Adaptive Financial Consulting — Technical Business Analyst Prep Foundation

Prepared for Paul Lyu  
Date: August 27, 2026

## 1. The short answer: what are capital markets?

Capital markets are the part of finance where organizations and investors raise, buy, sell, price, and manage longer-term financial instruments such as stocks, bonds, and derivatives.

In practical system terms, capital markets are the people, rules, venues, data, and technology involved in:

1. deciding what to buy or sell;
2. obtaining or publishing prices;
3. entering and validating orders;
4. routing orders to a dealer, exchange, or other venue;
5. matching or executing orders;
6. creating the resulting trade records;
7. clearing obligations and managing counterparty risk;
8. settling cash and securities; and
9. reporting, reconciling, supervising, and auditing the activity.

This is not a new domain for Paul. The unfamiliar part of Adaptive is the depth of its distributed-systems technology, not the basic business domain.

### Capital markets versus banking

| Area | Primary purpose | Simple example |
|---|---|---|
| Retail/commercial banking | Deposits, loans, payments, and customer accounts | A bank makes a mortgage |
| Capital markets | Issuance and trading of securities and derivatives | A corporation issues bonds; investors trade them |
| Asset/investment management | Invest portfolios on behalf of clients or funds | A fund manager buys Treasury securities |
| Market infrastructure | Connect, execute, clear, settle, and report transactions | An exchange matches orders; a clearinghouse manages obligations |

## 2. Yes—Farm Credit was capital-markets work

The Farm Credit BA exercise centered on Epic E6, **Issue and Settle Security**. That was a debt-capital-markets lifecycle:

- a funding need led to a proposed debt transaction;
- a security was structured and issued;
- dealers submitted orders;
- the issuer allocated the security;
- orders were executed;
- settlement instructions were produced;
- exceptions were resolved; and
- post-trade reports and controls were completed.

The package modeled five features, 25 stories, acceptance criteria, business rules, reviews, traceability, and end-to-end diagrams. That is directly relevant to Adaptive because Adaptive builds the systems on which similar workflows run.

### What each prior project contributed

| Experience | Capital-markets connection | Relevance to Adaptive |
|---|---|---|
| Farm Credit debt platform | Issuance, dealer orders, allocation, execution, settlement, exceptions, reporting | Business lifecycle and requirements modeling |
| Fidelity rep-code preparation | Pre-trade identity, OMS behavior, data lineage, legacy translation, clearing and settlement impacts | Trading workflow, system dependencies, controls, and traceability |
| Federal Reserve/Gresham | Streaming fixed-income pricing, cleansing, distribution, downstream consumers, production support | Real-time market data, operational resilience, and technical BA work |
| Capgemini/Fidelity | Ratings, reference data, pricing, time series, security master, golden-copy management | Data foundations used by trading, portfolio, risk, and regulatory systems |

## 3. Where Adaptive operates in the trade lifecycle

Adaptive builds custom front-office and market-infrastructure technology. Its published offerings include matching engines, liquidity distribution and streaming, trading user interfaces, RFQ workflow engines, single-dealer platforms, order management systems, execution management workflows and algorithms, pre-trade risk checks, internalization engines, smart order routers, pricing and market-making tools, and FIX gateways.

Source: [Adaptive — What We Build](https://weareadaptive.com/what-we-build/)

### Simplified lifecycle

| Stage | Business action | Typical systems | Key BA concerns |
|---|---|---|---|
| Market data and pricing | Participants see bids, offers, trades, reference data, and liquidity | Feed handlers, pricing engines, market-data platforms | Timeliness, completeness, sequence, stale data, entitlements |
| Pre-trade | Order is created and checked | Trading UI, OMS, pre-trade risk, credit check | Required fields, limits, identity, validation, rejection reasons |
| Routing | Order is sent to a venue or dealer | SOR, FIX gateway, RFQ engine | Venue rules, routing logic, acknowledgements, timeouts |
| Execution | Buy and sell interest is matched or a quote is accepted | Matching engine, execution engine | Price-time priority, partial fills, cancellations, deterministic results |
| Trade capture | Execution becomes an official trade record | Trade capture, booking, event stream | Unique IDs, lineage, state transitions, duplicate prevention |
| Clearing | Obligations are calculated and risk is managed | Clearing and risk platform | Netting, positions, collateral, counterparty exposure |
| Settlement | Cash and securities move | Settlement platform, custodian interfaces | Instructions, status, fails, cutoffs, reconciliation |
| Operations/reporting | Activity is supervised, reconciled, and audited | Operations UI, reports, surveillance, regulatory feeds | Exceptions, audit trail, recovery, historical reconstruction |

## 4. Adaptive’s business model and expertise

Adaptive is not primarily selling a fixed off-the-shelf application. It combines:

- capital-markets domain consulting;
- product and workflow design;
- software engineering;
- high-performance distributed-systems expertise;
- cloud and infrastructure modernization;
- delivery, QA, SRE, and production support; and
- reusable technology accelerators that clients can customize.

Its phrase **buy and build** means a client starts with tested foundational components and then builds proprietary workflows and business logic on top. This is intended to deliver faster than a complete greenfield build without forcing the client into an inflexible vendor product.

The Aeron Exchange Accelerator, for example, supplies building blocks for matching, risk management, reference data, market data, and FIX-based order entry while allowing customization and different deployment models: cloud, hybrid, or on-premises.

Source: [Aeron Exchange Accelerator](https://weareadaptive.com/aeron-exchange-accelerator/)

## 5. The technology foundation

### 5.1 Low latency versus high throughput

- **Latency** is how long one message or operation takes from input to result.
- **Throughput** is how many messages or operations the system can process in a period.
- **Predictable latency** means response times remain consistent, especially under load; avoiding rare but severe pauses matters in trading.

A trading platform may need all three: low latency, high throughput, and predictable performance. During volatile markets, message volume rises precisely when timely and correct processing matters most.

### 5.2 Why message ordering matters

Suppose these commands arrive:

1. submit order for 1,000 units;
2. reduce order to 400;
3. cancel remaining order.

If services process them in a different order, they can produce a wrong open quantity or an invalid execution. Ordering is therefore a business requirement, not merely an engineering concern.

A Technical BA should ask:

- What ordering guarantee applies: per client, per order, per instrument, or global?
- What sequence number or identifier detects gaps and duplicates?
- What happens when a message is late, repeated, missing, or received after recovery?
- Can the platform replay the exact event sequence?
- Which state is authoritative after failover?

### 5.3 Aeron in plain English

Aeron is open-source infrastructure designed for efficient messaging and resilient distributed systems.

| Component | Plain-English purpose | Trading analogy |
|---|---|---|
| Aeron Transport | Moves messages efficiently using UDP unicast, multicast, or inter-process communication | The fast, reliable delivery channel |
| Aeron Archive | Records message streams and supports replay | The recoverable event history |
| Aeron Cluster | Orders commands, replicates processing, and supports highly available services | Multiple synchronized engines able to survive a failure |
| Aeron Sequencer | Provides ordered, auditable event processing across components | The traffic controller that establishes an authoritative order |

Official Aeron documentation describes Transport as efficient reliable message transport, Archive as persistent recording and replay, and Cluster as providing fault-tolerant total ordering across streams.

Source: [Aeron documentation](https://aeron.io/docs/)

### 5.4 Replicated state machine

A state machine is a service whose current state changes in response to commands or events. An order, for example, may move through states such as New, Acknowledged, Partially Filled, Filled, Cancelled, or Rejected.

A **replicated state machine** runs equivalent copies on multiple nodes:

1. all nodes agree on one ordered log of commands;
2. every node processes the same commands in the same order;
3. the processing must be deterministic; and
4. the nodes therefore arrive at the same state.

If the leader fails, another synchronized node can continue. Aeron Cluster uses Raft consensus to establish the committed order of commands.

Sources: [Aeron replicated state machines](https://aeron.io/docs/distributed-systems-basics/replicated-state-machines/) and [Aeron Raft consensus](https://aeron.io/docs/cluster-quickstart/raft-consensus/)

### 5.5 Determinism

Deterministic processing means the same initial state plus the same ordered inputs always produces the same result. A replicated engine must avoid uncontrolled differences such as each node independently using its local clock or a random value.

For a BA, determinism affects requirements and acceptance criteria:

- Is event time supplied in the command or generated locally?
- Are rounding and price calculations precisely defined?
- Are reference-data versions fixed for the transaction?
- Does replay reproduce the same state and outputs?

### 5.6 Fault tolerance, high availability, and recovery

These terms overlap but are not identical:

| Term | Meaning |
|---|---|
| Resilience | The system continues or recovers acceptably when components fail or conditions degrade |
| High availability | The service remains accessible for the required proportion of time |
| Fault tolerance | The system continues operating despite specified failures |
| Recovery | State and service are restored after interruption |
| Replay | Recorded events are processed again to reconstruct state or resend outputs |
| Auditability | The organization can explain what happened, in what order, and why |

Paul’s DR failover work already provides a strong foundation here: business continuity, data integrity, operational readiness, failover validation, runbooks, and downstream verification.

## 6. Is this “hard-core cloud trading”?

Yes, but **cloud** and **low latency** are separate architectural dimensions.

Some trading functions are extremely latency-sensitive and may need specialized placement, networking, hardware, or on-premises/co-located deployment. Other functions—portals, reporting, risk services, data processing, clearing, reconciliation, and operational tooling—may benefit substantially from cloud scalability and managed infrastructure.

Adaptive explicitly supports cloud, hybrid, and on-premises deployments. The design question is not “cloud or no cloud?” It is:

> Which business capabilities have which latency, throughput, availability, security, recovery, data-sovereignty, and cost requirements, and where should each capability run?

### Example: EDX Clearing

Adaptive built an AWS-based institutional clearing and settlement platform for EDX. The work included an end-to-end clearing solution, risk and book-management functions, reconciliation, reporting, administrative tools, third-party integration, delivery management, and SRE. This was cloud-native capital-markets technology, but it was post-trade clearing rather than only an ultra-low-latency matching engine.

Source: [Adaptive EDX clearing case study](https://weareadaptive.com/trading-resources/client-stories/edx-markets-cloud-native-crypto-trading-adaptive/)

## 7. Domain-Driven Design for a Technical BA

Domain-Driven Design, or DDD, means structuring software and conversations around the business domain and a precise shared language.

The BA does not need to be the software architect. The BA should help establish:

- **Ubiquitous language:** terms mean the same thing to traders, operations, product, QA, and engineers.
- **Entities:** objects with continuing identity, such as Order, Trade, Account, Instrument, or Counterparty.
- **Value objects:** descriptive values without independent identity, such as Price, Quantity, Currency, or DateRange.
- **Aggregates and invariants:** consistency boundaries and rules that must always remain true.
- **Domain events:** business facts that occurred, such as OrderAccepted, TradeExecuted, or SettlementFailed.
- **Bounded contexts:** areas in which a model and vocabulary apply, such as Order Management, Execution, Risk, Clearing, or Settlement.

Example: an **order** and a **trade** are not interchangeable. An order expresses intent; an execution is a fill; a trade is the resulting transaction record. Preserving those distinctions prevents bad requirements and bad interfaces.

## 8. What the Adaptive Technical BA is likely expected to do

Based on the current NYC posting, the BA is expected to bridge product vision and detailed engineering delivery by:

- defining functional and non-functional requirements;
- describing operational scenarios, failure cases, and distributed workflows;
- writing backlog items, stories, acceptance criteria, and testable outcomes;
- participating in architecture and design discussions;
- producing process flows and sequence diagrams;
- working with engineering and QA throughout implementation;
- separating bugs from enhancements and new requirements;
- supporting releases and verifying that delivered behavior satisfies business and operational expectations; and
- bringing structure to ambiguous technical problems.

This is not a note-taking BA. It is a delivery BA who understands system behavior deeply enough to challenge assumptions and make requirements testable.

Source: [Adaptive NYC Senior Technical Business Analyst posting](https://www.linkedin.com/jobs/view/senior-technical-business-analyst-fintech-nyc-salary-up-to-200k-depending-on-experience-%2B-benefits-at-adaptive-4438692724)

## 9. How Paul should position his experience

### Core positioning

> I am a Technical Business Analyst who has worked at the intersection of capital-markets data, engineering delivery, QA, release coordination, and production operations. At the Federal Reserve Bank of New York, I supported mission-critical streaming fixed-income pricing across Linux, Oracle, and AWS environments. I translated epics into testable Jira stories and acceptance criteria, analyzed functional and non-functional requirements, validated data transformations and REST payloads, supported releases and DR exercises, and worked across business, architecture, infrastructure, development, QA, and operations.

### What Paul can claim confidently

- Capital-markets and fixed-income data exposure
- Real-time streaming market-data workflows
- Technical requirements and system dependencies
- Functional and non-functional requirements
- Jira stories and acceptance criteria
- Pre-QA, UAT support, troubleshooting, and data validation
- Linux, Oracle, AWS, REST APIs, JSON, logs, and operational tooling
- Release coordination, runbooks, production readiness, and DR
- Legacy-to-cloud modernization
- Process, data-flow, and sequence-diagram thinking

### What Paul should not overclaim

- Direct hands-on Aeron, Kafka, or Hydra implementation
- Designing a matching engine
- Implementing Raft consensus
- Formal DDD leadership
- Ultra-low-latency performance engineering

### Honest bridge for the technology gap

> I have not implemented Aeron or Raft directly. My adjacent experience is supporting real-time streaming market-data platforms where ordering, data integrity, downstream consistency, availability, failover, and operational recovery mattered. I understand why those concerns become explicit design requirements in a clustered trading platform, and I am building deeper familiarity with Aeron’s Transport, Archive, Cluster, ordering, replay, and replicated-state-machine concepts.

## 10. Fit and risk assessment

| Area | Fit | Assessment |
|---|---|---|
| Capital-markets domain | Strong | Federal Reserve, Fidelity, fixed income, pricing, reference data |
| Technical BA delivery | Strong | Requirements, stories, acceptance criteria, QA, release support |
| Market data and real-time systems | Strong adjacent | Streaming pricing and downstream distribution |
| Production resilience | Strong | DR, runbooks, production readiness, data integrity |
| Cloud modernization | Strong adjacent | Oracle-to-REST and AWS transition validation |
| Process and sequence modeling | Strong | Farm Credit and Fidelity preparation plus BA experience |
| Aeron/Kafka/Hydra | Gap | No direct implementation stated |
| Replicated state machines/Raft | Learning gap | Must explain conceptually, not claim engineering experience |
| DDD | Learning/terminology gap | Existing domain modeling maps naturally to it |
| Matching engines/exchange internals | Learning gap | Needs order-book and execution-state study |

Overall, this is a credible stretch role. The main question is whether Adaptive treats direct Aeron/Kafka/Hydra experience as mandatory or accepts strong equivalent real-time financial messaging experience.

## 11. Preparation curriculum

### Session 1 — Capital Markets Reconnection

- Buy side, sell side, issuers, investors, dealers, venues, clearinghouses, and custodians
- Asset classes: equities, fixed income, FX, commodities, derivatives, and digital assets
- Order-to-trade-to-settlement lifecycle
- Reconnect Farm Credit, Fidelity, and Federal Reserve experience

### Session 2 — Front-Office Trading Systems

- Market data, OMS, EMS, SOR, RFQ, FIX gateway, matching engine
- Orders, quotes, executions, fills, and trades
- Order states, time-in-force, partial fills, cancel/replace, and rejection

### Session 3 — Non-Functional Requirements

- Latency, throughput, scalability, availability, resilience, and recovery
- Measurable requirements rather than adjectives such as “fast” or “reliable”
- Failure scenarios and operational acceptance criteria

### Session 4 — Messaging and Event-Driven Systems

- Producers, consumers, messages, commands, events, topics/streams, and schemas
- Ordering, duplication, gaps, idempotency, replay, and back pressure
- Slow consumers and downstream recovery

### Session 5 — Aeron Foundation

- Transport, Archive, Cluster, and Sequencer
- Raft, leader election, replicated logs, deterministic state machines
- Aeron versus Kafka at the conceptual level

### Session 6 — Cloud Trading Architecture

- Cloud, hybrid, on-premises, and co-location tradeoffs
- Stateless versus stateful services
- Scaling, observability, deployment, failover, and data persistence
- AWS clearing-platform case study

### Session 7 — Domain-Driven Design and Workflow Modeling

- Ubiquitous language, entities, value objects, aggregates, events, bounded contexts
- Context mapping across OMS, execution, risk, clearing, and settlement
- Workflow diagrams and sequence diagrams

### Session 8 — Technical BA Delivery Exercise

- Turn a trading scenario into requirements
- Functional and non-functional requirements
- User stories and acceptance criteria
- Failure scenarios, test cases, operational readiness, and release controls

### Session 9 — Adaptive Interview Stories

- Streaming market-data modernization
- Oracle-to-REST data mapping and validation
- Pre-QA and anomaly investigation
- Release coordination and production readiness
- DR failover and resilience
- Ambiguous requirement or cross-team alignment example

### Session 10 — Mock Interview and Gap Defense

- Recruiter screen
- Detailed BA/technical interview
- Architecture-adjacent questioning
- Honest handling of Aeron and DDD gaps

## 12. Questions to ask Manuella when she replies

1. Is this the currently advertised Senior Technical Business Analyst role in New York?
2. Is the position full-time with Adaptive or assigned to a specific client engagement?
3. How strict is the requirement for direct Aeron, Kafka, or Hydra experience versus equivalent real-time financial messaging experience?
4. Which asset class and platform area would the initial project cover—market data, OMS/EMS, exchange, risk, clearing, or settlement?
5. What is the expected New York office schedule?
6. Which parts of the interview focus on capital-markets domain knowledge versus distributed-systems concepts?

## 13. Five concepts to remember first

1. **Capital markets is already part of Paul’s background.** Farm Credit covered debt issuance and settlement; Fidelity covered trading workflows; the Fed covered streaming fixed-income data.
2. **Adaptive builds the machinery of trading.** Its work spans pricing and market data through orders, execution, clearing, and settlement.
3. **Order matters.** In trading, processing the right messages in the wrong sequence can produce the wrong financial state.
4. **Aeron combines fast transport, recording/replay, and clustered ordered processing.** Paul needs conceptual fluency, not false claims of implementation experience.
5. **The BA makes technical behavior testable.** Requirements must cover normal flow, failure flow, performance, recovery, data integrity, auditability, and production operation.

