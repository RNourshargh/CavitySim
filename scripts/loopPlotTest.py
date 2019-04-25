from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import matplotlib.pyplot as plt
import numpy as np


for length1 in np.linspace(0.05, 0.15, num=10):


    cavity_elements_2 = [
            MirrorNormal(),
            PathConstantIndex(0.4),
            LensThinVac(0.15), #Edmund, query 785nm coated lenses
            PathConstantIndex(0.1625),
            LensThinVac(0.012), #Thorlabs lens
            PathConstantIndex(length1), #Standard length 11
            MirrorNormal()
        ]
        
    CavityIteration = Cavity(cavity_elements_2,True)
    
    print("ad = ", CavityIteration.ad())
    print("end_rad =", CavityIteration.end_radius())
    