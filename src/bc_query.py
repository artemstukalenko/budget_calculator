from bc_core import Account
from bc_core import ExchangeRate
from src.bc_db_connect import create_db_session

accounts_query = 'SELECT id, name, account_group, currency, amount, is_liquid, is_accumulative, interest_rate FROM accounts'
ex_rates_query = 'SELECT id, currency_a, currency_b, rate FROM exchange_rates'

def pull_data():
    session = create_db_session()

    accounts = session.query(Account).all()
    ex_rates = session.query(ExchangeRate).all()

    return accounts, ex_rates
