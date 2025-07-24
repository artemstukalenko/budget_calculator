from decimal import Decimal, ROUND_DOWN

import pytest

from src import bc_calculate
from src.bc_core import ExchangeRate, Account

exchange_rates = [ExchangeRate(1, 'USD', 'UAH', 10),
                  ExchangeRate(2, 'EUR', 'UAH', 100),
                  ExchangeRate(3, 'USD', 'EUR', 0.1)]

@pytest.fixture(scope="module", autouse=True)
def setup_ex_rates():
    bc_calculate.calculate_ex_rates(exchange_rates)


@pytest.fixture
def setup_accounts():
    return [Account(1, "Cash UAH", "Cash", "UAH", 100, True, False, 0),
                Account(1, "Cash USD", "Cash", "USD", 10, True, False, 0),
                Account(1, "Cash EUR", "Cash", "EUR", 10, True, False, 0),
                Account(1, "Card UAH", "Card", "UAH", 100, True, False, 0),
                Account(1, "Deposit USD", "Savings", "USD", 1000, False, True, 3),
                Account(1, "Binance", "Crypto", "EUR", 100, False, True, 5),
                ]


def test_usd_to_uah_calculation():
    assert bc_calculate.usd_to_uah == 10


def test_eur_to_uah_calculation():
    assert bc_calculate.eur_to_uah == 100


def test_usd_to_eur_calculation():
    assert bc_calculate.usd_to_eur == 0.1


def test_calculate_total_uah(setup_accounts):
    total_uah_expected = 100 + (10 * 10) + (10 * 100) + 100 + (1000 * 10) + (100 * 100)
    total_uah_result = bc_calculate.calculate_total_uah(setup_accounts)
    assert total_uah_expected == total_uah_result


def test_calculate_total_usd(setup_accounts):
    total_usd_expected = (100 / 10) + 10 + (10 * 0.1) + (100 / 10) + 1000 + (100 * 0.1)
    total_usd_result = bc_calculate.calculate_total_usd(setup_accounts)
    assert total_usd_expected == total_usd_result


def test_calculate_total_liq_uah(setup_accounts):
    total_liq_uah_expected = 100 + (10 * 10) + (10 * 100) + 100
    total_liq_uah_result = bc_calculate.calculate_total_liquid_uah(setup_accounts)
    assert total_liq_uah_expected == total_liq_uah_result


def test_calculate_total_liq_usd(setup_accounts):
    total_liq_usd_expected = (100 / 10) + 10 + (10 * 0.1) + (100 / 10)
    total_liq_usd_result = bc_calculate.calculate_total_liquid_usd(setup_accounts)
    assert total_liq_usd_expected == total_liq_usd_result


def test_calculate_total_liq_share(setup_accounts):
    total_liq_usd = (100 / 10) + 10 + (10 * 0.1) + (100 / 10)
    total_usd = (100 / 10) + 10 + (10 * 0.1) + (100 / 10) + 1000 + (100 * 0.1)
    total_liq_share_usd_expected = (total_liq_usd / total_usd) * 100

    total_liq_share_result = bc_calculate.calculate_total_liquid_share()

    assert Decimal(total_liq_share_usd_expected).quantize(Decimal('0.00'), rounding=ROUND_DOWN) == total_liq_share_result


def test_calculate_total_share_with_interest_rate(setup_accounts):
    total_usd_with_interest = 1000 + (100 * 0.1)
    total_usd = (100 / 10) + 10 + (10 * 0.1) + (100 / 10) + 1000 + (100 * 0.1)
    total_usd_with_interest_share_expected = (total_usd_with_interest / total_usd ) * 100

    total_usd_with_interest_share_result = bc_calculate.calculate_share_of_money_with_interest_rate(setup_accounts)

    assert Decimal(total_usd_with_interest_share_expected).quantize(Decimal('0.00'), rounding=ROUND_DOWN) == total_usd_with_interest_share_result