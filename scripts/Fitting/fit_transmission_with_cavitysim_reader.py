import os.path

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

from cavitysim.io import read_octascope_output

TEST_DATA_FILE = "TestScope.csv"
FSR = 300e6

# this uses seaborn's defaults rather than matplotlib's, see e.g.
# https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()

raw = read_octascope_output(os.path.join(os.path.dirname(__file__), TEST_DATA_FILE))
data = raw["data"]
time = data.index


transmission = data["CH1"].values
peaks, _ = find_peaks(transmission, height= 0.005, prominence=1e-2)

timeFSR = time[peaks[1]] - time[peaks[0]]
scanfrequency = (time - time[peaks[0]]) * FSR / timeFSR

def function_cavity_transmission(freq, Lroundtrip, Finesse, Tmax=1, T0=0):
    """
    Returns the amplitude for a given input frequency and cavity parameters
    Inputs:
    frequency
    Finesse
    Round trip path length
    """
    PhiRT = (freq * 2 * np.pi * Lroundtrip) / (3 * 10**8)

    return (
        Tmax
        / (1 + (2 * Finesse / np.pi)**2 * (np.sin(PhiRT / 2))**2)
        + T0
    )

popt, pcov = curve_fit(
    function_cavity_transmission, scanfrequency, transmission, p0=[1, 50, 1e-2, 0]
    )

fig = plt.figure(figsize=(10.0, 7.0))
ax = fig.add_subplot(1, 1, 1)

ax.set_title('Transmission Spectra')
ax.set_ylabel('Power')
ax.set_xlabel('Frequency (Hz)')
ax.plot(scanfrequency, transmission, label="transmission")
ax.plot(
    scanfrequency[peaks],
    transmission[peaks],
    "x",
    markersize=15,
    label="peaks"
)
fit_label = "fit (parameter values = {})".format(
    ", ".join(["{:.4f}".format(v) for v in popt])
)
ax.plot(
    scanfrequency,
    function_cavity_transmission(scanfrequency, *popt),
    label=fit_label
)
ax.legend(loc="upper center")

# plt.savefig('../plots/{}.png'.format(Title))
# plt.savefig('../plots/{}.pdf'.format(Title))
# plt.savefig('../plots/{}.eps'.format(Title))
plt.show()


fig = plt.figure(figsize=(10.0, 7.0))
ax = fig.add_subplot(1, 1, 1)

# seaborn dataframes have to be 'long' i.e. have one row per value
seaborn_df = data.stack("Channel")
seaborn_df.name = "value"
seaborn_df = seaborn_df.reset_index()

sns.lineplot(
    data=seaborn_df,
    x="Time",
    y="value",
    hue="Channel",
    ax=ax,
)

plt.show()
