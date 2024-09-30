import psycopg2
from bc_core import Account
from bc_core import ExchangeRate

accounts_query = 'SELECT id, name, account_group, currency, amount, is_liquid, is_accumulative, interest_rate FROM accounts'
ex_rates_query = 'SELECT id, currency_a, currency_b, rate FROM exchange_rates'

def pull_data(password):
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'budget_calculator_db',
        user = 'postgres',
        password=password
    )

    cursor = conn.cursor()

    cursor.execute(accounts_query)

    accounts_rows = cursor.fetchall()
    accounts = []

    for row in accounts_rows:
        account = Account(
            id = row[0],
            name = row[1],
            account_group = row[2],
            currency = row[3],
            amount = row[4],
            is_liquid = row[5],
            is_accumulative = row[6],
            interest_rate = row[7]
        )
        accounts.append(account)


    cursor.execute(ex_rates_query)

    ex_rates_rows = cursor.fetchall()
    ex_rates = []

    for row in ex_rates_rows:
        ex_rate = ExchangeRate(
            id = row[0],
            currency_a = row[1],
            currency_b = row[2],
            rate = row[3]
        )
        ex_rates.append(ex_rate)

    return accounts, ex_rates
