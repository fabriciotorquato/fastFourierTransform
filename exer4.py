import sys
import numpy as np
from plot_realtime import *
import matplotlib.pyplot as plt

i=0
f,ax = plt.subplots(3)

x = np.arange(10000)
y = np.random.randn(10000)

li, = ax[0].plot(x, y)
ax[0].set_xlim(0,4000)
ax[0].set_ylim(-60000,60000)
ax[0].set_title("Raw Audio Signal")

li2, = ax[1].plot(x, y)
ax[1].set_xlim(0,4000)
ax[1].set_ylim(0,100000)
ax[1].set_title("Fast Fourier Transform")

li3, = ax[2].plot(x, y)
ax[2].set_xlim(0,4000)
ax[2].set_ylim(0,100000)
ax[2].set_title("Spectrogram Signal")

plt.pause(0.1)
plt.tight_layout()

def plotSomething():
    
    if SR.newAudio==False: 
        return

    xs,ys=SR.fft()

    li.set_xdata(np.arange(len(SR.audio.flatten())))
    li.set_ydata(SR.audio.flatten())
    li2.set_xdata(xs)
    li2.set_ydata(ys)
    plt.subplot(3, 1, 3)
    Pxx, freqs, bins, im = plt.specgram(ys, NFFT=2048, Fs=4096, noverlap=10)
    li3.set_xdata(bins)
    li3.set_ydata(freqs)
    plt.pause(0.1)

    SR.newAudio=False

if __name__ == "__main__":
    
    SR=SwhRecorder()
    SR.setup()
    SR.continuousStart()

    while True:
        plotSomething()

    SR.close()