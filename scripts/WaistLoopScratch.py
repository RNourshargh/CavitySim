from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac

import numpy as np



CAVITY_SETUP = [
    MirrorNormal(5),
    PathConstantIndex(0.40756),
    MirrorNormal()
]

        
excav = Cavity(CAVITY_SETUP, True)



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

result_radiilist = []

expected_radii_lists = [
    [0.00016931952799938106, 0.00016931952799938106, 0.00016931952799938106, 0.00016931952799938106],
    [0.0002073732235436865, 0.0002073732235436865, 0.000414746447087373, 0.000414746447087373, 0.0002073732235436865, 0.0002073732235436865, 0.000414746447087373, 0.000414746447087373],
    [0.0006050383556457971, 0.000605038355645797, 0.0005819072571444502, 0.0005819072571444502, 0.0005819072571444503, 0.0005819072571444503],
    ]

    
for Cavity_input in test_inputs[:-1]:
    test_cav = Cavity(Cavity_input[0], Cavity_input[1])
    iteration_radii_list = test_cav.radii_list()
    #print(iteration_radii_list)
    
    result_radiilist.append(iteration_radii_list)
#print(result_radiilist)
    
    
    


np.testing.assert_allclose(expected_radii_lists, result_radiilist, rtol=1e-7, atol=1e-10, equal_nan=True)
       


# for Cavity_input in test_inputs[:-1]:
        # test_cav = Cavity(Cavity_input[0], Cavity_input[1])
        # print(test_cav.radii_list())
        # print(" ")       
        
        #print(excav.abcd())

#print(excav.abcd_shift())

#print( excav.radii_list())

#print("Cavity elements: {}".format(excav.elements))
#print("Shifted elements: {}".format(excav.ElementShift()))
#print("Cavity setup: {}".format(CAVITY_SETUP))

#print("ABCD is: {}".format(excav.abcd()))
#print("AD is: {}".format(excav.ad()))
#excav.properties()
#print(excav.end_radius())
#print(excav.ad()/2)
