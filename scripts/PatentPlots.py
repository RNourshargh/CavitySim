#from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac
import matplotlib.pyplot as plt
import numpy as np

def CavityTransmission(freq, Finesse, Lroundtrip,Tmax=1,):
    PhiRT = (freq*2*np.pi*Lroundtrip)/(3*10**8) 
    return Tmax/(1+(2*Finesse/np.pi)**2 *(np.sin(PhiRT/2))**2)


def PrepareTransmissionPlot(freq_doppler,fig, plotnumber, RoundtripLength, Finesse, Compensated=True, Cavity=True):      
    """Cavity Properties"""
    RoundtripLength #Round trip optical path length in metres
    Finesse         #Cavity Finesse

    """Generate frequency scan"""    
    FSR = (3*10**8)/RoundtripLength
    wavelength = (780*10**(-9))

    freq780 = round(3*10**8/wavelength)
    freq0 = round(freq780/FSR)*FSR
    freqEnd = freq0+3*FSR
    freqs = np.linspace(freq0, freqEnd, num = 10000)
    
    """Make function to rescale the X-axis"""
    def XaxisRescaler(xinput, offset=freq0+FSR, scalefactor=10**6):
        return (xinput-offset)/scalefactor

    
    """Generate Laser Frequencies and Pockels Cell Voltage"""
    print("Doppler frequency is:", freq_doppler/10**6,"MHz")

    """Pockels cell"""
    voltage = freq_doppler*2/FSR #This calculates the correct applied voltage in units of Vhalf wave to compensate for the doppler shift
    print("A Pockels cell voltage of:", voltage, "Vhwv will compensate for the doppler shift")  
    DeltaLroundtrip = (voltage/2)*wavelength # Half the shift is provided to each of the two polarisations
    DeltaFrequency = (voltage/2)*FSR

    #laser1
    laser1freq =freq0+FSR-freq_doppler
    laser1freqlist =np.array([laser1freq,laser1freq])
    laser1ampFree =np.array([0,1])
    

    #laser2
    laser2freq = freq0+2*FSR+freq_doppler
    laser2freqlist =np.array([laser2freq,laser2freq])
    laser2ampFree =np.array([0,1])
    #laser2ampTrans =np.array([0, CavityTransmission(laser2freq, Finesse, Lroundtrip = RoundtripLength-DeltaLroundtrip)])

    """Generate empty Cavity Tranmsission Data structures"""
    transmission = []
    transmissionP1 = []
    transmissionP2 = []
    
    """Generate axes and labels"""
    axes = fig.add_subplot(3, 1, plotnumber)
    TitleDopplerFrequency = freq_doppler/10**6
    if TitleDopplerFrequency - int(TitleDopplerFrequency) == 0:
        axes.set_title('Doppler Shift: {:.0f}MHz'.format(freq_doppler/10**6))
    else:
        axes.set_title('Doppler Shift: {:.1f}MHz'.format(freq_doppler/10**6))
    axes.set_ylabel('Transmitted Power (a.u.)')
    axes.set_xlabel('Relative Optical Frequency (MHz)')
    axes.set_xlim(XaxisRescaler(freq0+FSR/2), XaxisRescaler(freq0+5*FSR/2))
    
    """Plot Compensated Cavity"""
    if Cavity and Compensated :
        laser1ampTrans =np.array([0, CavityTransmission(laser1freq, Finesse, Lroundtrip = RoundtripLength+DeltaLroundtrip)])
        laser2ampTrans =np.array([0, CavityTransmission(laser2freq, Finesse, Lroundtrip = RoundtripLength-DeltaLroundtrip)])
        for freq in freqs:
            transmission.append(CavityTransmission(freq, Finesse, Lroundtrip=RoundtripLength))
            transmissionP1.append(CavityTransmission(freq, Finesse, Lroundtrip = RoundtripLength-DeltaLroundtrip))
            transmissionP2.append(CavityTransmission(freq, Finesse, Lroundtrip = RoundtripLength+DeltaLroundtrip))
        Polarisation1 = axes.plot(XaxisRescaler(freqs), transmissionP1, label = "Polarisation 1")
        Polarisation2 = axes.plot(XaxisRescaler(freqs), transmissionP2, label = "Polarisation 2")
        UncompensatedTransmission = axes.plot(XaxisRescaler(freqs), transmission, "b", linestyle="dashed", label = "Uncompensated")
        Raman1 = axes.plot(XaxisRescaler(laser1freqlist),laser1ampTrans, "r", label='Raman 1')
        Raman2 = axes.plot(XaxisRescaler(laser2freqlist),laser2ampTrans, "m", label='Raman 2')
        handles,labels = axes.get_legend_handles_labels()
        handles = [handles[3], handles[4], handles[0], handles[1], handles[2]]
        labels = [labels[3], labels[4],labels[0], labels[1], labels[2]]
        
    
    """Plot Uncompensated Cavity"""
    if Cavity and Compensated == False:
        laser1ampTrans =np.array([0, CavityTransmission(laser1freq, Finesse, Lroundtrip = RoundtripLength)])
        laser2ampTrans =np.array([0, CavityTransmission(laser2freq, Finesse, Lroundtrip = RoundtripLength)])
        for freq in freqs:
            transmission.append(CavityTransmission(freq, Finesse, Lroundtrip=RoundtripLength))
        UncompensatedTransmission = axes.plot(XaxisRescaler(freqs), transmission, "b", label="Cavity Transmission")
        Raman1 = axes.plot(XaxisRescaler(laser1freqlist),laser1ampTrans, "r", label='Raman 1')
        Raman2 = axes.plot(XaxisRescaler(laser2freqlist),laser2ampTrans, "m", label='Raman 2')
        handles,labels = axes.get_legend_handles_labels()
        handles = [handles[1], handles[2], handles[0]]
        labels = [labels[1], labels[2], labels[0]]


        """Plot Free Space"""    
    
    
    """Plot Free space"""
    if Cavity == False and Compensated == False:
        for freq in freqs:
            transmission.append(CavityTransmission(freq, Finesse, Lroundtrip=RoundtripLength))
        UncompensatedTransmission = axes.plot(XaxisRescaler(freqs), transmission, "b", linestyle="dashed", label="Uncompensated")
        Raman1 = axes.plot(XaxisRescaler(laser1freqlist),laser1ampFree, "r", label='Raman 1')
        Raman2 = axes.plot(XaxisRescaler(laser2freqlist),laser2ampFree, "m", label='Raman 2')
        handles,labels = axes.get_legend_handles_labels()
        handles = [handles[1], handles[2], handles[0]]
        labels = [labels[1], labels[2], labels[0]]
    
    axes.legend(handles, labels, loc="upper right")    
    return freq0, FSR


