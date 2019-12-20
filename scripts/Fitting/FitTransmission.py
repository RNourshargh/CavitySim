import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks

# THe cavity length and scope time scaling have both been fudged. There isn't actually any fitting happening yet

def import_octascope_csv(filepath,skipLines=0,headerSize=15):
    
    settings = {}
    settings_start = 0  # Line numbers for settings
    settings_end = headerSize
    f = open(filepath)
    for i, line in enumerate(f.readlines()):
        if i in range(settings_start, settings_end + 1):
            line = line.strip('\n').split(',')
            settings[line[0]] = line[1:]        
    timeRes = np.array(settings['"HResolution"           ']).astype(float)
    blockSize = np.array(settings['"BlockSize"             ']).astype(int)
    voltageOffset = np.array(settings['"HOffset"               ']).astype(float)
    noChannels = len(timeRes)
    
    ScopeData = np.loadtxt(filepath,delimiter=',',skiprows=headerSize+skipLines,usecols=list(np.arange(0,1+noChannels)))
    #    data = np.zeros((blockSize[0],2,noChannels))
    # for i in range(noChannels):
        # data[:,0,i] = np.arange(0,blockSize[i]*timeRes[i],timeRes[i])
        # if noChannels == 1:
            # data[:,1,i] = ScopeData[:]-voltageOffset[i]
        # else:
            # data[:,1,i] = ScopeData[:,i]-voltageOffset[i]
                
    #            np.save(path+'data'+file[:-4], data)
    return ScopeData

def function_cavity_transmission(freq, Lroundtrip, Finesse, Tmax=1, T0=0):
    """
    Returns the amplitude for a given input frequency and cavity parameters
    Inputs:
    frequency
    Finesse
    Round trip path length
    """
    PhiRT = (freq*2*np.pi*Lroundtrip)/(3*10**8) 
    return Tmax/(1+(2*Finesse/np.pi)**2 *(np.sin(PhiRT/2))**2)+T0

FSR = 300e6
    
ScopeData = import_octascope_csv("TestScope.csv")
time = ScopeData[:,0]
Transmission = ScopeData[:,1]
peaks, _ = find_peaks(Transmission, height= 0.005, prominence=1e-2)

timeFSR = time[peaks[1]]-time[peaks[0]]


scanfrequency = (time-time[peaks[0]])*FSR/timeFSR

popt, pcov = curve_fit(function_cavity_transmission, scanfrequency, Transmission, p0=[1,50,1e-2,0])

print(popt)

Title = Transmission

fig = plt.figure(figsize=(10.0, 7.0))
axes1 = fig.add_subplot(1, 1, 1)
axes1.set_title('Transmission Spectra')
axes1.set_ylabel('Power')
axes1.set_xlabel('Frequency Hz')
axes1.plot(scanfrequency,Transmission)
axes1.plot(scanfrequency[peaks],Transmission[peaks], "x")
axes1.plot(scanfrequency,function_cavity_transmission(scanfrequency,*popt))

#g = f'hello {variable}'
plt.savefig('../plots/{}.png'.format(Title))
plt.savefig('../plots/{}.pdf'.format(Title))
plt.savefig('../plots/{}.eps'.format(Title))
plt.show()


#print(ScopeData)
#print(type(ScopeData))





# def fit_gaussian_test():
    # InitialFitParameters = np.array([50,(0.12+0.1625+0.4)*2,1e-2,0])
    
    # ydata = gaussian(xdata,*testparameters) #Generate an ideal gaussian
    # noisy_ydata = ydata + np.sqrt(ydata)*(np.random.random(xdata.size)-0.5) #Add noise to the y_gaussian to better simulate real data
    # try:
        # popt, pcov = curve_fit(gaussian, xdata, noisy_ydata, p0=InitialFitParameters) #Fit a gaussian to the noisy test data
        # perr = np.sqrt(np.diag(pcov)) #Compute the 1 stddev errors on the fit parameters
    # except:
        # print("Failure to fit")
    # plt.plot(xdata,ydata,xdata,noisy_ydata,xdata,gaussian(xdata,*popt))
    # plt.show()
    # print(popt)