from __future__ import annotations
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def fit_mmm(X: pd.DataFrame, y, alpha: float = 1.0):
    model=Pipeline([('scale',StandardScaler()),('ridge',Ridge(alpha=alpha))])
    model.fit(X,y)
    return model

def channel_contribution(model, X: pd.DataFrame) -> pd.Series:
    ridge=model.named_steps['ridge']
    return pd.Series(ridge.coef_,index=X.columns,name='coefficient').sort_values(ascending=False)
