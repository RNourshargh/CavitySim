import numpy as np


from cavitysim.utils import legacy_path_constant_index, rayleigh_range_w0, radius_from_q, legacy_lens_thin_vacuum_abcd, legacy_mirror_planar_normal, abcd_stability, lens_thin_vac, path_constant_index, mirror_normal, cavity

def test_cavity():
    test_inputs = [([mirror_normal(0.2),path_constant_index(0.1),mirror_normal(0.2)],True),([mirror_normal(), path_constant_index(0.3), lens_thin_vac(0.2),path_constant_index(0.3),mirror_normal()],True),([mirror_normal(5),path_constant_index(0.3),mirror_normal(),path_constant_index(0.2),mirror_normal(),path_constant_index(0.3)],False)]
    
    """Test abcd matrix generation"""
    expected_abcds =[np.array([[0,0.1],[-10,-1]]),np.array([[-0.5,-0.15],[5,-0.5]]),np.array([[1,0.8],[-0.4,0.68]])]
    
    """Test abcd trace function"""
    expected_ads = [-1, -1, 1.68]
    
    """Test stable method"""
    expected_stability = [True, True, True]
    
    result_abcds =[]
    result_ads = []
    result_stability = []
    
    for cavity_input in test_inputs:
        result_abcds.append(cavity(cavity_input[0],cavity_input[1]).abcd())
        result_ads.append(cavity(cavity_input[0],cavity_input[1]).ad())
        result_stability.append(cavity(cavity_input[0],cavity_input[1]).stable())
        
    np.testing.assert_allclose(expected_abcds,result_abcds)
    np.testing.assert_allclose(expected_ads,result_ads)
    np.testing.assert_allclose(expected_stability,result_stability)
    

def test_pathconstantindex():
    test_path_length = 5.0
    test_n0 = 1.5
    
    expected_acbd = np.array([[1,test_path_length],[0,1]])
    expected_opl = test_n0*test_path_length
    
    result_path = path_constant_index(test_path_length,test_n0)
    result_abcd = result_path.abcd()
    result_opl = result_path.opl()
    
    np.testing.assert_allclose(expected_acbd,result_abcd)
    assert expected_opl == result_opl

def test_mirrornormal():
    test_rocs = [0.1,np.inf]
    
    expected_abcds = [np.array([[1,0],[-20,1]]),np.array([[1,0],[0,1]])]
    expected_opls  = [0,0]
    
    result_abcds = []
    result_opls = []
    
    for roc in test_rocs:
        mirror = mirror_normal(roc)
        result_abcds.append(mirror.abcd())
        result_opls.append(mirror.opl())
        
    np.testing.assert_allclose(expected_abcds,result_abcds)
    assert expected_opls == result_opls



def test_legacypathconstantindex():
    test_path_length = 7.0
    test_n0 = 1.1

    expected_abcd = np.array([[1, test_path_length], [0, 1]])
    expected_opl =  test_path_length*test_n0
    
    result_abcd, result_opl = legacy_path_constant_index(test_path_length, test_n0)

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
    
def test_legacylensthinvac():
    test_f = 0.1
    
    expected_abcd= np.matrix([[1,0],[-10,1]])
    expected_opl = 0   
    
    result_abcd,result_opl = legacy_lens_thin_vacuum_abcd(test_f)
    
    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl

def test_legacymirrorplanarnorm():
    expected_abcd= np.matrix([[1,0],[0,1]])
    expected_opl = 0   
    
    result_abcd,result_opl = legacy_mirror_planar_normal()
    
    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl    

def test_abcdstability():
    test_abcds = [np.matrix([[-0.3,13],[-0.07,-0.3]]), np.matrix([[1.3,13],[-0.07,1.5]]),np.matrix([[-1.3,13],[-0.07,-1.8]])]
    expected_results = [-0.6, True, 2.8, False,-3.1,False]
    
    test_results = []
    for matrix in test_abcds:
        test_results += abcd_stability(matrix)
        
    assert test_results == expected_results    

def test_classlensthinvac():
    test_lensthinvac50mm = lens_thin_vac(50e-3)
    
    expected_abcd= np.matrix([[1,0],[-20,1]])
    expected_opl = 0
    
    result_abcd = test_lensthinvac50mm.abcd()
    result_opl = test_lensthinvac50mm.opl()
    
    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl
    
test_cavity()
test_wavelength = 780E-9
