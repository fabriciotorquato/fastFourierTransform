from plot import plot_grapher
import numpy as np

Fs = 256.0  # sampling rate
Ts = 1.0/Fs  # sampling interval
t = np.arange(0, 1, Ts)  # time vector

if __name__ == "__main__":
    # Exercicio 2:
    y = 1*np.sin(2*np.pi*30*t) + 3*np.sin(2*np.pi*50*t) + \
        2*np.sin(2*np.pi*60*t)
    plot_grapher(y,t,Fs)
