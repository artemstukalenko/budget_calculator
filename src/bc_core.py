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


class HistoryRecord:
    def __init__(self, date, total_uah, total_usd, total_liq_uah,
                 total_liq_usd, liquid_percent, interest_rate_percent,
                 exposure_table):
        self.date = date
        self.total_uah = total_uah
        self.total_usd = total_usd
        self.total_liq_uah = total_liq_uah
        self.total_liq_usd = total_liq_usd
        self.liquid_percent = liquid_percent
        self.interest_rate_percent = interest_rate_percent
        self.exposure_table = exposure_table

    def __repr__(self):
        representation = '****************************************************************\n'
        representation += f'Total UAH = {"{:,}".format(self.total_uah)} ₴\n'
        representation += f'Total USD = {"{:,}".format(self.total_usd)} $\n'
        representation += f'Total liquid UAH = {"{:,}".format(self.total_liq_uah)} ₴\n'
        representation += f'Total liquid USD = {"{:,}".format(self.total_liq_usd)} $\n'
        representation += '****************************************************************\n'
        representation += f'{self.liquid_percent}% of net worth is liquid\n'
        representation += f'{self.interest_rate_percent}% of net worth has interest rate\n'
        representation += '****************************************************************\n'
        for account_group, share in self.exposure_table.items():
            representation += f'{share:5.2f}% of net worth is in {account_group.upper()}\n'

        return representation