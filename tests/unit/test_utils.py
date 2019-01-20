import numpy as np


from cavitysim.utils import pathfreespace


def test_pathfreespace():
    test_pathlength = 7.0
    test_n0 = 1.1

    expected = (np.array([[1, test_pathlength], [0, 1]]), test_pathlength*test_n0)
    result = pathfreespace(test_pathlength, test_n0)

    assert expected == result
