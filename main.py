import pyaudio
import math
import numpy as np
from synth import SineSynth, Synth, SquareSynth
from module import *

p = pyaudio.PyAudio()

d: Module = StrangeOne()

sampleslist = []

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=48000,
                output=True,
                frames_per_buffer=1024)

while True:
    samples = np.array([])
    sampleslist = []
    for i in range(0, 1023):
        sampleslist.append(d.get_sample())

    samples = np.array(sampleslist).astype(np.float32)
    samples *= 0.5

    stream.write(samples.tobytes())
