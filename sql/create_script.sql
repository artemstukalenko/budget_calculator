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