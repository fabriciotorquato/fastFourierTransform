import math
import pyaudio
import numpy as np


def iexp(n):
    return complex(math.cos(n), math.sin(n))


def is_pow2(n):
    return False if n == 0 else (n == 1 or is_pow2(n >> 1))


def dft(xs):
    "naive dft"
    n = len(xs)
    return [sum((xs[k] * iexp(-2 * math.pi * i * k / n) for k in range(n)))
            for i in range(n)]



def fft_(xs, n, start=0, stride=1):
    "cooley-turkey fft"
    if n == 1:
        return [xs[start]]
    hn, sd = n // 2, stride * 2
    rs = fft_(xs, hn, start, sd) + fft_(xs, hn, start + stride, sd)
    for i in range(hn):
        e = iexp(-2 * math.pi * i / n)
        rs[i], rs[i + hn] = rs[i] + e * rs[i + hn], rs[i] - e * rs[i + hn]
        pass
    return rs


def fft(xs):
    assert is_pow2(len(xs))
    return fft_(xs, len(xs))


def generate():
    p = pyaudio.PyAudio()

    volume = 0.5     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 1.0   # in seconds, may be float
    f = 440.0        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == "__main__":
    wave = [0, 1, 2, 3, 3, 2, 1, 0]
    dfreq = dft(wave)
    ffreq = fft(wave)
    # dwave = dftinv(dfreq)
    # fwave= fftinv(ffreq)
    print "DFT"
    print(dfreq)
    print
    print "FFT"
    print(ffreq)
