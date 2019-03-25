import numpy as np


from cavitysim.utils import path_free_space, rayleigh_range_w0


def test_pathfreespace():
    test_path_length = 7.0
    test_n0 = 1.1

    expected_abcd = np.array([[1, test_path_length], [0, 1]])
    expected_opl =  test_path_length*test_n0
    result_abcd, result_opl = path_free_space(test_path_length, test_n0)

    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl

def test_rayleighrangew0():
    test_w0 = 500E-6
    
    expected_rayleigh_range = np.pi*test_w0**2/wavelength
    result_rayleigh_range = rayleigh_range_w0(test_w0)
    
    np.testing.assert_allclose(expected_rayleigh_range, result_rayleigh_range)
    assert expected_rayleigh_range == result_rayleigh_range

wavelength = 780E-9