"""Generates a figure and 3 subplots for compensated or uncompensated doppler shifts"""
def FigureAssembler(Title, Compensated = True, Cavity = True, RoundtripLength=5, DopplerShift=10*10**6, Finesse=30, save=False, show=True):
    fig = plt.figure(figsize=(10.0, 9.0))
    fig.suptitle(Title)
    #subplot1, freq0, FSR = 
    PrepareTransmissionPlot(0, plotnumber=1, RoundtripLength=RoundtripLength, Compensated=Compensated, Cavity=Cavity, fig=fig, Finesse=Finesse)
    PrepareTransmissionPlot(1*DopplerShift, plotnumber=2,RoundtripLength=RoundtripLength, Compensated=Compensated, Cavity=Cavity, fig=fig,Finesse=Finesse)
    PrepareTransmissionPlot(2*DopplerShift, plotnumber=3,RoundtripLength=RoundtripLength,Compensated=Compensated, Cavity=Cavity, fig=fig,Finesse=Finesse)
    fig.tight_layout()
    fig.subplots_adjust(top=0.92)
    
    if save:
        plt.savefig('plots/{}.png'.format(Title))
        plt.savefig('plots/{}.pdf'.format(Title))
        plt.savefig('plots/{}.eps'.format(Title))
    if show:
        plt.show()
    return fig



"""Variables to adjust settings in a serries of plots"""    
plottingFinesse =20
plottingDoppler = 2.5*10**6
plottingRoundTripLength = 5 #round trip length used to generate the plots. Measured in metres
saveplots = True
showplots = True
    
figure1 = FigureAssembler(Title='Compensated Doppler Shift', Compensated = True, Cavity = True, RoundtripLength = plottingRoundTripLength, DopplerShift = plottingDoppler, Finesse = plottingFinesse, save=saveplots, show = showplots)
figure2 = FigureAssembler(Title='Uncompensated Doppler Shift', Compensated = False, Cavity = True, RoundtripLength = plottingRoundTripLength, DopplerShift = plottingDoppler, Finesse = plottingFinesse, save=saveplots, show = showplots)
figure3 = FigureAssembler(Title='Free space Doppler Shift', Compensated = False, Cavity = False, RoundtripLength = plottingRoundTripLength, DopplerShift = plottingDoppler, Finesse = plottingFinesse, save=saveplots, show = showplots)