from psycopg2 import OperationalError

import bc_query

incorrect_password_error = 'password authentication failed for user "postgres"'

def provide_data(accounts, ex_rates):
    print(f'Accounts = {accounts}')
    print(f'Rates = {ex_rates}')

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