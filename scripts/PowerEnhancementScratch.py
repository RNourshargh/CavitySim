import numpy as np
import matplotlib.pyplot as plt
from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac


def PE_Lossless_Mirror_Coefficients(Int_Reflectance):
    amp_reflectance = np.sqrt(Int_Reflectance)
    Int_Transmission = 1-Int_Reflectance
    amp_transmission = np.sqrt(Int_Transmission)
    return Int_Reflectance, amp_reflectance, Int_Transmission, amp_transmission
    
def PE_Lossy_Round_Trip_Coefficients(Int_Absorbtion):
    amp_absorbtion = np.sqrt(Int_Absorbtion)
    Int_Transmission = 1-Int_Absorbtion
    amp_transmission = np.sqrt(Int_Transmission)
    return Int_Absorbtion, amp_absorbtion, Int_Transmission, amp_transmission
    
def PE_Intensity_Enhancement_LosslessMirror(Rin, Rout, Art):
    Rin, rin, Tin, tin = PE_Lossless_Mirror_Coefficients(Rin)
    Rout, rout, Tout, tout = PE_Lossless_Mirror_Coefficients(Rout)
    I_Abs, amp_abs, I_Trans, amp_trans = PE_Lossy_Round_Trip_Coefficients(Art)
    Intensity_Enhancement_Ratio = tin**2/(1-rin*rout*amp_trans)**2
    
    #totalloss1= 1-Rin*Rout*I_Trans
    #totalloss2= 1-Rin +1-Rout +Art
    return Intensity_Enhancement_Ratio#, totalloss1, totalloss2
    
def PE_finesse(Rin,Rout, Art):
    Total_RT_loss = (1-Rin) + (1-Rout) +Art
    finesse = 2*np.pi/(Total_RT_loss)
    return finesse
    
    
    
"""User Inputs:"""
Numloops = 1000
Routput = 0.995
InternalIntensityLossRT =0.03
InputReflectances = np.linspace(0.8, 0.99, Numloops)
#print(InputReflectances)



IntensityEnhancement = np.zeros(Numloops)           #Initialise output arrays
Finesse = np.zeros(Numloops)

for n, InputReflectance in enumerate(InputReflectances): #Loop over input reflectances and calculate cavity enhancement
    IntensityEnhancement[n] = PE_Intensity_Enhancement_LosslessMirror(InputReflectance, Routput, InternalIntensityLossRT)
    Finesse[n] = PE_finesse(InputReflectance,Routput, InternalIntensityLossRT)
    

    
maxEnhancement = np.amax(IntensityEnhancement)
minEnhancement = np.amin(IntensityEnhancement)
print("Maximum power enhancement is:", maxEnhancement)

maxEnhancementLocation = np.nanargmax(IntensityEnhancement)
maxEnhancementFinesse = Finesse[maxEnhancementLocation]
maxEnhancementReflectance = InputReflectances[maxEnhancementLocation]
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
    
