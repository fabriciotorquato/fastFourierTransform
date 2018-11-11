import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
from core import fft, dft


def plot_grapher(y, t, Fs, isFFT=True):

    n = len(y)  # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T  # two sides frequency range
    frq = frq[range(n/2)]  # one side frequency range

    y = y.tolist()
    if isFFT:
        Y = fft(y)
    else:
        Y = dft(y)
    # Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[:n/2]
    Y = [abs(aux) for aux in Y]

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t, y)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.subplot(212)
    plt.plot(frq, Y, 'r')  # plotting the spectrum
    plt.xlabel('Freq (Hz)')
    plt.ylabel('|Y(freq)|')
    plt.show()
