SELECT * FROM accounts;

UPDATE accounts SET amount = 103809.49 WHERE name = 'card' AND account_Group = 'mono' AND currency = 'UAH';
UPDATE accounts SET amount = 1839.77 WHERE name = 'card' AND account_Group = 'mono' AND currency = 'USD';
UPDATE accounts SET amount = 2105.20 WHERE name = 'card' AND account_Group = 'mono' AND currency = 'EUR';
UPDATE accounts SET amount = 7686.75 WHERE name = 'deposit' AND account_Group = 'mono' AND currency = 'USD';
UPDATE accounts SET amount = 9200 WHERE name = 'cash' AND account_Group = 'cash' AND currency = 'USD';
UPDATE accounts SET amount = 0.03 WHERE name = 'card' AND account_Group = 'privat' AND currency = 'UAH';
UPDATE accounts SET amount = 14.11 WHERE name = 'card' AND account_Group = 'privat' AND currency = 'USD';
UPDATE accounts SET amount = 2.79 WHERE name = 'card' AND account_Group = 'zen' AND currency = 'USD';
UPDATE accounts SET amount = 0 WHERE name = 'card' AND account_Group = 'zen' AND currency = 'EUR';
UPDATE accounts SET amount = 3542, WHERE name = 'net liquidity' AND account_Group = 'IB' AND currency = 'USD';

SELECT * FROM exchange_rates;

UPDATE exchange_rates SET rate = 41.42 WHERE currency_a = 'USD' AND currency_b = 'UAH';
UPDATE exchange_rates SET rate = 46.16 WHERE currency_a = 'EUR' AND currency_b = 'UAH';
UPDATE exchange_rates SET rate = 0.89 WHERE currency_a = 'USD' AND currency_b = 'EUR';