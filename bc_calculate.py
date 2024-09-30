from decimal import Decimal, ROUND_DOWN

usd_to_uah = None
eur_to_uah = None
usd_to_eur = None

def calculate_ex_rates(exchange_rates):
    global usd_to_uah, eur_to_uah, usd_to_eur

    usd_to_uah = sum(map(lambda ex_rate: ex_rate.rate,
                         filter(lambda ex_rate: ex_rate.currency_a == 'USD' and ex_rate.currency_b == 'UAH',
                                exchange_rates)))

    eur_to_uah = sum(map(lambda ex_rate: ex_rate.rate,
                         filter(lambda ex_rate: ex_rate.currency_a == 'EUR' and ex_rate.currency_b == 'UAH',
                                exchange_rates)))

    usd_to_eur = sum(map(lambda ex_rate: ex_rate.rate,
                         filter(lambda ex_rate: ex_rate.currency_a == 'USD' and ex_rate.currency_b == 'EUR',
                                exchange_rates)))

def calculate_total_uah(accounts):
    uah_acc_sum = sum(map(lambda acc: acc.amount, filter(lambda acc: acc.currency == 'UAH', accounts)))
    usd_acc_sum = sum(map(lambda acc: acc.amount * usd_to_uah , filter(lambda acc: acc.currency == 'USD', accounts)))
    eur_acc_sum = sum(map(lambda acc: acc.amount * eur_to_uah , filter(lambda acc: acc.currency == 'EUR', accounts)))

    return Decimal(uah_acc_sum + usd_acc_sum + eur_acc_sum).quantize(Decimal('0.00'), rounding = ROUND_DOWN)


def calculate_total_usd(accounts):
    uah_acc_sum = sum(map(lambda acc: acc.amount / usd_to_uah, filter(lambda acc: acc.currency == 'UAH', accounts)))
    usd_acc_sum = sum(map(lambda acc: acc.amount, filter(lambda acc: acc.currency == 'USD', accounts)))
    eur_acc_sum = sum(map(lambda acc: acc.amount * usd_to_eur, filter(lambda acc: acc.currency == 'EUR', accounts)))

    return Decimal(uah_acc_sum + usd_acc_sum + eur_acc_sum).quantize(Decimal('0.00'), rounding = ROUND_DOWN)