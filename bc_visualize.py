import argparse
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--password", type=str, help="DB password")

    args = parser.parse_args()

    engine = create_engine(f"postgresql+psycopg2://postgres:{args.password}@localhost:5432/budget_calculator_db")

    # Query the data
    query = "SELECT * FROM history_test ORDER BY date;"
    df = pd.read_sql(query, engine)

    df['date'] = pd.to_datetime(df['date'])

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    axes[0, 0].plot(df['date'], df['total_uah'], label='Total UAH')
    axes[0, 0].plot(df['date'], df['total_liq_uah'], label='Total Liquid UAH')
    axes[0, 0].set_title('UAH Balances Over Time')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Amount')
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    axes[0, 1].plot(df['date'], df['total_usd'], label='Total USD')
    axes[0, 1].plot(df['date'], df['total_liq_usd'], label='Total Liquid USD')
    axes[0, 1].set_title('USD Balances Over Time')
    axes[0, 1].set_xlabel('Date')
    axes[0, 1].set_ylabel('Amount')
    axes[0, 1].legend()
    axes[0, 1].grid(True)

    axes[1, 0].plot(df['date'], df['liquid_percent'], color='green')
    axes[1, 0].set_title('Liquidity Percentage Over Time')
    axes[1, 0].set_xlabel('Date')
    axes[1, 0].set_ylabel('%')
    axes[1, 0].grid(True)

    # Fourth subplot: Interest Rate %
    axes[1, 1].plot(df['date'], df['interest_rate_percent'], color='orange')
    axes[1, 1].set_title('Interest Rate Over Time')
    axes[1, 1].set_xlabel('Date')
    axes[1, 1].set_ylabel('%')
    axes[1, 1].grid(True)

    for ax in axes.flat:
        ax.tick_params(axis='x', rotation=45)

    plt.tight_layout(pad=5.0)
    plt.show()

run()