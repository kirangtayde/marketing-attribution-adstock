# Marketing Attribution & Adstock Modeling

Production-style portfolio project for marketing mix modeling (MMM), channel attribution and budget optimization.

## Scope
- Adstock / carryover transformations
- Geometric and Weibull-style decay concepts
- Hill saturation transformation
- Regularized regression and channel contribution
- Incremental ROI / ROAS analysis
- Scenario-based budget allocation
- Time-series validation and leakage controls

## Architecture
`raw channel spend + outcomes -> validation -> adstock -> saturation -> regression -> contribution -> ROI -> budget scenarios`

## Data contract
Expected columns: `date`, `sales` (or conversions), and channel spend columns such as `tv`, `search`, `social`, `display`, `video`. No confidential client data is included.

## Responsible modeling
This repository is an educational/portfolio implementation. Real attribution requires controlled experiments, business context, calibrated priors and careful treatment of seasonality, trend and correlated media spend.

## Stack
Python, Pandas, NumPy, scikit-learn, statsmodels, Matplotlib, pytest.

## Structure
```text
src/adstock.py
src/saturation.py
src/model.py
src/attribution.py
src/budget.py
tests/test_transformations.py
requirements.txt
```

## Resume summary
Built a marketing attribution workflow using carryover/adstock, saturation, regularized regression, channel contribution analysis and budget-response scenarios to support data-driven media allocation.

Author: Kiran Tayde | Senior Data Scientist
