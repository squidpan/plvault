# Session 8 — PostgreSQL Refresher

Suggested database: `synthetic_rep_code_ba_lab`
Schema: `repcode_lab`
PostgreSQL: 14.23

## Purpose

Practice SQL from a Business Analyst / systems-analysis perspective using conceptual Rep Code Expansion training data. Focus: querying, validation, mapping, reconciliation, lineage, and data-quality investigation.

## Data Model

Tables: `rep_code_master`, `rep_code_translation`, `client_account`, `orders`, `executions`, `trades`.

Important relationships:
- `client_account.rep_code` FK → `rep_code_master.rep_code` PK
- `orders.account_id` FK → `client_account.account_id` PK
- `executions.order_id` FK → `orders.order_id` PK
- `trades.order_id` FK → `orders.order_id` PK
- `trades.account_id` FK → `client_account.account_id` PK

Rule: **FK → REFERENCES → PK**. Business/process-flow direction is a different perspective from FK-reference direction.

## psql Discovery

- `\dn` — schemas
- `\dt repcode_lab_v1.*` — lab tables
- `\d <table>` — columns, keys, references
- `\r` — clear unfinished query buffer
- `SET search_path TO repcode_lab_v1;`

`=>` means ready for a statement; `->` means the statement is unfinished. SQL statements end with `;`.

## SQL Covered

### Filtering and ordering

    SELECT account_id, client_name, rep_code, account_status
    FROM client_account
    WHERE account_status = 'ACTIVE'
    ORDER BY account_id;

    SELECT order_id, account_id, rep_code, symbol, side, quantity, order_status
    FROM orders
    WHERE side = 'BUY'
      AND order_status = 'FILLED'
    ORDER BY order_id;

    SELECT order_id, account_id, rep_code, symbol, order_status, created_at
    FROM orders
    WHERE created_at >= '2026-08-21'
    ORDER BY created_at;

### Aggregation

    SELECT order_status, COUNT(*)
    FROM orders
    GROUP BY order_status
    ORDER BY order_status;

    SELECT symbol, SUM(quantity) AS total_order_quantity
    FROM orders
    GROUP BY symbol
    HAVING SUM(quantity) > 100
    ORDER BY symbol;

`WHERE` filters rows before grouping; `HAVING` filters groups after aggregation.

### INNER JOIN — account/order Rep Code mismatch

    SELECT
        o.order_id,
        o.account_id,
        a.client_name,
        a.rep_code AS account_rep_code,
        o.rep_code AS order_rep_code,
        o.symbol,
        o.order_status
    FROM orders o
    JOIN client_account a
        ON o.account_id = a.account_id
    WHERE a.rep_code <> o.rep_code
    ORDER BY o.account_id;

Finding: account `10001` is assigned `ABC1`, while order `50006` carries `DEF1`.

`JOIN ... ON` establishes the relationship; `WHERE` filters the joined rows.

### INNER JOIN — order Rep Code business meaning

    SELECT
        o.order_id,
        o.account_id,
        o.rep_code,
        r.rep_name,
        r.rep_type,
        o.symbol,
        o.order_status
    FROM orders o
    JOIN rep_code_master r
        ON o.rep_code = r.rep_code;

### LEFT OUTER JOIN — missing legacy mappings

In `A LEFT JOIN B`, A is the left table. Read it as: **Keep A; bring B when available.**

    SELECT
        r.rep_code,
        r.rep_name,
        r.active_flag,
        t.active_flag AS translation_active,
        t.legacy_rep_code
    FROM rep_code_master r
    LEFT JOIN rep_code_translation t
        ON r.rep_code = t.new_rep_code
    WHERE r.active_flag = TRUE
      AND t.legacy_rep_code IS NULL;

Finding: active `JKL1` has an active translation row but a NULL legacy Rep Code.

### Trade-to-translation reconciliation

    SELECT
        tr.trade_id,
        tr.rep_code,
        tr.legacy_rep_code AS trade_legacy_code,
        t.legacy_rep_code AS expected_legacy_code,
        tr.trade_status
    FROM trades tr
    JOIN rep_code_translation t
        ON tr.rep_code = t.new_rep_code
    WHERE tr.legacy_rep_code IS DISTINCT FROM t.legacy_rep_code
    ORDER BY trade_id;

A deliberate test changed trade `90005` from expected `DEF` to `BAD`; this query caught it. The row was restored to `DEF`.

### CASE — mapping readiness

    SELECT
        r.rep_code,
        r.rep_name,
        t.legacy_rep_code,
        CASE
            WHEN r.active_flag = FALSE THEN 'INACTIVE'
            WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
            ELSE 'READY'
        END AS mapping_status
    FROM rep_code_master r
    LEFT JOIN rep_code_translation t
        ON r.rep_code = t.new_rep_code
    ORDER BY r.rep_code;

Examples: `ABC1 → READY`, `JKL1 → MISSING_MAPPING`, `MNO1 → INACTIVE`.

An earlier query used two tables without a join condition and produced 36 rows (6 × 6), demonstrating an unintended Cartesian product: syntactically valid SQL can still produce a logically wrong business answer.

### CTE

    WITH mapping_readiness AS (
        SELECT
            r.rep_code,
            r.rep_name,
            t.legacy_rep_code,
            CASE
                WHEN r.active_flag = FALSE THEN 'INACTIVE'
                WHEN t.legacy_rep_code IS NULL THEN 'MISSING_MAPPING'
                ELSE 'READY'
            END AS mapping_status
        FROM rep_code_master r
        LEFT JOIN rep_code_translation t
            ON r.rep_code = t.new_rep_code
    )
    SELECT rep_code, rep_name, mapping_status
    FROM mapping_readiness
    WHERE mapping_status <> 'READY';

Result: `JKL1 → MISSING_MAPPING`; `MNO1 → INACTIVE`.

### Subquery

    SELECT order_id, symbol, quantity, order_status
    FROM orders
    WHERE quantity > (
        SELECT AVG(quantity)
        FROM orders
    )
    ORDER BY quantity DESC;

## PostgreSQL → Oracle Bridge

Most BA-level SQL transfers directly: SELECT/FROM/WHERE, INNER/LEFT JOIN, GROUP BY/HAVING, COUNT/SUM/AVG, CASE, CTEs, subqueries, and `IS NULL`.

Recognize:
- PostgreSQL commonly uses `LIMIT`; modern Oracle supports `FETCH FIRST ... ROWS ONLY`.
- PostgreSQL has native boolean columns; Oracle environments may use flags such as `Y/N` or `1/0`, depending on schema/version.
- PostgreSQL commonly uses `VARCHAR`; Oracle commonly uses `VARCHAR2`.
- Both support `COALESCE`; Oracle code also commonly uses `NVL`.
- Do not assume PostgreSQL-specific NULL-safe operators behave identically in every Oracle environment.

## Interview Positioning

> I use SQL from a Business Analyst and systems-analysis perspective—to query and validate data, join related datasets, investigate mapping and reconciliation issues, trace values across tables, and support testing and production analysis. I'm comfortable with joins, filtering, aggregation, CTEs and basic subqueries.

## Status

The SQL foundation is complete; the lab now continues with effective-dated, consumer-specific mapping and exception analysis.
