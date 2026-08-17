# 📣 Marketing Attribution & Adstock Modeling

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![MMM](https://img.shields.io/badge/Marketing%20Mix%20Modeling-MMM-orange)
![Testing](https://img.shields.io/badge/Testing-PyTest-green)

Production-oriented portfolio implementation for **marketing mix modeling (MMM), channel attribution, media carryover and budget-response analysis**.

## 👨‍💻 Author

**Kiran Tayde — Senior Data Scientist | Marketing Analytics | Machine Learning | Predictive Modeling**

GitHub: https://github.com/kirangtayde

## 🎯 Objective

Estimate the relationship between marketing investment and business outcomes while accounting for **carryover, saturation, seasonality and correlated media channels**.

## 🔬 Core Capabilities

- Geometric adstock / media carryover
- Weibull-style decay concepts
- Hill saturation transformation
- Regularized regression
- Channel contribution estimation
- Incremental ROI / ROAS analysis
- Scenario-based budget allocation
- Time-series validation
- Leakage and correlation controls

## 🧩 Architecture

```text
Channel Spend + Outcomes
          ↓
Data Validation
          ↓
Adstock / Carryover
          ↓
Saturation
          ↓
Regression / MMM
          ↓
Channel Contribution
          ↓
ROI / ROAS
          ↓
Budget Scenarios
```

## 📐 Modeling Concepts

**Adstock:** captures delayed media impact.

**Saturation:** captures diminishing returns as spend increases.

**Contribution:** estimates the modeled incremental contribution of each channel.

**Scenario Planning:** evaluates alternative media allocations under business constraints.

## 📊 Data Contract

Expected columns include `date`, `sales` or `conversions`, and channel spend such as `tv`, `search`, `social`, `display` and `video`.

No confidential client data is included.

## ⚠️ Responsible Modeling

This is an educational/portfolio implementation. Real-world attribution should be validated with controlled experiments where possible and should carefully address seasonality, trend, pricing, promotions, correlated media spend and business context.

## 🛠️ Stack

Python • Pandas • NumPy • scikit-learn • statsmodels • Matplotlib • PyTest

## 📁 Structure

```text
src/
├── adstock.py
├── saturation.py
├── model.py
├── attribution.py
└── budget.py

tests/
└── test_transformations.py

requirements.txt
README.md
```

## 🚀 Quick Start

```bash
git clone https://github.com/kirangtayde/marketing-attribution-adstock.git
cd marketing-attribution-adstock
python -m venv .venv
pip install -r requirements.txt
pytest -q
```

## 📌 Resume Summary

**Marketing Attribution & Adstock Modeling | Python, MMM, Statistics** — Built a marketing attribution workflow using media carryover, saturation, regularized regression, channel contribution analysis and budget-response scenarios to support data-driven media allocation.

## 🔗 Connect

**Kiran Tayde** · Senior Data Scientist · Marketing Analytics · Machine Learning

https://github.com/kirangtayde