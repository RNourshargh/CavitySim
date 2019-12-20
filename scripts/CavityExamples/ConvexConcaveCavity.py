from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex
import numpy as np
"""A simulation of a convexconcave cavity, ROC 3m, L = 1m , ROC -2m"""

cavity_elements = [
        MirrorNormal(3),
        PathConstantIndex(1.1),
        MirrorNormal(-2)
        ]
Cavity = Cavity(cavity_elements,True)

m = Cavity.ad()/2
print("Half Trace is:", m)

print( "Radii List: ", Cavity.radii_list())
print("End Radius: ", Cavity.end_radius())