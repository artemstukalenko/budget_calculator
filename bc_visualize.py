import argparse
import ast

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--password", type=str, help="DB password")

    args = parser.parse_args()

    engine = create_engine(f"postgresql+psycopg2://postgres:{args.password}@localhost:5432/budget_calculator_db")

    # Query the data
    query = "SELECT * FROM history ORDER BY date;"
    df = pd.read_sql(query, engine)

    df['date'] = pd.to_datetime(df['date'])
    df['exposure_dict'] = df['exposure_table'].apply(ast.literal_eval)
    exposure_df = pd.DataFrame(df['exposure_dict'].to_list(), index=df['date'])

    fig_static, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig_static.canvas.manager.set_window_title("Total Figures")

    axes[0, 0].plot(df['date'], df['total_uah'], label='Total UAH')
    axes[0, 0].plot(df['date'], df['total_liq_uah'], label='Total Liquid UAH')
    axes[0, 0].set_title('UAH Balances Over Time')
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    axes[0, 1].plot(df['date'], df['total_usd'], label='Total USD')
    axes[0, 1].plot(df['date'], df['total_liq_usd'], label='Total Liquid USD')
    axes[0, 1].set_title('USD Balances Over Time')
    axes[0, 1].legend()
    axes[0, 1].grid(True)

    axes[1, 0].plot(df['date'], df['liquid_percent'], color='green')
    axes[1, 0].set_title('Liquidity Share')
    axes[1, 0].grid(True)

    # Fourth subplot: Interest Rate %
    axes[1, 1].plot(df['date'], df['interest_rate_percent'], color='orange')
    axes[1, 1].set_title('Interest Rate Share')
    axes[1, 1].grid(True)

    for ax in axes.flat:
        ax.tick_params(axis='x', rotation=45)

    fig_static.tight_layout(pad=5.0)

    ###############Exposure layout
    num_accounts = exposure_df.shape[1]
    cols = 3
    rows = (num_accounts + cols - 1) // cols  # +1 for pie chart
    fig_dynamic, axes2 = plt.subplots(rows, cols, figsize=(18, 5 * rows))
    fig_dynamic.canvas.manager.set_window_title("Allocation")
    axes2 = axes2.flatten()

    # Line charts for each account
    for i, account in enumerate(exposure_df.columns):
        axes2[i].plot(exposure_df.index, exposure_df[account], marker='o')
        axes2[i].set_title(f"Exposure to {account} in %")
        axes2[i].grid(True)

    # Hide any unused subplots
    for j in range(num_accounts, len(axes2)):
        fig_dynamic.delaxes(axes2[j])

    for ax in axes2.flat:
        ax.tick_params(axis='x', rotation=45)

    fig_dynamic.tight_layout(pad=8.0)

    #############Latest Exposure Layout
    # Pie chart for the latest record
    latest = exposure_df.iloc[-1]
    non_zero = latest[latest > 1]
    zero = latest[latest < 1]

    if not zero.empty:
        non_zero["Other (0.0%)"] = 0.0

    fig_pie, axes_pie = plt.subplots(1, 1, figsize=(14, 10))
    axes_pie.pie(non_zero, labels=non_zero.index, autopct='%1.1f%%', startangle=140)
    axes_pie.set_title("Latest Account Distribution")

    plt.show()

run()