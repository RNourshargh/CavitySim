from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import numpy as np


cavity_elements = [
    MirrorNormal(),
    PathConstantIndex(0.4),
    LensThinVac(0.15),  # Edmund, query 785nm coated lenses
    PathConstantIndex(0.1625),  # Standard length 0.1625
    LensThinVac(0.012),  # Thorlabs lens
    PathConstantIndex(0.05),  
    PathConstantIndex(0.05,1.7),
    PathConstantIndex(0.05),
    MirrorNormal(),
]


GI3Cavity = Cavity(cavity_elements, True)
print("ABCD:", GI3Cavity.abcd())

print( GI3Cavity.radii_list())

m = GI3Cavity.ad()/2
print("Half Trace is:", m)

EigenA = m + np.sqrt(m**2-1+0j)
EigenB = m - np.sqrt(m**2-1+0j)

Theta = np.arccos(m)

print("For m=0 Theta:", np.arccos(0)/np.pi, "pi")

print("Theta:", Theta)

print("EigenA:", EigenA)
print("EigenB", EigenB)

print("End Radius:", GI3Cavity.end_radius())
