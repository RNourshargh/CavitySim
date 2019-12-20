from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex
import numpy as np
"""A simulation of the cavities built by Jonathan Jones for the CLock group, ROC 1m, L = 0.1m , Planar"""

cavity_elements = [
        MirrorNormal(1),
        PathConstantIndex(0.1),
        MirrorNormal()
        ]
ClockCavity = Cavity(cavity_elements,True)

m = ClockCavity.ad()/2
print("Half Trace is:", m)

print( "Radii List: ", ClockCavity.radii_list())
print("End Radius: ", ClockCavity.end_radius())