import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import setup_directories, set_plot_style, save_plot


def calculate_metrics(returns_df):
    metrics = {}
    T = len(returns_df)
    for col in returns_df.columns:
        r = returns_df[col]
        cum_ret = np.exp(r.cumsum())

        # 1. Geometric Return (CAGR) for the performance table display
        ann_ret_cagr = (cum_ret.iloc[-1])**(252 / T) - 1

        # 2. Arithmetic Return for the theoretical Sharpe calculation
        ann_ret_arithmetic = r.mean() * 252 

        ann_vol = r.std() * np.sqrt(252)

        # 3. Calculate Sharpe using Arithmetic Mean
        sharpe = ann_ret_arithmetic / ann_vol if ann_vol > 0 else 0

        max_dd = (cum_ret / cum_ret.cummax() - 1).min()
        abs_ret = (cum_ret.iloc[-1] - 1)

        metrics[col] = {
            "Ann. Return": ann_ret_cagr,
            "Ann. Vol": ann_vol,
            "Sharpe": sharpe,
            "Max Drawdown": max_dd,
            "Total Return": abs_ret,
        }
    return pd.DataFrame(metrics)


def main():
    setup_directories()
    set_plot_style()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    ret_df = pd.read_csv(os.path.join(DATA_DIR, "backtest_returns.csv"), index_col=0, parse_dates=True)

    metrics = calculate_metrics(ret_df)
    print(metrics.to_string())
    print()

    cum_wealth = (1 + ret_df).cumprod()

    # Plot cumulative wealth
    fig, ax = plt.subplots(figsize=(10, 6))
    cum_wealth.drop(columns=['Classical MV'], errors='ignore').plot(ax=ax)
    ax.set_title("Cumulative Wealth")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Wealth")
    save_plot(fig, "cumulative_wealth.png")

    metrics.to_csv(os.path.join(DATA_DIR, "performance_metrics.csv"))
    cum_wealth.to_csv(os.path.join(DATA_DIR, "cumulative_wealth.csv"))


if __name__ == "__main__":
    main()
