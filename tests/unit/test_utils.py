import numpy as np


from cavitysim.utils import (
    legacy_path_constant_index,
    rayleigh_range_w0,
    radius_from_abcd,
    radius_from_q,
    legacy_lens_thin_vacuum_abcd,
    legacy_mirror_planar_normal,
    abcd_stability,
    LensThinVac,
    PathConstantIndex,
    MirrorNormal,
    Cavity,
)


def test_Cavity():
    test_inputs = [
        ([MirrorNormal(0.2), PathConstantIndex(0.1), MirrorNormal(0.2)], True),
        (
            [
                MirrorNormal(),
                PathConstantIndex(0.3),
                LensThinVac(0.2),
                PathConstantIndex(0.3),
                MirrorNormal(),
            ],
            True,
        ),
        (
            [
                MirrorNormal(5),
                PathConstantIndex(0.3),
                MirrorNormal(),
                PathConstantIndex(0.2),
                MirrorNormal(),
                PathConstantIndex(0.3),
            ],
            False,
        ),
        ([MirrorNormal(-0.2), PathConstantIndex(0.2), MirrorNormal()], True),
    ]

    # Test abcd matrix generation
    expected_abcds = [
        np.array([[0, 0.1], [-10, -1]]),
        np.array([[-0.5, -0.15], [5, -0.5]]),
        np.array([[1, 0.8], [-0.4, 0.68]]),
        np.array([[1, 0.4], [10, 5]]),
    ]

    # Test shifted abcds
    expected_shiftabcds2 = [
    np.array([[  0. ,   0.1],[-10. ,  -1. ]]),
    np.array([[-2. , -0.6],[ 5. ,  1. ]]),
    np.array([[ 0.8 ,  0.74],[-0.4 ,  0.88]]), 
    np.array([[ 3. ,  0.8],[10. ,  3. ]]),
    ]

    expected_shiftabcds3 = [
    np.array([[ -1. ,   0.1],[-10. ,   0. ]]), 
    np.array([[ 1. , -0.6],[ 5. , -2. ]]), 
    np.array([[ 0.8 ,  0.74],[-0.4 ,  0.88]]),
    np.array([[ 3. ,  0.8],[10. ,  3. ]]),
    ]

    
    # Test abcd trace function
    expected_ads = [-1, -1, 1.68, 6]

    # Test stable method
    expected_stability = [True, True, True, False]
    
    # Test end_radius method
    expected_endradii = [
        0.00016931952799938106,
        0.0002073732235436865,
        0.0006050383556457971,
        np.nan,
    ]

    result_abcds = []
    result_shiftedabcds2 = []
    result_shiftedabcds3 = []
    result_ads = []
    result_stability = []
    result_endradii = []
    

    for Cavity_input in test_inputs:
        test_cav = Cavity(Cavity_input[0], Cavity_input[1])
        result_abcds.append(test_cav.abcd())
        result_ads.append(test_cav.ad())
        result_stability.append(test_cav.stable())
        result_endradii.append(test_cav.end_radius())
        result_shiftedabcds2.append(test_cav.abcd_shift(n=2))
        result_shiftedabcds3.append(test_cav.abcd_shift(n=3))
        test_cav.properties()

    np.testing.assert_allclose(expected_abcds, result_abcds, rtol=1e-7, atol=1e-10)
    np.testing.assert_allclose(expected_shiftabcds2, result_shiftedabcds2, rtol=1e-7, atol=1e-10)
    np.testing.assert_allclose(expected_shiftabcds3, result_shiftedabcds3, rtol=1e-7, atol=1e-10)
    np.testing.assert_allclose(expected_ads, result_ads)
    np.testing.assert_allclose(expected_stability, result_stability)
    np.testing.assert_allclose(
        expected_endradii, result_endradii, rtol=1e-7, atol=1e-10, equal_nan=True
    )
        
    #Test reindex function
    
    test_reindex1 = Cavity.reindex([0,1,2,3], n=2)
    test_reindex2 = Cavity.reindex([2,5,7,8,9],n=3)
    expected_reindexout1 = [2,3,0,1]
    expected_reindexout2 = [9,2,5,7,8]
    np.testing.assert_allclose(expected_reindexout1,  test_reindex1)
    np.testing.assert_allclose(expected_reindexout2,  test_reindex2)
    


