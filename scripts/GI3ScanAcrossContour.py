from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

#Generate lists for the lengths to be scanned
path1 = 0.12
path2 = np.linspace(0.161, 0.166, num = 300)

#Generate results arrays of the correct size 
ad = 5*np.ones(len(path2))
end_radii =  10*np.ones(len(path2))


l1 = path1

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
	end_radii[j] = CavityIteration.end_radius()

	advalue = CavityIteration.ad()
	if -2<= advalue <= 2:
		ad[j] = CavityIteration.ad()
	else:
		ad[j] = np.NaN
	
# """Generates plot for a single length l1"""
# fig = plt.figure(figsize=(10.0, 7.0))
# axes1 = fig.add_subplot(1, 1, 1)
# axes1.set_title('Large Beam radius against telescope spacing L2')
# axes1.set_ylabel('Large Beam Radius (metres)')
# axes1.set_xlabel('L2: Telescope Spacing (metres)')
# subplot1=axes1.plot(path2,end_radii)
# fig.tight_layout()
# plt.show()


"""Generates plot for a single length l1"""
fig = plt.figure(figsize=(10.0, 10.0))
axes1 = fig.add_subplot(2, 1, 1)
axes1.set_title('Large Beam radius against telescope spacing L2')
axes1.set_ylabel('Large Beam Radius (metres)')
axes1.set_xlabel('L2: Telescope Spacing (metres)')
subplot1=axes1.plot(path2,end_radii)

axes2 = fig.add_subplot(2, 1, 2)
axes2.set_title('AD value against telescope spacing')
axes2.set_ylabel('AD value')
axes2.set_xlabel('L2: Telescope Spacing (metres)')
subplot2=axes2.plot(path2,ad)
fig.tight_layout()
plt.show()