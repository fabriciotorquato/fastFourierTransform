import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
from core import fft, dft

Fs = 256.0  # sampling rate
Ts = 1.0/Fs  # sampling interval
t = np.arange(0, 1, Ts)  # time vector


def plot_grapher(y, isFFT=True):

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


if __name__ == "__main__":

    # Exercicio 1:
    # - A
    y = np.sin(2*np.pi*40*t)
    plot_grapher(y,False)
    # Exercicio 1:
    # - B
    y = np.sin(2*np.pi*40*t)
    plot_grapher(y)

    # Exercicio 1:
    # - C
    y = np.sin(2*np.pi*30*t)
    plot_grapher(y)

    y = np.sin(2*np.pi*50*t)
    plot_grapher(y)

    y = np.sin(2*np.pi*60*t)
    plot_grapher(y)

    # Exercicio 2:
    y = 1*np.sin(2*np.pi*30*t) + 3*np.sin(2*np.pi*50*t) + \
        2*np.sin(2*np.pi*60*t)
    plot_grapher(y)
