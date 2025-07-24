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


def calculate_exposures(accounts):
    exposure_table = {}

    account_group_to_account = {}
    account_groups = set(map(lambda acc: acc.account_group, accounts))

    for account_group in account_groups:
        account_group_to_account[account_group] = []

    for account in accounts:
        account_group_to_account[account.account_group].append(account)

    for account_group, accounts_in_group in account_group_to_account.items():
        account_group_sum = calculate_account_group_sum_usd(accounts_in_group)
        exposure_table[account_group] = Decimal((account_group_sum / total_usd) * 100).quantize(Decimal('0.00'), rounding=ROUND_DOWN)

    return dict(sorted(exposure_table.items(), key = lambda item: item[1], reverse = True))


def calculate_account_group_sum_usd(accounts_in_group):
    return sum(map(lambda account: calculate_account_sum_usd(account), accounts_in_group))

def calculate_account_sum_usd(account):
    account_sum_usd = 0

    if account.currency == 'UAH':
        account_sum_usd = account.amount / usd_to_uah
    elif account.currency == 'USD':
        account_sum_usd = account.amount
    elif account.currency == 'EUR':
        account_sum_usd = account.amount * usd_to_eur

    return account_sum_usd