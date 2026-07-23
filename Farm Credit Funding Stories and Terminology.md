---
categories:
  - "[[Processes]]"
type:
description: Basic debt Terminology and Stories
source: chatgpt-manual
tags:
created: 2026-07-21
last: 2026-07-21
status:
origin:
run_id:
input_prompt:
---
---
Yes. Before writing detailed stories, you need a simple mental model of **what is being issued, who owes whom, when money moves, and what happens after issuance**.

# 1. The basic Farm Credit funding model

Farm Credit associations generally do not obtain their lending money from customer deposits. The four Farm Credit System Banks raise funds primarily by issuing Systemwide debt through the Federal Farm Credit Banks Funding Corporation. The associations then borrow from their affiliated System Bank to make loans to farmers, ranchers, agribusinesses, and rural communities. ([Farm Credit Administration](https://www.fca.gov/bank-oversight/about-banks-and-associations?utm_source=chatgpt.com "About banks & associations"))

```text
Investors
   │
   │ Pay cash to purchase Farm Credit debt
   ▼
Federal Farm Credit Banks Funding Corporation
   │
   │ Coordinates issuance for the four System Banks
   ▼
Four Farm Credit System Banks
   │
   │ Provide wholesale funding
   ▼
Local Farm Credit Associations
   │
   │ Make loans
   ▼
Farmers, ranchers and rural businesses
```

The Funding Corporation is best understood as the **central capital-markets and fiscal agent**. It markets and facilitates the issuance of the securities on behalf of the System Banks. The four Banks are the actual obligors—the entities responsible for repaying the debt.

---

# 2. Does the Federal Reserve pay the Farm Credit Banks?

**Not in the sense of lending Farm Credit the money.**

The Federal Reserve Banks support the **book-entry issuance, transfer, settlement, safekeeping and payment infrastructure** used for these securities. They act as financial-market infrastructure and paying agents, not as the investor funding Farm Credit.

A simplified settlement looks like this:

```text
Investor or Dealer Bank                    Farm Credit side
        │                                        │
        │ Cash payment                           │ Security
        └──────────────────► Fedwire ◄───────────┘
```

Through Fedwire Securities, securities are commonly transferred using **delivery versus payment**, or DVP:

- the buyer receives the security;
    
- the buyer’s bank account is debited;
    
- the seller’s bank account is credited;
    
- both movements occur together;
    
- the transfer is final.
    

The Federal Reserve Banks operate this settlement mechanism. The money ultimately comes from the investor purchasing the security—not from the Federal Reserve acting as a lender to Farm Credit. ([Federal Reserve Financial Services](https://www.frbservices.org/financial-services/securities?utm_source=chatgpt.com "Fedwire Securities Service"))

## At maturity or an interest-payment date

Farm Credit provides the required principal or interest funds through the applicable payment arrangements. The Federal Reserve’s infrastructure helps deliver those payments to the holders of the book-entry securities.

So a safer interview statement is:

> “The Federal Reserve Banks provide book-entry, transfer, settlement and paying-agent infrastructure for Farm Credit securities. They do not ordinarily supply the funding being raised; the investors supply the cash.”

The Farm Credit System Insurance Corporation separately insures the timely payment of principal and interest on insured Systemwide debt if a System Bank cannot make a required payment. ([fcsic.gov](https://www.fcsic.gov/about/FAQs_new/the-basics?utm_source=chatgpt.com "The Basics | Farm Credit System Insurance Corporation"))

---

# 3. Essential debt terminology

## Core terms

|Term|Plain-English meaning|Simple example|
|---|---|---|
|**Debt security**|A tradable promise to repay borrowed money|Farm Credit borrows $1,000 from an investor by issuing a bond|
|**Issuer**|Entity raising money by selling debt|The System Banks issue Systemwide debt through the Funding Corporation|
|**Investor**|Entity providing money by purchasing the debt|Pension fund, bank, money-market fund|
|**Principal / face value / par value**|Amount repaid at maturity|$1,000|
|**Issue date**|Date the security legally comes into existence|August 1|
|**Trade date**|Date buyer and seller agree to the transaction|July 28|
|**Settlement date**|Date cash and the security actually exchange|August 1|
|**Maturity date**|Date the remaining principal must be repaid|August 1, 2031|
|**Term / tenor**|Length of time from issuance to maturity|Five years|
|**Coupon**|Interest rate paid on a bond’s face value|4% per year|
|**Interest-payment date**|Date a coupon payment is due|Every February 1 and August 1|
|**Yield**|Investor’s effective return based on price and cash flows|Depends on coupon, price and maturity|
|**Spread**|Extra yield above a benchmark|SOFR plus 0.40%|
|**Benchmark**|Reference market rate used in pricing|Treasury yield or SOFR|
|**CUSIP**|Identifier assigned to a security|Similar to a unique product ID|
|**Outstanding debt**|Debt issued but not yet repaid, called or matured|Current unpaid securities|
|**Redemption**|Repayment of the security|Normally at maturity or through an early call|
|**Call**|Issuer’s contractual right to repay before maturity|A 10-year bond may be callable after year three|
|**Allocation**|Decision about how much of an offering each purchaser receives|Dealer requested $50M but received $30M|
|**Book entry**|Electronic ownership record; no physical certificate|Ownership recorded in securities accounts|
|**DVP**|Security and payment move simultaneously|Buyer receives bond as cash is transferred|

---

# 4. Major Farm Credit debt products

Farm Credit publicly identifies Discount Notes, Designated Bonds, Floating-Rate Bonds and Fixed-Rate Bonds among its main debt products. ([farmcreditfunding.com](https://www.farmcreditfunding.com/ffcb_live/debtSecurities/floatingRateBonds.html?utm_source=chatgpt.com "Floating Rate Bonds"))

|Product|How investor earns money|Typical purpose or characteristic|Main system complexity|
|---|---|---|---|
|**Discount Note**|Buy below face value; receive face value at maturity|Short-term funding, commonly one year or less|Discount pricing, daily issuance, short maturities|
|**Fixed-Rate Bond**|Receive a fixed coupon and principal at maturity|Predictable long-term interest payments|Coupon schedule, interest accrual, maturity|
|**Floating-Rate Bond**|Coupon resets based on benchmark plus spread|Rate adjusts with market rates|Benchmark retrieval, resets, fallback rules|
|**Designated Bond**|Usually fixed coupon plus principal repayment|Large, liquid, non-callable benchmark-style issue|Large offering, investor distribution, disclosure|
|**Callable Bond**|Coupon until maturity or early call|Issuer can repay early under defined terms|Call schedules, notices, early redemption|

Farm Credit says its Discount Notes are issued daily, sold below par and used to meet Bank needs while considering investor interests and market conditions. Its Designated Bonds are generally at least $1 billion and are intended to be liquid, non-callable securities. ([farmcreditfunding.com](https://www.farmcreditfunding.com/ffcb_live/debtSecurities/discountNotes.html?utm_source=chatgpt.com "Discount Notes"))

---

# 5. How a Discount Note works

Assume Farm Credit issues a note with:

- face value: **$1,000**
    
- purchase price: **$980**
    
- maturity: **six months**
    
- coupon: **none**
    

The investor pays $980 at settlement.

At maturity, the investor receives $1,000.

```text
Settlement                         Maturity
Investor pays $980  ───────────►  Investor receives $1,000
```

The $20 difference is the investor’s return.

A Discount Note generally does not make periodic coupon payments. It is similar in concept to a Treasury bill. ([farmcreditfunding.com](https://www.farmcreditfunding.com/ffcb_live/debtSecurities/discountNotes.html?utm_source=chatgpt.com "Discount Notes"))

---

# 6. How a fixed-rate bond works

Assume:

- face value: **$1,000**
    
- coupon: **5%**
    
- maturity: **five years**
    
- interest paid twice annually
    

The investor receives:

- $25 every six months;
    
- $50 total per year;
    
- $1,000 principal at maturity.
    

```text
Issue              Coupon payments                    Maturity
$1,000 invested → $25 → $25 → $25 ... → $25 → $1,000 principal
```

The bond’s **coupon remains 5%**, but its market price may move after issuance.

---

# 7. Price, coupon, yield and maturity

This is one of the most important concepts.

## Coupon is not the same as yield

The **coupon** is normally fixed when a fixed-rate bond is issued.

The **yield** changes because the price investors are willing to pay changes.

Suppose an existing bond pays 4%, but newly issued similar bonds now pay 5%.

Why would an investor pay full price for the old 4% bond?

Usually, they would not. The old bond’s market price must fall enough to make its return competitive.

```text
Market rates rise  → Existing fixed-rate bond prices generally fall
Market rates fall  → Existing fixed-rate bond prices generally rise
```

## Example

Existing bond:

- face value: $1,000
    
- coupon: 4%
    
- annual interest: $40
    

New similar bonds:

- coupon or market yield: approximately 5%
    

The older bond may trade below $1,000 because its $40 annual payment is less attractive.

Conversely, if current market yields fall to 3%, the old 4% bond becomes attractive and may trade above $1,000.

---

# 8. Why maturity affects rates and prices

Maturity determines how long the investor’s money and interest rate are committed.

## Longer maturity usually means more uncertainty

Over ten years, more things can change:

- inflation;
    
- interest rates;
    
- the economy;
    
- liquidity;
    
- credit conditions;
    
- investor demand.
    

Therefore, longer-term securities frequently offer a different—and often higher—yield than shorter securities. But this is not guaranteed; the yield curve can invert.

## Longer bonds are usually more price-sensitive

Consider two fixed-rate bonds:

- Bond A matures in three months.
    
- Bond B matures in ten years.
    

If market rates rise, Bond A will mature soon and return principal that can be reinvested at the new rate.

Bond B locks the investor into its old coupon for much longer. Its price therefore normally falls more.

```text
Short maturity:
Less time locked into old rate
Usually lower price sensitivity

Long maturity:
More time locked into old rate
Usually higher price sensitivity
```

You do not need to calculate duration for this interview. Understand the principle:

> “The longer the remaining maturity of a fixed-rate bond, the more sensitive its market value generally is to changes in interest rates.”

---

# 9. How floating-rate bonds work

A Floating-Rate Bond does not keep the same coupon throughout its life.

It may pay:

```text
SOFR + 0.40%
```

Suppose SOFR is 4.80%.

The coupon becomes:

```text
4.80% + 0.40% = 5.20%
```

At the next reset date, suppose SOFR falls to 4.10%.

The new coupon becomes:

```text
4.10% + 0.40% = 4.50%
```

Farm Credit says its floating-rate bonds may be linked to SOFR, Treasury bills, Prime or Fed Funds. ([farmcreditfunding.com](https://www.farmcreditfunding.com/ffcb_live/debtSecurities/floatingRateBonds.html?utm_source=chatgpt.com "Floating Rate Bonds"))

For the platform, this creates business requirements around:

- reference-rate source;
    
- determination date;
    
- reset date;
    
- spread;
    
- rounding;
    
- day-count convention;
    
- missing-rate fallback;
    
- approval;
    
- notification;
    
- audit history.
    

That is a rich area for BA stories.

---

# 10. Settlement versus maturity

These terms are easy to confuse.

|Event|What happens|
|---|---|
|**Trade date**|Buyer and seller agree|
|**Settlement date**|Buyer pays and receives the security|
|**Coupon dates**|Investor receives scheduled interest|
|**Reset dates**|Floating-rate coupon is recalculated|
|**Call date**|Issuer may repay early if permitted|
|**Maturity date**|Final principal must be repaid|

Example:

```text
July 28, 2026     August 3, 2026       Every 6 months       August 3, 2031
Trade agreed  →   Settlement       →   Interest paid    →   Maturity
```

Farm Credit publicly lists typical settlement periods of approximately three to five business days for Designated Bonds and five to seven business days for many fixed- and floating-rate bonds, although actual transaction terms govern. ([farmcreditfunding.com](https://www.farmcreditfunding.com/ffcb_live/debtSecurities/overview.html?utm_source=chatgpt.com "Debt Securities"))

---

# 11. How many core users might the platform have?

The exact personas are not publicly confirmed, and a greenfield discovery process would validate them. For interview preparation, I would use **eight core business personas**, plus several external or system actors.

## Eight practical core personas

|Persona|Primary responsibility|
|---|---|
|**System Bank Funding Representative**|Submits or confirms a Bank’s funding and liquidity requirements|
|**Funding Strategy Analyst**|Consolidates Bank needs and helps decide amount, timing, maturity and product mix|
|**Issuance Officer**|Creates offerings, manages terms, pricing and issuance workflow|
|**Issuance Approver / Treasury Manager**|Reviews and approves transactions, pricing and exceptions|
|**Dealer / Dealer Representative**|Receives offerings, submits orders and receives allocations|
|**Settlement Operations Analyst**|Manages book-entry issuance, settlement, reconciliation and failures|
|**Debt Operations Analyst**|Manages coupons, resets, calls, maturities, redemptions and payment events|
|**Disclosure / Investor Relations Analyst**|Publishes disclosures, security information and investor reporting|

## Cross-cutting personas

|Persona|Role|
|---|---|
|**Risk Analyst**|Reviews funding, interest-rate, liquidity and concentration risks|
|**Compliance or Legal Reviewer**|Reviews offering terms, controls and disclosures|
|**Finance / Accounting Analyst**|Reconciles proceeds, interest expense, principal and Bank allocations|
|**Platform Administrator**|Manages entitlements, reference data and configuration|
|**Auditor**|Reviews transactions, approvals and historical changes|
|**Executive / Product Owner**|Monitors performance and prioritizes roadmap capabilities|

## External and system actors

These are not always human users, but they appear in stories and requirements:

- Federal Reserve/Fedwire Securities;
    
- pricing or benchmark data provider;
    
- CUSIP or security-identification service;
    
- dealer systems;
    
- Bank treasury systems;
    
- general ledger;
    
- investor-information website;
    
- document-management system;
    
- notification service;
    
- regulatory reporting systems.
    

For interview purposes, do not try to memorize 15 titles. Start with these five:

1. System Bank Funding Representative
    
2. Funding Strategy Analyst
    
3. Issuance Officer
    
4. Dealer
    
5. Settlement Operations Analyst
    

Then add Debt Operations, Disclosure, Risk and Compliance as the lifecycle expands.

---

# 12. High-level debt-platform backlog

The following can become our master map.

|Epic|Business objective|Primary actor|Supporting actors|Representative stories|High-level acceptance criteria|
|---|---|---|---|---|---|
|**E1. Aggregate Bank Funding Requirements**|Understand how much money the four Banks require and when|Funding Strategy Analyst|System Bank representatives, Treasury Manager, Risk|Submit request; revise request; consolidate requests; identify gaps; approve funding plan|Required fields validated; Bank and date identified; versions retained; late or missing requests flagged; totals reconcile|
|**E2. Plan Funding and Product Mix**|Decide which instruments and maturities should be issued|Funding Strategy Analyst|Risk, Issuance Officer, Finance|Analyze funding gap; compare maturities; recommend Discount Notes versus bonds; approve issuance plan|Plan covers approved requirement; limits checked; assumptions visible; approval recorded; changes audited|
|**E3. Create and Approve Debt Transaction**|Create accurate issuance terms|Issuance Officer|Treasury Manager, Legal, Compliance|Create draft; select product; enter terms; validate terms; submit for approval; approve or reject|Product-specific fields required; invalid dates rejected; status controlled; maker-checker separation enforced; audit record created|
|**E4. Manage Dealer Offering and Orders**|Distribute the security and capture investor demand|Dealer / Issuance Officer|Dealer administrator, Compliance|Open offering; notify dealers; submit order; amend order; cancel order; close offering|Only authorized dealers participate; offering window enforced; order history retained; duplicates handled; late orders flagged|
|**E5. Price and Allocate Offering**|Finalize economics and distribute the issue|Issuance Officer|Treasury Manager, Risk, Dealers|Review demand; set final terms; allocate orders; approve allocation; send notices|Total allocation cannot exceed issue size; only valid orders allocated; approval required; final terms locked; notices produced|
|**E6. Issue and Settle Security**|Exchange securities and cash accurately|Settlement Operations Analyst|Issuance Officer, Fedwire, Dealers, Finance|Create issuance instruction; validate CUSIP; transmit instruction; monitor settlement; resolve failure; reconcile proceeds|Required fields complete; security and payment statuses tracked; failures visible; settlement totals reconcile; messages auditable|
|**E7. Allocate Proceeds to System Banks**|Distribute raised funds according to approved needs|Finance or Funding Operations Analyst|Four Banks, Accounting, Treasury|Calculate allocations; approve allocation; transfer proceeds; reconcile balances; report exceptions|Total Bank allocations equal net proceeds; allocation rules applied; approvals captured; exceptions resolved; ledger entries reconcile|
|**E8. Manage Debt Lifecycle**|Process obligations from issuance through final repayment|Debt Operations Analyst|Finance, Risk, Settlement, Paying Agent|Generate coupon schedule; reset floating rate; process call; process maturity; pay principal and interest|Dates calculated correctly; benchmark and spread recorded; payments approved; called debt removed from outstanding balance; audit retained|
|**E9. Publish Disclosure and Investor Data**|Provide accurate and timely market information|Disclosure Analyst|Investor Relations, Legal, Compliance|Publish offering terms; publish outstanding debt; publish maturity/call activity; issue disclosure; correct publication|Only approved data published; effective date shown; version controlled; corrections traceable; portal matches source records|
|**E10. Monitor Risk, Operations and Market Trends**|Detect issues and guide product decisions|Risk or Product Analyst|Funding Strategy, Operations, Product Owner|Monitor maturity profile; track funding costs; analyze investor demand; identify settlement failures; propose roadmap changes|Metrics derived from controlled data; thresholds configurable; exceptions alert users; drill-down available; recommendation evidence retained|

---

# 13. Epic-to-lifecycle view

|Lifecycle stage|Epics|
|---|---|
|Determine need for money|E1 Aggregate Bank Funding Requirements|
|Decide how to borrow|E2 Plan Funding and Product Mix|
|Define the security|E3 Create and Approve Debt Transaction|
|Offer it to the market|E4 Manage Dealer Offering and Orders|
|Determine price and buyers|E5 Price and Allocate Offering|
|Exchange security for money|E6 Issue and Settle Security|
|Send funds into Farm Credit|E7 Allocate Proceeds to System Banks|
|Pay interest and principal|E8 Manage Debt Lifecycle|
|Inform investors and regulators|E9 Publish Disclosure and Investor Data|
|Improve decisions and platform|E10 Monitor Risk, Operations and Market Trends|

---

# 14. One complete example

## Epic

**E6 — Issue and Settle Security**

## Feature

Generate and monitor book-entry issuance instructions.

## User story

> As a Settlement Operations Analyst, I want the platform to generate a validated issuance instruction for an approved security so that the security can be issued and settled through the applicable book-entry process.

## Acceptance criteria

|ID|Given|When|Then|
|---|---|---|---|
|AC-1|The transaction has final approval|The instruction is generated|It contains CUSIP, principal, settlement date, maturity date and product terms|
|AC-2|A mandatory field is missing|The user attempts transmission|Transmission is blocked and the missing field is identified|
|AC-3|A valid instruction is submitted|A response is received|The platform records accepted, pending or rejected status|
|AC-4|An instruction is rejected|Operations reviews the transaction|The rejection reason and corrective action are visible|
|AC-5|Settlement completes|Reconciliation runs|Security quantity and cash proceeds agree with final allocation|
|AC-6|Any instruction changes|A user saves the change|Previous and current values, user and timestamp are retained|

## Possible UAT scenarios

- normal successful settlement;
    
- missing CUSIP;
    
- invalid settlement date;
    
- duplicate transmission;
    
- partial failure;
    
- rejected instruction;
    
- corrected and retransmitted instruction;
    
- cash amount does not reconcile;
    
- unauthorized user attempts transmission.
    

---

# The interview-level mental model

Remember this sequence:

> **Need money → decide what debt to issue → create terms → collect orders → price and allocate → settle security for cash → distribute proceeds → pay interest → repay principal.**

And remember the Federal Reserve distinction:

> **Investors provide the money. The Federal Reserve Banks provide critical book-entry, payment and settlement infrastructure.**

Your FRBNY experience gives you a credible bridge into this platform because you already understand controlled financial data, downstream consumers, Linux/Oracle and API modernization, testing, operational readiness, production releases and audit-sensitive workflows.

