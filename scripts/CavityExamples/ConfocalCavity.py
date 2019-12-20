from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex
import numpy as np
"""A simulation of a confocal cavity, ROC 1m, L = 0.99m , PROC 1m"""

cavity_elements = [
        MirrorNormal(1),
        PathConstantIndex(0.99),
        MirrorNormal(1)
        ]
ConfocalCavity = Cavity(cavity_elements,True)

m = ConfocalCavity.ad()/2
print("Half Trace is:", m)

print( "Radii List: ", ConfocalCavity.radii_list())
print("End Radius: ", ConfocalCavity.end_radius())