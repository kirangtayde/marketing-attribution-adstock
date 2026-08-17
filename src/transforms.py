from __future__ import annotations

import numpy as np


def geometric_adstock(values: np.ndarray, decay: float) -> np.ndarray:
    """Apply geometric media carryover without leaking future observations."""
    if not 0 <= decay < 1:
        raise ValueError("decay must be in [0, 1)")
    x = np.asarray(values, dtype=float)
    if x.ndim != 1:
        raise ValueError("values must be one-dimensional")
    result = np.zeros_like(x)
    for i, value in enumerate(x):
        result[i] = value if i == 0 else value + decay * result[i - 1]
    return result


def hill_saturation(values: np.ndarray, half_saturation: float, slope: float = 1.0) -> np.ndarray:
    """Model diminishing returns using a Hill transformation."""
    if half_saturation <= 0 or slope <= 0:
        raise ValueError("half_saturation and slope must be positive")
    x = np.maximum(np.asarray(values, dtype=float), 0)
    return np.power(x, slope) / (np.power(x, slope) + half_saturation**slope)
