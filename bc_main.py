from psycopg2 import OperationalError

import bc_query
import bc_calculate

incorrect_password_error = 'password authentication failed for user "postgres"'

def provide_data(accounts, ex_rates):
    bc_calculate.calculate_ex_rates(ex_rates)
    print(f'Total UAH = {"{:,}".format(bc_calculate.calculate_total_uah(accounts))} ₴')
    print(f'Total USD = {"{:,}".format(bc_calculate.calculate_total_usd(accounts))} $')
    print('****************************************************************')
    print(f'Total liquid UAH = {"{:,}".format(bc_calculate.calculate_total_liquid_uah(accounts))} ₴')
    print(f'Total liquid USD = {"{:,}".format(bc_calculate.calculate_total_liquid_usd(accounts))} $')
    print(f'{bc_calculate.calculate_total_liquid_share()}% of net worth is liquid')

def request_password():
    password = input("Enter password: ")
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