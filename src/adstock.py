from __future__ import annotations
import numpy as np
import pandas as pd

def geometric_adstock(x: pd.Series, decay: float) -> pd.Series:
    if not 0 <= decay < 1: raise ValueError('decay must be in [0,1)')
    values=np.asarray(x,dtype=float); out=np.zeros(len(values));
    for i,v in enumerate(values): out[i]=v+(decay*out[i-1] if i else 0.0)
    return pd.Series(out,index=x.index,name=x.name)

def adstock_matrix(df: pd.DataFrame, channels: list[str], decay: float) -> pd.DataFrame:
    out=df.copy()
    for c in channels: out[f'{c}_adstock']=geometric_adstock(df[c],decay)
    return out
