INSERT INTO accounts (name, account_group, currency, amount, is_liquid, is_accumulative, interest_rate)
VALUES
	('card', 'mono', 'UAH', 0.0, TRUE, FALSE, 0.0),
	('card', 'mono', 'USD', 0.0, TRUE, FALSE, 0.0),
	('card', 'mono', 'EUR', 0.0, TRUE, FALSE, 0.0),
	('deposit', 'mono', 'USD', 0.0, FALSE, TRUE, 1.7),
	('cash', 'cash', 'USD', 0.0, TRUE, FALSE, 0.0),
	('card', 'privat', 'UAH', 0.0, TRUE, FALSE, 0.0),
	('card', 'privat', 'USD', 0.0, TRUE, FALSE, 0.0),
	('card', 'zen', 'USD', 0.0, TRUE, FALSE, 0.0),
	('card', 'zen', 'EUR', 0.0, TRUE, FALSE, 0.0),
	('net liquidity', 'IB', 'USD', 0.0, FALSE, TRUE, 0.0);


INSERT INTO exchange_rates (currency_a, currency_b, rate)
VALUES
	('USD', 'UAH', 0.0),
	('EUR', 'UAH', 0.0),
	('USD', 'EUR', 0.0);

SELECT * FROM accounts;
SELECT * FROM exchange_rates;