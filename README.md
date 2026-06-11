# Bayesian Portfolio Selection via the Black-Litterman Model with Cross-Sectional Momentum Views

This repository contains the empirical implementation of a portfolio optimization strategy that integrates **Cross-Sectional Momentum** views into the **Black-Litterman (BL)** Bayesian framework. It evaluates the framework across a universe of ten developed-market equity indices over a 16-year period (2010–2026).

## 📖 Overview

Modern portfolio theory often struggles with sensitivity to estimation error in expected returns. This project implements the **Black-Litterman (BL)** model to address this by combining:
1. **Market-Implied Returns:** Derived via the Capital Asset Pricing Model (CAPM) and market capitalization weights.
2. **Investor Views:** Cross-Sectional Momentum views weighted by conviction (trend-quality).

By utilizing a rolling 252-day window for covariance and a 189-day lookback for momentum, the resulting **BL Momentum** portfolio dramatically improves risk-adjusted returns and mitigates maximum drawdowns compared to standard market-cap or naive equal-weight allocations.

## ✨ Key Findings

- **Structural Rescue:** The Black-Litterman model successfully saves the portfolio from the devastating estimation errors that cripple traditional Mean-Variance Optimization (MVO).
- **Momentum Alpha:** A composite $R^2$ signal evaluating both trend magnitude and smoothness systematically injects statistically significant alpha.
- **Concentrated Long-Only:** Instead of traditional market-neutral long-short spreads (which fight the equity risk premium), this approach uses an unconstrained long-only vector targeting the top 2 momentum performers.
- **Superior Performance:** Outperforms Market Cap weighting by +3.63 percentage points annually (14.26% vs 10.63%) and practically doubles the cumulative return.

## 📊 Dataset

Daily closing prices for 10 Exchange-Traded Funds (ETFs) representing global developed market equity indices:
- `SPY` (US), `EWU` (UK), `EWJ` (Japan), `EWG` (Germany), `EWQ` (France)
- `EWC` (Canada), `EWL` (Switzerland), `EWA` (Australia), `EWN` (Netherlands), `EWD` (Sweden)

**Sample Period:** January 2010 to April 2026

## ⚙️ Installation

Ensure you have Python 3.8+ installed. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

The project is structured as a pipeline. To execute the entire backtest, simply run:

```bash
python main.py
```

Alternatively, you can run the modules sequentially:
1. `01_download_data.py`: Fetches ETF price data.
2. `02_descriptive_stats.py`: Computes historical risk-return metrics.
3. `03_equilibrium_returns.py`: Derives CAPM-based prior expectations.
4. `04_momentum_views.py`: Calculates cross-sectional momentum and trend-quality $R^2$.
5. `05_black_litterman.py`: Computes the posterior expected returns via Bayesian updating.
6. `06_backtest.py`: Runs the out-of-sample portfolio simulations.
7. `07_analysis.py`: Generates performance metrics, correlation matrices, and cumulative wealth plots.

## 📜 Contributors

- Shaondeep Mandal
- Abhishek Chhawai
- Devesh Choudhury
- Sanket Agarwal
*(Indian Institute of Technology Kanpur)*
