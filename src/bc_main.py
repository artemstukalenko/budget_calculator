from psycopg2 import OperationalError
import argparse

import bc_persist
import bc_query
import bc_calculate
from datetime import datetime
from bc_core import HistoryRecord

incorrect_password_error = 'password authentication failed for user "postgres"'

def provide_data(accounts, ex_rates) -> HistoryRecord:
    bc_calculate.calculate_ex_rates(ex_rates)
    record = HistoryRecord(datetime.now(), bc_calculate.calculate_total_uah(accounts),
                           bc_calculate.calculate_total_usd(accounts),
                           bc_calculate.calculate_total_liquid_uah(accounts),
                           bc_calculate.calculate_total_liquid_usd(accounts),
                           bc_calculate.calculate_total_liquid_share(),
                           bc_calculate.calculate_share_of_money_with_interest_rate(accounts),
                           bc_calculate.calculate_exposures(accounts))

    return record

def request_password():
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action='store_true', help="Whether to persist result to DB")

    args, unknown = parser.parse_known_args()

    try:
        accounts, ex_rates = bc_query.pull_data()
        record = provide_data(accounts, ex_rates)
        print(record)

        if args.persist:
            bc_persist.persist(record)

    except OperationalError as error:
        error_message = str(error)

        if incorrect_password_error in error_message:
            print('Incorrect password!')
            request_password()
        else:
            print('An error occurred while pulling data from DB:')
            print(error_message)


request_password()