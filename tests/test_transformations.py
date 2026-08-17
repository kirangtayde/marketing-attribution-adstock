import pandas as pd
from src.adstock import geometric_adstock
from src.saturation import hill_saturation

def test_adstock():
    out=geometric_adstock(pd.Series([1,0,0]),0.5)
    assert list(out.round(3)) == [1.0,0.5,0.25]

def test_hill_bounds():
    y=hill_saturation([0,1,10],alpha=1,gamma=1)
    assert y[0] == 0 and y[-1] < 1
