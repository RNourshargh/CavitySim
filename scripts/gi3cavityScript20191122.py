from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import numpy as np


cavity_elements = [
    MirrorNormal(),
    PathConstantIndex(0.4),
    LensThinVac(0.15),  # Edmund, query 785nm coated lenses
    PathConstantIndex(0.1625),  # Standard length 0.1625
    LensThinVac(0.012),  # Thorlabs lens
    PathConstantIndex(0.125),
    MirrorNormal(),
]

cavity_elements_rev = [  
    MirrorNormal(),
    PathConstantIndex(0.125),
    LensThinVac(0.012), # Thorlabs lens 
    PathConstantIndex(0.1625),  # Standard length 0.1625
    LensThinVac(0.15),  # Edmund, query 785nm coated lenses
    PathConstantIndex(0.4),
    MirrorNormal(),
]

cavity_elements_Pcell = [
    MirrorNormal(),
    PathConstantIndex(0.4),
    LensThinVac(0.15),  # Edmund, query 785nm coated lenses
    PathConstantIndex(0.1625),  # Standard length 0.1625
    LensThinVac(0.012),  # Thorlabs lens
    PathConstantIndex(0.04),
    PathConstantIndex(0.0035,1.45),
    PathConstantIndex(0.038,1.7),
    PathConstantIndex(0.0035,1.45),
    PathConstantIndex(0.04),
    MirrorNormal(),
]

cavity_elements_Pcell_rev = [  
    MirrorNormal(),
    PathConstantIndex(0.04),
    PathConstantIndex(0.0035,1.45),
    PathConstantIndex(0.038,1.7),
    PathConstantIndex(0.0035,1.45),
    PathConstantIndex(0.04),
    LensThinVac(0.012), # Thorlabs lens 
    PathConstantIndex(0.1625),  # Standard length 0.1625
    LensThinVac(0.15),  # Edmund, query 785nm coated lenses
    PathConstantIndex(0.4),
    MirrorNormal(),
]

for elements in [cavity_elements, cavity_elements_rev, cavity_elements_Pcell, cavity_elements_Pcell_rev]:
    GI3Cavity = Cavity(elements, True)
    # print("ABCD:", GI3Cavity.abcd())

    # print("Radii List:", GI3Cavity.radii_list())

    # m = GI3Cavity.ad()/2
    # print("Half Trace is:", m)

    # EigenA = m + np.sqrt(m**2-1+0j)
    # EigenB = m - np.sqrt(m**2-1+0j)

    # Theta = np.arccos(m)

    # print("For m=0 Theta:", np.arccos(0)/np.pi, "pi")

    # print("Theta:", Theta)

    # print("EigenA:", EigenA)
    # print("EigenB", EigenB)

    print("End Diameter:", round(GI3Cavity.end_radius()*2,8))
