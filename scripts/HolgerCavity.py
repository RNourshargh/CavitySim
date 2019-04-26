from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

#Generate lists for the lengths to be scanned
path1 = np.linspace(0.39, 0.42, num = 10)


#Generate results arrays of the correct size 
ad = 5*np.ones(len(path1))
end_radii =  10*np.ones(len(path1))

for i, l1 in enumerate(path1):
    cavity_elements = [
        MirrorNormal(5),
        PathConstantIndex(l1), #standard length 0.40756
        MirrorNormal()
    ]
    CavityIteration = Cavity(cavity_elements,True)
    ad[i] = CavityIteration.ad()
    end_radii[i] = CavityIteration.end_radius()

print(ad)
print(end_radii)
#ad = ad[ :-1]
#end_radii = end_radii[ :-1]


"""Generates single plot Radius"""
fig = plt.figure(figsize=(10.0, 7.0))
axes1 = fig.add_subplot(1, 1, 1)
axes1.set_title('Large Beam radius against optic spacings L1')
axes1.set_ylabel('End Radii (metres)')
axes1.set_xlabel('L1: Cavity Length (metres)')
subplot1=axes1.plot(path1, end_radii)
fig.tight_layout()
plt.show()


"""Generates double plot, Radius and stability"""
fig = plt.figure(figsize=(7.0, 7.0))
axes1 = fig.add_subplot(2, 1, 1)
axes1.set_title('A+D')
axes1.set_ylabel('A+D')
axes1.set_xlabel('L1: Cavity Length (metres)')
subplot1=axes1.plot(path1,ad)

axes2 = fig.add_subplot(2, 1, 2)
axes2.set_title('Large Beam radius against optic spacings L1')
axes2.set_ylabel('A+D parameter')
axes2.set_xlabel('L1: Cavity Length (metres)')
subplot2=axes2.plot(path1,end_radii)

fig.tight_layout()
plt.show()