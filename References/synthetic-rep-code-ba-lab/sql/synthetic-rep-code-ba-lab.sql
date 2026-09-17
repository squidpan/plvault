-- Synthetic Rep Code BA Lab (PostgreSQL)
-- Fictional training schema and data only. Not an employer schema or implementation.

DROP SCHEMA IF EXISTS repcode_lab CASCADE;
CREATE SCHEMA repcode_lab;
SET search_path TO repcode_lab;

CREATE TABLE rep_code_master (
    rep_code VARCHAR(4) PRIMARY KEY,
    rep_name VARCHAR(100) NOT NULL,
    rep_type VARCHAR(30) NOT NULL,
    active_flag BOOLEAN NOT NULL DEFAULT TRUE,
    CHECK (rep_code ~ '^[A-Z0-9]{4}$')
);

CREATE TABLE interface_consumer (
    consumer_id VARCHAR(40) PRIMARY KEY,
    consumer_name VARCHAR(100) NOT NULL,
    max_rep_code_length INTEGER NOT NULL CHECK (max_rep_code_length IN (3, 4)),
    active_flag BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE rep_code_translation (
    translation_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    new_rep_code VARCHAR(4) NOT NULL REFERENCES rep_code_master(rep_code),
    consumer_id VARCHAR(40) NOT NULL REFERENCES interface_consumer(consumer_id),
    legacy_rep_code VARCHAR(3) NOT NULL,
    effective_from TIMESTAMP NOT NULL,
    effective_to TIMESTAMP,
    mapping_status VARCHAR(20) NOT NULL CHECK (mapping_status IN ('DRAFT', 'APPROVED', 'RETIRED')),
    mapping_version VARCHAR(30) NOT NULL,
    CHECK (legacy_rep_code ~ '^[A-Z0-9]{3}$'),
    CHECK (effective_to IS NULL OR effective_to > effective_from),
    UNIQUE (new_rep_code, consumer_id, effective_from, mapping_version)
);

CREATE TABLE client_account (
    account_id BIGINT PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    rep_code VARCHAR(4) REFERENCES rep_code_master(rep_code),
    account_status VARCHAR(20) NOT NULL
);

CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    account_id BIGINT NOT NULL REFERENCES client_account(account_id),
    rep_code VARCHAR(4) REFERENCES rep_code_master(rep_code),
    symbol VARCHAR(12) NOT NULL,
    side VARCHAR(4) NOT NULL CHECK (side IN ('BUY', 'SELL')),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    order_status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE executions (
    execution_id BIGINT PRIMARY KEY,
    order_id BIGINT NOT NULL REFERENCES orders(order_id),
    executed_qty INTEGER NOT NULL CHECK (executed_qty > 0),
    executed_price NUMERIC(12,2) NOT NULL CHECK (executed_price > 0),
    executed_at TIMESTAMP NOT NULL
);

CREATE TABLE trades (
    trade_id BIGINT PRIMARY KEY,
    order_id BIGINT NOT NULL REFERENCES orders(order_id),
    account_id BIGINT NOT NULL REFERENCES client_account(account_id),
    rep_code VARCHAR(4) REFERENCES rep_code_master(rep_code),
    legacy_rep_code VARCHAR(3),
    consumer_id VARCHAR(40) REFERENCES interface_consumer(consumer_id),
    mapping_version VARCHAR(30),
    symbol VARCHAR(12) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    trade_status VARCHAR(30) NOT NULL
);

INSERT INTO rep_code_master VALUES
('A7Q4', 'North Advisory Team', 'TEAM', TRUE),
('B2M8', 'Central Advisory Team', 'TEAM', TRUE),
('C5R1', 'Trading Support Desk', 'ORDER_ROLE', TRUE),
('Z9X8', 'Transition Group', 'TEAM', TRUE),
('D4N6', 'Retired Advisory Group', 'TEAM', FALSE);

INSERT INTO interface_consumer VALUES
('MODERN-OMS', 'Modern Order Consumer', 4, TRUE),
('LEGACY-ROUTER-1', 'Legacy Routing Consumer', 3, TRUE),
('LEGACY-REPORT-1', 'Legacy Reporting Consumer', 3, TRUE);

INSERT INTO rep_code_translation
    (new_rep_code, consumer_id, legacy_rep_code, effective_from, effective_to, mapping_status, mapping_version)
VALUES
('A7Q4', 'LEGACY-ROUTER-1', 'K42', '2026-01-01', NULL, 'APPROVED', 'MAP-V1'),
('A7Q4', 'LEGACY-REPORT-1', 'R42', '2026-01-01', NULL, 'APPROVED', 'MAP-V1'),
('B2M8', 'LEGACY-ROUTER-1', 'M28', '2026-01-01', NULL, 'APPROVED', 'MAP-V1'),
('D4N6', 'LEGACY-ROUTER-1', 'N46', '2025-01-01', '2026-01-01', 'RETIRED', 'MAP-V0');

INSERT INTO client_account VALUES
(10001, 'Sample Client One', 'A7Q4', 'ACTIVE'),
(10002, 'Sample Client Two', 'B2M8', 'ACTIVE'),
(10003, 'Sample Family Trust', 'Z9X8', 'ACTIVE'),
(10004, 'Closed Sample Account', 'D4N6', 'CLOSED');

INSERT INTO orders VALUES
(50001, 10001, 'A7Q4', 'ALFA', 'BUY', 100, 'FILLED', '2026-09-16 09:35:00'),
(50002, 10002, 'B2M8', 'BETA', 'SELL', 50, 'FILLED', '2026-09-16 10:15:00'),
(50003, 10003, 'Z9X8', 'GAMA', 'BUY', 75, 'EXCEPTION', '2026-09-16 11:10:00'),
(50004, 10001, 'B2M8', 'DLTA', 'BUY', 25, 'FILLED', '2026-09-16 12:10:00');

INSERT INTO executions VALUES
(70001, 50001, 100, 25.00, '2026-09-16 09:36:10'),
(70002, 50002, 50, 42.50, '2026-09-16 10:16:12'),
(70003, 50004, 25, 34.10, '2026-09-16 12:11:15');

INSERT INTO trades VALUES
(90001, 50001, 10001, 'A7Q4', 'K42', 'LEGACY-ROUTER-1', 'MAP-V1', 'ALFA', 100, 'SETTLED'),
(90002, 50002, 10002, 'B2M8', 'M28', 'LEGACY-ROUTER-1', 'MAP-V1', 'BETA', 50, 'SETTLED'),
(90003, 50003, 10003, 'Z9X8', NULL, 'LEGACY-ROUTER-1', NULL, 'GAMA', 75, 'EXCEPTION'),
(90004, 50004, 10001, 'B2M8', 'M28', 'LEGACY-ROUTER-1', 'MAP-V1', 'DLTA', 25, 'SETTLED');

-- 1. Account/order attribution mismatch.
SELECT o.order_id, o.account_id, a.rep_code AS account_rep_code, o.rep_code AS order_rep_code
FROM orders o JOIN client_account a USING (account_id)
WHERE a.rep_code IS DISTINCT FROM o.rep_code ORDER BY o.order_id;

-- 2. Active codes missing an approved mapping for each legacy consumer as of a timestamp.
SELECT r.rep_code, c.consumer_id
FROM rep_code_master r
CROSS JOIN interface_consumer c
LEFT JOIN rep_code_translation t
  ON t.new_rep_code = r.rep_code AND t.consumer_id = c.consumer_id
 AND t.mapping_status = 'APPROVED'
 AND TIMESTAMP '2026-09-16 12:00:00' >= t.effective_from
 AND (t.effective_to IS NULL OR TIMESTAMP '2026-09-16 12:00:00' < t.effective_to)
WHERE r.active_flag AND c.active_flag AND c.max_rep_code_length = 3
  AND t.translation_id IS NULL
ORDER BY r.rep_code, c.consumer_id;

-- 3. Trade output differs from the effective mapping/version.
SELECT tr.trade_id, tr.rep_code, tr.consumer_id,
       tr.legacy_rep_code AS actual_alias, t.legacy_rep_code AS expected_alias,
       tr.mapping_version AS actual_version, t.mapping_version AS expected_version
FROM trades tr
JOIN rep_code_translation t
  ON t.new_rep_code = tr.rep_code AND t.consumer_id = tr.consumer_id
 AND t.mapping_status = 'APPROVED'
 AND TIMESTAMP '2026-09-16 12:00:00' >= t.effective_from
 AND (t.effective_to IS NULL OR TIMESTAMP '2026-09-16 12:00:00' < t.effective_to)
WHERE tr.legacy_rep_code IS DISTINCT FROM t.legacy_rep_code
   OR tr.mapping_version IS DISTINCT FROM t.mapping_version
ORDER BY tr.trade_id;

-- 4. Duplicate active candidates; a production design should prevent this.
SELECT new_rep_code, consumer_id, COUNT(*) AS active_candidate_count
FROM rep_code_translation
WHERE mapping_status = 'APPROVED'
  AND TIMESTAMP '2026-09-16 12:00:00' >= effective_from
  AND (effective_to IS NULL OR TIMESTAMP '2026-09-16 12:00:00' < effective_to)
GROUP BY new_rep_code, consumer_id
HAVING COUNT(*) > 1;
