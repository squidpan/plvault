---
categories: "[[Apps]]"
maker: "[[FRBNY]]"
rating:
---
# TL;DR

NPQS distributes consolidated streaming market prices for fixed income assets both in real-time and as snapshot quotes to internal policy makers and Federal Reserve Systems. 

A 24x7 hybrid system, combining on-premises, colocation, and cloud infrastructure, ensures continuous operation, high availability, and workload flexibility.


>[!tldr]
>- 24x7 system that operates on both on-premises and in-cloud data centers.
>- streaming vs realtime vs snapshot finalcial data
>- federal reserve bank of new york Markets Group treasury data consumers
>


> [!Question]
> You mentioned mapping relational pricing schemas to JSON payloads. **Walk me through that. What exactly did you do?**



The streaming market data application distributed consolidated fixed income pricing data to downstream consumers such as FedTrade and analytics applications in real-time - every second.

The application delivered the time-series pricing data to a relational database in the legacy on-premises environment and via APIs in the new cloud based environment. The mandate is clear, in both environments, consumers need access to the same prices for a given set of securities (CUSIPs) whether they are sourced from a relational database or fetched via APIs. this is where the mapping of the legacy relational schema to the API JSON payload becomes critical.

During the mapping, each consolidated database pricing field, we had to understand its lineage back to the source data vendor price field and any transformations along the way in order to decide how to map as a field in the target JSON payload.

---



The market (or exchange) quotes prices (bid/ask) for active securities every second throughout the day. The same pricing data  

In order to process these prices, the application subscribes to receive raw pricing from multiple data vendors by submitting  a shopping list of unique security identifiers (e.g. CUSIP-xyz) and consolidates them and distributes to downstream consumers.

In the legacy oracle based environment, these prices are inserted into an oracle database with a table schema of about 30+ fields. The database schema fields consist of key reference data (securities identifiers dates like issue-date, settlement date, etc) plus the pricing fields( e.g. bid, ask, discount margins and yields). 

---

> [!Q]
> “Tell me about a specific time when you were given a business need, but the detailed requirements weren't clear. How did you figure out what was actually needed?”


Going back to the use case where the consumers want to use the MID price field provided by Bloomberg wholesale instead of calculating it from the raw BID and ASK fields in the application, the validation rules were failing MID price field check when the vendor failed to provided a value and this keeps the entire price record from being distributed. The assumption that BB will always reliably provide the MID value despite their promise was incorrect and we had to update the requirements to say that if the raw MID price is not available from the vendor, calculate it from BID and ASK like we always did and indicate the source of MID as wither 'Derived' or 'BB/CBBT'. Therefore the source 'derived' or 'BB' gives more context on the origin of MID price value they are seeing and them to override the suspect status to normal and allow it to flow into the downstream consolidation data store. 



1. subscribes to receive 

Going back to the user story where Bloomberg retired one price field and added a new piece of data, MID, the requirement was for the system to use the new MID price from BB as-is rather the calculate it BID/ASK) in the consolidated price table. One of the critical process before certifying the consolidated prices as the golden copy, the pricing directorate cleanses those prices flagged as suspects by the application and if the consolidated pricing fails one of the validation rules such as 'bid/ask spread', missing prices, and MID price that calculated/derived from Bid and Ask (bid+ask)/2. using a cleansing workflow application with a UI As a final validation before the prices are cleansed