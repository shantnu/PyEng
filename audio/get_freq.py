import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

frame_rate = 48000.0
infile = "test.wav"
num_samples = 48000

wav_file = wave.open(infile, 'r')
data = wav_file.readframes(num_samples)
wav_file.close()

data = struct.unpack('{n}h'.format(n=num_samples), data)
data = np.array(data)

data_fft = np.fft.fft(data)

# This will give us the graph we want
a = np.abs(data_fft[:len(data_fft)/2])
x = range(num_samples/2)
plt.plot(x,a)
plt.xlim(0,1200)
print("The frequency is {} Hz".format(np.argmax(a)))
#Out[72]: 1000

plt.show()
plt.plot(x,a)