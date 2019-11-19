from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import numpy as np




cavity_elements = [
        MirrorNormal(),
        PathConstantIndex(0.4),
        LensThinVac(0.15), #Edmund, query 785nm coated lenses
        PathConstantIndex(0.1625),# Standard length 0.1625
        LensThinVac(0.012), #Thorlabs lens
        PathConstantIndex(0.18), #Standard length 0.11
        MirrorNormal()
]

reversed_cavity_elements = [
        MirrorNormal(),
        PathConstantIndex(0.18), #Standard length 0.11
        LensThinVac(0.012), #Thorlabs lens
        PathConstantIndex(0.1625),# Standard length 0.1625
        LensThinVac(0.15), #Edmund, query 785nm coated lenses
        PathConstantIndex(0.4),
        MirrorNormal()
]


GI3Cavity = Cavity(cavity_elements, True)
GI3CavityReversed = Cavity(reversed_cavity_elements, True)

CavityInputRadius = GI3CavityReversed.end_radius()

print( GI3Cavity.radii_list())


print("Cavity Input radius is:", CavityInputRadius)

FibreOutRadius = 0.00043

LensFocalLength = (np.pi*CavityInputRadius**2)/(780e-9) * np.sqrt((FibreOutRadius/CavityInputRadius)**2-1)
print("Lens Focal Length:", LensFocalLength)


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
