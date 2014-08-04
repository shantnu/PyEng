#! /usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

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
frequencies = np.abs(data_fft[:len(data_fft)])

plt.plot(frequencies)
plt.xlim(0,1200)
print("The frequency is {} Hz".format(np.argmax(frequencies)))

plt.show()