import numpy as np

from src.transforms import geometric_adstock, hill_saturation


def test_geometric_adstock_captures_carryover():
    result = geometric_adstock(np.array([1.0, 0.0, 0.0]), decay=0.5)
    assert np.allclose(result, [1.0, 0.5, 0.25])


def test_hill_saturation_is_bounded():
    result = hill_saturation(np.array([0.0, 10.0, 100.0]), half_saturation=10)
    assert np.all(result >= 0)
    assert np.all(result <= 1)
