CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
	account_group VARCHAR(20) NOT NULL,
    currency VARCHAR(5) NOT NULL,
    amount DECIMAL,
    is_liquid BOOLEAN NOT NULL,
    is_accumulative BOOLEAN NOT NULL,
    interest_rate DECIMAL
);

CREATE TABLE exchange_rates (
	id SERIAL PRIMARY KEY,
	currency_a VARCHAR(5) NOT NULL,
	currency_b VARCHAR(5) NOT NULL,
	rate DECIMAL
);

CREATE TABLE history (
	id SERIAL PRIMARY KEY,
	date DATE,
	total_uah DECIMAL,
    total_usd DECIMAL,
    total_liq_uah DECIMAL,
    total_liq_usd DECIMAL,
    liquid_percent DECIMAL,
    interest_rate_percent DECIMAL,
    exposure_table VARCHAR(1000)
);