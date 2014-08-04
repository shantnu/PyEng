#! /usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# frequency is the number of times a wave repeats a second
frequency = 1000
noisy_freq = 50
num_samples = 48000

# The sampling rate of the analog to digital convert
sampling_rate = 48000.0

#Create the sine wave and noise
sine_wave = [np.sin(2 * np.pi * frequency * x1 / sampling_rate) for x1 in range(num_samples)]

sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/  sampling_rate) for x1 in range(num_samples)]


#Convert them to numpy arrays
sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)

# Add them to create a noisy signal
combined_signal = sine_wave + sine_noise

x1 = range(num_samples)
'''
plt.subplot(3,1,1)
plt.title("Original sine wave")

# Need to add empty space, else everything looks scrunched up!
plt.subplots_adjust(hspace=.5)
plt.plot(x1[:500], sine_wave[:500])

plt.subplot(3,1,2)
plt.title("Noisy wave")
plt.plot(x1[:4000], sine_noise[:4000])

plt.subplot(3,1,3)
plt.title("Original + Noise")
plt.plot(x1[:3000], combined_signal[:3000])

plt.show()
'''

data_fft = np.fft.fft(combined_signal)

freq = (np.abs(data_fft[:len(data_fft)]))

x2 = np.arange(num_samples)
'''
plt.plot(x2, freq)
plt.xlim(0,1200)


plt.show()
'''
filtered_freq = []
index = 0
for f in freq:
    # Choosing 950, as closest to 1000. In real world, won't get exact numbers like these
    if index > 950 and index < 1050:
        # Has a real value. I'm choosing >1, as many values are like 0.000000001 etc
        if f > 1:
            filtered_freq.append(f)

        else:
            filtered_freq.append(0)
    else:
        filtered_freq.append(0)
    index += 1
'''
plt.plot(x2, filtered_freq)
plt.xlim(0,1200)
plt.show()
'''
recovered_signal = np.fft.ifft(filtered_freq)

print(len(recovered_signal), recovered_signal[:8])
plt.subplot(3,1,1)
plt.title("Original sine wave")
# Need to add empty space, else everything looks scrunched up!
plt.subplots_adjust(hspace=.5)

plt.plot(x1[:500], sine_wave[:500])

plt.subplot(3,1,2)
plt.title("Sine wave after clean up")
plt.plot((recovered_signal[:500]))

plt.show()


