from __future__ import annotations
import numpy as np

def hill_saturation(x, alpha: float = 1.0, gamma: float = 1.0):
    x=np.maximum(np.asarray(x,dtype=float),0)
    if alpha <= 0 or gamma <= 0: raise ValueError('alpha and gamma must be positive')
    return np.power(x,alpha)/(np.power(x,alpha)+np.power(gamma,alpha)+1e-12)

def log_saturation(x): return np.log1p(np.maximum(np.asarray(x,dtype=float),0))
