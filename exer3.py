import pyaudio
import numpy as np
import pylab
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time
import sys
import seaborn as sns
from core import fft, dft

i=0
f,ax = plt.subplots(2)

x = np.arange(10000)
y = np.random.randn(10000)

li, = ax[0].plot(x, y)
ax[0].set_xlim(0,1000)
ax[0].set_ylim(-10000,10000)
ax[0].set_title("Raw Audio Signal")

li2, = ax[1].plot(x, y)
ax[1].set_xlim(0,4000)
ax[1].set_ylim(0,100)
ax[1].set_title("Fast Fourier Transform")

plt.pause(0.01)
plt.tight_layout()

FORMAT = pyaudio.paInt16 # We use 16bit format per sample
CHANNELS = 1
RATE = 44100
CHUNK = 1024 # 1024bytes of data red from a buffer
RECORD_SECONDS = 0.1

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True)#,
                    #frames_per_buffer=CHUNK)

global keep_going
keep_going = True

def plot_data(in_data):
    
    # Fs = 256.0  # sampling rate
    y = np.fromstring(in_data, np.int16)

    n = len(y)

    y = y.tolist()
    Y = dft(y)

    Y = Y[:n/2]
    Y = [abs(aux) for aux in Y]

    li.set_xdata(np.arange(len(y)))
    li.set_ydata(y)
    li2.set_xdata(np.arange(RATE))
    li2.set_ydata(Y)

    # Show the updated plot, but without blocking
    plt.pause(0.01)
    if keep_going:
        return True
    else:
        return False

# Open the connection and start streaming the data
stream.start_stream()
print "\n+---------------------------------+"
print "| Press Ctrl+C to Break Recording |"
print "+---------------------------------+\n"

# Loop so program doesn't end while the stream callback's
# itself for new data
while keep_going:
    try:
        plot_data(stream.read(CHUNK))
    except KeyboardInterrupt:
        keep_going=False
    except:
        pass

# Close up shop (currently not used because KeyboardInterrupt
# is the only way to close)
stream.stop_stream()
stream.close()

audio.terminate()