from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import numpy as np


#"""THe following setup produces a 6mm beam diameter and is hopefully less scary"""
#cavity_elements_2 = [
#        mirror_normal(),
#        path_constant_index(0.4),
#        lens_thin_vac(0.15), #Edmund, query 785nm coated lenses
#        path_constant_index(0.1625),
#        lens_thin_vac(0.012), #Thorlabs lens
#        path_constant_index(0.11),
#        mirror_normal()
#]

"""THe following setup is reversed to see the small mode produces a 6mm beam diameter and is hopefully less scary"""
cavity_elements = [
        MirrorNormal(),
        PathConstantIndex(0.4),
        LensThinVac(0.15), #Edmund, query 785nm coated lenses
        PathConstantIndex(0.1625),# Standard length 0.1625
        LensThinVac(0.012), #Thorlabs lens
        PathConstantIndex(0.11), #Standard length 0.11
        MirrorNormal()
]

GI3Cavity = Cavity(cavity_elements, True)

m = GI3Cavity.ad()/2
print("Half Trace is:", m)

EigenA = m + np.sqrt(m**2-1+0j)
EigenB = m - np.sqrt(m**2-1+0j)

Theta = np.arccos(m)

print("For m=0 Theta:", np.arccos(0)/np.pi, "pi")

print("Theta:", Theta)

print("EigenA:", EigenA)
print("EigenB", EigenB)

print(GI3Cavity.end_radius())
