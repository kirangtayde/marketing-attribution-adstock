from __future__ import annotations
import pandas as pd

def scenario_table(current: pd.Series, change_grid=(-0.2,-0.1,0,0.1,0.2)) -> pd.DataFrame:
    rows=[]
    for change in change_grid:
        allocation=(current*(1+change)).clip(lower=0)
        rows.append({'scenario_change':change,'total_budget':float(allocation.sum()),**allocation.to_dict()})
    return pd.DataFrame(rows)
