import pyaudio
import math
import numpy as np
from synth import SineSynth, Synth

p = pyaudio.PyAudio()

x: Synth = SineSynth()
y: Synth = SineSynth()
z: Synth = SineSynth()
v: Synth = SineSynth()

y.setFrequency(6)
z.setFrequency(2)
v.setFrequency(100)
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
    sampleslist = []
    for i in range(0,1023):    
        sampleslist.append(x.getSample())
        x.setFrequency(abs(y.getSample())*440)
        y.setFrequency(abs(z.getSample())*2)
        
    samples = np.array(sampleslist).astype(np.float32)
    #samples *= v.getSample()
    samples *= 0.5
   
    #samples = x.getBuffer()
    #samples += y.getBuffer()
    #samples *= 0.2
    stream.write(samples.tobytes())

stream.stop_stream()
stream.close()

p.terminate()