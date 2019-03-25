import numpy as np


from cavitysim.utils import path_free_space, rayleigh_range_w0, radius_from_q, lens_thin_vacuum_abcd, mirror_planar_normal


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
    
    expected_rayleigh_range = np.pi*test_w0**2/test_wavelength
    result_rayleigh_range = rayleigh_range_w0(test_w0)
    
    assert expected_rayleigh_range == result_rayleigh_range

def test_radiusfromq():
    test_q=0.5  +   1j*np.pi*(0.1e-3)**2/test_wavelength
    
    expected_beam_radius = 0.001245429726319377
    result_beam_radius = radius_from_q(test_q)
    np.testing.assert_allclose(expected_beam_radius, result_beam_radius)
    
def test_lensthinvac():
    test_f = 0.1
    
    expected_abcd= np.matrix([[1,0],[-10,1]])
    expected_opl = 0   
    
    result_abcd,result_opl = lens_thin_vacuum_abcd(test_f)
    
    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl

def test_mirrorplanarnorm():
    expected_abcd= np.matrix([[1,0],[0,1]])
    expected_opl = 0   
    
    result_abcd,result_opl = mirror_planar_normal()
    
    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl    

test_wavelength = 780E-9