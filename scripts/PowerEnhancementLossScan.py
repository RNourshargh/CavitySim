import numpy as np
import matplotlib.pyplot as plt
from cavitysim.utils import PE_Lossless_Mirror_Coefficients, PE_Lossy_Round_Trip_Coefficients, PE_Intensity_Enhancement_LosslessMirror, PE_finesse


"""User Inputs:"""
InputReflectances = np.linspace(0.92,0.97,6)

Routput = 0.99
Numloops = 1000
InternalIntensityLossRT =np.linspace(0.04, 0.15, Numloops)



for InputReflectance in InputReflectances:
    IntensityEnhancement = np.zeros(Numloops)           #Initialise output arrays
    Finesse = np.zeros(Numloops)

    for n, Loss in enumerate(InternalIntensityLossRT): #Loop over input reflectances and calculate cavity enhancement
        IntensityEnhancement[n] = PE_Intensity_Enhancement_LosslessMirror(InputReflectance, Routput, Loss)
        Finesse[n] = PE_finesse(InputReflectance,Routput, Loss)
        

        
    #maxEnhancement = np.amax(IntensityEnhancement)          #Finds the highest value for intensity enhancement
    #minEnhancement = np.amin(IntensityEnhancement)          #Finds the lowest value for the benefit of plotting
    #print("Maximum power enhancement is:", maxEnhancement)  
    #maxEnhancementLocation = np.nanargmax(IntensityEnhancement)     #Finds the index corresponding to the maximum value of intensity emhancement
    #maxEnhancementFinesse = Finesse[maxEnhancementLocation]         #Finds the finesse at the reflectance giving maximum power enhancement
    #maxEnhancementReflectance = InputReflectances[maxEnhancementLocation] #Finds the reflectance corresponding to maximum enhancement
    #print("Maximum enhancement Finesse is :", maxEnhancementFinesse)
    #print("Optimum input reflectance for power enhancement:", maxEnhancementReflectance)
        

    """Generates plot for fixed round trip loss"""
    fig = plt.figure(figsize=(10.0, 7.0))
    axes1 = fig.add_subplot(2, 1, 1)
    axes1.set_title('Circulating Intensity Enhancement: InputReflectance {:.2f}'.format(InputReflectance))
    axes1.set_ylabel('Intensity Enhancment Ratio')
    axes1.set_xlabel('Internal Round trip loss')
    axes1.plot(InternalIntensityLossRT,IntensityEnhancement)
    #axes1.plot([maxEnhancementReflectance,maxEnhancementReflectance],[minEnhancement,maxEnhancement], "r")


    axes2 = fig.add_subplot(2, 1, 2)
    axes2.set_title('Finesse against Input reflectance: InputReflectance {:.2f}'.format(InputReflectance))
    axes2.set_ylabel('Finesse')
    axes2.set_xlabel('Internal Round trip loss')
    axes2.plot(InternalIntensityLossRT,Finesse)
    #axes2.plot([maxEnhancementReflectance,maxEnhancementReflectance],[np.amin(Finesse),maxEnhancementFinesse], "r")
    fig.tight_layout()
    
plt.show()