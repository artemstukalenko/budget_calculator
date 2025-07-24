from src import bc_calculate
from src.bc_core import ExchangeRate

exchange_rates = [ExchangeRate(1, 'USD', 'UAH', 10),
                  ExchangeRate(2, 'EUR', 'UAH', 100),
                  ExchangeRate(3, 'USD', 'EUR', 0.1)]

def test_usd_to_uah_calculation():
    bc_calculate.calculate_ex_rates(exchange_rates)
    assert bc_calculate.usd_to_uah == 10


def test_eur_to_uah_calculation():
    bc_calculate.calculate_ex_rates(exchange_rates)
    assert bc_calculate.eur_to_uah == 100


def test_usd_to_eur_calculation():
    bc_calculate.calculate_ex_rates(exchange_rates)
    assert bc_calculate.usd_to_eur == 0.1