import numpy as np
import matplotlib.pyplot as plt
from cavitysim.utils import PE_Lossless_Mirror_Coefficients, PE_Lossy_Round_Trip_Coefficients, PE_Intensity_Enhancement_LosslessMirror, PE_finesse


"""User Inputs:"""
Numloops = 1000
Routput = 0.99
InternalIntensityLossRT =0.06
InputReflectances = np.linspace(0.92, 1.0, Numloops)
#print(InputReflectances)



IntensityEnhancement = np.zeros(Numloops)           #Initialise output arrays
Finesse = np.zeros(Numloops)

for n, InputReflectance in enumerate(InputReflectances): #Loop over input reflectances and calculate cavity enhancement
    IntensityEnhancement[n] = PE_Intensity_Enhancement_LosslessMirror(InputReflectance, Routput, InternalIntensityLossRT)
    Finesse[n] = PE_finesse(InputReflectance,Routput, InternalIntensityLossRT)
    

    
maxEnhancement = np.amax(IntensityEnhancement)          #Finds the highest value for intensity enhancement
minEnhancement = np.amin(IntensityEnhancement)          #Finds the lowest value for the benefit of plotting
print("Maximum power enhancement is:", maxEnhancement)  

maxEnhancementLocation = np.nanargmax(IntensityEnhancement)     #Finds the index corresponding to the maximum value of intensity emhancement
maxEnhancementFinesse = Finesse[maxEnhancementLocation]         #Finds the finesse at the reflectance giving maximum power enhancement
maxEnhancementReflectance = InputReflectances[maxEnhancementLocation] #Finds the reflectance corresponding to maximum enhancement
print("Maximum enhancement Finesse is :", maxEnhancementFinesse)
print("Optimum input reflectance for power enhancement:", maxEnhancementReflectance)
    

"""Generates plot for fixed round trip loss"""
fig = plt.figure(figsize=(10.0, 7.0))
axes1 = fig.add_subplot(2, 1, 1)
axes1.set_title('Circulating Intensity Enhancement: Internal Loss {}'.format(InternalIntensityLossRT))
axes1.set_ylabel('Intensity Enhancment Ratio')
axes1.set_xlabel('Input Mirror Power Reflectance')
axes1.plot(InputReflectances,IntensityEnhancement)
axes1.plot([maxEnhancementReflectance,maxEnhancementReflectance],[minEnhancement,maxEnhancement], "r")


axes2 = fig.add_subplot(2, 1, 2)
axes2.set_title('Finesse against Input reflectance: Internal Loss {}'.format(InternalIntensityLossRT))
axes2.set_ylabel('Finesse')
axes2.set_xlabel('Input mirror Power Reflectance')
axes2.plot(InputReflectances,Finesse)
axes2.plot([maxEnhancementReflectance,maxEnhancementReflectance],[np.amin(Finesse),maxEnhancementFinesse], "r")
fig.tight_layout()
plt.show()