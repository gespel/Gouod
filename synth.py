import math
import numpy as np

class Synth:
    phase: np.float32 = 0.0
    sample: np.float32 = 0.0
    freq: np.float32 = 600.0
    samplerate: np.float32 = 48000.0

    def __init__(self):
        pass
    def getSample(self):
        pass
    def getSynthName(self):
        pass
    def setFrequency(self, input: float):
        pass

class SineSynth(Synth):
    def getSample(self) -> np.float32:
        self.phase += ((self.freq) / self.samplerate) * 2.0 * 3.14159265
        return np.float32(np.sin(self.phase))
    def getSynthName(self):
        return "SineSynth"
    def setFrequency(self, input: np.float32):
        self.freq = input
    def getBuffer(self):
        sampleslist = []
        for i in range(0,1023):
            
            sampleslist.append(self.getSample())
            #x.setFrequency(abs(y.getSample())*1000)
        
        samples = np.array(sampleslist).astype(np.float32)
        return samples