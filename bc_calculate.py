from decimal import Decimal, ROUND_DOWN

usd_to_uah = None
eur_to_uah = None
usd_to_eur = None

total_uah = None
total_usd = None

total_liquid_uah = None
total_liquid_usd = None

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
    global total_uah

    uah_acc_sum = sum(map(lambda acc: acc.amount, filter(lambda acc: acc.currency == 'UAH', accounts)))
    usd_acc_sum = sum(map(lambda acc: acc.amount * usd_to_uah , filter(lambda acc: acc.currency == 'USD', accounts)))
    eur_acc_sum = sum(map(lambda acc: acc.amount * eur_to_uah , filter(lambda acc: acc.currency == 'EUR', accounts)))

    result = uah_acc_sum + usd_acc_sum + eur_acc_sum
    total_uah = result

    return Decimal(result).quantize(Decimal('0.00'), rounding = ROUND_DOWN)


def calculate_total_usd(accounts):
    global total_usd

    uah_acc_sum = sum(map(lambda acc: acc.amount / usd_to_uah, filter(lambda acc: acc.currency == 'UAH', accounts)))
    usd_acc_sum = sum(map(lambda acc: acc.amount, filter(lambda acc: acc.currency == 'USD', accounts)))
    eur_acc_sum = sum(map(lambda acc: acc.amount * usd_to_eur, filter(lambda acc: acc.currency == 'EUR', accounts)))

    result = uah_acc_sum + usd_acc_sum + eur_acc_sum
    total_usd = result

    return Decimal(result).quantize(Decimal('0.00'), rounding = ROUND_DOWN)


def calculate_total_liquid_uah(accounts):
    global total_liquid_uah

    uah_acc_sum = sum(map(lambda acc: acc.amount, filter(lambda acc: acc.currency == 'UAH' and acc.is_liquid, accounts)))
    usd_acc_sum = sum(map(lambda acc: acc.amount * usd_to_uah, filter(lambda acc: acc.currency == 'USD' and acc.is_liquid, accounts)))
    eur_acc_sum = sum(map(lambda acc: acc.amount * eur_to_uah, filter(lambda acc: acc.currency == 'EUR' and acc.is_liquid, accounts)))

    result = uah_acc_sum + usd_acc_sum + eur_acc_sum
    total_liquid_uah = result

    return Decimal(result).quantize(Decimal('0.00'), rounding = ROUND_DOWN)


def calculate_total_liquid_usd(accounts):
    global total_liquid_usd

    uah_acc_sum = sum(map(lambda acc: acc.amount / usd_to_uah, filter(lambda acc: acc.currency == 'UAH' and acc.is_liquid, accounts)))
    usd_acc_sum = sum(map(lambda acc: acc.amount, filter(lambda acc: acc.currency == 'USD' and acc.is_liquid, accounts)))
    eur_acc_sum = sum(map(lambda acc: acc.amount * usd_to_eur, filter(lambda acc: acc.currency == 'EUR' and acc.is_liquid, accounts)))

    result = uah_acc_sum + usd_acc_sum + eur_acc_sum
    total_liquid_usd = result

    return Decimal(result).quantize(Decimal('0.00'), rounding = ROUND_DOWN)


def calculate_total_liquid_share():
    result = (total_liquid_usd / total_usd) * 100
    return Decimal(result).quantize(Decimal('0.00'), rounding = ROUND_DOWN)


def calculate_share_of_money_with_interest_rate(accounts):
    uah_acc_sum = sum(
        map(lambda acc: acc.amount / usd_to_uah,
            filter(lambda acc: acc.currency == 'UAH' and acc.interest_rate != 0, accounts)))
    usd_acc_sum = sum(
        map(lambda acc: acc.amount, filter(lambda acc: acc.currency == 'USD' and acc.interest_rate != 0, accounts)))
    eur_acc_sum = sum(
        map(lambda acc: acc.amount * usd_to_eur,
            filter(lambda acc: acc.currency == 'EUR' and acc.interest_rate != 0, accounts)))

    total_interest_rate_usd = uah_acc_sum + usd_acc_sum + eur_acc_sum

    result = (total_interest_rate_usd / total_usd) * 100
    return Decimal(result).quantize(Decimal('0.00'), rounding=ROUND_DOWN)


def calculate_share_of_accounts_beat_inflation(accounts):
    uah_acc_sum = sum(
        map(lambda acc: acc.amount / usd_to_uah,
            filter(lambda acc: acc.currency == 'UAH' and acc.interest_rate > 3, accounts)))
    usd_acc_sum = sum(
        map(lambda acc: acc.amount, filter(lambda acc: acc.currency == 'USD' and acc.interest_rate > 3, accounts)))
    eur_acc_sum = sum(
        map(lambda acc: acc.amount * usd_to_eur,
            filter(lambda acc: acc.currency == 'EUR' and acc.interest_rate > 3, accounts)))

    total_interest_rate_usd = uah_acc_sum + usd_acc_sum + eur_acc_sum

    result = (total_interest_rate_usd / total_usd) * 100
    return Decimal(result).quantize(Decimal('0.00'), rounding=ROUND_DOWN)