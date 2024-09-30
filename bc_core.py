class Account:
    def __init__(self, id, name, account_group, currency, amount,
                 is_liquid, is_accumulative, interest_rate):
        self.id = id
        self.name = name
        self.account_group = account_group
        self.currency = currency
        self.amount = amount
        self.is_liquid = is_liquid
        self.is_accumulative = is_accumulative
        self.interest_rate = interest_rate


    def __repr__(self):
        return (f'Account(id = {self.id}, name = {self.name}, account_group = {self.account_group}, currency = {self.currency}, '
                f'amount = {self.amount}, is_liquid = {self.is_liquid}, is_accumulative = {self.is_accumulative}, interest_rate = {self.interest_rate})')



class ExchangeRate:
    def __init__(self, id, currency_a, currency_b, rate):
        self.id = id
        self.currency_a = currency_a
        self.currency_b = currency_b
        self.rate = rate


    def __repr__(self):
        return f'ExchangeRate(id = {self.id}, currency_a = {self.currency_a}, currency_b = {self.currency_b}, rate = {self.rate})'