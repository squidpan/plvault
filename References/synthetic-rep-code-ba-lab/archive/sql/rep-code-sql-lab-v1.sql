-- Synthetic Rep Code SQL Lab (PostgreSQL)
-- Conceptual training data only; not production schema/data.

DROP SCHEMA IF EXISTS repcode_lab_v1 CASCADE;
CREATE SCHEMA repcode_lab_v1;
SET search_path TO repcode_lab_v1;

CREATE TABLE rep_code_master (
    rep_code        VARCHAR(4) PRIMARY KEY,
    rep_name        VARCHAR(100) NOT NULL,
    rep_type        VARCHAR(30) NOT NULL,
    active_flag     BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE rep_code_translation (
    new_rep_code    VARCHAR(4) PRIMARY KEY,
    legacy_rep_code VARCHAR(3),
    active_flag     BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_translation_rep
        FOREIGN KEY (new_rep_code) REFERENCES rep_code_master(rep_code)
);

CREATE TABLE client_account (
    account_id      BIGINT PRIMARY KEY,
    client_name     VARCHAR(100) NOT NULL,
    rep_code        VARCHAR(4),
    account_status  VARCHAR(20) NOT NULL,
    CONSTRAINT fk_account_rep
        FOREIGN KEY (rep_code) REFERENCES rep_code_master(rep_code)
);

CREATE TABLE orders (
    order_id        BIGINT PRIMARY KEY,
    account_id      BIGINT NOT NULL,
    rep_code        VARCHAR(4),
    symbol          VARCHAR(12) NOT NULL,
    side            VARCHAR(4) NOT NULL,
    quantity        INTEGER NOT NULL,
    order_status    VARCHAR(30) NOT NULL,
    created_at      TIMESTAMP NOT NULL,
    CONSTRAINT fk_order_account
        FOREIGN KEY (account_id) REFERENCES client_account(account_id)
);

CREATE TABLE executions (
    execution_id    BIGINT PRIMARY KEY,
    order_id        BIGINT NOT NULL,
    executed_qty    INTEGER NOT NULL,
    executed_price  NUMERIC(12,2) NOT NULL,
    executed_at     TIMESTAMP NOT NULL,
    CONSTRAINT fk_execution_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE trades (
    trade_id        BIGINT PRIMARY KEY,
    order_id        BIGINT NOT NULL,
    account_id      BIGINT NOT NULL,
    rep_code        VARCHAR(4),
    legacy_rep_code VARCHAR(3),
    symbol          VARCHAR(12) NOT NULL,
    quantity        INTEGER NOT NULL,
    trade_status    VARCHAR(30) NOT NULL,
    CONSTRAINT fk_trade_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CONSTRAINT fk_trade_account
        FOREIGN KEY (account_id) REFERENCES client_account(account_id)
);

INSERT INTO rep_code_master (rep_code, rep_name, rep_type, active_flag) VALUES
('ABC1', 'Smith Advisory Team', 'TEAM', TRUE),
('DEF1', 'Mary Jones', 'INDIVIDUAL', TRUE),
('GHI1', 'North Region Advisory', 'TEAM', TRUE),
('JKL1', 'Legacy Transition Group', 'TEAM', TRUE),
('MNO1', 'Inactive Advisor Group', 'TEAM', FALSE),
('PQR1', 'Trading Support Desk', 'ORDER_ROLE', TRUE);

INSERT INTO rep_code_translation (new_rep_code, legacy_rep_code, active_flag) VALUES
('ABC1', 'XYZ', TRUE),
('DEF1', 'DEF', TRUE),
('GHI1', 'GHI', TRUE),
('JKL1', NULL, TRUE),
('MNO1', 'MNO', FALSE),
('PQR1', 'PQR', TRUE);

INSERT INTO client_account (account_id, client_name, rep_code, account_status) VALUES
(10001, 'Paul Client', 'ABC1', 'ACTIVE'),
(10002, 'Jane Investor', 'DEF1', 'ACTIVE'),
(10003, 'Robert Client', 'GHI1', 'ACTIVE'),
(10004, 'Acme Family Trust', 'ABC1', 'ACTIVE'),
(10005, 'Northshore LLC', 'JKL1', 'ACTIVE'),
(10006, 'Old Account', 'MNO1', 'CLOSED');

INSERT INTO orders (order_id, account_id, rep_code, symbol, side, quantity, order_status, created_at) VALUES
(50001, 10001, 'ABC1', 'IBM',  'BUY',  100, 'FILLED',           '2026-08-20 09:35:00'),
(50002, 10002, 'DEF1', 'AAPL', 'BUY',   50, 'FILLED',           '2026-08-20 10:15:00'),
(50003, 10003, 'GHI1', 'MSFT', 'SELL', 200, 'PARTIALLY_FILLED', '2026-08-20 11:10:00'),
(50004, 10004, 'ABC1', 'IBM',  'BUY',  125, 'NEW',              '2026-08-21 09:05:00'),
(50005, 10005, 'JKL1', 'NVDA', 'BUY',   75, 'FILLED',           '2026-08-21 13:25:00'),
(50006, 10001, 'DEF1', 'TSLA', 'BUY',   25, 'FILLED',           '2026-08-21 14:10:00');

INSERT INTO executions (execution_id, order_id, executed_qty, executed_price, executed_at) VALUES
(70001, 50001,  40, 250.00, '2026-08-20 09:36:10'),
(70002, 50001,  60, 250.05, '2026-08-20 09:36:25'),
(70003, 50002,  50, 225.50, '2026-08-20 10:16:12'),
(70004, 50003, 100, 410.25, '2026-08-20 11:12:30'),
(70005, 50005,  75, 135.75, '2026-08-21 13:27:05'),
(70006, 50006,  25, 340.10, '2026-08-21 14:11:15');

INSERT INTO trades (trade_id, order_id, account_id, rep_code, legacy_rep_code, symbol, quantity, trade_status) VALUES
(90001, 50001, 10001, 'ABC1', 'XYZ', 'IBM',  100, 'SETTLED'),
(90002, 50002, 10002, 'DEF1', 'DEF', 'AAPL',  50, 'SETTLED'),
(90003, 50003, 10003, 'GHI1', 'GHI', 'MSFT', 100, 'PENDING'),
(90004, 50005, 10005, 'JKL1', NULL,  'NVDA',  75, 'EXCEPTION'),
(90005, 50006, 10001, 'DEF1', 'DEF', 'TSLA',  25, 'SETTLED');

-- Intentional data-quality scenarios:
-- 50006 uses DEF1 even though account 10001 is assigned ABC1.
-- JKL1 has no legacy mapping, creating an exception scenario.
