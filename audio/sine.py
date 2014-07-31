import numpy as np
import wave
import struct
#import pylab.plot as plt
import pdb

# Explain why ap of 16000 chpsen- for 16 bits, 32767 is max, so 16000 is half of that

def create_sine_wave(frequency = 1000, num_samples = 40000, frame_rate = 48000.0, amplitude = 16000, file = "test.wav"):
    
    sine_wave = [np.sin(2 * np.pi * frequency * x/frame_rate) for x in range(num_samples)]

    nframes=num_samples
    comptype="NONE"
    compname="not compressed"
    nchannels=1
    sampwidth=2

    wav_file=wave.open(file, 'w')    
    wav_file.setparams((nchannels, sampwidth, int(frame_rate), nframes, comptype, compname))
    
    for s in sine_wave:
        wav_file.writeframes(struct.pack('h', int(s*amplitude)))

    wav_file.close()

def get_frequency(frame_rate = 48000.0,  infile = "test.wav", num_samples = 40000):
    wav_file = wave.open(infile, 'r')
    data = wav_file.readframes(num_samples)
    wav_file.close()
    
    data = struct.unpack('{n}h'.format(n=num_samples), data)
    data = np.array(data)

    data_fft = np.fft.fft(data)
    frequencies_spread = np.fft.fftfreq(len(data_fft))

    idx = np.argmax(np.abs(data_fft))
    frequency = frequencies_spread[idx]
    frequency_in_hertz = frequency * frame_rate
    print "The frequency found is {}".format(frequency_in_hertz)


create_sine_wave()

#get_frequency()  

