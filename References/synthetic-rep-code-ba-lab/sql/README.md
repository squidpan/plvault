# SQL Lab

Suggested database: `synthetic_rep_code_ba_lab`
Schema: `repcode_lab`
PostgreSQL: 14+

## Tables
- rep_code_master
- interface_consumer
- rep_code_translation (consumer-specific, effective-dated, versioned)
- client_account
- orders
- executions
- trades

## Current script

Run `synthetic-rep-code-ba-lab.sql`. It creates and seeds the lab and runs four BA investigations:

1. Account/order attribution mismatch
2. Missing effective mapping by consumer
3. Trade output versus effective mapping/version reconciliation
4. Duplicate active mapping candidates

The original v1 schema is retained under `archive/sql/` for learning comparison. The current model fixes its biggest limitation: a single mapping per new code could not represent multiple consumers or mapping history.

The example uniqueness constraint prevents an exact duplicate version, but it does not prevent overlapping effective-date intervals. A production implementation would require an approved exclusion constraint, trigger, or controlled mapping service policy.

## Setup

    createdb synthetic_rep_code_ba_lab
    psql -d synthetic_rep_code_ba_lab -f sql/synthetic-rep-code-ba-lab.sql

All identifiers and data are fictional.
