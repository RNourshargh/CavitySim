
from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

#Generate lists for the lengths to be scanned
path1 = np.linspace(0.05, 0.15, num = 300)
path2 = np.linspace(0.161, 0.166, num = 300)

#Generate results arrays of the correct size 
ad = 5*np.ones((len(path1),len(path2)))
end_radii =  10*np.ones((len(path1),len(path2)))

for i, l1 in enumerate(path1):
    for j, l2 in enumerate(path2):
        cavity_elements = [
            MirrorNormal(),
            PathConstantIndex(0.4),
            LensThinVac(0.15), #Edmund, query 785nm coated lenses
            PathConstantIndex(l2),# Standard length 0.1625
            LensThinVac(0.012), #Thorlabs lens
            PathConstantIndex(l1), #Standard length 0.11
            MirrorNormal()
        ]
        CavityIteration = Cavity(cavity_elements,True)
        ad[i,j] = CavityIteration.ad()
        end_radii[i,j] = CavityIteration.end_radius()
	
print(ad)
print(end_radii)
ad = ad[ :-1, :-1]
end_radii = end_radii[ :-1, :-1]


"""Generates single plot Radius"""
fig = plt.figure(figsize=(10.0, 7.0))
axes1 = fig.add_subplot(1, 1, 1)
axes1.set_title('Large Beam radius against optic spacings L1 and L2')
axes1.set_ylabel('L2: Telescope eyepiece to end mirror (metres)')
axes1.set_xlabel('L1: Telescope Spacing (metres)')
subplot1=axes1.pcolormesh(path2,path1,end_radii, vmin=0.002, vmax = 0.005)
fig.colorbar(subplot1,ax=axes1)
fig.tight_layout()
plt.show()


"""Generates double plot, Radius and stability"""
fig = plt.figure(figsize=(7.0, 7.0))
axes1 = fig.add_subplot(2, 1, 1)
axes1.set_title('A+D')
axes1.set_ylabel('L2 (metres)')
axes1.set_xlabel('L1: Telescope Spacing (metres)')
subplot1=axes1.pcolormesh(path2,path1,ad, vmin=-2, vmax=2)

axes2 = fig.add_subplot(2, 1, 2)
axes2.set_title('Large Beam radius against optic spacings L1 and L2')
axes2.set_ylabel('L2: Telescope eyepiece to end mirror (metres)')
axes2.set_xlabel('L1: Telescope Spacing (metres)')
subplot2=axes2.pcolormesh(path2,path1,end_radii, vmin=0.002, vmax = 0.005)

fig.colorbar(subplot1, ax=axes1)
fig.colorbar(subplot2, ax=axes2)

fig.tight_layout()

plt.show()