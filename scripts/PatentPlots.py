#from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import matplotlib.pyplot as plt
import numpy as np

def CavityTransmission(freq, Finesse=100, Lroundtrip=1,Tmax=1,):
    PhiRT = (freq*2*np.pi*Lroundtrip)/(3*10**8) 
    return Tmax/(1+(2*F/np.pi)**2 *(np.sin(PhiRT/2))**2)


"""Cavity Properties"""
RoundtripLength =1 #Round trip optical path length in metres
F = 20              #Cavity Finesse

"""Generate frequency scan"""    
FSR = (3*10**8)/RoundtripLength
wavelength = (780*10**(-9))

freq780 = round(3*10**8/wavelength)
freq0 = round(freq780/FSR)*FSR
freqEnd = freq0+3*FSR
freqs = np.linspace(freq0, freqEnd, num = 10000)


"""Pockels cell"""
voltage = 0.2 #this should be set to fractions of a wavelength such that volatge = 0.5 is the application of a halfwave voltage to the crystal, THis code is for single pass    
DeltaLroundtrip = (voltage/2)*wavelength # Half the shift is provided to each of the two polarisations
DeltaFrequency = (voltage/2)*FSR


"""Generate Cavity Tranmsission Data"""
transmission = []
transmissionP1 = []
transmissionP2 = []
for freq in freqs:
    transmission.append(CavityTransmission(freq, Finesse=F, Lroundtrip=RoundtripLength))
    transmissionP1.append(CavityTransmission(freq, Finesse=F, Lroundtrip = RoundtripLength-DeltaLroundtrip))
    transmissionP2.append(CavityTransmission(freq, Finesse=F, Lroundtrip = RoundtripLength+DeltaLroundtrip))
    

#print(freqs[np.argmax(transmission)])


"""Generate Laser Frequencies"""
freq_doppler = FSR/21
laserfreqs = [freq0+FSR-freq_doppler,freq0+2*FSR+freq_doppler]  

#laser1
laser1freq =freq0+FSR-freq_doppler
laser1freqlist =[laser1freq,laser1freq]
laser1ampFree =[0,1]
laser1ampTrans =[0, CavityTransmission(laser1freq, Finesse=F, Lroundtrip = RoundtripLength+DeltaLroundtrip)]

#laser2
laser2freq = freq0+2*FSR+freq_doppler
laser2freqlist =[laser2freq,laser2freq]
laser2ampFree =[0,1]
laser2ampTrans =[0, CavityTransmission(laser2freq, Finesse=F, Lroundtrip = RoundtripLength-DeltaLroundtrip)]




 
"""Generates single plot cavity transmission"""
fig = plt.figure(figsize=(10.0, 7.0))
axes1 = fig.add_subplot(1, 1, 1)
axes1.set_title('Transmitted Power against frequency')
axes1.set_ylabel('Transmitted Power (a.u.)')
axes1.set_xlabel('Optical Frequency')
axes1.set_xlim(freq0+FSR/2, freq0+5*FSR/2) 
subplot1=axes1.plot(freqs, transmission, linestyle="dashed")
#subplot1=axes1.plot(freqs, transmissionP1)
#subplot1=axes1.plot(freqs, transmissionP2)
#subplot1=axes1.plot(laser1freqlist,laser1ampTrans)
#subplot1=axes1.plot(laser2freqlist,laser2ampTrans)
subplot1=axes1.plot(laser1freqlist,laser1ampFree)
subplot1=axes1.plot(laser2freqlist,laser2ampFree)

fig.tight_layout()
plt.show()
#[freq0+2.2e8,freq0+2.2e8], [0,1] )[0,CavityTransmission(freq0+2.2e8, Finesse=F, Lroundtrip=RoundtripLength)]