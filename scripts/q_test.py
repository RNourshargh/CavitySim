from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac, abcd_transform, radius_from_q, roc_from_q
import numpy as np

l = 400e-9 # Wavelength

cavity_elements = [
        MirrorNormal(0.5),
        PathConstantIndex(0.1),
        MirrorNormal(),
]

sls = Cavity(cavity_elements ,True, l)
abcd=sls.abcd()
print(abcd)
q = sls.q_stableMode()
print(q)