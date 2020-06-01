from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import numpy as np

"""Output:
L1 is: 0.11100000000000002
l1 effective is  0.09318052738336714
Pockels Cell:
Optical Path Length: 1.3867 m
FSR 2.16e+02 MHz
End Radius: 0.00258392
Optical Path Length: 1.3867 m
FSR 2.16e+02 MHz
End Radius: 0.0001687
Without Pockels Cell:
Optical Path Length: 1.3272 m
FSR 2.26e+02 MHz
End Radius: 0.00279499
Optical Path Length: 1.3272 m
FSR 2.26e+02 MHz
End Radius: 0.00017194
"""


l1a = 0.033
l1b = l1a
lwindow = 0.0035
nwindow = 1.45
lpockels = 0.038
npockels = 1.7

l1 = l1a+l1b +2*lwindow +lpockels
l1effective = l1a + l1b + 2 * lwindow/nwindow + lpockels / npockels
print("L1 is:", l1)
print("l1 effective is ", l1effective)
l2 = 0.1626
l3 = 0.39
f1 = 0.012
f2 = 0.15

cavity_elements_Pcell = [
    MirrorNormal(),
    PathConstantIndex(l3),
    LensThinVac(f2),  # Edmund, query 785nm coated lenses
    PathConstantIndex(l2),  # Standard length 0.1625
    LensThinVac(f1),  # Thorlabs lens
    PathConstantIndex(l1b),
    PathConstantIndex(lwindow,nwindow),
    PathConstantIndex(lpockels,npockels),
    PathConstantIndex(lwindow,nwindow),
    PathConstantIndex(l1a),
    MirrorNormal(),
]

cavity_elements_Pcell_rev = [  
    MirrorNormal(),
    PathConstantIndex(l1a),
    PathConstantIndex(lwindow,nwindow),
    PathConstantIndex(lpockels,npockels),
    PathConstantIndex(lwindow,nwindow),
    PathConstantIndex(l1b),
    LensThinVac(f1), # Thorlabs lens 
    PathConstantIndex(l2),  # Standard length 0.1625
    LensThinVac(f2),  # Edmund, query 785nm coated lenses
    PathConstantIndex(l3),
    MirrorNormal(),
]
print("Pockels Cell:")
for elements in [cavity_elements_Pcell, cavity_elements_Pcell_rev]:
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
    OPL = 2 * (l1a + l1b + l2 + l3 + lpockels * npockels + 2 * (lwindow * nwindow))
    print("Optical Path Length: {} m".format(OPL))
    FSR = 299792452/OPL
    print("FSR {:.2e} MHz".format(FSR/1e6))
    print("End Radius:", round(GI3Cavity.end_radius(),8))
    

    
cavity_elements = [
    MirrorNormal(),
    PathConstantIndex(l3),
    LensThinVac(f2),  # Edmund, query 785nm coated lenses
    PathConstantIndex(l2),  # Standard length 0.1625
    LensThinVac(f1),  # Thorlabs lens
    PathConstantIndex(l1),
    MirrorNormal(),
]

cavity_elements_rev = [  
    MirrorNormal(),
    PathConstantIndex(l1),
    LensThinVac(f1), # Thorlabs lens 
    PathConstantIndex(l2),  # Standard length 0.1625
    LensThinVac(f2),  # Edmund, query 785nm coated lenses
    PathConstantIndex(l3),
    MirrorNormal(),
]
print("Without Pockels Cell:")
for elements in [cavity_elements, cavity_elements_rev]:
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
    OPL = 2 * (l1 + l2 + l3)
    print("Optical Path Length: {} m".format(OPL))
    FSR = 299792452/OPL
    print("FSR {:.2e} MHz".format(FSR/1e6))
    print("End Radius:", round(GI3Cavity.end_radius(),8))