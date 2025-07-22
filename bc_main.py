from psycopg2 import OperationalError
import argparse
import bc_query
import bc_calculate

incorrect_password_error = 'password authentication failed for user "postgres"'

def provide_data(accounts, ex_rates):
    bc_calculate.calculate_ex_rates(ex_rates)
    print('\n')
    print('****************************************************************')
    print(f'Total UAH = {"{:,}".format(bc_calculate.calculate_total_uah(accounts))} ₴')
    print(f'Total USD = {"{:,}".format(bc_calculate.calculate_total_usd(accounts))} $')
    print(f'Total liquid UAH = {"{:,}".format(bc_calculate.calculate_total_liquid_uah(accounts))} ₴')
    print(f'Total liquid USD = {"{:,}".format(bc_calculate.calculate_total_liquid_usd(accounts))} $')
    print('****************************************************************')
    print(f'{bc_calculate.calculate_total_liquid_share()}% of net worth is liquid')
    print(f'{bc_calculate.calculate_share_of_money_with_interest_rate(accounts)}% of net worth has interest rate')
    print(f'{bc_calculate.calculate_share_of_accounts_beat_inflation(accounts)}% of net worth has interest rate that can beat inflation')
    print('****************************************************************')
    exposure_table = bc_calculate.calculate_exposures(accounts)
    for account_group, share in exposure_table.items():
        print(f'{share:5.2f}% of net worth is in {account_group.upper()}')

def request_password():
    parser = argparse.ArgumentParser()
    parser.add_argument("--password", type=str, help="DB password")
    parser.add_argument("--persist", type=bool, help="Whether to persist result to DB")

    args = parser.parse_args()

    password = args.password
    if password:
        try:
            accounts, ex_rates = bc_query.pull_data(password)
            provide_data(accounts, ex_rates)
        except OperationalError as error:
            error_message = str(error)

            if incorrect_password_error in error_message:
                print('Incorrect password!')
                request_password()
            else:
                print('An error occurred while pulling data from DB:')
                print(error_message)


request_password()