def test_pathconstantindex():
    test_path_length = 5.0
    test_n0 = 1.5

    expected_acbd = np.array([[1, test_path_length], [0, 1]])
    expected_opl = test_n0 * test_path_length

    result_path = PathConstantIndex(test_path_length, test_n0)
    result_abcd = result_path.abcd()
    result_opl = result_path.opl()

    np.testing.assert_allclose(expected_acbd, result_abcd)
    assert expected_opl == result_opl


def test_mirrornormal():
    test_rocs = [0.1, np.inf]

    expected_abcds = [np.array([[1, 0], [-20, 1]]), np.array([[1, 0], [0, 1]])]
    expected_opls = [0, 0]

    result_abcds = []
    result_opls = []

    for roc in test_rocs:
        mirror = MirrorNormal(roc)
        result_abcds.append(mirror.abcd())
        result_opls.append(mirror.opl())

    np.testing.assert_allclose(expected_abcds, result_abcds)
    assert expected_opls == result_opls


def test_legacypathconstantindex():
    test_path_length = 7.0
    test_n0 = 1.1

    expected_abcd = np.array([[1, test_path_length], [0, 1]])
    expected_opl = test_path_length * test_n0

    result_abcd, result_opl = legacy_path_constant_index(test_path_length, test_n0)

    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl


def test_rayleighrangew0():
    test_w0 = 500e-6

    expected_rayleigh_range = np.pi * test_w0 ** 2 / test_wavelength
    result_rayleigh_range = rayleigh_range_w0(test_w0)

    assert expected_rayleigh_range == result_rayleigh_range

def test_radiusfromabcd():
     #test values
    test_wavelength = 780e-9
    test_abcds = [
        np.array([[0, 0.1], [-10, -1]]),
        np.array([[-0.5, -0.15], [5, -0.5]]),
        np.array([[1, 0.8], [-0.4, 0.68]]),
        np.array([[1, 0.4], [10, 5]])
    ]
    expected_endradii = [
        0.00016931952799938106,
        0.0002073732235436865,
        0.0006050383556457971,
        np.nan
    ]
    result_radii =[]
    
    for abcd in test_abcds:
        result_radii.append(radius_from_abcd(abcd, test_wavelength))
    np.testing.assert_allclose(expected_endradii, result_radii)
    
    
    
def test_radiusfromq():
    test_q = 0.5 + 1j * np.pi * (0.1e-3) ** 2 / test_wavelength

    expected_beam_radius = 0.001245429726319377
    result_beam_radius = radius_from_q(test_q)
    np.testing.assert_allclose(expected_beam_radius, result_beam_radius)


def test_legacylensthinvac():
    test_f = 0.1

    expected_abcd = np.array([[1, 0], [-10, 1]])
    expected_opl = 0

    result_abcd, result_opl = legacy_lens_thin_vacuum_abcd(test_f)

    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl


def test_legacymirrorplanarnorm():
    expected_abcd = np.array([[1, 0], [0, 1]])
    expected_opl = 0

    result_abcd, result_opl = legacy_mirror_planar_normal()

    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl


def test_abcdstability():
    test_abcds = [
        np.array([[-0.3, 13], [-0.07, -0.3]]),
        np.array([[1.3, 13], [-0.07, 1.5]]),
        np.array([[-1.3, 13], [-0.07, -1.8]]),
    ]
    expected_results = [-0.6, True, 2.8, False, -3.1, False]

    test_results = []
    for matrix in test_abcds:
        test_results += abcd_stability(matrix)

    assert test_results == expected_results


def test_classlensthinvac():
    test_lensthinvac50mm = LensThinVac(50e-3)

    expected_abcd = np.array([[1, 0], [-20, 1]])
    expected_opl = 0

    result_abcd = test_lensthinvac50mm.abcd()
    result_opl = test_lensthinvac50mm.opl()

    np.testing.assert_allclose(expected_abcd, result_abcd)
    assert expected_opl == result_opl


test_wavelength = 780e-9
