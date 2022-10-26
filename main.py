import pyaudio
import math
import numpy as np
from synth import SineSynth, Synth

p = pyaudio.PyAudio()

x: Synth = SineSynth()
y: Synth = SineSynth()
y.setFrequency(1200)
sampleslist = []
#np.array([])
# generate samples, note conversion to float32 array
#samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)


stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=48000,
                output=True,
                frames_per_buffer=1024)

while(True):
    samples = np.array([])
   
    samples = x.getBuffer()
    samples += y.getBuffer()
    samples *= 0.2
    stream.write(samples.tobytes())

stream.stop_stream()
stream.close()

p.terminate()