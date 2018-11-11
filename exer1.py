from plot import plot_grapher
import numpy as np

Fs = 256.0  # sampling rate
Ts = 1.0/Fs  # sampling interval
t = np.arange(0, 1, Ts)  # time vector

if __name__ == "__main__":

    # Exercicio 1:
    # - A
    y = np.sin(2*np.pi*40*t)
    plot_grapher(y,t,Fs,False)

    # Exercicio 1:
    # - B
    y = np.sin(2*np.pi*40*t)
    plot_grapher(y,t,Fs)

    # Exercicio 1:
    # - C
    y = np.sin(2*np.pi*30*t)
    plot_grapher(y,t,Fs)

    y = np.sin(2*np.pi*50*t)
    plot_grapher(y,t,Fs)

    y = np.sin(2*np.pi*60*t)
    plot_grapher(y,t,Fs)
